import streamlit as st

# DB
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()



def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT,title TEXT,article TEXT,postdate DATE)')

def add_data(author,title,article,postdate):
	c.execute('INSERT INTO blogtable(author,title,article,postdate) VALUES (?,?,?,?)',(author,title,article,postdate))
	conn.commit()

def view_all_notes():
	c.execute('SELECT * FROM blogtable')
	data = c.fetchall()
	return data

def view_all_titles():
	c.execute('SELECT DISTINCT title FROM blogtable')
	data = c.fetchall()
	return data


def get_blog_by_title(title):
	c.execute('SELECT * FROM blogtable WHERE title="{}"'.format(title))
	data = c.fetchall()
	return data
def get_blog_by_author(author):
	c.execute('SELECT * FROM blogtable WHERE author="{}"'.format(author))
	data = c.fetchall()
	return data

def delete_data(title):
	c.execute('DELETE FROM blogtable WHERE title="{}"'.format(title))
	conn.commit()


# Layout Templates
html_temp = """
<div style="background-color:{};padding:10px;border-radius:10px">
<h1 style="color:{};text-align:center;">EzBook </h1>
</div>
"""
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



st.markdown(html_temp.format('DarkMagenta','white'),unsafe_allow_html=True)

menu = ["Home","Shop Library","Add books (only Admin)","Search Books","Request Books","Feedback"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
	st.text(" ")
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
	all_titles = [i[0] for i in view_all_titles()]
	postlist = st.sidebar.selectbox("View Books",all_titles)
	post_result = get_blog_by_title(postlist)
	for i in post_result:
		b_author = i[0]
		b_title = i[1]
		b_price = i[2]
		b_date_of_publication = i[3]
		b_rating=i[4]
		b_genre=i[5]
		b_isbn=i[6]
		#st.text("Reading Time:{}".format(readingTime(b_article)))
		st.markdown(head_message_temp.format(b_title,b_author,b_price,b_date_of_publication,b_genre,b_rating,b_isbn),unsafe_allow_html=True)
		#st.markdown(full_message_temp.format(b_article),unsafe_allow_html=True)
		if st.button("Add to cart"):
			cust_no=st.text_input("Enter Contact no")
			add_to_cart(cust_no,b_isbn)
		if st.button("Checkout"):
			cust_name=st.text_input("Enter Name")
			cust_no=st.text_input("Enter Contact no")
			cust_addr=st.text_area("Enter address")
			amount=billing(cust_no,cust_name,cust_addr)
			st.success("Total amount: {}".format(amount))

if choice == "Add Books":
	st.subheader("Add Books")
	create_table()
	# pwd=st.text_input("Enter Passsword:",type="password")
	# if st.button("Login"):
	# 	if(pwd=="admin1234"):
			# st.subheader("Add Books")
	blog_author = st.text_input("Enter Author Name",max_chars=50)
	blog_title = st.text_input("Enter Book Title")
	blog_price = st.text_input("Enter Price")
	blog_rating=st.text_input("Enter Rating")
	blog_date_of_publication=st.date_input("Enter Date of Publication")
	blog_genre=st.text_input("Enter Genre")
	blog_isbn = st.text_input("ISBN")
	if st.button("Add"):
		add_data(blog_author,blog_title,blog_price,blog_rating,blog_date_of_publication,blog_genre,blog_isbn)
		st.success("Post:{} saved".format(blog_title))	
		# else:
		# 	st.text("ACCESS DENIED")




if choice == "Search Books":
	st.subheader("Search Books")
	search_term = st.text_input('Enter Search Term')
	search_choice = st.radio("Field to Search By",("title","author","genre"))
	
	if st.button("Search"):

		if search_choice == "title":
			article_result = get_blog_by_title(search_term)
		elif search_choice == "author":
			article_result = get_blog_by_author(search_term)
		elif search_choice=="genre":
			article_result = get_blog_by_genre(search_term)


		for i in article_result:
			b_author = i[0]
			b_title = i[1]
			b_price = i[2]
			b_date_of_publication = i[3]
			b_rating=i[4]
			b_genre=i[5]
			b_isbn=i[6]
			#st.text("Reading Time:{}".format(readingTime(b_article)))
			#st.markdown(head_message_temp.format(b_title,b_author,b_post_date),unsafe_allow_html=True)
			st.markdown(head_message_temp.format(b_title,b_author,b_price,b_date_of_publication,b_genre,b_rating,b_isbn),unsafe_allow_html=True)
		#st.markdown(full_message_temp.format(b_article),unsafe_allow_html=True)
			if st.button("Add to cart"):
				cust_no=st.text_input("Enter Contact no")
				add_to_cart(cust_no,b_isbn)
			if st.button("Checkout"):
				cust_name=st.text_input("Enter Name")
				cust_no=st.text_input("Enter Contact no")
				cust_addr=st.text_area("Enter address")
				amount=billing(cust_no,cust_name,cust_addr)
				st.success("Total amount: {}".format(amount))
			#st.markdown(full_message_temp.format(b_article),unsafe_allow_html=True)




if choice == "Request Books":
	st.subheader("Request Books")
	book_name = st.text_input("Enter Book Name")
	cust_no=st.text_input("Enter Contact no")
	if st.button("Add"):
		request_for_books(cust_no,book_name)
		st.success("Post:{} saved".format(book_name))	


if choice == "Feedback":
	st.subheader("Feedback")
	cust_no = st.text_input("Enter contact no")
	book_name = st.text_input("Enter Book Name")
	feedback = st.text_area('Enter Feedback')
	if st.button("Add"):
		add_feedback(cust_no,book_name,feedback)
		st.success("Post:{} saved".format(feedback))


