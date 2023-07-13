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

def discount():
  stc.html(HTML_BANNER)
  menu = ["Create", "Read", "Update", "Delete"]
  choice = st.sidebar.selectbox("Menu", menu)

  if choice == "Create":
    st.subheader("Add Item")
    col1,col2 = st.columns(2)
    with col1:
      DISCOUNT_CODE = st.number_input("DISCOUNT_CODE")
      DISCOUNT_NAME=st.text_input("DISCOUNT_NAME")
      EXPIRY_DATE=st.date_input("EXPIRY_DATE")
      DISCOUNT_PERCENTAGE=st.number_input(" DISCOUNT_PERCENTAGE")
      
      

       # DISCOUNT_CODE  DISCOUNT_NAME EXPIRY_DATE  DISCOUNT_PERCENTAGE LATE_FEE_PER_HOUR

    if st.button("submit"):
          add_data_bike_discount(DISCOUNT_CODE,DISCOUNT_NAME ,EXPIRY_DATE , DISCOUNT_PERCENTAGE )
          st.success("Added ::{} ::To bike".format(DISCOUNT_CODE))

  elif choice == "Read":
    st.subheader("View Items")
    with st.expander("View All"):
      result = view_all_bike_discount()
      #st.write(result)
      clean_df = pd.DataFrame(result,columns=['DISCOUNT_CODE','DISCOUNT_NAME' ,'EXPIRY_DATE' ,' DISCOUNT_PERCENTAGE' ])
      st.dataframe(clean_df)

  elif choice == "Update":
    st.subheader("Edit Items")
    with st.expander("Current Data"):
      result = view_all_bike_discount()
      # st.write(result)
      clean_df = pd.DataFrame(result,columns=['DISCOUNT_CODE','DISCOUNT_NAME','EXPIRY_DATE' ,' DISCOUNT_PERCENTAGE' ])
      st.dataframe(clean_df)

    list_of_regno = [i[0] for i in view_all_discount()]
    selected_favorite_category = st.selectbox("DISCOUNT_CODE",list_of_regno)
    regno_result = get_discount(selected_favorite_category)
		

    if regno_result:
      DISCOUNT_CODE = regno_result[0][0]
      DISCOUNT_NAME =regno_result[0][1]
      EXPIRY_DATE = regno_result[0][2]
      DISCOUNT_PERCENTAGE=regno_result[0][3]
     
      
      


      col1,col2 = st.columns(2)
      
      with col1:
        new_DISCOUNT_CODE = st.text_input("DISCOUNT_CODE", DISCOUNT_CODE)

      with col2:
        new_DISCOUNT_NAME = st.text_input("DISCOUNT_NAME",DISCOUNT_NAME)
        new_EXPIRY_DATE=st.date_input("EXPIRY_DATE", EXPIRY_DATE)
        new_DISCOUNT_PERCENTAGE=st.number_input(" DISCOUNT_PERCENTAGE", DISCOUNT_PERCENTAGE)
        
        
       

      if st.button("Update Task"):
        edit_bike_discount(new_DISCOUNT_CODE,new_DISCOUNT_NAME,new_EXPIRY_DATE,new_DISCOUNT_PERCENTAGE,DISCOUNT_CODE,DISCOUNT_NAME,EXPIRY_DATE,DISCOUNT_PERCENTAGE)
        st.success("updated {} To discount".format(DISCOUNT_CODE))
       

      with st.expander("View Updated Data"):
        result = view_all_bike_discount()
        # st.write(result)
        clean_df = pd.DataFrame(result,columns=['DISCOUNT_CODE','DISCOUNT_NAME' ,'EXPIRY_DATE' ,' DISCOUNT_PERCENTAGE'  ])
        st.dataframe(clean_df)

  elif choice == "Delete":
        st.subheader("Delete")
        with st.expander("View Data"):
          result = view_all_bike_discount()
          # st.write(result)
          clean_df = pd.DataFrame(result,columns=['DISCOUNT_CODE','DISCOUNT_NAME' ,'EXPIRY_DATE' ,' DISCOUNT_PERCENTAGE'  ])
          st.dataframe(clean_df)

        unique_list = [i[0] for i in view_all_bike_discount()]
        delete_by_regno =  st.selectbox("Select coupon",unique_list)
        if st.button("Delete"):
          delete_data_discount(delete_by_regno)
          st.warning("Deleted: '{}'".format(delete_by_regno))

        with st.expander("Updated Data"):
          result = view_all_bike_discount()
          # st.write(result)
          clean_df = pd.DataFrame(result,columns=['DISCOUNT_CODE','DISCOUNT_NAME' ,'EXPIRY_DATE' ,' DISCOUNT_PERCENTAGE'  ])
          st.dataframe(clean_df)



