-- .b creating table student in school.

use school;
create table student
(no int primary key,
stname varchar(25),
age int,
dept varchar(20),
doa date,
fee int,
gender char(1));

-- .r inserting values into the table student.

use school;
delete from student where no = 6 or no = 7;
insert into student
values(1,"Abel",16,"Science","2019-10-01",275,"M");
insert into student
values(2,"Zerin",17,"Commerce","2020-03-24",250,"F");
insert into student
values(3,"Clara",16,"Commerce","2019-12-12",250,"F");
insert into student
values(4,"Faraz",16,"Science","2019-01-07",275,"M");
insert into student
values(5,"Diana",17,"Commerce","2020-05-09",250,"F");

-- .y verifying like operation.

use school;
select * from student where stname like "%A%";

-- .g verifying between operator.

use school;
select * from student where
fee between 250 and 300;
-- .b updating the table.
use school;
update student set fee = fee+10 where fee = 255;
select * from student;

-- .b verifying greater than, less than operators.

use school;
select * from student
where fee>250 and fee<300;

-- .r verifying sort method.

use school;
select * from student
order by no;

-- .y verifying DESC sort method.

use school;
select * from student
order by no DESC;

--.g verifying the selection using month

use school;
select * from student
where month(doa) = 5;

--.b verifying the selection using year

use school;
select * from student
where year(doa) = 2020;

--.r verifying the selection using range of date

use school;
select * from student
where doa between '2019-01-01' and '2019-12-31';

--.y verifying the deletion of contents using DELETE.

