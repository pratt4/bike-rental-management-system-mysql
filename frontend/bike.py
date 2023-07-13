import streamlit as st
import pandas as pd
from functiondb import *
import streamlit.components.v1 as stc


HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">DBMS PROJECT</h1>
    <p style="color:white;text-align:center;">PES1UG20CS577</p>
    </div>
    """

def bike():
  stc.html(HTML_BANNER)
  menu = ["Create", "Read", "Update", "Delete"]
  choice = st.sidebar.selectbox("Menu", menu)

  if choice == "Create":
    st.subheader("Add Item")
    col1,col2 = st.columns(2)
    with col1:
      REGISTRATION_NUMBER = st.number_input("REGISTRATION_NUMBER")
      MODEL_NAME=st.text_input("MODEL_NAME")
      MAKE=st.text_input("MAKE")
      MODEL_YEAR=st.number_input("MODEL_YEAR")
      MILEAGE=st.number_input("MILEAGE")
      BIKE_CATEGORY_NAME=st.text_input("BIKE_CATEGORY_NAME")
      LOC_ID=st.number_input("LOC_ID")
      AVAILABILITY_FLAG = st.radio("AVAILABILITY_FLAG",["Yes", "No"])

      # BIKE_AGE

    if st.button("submit"):
          add_data_bike(REGISTRATION_NUMBER,MODEL_NAME ,MAKE ,MODEL_YEAR ,MILEAGE ,BIKE_CATEGORY_NAME ,LOC_ID ,AVAILABILITY_FLAG)
          st.success("Added ::{} ::To bike".format(REGISTRATION_NUMBER))

  elif choice == "Read":
    st.subheader("View Items")
    with st.expander("View All"):
      result = view_all_bike()
      #st.write(result)
      clean_df = pd.DataFrame(result,columns=['REGISTRATION_NUMBER','MODEL_NAME' ,'MAKE' ,'MODEL_YEAR' ,'MILEAGE' ,'BIKE_CATEGORY_NAME' ,'LOC_ID' ,'AVAILABILITY_FLAG'])
      st.dataframe(clean_df)

  elif choice == "Update":
    st.subheader("Edit Items")
    with st.expander("Current Data"):
      result = view_all_bike()
      # st.write(result)
      clean_df = pd.DataFrame(result,columns=['REGISTRATION_NUMBER','MODEL_NAME' ,'MAKE' ,'MODEL_YEAR' ,'MILEAGE' ,'BIKE_CATEGORY_NAME' ,'LOC_ID' ,'AVAILABILITY_FLAG'])
      st.dataframe(clean_df)

    list_of_regno = [i[0] for i in view_all_regno()]
    selected_favorite_id = st.selectbox("regno",list_of_regno)
    regno_result = get_regno(selected_favorite_id)
		

    if regno_result:
      REGISTRATION_NUMBER = regno_result[0][0]
      MODEL_NAME =regno_result[0][1]
      MAKE = regno_result[0][2]
      MODEL_YEAR=regno_result[0][3]
      MILEAGE=regno_result[0][4]
      BIKE_CATEGORY_NAME=regno_result[0][5]
      LOC_ID=regno_result[0][6]
      AVAILABILITY_FLAG=regno_result[0][7]
      


      col1,col2 = st.columns(2)
      
      with col1:
        new_id = st.text_input("regno", REGISTRATION_NUMBER)

      with col2:
        new_MODEL_NAME = st.text_input("MODEL_NAME",MODEL_NAME)
        new_MAKE=st.text_input("MAKE", MAKE)
        new_MODEL_YEAR=st.number_input("MODEL_YEAR",MODEL_YEAR)
        new_MILEAGE=st.number_input("MILEAGE",MILEAGE)
        new_BIKE_CATEGORY_NAME=st.text_input("BIKE_CATEGORY_NAME",BIKE_CATEGORY_NAME)
        new_LOC_ID=st.text_input("LOC_ID",LOC_ID)
        new_AVAILABILITY_FLAG=st.radio("AVAILABILITY_FLAG",["Yes", "No"])

      if st.button("Update Task"):
        edit_bike_data(new_id,new_MODEL_NAME,new_MAKE,new_MODEL_YEAR,new_MILEAGE,new_BIKE_CATEGORY_NAME,new_LOC_ID,new_AVAILABILITY_FLAG , REGISTRATION_NUMBER,MODEL_NAME,MAKE,MODEL_YEAR,MILEAGE,BIKE_CATEGORY_NAME,LOC_ID,AVAILABILITY_FLAG)
        st.success("updated {} To bike".format(REGISTRATION_NUMBER))
       

      with st.expander("View Updated Data"):
        result = view_all_bike()
        # st.write(result)
        clean_df = pd.DataFrame(result,columns=['REGISTRATION_NUMBER','MODEL_NAME' ,'MAKE' ,'MODEL_YEAR' ,'MILEAGE' ,'BIKE_CATEGORY_NAME' ,'LOC_ID' ,'AVAILABILITY_FLAG'])
        st.dataframe(clean_df)

  elif choice == "Delete":
        st.subheader("Delete")
        with st.expander("View Data"):
          result = view_all_bike()
          # st.write(result)
          clean_df = pd.DataFrame(result,columns=['REGISTRATION_NUMBER','MODEL_NAME' ,'MAKE' ,'MODEL_YEAR' ,'MILEAGE' ,'BIKE_CATEGORY_NAME' ,'LOC_ID' ,'AVAILABILITY_FLAG'])
          st.dataframe(clean_df)

        unique_list = [i[0] for i in view_all_regno()]
        delete_by_regno =  st.selectbox("Select regno",unique_list)
        if st.button("Delete"):
          delete_data_bike(delete_by_regno)
          st.warning("Deleted: '{}'".format(delete_by_regno))

        with st.expander("Updated Data"):
          result = view_all_bike()
          # st.write(result)
          clean_df = pd.DataFrame(result,columns=['REGISTRATION_NUMBER','MODEL_NAME' ,'MAKE' ,'MODEL_YEAR' ,'MILEAGE' ,'BIKE_CATEGORY_NAME' ,'LOC_ID' ,'AVAILABILITY_FLAG'])
          st.dataframe(clean_df)



