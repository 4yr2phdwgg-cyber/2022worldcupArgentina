import json
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
import seaborn as sns

root=r"C:\Users\李小鹏\Desktop\python脚本\项目\open-data-master\data"
filepath1=os.path.join(root,"competitions.json")
with open(filepath1,"r",encoding="utf-8")as f:
    com=json.load(f)
for item in com:
    com_name=item["competition_name"]
    season_name=item["season_name"]
    if com_name=="FIFA World Cup" and season_name=="2022":
        com_id=item["competition_id"]
        saa_id=item["season_id"]
        print(com_id,saa_id)

root1=r"C:\Users\李小鹏\Desktop\python脚本\项目\open-data-master\data\matches"
filepath02=os.path.join(root1,str(com_id))
filepath2=os.path.join(filepath02,f"{str(saa_id)}.json")
with open(filepath2,"r",encoding="utf-8")as f:
    match=json.load(f)
mat_ids=[]
match_sc=[]
for item in match:
    home=item["home_team"]["home_team_name"]
    away=item["away_team"]["away_team_name"]
    if home=="Argentina" or away=="Argentina":
        mid=item["match_id"]
        mat_ids.append(mid)
        match_sc.append({
            "match_id":mid,
            "home":home,
            "away":away,
            "score": f"{item['home_score']}:{item['away_score']}",
            "stage":item["competition_stage"]["name"]
        })
print(len(mat_ids))
events={}
root2=r"C:\Users\李小鹏\Desktop\python脚本\项目\open-data-master\data\events"
for mid in mat_ids:
    filepath3=os.path.join(root2,f"{mid}.json")
    with open(filepath3,"r",encoding="utf-8")as f:
        event=json.load(f)
        events[mid]=event

def parse_events_to_df(events_list, match_id):
    rows=[]
    for ev in events_list:
        # 基础字段
        row={
            'match_id':match_id,
            'period':ev.get('period'),
            'minute':ev.get('minute'),
            'second':ev.get('second'),
            'team':ev.get('team',{}).get('name'),
            'player':ev.get('player',{}).get('name'),
            'type':ev.get('type',{}).get('name'),
            'possession':ev.get('possession'),
            'possession_team':ev.get('possession_team',{}).get('name'),
            'location_x':ev.get('location',[None,None])[0],
            'location_y':ev.get('location',[None,None])[1],
        }
        # 传球细节
        pass_info=ev.get('pass',{})
        if pass_info:
            row['pass_outcome']=pass_info.get('outcome',{}).get('name')
            row['pass_recipient']=pass_info.get('recipient',{}).get('name')
            end_loc=pass_info.get('end_location',[None, None])
            row['pass_end_x']=end_loc[0]
            row['pass_end_y']=end_loc[1]
            row['pass_length']=pass_info.get('length')
            row['pass_cross']=pass_info.get('cross')
            row['pass_switch']=pass_info.get('switch')
            row['pass_goal_assist']=pass_info.get('goal_assist')  
            row['pass_shot_assist']=pass_info.get('shot_assist')     
            row['pass_type']=pass_info.get('type',{}).get('name') 
            row['pass_height']=pass_info.get('height',{}).get('name')
        # 射门细节
        shot_info=ev.get('shot',{})
        if shot_info:
            row['shot_outcome']=shot_info.get('outcome',{}).get('name')
            row['shot_xg']=shot_info.get('statsbomb_xg')
            row['shot_body_part']=shot_info.get('body_part',{}).get('name')
            row['shot_technique']=shot_info.get('technique',{}).get('name')
            end_loc=pass_info.get('end_location',[None,None])
            row['shot_end_x']=end_loc[0]
            row['shot_end_y']=end_loc[1]
        #盘带
        carry_info=ev.get('carry',{})
        if carry_info:
            end_loc=pass_info.get('end_location',[None, None])
            row['carry_end_x']=end_loc[0]
            row['carry_end_y']=end_loc[1]
        # 过人
        dribble_info=ev.get('dribble',{})
        if dribble_info:
            row['dribble_outcome']=dribble_info.get('outcome',{}).get('name')
        # 防守
        duel_info=ev.get('duel',{})
        if duel_info:
            row['duel_type']=duel_info.get('type',{}).get('name')
            row['duel_outcome']=duel_info.get('outcome',{}).get('name')
        
        clearance_info=ev.get('clearance',{})
        if clearance_info:
            row['clearance_body_part']=clearance_info.get('body_part',{}).get('name')
        
        interception_info=ev.get('interception',{})
        if interception_info:
            row['interception_outcome']=interception_info.get('outcome',{}).get('name')
        # 犯规与纪律
        foul_committed=ev.get('foul_committed',{})
        if foul_committed:
            row['foul_type']=foul_committed.get('type',{}).get('name')
            row['card']=foul_committed.get('card',{}).get('name')
        
        rows.append(row)
    
    return pd.DataFrame(rows)

