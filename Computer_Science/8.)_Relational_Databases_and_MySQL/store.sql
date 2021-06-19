drop database store;
create database store;
use store;
create table products(
    PID int(3) primary key,
    Pname varchar(25),
    Qty int,
    Price int,
    Company varchar(20),
    Supcode varchar(3)
);
desc products;
create table suppliers(
    Supcode varchar(3) primary key,
    Sname varchar(25),
    City varchar(20)
);
desc suppliers;
insert into products
values(101,"Digital Camera 14X", 120,12000,"Renix","S01"),
(102,"Digital Pad 11i",100,22000,"Digi POP","S02"),
(104,"Pen Drive 16 GB",500,1100,"Storeking","S01"),
(105,"Car GPS System",60,12000,"Moveon","S03"),
(106,"Led Screen 32",70,28000,"Dispexperts","S02");
select * from products;
insert into suppliers
values("S01","Get All Inc","Kolkata"),
("S03","Easy Market Corp","Delhi"),
("S02","Digi Busy Group","Chennai");
select * from suppliers;
update suppliers
set sname = "Get Digigtal"
where sname = "Get all inc";
select * from products
order by Pname;
select Pname,price from products
where price between 10000 and 15000;
select Pname,price,Qty from products
where Qty > 100;
select sname from suppliers
where City in ("Delhi","Chennai");
select Pname,Sname,City from products,suppliers
where products.Supcode = suppliers.Supcode and City = "Kolkata";
select PID,Pname,Sname,Price*Qty from suppliers,products
where products.Supcode = suppliers.Supcode and products.Supcode = "S02";
select sname,count(PID) from suppliers,products
group by products.Supcode;
