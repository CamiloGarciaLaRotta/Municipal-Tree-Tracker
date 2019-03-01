-- 5.1
-- relations used: city, municipality
-- query: list the names of cities that have more than 2 municipalities in descending order

SELECT city.c_name, COUNT(mid) as num_municipality 
FROM city, municipality WHERE municipality.cid = city.cid 
GROUP BY city.c_name HAVING COUNT(mid) > 2 
ORDER BY COUNT(mid) DESC;

-- 5.2
-- relations used: works_for
-- query: display the uids of workers who started working after Feb 2019

SELECT uid, start_date FROM works_for WHERE start_date > '2019-02-01' ORDER BY start_date;

-- 5.3
-- relations used: municipality, tree
-- query: display the names of the municipalities that have more than 2 trees located inside, and the count of trees, in descending order

SELECT municipality.m_name, COUNT(tid) as tree_count
FROM municipality, tree 
WHERE municipality.mid = tree.mid 
GROUP BY municipality.m_name HAVING count(tid) >2 
ORDER BY tree_count DESC, municipality.m_name;

-- 5.4
-- relations used: users, orders
-- query: Find all the users who have placed more than 5 orders and display their uid, names and email addresses in descending order of number of orders placed.

SELECT users.uid, u_name, users.u_email, COUNT(transid) as number_of_orders_placed
FROM users, orders
WHERE orders.uid = users.uid
GROUP BY u_name, users.uid, users.u_email HAVING COUNT(transid) > 5
ORDER BY number_of_orders_placed DESC, u_name;

-- 5.5
-- relations used: works_for, city
-- query: find all the cities that have more than 3 workers in descending order, and displays the cid, city name and the number of workers

SELECT city.cid, city.c_name, COUNT(works_for.uid) as number_of_workers 
FROM works_for, city WHERE works_for.cid = city.cid 
GROUP BY city.cid, city.c_name HAVING COUNT(uid) > 3 
ORDER BY COUNT(works_for.uid) DESC, city.c_name;