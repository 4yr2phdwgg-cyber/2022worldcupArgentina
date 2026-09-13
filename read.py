1#starting XI事件，首发11人
#data['type']['name']= "Starting XI",
{
  "id" : "0b483cd2-1d36-49a0-85c2-149a9de553df",#事件id
  "index" : 1,#该比赛中的事件编号
  "period" : 1,#上下半场（1上半场，2下半场）
  "timestamp" : "00:00:00.000",#发生事件点，minute，second将timestamp中的时间拆分
  "minute" : 0,
  "second" : 0,
  "type" : {#动作类型
    "id" : 35,
    "name" : "Starting XI"
  },
  "possession" : 1, #当前控球回合编号，连续控球逐渐增加
  "possession_team" : {#控球队伍
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "play_pattern" : {#比赛模式
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {#执行该动作的队伍，与possession team可能不同，如拦截，解围
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "duration" : 0.0,#持续时间
  "tactics" : {#战术
    "formation" : 433,#阵型
    "lineup" : [ {
      "player" : {
        "id" : 4637,
        "name" : "Ellie Roebuck"
      },
      "position" : {
        "id" : 1,
        "name" : "Goalkeeper"
      },
      "jersey_number" : 26
    }, {
      "player" : {
        "id" : 4649,
        "name" : "Esme Beth Morgan"
      },
      "position" : {
        "id" : 2,
        "name" : "Right Back"
      },
      "jersey_number" : 14
    }, {
      "player" : {
        "id" : 4648,
        "name" : "Abbie McManus"
      },
      "position" : {
        "id" : 3,
        "name" : "Right Center Back"
      },
      "jersey_number" : 23
    }, {
      "player" : {
        "id" : 17524,
        "name" : "Jennifer Patricia Beattie"
      },
      "position" : {
        "id" : 5,
        "name" : "Left Center Back"
      },
      "jersey_number" : 5
    }, {
      "player" : {
        "id" : 4651,
        "name" : "Demi Stokes"
      },
      "position" : {
        "id" : 6,
        "name" : "Left Back"
      },
      "jersey_number" : 3
    }, {
      "player" : {
        "id" : 10172,
        "name" : "Jill Scott"
      },
      "position" : {
        "id" : 13,
        "name" : "Right Center Midfield"
      },
      "jersey_number" : 8
    }, {
      "player" : {
        "id" : 4658,
        "name" : "Keira Walsh"
      },
      "position" : {
        "id" : 14,
        "name" : "Center Midfield"
      },
      "jersey_number" : 24
    }, {
      "player" : {
        "id" : 4645,
        "name" : "Isobel Mary Christiansen"
      },
      "position" : {
        "id" : 15,
        "name" : "Left Center Midfield"
      },
      "jersey_number" : 11
    }, {
      "player" : {
        "id" : 4654,
        "name" : "Nikita Parris"
      },
      "position" : {
        "id" : 17,
        "name" : "Right Wing"
      },
      "jersey_number" : 17
    }, {
      "player" : {
        "id" : 4635,
        "name" : "Julia Spetsmark"
      },
      "position" : {
        "id" : 21,
        "name" : "Left Wing"
      },
      "jersey_number" : 15
    }, {
      "player" : {
        "id" : 4650,
        "name" : "Nadia Nadim"
      },
      "position" : {
        "id" : 23,
        "name" : "Center Forward"
      },
      "jersey_number" : 10
    } ]
  }
}
2#half start事件，半场开始
#data['type']['name']="Half Start" 
{
  "id" : "040940a1-5972-431e-b6ac-e723edd8e7c2",
  "index" : 3,
  "period" : 1,
  "timestamp" : "00:00:00.000",
  "minute" : 0,
  "second" : 0,
  "type" : {
    "id" : 18,
    "name" : "Half Start"
  },
  "possession" : 1,
  "possession_team" : {
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "duration" : 7.96,
  "related_events" : [ "5ba286bd-c397-4ac4-b12f-6bace943afce" ]
}
3#pass事件，传球
#data['type']['name']="Pass"
{
  "id" : "2a456ec2-352c-499b-b5cc-e68bf84c7e9a",
  "index" : 5,
  "period" : 1,
  "timestamp" : "00:00:00.100",
  "minute" : 0,
  "second" : 0,
  "type" : {
    "id" : 30,
    "name" : "Pass"
  },
  "possession" : 2,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 9,
    "name" : "From Kick Off"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "player" : {
    "id" : 4647,
    "name" : "So-Yun Ji"
  },
  "position" : {
    "id" : 14,
    "name" : "Center Midfield"
  },
  "location" : [ 61.0, 40.0 ],#开始位置
  "duration" : 0.0,
  "related_events" : [ "483b7286-e75e-4191-80be-ac93bfed1473" ],
  "pass" : {
    "recipient" : {#接球人
      "id" : 4659,
      "name" : "Ramona Bachmann"
    },
    "length" : 3.6055512,#传球距离
    "angle" : -0.98279375,#传球角度
    "height" : {#高度
      "id" : 1,
      "name" : "Ground Pass"
    },
    "end_location" : [ 63.0, 37.0 ],#结束位置
    "body_part" : {#触球部位
      "id" : 40,
      "name" : "Right Foot"
    },
    "type" : {
      "id" : 65,
      "name" : "Kick Off"
    }
  }
}
4#ball receipt事件，接球
#data['type']['name']="Ball Receipt*"
{
  "id" : "483b7286-e75e-4191-80be-ac93bfed1473",
  "index" : 6,
  "period" : 1,
  "timestamp" : "00:00:00.100",
  "minute" : 0,
  "second" : 0,
  "type" : {
    "id" : 42,
    "name" : "Ball Receipt*"
  },
  "possession" : 2,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 9,
    "name" : "From Kick Off"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "player" : {
    "id" : 4659,
    "name" : "Ramona Bachmann"
  },
  "position" : {
    "id" : 24,
    "name" : "Left Center Forward"
  },
  "location" : [ 63.0, 37.0 ],#接球位置
  "related_events" : [ "2a456ec2-352c-499b-b5cc-e68bf84c7e9a" ]
}
5#carry事件，带球
#data['type']['name']="Carry"
{
  "id" : "7e908bd8-8e2f-44f8-9cc6-0435cd9ed3ed",
  "index" : 7,
  "period" : 1,
  "timestamp" : "00:00:00.100",
  "minute" : 0,
  "second" : 0,
  "type" : {
    "id" : 43,
    "name" : "Carry"
  },
  "possession" : 2,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 9,
    "name" : "From Kick Off"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "player" : {
    "id" : 4659,
    "name" : "Ramona Bachmann"
  },
  "position" : {
    "id" : 24,
    "name" : "Left Center Forward"
  },
  "location" : [ 63.0, 37.0 ],#开始位置
  "duration" : 0.4,
  "under_pressure" : true,#是否处于压迫下
  "related_events" : [ "22f23387-caec-4ddd-8b31-8f25608094c3", "38023613-6b26-44e2-a0f8-9aab9960d2ff", "483b7286-e75e-4191-80be-ac93bfed1473" ],
  "carry" : {
    "end_location" : [ 69.0, 33.0 ],#结束位置
  }
}
6#pressure事件，压迫
#data['type']['name']="Pressure"
{
  "id" : "22f23387-caec-4ddd-8b31-8f25608094c3",
  "index" : 8,
  "period" : 1,
  "timestamp" : "00:00:00.340",
  "minute" : 0,
  "second" : 0,
  "type" : {
    "id" : 17,
    "name" : "Pressure"
  },
  "possession" : 2,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 9,
    "name" : "From Kick Off"
  },
  "team" : {
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "player" : {
    "id" : 4658,
    "name" : "Keira Walsh"
  },
  "position" : {
    "id" : 14,
    "name" : "Center Midfield"
  },
  "location" : [ 47.0, 41.0 ],
  "duration" : 0.373,
  "related_events" : [ "38023613-6b26-44e2-a0f8-9aab9960d2ff", "7e908bd8-8e2f-44f8-9cc6-0435cd9ed3ed" ]
}
7#Miscontrol事件，失去控球权
#data['type']['name']="Miscontrol"
{
  "id" : "ccb57323-17d3-43db-8ae4-0d170c59c9cb",
  "index" : 13,
  "period" : 1,
  "timestamp" : "00:00:06.740",
  "minute" : 0,
  "second" : 6,
  "type" : {
    "id" : 38,
    "name" : "Miscontrol"
  },
  "possession" : 2,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 9,
    "name" : "From Kick Off"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "player" : {
    "id" : 5088,
    "name" : "Crystal Alyssia Dunn Soubrier"
  },
  "position" : {
    "id" : 16,
    "name" : "Left Midfield"
  },
  "location" : [ 108.0, 10.0 ]
}
8#block事件，封堵
#data['type']['name']="Block"
{
  "id" : "30cb10cd-5f73-472a-a0e0-a67f37e8eb83",
  "index" : 21,
  "period" : 1,
  "timestamp" : "00:00:29.780",
  "minute" : 0,
  "second" : 29,
  "type" : {
    "id" : 6,
    "name" : "Block"
  },
  "possession" : 3,
  "possession_team" : {
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "play_pattern" : {
    "id" : 7,
    "name" : "From Goal Kick"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "player" : {
    "id" : 5088,
    "name" : "Crystal Alyssia Dunn Soubrier"
  },
  "position" : {
    "id" : 16,
    "name" : "Left Midfield"
  },
  "location" : [ 78.0, 8.0 ],
  "related_events" : [ "7cc1c0c6-2c01-44d7-84dc-af3174363676" ]
}
9#ball recovery事件，夺回球权
#data['type']['name']="Ball Recovery"
{
  "id" : "a685120b-4ae5-4ac3-9cf0-96168f46837a",
  "index" : 31,
  "period" : 1,
  "timestamp" : "00:00:35.620",
  "minute" : 0,
  "second" : 35,
  "type" : {
    "id" : 2,
    "name" : "Ball Recovery"
  },
  "possession" : 4,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 6,
    "name" : "From Counter"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "player" : {
    "id" : 4657,
    "name" : "Anita Amma Ankyewah Asante"
  },
  "position" : {
    "id" : 4,
    "name" : "Center Back"
  },
  "location" : [ 37.0, 10.0 ]
}
10#dribbled past事件，被过
#data['type']['name']="Dribbled Past"
{
  "id" : "b959ca15-ef15-42df-a945-d25c7822c98e",
  "index" : 36,
  "period" : 1,
  "timestamp" : "00:00:42.220",
  "minute" : 0,
  "second" : 42,
  "type" : {
    "id" : 39,
    "name" : "Dribbled Past"
  },
  "possession" : 4,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 6,
    "name" : "From Counter"
  },
  "team" : {
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "player" : {
    "id" : 4637,
    "name" : "Ellie Roebuck"
  },
  "position" : {
    "id" : 1,
    "name" : "Goalkeeper"
  },
  "location" : [ 23.0, 59.0 ],
  "related_events" : [ "5584b111-1570-492e-850b-8b5ed01816e3", "d3db2f8e-7d93-4477-9caf-d839227ddd69", "dc52bb06-d05d-42b1-b695-40ac6004b283" ]
}
11#dribble事件，过人
#data['type']['name']="Dribble"
{
  "id" : "d3db2f8e-7d93-4477-9caf-d839227ddd69",
  "index" : 37,
  "period" : 1,
  "timestamp" : "00:00:42.220",
  "minute" : 0,
  "second" : 42,
  "type" : {
    "id" : 14,
    "name" : "Dribble"
  },
  "possession" : 4,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 6,
    "name" : "From Counter"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "player" : {
    "id" : 4641,
    "name" : "Francesca Kirby"
  },
  "position" : {
    "id" : 22,
    "name" : "Right Center Forward"
  },
  "location" : [ 98.0, 22.0 ],
  "under_pressure" : true,
  "related_events" : [ "b959ca15-ef15-42df-a945-d25c7822c98e" ],
  "dribble" : {
    "outcome" : {
      "id" : 8,
      "name" : "Complete"
    }
  }
}
12#shot事件，射门
#data['type']['name']="Shot"
{
  "id" : "9b82eaa3-2048-4157-aa9a-eabeb4fa0ebe",
  "index" : 42,
  "period" : 1,
  "timestamp" : "00:00:47.620",
  "minute" : 0,
  "second" : 47,
  "type" : {
    "id" : 16,
    "name" : "Shot"
  },
  "possession" : 4,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 6,
    "name" : "From Counter"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "player" : {
    "id" : 4641,
    "name" : "Francesca Kirby"
  },
  "position" : {
    "id" : 22,
    "name" : "Right Center Forward"
  },
  "location" : [ 115.0, 25.0 ],
  "duration" : 0.56,
  "related_events" : [ "a1c408ce-f949-4dfd-801f-08ed281da0cc", "e3be7ccf-7637-4c6b-b87d-12e7841d84de" ],
  "shot" : {
    "statsbomb_xg" : 0.018856188,
    "end_location" : [ 117.0, 34.0 ],
    "key_pass_id" : "00821d9b-c6c8-4c05-9b81-3cb1bba0e845",
    "body_part" : {
      "id" : 40,
      "name" : "Right Foot"
    },
    "technique" : {
      "id" : 93,
      "name" : "Normal"
    },
    "type" : {
      "id" : 87,
      "name" : "Open Play"
    },
    "outcome" : {
      "id" : 96,
      "name" : "Blocked"
    },
    "freeze_frame" : [ {#此刻球员场上位置
      "location" : [ 97.0, 48.0 ],
      "player" : {
        "id" : 17275,
        "name" : "Hannah Jayne Blundell"
      },
      "position" : {
        "id" : 12,
        "name" : "Right Midfield"
      },
      "teammate" : true
    }, {
      "location" : [ 113.0, 38.0 ],
      "player" : {
        "id" : 4638,
        "name" : "Drew Spence"
      },
      "position" : {
        "id" : 15,
        "name" : "Left Center Midfield"
      },
      "teammate" : true
    }, {
      "location" : [ 112.0, 28.0 ],
      "player" : {
        "id" : 4649,
        "name" : "Esme Beth Morgan"
      },
      "position" : {
        "id" : 2,
        "name" : "Right Back"
      },
      "teammate" : false
    }, {
      "location" : [ 103.0, 50.0 ],
      "player" : {
        "id" : 4635,
        "name" : "Julia Spetsmark"
      },
      "position" : {
        "id" : 21,
        "name" : "Left Wing"
      },
      "teammate" : false
    }, {
      "location" : [ 120.0, 26.0 ],
      "player" : {
        "id" : 4637,
        "name" : "Ellie Roebuck"
      },
      "position" : {
        "id" : 1,
        "name" : "Goalkeeper"
      },
      "teammate" : false
    }, {
      "location" : [ 109.0, 39.0 ],
      "player" : {
        "id" : 4645,
        "name" : "Isobel Mary Christiansen"
      },
      "position" : {
        "id" : 15,
        "name" : "Left Center Midfield"
      },
      "teammate" : false
    }, {
      "location" : [ 117.0, 31.0 ],
      "player" : {
        "id" : 4648,
        "name" : "Abbie McManus"
      },
      "position" : {
        "id" : 3,
        "name" : "Right Center Back"
      },
      "teammate" : false
    }, {
      "location" : [ 115.0, 41.0 ],
      "player" : {
        "id" : 4651,
        "name" : "Demi Stokes"
      },
      "position" : {
        "id" : 6,
        "name" : "Left Back"
      },
      "teammate" : false
    }, {
      "location" : [ 113.0, 32.0 ],
      "player" : {
        "id" : 4658,
        "name" : "Keira Walsh"
      },
      "position" : {
        "id" : 14,
        "name" : "Center Midfield"
      },
      "teammate" : false
    }, {
      "location" : [ 115.0, 36.0 ],
      "player" : {
        "id" : 17524,
        "name" : "Jennifer Patricia Beattie"
      },
      "position" : {
        "id" : 5,
        "name" : "Left Center Back"
      },
      "teammate" : false
    } ]
  }
}
13#goalkeeper事件，守门员相关事件
#data['type']['name']="Goal Keeper"
{
  "id" : "e3be7ccf-7637-4c6b-b87d-12e7841d84de",
  "index" : 44,
  "period" : 1,
  "timestamp" : "00:00:48.793",
  "minute" : 0,
  "second" : 48,
  "type" : {
    "id" : 23,
    "name" : "Goal Keeper"
  },
  "possession" : 4,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "player" : {
    "id" : 4637,
    "name" : "Ellie Roebuck"
  },
  "position" : {
    "id" : 1,
    "name" : "Goalkeeper"
  },
  "location" : [ 1.0, 55.0 ],
  "related_events" : [ "9b82eaa3-2048-4157-aa9a-eabeb4fa0ebe" ],
  "goalkeeper" : {
    "end_location" : [ 2.0, 54.0 ],
    "position" : {
      "id" : 42,
      "name" : "Moving"
    },
    "type" : {
      "id" : 32,
      "name" : "Shot Faced"
    }
  }
}
14#clearance事件，解围
#data['type']['name']="Clearance"
{
  "id" : "867de81d-f448-4035-bde5-02194ee81f17",
  "index" : 47,
  "period" : 1,
  "timestamp" : "00:01:21.460",
  "minute" : 1,
  "second" : 21,
  "type" : {
    "id" : 9,
    "name" : "Clearance"
  },
  "possession" : 5,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 2,
    "name" : "From Corner"
  },
  "team" : {
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "player" : {
    "id" : 4650,
    "name" : "Nadia Nadim"
  },
  "position" : {
    "id" : 23,
    "name" : "Center Forward"
  },
  "location" : [ 5.0, 48.0 ],
  "under_pressure" : true,
  "related_events" : [ "4a0bdf52-ad74-45bd-9add-7d8e55363bb5" ]
}
15#duel事件，对抗
#data['type']['name']="Duel"
{
  "id" : "09f103ef-c29f-474f-9d0e-852813aa2bfc",
  "index" : 79,
  "period" : 1,
  "timestamp" : "00:02:07.500",
  "minute" : 2,
  "second" : 7,
  "type" : {
    "id" : 4,
    "name" : "Duel"
  },
  "possession" : 6,
  "possession_team" : {
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "player" : {
    "id" : 5088,
    "name" : "Crystal Alyssia Dunn Soubrier"
  },
  "position" : {
    "id" : 16,
    "name" : "Left Midfield"
  },
  "location" : [ 6.0, 22.0 ],
  "under_pressure" : true,
  "related_events" : [ "a5c9061b-3ccf-4714-8d0b-49ca89c4b536" ],
  "duel" : {
    "type" : {
      "id" : 11,
      "name" : "Tackle"
    },
    "outcome" : {
      "id" : 14,
      "name" : "Lost Out"
    }
  }
}
16#interception事件，拦截
#data['type']['name']="Interception"
{
  "id" : "a876cd50-2e91-4149-8d62-8cebe8b750ee",
  "index" : 376,
  "period" : 1,
  "timestamp" : "00:09:08.340",
  "minute" : 9,
  "second" : 8,
  "type" : {
    "id" : 10,
    "name" : "Interception"
  },
  "possession" : 20,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "player" : {
    "id" : 4642,
    "name" : "Millie Bright"
  },
  "position" : {
    "id" : 3,
    "name" : "Right Center Back"
  },
  "location" : [ 90.0, 74.0 ],
  "related_events" : [ "a496c2fc-96b6-41bc-b0fd-d9fa9c9b3a25" ],
  "interception" : {
    "outcome" : {
      "id" : 4,
      "name" : "Won"
    }
  }
}
17#foul committed事件，犯规
#data['type']['name']="Foul Committed"
{
  "id" : "5732d059-2120-4443-ad53-c0eccc34de43",
  "index" : 778,
  "period" : 1,
  "timestamp" : "00:18:39.060",
  "minute" : 18,
  "second" : 39,
  "type" : {
    "id" : 22,
    "name" : "Foul Committed"
  },
  "possession" : 43,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "player" : {
    "id" : 4638,
    "name" : "Drew Spence"
  },
  "position" : {
    "id" : 15,
    "name" : "Left Center Midfield"
  },
  "location" : [ 110.0, 55.0 ],
  "counterpress" : true,
  "related_events" : [ "b2ab16a9-d574-4c03-8c1c-14aad7c99cf3", "c6b0d0e4-72df-4445-bea4-73d94e165eb8" ]
}
18#foul won事件，赢得犯规
#data['type']['name']="Foul Won"
{
  "id" : "b2ab16a9-d574-4c03-8c1c-14aad7c99cf3",
  "index" : 779,
  "period" : 1,
  "timestamp" : "00:18:39.060",
  "minute" : 18,
  "second" : 39,
  "type" : {
    "id" : 21,
    "name" : "Foul Won"
  },
  "possession" : 43,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "player" : {
    "id" : 17524,
    "name" : "Jennifer Patricia Beattie"
  },
  "position" : {
    "id" : 5,
    "name" : "Left Center Back"
  },
  "location" : [ 11.0, 26.0 ],
  "under_pressure" : true,
  "related_events" : [ "5732d059-2120-4443-ad53-c0eccc34de43" ]
}
19#offside事件，越位
#data['type']['name']="Offside"
{
  "id" : "62fcf9a6-4404-40dc-92d1-28622b69f1c0",
  "index" : 978,
  "period" : 1,
  "timestamp" : "00:24:42.980",
  "minute" : 24,
  "second" : 42,
  "type" : {
    "id" : 8,
    "name" : "Offside"
  },
  "possession" : 55,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "player" : {
    "id" : 10395,
    "name" : "Maren Nævdal Mjelde"
  },
  "position" : {
    "id" : 13,
    "name" : "Right Center Midfield"
  },
  "location" : [ 116.0, 34.0 ]
}
20#tactical shift事件，战术调整
#data['type']['name']="Tactical Shift"
{
  "id" : "f4dadac0-8a37-4547-a33f-80c5121ea7ab",
  "index" : 1191,
  "period" : 1,
  "timestamp" : "00:29:05.660",
  "minute" : 29,
  "second" : 5,
  "type" : {
    "id" : 36,
    "name" : "Tactical Shift"
  },
  "possession" : 66,
  "possession_team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "duration" : 0.0,
  "tactics" : {
    "formation" : 352,
    "lineup" : [ {
      "player" : {
        "id" : 4640,
        "name" : "Rut Hedvig Lindahl"
      },
      "position" : {
        "id" : 1,
        "name" : "Goalkeeper"
      },
      "jersey_number" : 1
    }, {
      "player" : {
        "id" : 4642,
        "name" : "Millie Bright"
      },
      "position" : {
        "id" : 3,
        "name" : "Right Center Back"
      },
      "jersey_number" : 4
    }, {
      "player" : {
        "id" : 4657,
        "name" : "Anita Amma Ankyewah Asante"
      },
      "position" : {
        "id" : 4,
        "name" : "Center Back"
      },
      "jersey_number" : 6
    }, {
      "player" : {
        "id" : 4633,
        "name" : "Magdalena Lilly Eriksson"
      },
      "position" : {
        "id" : 5,
        "name" : "Left Center Back"
      },
      "jersey_number" : 16
    }, {
      "player" : {
        "id" : 5088,
        "name" : "Crystal Alyssia Dunn Soubrier"
      },
      "position" : {
        "id" : 12,
        "name" : "Right Midfield"
      },
      "jersey_number" : 19
    }, {
      "player" : {
        "id" : 4638,
        "name" : "Drew Spence"
      },
      "position" : {
        "id" : 13,
        "name" : "Right Center Midfield"
      },
      "jersey_number" : 24
    }, {
      "player" : {
        "id" : 4647,
        "name" : "So-Yun Ji"
      },
      "position" : {
        "id" : 14,
        "name" : "Center Midfield"
      },
      "jersey_number" : 10
    }, {
      "player" : {
        "id" : 10395,
        "name" : "Maren Nævdal Mjelde"
      },
      "position" : {
        "id" : 15,
        "name" : "Left Center Midfield"
      },
      "jersey_number" : 18
    }, {
      "player" : {
        "id" : 17275,
        "name" : "Hannah Jayne Blundell"
      },
      "position" : {
        "id" : 16,
        "name" : "Left Midfield"
      },
      "jersey_number" : 3
    }, {
      "player" : {
        "id" : 4659,
        "name" : "Ramona Bachmann"
      },
      "position" : {
        "id" : 22,
        "name" : "Right Center Forward"
      },
      "jersey_number" : 23
    }, {
      "player" : {
        "id" : 4641,
        "name" : "Francesca Kirby"
      },
      "position" : {
        "id" : 24,
        "name" : "Left Center Forward"
      },
      "jersey_number" : 14
    } ]
  }
}
21#shield事件,护球
#data['type']['name']="Shield"
{
  "id" : "74df5ffb-b061-4d0f-beda-41f165e93d00",
  "index" : 580,
  "period" : 1,
  "timestamp" : "00:13:46.180",
  "minute" : 13,
  "second" : 46,
  "type" : {
    "id" : 28,
    "name" : "Shield"
  },
  "possession" : 31,
  "possession_team" : {
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 971,
    "name" : "Chelsea FCW"
  },
  "player" : {
    "id" : 10395,
    "name" : "Maren Nævdal Mjelde"
  },
  "position" : {
    "id" : 13,
    "name" : "Right Center Midfield"
  },
  "location" : [ 38.0, 2.0 ],
  "under_pressure" : true,
  "related_events" : [ "bebf2270-b8d9-4870-a41b-afbcfea06b3b" ]
}
22#dispossessed事件，传球失败
#data['type']['name']="Dispossessed"
{
  "id" : "b5983225-fba0-4ea2-b6d9-c83279110839",
  "index" : 106,
  "period" : 1,
  "timestamp" : "00:03:10.113",
  "minute" : 3,
  "second" : 10,
  "type" : {
    "id" : 3,
    "name" : "Dispossessed"
  },
  "possession" : 9,
  "possession_team" : {
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 746,
    "name" : "Manchester City WFC"
  },
  "player" : {
    "id" : 4635,
    "name" : "Julia Spetsmark"
  },
  "position" : {
    "id" : 21,
    "name" : "Left Wing"
  },
  "location" : [ 50.0, 3.0 ],
  "under_pressure" : true,
  "related_events" : [ "de1de81c-0455-4078-97c4-d0eba0e3b95c" ]
}