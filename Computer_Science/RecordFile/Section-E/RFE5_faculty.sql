drop database faculty;
create database faculty;
use faculty;

create table teacher(
    tid int primary key,
    name varchar(25),
    deptid int,
    age int,
    salary int,
    gender char(1)
);

insert into teacher values
(1,'JUGAL',103,34,12000,'M'),
(2,'SHARMILLA',101,31,20000,'F'),
(3,'SANDEEP',102,32,30000,'M'),
(4,'SANGEETA',101,35,40000,'F'),
(5,'RAKESH',102,42,25000,'M'),
(6,'SHYAM',101,50,15000,'M'),
(7,'SHIVA',103,44,9000,'M'),
(8,'SHILPA',102,33,20000,'F');

SELECT * FROM teacher;
SELECT * FROM posting;

create table posting(
    dept_id int primary key,
    department varchar(25),
    posting varchar(20)
);

insert into posting values
(101,'History','Agra'),
(102,'Mathematics','Raipur'),
(103,'ComputerScience','Delhi');

select department,count(tid) from teacher,posting 
where deptid=dept_id group by deptid;

select max(age),min(age) from teacher;

SELECT name,department,posting FROM teacher,posting 
WHERE posting='Delhi' AND deptid=dept_id;

SELECT name FROM teacher
WHERE name LIKE '%a';

SELECT name,department,posting,salary,gender FROM teacher,posting 
WHERE deptid = dept_id AND gender = 'M' AND salary < 25000;

SELECT gender,COUNT(gender) FROM teacher
GROUP BY gender;