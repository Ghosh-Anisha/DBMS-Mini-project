drop database ezbook;
create database ezbook;

\c ezbook

create table Books (
	ISBN VARCHAR(10) NOT NULL UNIQUE,
	BookID VARCHAR UNIQUE,
	BName VARCHAR,
	Genre VARCHAR(100),
	Author VARCHAR,
	PublishingYear int,
	Price DECIMAL(7,2),
	Rating DECIMAL(3,1),
	PRIMARY KEY (ISBN)
); --imputed

create table PublicationHouse (
	BookID VARCHAR unique not null references Books(BookID),
	Publication_House VARCHAR not null,
	ISBN VARCHAR(10) NOT NULL UNIQUE,
	PRIMARY KEY (ISBN) --imputed
);

create table Produces(
	ProducedBookID VARCHAR references Books(BookID),
	PublicationISBN VARCHAR references PublicationHouse(ISBN),
	PRIMARY KEY(ProducedBookID,PublicationISBN) --imputed
);

create table Customer(
	CustomerID INT PRIMARY KEY,
	CustName VARCHAR(20),
	CustNumber VARCHAR(10),
	EmailID VARCHAR(40)
); --imputed

create table RequestForBooks(
	RequestID INT,
	Book_title VARCHAR,
	CustomerID INT references Customer(CustomerID),
	PRIMARY KEY(RequestID)
); --imputed 

create table Buys(
	CustomerID INT not null references Customer(CustomerID),
	ISBN VARCHAR(10) references Books(ISBN),
	PurchaseId INT UNIQUE,
	PRIMARY KEY(PurchaseId)
); --imputed

create table CustomerFeedback(
	CustomerID INT references Customer(CustomerID),
	CustDesc VARCHAR,
	ISBN VARCHAR(10) references Books(ISBN),
	PRIMARY KEY(CustomerID, ISBN)
); --imputed

create table Cart(
	CustomerID INT references Customer(CustomerID),
	CartID INT unique ,
	BookID VARCHAR references Books(BookID),
	Book_Count INT,
	PRIMARY KEY (CartID)
); --imputed

create table Bills(
	BillNumber INT PRIMARY KEY,
	CartID INT references Cart(CartID),
	BillDate DATE,
	TotalAmount DECIMAL(15,2),
	ModeOfPayment VARCHAR
); --imputed

create table BestSellers(
	BillNumber INT references Bills(BillNumber),
	PurchaseId int references Buys(PurchaseId),
	PRIMARY KEY (BillNumber, PurchaseId)
); --imputed

create table CountBooks(
	BillNumber INT references Bills(BillNumber),
	ISBN VARCHAR(10) references Books(ISBN)
); --imputed 