# 合并所有比赛
all_dfs=[]
for mid,events_list in events.items():
    df=parse_events_to_df(events_list, mid)
    all_dfs.append(df)
 
df_all=pd.concat(all_dfs,ignore_index=True)
action_types=['Pass','Shot','Dribble','Ball Recovery','Duel', 
            'Clearance','Interception','Block','Foul Committed',
            'Pressure','Offside','Miscontrol','Carry']
df_clean=df_all[df_all['type'].isin(action_types)].copy()
#传向进攻三区的球
def analyze_final_third_passes(df_clean,team,xth,yth1,yth2,mid):
    # 筛选本队所有传球
    passes=df_clean[(df_clean['team']==team)&(df_clean['type']=='Pass')&(df_clean['match_id']==mid)]
    # 定义成功传球
    success_mask=(passes['pass_outcome'].isna() | 
                passes['pass_outcome'].str.contains('Complete', na=False))
    successful=passes[success_mask]
    # 进攻三区传球：终点 x 坐标 >= 阈值
    final_third=passes[passes['pass_end_x']>=xth]
    ft_counts=len(final_third)#进攻三区传球
    final_third_successful=successful[successful['pass_end_x']>=xth]
    fts_counts=len(final_third_successful)#进攻三区成功传球
    assists=passes[passes['pass_goal_assist']==True]
    ast_counts=len(assists)#助攻
    #右路进攻三区传球&助攻传球&形成射门的传球
    right_final_third=final_third[final_third['pass_end_y']<=yth1]
    rft_counts=len(right_final_third)#右边路进攻三区传球
    right_final_third_successful=final_third_successful[final_third_successful['pass_end_y']<=yth1]
    rfts_counts=len(right_final_third_successful)#右边路进攻三区成功传球
    r_assists=right_final_third[right_final_third['pass_goal_assist']==True]
    r_ast_counts=len(r_assists)#右边路助攻
    #中路进攻三区传球&助攻传球&形成射门的传球
    middle_final_third=final_third[(final_third['pass_end_y']<yth2)&(final_third['pass_end_y']>yth1)]
    mft_counts=len(middle_final_third)#中路进攻三区传球
    middle_final_third_successful=final_third_successful[(final_third_successful['pass_end_y']<yth2)&(final_third['pass_end_y']>yth1)]
    mfts_counts=len(middle_final_third_successful)#中路进攻三区传球
    m_assists=middle_final_third[middle_final_third['pass_goal_assist']==True]
    m_ast_counts=len(m_assists)#中路助攻
    #左路进攻三区传球&助攻传球&形成射门的传球
    left_final_third=final_third[final_third['pass_end_y']>=yth2]
    lft_counts=len(left_final_third)#左边路进攻三区传球
    left_final_third_successful=final_third_successful[final_third_successful['pass_end_y']>=yth2]
    lfts_counts=len(left_final_third_successful)#左边路进攻三区成功传球
    l_assists=left_final_third[left_final_third['pass_goal_assist']==True]
    l_ast_counts=len(l_assists)#左边路助攻
    result={'match_id':mid,
        'ft_counts':ft_counts,
        'fts_counts':fts_counts,
        'ast_counts':ast_counts,
        'rft_counts':rft_counts,
        'rfts_counts':rfts_counts,
        'r_ast_counts':r_ast_counts,
        'mft_counts':mft_counts,
        'mfts_counts':mfts_counts,
        'm_ast_counts':m_ast_counts,
        'lft_counts':lft_counts,
        'lfts_counts':lfts_counts,
        'l_ast_counts':l_ast_counts}
    return result
