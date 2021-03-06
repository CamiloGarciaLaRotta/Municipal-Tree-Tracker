
-- CITY inserts
INSERT INTO CITY (cid, c_name, c_polygon) VALUES (1, 'Montreal', '((2,2),(3,4),(3,6),(1,1))' );
INSERT INTO CITY (cid, c_name, c_polygon) VALUES (2, 'Laval', '((2,2),(3,4),(3,6),(1,1))' );
INSERT INTO CITY (cid, c_name, c_polygon) VALUES (3, 'Toronto', '((2,2),(3,4),(3,6),(1,1))' );
INSERT INTO CITY (cid, c_name, c_polygon) VALUES (4, 'Vancouver', '((2,2),(3,4),(3,6),(1,1))' );
INSERT INTO CITY (cid, c_name, c_polygon) VALUES (5, 'NewYork', '((2,2),(3,4),(3,6),(1,1))' );

-- Municipality inserts
INSERT INTO MUNICIPALITY (mid, m_name, m_population, m_polygon, cid) VALUES (1, 'Ville Marie', 33333, '((2,2),(3,4),(3,6),(1,1))', 1);
INSERT INTO MUNICIPALITY (mid, m_name, m_population, m_polygon, cid) VALUES (2, 'Queens', 33333, '((2,2),(3,4),(3,6),(1,1))', 5);
INSERT INTO MUNICIPALITY (mid, m_name, m_population, m_polygon, cid) VALUES (3, 'Mont Royal', 33333, '((2,2),(3,4),(3,6),(1,1))', 1);
INSERT INTO MUNICIPALITY (mid, m_name, m_population, m_polygon, cid) VALUES (4, 'WestMount', 33333, '((2,2),(3,4),(3,6),(1,1))', 1);
INSERT INTO MUNICIPALITY (mid, m_name, m_population, m_polygon, cid) VALUES (5, 'Concorde', 33333, '((2,2),(3,4),(3,6),(1,1))', 2);

-- Civic location inserts
INSERT INTO CIVIC_LOCATION (civid, civic_address, civic_type) VALUES (1, '324 cote vertu', 'RESIDENTIAL');
INSERT INTO CIVIC_LOCATION (civid, civic_address, civic_type) VALUES (2, '324 de le concorde', 'RESIDENTIAL');
INSERT INTO CIVIC_LOCATION (civid, civic_address, civic_type) VALUES (3, '3919 west 18th avenue', 'INDUSTRIAL');
INSERT INTO CIVIC_LOCATION (civid, civic_address, civic_type) VALUES (4, '2131 rue de le victoire', 'COMERCIAL');
INSERT INTO CIVIC_LOCATION (civid, civic_address, civic_type) VALUES (5, '3 watson street', 'FARM');

-- Park inserts
INSERT INTO PARK (pid, p_name, p_polygon, mid) VALUES (1, 'mont royal', '((2,2),(3,4),(3,6),(1,1))', 1);
INSERT INTO PARK (pid, p_name, p_polygon, mid) VALUES (2, 'central park','((2,2),(3,4),(3,6),(1,1))', 2);
INSERT INTO PARK (pid, p_name, p_polygon, mid) VALUES (3, 'park de rose', '((2,2),(3,4),(3,6),(1,1))', 3);
INSERT INTO PARK (pid, p_name, p_polygon, mid) VALUES (4, 'freedom park','((2,2),(3,4),(3,6),(1,1))', 4);
INSERT INTO PARK (pid, p_name, p_polygon, mid) VALUES (5, 'joy park', '((2,2),(3,4),(3,6),(1,1))', 5);

-- Tree inserts
INSERT INTO  TREE (tid, geog_loc, planted_date, species, mid, pid, civid) VALUES (1, Point(47.65100, -122.34900)  , '2019-01-01', 'ALDER', 1, 1, 1);
INSERT INTO  TREE (tid, geog_loc, planted_date, species, mid, pid, civid) VALUES (2, Point(47.65100, -122.34900)  , '2015-03-01', 'COTTONWOOD', 2, 2, 2);
INSERT INTO  TREE (tid, geog_loc, planted_date, species, mid, pid, civid) VALUES (3, Point(47.65100, -122.34900)  , '2011-04-01', 'CHINKAPIN', 3, 3, 3);
INSERT INTO  TREE (tid, geog_loc, planted_date, species, mid, pid, civid) VALUES (4, Point(47.65100, -122.34900)  , '2012-05-01', 'CHESTNUT', 4, 4, 4);
INSERT INTO  TREE (tid, geog_loc, planted_date, species, mid, pid, civid) VALUES (5, Point(47.65100, -122.34900)  , '2013-06-01', 'CHERRY', 5, 5, 5);

