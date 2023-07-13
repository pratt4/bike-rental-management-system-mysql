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

def user():
  stc.html(HTML_BANNER)
  menu = ["Rent a bike","Cancel booking"]
  choice = st.sidebar.selectbox("Menu", menu)

  if choice == "Rent a bike":
    st.subheader("Rent a bike")
    
    with st.expander("Available Bikes"):
      result = view_all_available()
      # st.write(result)
      clean_df = pd.DataFrame(result,columns=['REGISTRATION_NUMBER','MODEL_NAME' ,'MAKE' ,'MODEL_YEAR' ,'total_km' ,'BIKE_CATEGORY_NAME' ,'LOC_ID' ,'AVAILABILITY_FLAG'])
      st.dataframe(clean_df)



    col1,col2 = st.columns(2)
    with col1:
      list_of_regno = [i[0] for i in view_all_available()]
      
      REGISTRATION_NUMBER = st.selectbox("regno",list_of_regno)
      BOOKING_ID=st.text_input("Booking_id")
      FROM_DT_TIME=st.date_input("booking date")
      RET_DT_TIME=st.date_input("return date")
      PICKUP_LOC=st.text_input("PICKUP_LOC")
      DROP_LOC=st.text_input("DROP_LOC")

      if st.button("Confirm booking"):
          add_data_booking(BOOKING_ID ,FROM_DT_TIME ,RET_DT_TIME ,REGISTRATION_NUMBER,PICKUP_LOC,DROP_LOC)
          # add_AMOUNT(BOOKING_ID)
          st.success("successfully booked")
    if st.button("SHOW AMOUNT"):
      add_AMOUNT(BOOKING_ID)
      result = view_all_available_booked1(BOOKING_ID)
  # st.write(result)
      clean_df = pd.DataFrame(result,columns=['BOOKING_ID' ,'FROM_DT_TIME' ,'RET_DT_TIME' ,'AMOUNT' , 'BOOKING_STATUS' ,'PICKUP_LOC'  ,'DROP_LOC' ,'REG_NUM' ,'DL_NUM' ,'INS_CODE' ,'ACT_RET_DT_TIME' ,'DISCOUNT_CODE' ])
      st.dataframe(clean_df)


  # elif choice == "show amount":         
  #   BOOKING_ID=st.text_input("Booking_id")
  #   if st.button("SHOW AMOUNT"):
  #       add_AMOUNT(BOOKING_ID)
  #       result = view_all_available_booked1(BOOKING_ID)
  #   # st.write(result)
  #       clean_df = pd.DataFrame(result,columns=['BOOKING_ID' ,'FROM_DT_TIME' ,'RET_DT_TIME' ,'AMOUNT' , 'BOOKING_STATUS' ,'PICKUP_LOC'  ,'DROP_LOC' ,'REG_NUM' ,'DL_NUM' ,'INS_CODE' ,'ACT_RET_DT_TIME' ,'DISCOUNT_CODE' ])
  #       st.dataframe(clean_df)


  elif choice == "Cancel booking":  
    st.subheader("Cancel booking")
    
    with st.expander("booked bikes"):
      result = view_all_available_booked()
      # st.write(result)
      clean_df = pd.DataFrame(result,columns=['BOOKING_ID' ,'FROM_DT_TIME' ,'RET_DT_TIME' ,'AMOUNT' , 'BOOKING_STATUS' ,'PICKUP_LOC'  ,'DROP_LOC' ,'REG_NUM' ,'DL_NUM' ,'INS_CODE' ,'ACT_RET_DT_TIME' ,'DISCOUNT_CODE' ])
      st.dataframe(clean_df)

    col1,col2 = st.columns(2)
    with col1:
        list_of_regno = [i[0] for i in view_all_available_booked()]
        BOOKING_ID=st.selectbox("BOOKING_ID",list_of_regno)
        if st.button("Cancel booking"):
          edit_data_booking(BOOKING_ID)
          st.success("successfully canceled")

    result = view_all_available_booked()
    # st.write(result)
    clean_df = pd.DataFrame(result,columns=['BOOKING_ID' ,'FROM_DT_TIME' ,'RET_DT_TIME' ,'AMOUNT' , 'BOOKING_STATUS' ,'PICKUP_LOC'  ,'DROP_LOC' ,'REG_NUM' ,'DL_NUM' ,'INS_CODE' ,'ACT_RET_DT_TIME' ,'DISCOUNT_CODE' ])
    st.dataframe(clean_df)
      

      

   
     