match_final_third_passes=[]
for mid in mat_ids:
    passes=df_clean[(df_clean['type']=='Pass')&(df_clean['match_id']==mid)]
    k=passes[passes['pass_type']=='Kick Off']
    xth=(k.iloc[0]['location_x'])*4/3
    yth1=(k.iloc[0]['location_y'])*2/3
    yth2=(k.iloc[0]['location_y'])*4/3
    a=analyze_final_third_passes(df_clean,'Argentina',xth,yth1,yth2,mid)
    match_final_third_passes.append(a)
re=pd.DataFrame(match_final_third_passes)#进攻三区传球左中右按比赛id
re1=re.drop(['match_id'],axis=1).sum()#进攻三区传球左中右
print(re)
#左中右
def analyze_rlm_passes(df_clean,team,xth,yth1,yth2,mid):
    # 筛选本队所有传球
    passes=df_clean[(df_clean['team']==team)&(df_clean['type']=='Pass')&(df_clean['match_id']==mid)]
    # 定义成功传球
    success_mask=(passes['pass_outcome'].isna() | 
                passes['pass_outcome'].str.contains('Complete', na=False))
    successful=passes[success_mask]
    assists=passes[passes['pass_goal_assist']==True]
    key_passes=passes[passes['pass_shot_assist']==True]
    p_counts=len(passes)
    ps_counts=len(successful)
    spre=len(successful)/len(passes)*100
    a_counts=len(assists)#助攻
    k_counts=len(key_passes)#关键传球
    #进攻三区
    final_third=passes[passes['location_x']>=xth]
    final_third_successful=successful[successful['location_x']>=xth]
    final_third_assists=final_third[final_third['pass_goal_assist']==True]
    final_third_key_passes=final_third[final_third['pass_shot_assist']==True]
    ftp_counts=len(final_third)#进攻三区传球
    ftps_counts=len(final_third_successful)#进攻三区成功传球
    ftspre=ftps_counts/ftp_counts*100
    fta_counts=len(final_third_assists)#进攻三区助攻
    ftk_counts=len(final_third_key_passes)#进攻三区关键传球
    #右路
    right=passes[passes['location_y']<=yth1]
    right_successful=successful[successful['location_y']<=yth1]
    r_assists=right[right['pass_goal_assist']==True]
    r_key=right[right['pass_shot_assist']==True]
    rp_counts=len(right)#右边路传球
    rps_counts=len(right_successful)#右边路成功传球
    rspre=rps_counts/rp_counts*100
    r_a_counts=len(r_assists)#右边路助攻
    r_k_counts=len(r_key)
    #中路
    middle=passes[(passes['location_y']<yth2)&(passes['location_y']>yth1)]
    middle_successful=successful[(successful['location_y']<yth2)&(successful['location_y']>yth1)]
    m_assists=middle[middle['pass_goal_assist']==True]
    m_key=middle[middle['pass_shot_assist']==True]
    mp_counts=len(middle)#中路传球
    mps_counts=len(middle_successful)#中路成功传球
    mspre=mps_counts/mp_counts*100
    m_a_counts=len(m_assists)#中路助攻
    m_k_counts=len(m_key)
    #左路
    left=passes[passes['location_y']>=yth2]
    left_successful=successful[successful['location_y']>=yth2]
    l_assists=left[left['pass_goal_assist']==True]
    l_key=left[left['pass_shot_assist']==True]
    lp_counts=len(left)#左边路传球
    lps_counts=len(left_successful)#左边路成功传球
    lspre=lps_counts/lp_counts*100
    l_a_counts=len(l_assists)#左边路助攻
    l_k_counts=len(l_key)
    res={'match_id':mid,
        'all pass':p_counts,
         'all successful pass':ps_counts,
         'all successful precent':spre,
         'all assist':a_counts,
         'all key pass':k_counts,
         'final third pass':ftp_counts,
         'final third successful pass':ftps_counts,
         'final third successful precent':ftspre,
         'final third assist':fta_counts,
         'final third key pass':ftk_counts,
         'right pass':rp_counts,
         'right successful pass':rps_counts,
         'right successful precent':rspre,
         'right assist':r_a_counts,
         'right key pass':r_k_counts,
         'middle pass':mp_counts,
         'middle successful pass':mps_counts,
         'middle successful precent':mspre,
         'middle assist':m_a_counts,
         'middle key pass':m_k_counts,
         'left pass':lp_counts,
         'left successful pass':lps_counts,
         'left successful precent':lspre,
         'left assist':l_a_counts,
         'left key pass':l_k_counts}
    return res
