-- You are given a table Products with the following structure:
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | product_id  | int     |
-- | low_fats    | enum    |
-- | recyclable  | enum    |
-- +-------------+---------+
-- -> product_id is the primary key.
-- -> low_fats is an ENUM with values 'Y' or 'N', indicating whether the product is low-fat.
-- -> recyclable is an ENUM with values 'Y' or 'N', indicating whether the product is recyclable.

-- Task:
-- Write an SQL query to return the IDs of all products that are both low-fat and recyclable.
-- Return the result in any order.

/****************************************************************************************/

-- TABLE: customers                 TABLE: books                     TABLE: authors                 TABLE: sales
-- +----------------+---------+     +--------------+---------+       +----------------+---------+     +----------------+-----------+
-- | customer_id    | int     |     | book_id      | int     |       | author_id      | int     |     | sale_id        | int       |
-- | invited_by     | int     |     | author_id    | int     |       | website_url    | varchar |     | customer_id    | int       |
-- +----------------+---------+     | price        | decimal |       +----------------+---------+     | book_id        | int       |
--                                  +--------------+---------+                                       | payment_type   | varchar   |
--                                                                                                   | amount         | decimal   |
--                                                                                                   +----------------+-----------+

-- Q1. Find the top 5 customers ranked by the average payment per book made by the customers they personally invited.

-- Q2. From the authors table, determine: 
-- the total number of authors,
-- the percentage whose website contains .com,
-- the percentage who never recorded a sale through any of their books.

-- Q3. For each payment type, compute the total sales amount and the count of unique customers, then return the results grouped and sorted in descending order by payment type.

/****************************************************************************************/

-- TABLE: customers                      TABLE: books                          TABLE: sales
-- +-------------------+-------------+   +-------------------+-------------+    +-------------------+-------------+
-- | customer_id       | int         |   | book_id           | int         |    | sale_id           | int         |
-- | reward_status     | varchar     |   | price             | decimal     |    | customer_id       | int         |
-- +-------------------+-------------+   +-------------------+-------------+    | book_id           | int         |
--                                                                               | quantity          | int         |
--                                                                               | amount            | decimal     |
--                                                                               | sale_date         | date        |
--                                                                               | refunded          | boolean     |
--                                                                               +-------------------+-------------+
-- Q1. Retrieve the top 10 customers who purchased the highest total number of books in 2019, considering only non-refunded sales.

-- Q2. Calculate the average total purchase amount, grouped by:
--     reward membership status, and
--     whether the purchase occurred in season (after Nov 15) or non-season.

-- Q3.Determine what percentage of total revenue is contributed by the top 5 most expensive books.

-- Q4.Identify customers who:
--     made purchases on more than one distinct day, and
--     bought more than 3 books combined across their first and last purchase dates.

/****************************************************************************************/

-- Find the second highest salary from an employee table.

/****************************************************************************************/

-- TABLE: books                          TABLE: inventory                     TABLE: borrowers
-- +-------------+-------------+          +-------------+-------------+        +-------------+-------------+
-- | book_id     | int         |          | book_id     | int         |        | borrower_id | int         |
-- | condition   | varchar     |          | copies      | int         |        | referred_by | int         |
-- | renew_count | int         |          +-------------+-------------+        +-------------+-------------+

-- TABLE: transactions                   TABLE: book_logs
-- +-------------+-------------+          +-------------+-------------+
-- | borrower_id | int         |          | book_id     | int         |
-- | book_id     | int         |          | log_flag    | boolean     | -- True=checkout, False=return
-- | category    | varchar     |          +-------------+-------------+
-- | price       | decimal     |
-- +-------------+-------------+

-- Q1. Identify all books that are in good condition and have been renewed exactly twice.

-- Q2. Calculate the percentage of books whose inventory shows more than 10 available copies.

-- Q3. For each borrower, compute the difference in renewal counts between them and the member who referred them.

-- Q4. Given a list of (category, price) pairs per user, compute the total borrowed price assuming each user may borrow from up to 3 distinct categories.

-- Q5. Validate book log entries so that:
--     a book cannot be checked out if it is already checked out, and
--     a book cannot be returned if it is not currently checked out.

-- Q6. Compare the percentage of total sales that occurred on the first sale day vs. the last sale day (based on the earliest and latest sale_date across all transactions)

-- Q7. Determine how many books are in good condition and have not been returned (i.e., their last log entry is a checkout).

-- Q8. Among the books identified in Q7, calculate the percentage whose renew_count is greater than 2.

/****************************************************************************************/

-- TABLE: customers                       TABLE: restaurants                    TABLE: orders
-- +-------------------+-------------+     +-------------------+-------------+   +-------------------+-------------+
-- | customer_id       | int         |     | restaurant_id     | int         |   | order_id          | int         |
-- | name              | varchar     |     | name              | varchar     |   | customer_id       | int         |
-- +-------------------+-------------+     | location          | varchar     |   | restaurant_id     | int         |
--                                         +-------------------+-------------+   | order_date        | date        |
--                                                                                 +-------------------+-------------+

-- Q1. Design a data model for a food-delivery service that tracks customers, restaurants, and orders.

-- Q2. Identify all customers who did not place any order from the restaurant with restaurant_id = 3.

-- Q3. Determine how many customers never placed an order at all.