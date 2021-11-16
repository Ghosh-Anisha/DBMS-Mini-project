import streamlit as st
import psycopg2
from streamlit import cursor
from datetime import date

def createTableBooks():
    connection1 = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection1.autocommit = True
    cursor = connection1.cursor()

    sql = '''CREATE TABLE books(BookId int NOT NULL,
    Title varchar(300),
    CoverLink varchar(500),
    Author varchar(500),
    RatingCount int,
    Rating float,
    PublishingDate varchar(30),
    Publisher varchar(200),
    Genre varchar(200),
    ISBN varchar(14));'''

    cursor.execute(sql)

    connection1.commit()
    connection1.close()

def insertBooks():

    connection3 = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection3.autocommit = True
    cursor = connection3.cursor()

    sql2 = '''COPY books(BookId,Title,CoverLink,Author,RatingCount,Rating,PublishingDate,Publisher,Genre,ISBN)
    FROM '/Users/aanchalnarendran/Desktop/Books.csv'
    DELIMITER ','
    CSV HEADER;'''

    cursor.execute(sql2)
    connection3.commit()
    connection3.close()

def shopBooks():
    connection2 = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection2.autocommit = True
    cursor = connection2.cursor()

    sql4 = '''select * from books;'''
    cursor.execute(sql4)

    for i in cursor.fetchall():
        print(i)

    connection2.commit()
    connection2.close()

def createCart():
    connection1 = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection1.autocommit = True
    cursor = connection1.cursor()

    sql = '''CREATE TABLE cart(PhoneNum varchar(15) NOT NULL,
    isbn varchar(18),
    book_count int,
    price float);'''

    cursor.execute(sql)

    connection1.commit()
    connection1.close()

def insertIntoCart(cust_no,isbn):
    connection2 = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection2.autocommit = True
    cursor = connection2.cursor()

    sql4 = '''select rating from books where isbn = %s;'''
    cursor.execute(sql4,(isbn,))
    valuesCur = list(cursor.fetchall())
    price = valuesCur[0][0]*100 
    
    sql5 = '''select * from cart where phonenum = %s and isbn = %s; '''
    cursor.execute(sql5,(cust_no,isbn))
    cartVal = list(cursor.fetchall())
    
    if len(cartVal) == 0:
        curCount = 1
        sql6 = '''insert into cart values(%s,%s,%s,%s)'''
        cursor.execute(sql6,(cust_no,isbn,curCount,price))

    else:
        sql7 = '''update cart set book_count = book_count+1 , price=price+%s where phonenum=%s and isbn=%s'''
        cursor.execute(sql7,(price,cust_no,isbn))
    
    connection2.commit()
    connection2.close()

def createHistory():
    connection = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection.autocommit = True
    cursor = connection.cursor()

    sql = '''CREATE TABLE history(PhoneNum varchar(15) NOT NULL,
    date varchar(20),
    isbn varchar(18),
    book_count int,
    price float);'''

    cursor.execute(sql)

    connection.commit()
    connection.close()

def insertIntoHistory(phonenum,isbn,count,price):
    connection = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection.autocommit = True
    cursor = connection.cursor()

    curDate = date.today()
    sql = '''insert into history values(%s,%s,%s,%s,%s);'''
    cursor.execute(sql,(phonenum,curDate,isbn,count,price))

    connection.commit()
    connection.close()

def generateBill(cust_no):
    connection = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection.autocommit = True
    cursor = connection.cursor()

    #createBill
    sql = '''select * from cart where phonenum=%s;'''
    cursor.execute(sql,(cust_no,))
    listValues = cursor.fetchall()
    
    totalPrice = 0.0
    curDate = date.today()
    for i in range(len(listValues)):
        totalPrice+= listValues[i][-1]
        sql1 = '''insert into history values (%s,%s,%s,%s,%s);'''
        cursor.execute(sql1,(listValues[i][0],curDate,listValues[i][1],listValues[i][2],listValues[i][3]))

    sql3 = '''delete from cart where phonenum=%s;'''
    cursor.execute(sql3,(cust_no,))

    connection.commit()
    connection.close()
    return(listValues,totalPrice)

