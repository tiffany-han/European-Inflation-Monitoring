# European Inflation Monitoring－Data Pipeline Development and Economic Analysis

[English](README.md) | [繁體中文](README.zh-TW.md)


## Project Overview

This project aims to develop a semi-automated data pipeline for monitoring European inflation trends by integrating Python, SQL, and Power BI.

Monthly economic data is retrieved from the Eurostat API, processed using Python and pandas, and stored in a MySQL database. Power BI is then connected to the database to create interactive dashboards for economic monitoring and analysis.

The goal is to transform publicly available economic data into meaningful insights that can support business monitoring and financial decision-making.

**Data Coverage: Monthly data updated through October 2026.**

## Business Objectives

The dashboard aims to provide insights into three key areas:

- **Consumer Demand:** Monitor inflation trends across countries to assess potential impacts on local purchasing power and consumer demand, which may indirectly affect business revenue.
- **Inflation Trends:** Identify whether inflation is accelerating or slowing down across different European markets.
- **Financial and Monetary Environment:** Track inflation developments to help finance and treasury teams monitor potential implications for interest rate expectations, borrowing costs, and foreign currency exposure.

## Data Workflow

| Stage | Tools | Key Activities |
|---|---|---|
| Data Extraction | Python, Eurostat API | Retrieve data using configurable parameters for countries, periods, and categories |
| Data Processing | Python, pandas | Parse JSON, clean, transform, and standardize data |
| Data Management | SQL, MySQL | Store data, validate records, prevent duplicates, and create analytical views |
| Data Visualization | Power BI | Build interactive dashboards for economic analysis |

**Monthly Update Process**

Eurostat Data Release → Python Data Extraction → MySQL Data Update → Power BI Refresh

## Dashboard & Economic Analysis

The Power BI dashboard provides four major analytical perspectives:

- **Inflation Overview:** Compare EU and Euro Area inflation trends.
- **Country Comparison:** Visualize geographical differences and country-level inflation rankings.
- **Category Analysis:** Examine inflation across energy, services, industrial goods, and food.
- **Energy & Retail Analysis:** Explore crude oil prices, energy inflation, food inflation, and retail trade volume.

### Key Findings

- **Inflation Differences:** Observed significant differences in inflation developments across European countries.
- **Energy Price Impact:** Liquid fuel inflation reached approximately 31% year-on-year, with movements broadly aligned with crude oil prices.
- **Consumer and Retail Trends:** Compared food inflation and retail trade volume in the Netherlands and Belgium to examine differences in consumption trends.

For detailed charts and economic interpretations, please refer to the project presentation.

## Technology Stack

| Technology | Application |
|---|---|
| Eurostat API | European economic data source |
| Python / pandas | API extraction and data processing |
| SQL / MySQL | Database management and data validation |
| Power BI | Interactive dashboards and visualization |

## Development Progress

**Completed**
- Developed configurable multi-country and multi-period data extraction.
- Processed and standardized Eurostat data using Python and pandas.
- Stored historical data in MySQL with composite unique keys to prevent duplicate records.
- Created SQL validation queries and analytical views.
- Connected MySQL to Power BI and completed interactive dashboards.
- Completed economic analysis and project presentation.

**Future Development**
- Incorporate additional European indicators, such as PPI, employment, wage growth, and household savings.
- Integrate US CPI and EUR/USD exchange rate data.
- Further automate monthly data updates and expand cross-market analysis.

## Data Source

- [Eurostat – Harmonised Index of Consumer Prices (HICP)](https://ec.europa.eu/eurostat/databrowser/product/page/PRC_HICP_MINR)
- [Eurostat – Retail Trade Statistics](https://ec.europa.eu/eurostat)
- Taiwan Ministry of Economic Affairs, Energy Administration – Crude Oil Price Data

---

**Project Focus:** Data Pipeline Development | Economic Analysis | Financial and Business Decision Support

**Project Status:** Completed


