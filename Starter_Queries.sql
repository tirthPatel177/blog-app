-- To create a database
CREATE DATABASE blog;


-- To Drop/Delete Database
-- DROP DATABASE blog;


-- To start psql in terminal
-- -U username -h host -p portnumber 
-- psql -h localhost -p 5432 -U postgres databasename


--To connect to a data base 
-- \c databasename


-- To Create user
CREATE USER dbmsproj WITH ENCRYPTED PASSWORD '1772002';
GRANT ALL PRIVILEGES ON DATABASE blog TO dbmsproj;
