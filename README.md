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

## Setting up the python app

### Install dependencies

`pip install -r dependencies.txt`

### Insert your db credentials

Modify the code of app.py to make the app use your own database :

```
# MySQL configuration

db = mysql.connector.connect(

host="localhost",

user="DB_USERNAME", # Replace with your MySQL username

password="DB_PASSWORD", # Replace with your MySQL password

database="flask_data" # Replace with your MySQL database name

)
```

### Run the app

`python app.py`

Visit : http://127.0.0.1:5000/ to access the app.

### Verify your data 

Verify if the data you submitted is in your database : 

`mysql -u username -p flask_data`

`SELECT * FROM flask_data;`

 The data should be stored there ! 