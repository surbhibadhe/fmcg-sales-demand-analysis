SELECT ROUND(SUM(sales), 2) AS total_sales
FROM nestle_fmcg_transformed;

SELECT SUM(quantity) AS total_quantity_sold
FROM nestle_fmcg_transformed;

SELECT ROUND(SUM(gross_income), 2) AS total_gross_income
FROM nestle_fmcg_transformed;

SELECT nestle_category, ROUND(SUM(sales), 2) AS total_sales
FROM nestle_fmcg_transformed
GROUP BY nestle_category
ORDER BY total_sales DESC;

SELECT sales_channel, ROUND(SUM(sales), 2) AS total_sales
FROM nestle_fmcg_transformed
GROUP BY sales_channel
ORDER BY total_sales DESC;

SELECT city, ROUND(SUM(sales), 2) AS total_sales
FROM nestle_fmcg_transformed
GROUP BY city
ORDER BY total_sales DESC;

SELECT demand_level, COUNT(*) AS total_transactions
FROM nestle_fmcg_transformed
GROUP BY demand_level
ORDER BY total_transactions DESC;

SELECT month, ROUND(SUM(sales), 2) AS total_sales
FROM nestle_fmcg_transformed
GROUP BY month
ORDER BY total_sales DESC;

SELECT nestle_category, ROUND(AVG(rating), 2) AS avg_rating
FROM nestle_fmcg_transformed
GROUP BY nestle_category
ORDER BY avg_rating DESC;

SELECT nestle_category, COUNT(*) AS high_demand_orders
FROM nestle_fmcg_transformed
WHERE demand_level = 'High Demand'
GROUP BY nestle_category
ORDER BY high_demand_orders DESC;