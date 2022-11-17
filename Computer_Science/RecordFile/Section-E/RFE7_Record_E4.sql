DROP DATABASE record_e4;
CREATE DATABASE record_e4;
USE record_e4;

CREATE Table student(
    rollno INTEGER PRIMARY KEY,
    name VARCHAR(20),
    percentage DECIMAL(4,1),
    section CHAR(1),
    assignment VARCHAR(15)
);
DESC student;

INSERT INTO student VALUES
(103,'Ruhani',76.8 ,'A',"Pending"),
(104,'George',71.2 ,'A',"Submitted"),
(105,'Simran',81.2 ,'B',"Evaluated"),
(107,'Ahmed',61.2 ,'C',"Pending"),
(108,'Raunak',32.5 ,'B',"Submitted");
SELECT * FROM student;

SELECT * FROM employee WHERE empno=1032;