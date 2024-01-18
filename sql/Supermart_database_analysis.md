# Supermart Database Analyis

## Entity Relationship Diagram
<img width="577" alt="image" src="https://raw.githubusercontent.com/tengkumuazabs/my-portfolio/main/sql/erd%20diagram/ERD_Supermart.png">
This database contains 3 tables and has no any relations.

## Q1: How many orders recorded?
````sql
select count(distinct order_id) from sales;
````
**Answer:**
|count|
|-----|
|5009 |

Total overall orders are 5009 orders.

## Q2: Who did the sales the most? (Top 5)
````sql
select c.customer_name, count(s.*) as sales_count from sales s 
inner join customer c on s.customer_id=c.customer_id
group by c.customer_name order by sales_count desc limit 5;
````
**Answer:**
|customer_name|sales_count                      |
|-------------|---------------------------------|
|William Brown|37                               |
|Matt Abelman |34                               |
|John Lee     |34                               |
|Paul Prost   |34                               |
|Jonathan Doherty|32                               |

William Brown did the most orders. He did it 37 times.

## Q3: Who ordered the Xerox 21 and when they were bought?
````sql
select c.customer_name, p.product_name, s.order_date from sales s
inner join customer c on s.customer_id=c.customer_id
inner join product p on s.product_id=p.product_id
where p.product_name = 'Xerox 21';  
````
**Answer:**
|customer_name|product_name                     |order_date|
|-------------|---------------------------------|----------|
|Andy Gerbode |Xerox 21                         |2014-08-09|
|Nat Gilpin   |Xerox 21                         |2015-09-15|
|Sylvia Foulston|Xerox 21                         |2015-01-03|
|Ralph Ritter |Xerox 21                         |2017-12-11|
|Keith Herrera|Xerox 21                         |2017-10-28|
|Benjamin Venier|Xerox 21                         |2015-06-18|
|Steven Cartwright|Xerox 21                         |2015-08-17|

There were 7 people who bought Xerox 21 with the earliest record written on August 9th 2014.

## Q4: What is the most ordered products?
````sql
select p.product_name, count(*) from sales s
inner join product p on s.product_id=p.product_id
group by product_name order by 2 desc limit 5;
````
**Answer:**
|product_name|count                            |
|------------|---------------------------------|
|Staple envelope|48                               |
|Staples     |46                               |
|Easy-staple paper|46                               |
|Avery Non-Stick Binders|20                               |
|Staples in misc. colors|19                               |

Staple envelope is the most ordered product with 48 times of sales record.