match_passes=[]
for mid in mat_ids:
    passes=df_clean[(df_clean['type']=='Pass')&(df_clean['match_id']==mid)]
    k=passes[passes['pass_type']=='Kick Off']
    xth=(k.iloc[0]['location_x'])*4/3
    yth1=(k.iloc[0]['location_y'])*2/3
    yth2=(k.iloc[0]['location_y'])*4/3
    a=analyze_rlm_passes(df_clean,'Argentina',xth,yth1,yth2,mid)
    match_passes.append(a)
res=pd.DataFrame(match_passes)
res1={'where':['all','final third','right','middle','left'],
      'pass':[res['all pass'].sum(),res['final third pass'].sum(),res['right pass'].sum(),res['middle pass'].sum(),res['left pass'].sum()],
      'successful pass':[res['all successful pass'].sum(),res['final third successful pass'].sum(),res['right successful pass'].sum(),res['middle successful pass'].sum(),res['left successful pass'].sum()],
      'successful precent':[res['all successful precent'].mean(),res['final third successful precent'].mean(),res['right successful precent'].mean(),res['middle successful precent'].mean(),res['left successful precent'].mean()],
      'assist':[res['all assist'].sum(),res['final third assist'].sum(),res['right assist'].sum(),res['middle assist'].sum(),res['left assist'].sum()],
      'key pass':[res['all key pass'].sum(),res['final third key pass'].sum(),res['right key pass'].sum(),res['middle key pass'].sum(),res['left key pass'].sum()]}
