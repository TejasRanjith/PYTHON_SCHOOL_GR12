create database assignment;
use assignment;
create table Student(
    RollNo int primary key,
    Name varchar(20),
    Percentage decimal(4,1),
    Section char(1),
    Assignment varchar(15)
);
insert into Student
values(103,"Ruhani",76.8,"A","Pending"),
(104,"George",71.2,"A","Submitted"),
(105,"Simran",81.2,"B","Evaluated"),
(107,"Ahmed",61.2,"C","Pending"),
(108,"Raunak",32.5,"B","Submitted");
select * from Student;
