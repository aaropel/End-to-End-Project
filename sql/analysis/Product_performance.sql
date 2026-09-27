SELECT	
	sum(net_revenue)  as total_sales,
	round(sum(net_revenue)-sum(cost_of_goods),2) AS Profit,
	round(round(sum(net_revenue)-sum(cost_of_goods),2)/sum(net_revenue),2) * 100.0 AS gross_margin_pct, 
	p.product_id,
	p.product_name,
	count(r.order_item_id ) AS returns,
	round(count(r.order_item_id) * 100.0 / count(oi.order_item_id),2) AS return_rate_pct
FROM orders o
JOIN order_items oi
	ON o.order_id = oi.order_id
JOIN products p
	ON oi.product_id = p.product_id 
LEFT JOIN returns r
	ON oi.order_item_id  = r.order_item_id
GROUP BY p.product_id
ORDER BY total_sales DESC