qq=pd.DataFrame(res1)
print(qq)
#shotassist goalassist shot xg
def analyze_rlm_shot(df_clean,team,xth,yth1,yth2,mid):
    # 筛选本队所有传球
    passes=df_clean[(df_clean['team']==team)&(df_clean['type']=='Pass')&(df_clean['match_id']==mid)]
    shots=df_clean[(df_clean['team']==team)&(df_clean['type']=='Shot')&(df_clean['match_id']==mid)&(df_clean['period']<=4)]
    shot_on_target=shots[shots['shot_outcome'].isin(['Saved','Goal','Post'])]
    goals=shot_on_target[shot_on_target['shot_outcome']=='Goal']
    # 定义成功传球
    success_mask=(passes['pass_outcome'].isna() | 
                passes['pass_outcome'].str.contains('Complete', na=False))
    successful=passes[success_mask]
    assists=passes[passes['pass_goal_assist']==True]
    key_passes=passes[passes['pass_shot_assist']==True]
    p_counts=len(passes)
    ps_counts=len(successful)
    spre=len(successful)/len(passes)*100
    a_counts=len(assists)#助攻
    k_counts=len(key_passes)#关键传球
    s_counts=len(shots)#射门
    sont_counts=len(shot_on_target)#射正
    g_counts=len(goals)#进球
    axg=shots['shot_xg'].sum()#xg
    #进攻三区
    final_third=passes[passes['location_x']>=xth]
    final_third_successful=successful[successful['location_x']>=xth]
    final_third_assists=final_third[final_third['pass_goal_assist']==True]
    final_third_key_passes=final_third[final_third['pass_shot_assist']==True]
    final_third_shot=shots[shots['location_x']>=xth]
    final_third_shot_on_target=final_third_shot[final_third_shot['shot_outcome'].isin(['Saved','Goal','Post'])]
    final_third_goal=final_third_shot_on_target[final_third_shot_on_target['shot_outcome']=='Goal']
    final_third_xg=final_third_shot['shot_xg'].sum()
    ftp_counts=len(final_third)#进攻三区传球
    ftps_counts=len(final_third_successful)#进攻三区成功传球
    ftspre=ftps_counts/ftp_counts*100
    fta_counts=len(final_third_assists)#进攻三区助攻
    ftk_counts=len(final_third_key_passes)#进攻三区关键传球
    fts_counts=len(final_third_shot)
    ftsot_counts=len(final_third_shot_on_target)
    ftg_counts=len(final_third_goal)
    #右路
    right=passes[passes['location_y']<=yth1]
    right_successful=successful[successful['location_y']<=yth1]
    r_assists=right[right['pass_goal_assist']==True]
    r_key=right[right['pass_shot_assist']==True]
    r_shot=shots[shots['location_y']<=yth1]
    r_shoton=r_shot[r_shot['shot_outcome'].isin(['Saved','Goal','Post'])]
    r_goal=r_shoton[r_shoton['shot_outcome']=='Goal']
    r_xg=r_shot['shot_xg'].sum()
    rp_counts=len(right)#右边路传球
    rps_counts=len(right_successful)#右边路成功传球
    rspre=rps_counts/rp_counts*100
    r_a_counts=len(r_assists)#右边路助攻
    r_k_counts=len(r_key)
    rs_counts=len(r_shot)
    rsog_counts=len(r_shoton)
    rg_counts=len(r_goal)
    #中路
    middle=passes[(passes['location_y']<yth2)&(passes['location_y']>yth1)]
    middle_successful=successful[(successful['location_y']<yth2)&(successful['location_y']>yth1)]
    m_assists=middle[middle['pass_goal_assist']==True]
    m_key=middle[middle['pass_shot_assist']==True]
    m_shot=shots[(shots['location_y']<yth2)&(shots['location_y']>yth1)]
    m_shoton=m_shot[m_shot['shot_outcome'].isin(['Saved','Goal','Post'])]
    m_goal=m_shoton[m_shoton['shot_outcome']=='Goal']
    m_xg=m_shot['shot_xg'].sum()
    mp_counts=len(middle)#中路传球
    mps_counts=len(middle_successful)#中路成功传球
    mspre=mps_counts/mp_counts*100
    m_a_counts=len(m_assists)#中路助攻
    m_k_counts=len(m_key)
    ms_counts=len(m_shot)
    msog_counts=len(m_shoton)
    mg_counts=len(m_goal) 
    #左路
    left=passes[passes['location_y']>=yth2]
    left_successful=successful[successful['location_y']>=yth2]
    l_assists=left[left['pass_goal_assist']==True]
    l_key=left[left['pass_shot_assist']==True]
    l_shot=shots[shots['location_y']>=yth2]
    l_shoton=l_shot[l_shot['shot_outcome'].isin(['Saved','Goal','Post'])]
    l_goal=l_shoton[l_shoton['shot_outcome']=='Goal']
    l_xg=l_shot['shot_xg'].sum()
    lp_counts=len(left)#左边路传球
    lps_counts=len(left_successful)#左边路成功传球
    lspre=lps_counts/lp_counts*100
    l_a_counts=len(l_assists)#左边路助攻
    l_k_counts=len(l_key)
    ls_counts=len(l_shot)
    lsog_counts=len(l_shoton)
    lg_counts=len(l_goal) 
    res={'match_id':mid,
        'all pass':p_counts,
         'all successful pass':ps_counts,
         'all successful precent':spre,
         'all assist':a_counts,
         'all key pass':k_counts,
         'all shot':s_counts,
         'all shot on':sont_counts,
         'all goal':g_counts,
         'all xg':axg,
         'final third pass':ftp_counts,
         'final third successful pass':ftps_counts,
         'final third successful precent':ftspre,
         'final third assist':fta_counts,
         'final third key pass':ftk_counts,
         'final third shot':fts_counts,
         'final third shot on':ftsot_counts,
         'final third goal':ftg_counts,
         'final third xg':final_third_xg,
         'right pass':rp_counts,
         'right successful pass':rps_counts,
         'right successful precent':rspre,
         'right assist':r_a_counts,
         'right key pass':r_k_counts,
         'right shot':rs_counts,
         'right shot on':rsog_counts,
         'right goal':rg_counts,
         'right xg':r_xg,
         'middle pass':mp_counts,
         'middle successful pass':mps_counts,
         'middle successful precent':mspre,
         'middle assist':m_a_counts,
         'middle key pass':m_k_counts,
         'middle shot':ms_counts,
         'middle shot on':msog_counts,
         'middle goal':mg_counts,
         'middle xg':m_xg,
         'left pass':lp_counts,
         'left successful pass':lps_counts,
         'left successful precent':lspre,
         'left assist':l_a_counts,
         'left key pass':l_k_counts,
         'left shot':ls_counts,
         'left shot on':lsog_counts,
         'left goal':lg_counts,
         'left xg':l_xg}
    return res
