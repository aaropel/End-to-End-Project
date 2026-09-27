SELECT 
	c.campaign_id,
	c.clicks, c.impressions,
	count(o.campaign_id) AS made_purchases,
	round(count(o.order_id) * 100.0/ NULLIF(c.clicks, 0),2) AS conversion_rate_pct,
	round(c.spend / NULLIF(count(o.campaign_id),0),2) AS cost_per_purchase,
	round(sum(op.order_price) / c.spend,2) AS ROAS
FROM campaigns c  
LEFT JOIN orders o
	ON o.campaign_id = c.campaign_id 
LEFT JOIN order_price op
	ON o.order_id = op.order_id 
GROUP BY 
	c.campaign_id,
	c.clicks,
	c.impressions ,
	c.spend
ORDER BY ROAS DESC
