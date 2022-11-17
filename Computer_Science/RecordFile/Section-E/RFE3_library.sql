drop database library;
create database library;
use library;

create table books(
    Book_Id char(5) primary key,
    Book_Name varchar(25),
    Author_Name varchar(25),
    Publishers varchar(20),
    Price int,
    Type varchar(20),
    Qty int
);
desc books;

create table issued(
    Book_Id char(5) primary key,
    Quantity_Issued int
);
desc issued;

insert into books values
("C0001","Fast Cook","Lata Kapoor","EPB",355,"Cookery",5),
("F0001","The Tears","William Hopkins","First Publ.",650,"Fiction",20),
("T0001","My First C++","Brian & Brooke","EPB",350,"Textbook",10),
("T0002","C++ Brainworks","A W Rossaine","TDH",350,"Textbook",15),
("F0002","Thunderbolts","Anna Roberts","First Publ.",750,"Fiction",50);
select * from books;

insert into issued values
("T0001", 4),
("C0001", 5),
("F0001", 2);
select * from issued;

select Book_Name,Author_Name,Price from books
where Publishers = "First Publ.";

select Book_Name from books
where Type = "Textbook";

select Book_Name,Price from books
order by Price;

update books
set Price = Price + 50
where Publishers = "EPB";

select issued.Book_Id,Book_Name,Quantity_Issued from books,issued
where books.Book_Id = issued.Book_Id;

