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

def location():
  stc.html(HTML_BANNER)
  menu = ["Create", "Read", "Update", "Delete"]
  choice = st.sidebar.selectbox("Menu", menu)

  if choice == "Create":
    st.subheader("Add Item")
    col1,col2 = st.columns(2)
    with col1:
      LOCATION_ID = st.number_input("LOCATION_ID")
      LOCATION_NAME=st.text_input("LOCATION_NAME")
      STREET=st.text_input(" STREET")
      CITY=st.text_input(" CITY")
      STATE_NAME=st.text_input(" STATE_NAME")
      

       # LOCATION_ID  LOCATION_NAME  STREET  CITY STATE_NAME

    if st.button("submit"):
          add_data_bike_location(LOCATION_ID,LOCATION_NAME , STREET , CITY , STATE_NAME )
          st.success("Added ::{} ::To LOCATION TABLE".format(LOCATION_ID))

  elif choice == "Read":
    st.subheader("View Items")
    with st.expander("View All"):
      result = view_all_bike_location()
      #st.write(result)
      clean_df = pd.DataFrame(result,columns=['LOCATION_ID','LOCATION_NAME' ,' STREET' ,' CITY' ,' STATE_NAME' ])
      st.dataframe(clean_df)

  elif choice == "Update":
    st.subheader("Edit Items")
    with st.expander("Current Data"):
      result = view_all_bike_location()
      # st.write(result)
      clean_df = pd.DataFrame(result,columns=['LOCATION_ID','LOCATION_NAME' ,' STREET' ,' CITY' ,' STATE_NAME'])
      st.dataframe(clean_df)

    list_of_regno = [i[0] for i in view_all_location()]
    selected_favorite_location = st.selectbox("location",list_of_regno)
    regno_result = get_location(selected_favorite_location)
		

    if regno_result:
      LOCATION_ID = regno_result[0][0]
      LOCATION_NAME =regno_result[0][1]
      STREET = regno_result[0][2]
      CITY=regno_result[0][3]
      STATE_NAME=regno_result[0][4]
      
      


      col1,col2 = st.columns(2)
      
      with col1:
        new_LOCATION_ID = st.text_input("regno", LOCATION_ID)

      with col2:
        new_LOCATION_NAME = st.text_input("LOCATION_NAME",LOCATION_NAME)
        new_STREET=st.text_input(" STREET",STREET)
        new_CITY=st.text_input(" CITY", CITY)
        new_STATE_NAME=st.text_input(" STATE_NAME", STATE_NAME)
        
       

      if st.button("Update Task"):
        edit_bike_location(new_LOCATION_ID,new_LOCATION_NAME,new_STREET,new_CITY,new_STATE_NAME,LOCATION_ID,LOCATION_NAME, STREET,CITY, STATE_NAME)
        st.success("updated {} To LOCATION TABLE".format(LOCATION_ID))
       

      with st.expander("View Updated Data"):
        result = view_all_bike_location()
        # st.write(result)
        clean_df = pd.DataFrame(result,columns=['LOCATION_ID','LOCATION_NAME' ,' STREET' ,' CITY' ,' STATE_NAME' ])
        st.dataframe(clean_df)

  elif choice == "Delete":
        st.subheader("Delete")
        with st.expander("View Data"):
          result = view_all_bike_location()
          # st.write(result)
          clean_df = pd.DataFrame(result,columns=['LOCATION_ID','LOCATION_NAME' ,' STREET' ,' CITY' ,' STATE_NAME' ])
          st.dataframe(clean_df)

        unique_list = [i[0] for i in view_all_bike_location()]
        delete_by_regno =  st.selectbox("Select location",unique_list)
        if st.button("Delete"):
          delete_data_location(delete_by_regno)
          st.warning("Deleted: '{}'".format(delete_by_regno))

        with st.expander("Updated Data"):
          result = view_all_bike_location()
          # st.write(result)
          clean_df = pd.DataFrame(result,columns=['LOCATION_ID','LOCATION_NAME' ,' STREET' ,' CITY' ,' STATE_NAME' ])
          st.dataframe(clean_df)



