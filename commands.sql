--given the customer ID , find the title of the books bought 
--given the ISBN , find books not bought by any customer
--given the ISBN , obtain customer feedback for books not in bestsellers
--given customer ID , see the requested books for a user and obtain the author name and genre
--number of books produced by each pub. house
--find the oldest book 
--select all books with rating > 3
--find the lowest rated book

SELECT C.CustomerId , B.bname 
FROM BUYS C , BOOKS B WHERE C.isbn = B.isbn;

SELECT isbn , bname , price , rating FROM BOOKS
WHERE isbn not in ( 
SELECT isbn FROM BUYS);

SELECT CustDesc,isbn FROM CUSTOMERFEEDBACK
WHERE isbn not in (
SELECT isbn from BestSellers);

SELECT PublicationISBN FROM PRODUCES 
WHERE PublicationISBN not in 
(
	SELECT isbn FROM BOOKS
);

SELECT COUNT(ISBN) 
FROM PublicationHouse 
GROUP BY Publication_House;

SELECT * FROM BOOKS WHERE PublishingYear in 
(
	SELECT MIN(PublishingYear)
	FROM BOOKS
);

SELECT * FROM BOOKS WHERE rating>3;

SELECT * FROM BOOKS WHERE rating in 
(
	SELECT MIN(rating)
	FROM BOOKS
);
