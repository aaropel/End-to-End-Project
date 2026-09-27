SELECT 
	p.product_name,
	count(r.return_id)AS return_amount,
	round(count(r.return_id) * 100.0 / count(oi.product_id),1) AS return_rate_pct
FROM order_items oi
LEFT JOIN returns r
	ON r.order_item_id = oi.order_item_id 
LEFT JOIN products p 
	ON oi.product_id = p.product_id 
GROUP BY 
	p.product_id, 
	p.product_name 
ORDER BY return_amount DESC