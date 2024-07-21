-- Solved on: PostgreSQL 14
SELECT 
  A.employee_id
  , CASE WHEN SUM(deal_size) >= quota THEN 'yes' ELSE 'no' END AS made_quota
FROM sales_quotas A
LEFT JOIN deals B ON A.employee_id = B.employee_id
GROUP BY A.employee_id, quota
ORDER BY 1;