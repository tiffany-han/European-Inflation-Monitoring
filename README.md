# Semi-automated Data Pipeline for European Inflation Monitoring
## Project Overview

This project aims to automate the collection, processing, and storage of European inflation data using Python and SQL, with Power BI used to create interactive visualizations and monitor inflation trends.

By retrieving monthly Harmonised Index of Consumer Prices (HICP) data from Eurostat, the project develops an interactive dashboard to monitor inflation trends and compare price developments across European countries.

The goal is to transform publicly available economic data into meaningful insights that can support business monitoring and financial decision-making.

## Business Objectives

The dashboard aims to provide insights into three key areas:

- **Consumer Demand:** Monitor inflation trends across countries to assess potential impacts on local purchasing power and consumer demand, which may indirectly affect business revenue.
- **Inflation Trends:** Identify whether inflation is accelerating or slowing down across different European markets.
- **Financial and Monetary Environment:** Track inflation developments to help finance and treasury teams monitor potential implications for interest rate expectations, borrowing costs, and foreign currency exposure.

## Data Workflow

1. **Data Extraction:** Retrieve monthly HICP data from the Eurostat API using Python.
2. **Data Processing:** Parse JSON responses, clean and transform the data using Python.
3. **Data Storage:** Store processed data in a SQL database.
4. **Data Retrieval:** Query structured data from the database.
5. **Data Visualization:** Build interactive dashboards in Power BI to explore inflation trends and compare countries.

## Tools & Technologies

| Tool | Application |
|---|---|
| Python | API data extraction and data processing |
| SQL | Database management and data retrieval |
| Power BI | Interactive data visualization |
| Eurostat API | Public economic data source |

## Potential Business Applications

- Monitoring inflation developments across European markets.
- Identifying country-level differences in price trends.
- Supporting business environment assessments.
- Providing economic indicators for financial and treasury monitoring.

## Future Development

- Incorporate additional European economic indicators to provide a broader view of the economic environment.
- Integrate US CPI data and exchange rate data to explore international inflation differentials and their potential relationship with foreign exchange movements.
- Further automate the data pipeline to support regular data updates.

## Data Source

- [Eurostat – Harmonised Index of Consumer Prices (HICP)](https://ec.europa.eu/eurostat/databrowser/product/page/PRC_HICP_MINR)

---

**Project Status:** In Progress

### Current Version – Data Extraction

- Supports data extraction for multiple countries and different time periods through configurable parameters.
- Successfully consolidates the extracted data from multiple countries into a single CSV file.
- The current dataset includes the following columns:

| Column | Description |
|---|---|
| `country_code` | Country code |
| `country_name` | Country name |
| `categories` | Classification of individual consumption by purpose |
| `period` | Reporting period |
| `value` | HICP value |


