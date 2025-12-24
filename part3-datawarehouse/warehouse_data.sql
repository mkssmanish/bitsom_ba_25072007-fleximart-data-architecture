USE fleximart_dw;

INSERT INTO dim_date VALUES
(20240115,'2024-01-15','Monday',15,1,'January','Q1',2024,FALSE),
(20240116,'2024-01-16','Tuesday',16,1,'January','Q1',2024,FALSE),
(20240120,'2024-01-20','Saturday',20,1,'January','Q1',2024,TRUE),
(20240128,'2024-01-28','Sunday',28,1,'January','Q1',2024,TRUE),
(20240201,'2024-02-01','Thursday',1,2,'February','Q1',2024,FALSE),
(20240205,'2024-02-05','Monday',5,2,'February','Q1',2024,FALSE),
(20240210,'2024-02-10','Saturday',10,2,'February','Q1',2024,TRUE),
(20240218,'2024-02-18','Sunday',18,2,'February','Q1',2024,TRUE);


INSERT INTO dim_product (product_id, product_name, category, subcategory, unit_price) VALUES
('P001','Samsung Galaxy S21','Electronics','Mobile',45999),
('P007','HP Laptop','Electronics','Laptop',52999),
('P014','iPhone 13','Electronics','Mobile',69999),
('P004','Levi''s Jeans','Fashion','Clothing',2999),
('P008','Adidas T-Shirt','Fashion','Clothing',1299),
('P011','Puma Sneakers','Fashion','Footwear',4599),
('P009','Basmati Rice 5kg','Groceries','Food Grains',650),
('P015','Organic Honey 500g','Groceries','Organic',450),
('P018','Masoor Dal 1kg','Groceries','Pulses',120);


INSERT INTO dim_customer (customer_id, customer_name, city, state, customer_segment) VALUES
('C001','Rahul Sharma','Bangalore','Karnataka','Urban'),
('C002','Priya Patel','Mumbai','Maharashtra','Metro'),
('C003','Amit Kumar','Delhi','Delhi','Metro'),
('C004','Sneha Reddy','Hyderabad','Telangana','Urban'),
('C005','Vikram Singh','Chennai','Tamil Nadu','Urban'),
('C006','Anjali Mehta','Bangalore','Karnataka','Urban'),
('C007','Ravi Verma','Pune','Maharashtra','Urban'),
('C008','Pooja Iyer','Bangalore','Karnataka','Urban'),
('C009','Karthik Nair','Kochi','Kerala','Urban'),
('C010','Deepa Gupta','Delhi','Delhi','Metro'),
('C011','Arjun Rao','Hyderabad','Telangana','Urban'),
('C012','Lakshmi Krishnan','Chennai','Tamil Nadu','Urban');


INSERT INTO fact_sales
(date_key, product_key, customer_key, quantity_sold, unit_price, discount_amount, total_amount)
VALUES
(20240115,1,1,1,45999,0,45999),
(20240116,4,2,2,2999,0,5998),
(20240120,7,5,3,650,0,1950),
(20240128,3,10,1,69999,0,69999),
(20240201,6,3,1,4599,0,4599),
(20240205,2,6,1,52999,2000,50999),
(20240210,8,8,4,450,0,1800),
(20240218,9,9,10,120,0,1200);
