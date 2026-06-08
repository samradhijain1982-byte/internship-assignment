CREATE DATABASE DataBank;
GO

USE DataBank;
GO

CREATE TABLE regions (
    region_id INT,
    region_name VARCHAR(20)
);

INSERT INTO regions VALUES
(1,'Africa'),
(2,'America'),
(3,'Asia'),
(4,'Europe'),
(5,'Oceania');

CREATE TABLE customer_nodes (
    customer_id INT,
    region_id INT,
    node_id INT,
    start_date DATE,
    end_date DATE
);

INSERT INTO customer_nodes VALUES
(1,3,4,'2020-01-02','2020-01-03'),
(2,3,5,'2020-01-03','2020-01-17'),
(3,5,4,'2020-01-27','2020-02-18'),
(4,5,4,'2020-01-07','2020-01-19'),
(5,3,3,'2020-01-15','2020-01-23'),
(6,1,1,'2020-01-11','2020-02-06'),
(7,2,5,'2020-01-20','2020-02-04'),
(8,1,2,'2020-01-15','2020-01-28'),
(9,4,5,'2020-01-21','2020-01-25'),
(10,3,4,'2020-01-13','2020-01-14');

CREATE TABLE customer_transactions (
    customer_id INT,
    txn_date DATE,
    txn_type VARCHAR(20),
    txn_amount INT
);

INSERT INTO customer_transactions VALUES
(429,'2020-01-21','deposit',82),
(155,'2020-01-10','deposit',712),
(398,'2020-01-01','deposit',196),
(255,'2020-01-14','deposit',563),
(185,'2020-01-29','deposit',626),
(309,'2020-01-13','deposit',995),
(312,'2020-01-20','deposit',485),
(376,'2020-01-03','deposit',706),
(188,'2020-01-13','deposit',601),
(138,'2020-01-11','deposit',520);

SELECT * FROM regions;
SELECT * FROM customer_nodes;
SELECT * FROM customer_transactions;

--- part A-----

--question 1

SELECT COUNT(DISTINCT node_id) AS total_nodes
FROM customer_nodes;


--question 2
SELECT region_name,
       COUNT(DISTINCT node_id) AS total_nodes
FROM customer_nodes c
JOIN regions r
ON c.region_id=r.region_id
GROUP BY r.region_name;

--question 3
SELECT r.region_name,
       COUNT(DISTINCT c.customer_id) AS total_customers
FROM customer_nodes c
JOIN regions r
ON c.region_id=r.region_id
GROUP BY r.region_name;

--question 4
SELECT AVG(DATEDIFF(day,start_date,end_date)*1.0)
AS avg_days
FROM customer_nodes;

----part B-----

--question 1--
SELECT txn_type,
       COUNT(*) AS total_transactions,
       SUM(txn_amount) AS total_amount
FROM customer_transactions
GROUP BY txn_type;

--question 2--
SELECT AVG(txn_amount*1.0) AS avg_deposit
FROM customer_transactions
WHERE txn_type='deposit';

--question 3--
SELECT MONTH(txn_date) AS month_no,
       COUNT(*) AS total_transactions
FROM customer_transactions
GROUP BY MONTH(txn_date);

--question 4--
SELECT customer_id,
       SUM(txn_amount) AS closing_balance
FROM customer_transactions
GROUP BY customer_id;


--PART C-----
--question 1--
SELECT customer_id,
       txn_date,
       txn_amount,

       SUM(txn_amount)
       OVER(
            PARTITION BY customer_id
            ORDER BY txn_date
       ) AS running_balance

FROM customer_transactions;

--question 2--
SELECT customer_id,
       MONTH(txn_date) AS month_no,
       SUM(txn_amount) AS balance
FROM customer_transactions
GROUP BY customer_id,
         MONTH(txn_date);

--question 3--
SELECT customer_id,
       MIN(txn_amount) AS min_balance,
       AVG(txn_amount*1.0) AS avg_balance,
       MAX(txn_amount) AS max_balance
FROM customer_transactions
GROUP BY customer_id;