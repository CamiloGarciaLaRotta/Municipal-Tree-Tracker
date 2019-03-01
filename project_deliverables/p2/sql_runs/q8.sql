-- 8.1
-- Add the constraint that all workers should start after 2015
ALTER TABLE works_for                                 
ADD CONSTRAINT start_from_2015 
CHECK (start_date > '2015-01-01');


-- 8.2
-- Add constraint that all user's email address should be valid (have an @)
ALTER TABLE users ADD CONSTRAINT valid_email CHECK (u_email LIKE '%@%');