match_shot=[]
for mid in mat_ids:
    passes=df_clean[(df_clean['type']=='Pass')&(df_clean['match_id']==mid)]
    k=passes[passes['pass_type']=='Kick Off']
    xth=(k.iloc[0]['location_x'])*4/3
    yth1=(k.iloc[0]['location_y'])*2/3
    yth2=(k.iloc[0]['location_y'])*4/3
    b=analyze_rlm_shot(df_clean,'Argentina',xth,yth1,yth2,mid)
    match_shot.append(b)
res=pd.DataFrame(match_shot)
res2={'where':['all','final third','right','middle','left'],
      'pass':[res['all pass'].sum(),res['final third pass'].sum(),res['right pass'].sum(),res['middle pass'].sum(),res['left pass'].sum()],
      'assist':[res['all assist'].sum(),res['final third assist'].sum(),res['right assist'].sum(),res['middle assist'].sum(),res['left assist'].sum()],
      'key pass':[res['all key pass'].sum(),res['final third key pass'].sum(),res['right key pass'].sum(),res['middle key pass'].sum(),res['left key pass'].sum()],
      'shot':[res['all shot'].sum(),res['final third shot'].sum(),res['right shot'].sum(),res['middle shot'].sum(),res['left shot'].sum()],
      'shot on target':[res['all shot on'].sum(),res['final third shot on'].sum(),res['right shot on'].sum(),res['middle shot on'].sum(),res['left shot on'].sum()],
      'goal':[res['all goal'].sum(),res['final third goal'].sum(),res['right goal'].sum(),res['middle goal'].sum(),res['left goal'].sum()],
      'xg':[res['all xg'].sum(),res['final third xg'].sum(),res['right xg'].sum(),res['middle xg'].sum(),res['left xg'].sum()]}
aa=pd.DataFrame(res2)
print(aa)
res3={'where':['all','right','middle','left'],
      'shot/pass':[(res['all shot'].sum()/res['all pass'].sum()),(res['right shot'].sum()/res['right pass'].sum()),(res['middle shot'].sum()/res['middle pass'].sum()),(res['left shot'].sum()/res['left pass'].sum())],
      'xg/pass':[(res['all xg'].sum()/res['all pass'].sum()),(res['right xg'].sum()/res['right pass'].sum()),(res['middle xg'].sum()/res['middle pass'].sum()),(res['left xg'].sum()/res['left pass'].sum())],
      'goal/pass':[(res['all goal'].sum()/res['all pass'].sum()),(res['right goal'].sum()/res['right pass'].sum()),(res['middle goal'].sum()/res['middle pass'].sum()),(res['left goal'].sum()/res['left pass'].sum())],}
