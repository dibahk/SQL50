# Write your MySQL query statement below
SELECT product_id, COALESCE(ROUND(SUM(price * units)/SUM(units), 2), 0) AS "average_price"
FROM (
    SELECT p.product_id, p.price, u.units
    FROM Prices p
    LEFT JOIN UnitsSold u 
    ON p.product_id = u.product_id 
    AND u.purchase_date <= p.end_date
    AND u.purchase_date >= p.start_date
) AS result
GROUP BY product_id;
