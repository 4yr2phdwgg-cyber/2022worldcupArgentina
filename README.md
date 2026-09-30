
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

## 8. Author / 作者

This is a personal learning project focused on Python, Pandas, and football data analysis, with the long-term goal of developing skills in football analytics.

这是一个个人学习与实践项目，主要围绕 Python、Pandas 和足球数据分析展开，长期目标是进一步学习足球数据分析。
