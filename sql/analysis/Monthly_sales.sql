SELECT 
	STRFTIME('%Y-%m',order_date) AS month,
	sum(net_revenue)  AS revenue,
	round(sum(net_revenue)-sum(cost_of_goods),2) AS profit,
	ROUND((sum(net_revenue)-sum(cost_of_goods))/sum(net_revenue),3) * 100.0 AS profit_margin_pct
FROM orders
JOIN order_items
ON orders.order_id = order_items.order_id
GROUP BY month
ORDER BY month;