bb=pd.DataFrame(res3)
print(bb)
def draw_pitch(ax,xth,yth):
    # 边线
    ax.plot([0, 0],[0, yth],'black',linewidth=2)
    ax.plot([0, xth],[yth, yth],'black',linewidth=2)
    ax.plot([xth, xth],[yth, 0],'black',linewidth=2)
    ax.plot([xth, 0],[0, 0],'black',linewidth=2)
    # 中线
    ax.plot([xth/2, xth/2],[0, yth],'black',linewidth=2)
    # 中圈
    circle=plt.Circle((xth/2, yth/2),10,color='black',fill=False,linewidth=2)
    ax.add_artist(circle)
    # 禁区（简化）
    yy=(yth-40.32)/2
    ax.plot([0, 16.5],[16.5, 16.5],'black')
    ax.plot([16.5, 16.5],[16.5, yy+40.32],'black')
    ax.plot([16.5, 0],[yy+40.32, yy+40.32],'black')
    ax.plot([xth, xth-16.5],[16.5, 16.5],'black')
    ax.plot([xth-16.5, xth-16.5],[16.5, yy+40.32],'black')
    ax.plot([xth-16.5, xth],[yy+40.32, yy+40.32],'black')

def shot_color(row):
        if row['shot_outcome']=='Goal':return'green'
        elif row['shot_outcome']in['Saved','Saved Off Line']:return'blue'
        else: return 'red'

for mid in mat_ids:
    passes=df_clean[(df_clean['type']=='Pass')&(df_clean['match_id']==mid)]
    k=passes[passes['pass_type']=='Kick Off']
    xt=(k.iloc[0]['location_x'])*2
    yt=(k.iloc[0]['location_y'])*2
    passes=df_clean[(df_clean['team']=='Argentina')&(df_clean['type']=='Pass')&(df_clean['match_id']==mid)]
    success_mask=(passes['pass_outcome'].isna() | 
            passes['pass_outcome'].str.contains('Complete',na=False))
    successful=passes[success_mask].dropna(subset=['location_x','location_y','pass_end_x','pass_end_y']) 
    shots=df_clean[(df_clean['team']=='Argentina')&(df_clean['type']=='Shot')&(df_clean['match_id']==mid)&(df_clean['period']<=4)].copy()
    shots=shots.dropna(subset=['location_x','location_y'])
    colors=shots.apply(shot_color,axis=1)
    xg=shots['shot_xg'].fillna(0.05)
    sizes=20+(xg/xg.max())*280
    fig, ax=plt.subplots(figsize=(14, 10))
    draw_pitch(ax,xt,yt)
    ax.scatter(shots['location_x'],yt-shots['location_y'],
            c=colors,s=sizes,alpha=0.7,edgecolors='black',linewidth=0.5)
    goals=shots[shots['shot_outcome']=='Goal']
    for _,goal in goals.iterrows():
       ax.text(goal['location_x'],80-goal['location_y'],'★',
            fontsize=14,color='gold',ha='center',va='center')
    legend_elements=[
        Patch(facecolor='green',label='Goal'),
        Patch(facecolor='blue',label='On target saved'),
        Patch(facecolor='red',label='Off target / Blocked')
        ]
    ax.legend(handles=legend_elements,loc='lower left')
    for _,row in successful.iterrows():
       x1=row['location_x']
       y1=yt-row['location_y']   
       x2=row['pass_end_x']
       y2=yt-row['pass_end_y']
    # 用透明度、细线，颜色代表成功传球，形成射门的传球，助攻（成功=蓝，形成射门的传球=金，助攻=红）
       if row.get('pass_goal_assist')==True:
         color='red'   
         alpha=0.8
       elif row.get('pass_shot_assist')==True:
         color='gold'      
         alpha=0.8  
       else:
          color='steelblue'
          alpha=0.15  
       ax.plot([x1,x2],[y1,y2],color=color,linewidth=0.8,alpha=alpha)
    ax.set_xlim(0,xt)
    ax.set_ylim(0,yt)  
    ax.set_aspect('equal')
    ax.set_title(f'Shot and Pass Map{mid}', fontsize=14)
    ax.axis('off')
    plt.tight_layout()
    out_dir=r'C:\Users\李小鹏\Desktop\python脚本\项目\shot_maps'
    os.makedirs(out_dir,exist_ok=True)
    save_path=os.path.join(out_dir,f'shot_pass_map_{mid}.png')
    plt.savefig(save_path,dpi=150,bbox_inches='tight')
