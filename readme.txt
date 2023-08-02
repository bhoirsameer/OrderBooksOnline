To run the project first we have to setup for database( MySQL )
step 1:
       create database --->mydtabase    command (create database mydtabase;) 

Step 2:
       Now we have to create the database tables we can create the tables using 
       commands or by using importing script by php myadmin Use any 1 method from 
        Method 1:
            Run all this commands in MySQL
            A:create table library1(id int primary key auto_increment,name varchar(50),author varchar(50),price float,type varchar(50));
            B:create table cart1(cartid int primary key auto_increment,name varchar(50),author varchar(50),price float,email varchar(50),quantity int);
            C:create table admin1(username varchar(50),password varchar(50));
            D:create table reglogin1(id int primary key auto_increment,name varchar(50),email varchar(50),password varchar(50));
            E:create table orders1(oid int primary key auto_increment,book_name varchar(50),price float,email varchar(50),quantity int,ord_date varchar(50),total_amt float,id int);

        Method 2:
            import the given file(mydtabase.sql) in phpMyadmin in database  mydtabase.

Step 3:
       After creating tables insert username and password in admin1 table
       command --->   eg --->      insert into admin1 values("user","P@ss123");

Step 4:
       Now we have to login as a host by the username and password which we just insert in admin1 table 
       after login we have to add books in db add at least 4 to 5 books

Step 5:
       now run the code again and select customer option 