USE DB;
create table airline(flightNo int(5) primary key,
departure varchar(15),
destination varchar(15),
amount int (8), seats int(5));

insert into airline(flightNo,departure,destination,amount,seats)
 values(103,"UAE","CANADA",20000,30);
 
 SELECT * FROM airline
 
 update airline 
 set seats =3
 where flightNo = 101;
 
 