def analyze_cross(df_clean,team,xth,yth1,yth2,mid):
    passes=df_clean[(df_clean['team']==team)&(df_clean['type']=='Pass')&(df_clean['match_id']==mid)]
    cross=passes[(passes['location_x']>=xth)&(passes['pass_height']=='High Pass')]
    cross_mask=(cross['pass_outcome'].isna() | 
                 cross['pass_outcome'].str.contains('Complete', na=False))
    successful_cross=cross[cross_mask]
    crosses=len(cross)
    s_crosses=len(successful_cross)
    ca=cross[cross['pass_goal_assist']==True]
    ck=cross[cross['pass_shot_assist']==True]
    cross_assist=len(ca)
    cross_key=len(ck)
    #左路
    left=cross[cross['location_y']>=yth2]
    s_left=successful_cross[successful_cross['location_y']>=yth2]
    lca=ca[ca['location_y']>=yth2]
    lck=ck[ck['location_y']>=yth2]
    leftc=len(left)
    leftsc=len(s_left)
    lcac=len(lca)
    lckc=len(lck)
    #中路
    middle=cross[(cross['location_y']<=yth2)&(cross['location_y']>=yth1)]
    s_middle=successful_cross[(cross['location_y']<=yth2)&(successful_cross['location_y']>=yth1)]
    mca=ca[(ca['location_y']<=yth2)&(ca['location_y']>=yth1)]
    mck=ck[(ck['location_y']<=yth2)&(ck['location_y']>=yth1)]
    middlec=len(middle)
    middlesc=len(s_middle)
    mcac=len(mca)
    mckc=len(mck)
    #右路
    right=cross[cross['location_y']<=yth1]
    s_right=successful_cross[successful_cross['location_y']<=yth1]
    rca=ca[ca['location_y']<=yth1]
    rck=ck[ck['location_y']<=yth1]
    rightc=len(right)
    rightsc=len(s_right)
    rcac=len(rca)
    rckc=len(rck)
    res={
        'match_id':mid,
        'cross':crosses,
        'successful cross':s_crosses,
        'cross assist':cross_assist,
        'cross key':cross_key,
        'left cross':leftc,
        'left s cross':leftsc,
        'left assist':lcac,
        'left key':lckc,
        'middle cross':middlec,
        'middle s cross':middlesc,
        'middle assist':mcac,
        'middle key':mckc,
        'right cross':rightc,
        'right s cross':rightsc,
        'right assist':rcac,
        'right key':rckc
    }
    return res
match_cross=[]
for mid in mat_ids:
    passes=df_clean[(df_clean['type']=='Pass')&(df_clean['match_id']==mid)]
    k=passes[passes['pass_type']=='Kick Off']
    yth1=(k.iloc[0]['location_y'])*2/3
    yth2=(k.iloc[0]['location_y'])*4/3
    xth=(k.iloc[0]['location_x'])
    c=analyze_cross(df_clean,'Argentina',xth,yth1,yth2,mid)
    match_cross.append(c)
res=pd.DataFrame(match_cross)
res4={'where':['all','right','middle','left'],
      'cross':[res['cross'].sum(),res['right cross'].sum(),res['middle cross'].sum(),res['left cross'].sum()],
      'assist':[res['cross assist'].sum(),res['right assist'].sum(),res['middle assist'].sum(),res['left assist'].sum()],
      'key pass':[res['cross key'].sum(),res['right key'].sum(),res['middle key'].sum(),res['left key'].sum()],
      'successful cross':[res['successful cross'].sum(),res['right s cross'].sum(),res['middle s cross'].sum(),res['left s cross'].sum()]}
zz=pd.DataFrame(res4)
print(zz)
    








