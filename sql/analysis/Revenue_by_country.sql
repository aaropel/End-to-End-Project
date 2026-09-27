SELECT 
	sum(op.order_price)  as total_sales,
	country,
	round(avg(age),1) AS average_age,
	round(avg(op.order_price),2) AS avg_spent
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id
JOIN order_price op 
	ON o.order_id = op.order_id 
GROUP BY 
	country
ORDER BY total_sales DESC