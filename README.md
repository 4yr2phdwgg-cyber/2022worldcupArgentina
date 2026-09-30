
# Argentina 2022 World Cup — Football Event Data Analysis
# 阿根廷 2022 世界杯足球事件数据分析

## 1. Project Overview / 项目简介

This project analyzes Argentina's matches in the 2022 FIFA World Cup using StatsBomb event-level data. It focuses on data processing, passing analysis, shooting analysis, spatial analysis, and visualization.

本项目使用 StatsBomb 足球事件级数据，对阿根廷队在 2022 年 FIFA 世界杯中的比赛进行分析，重点包括数据处理、传球分析、射门分析、空间区域分析和数据可视化。

The goal is to transform raw JSON event data into structured datasets and meaningful analytical insights.

项目旨在将原始 JSON 事件数据转换为结构化数据集，并从中提取有意义的分析结果。

## 2. Data Source / 数据来源

- **Source / 数据来源:** StatsBomb Open Data
- **Format / 数据格式:** JSON
- **Data Types / 数据类型:** Passes, Shots, Carries, Pressures, and other match events
- **数据内容：** 传球、射门、带球、压迫及其他比赛事件

Raw data files are not included in this repository. Please obtain the data from the original source and follow its usage requirements.

本仓库不包含原始数据文件。请从原始数据来源获取数据，并遵守相应的使用要求。

## 3. Tech Stack / 技术栈

- Python
- Pandas
- NumPy
- Matplotlib
- JSON data processing
- Football event data analysis

## 4. Analysis / 分析内容

### 4.1 Passing Analysis / 传球分析

- Pass volume and completion
- Passing locations and passing maps
- Final-third passing analysis
- Cross analysis

- 传球次数与成功情况
- 传球位置及传球路线可视化
- 最后三区传球分析
- 传中分析

### 4.2 Shooting Analysis / 射门分析

- Shot locations
- Shot outcomes
- Expected Goals (xG), where available
- Shot maps

- 射门位置分析
- 射门结果分析
- 预期进球（xG）分析（在数据支持的情况下）
- 射门分布图

### 4.3 Spatial Analysis / 空间区域分析

The project examines the distribution of football events across different pitch areas.

本项目分析不同足球事件在球场各区域的分布情况。

### 4.4 Match Analysis / 比赛分析

The project explores passing and attacking patterns across selected matches.

本项目对选定比赛中的传球和进攻特征进行探索性分析。

## 5. Project Structure / 项目结构

```text
argentina_2022_world_cup/
├── README.md
├── src/
│   ├── load_data.py
│   ├── parse_events.py
│   ├── analysis.py
│   └── visualization.py
├── data/
│   └── README.md
├── figures/
│   ├── pass_maps/
│   ├── shot_maps/
│   └── charts/
└── outputs/
    ├── passing_summary.csv
    ├── shooting_summary.csv
    └── match_summary.csv
```

## 6. Key Learning Outcomes / 项目收获

Through this project, I practiced:

- Loading and processing nested JSON data
- Converting event data into structured Pandas DataFrames
- Data cleaning and feature extraction
- Data filtering, grouping, and aggregation
- Football passing and shooting analysis
- Spatial data visualization with Matplotlib
- Organizing a reproducible data analysis project

通过本项目，我练习了：

- 嵌套 JSON 数据的读取与处理
- 使用 Pandas 将事件数据转换为结构化 DataFrame
- 数据清洗与特征提取
- 数据筛选、分组与聚合
- 足球传球与射门分析
- 使用 Matplotlib 进行空间数据可视化
- 组织结构清晰、便于复现的数据分析项目

## 7. Future Improvements / 后续计划

- Player-level performance comparison / 球员表现对比
- Possession sequence analysis / 控球进攻序列分析
- More advanced passing metrics / 更深入的传球指标分析
- Team tactical analysis / 球队战术分析
- SQL-based football data analysis / 使用 SQL 进行足球数据分析
- Interactive dashboards / 交互式数据看板

## 8. Key Findings | 关键发现

### 8.1 Strong Overall Passing Efficiency | 整体传球效率较高

Across the seven matches, Argentina recorded **4,615 passes**, including **3,939 successful passes**, corresponding to an overall pass completion rate of approximately **85.4%**.

在 7 场比赛中，阿根廷共完成 **4,615 次传球**，其中 **3,939 次成功传球**，整体传球成功率约为 **85.4%**。

In the final third, Argentina completed **1,002 passes**, of which **780 were successful**, giving a completion rate of approximately **77.8%**.

在进攻三区，阿根廷共完成 **1,002 次传球**，其中 **780 次成功**，传球成功率约为 **77.8%**。

The lower completion rate in the final third suggests that passing became more difficult in advanced attacking areas, where space and defensive pressure were more constrained.

相比整体区域，进攻三区的传球成功率有所下降，说明随着进攻推进到更靠近对方球门的区域，传球处理难度有所增加。


### 8.2 Most Key Passes Occurred in the Final Third | 大部分关键传球发生在进攻三区

Argentina recorded **65 key passes** across the seven matches, with **59 occurring in the final third**, accounting for approximately **90.8%** of all key passes.

7 场比赛中，阿根廷共完成 **65 次关键传球**，其中 **59 次发生在进攻三区**，约占全部关键传球的 **90.8%**。

This indicates that most passes directly associated with creating shooting opportunities were generated in advanced attacking areas.

这说明阿根廷大部分与创造射门机会直接相关的关键传球，都发生在靠近对方球门的进攻区域。


### 8.3 The Left Attacking Channel Was Frequently Used | 左路进攻三区使用频率较高

