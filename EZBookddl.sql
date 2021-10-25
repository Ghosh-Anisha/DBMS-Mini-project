drop database ezbook;
create database ezbook;

\c ezbook

create table Books (
	ISBN VARCHAR(10) NOT NULL UNIQUE,
	BookID INT UNIQUE,
	BName VARCHAR,
	Genre VARCHAR(100),
	Author VARCHAR,
	PublishingYear int,
	Price DECIMAL(7,2),
	Rating DECIMAL(3,1),
	PRIMARY KEY (ISBN, BookID)
);

create table PublicationHouse (
	BookID int unique references Books(BookID),
	Publication_House VARCHAR,
	ISBN VARCHAR(10) references Books(ISBN),
	PRIMARY KEY (BookID,Publication_House)
);

create table Produces(
	ISBN VARCHAR(10) references Books(ISBN),
	Publication_House VARCHAR references PublicationHouse(Publication_House),
	PRIMARY KEY(ISBN,Publication_House)
);

create table Customer(
	CustomerID INT PRIMARY KEY,
	CustName VARCHAR(20),
	CustNumber INT,
	EmailID VARCHAR(40)
);

create table RequestForBooks(
	RequestID INT,
	Book_title VARCHAR,
	CustomerID INT references Customer(CustomerID),
	ISBN VARCHAR(10) references Books(ISBN),
	PRIMARY KEY(RequestID, CustomerID)
);

create table Buys(
	CustomerID references Customer(CustomerID),
	ISBN VARCHAR(10) references Books(ISBN),
	PRIMARY KEY(CustomerID, ISBN)
);

create table CustomerFeedback(
	CustomerID references Customer(CustomerID),
	CustDesc VARCHAR,
	ISBN VARCHAR(10) references Books(ISBN),
	PRIMARY KEY(CustomerID, ISBN)
);

create table Cart(
	CustomerID references Customer(CustomerID),
	CartID INT PRIMARY KEY,
	BookID INT references Books(BookID),
	Book_Count INT
);

create table Bills(
	BillNumber INT PRIMARY KEY,
	CartID INT references Cart(CartID),
	BillDate DATE,
	TotalAmount DECIMAL(15,2),
	ModeOfPayment VARCHAR
);

create table BestSellers(
	BillNumber INT references Bills(BillNumber),
	ISBN VARCHAR(10) references Buys(ISBN),
	PRIMARY KEY (BillNumber, ISBN)
);

create table CountBooks(
	BillNumber INT references Bills(BillNumber),
	ISBN VARCHAR(10) references Books(ISBN) PRIMARY KEY
);

