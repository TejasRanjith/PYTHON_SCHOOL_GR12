drop database automobile;
create database automobile;
use automobile;

create table car_den(
    ccode int primary key,
    cname varchar(25),
    company varchar(25),
    colour varchar(25),
    capacity int,
    charge int,
);
desc car_den;

insert into car_den values
(501,"A-Star","Suzuki","RED",3,140),
(502,"Innova","Toyota","WHITE",7,300),
(503,"Indigo","Tata","SILVER",3,120),
(509,"SX4","Suzuki","SILVER",4,200),
(510,"CClass","Mercedes","RED",4,450);
select * from car_den;

select * from car_den 
where colour = "SILVER";

select cname,company,capacity from car_den
order by capacity desc;

select distinct company from car_den;
select count(distinct company) from car_den;

select max(charge),min(charge) from car_den;

select cname from car_den
where capacity = 4;

select car_den.colour,count(*) from car_den
group by colour;

-- to add new column called 'tot_price' in table 'car_den' with formula 'charge*capacity'

ALTER TABLE car_den MODIFY tot_price int;