Across the seven matches, Argentina recorded:

- **476 passes on the left**
- **398 passes on the right**
- **373 passes through the middle**

在 7 场比赛中，阿根廷在进攻三区的传球分布为：

- **左路：476 次**
- **右路：398 次**
- **中路：373 次**

The left side accounted for approximately **38.2%** of the recorded final-third passes, making it the most frequently used of the three areas.

左路传球约占进攻三区传球的 **38.2%**，是三个区域中使用频率最高的区域。

The left attacking channel was also the most frequently used final-third area in **5 of the 7 matches**.

从单场比赛来看，左路在 **7 场比赛中的 5 场**都是进攻三区传球次数最多的区域。


### 8.4 Shooting and xG | 射门与 xG

Across the seven matches, Argentina recorded:

- **101 shots**
- **49 shots on target**
- **15 goals**
- **13.94 total xG**

7 场比赛累计数据为：

- **101 次射门**
- **49 次射正**
- **15 个进球**
- **13.94 总 xG**

The shot-on-target rate was approximately **48.5%**, while the actual number of goals was slightly higher than the aggregated xG value.

射正率约为 **48.5%**，实际进球数 **15 球**略高于累计 xG **13.94**。

The shot data shows that Argentina consistently generated shooting opportunities during the tournament, with many shots occurring in and around the opponent's penalty area.

从射门数据来看，阿根廷在整个赛事中持续创造射门机会，且较多射门发生在对方禁区及禁区附近区域。

> **Note:** The xG result is based on the available event data and the calculation method used in this project. It should not be interpreted as a newly trained xG prediction model.
>
> **说明：**本项目中的 xG 结果基于可获得的比赛事件数据以及项目中的计算方法，并不代表重新训练得到的独立 xG 预测模型。


### 8.5 Crosses Were Concentrated on the Flanks | 横传主要集中在左右两侧

Argentina recorded **227 crosses**, including **122 successful crosses**, corresponding to an overall completion rate of approximately **53.7%**.

阿根廷共完成 **227 次横传**，其中 **122 次成功**，整体横传成功率约为 **53.7%**。

The distribution of crosses was:

- **Left: 97**
- **Right: 86**
- **Middle: 44**

横传区域分布为：

- **左路：97 次**
- **右路：86 次**
- **中路：44 次**

The left side recorded the highest number of crosses, which is consistent with the relatively high frequency of final-third passing observed on the left side.

左路横传次数最高，与进攻三区左路传球次数较高的结果基本一致。


### 8.6 Final-Third Passing Varied Across Matches | 不同比赛之间进攻三区传球表现存在差异

The Poland match recorded the highest final-third passing volume, with:

- **311 final-third passes**
- **260 successful passes**
- **83.6% completion rate**
- **2 assists**

对阵波兰的比赛中，阿根廷进攻三区传球数量最高：

- **311 次进攻三区传球**
- **260 次成功传球**
- **83.6% 成功率**
- **2 次助攻**

In contrast, the Argentina vs. Saudi Arabia match recorded **161 final-third passes**, with a completion rate of approximately **61.5%**.

相比之下，阿根廷对阵沙特阿拉伯的比赛完成 **161 次进攻三区传球**，成功率约为 **61.5%**。

This shows that Argentina's final-third passing volume and efficiency varied across different matches rather than remaining constant throughout the tournament.

这说明阿根廷在不同比赛中的进攻三区传球数量和效率存在一定差异，并不是整个赛事都保持相同水平。


### 8.7 Spatial Distribution of Shots and Passes | 射门与传球的空间分布

The shot and pass maps provide a spatial view of Argentina's attacking behavior.

Shot events are mainly concentrated around the opponent's penalty area, while passing events cover a much larger area of the attacking half.

Shot/Pass Map 从空间角度展示了阿根廷的进攻行为。

从可视化结果来看，射门事件主要集中在对方禁区及禁区前沿，而传球事件则覆盖了更大范围的进攻半场。

The visualizations complement the numerical analysis by showing not only how many events occurred, but also where those events took place.

这种可视化与前面的数值分析形成互补，不仅能够观察事件数量，还能够进一步观察这些事件在球场上的空间位置。


## 9. Overall Summary | 总结

Overall, the analysis of Argentina's seven matches shows several notable patterns:

综合 7 场比赛的数据分析，可以观察到以下几个主要特征：

- **High overall passing efficiency**  
  **整体传球成功率较高**

- **Lower passing efficiency in the final third compared with overall passing**  
  **进攻三区传球成功率低于整体传球成功率**

- **A large proportion of key passes occurred in the final third**  
  **大部分关键传球发生在进攻三区**

- **The left attacking channel was frequently used**  
  **左路进攻三区使用频率较高**

- **Shooting events were concentrated around the opponent's penalty area**  
  **射门事件主要集中在对方禁区及附近区域**

- **Crosses were mainly distributed on the left and right attacking sides**  
  **横传主要分布在左右两侧**

- **Passing volume and efficiency varied across different matches**  
  **不同比赛之间的传球数量和效率存在差异**

By combining event-level statistics with spatial visualization, this project provides both quantitative and spatial perspectives on Argentina's attacking behavior during the 2022 FIFA World Cup.

通过将**事件级数据统计**与**球场空间可视化**结合，本项目从数量和空间两个维度分析了阿根廷队在 2022 FIFA 世界杯中的进攻行为。

## 10. Author / 作者

This is a personal learning project focused on Python, Pandas, and football data analysis, with the long-term goal of developing skills in football analytics.

这是一个个人学习与实践项目，主要围绕 Python、Pandas 和足球数据分析展开，长期目标是进一步学习足球数据分析。
