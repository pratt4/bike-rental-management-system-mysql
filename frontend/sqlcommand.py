# Core Pkgs
import streamlit as st 
import pandas as pd
import mysql
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="abc")
if mydb:
	print("success")
else:
	print("fail")


c=mydb.cursor()


# Fxn Make Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	if(raw_code[0]=="s" or "S"):
		data = c.fetchall()
		return data
		
	else:
		mydb.commit()
		print("success")
		
def command():

	
	st.title("bikerental query box")

	menu = ["Query Box","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Query Box":
		st.subheader("Query Box")

		# Columns/Layout
		col1,col2 = st.columns(2)

		with col1:
			with st.form(key='query_form'):
				raw_code = st.text_area("SQL Code Here")
				submit_code = st.form_submit_button("Execute")

			# Table of Info

			# with st.expander("Table Info"):
			# 	table_info = {'city':city,'country':country,'countrylanguage':countrylanguage}
			# 	st.json(table_info)
			
		# Results Layouts
		with col2:
			if submit_code:
				st.info("Query Submitted")
				st.code(raw_code)

				# Results 
				query_results = sql_executor(raw_code)
				with st.expander("Results"):
					st.write(query_results)

				with st.expander("Pretty Table"):
					query_df = pd.DataFrame(query_results)
					st.dataframe(query_df)


	else:
		st.subheader("About")
		st.text("This project is designed so as to be used by Bike Rental Company specializing \nin rentingbikes to customers. It is an online system through which customers can \nview availablebikes, register, view profile and book bike")








