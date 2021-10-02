drop database ezbook;
create database ezbook;

\c ezbook

create table Books (
	ISBN VARCHAR(10) NOT NULL,
	BookID INT,
	BName VARCHAR,
	Genre VARCHAR(100),
	Author VARCHAR,
	PublishingYear int,
	Price DECIMAL(7,2),
	Rating DECIMAL(3,1),
	PRIMARY KEY (ISBN)
);

create table PublisherDetails (
	BookID int,
	PublisherName VARCHAR,
	PRIMARY KEY (BookID,PublisherName)
);

