## For login checking purpose we have to create  user and its password 

```
CREATE DATABASE userdb;

USE userdb;

CREATE TABLE user_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

INSERT INTO user_details (username, password) VALUES ('testuser', 'testpassword');

```

### For adding training data -- we need to create table

```
USE userdb;
CREATE TABLE training_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    training_name VARCHAR(255) NOT NULL,
    technology VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    vendor VARCHAR(255),
    company_name VARCHAR(255),
    remarks TEXT,
    labs_used VARCHAR(255)
);

```