def addBook(bookid,title,coverlink,author,ratingcount,rating,publishingdate,publisher,genre,isbn):
    connection = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection.autocommit = True
    cursor = connection.cursor()

    sql = '''insert into books values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    cursor.execute(sql,(bookid,title,coverlink,author,ratingcount,rating,publishingdate,publisher,genre,isbn))

    connection.commit()
    connection.close()

def searchByTitle(title):
    connection = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection.autocommit = True
    cursor = connection.cursor()

    sql = '''select * from books where title=%s;'''
    cursor.execute(sql,(title,))

    for i in cursor.fetchall():
        print(i)

    connection.commit()
    connection.close()

def searchByAuthor(author):
    connection = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection.autocommit = True
    cursor = connection.cursor()

    sql = '''select * from books where author=%s;'''
    cursor.execute(sql,(author,))

    for i in cursor.fetchall():
        print(i)

    connection.commit()
    connection.close()

def searchByGenre(genre):
    connection = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection.autocommit = True
    cursor = connection.cursor()

    sql = '''select * from books where genre=%s;'''
    cursor.execute(sql,(genre,))

    for i in cursor.fetchall():
        print(i)

    connection.commit()
    connection.close()

def createRequest():
    connection = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection.autocommit = True
    cursor = connection.cursor()

    sql = '''CREATE TABLE request(PhoneNum varchar(15) NOT NULL,
    title varchar(300));'''

    cursor.execute(sql)

    connection.commit()
    connection.close()

def addRequest(cust_no,title):
    connection = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection.autocommit = True
    cursor = connection.cursor()

    sql = '''insert into request values(%s,%s);'''
    cursor.execute(sql,(cust_no,title))

    connection.commit()
    connection.close()

def createFeedback():
    connection = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection.autocommit = True
    cursor = connection.cursor()

    sql = '''CREATE TABLE feedback(PhoneNum varchar(15) NOT NULL,
    title varchar(300),
    feedback varchar(2000));'''

    cursor.execute(sql)

    connection.commit()
    connection.close()

def addFeedback(cust_no,title,feedback):
    connection = psycopg2.connect(database='ezbook',user='aanchalnarendran',host='127.0.0.1',port='5432')
    connection.autocommit = True
    cursor = connection.cursor()

    sql = '''insert into feedback values(%s,%s,%s);'''
    cursor.execute(sql,(cust_no,title,feedback))

    connection.commit()
    connection.close()

def buildDatabase(): #only execute once
	createTableBooks()
	insertBooks()
	createCart()
	createFeedback()
	createHistory()
	createRequest()


# Layout Templates
html_temp = """
<div style="background-color:{};padding:10px;border-radius:10px">
<h1 style="color:{};text-align:center;">EzBook </h1>
</div>
"""
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366%22);
background-size: cover;
}
</style>
'''
title_temp ="""
<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h1>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
<h6>Author:{}</h6>
<br/>
<br/> 
<p style="text-align:justify">{}</p>
</div>
"""
article_temp ="""
<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h1>
<h6>Author:{}</h6> 
<h6>Post Date: {}</h6>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;" >
<br/>
<br/>
<p style="text-align:justify">{}</p>
</div>
"""
head_message_temp ="""
<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h1>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
<h6>Author:{}</h6> 
<h6>Price: {}</h6> 
<h6>Date of publication: {}</h6> 
<h6>Genre: {}</h6> 
<h6>Rating: {}</h6> 
<h6>ISBN: {}</h6> 
</div>
"""
full_message_temp ="""
<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
<p style="text-align:justify;color:black;padding:10px">{}</p>
</div>
"""


st.markdown(html_temp.format('rgb(0,139,139)','white'),unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,1,1])
col2.image("logo1.jpg", use_column_width=True, width = 400)

# st.image("logo1.jpg", width=400)

menu = ["Home","Shop Library","Add books (only Admin)","Search Books","Request Books","Feedback"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
	#Button Formatting 
	st.text(" ") 

	m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(0,206,209);
    color:black;
}

