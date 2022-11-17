drop database electricity;
create database electricity;
use electricity;

create table ebill(
    RR_NO varchar(3) primary key,
    con_name varchar(20),
    Date_Bill date,
    Unit int
);
desc ebill;

insert into ebill values
("A11","Jothika","2020-10-02",224),
("A12","Titas","2020-09-12",212),
("A13","Ankan","2020-09-24",232),
("A14","Deepak","2020-10-01",242),
("A15","Archana","2020-10-04",244);
select * from ebill;

alter table ebill
add(bill_amt decimal(10,2));
desc ebill;

update ebill
set bill_amt = 50+(4.5*Unit);
select * from ebill;

select con_name,bill_amt from ebill
where bill_amt>1000;

select min(Unit),max(Unit),sum(Unit),avg(unit) from ebill;

select * from ebill
where con_name like "A%";

select * from ebill
where month(Date_Bill) = "10";

select * from ebill
order by Date_Bill;
