# Flask

## Setting up MySQL 

### Installing MySQL on Linux ( Fedora )

`sudo dnf install mysql-server`

### Verify the MySQL installation:

`mysql --version`

### Start MySQL service

`sudo systemctl enable mysqld
sudo systemctl enable mysqld`

### Secure MySQL installation (Optional)

`sudo mysql_secure_installation`

### Log into MySQL

`mysql -u root -p`

### Create a database

`CREATE DATABASE flask_data;`

### Create a user and grant privileges (Optional)

`CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON flask_data.* TO 'username'@'localhost';
FLUSH PRIVILEGES;`

### Verify the database creation 

`SHOW DATABASES;`

### Use the database

`USE flask_data;`

### Create the table for submissions

`CREATE TABLE submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    country VARCHAR(50) NOT NULL,
    message TEXT NOT NULL,
    gender ENUM('M', 'F') NOT NULL,
    subjects TEXT,
    submission_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);`

### Exit MySQL 

`EXIT;`

