# Nestlé-Style FMCG Sales and Demand Analysis

A data analytics project focused on analyzing FMCG-style sales and demand patterns using **Python, SQL, and Tableau**, with a Nestlé-inspired business perspective on category performance, sales channels, city-level trends, and monthly demand behavior.

---

## Project Overview

This project transforms a raw retail supermarket dataset into a **Nestlé-style FMCG portfolio** for business analysis.  
The objective was to simulate how an FMCG company can use data to understand:

- Which product categories drive the highest sales
- Which sales channels contribute the most revenue
- Which cities perform best
- How demand changes over time
- What transaction patterns indicate high, medium, or low demand

The project combines **Python for data cleaning and feature engineering**, **SQL for KPI and business analysis**, and **Tableau for dashboard visualization**.

---

## Tools & Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **SQL (MySQL)**
- **Tableau Public**
- **Excel / CSV**

---

## Data Preparation & Transformation

The original supermarket sales dataset was transformed into a more business-relevant FMCG structure by creating custom fields such as:

- **Nestlé-style product categories**
- **Sales channel segmentation**
- **Demand level classification**
- **Month and day-based features**

### Example transformations:
- `Health and beauty` → `Nutrition & Wellness`
- `Food and beverages` → `Packaged Foods & Beverages`
- `Member / Normal` customer types → `Modern Trade / General Trade`
- Quantity-based transaction segmentation into:
  - High Demand
  - Medium Demand
  - Low Demand

---

## Key KPIs

- **Total Sales:** 322,966.75
- **Total Gross Income:** 15,379.37
- **Total Quantity Sold:** 5,510
- **Top Category by Sales:** Packaged Foods & Beverages
- **Top Sales Channel:** Modern Trade
- **Top City by Sales:** Naypyitaw

---

## Key Business Insights

- **Packaged Foods & Beverages** emerged as the top-performing category by sales.
- **Modern Trade** generated higher revenue than General Trade.
- **Naypyitaw** recorded the highest city-level sales.
- **Medium-demand transactions** were the most frequent, indicating stable routine purchase behavior.
- Sales peaked in the **early months**, suggesting possible seasonality or promotional demand concentration.
- **Nutrition & Wellness** underperformed relative to other categories, indicating scope for stronger category strategy.

---

## SQL Analysis Performed

Using SQL, the project analyzed:

- Total sales, quantity sold, and gross income
- Category-wise sales contribution
- Sales by channel
- City-wise sales trends
- Demand level distribution
- Monthly sales trends
- Average rating by category
- High-demand transactions by category

All SQL queries are available in the file:  
`sql_queries.sql`

---

## Dashboard

The Tableau dashboard highlights:

- Sales by Nestlé Category
- Sales by Channel
- Sales by City
- Monthly Sales Trend
- Demand Level Distribution

If published later, add Tableau Public link here:

**Tableau Public Link:** _Add your dashboard link here_

---

## Repository Structure

```text
fmcg-sales-demand-analysis/
│
├── analysis.py
├── sql_queries.sql
├── requirements.txt
├── .gitignore
├── README.md
├── nestle_fmcg_transformed.csv
└── dashboard/
