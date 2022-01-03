create database Company;
use Company
create table employee(
    Empno varchar(5) primary key,
    Name varchar(20),
    Dept varchar(20),
    Salary int);
desc employee;
insert into employee
values(1010,"AMIT","SALES",20000),
(1021,"NITIN" ,"IT",28000),
(1032,"JAMES","ACCOUNTS",16000),
(1014,"ABEL","IT",32000);
select * from employee;