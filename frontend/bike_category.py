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

def bike_category():
  stc.html(HTML_BANNER)
  menu = ["Create", "Read", "Update", "Delete"]
  choice = st.sidebar.selectbox("Menu", menu)

  if choice == "Create":
    st.subheader("Add Item")
    col1,col2 = st.columns(2)
    with col1:
      CATEGORY_NAME = st.text_input("CATEGORY_NAME")
      BIKE_AGE=st.number_input("BIKE_AGE")
      LUGGAGE_CAPACITY=st.text_input("LUGGAGE_CAPACITY")
      COST_PER_DAY=st.number_input(" COST_PER_DAY")
      LATE_FEE_PER_HOUR=st.number_input(" LATE_FEE_PER_HOUR")
      

       # CATEGORY_NAME  BIKE_AGE LUGGAGE_CAPACITY  COST_PER_DAY LATE_FEE_PER_HOUR

    if st.button("submit"):
          add_data_bike_category(CATEGORY_NAME,BIKE_AGE ,LUGGAGE_CAPACITY , COST_PER_DAY , LATE_FEE_PER_HOUR )
          st.success("Added ::{} ::To bike".format(CATEGORY_NAME))

  elif choice == "Read":
    st.subheader("View Items")
    with st.expander("View All"):
      result = view_all_bike_category()
      #st.write(result)
      clean_df = pd.DataFrame(result,columns=['CATEGORY_NAME','BIKE_AGE' ,'LUGGAGE_CAPACITY' ,' COST_PER_DAY' ,' LATE_FEE_PER_HOUR' ])
      st.dataframe(clean_df)

  elif choice == "Update":
    st.subheader("Edit Items")
    with st.expander("Current Data"):
      result = view_all_bike_category()
      # st.write(result)
      clean_df = pd.DataFrame(result,columns=['CATEGORY_NAME','BIKE_AGE' ,'LUGGAGE_CAPACITY' ,' COST_PER_DAY' ,' LATE_FEE_PER_HOUR'])
      st.dataframe(clean_df)

    list_of_regno = [i[0] for i in view_all_category()]
    selected_favorite_category = st.selectbox("category",list_of_regno)
    regno_result = get_category(selected_favorite_category)
		

    if regno_result:
      CATEGORY_NAME = regno_result[0][0]
      BIKE_AGE =regno_result[0][1]
      LUGGAGE_CAPACITY = regno_result[0][2]
      COST_PER_DAY=regno_result[0][3]
      LATE_FEE_PER_HOUR=regno_result[0][4]
      
      


      col1,col2 = st.columns(2)
      
      with col1:
        new_CATEGORY_NAME = st.text_input("CATEGORY_NAME", CATEGORY_NAME)

      with col2:
        new_BIKE_AGE = st.number_input("BIKE_AGE",BIKE_AGE)
        new_LUGGAGE_CAPACITY=st.number_input("LUGGAGE_CAPACITY", LUGGAGE_CAPACITY)
        new_COST_PER_DAY=st.number_input(" COST_PER_DAY", COST_PER_DAY)
        new_LATE_FEE_PER_HOUR=st.number_input(" LATE_FEE_PER_HOUR", LATE_FEE_PER_HOUR)
        
       

      if st.button("Update Task"):
        edit_bike_category(new_CATEGORY_NAME,new_BIKE_AGE,new_LUGGAGE_CAPACITY,new_COST_PER_DAY,new_LATE_FEE_PER_HOUR,CATEGORY_NAME,BIKE_AGE,LUGGAGE_CAPACITY,COST_PER_DAY, LATE_FEE_PER_HOUR)
        st.success("updated {} To bike".format(CATEGORY_NAME))
       

      with st.expander("View Updated Data"):
        result = view_all_bike_category()
        # st.write(result)
        clean_df = pd.DataFrame(result,columns=['CATEGORY_NAME','BIKE_AGE' ,'LUGGAGE_CAPACITY' ,' COST_PER_DAY' ,' LATE_FEE_PER_HOUR' ])
        st.dataframe(clean_df)

  elif choice == "Delete":
        st.subheader("Delete")
        with st.expander("View Data"):
          result = view_all_bike_category()
          # st.write(result)
          clean_df = pd.DataFrame(result,columns=['CATEGORY_NAME','BIKE_AGE' ,'LUGGAGE_CAPACITY' ,' COST_PER_DAY' ,' LATE_FEE_PER_HOUR' ])
          st.dataframe(clean_df)

        unique_list = [i[0] for i in view_all_bike_category()]
        delete_by_regno =  st.selectbox("Select category",unique_list)
        if st.button("Delete"):
          delete_data_category(delete_by_regno)
          st.warning("Deleted: '{}'".format(delete_by_regno))

        with st.expander("Updated Data"):
          result = view_all_bike_category()
          # st.write(result)
          clean_df = pd.DataFrame(result,columns=['CATEGORY_NAME','BIKE_AGE' ,'LUGGAGE_CAPACITY' ,' COST_PER_DAY' ,' LATE_FEE_PER_HOUR' ])
          st.dataframe(clean_df)