-- Users inserts
INSERT INTO USERS (uid, u_type, u_name, u_email, u_phone, civid) VALUES (1,'RESIDENT', 'elias', 'elias@elias.ca', '4232828282', 1);
INSERT INTO USERS (uid, u_type, u_name, u_email, u_phone, civid) VALUES (2,'RESIDENT', 'patrik', 'patriks@patrik.ca', '4232228282', 2);
INSERT INTO USERS (uid, u_type, u_name, u_email, u_phone, civid) VALUES (3,'ENV_SCIENTIST', 'majd', 'majd@majd.ca', '4232818282', 3);
INSERT INTO USERS (uid, u_type, u_name, u_email, u_phone, civid) VALUES (4,'URBAN_PLANNER', 'rose', 'rose@rose.ca', '4232823292', 4);
INSERT INTO USERS (uid, u_type, u_name, u_email, u_phone, civid) VALUES (5,'URBAN_PLANNER', 'marie', 'marie@marie.ca', '4233382282', 5);

-- Works For Inserts
INSERT INTO WORKS_FOR (cid, uid, start_date) VALUES (1, 1, '2019-01-01');
INSERT INTO WORKS_FOR (cid, uid, start_date) VALUES (2, 2, '2012-01-01');
INSERT INTO WORKS_FOR (cid, uid, start_date) VALUES (3, 3, '2013-01-01');
INSERT INTO WORKS_FOR (cid, uid, start_date) VALUES (4, 4, '2011-01-01');
INSERT INTO WORKS_FOR (cid, uid, start_date) VALUES (5, 5, '2010-01-01');

-- Transactions inserts
INSERT INTO TRANSACTIONS (transid, trans_status, tree_species, civid) VALUES (1,'REFUSED', 'ALDER', 1);
INSERT INTO TRANSACTIONS (transid, trans_status, tree_species, civid) VALUES (2,'APPROVED', 'CALIFORNIALAUREL', 2);
INSERT INTO TRANSACTIONS (transid, trans_status, tree_species, civid) VALUES (3,'REFUSED', 'CEDAR', 3);
INSERT INTO TRANSACTIONS (transid, trans_status, tree_species, civid) VALUES (4,'PENDING', 'CHESTNUT', 4);
INSERT INTO TRANSACTIONS (transid, trans_status, tree_species, civid) VALUES (5,'APPROVED', 'CHERRY', 5);

-- Review inserts
INSERT INTO REVIEW (transid, uid) VALUES  (1, 1);
INSERT INTO REVIEW (transid, uid) VALUES  (2, 2);
INSERT INTO REVIEW (transid, uid) VALUES  (3, 3);
INSERT INTO REVIEW (transid, uid) VALUES  (4, 4);
INSERT INTO REVIEW (transid, uid) VALUES  (5, 5);

-- Orders inserts
INSERT INTO ORDERS (transid, uid) VALUES  (1, 1);
INSERT INTO ORDERS (transid, uid) VALUES  (2, 2);
INSERT INTO ORDERS (transid, uid) VALUES  (3, 3);
INSERT INTO ORDERS (transid, uid) VALUES  (4, 4);
INSERT INTO ORDERS (transid, uid) VALUES  (5, 5);

-- Assessment inserts
INSERT INTO ASSESSMENT (assess_date, assess_status, assess_action, tid, uid)  VALUES ('2019-01-01', 'HEALTHY', 'leave it as is :)', 1, 1);
INSERT INTO ASSESSMENT (assess_date, assess_status, assess_action, tid, uid)  VALUES ('2013-03-02', 'TO_CUT', 'leave it as is :)', 2, 2);
INSERT INTO ASSESSMENT (assess_date, assess_status, assess_action, tid, uid)  VALUES ('2011-02-03', 'INFESTED', 'leave it as is :)', 3, 3);
INSERT INTO ASSESSMENT (assess_date, assess_status, assess_action, tid, uid)  VALUES ('2013-08-04', 'DAMAGED', 'leave it as is :)', 4, 4);
INSERT INTO ASSESSMENT (assess_date, assess_status, assess_action, tid, uid)  VALUES ('2012-02-05', 'HEALTHY', 'leave it as is :)', 5, 5);


