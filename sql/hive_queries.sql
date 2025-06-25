-- Query to analyze joined data
SELECT
  city,
  COUNT(user_id) AS user_count,
  SUM(amount) AS total_sales,
  AVG(avg_order_value) AS avg_value
FROM user_activity_summary
GROUP BY city;