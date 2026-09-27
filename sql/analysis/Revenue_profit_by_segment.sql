SELECT 
	c.customer_segment,
	sum(oi.net_revenue) AS revenue,
	round(sum(net_revenue)-sum(cost_of_goods),2) AS profit
FROM customers c 
LEFT JOIN orders o 
	ON c.customer_id = o.customer_id 
LEFT JOIN order_items oi 
	ON o.order_id = oi.order_id 
GROUP BY c.customer_segment 


