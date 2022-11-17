DROP DATABASE revision;
CREATE DATABASE revision;
USE revision;
-- .b                                   REVISON : SQL - 1
CREATE TABLE furniture (
    fid CHAR(4) PRIMARY KEY,
    name VARCHAR(20),
    dateofpurchase DATE,
    cost INT,
    discount INT
);
DESC furniture;

INSERT INTO furniture VALUES
("BOO1","Double Bed",'2018-01-03',45000,10),
("TO10","Dining Table",'2020-03-10',51000,5),
("BOO4","Single Bed",'2021-07-19',22000,0),
("CO03","Long Back Chair",'2016-12-30',12000,3),
("TO06","Console Table",'2019-11-17',15000,12),
("BO06","Bunk Bed",'2021-01-01',28000,14);
SELECT * FROM furniture;

SELECT SUM(discount) FROM furniture
WHERE cost > 15000;

SELECT MAX(dateofpurchase) FROM furniture;

SELECT * FROM furniture
WHERE discount > 5 AND fid LIKE "T%";

SELECT dateofpurchase FROM furniture
WHERE name in ("Dining Table","Console Table");

-- .b                                  REVISON : SQL - 2

CREATE Table employee(
    empid INT PRIMARY KEY,
    name VARCHAR(20),
    DOB DATE,
    deptid CHAR(4),
    desig VARCHAR(20),
    salary INT
);
DESC employee;

CREATE Table department(
    deptid CHAR(4) PRIMARY KEY,
    deptname VARCHAR(20),
    floorno INT
);
DESC department;

INSERT INTO employee VALUES
(120,"Alisha",'1978-01-23','D001','Manager',25000),
(123,"Nitin","1977-10-10","D002","AO",59000),
(129,"Navjot","1971-07-12","D003","Supervisor",40000),
(130,"Jimmy","1980-12-30","D004","Sales Rep",NULL),
(131,"Faiz","1984-04-06","D001","Dep Manager",65000);
SELECT * FROM employee;

INSERT INTO department VALUES
('D001','Personal',4),
('D004','Sales',3),
('D003','Production',1),
('D002','Admin',10);
SELECT * FROM department;

DROP TABLE department;

SELECT AVG(salary) FROM employee GROUP BY deptid;

SELECT name,deptname FROM employee,department
WHERE employee.deptid = department.deptid AND salary > 50000;

SELECT name FROM employee
WHERE salary IS NULL;

SELECT distinct deptid FROM employee;

--.b                                  REVISON : SQL - 3

CREATE Table loans(
    accno INT PRIMARY KEY,
    cust_name VARCHAR(20),
    loan_amount INT,
    instalments INT,
    int_Rate FLOAT,
    start_date DATE,
    interest INT
);

INSERT INTO loans VALUES
(1,"R K GUPTA",300000,36,12.00,'2009-07-19',1200),
(2,"S P SHARMA",500000,48,10.00,'2008-03-22',1800),
(3,"K P JAIN",300000,36,NULL,'2007-03-08',1600),
(4,"M P YADAV",800000,60,10.00,'2010-12-06',2250),
(5,"S P SINHA",200000,36,12.50,'2008-01-03',4500),
(6,"P SHARMA",700000,60,12.50,'2008-06-05',3500),
(7,"K S DHALL",500000,48,NULL,'2008-06-05',3800);
SELECT * FROM loans;


-- Display the sum of all Loan Amount whose Interest rate is greater than 10.

SELECT SUM(loan_amount) FROM loans
WHERE int_Rate > 10;

-- Display the Maximum Interest from Loans Table.

SELECT MAX(interest) FROM loans;

-- Display the count of all loan holders whose name ends with ‘Sharma’.

SELECT COUNT(cust_name) FROM loans
WHERE cust_name LIKE '%Sharma';

-- Display the count of all loan holders whose Interest is NULL.

SELECT COUNT(interest) FROM loans
WHERE interest IS NULL;

-- Display the interest-wise details of Loan Account Holders.

SELECT cust_name,loan_amount,interest FROM loans
GROUP BY interest;

-- Display the Interest-wise details of Loan Account Holders with at least 10 instalments remaining.

SELECT cust_name,loan_amount,interest FROM loans
WHERE instalments > 10 GROUP BY interest;

-- Display the Interest-wise count of all loan holders whose instalment due is more than 5 in each group.

SELECT cust_name,loan_amount,interest FROM loans
WHERE instalments > 5 GROUP BY interest;

--.y ???????????????????????????????????????????????????????

-- Display the names of all Cust_Name ending with ‘a’

SELECT cust_name FROM loans
WHERE cust_name LIKE '%a';


--.b                                  REVISON : SQL - 4


CREATE Table trains(
    tno INT PRIMARY KEY,
    tname VARCHAR(20),
    start VARCHAR(20),
    end VARCHAR(20)
);
--TNO : 11096,12015,1651,13005,12002,12417,14673,12314,12498,12451,12030
--TNAME :Ahimsa Express ,Ajmer Shatabdi ,Pune Hbj Special ,Amritsar Mail ,Bhopal Shatabdi ,Prayag Raj Express ,Shaheed Express ,Sealdah Rajdhani ,Shane Punjab ,Shram Shakti Express ,Swarna Shatabdi 
--START : Pune Junction ,New Delhi ,Pune Junction ,Howrah Junction ,New Delhi ,Allahabad Junction ,Jaynagar ,New Delhi ,Amritsar Junction ,Kanpur Central ,Amritsar Junction
--END : Ahmedabad Junction ,Ajmer Junction ,Habibganj ,Amritsar Junction ,Habibganj ,New Delhi ,Amritsar Junction ,Sealdah ,New Delhi ,New Delhi ,New Delhi 

CREATE TABLE trains(
    tno INT PRIMARY KEY,
    tname VARCHAR(20),
    start VARCHAR(20),
    end VARCHAR(20)
);

INSERT INTO