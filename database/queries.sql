SELECT
    product,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;

SELECT
    region,
    SUM(revenue) AS total_revenue,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;