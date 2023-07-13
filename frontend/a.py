import streamlit as st
import mysql.connector
from PIL import Image

from bike import bike
from bike_category import bike_category
from sqlcommand import command
from discount import discount
from location import location
from user import user

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
	database="abc"
)
c = mydb.cursor()

def main():
    image = Image.open('b2.png')

    st.image(image,width=230)
    st.title("Bike Rental Management System")
    menu = ["User","Bike","Bike Category","Discount","Location","sql command"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice=="Bike":
       bike()
    elif choice=="Bike Category":
        bike_category()

    elif choice=="Discount":
        discount()

    elif choice=="Location":
       location()
        
    # elif choice=="customer":
    elif choice=="sql command":
        command()

    elif choice=="User":
        user()



if __name__ == '__main__':
    main()

