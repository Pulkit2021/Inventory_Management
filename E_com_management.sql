create database E_Store;
use E_store;
create table Category (
CategoryID int primary key auto_increment,
CategoryName varchar(50) not null
);


create table Customer (
CustomerID int primary key auto_increment,
CustomerName varchar(30) not null,
Address varchar(50) not null,
Email varchar(30),
Phone int);


create table Orders(
OrderID int primary key auto_increment,
OrderDate date not null,
CustomerID int,
foreign key(CustomerID) references Customer(CustomerID));

create table Product(
ProductID int primary key auto_increment,
ProductName varchar(40),
Price int not null,
CategoryID int,
foreign key(CategoryID) references Category(CategoryID));

create table Order_item(
Order_ItemID int primary key auto_increment,
Quantity int not null,
ProductID int,
OrderID int,
Price int not null,
FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
FOREIGN KEY (OrderID) REFERENCES Orders(OrderID));


select * from Product;
select * from Order_item;
select * from Orders;
select * from Category;
select * from Customer;