</style>""", unsafe_allow_html=True)


	if st.button("Home"):
		choice = "Home"
	if st.button("Shop Library"):
		choice = "Shop Library"
	if st.button("Add Books"):
		choice = "Add Books"
	if st.button("Search Books"):
		choice = "Search Books"
	if st.button("Request Books"):
		choice = "Request Books"
	if st.button("Feedback"):
		choice = "Feedback"



if choice == "Home":
	st.text('Welcome to EzBook - An Online Book Store')

if choice == "Shop Library":
	st.subheader("Shop Library")
	all_titles = [i[0] for i in shopBooks()]
	postlist = st.sidebar.selectbox("View Books",all_titles)
	post_result = shopBooks(postlist)
	for i in post_result: #bookid,title,coverlink,author,ratingcount,rating,publishingdate,publisher,genre,isbn
		b_id = i[0]
		b_title = i[1]
		b_coverlink=i[2]
		b_author=i[3]
		b_rating_count = i[4]
		b_rating = i[5]
		b_date_of_publication=i[6]
		b_publisher=i[7]
		b_genre=i[8]
		b_isbn=i[9]
		st.markdown(head_message_temp.format(b_id, b_title , b_coverlink, b_author ,b_rating_count , b_rating , b_date_of_publication , b_publisher , b_genre , b_isbn),unsafe_allow_html=True)
		if st.button("Add to cart"):
			cust_no=st.text_input("Enter Contact no")
			insertIntoCart(cust_no,b_isbn) 
		if st.button("Checkout"):
			cust_name=st.text_input("Enter Name")
			cust_no=st.text_input("Enter Contact no")
			cust_addr=st.text_area("Enter address")
			amount=generateBill(cust_no,cust_name,cust_addr) 
			st.success("Total amount: {}".format(amount))

if choice == "Add Books":
    st.subheader("Add Books")
    #create_table()
	# pwd=st.text_input("Enter Passsword:",type="password")
	# if st.button("Login"):
	# 	if(pwd=="admin1234"):
			# st.subheader("Add Books")
    b_id = st.text_input("Enter book_id")
    b_title = st.text_input("Enter Book Title")
    b_coverlink=st.text_input("Enter coberlink")
    b_author=st.text_input("Enter Author")
    b_rating_count = st.text_input("Enter Rating Count")
    b_rating = st.text_input("Enter Rating")
    b_date_of_publication=st.text_input("Enter Date of Publication")
    b_publisher=st.text_input("Enter Publisher")
    b_genre=st.text_input("Enter Genre")
    b_isbn=st.text_input("ISBN")
    if st.button("Add"):	
        addBook(b_id, b_title , b_coverlink, b_author ,b_rating_count , b_rating , b_date_of_publication , b_publisher , b_genre , b_isbn)
        st.success("Post:{} saved".format(b_title))	
		# else:
		# 	st.text("ACCESS DENIED")




if choice == "Search Books":
	st.subheader("Search Books")
	search_term = st.text_input('Enter Search Term')
	search_choice = st.radio("Field to Search By",("title","author","genre"))
	
	if st.button("Search"):

		if search_choice == "title":
			article_result = searchByTitle(search_term) 
		elif search_choice == "author":
			article_result = searchByAuthor(search_term) 
		elif search_choice=="genre":
			article_result = searchByGenre(search_term) 


		for i in article_result:
			b_author = i[0]
			b_title = i[1]
			b_price = i[2]
			b_date_of_publication = i[3]
			b_rating=i[4]
			b_genre=i[5]
			b_isbn=i[6]
			st.markdown(head_message_temp.format(b_title,b_author,b_price,b_date_of_publication,b_genre,b_rating,b_isbn),unsafe_allow_html=True)
	
			if st.button("Add to cart"):
				cust_no=st.text_input("Enter Contact no")
				insertIntoCart(cust_no,b_isbn) 
			if st.button("Checkout"):
				cust_name=st.text_input("Enter Name")
				cust_no=st.text_input("Enter Contact no")
				cust_addr=st.text_area("Enter address")
				amount=generateBill(cust_no,cust_name,cust_addr) 
				st.success("Total amount: {}".format(amount))




if choice == "Request Books":
	st.subheader("Request Books")
	book_name = st.text_input("Enter Book Name")
	cust_no=st.text_input("Enter Contact no")
	if st.button("Add"):
		addRequest(cust_no,book_name) 
		st.success("Post:{} saved".format(book_name))	


if choice == "Feedback":
	st.subheader("Feedback")
	cust_no = st.text_input("Enter contact no")
	book_name = st.text_input("Enter Book Name")
	feedback = st.text_area('Enter Feedback')
	if st.button("Add"):
		addFeedback(cust_no,book_name,feedback) 
		st.success("Post:{} saved".format(feedback))