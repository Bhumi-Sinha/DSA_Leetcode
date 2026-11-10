# Write your MySQL query statement below
SELECT p.product_name, sum(o.unit) as unit 
FROM Products p JOIN Orders o
ON p.product_id=o.product_id
WHERE order_date >= '2020-02-01' AND order_date <= '2020-02-29'
GROUP BY p.product_name
HAVING SUM(o.unit)>=100;