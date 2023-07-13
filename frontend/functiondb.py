import mysql.connector
import streamlit as st


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
	database="abc"
)
c = mydb.cursor()

def create_table_bike():
	c.execute('CREATE TABLE IF NOT EXISTS BIKE ( REGISTRATION_NUMBER VARCHAR(7) NOT NULL,BIKE_AGE VARCHAR(25) NOT NULL,LUGGAGE_CAPACITY VARCHAR(25) NOT NULL,COST_PER_DAY INTEGER(4) NOT NULL,LATE_FEE_PER_HOUR INTEGER NOT NULL,BIKE_CATEGORY_NAME VARCHAR(25) NOT NULL,LOC_ID VARCHAR(4) NOT NULL,AVAILABILITY_FLAG VARCHAR(1) NOT NULL)')
def create_table_bike_category():
	c.execute('CREATE TABLE IF NOT EXISTS BIKE_CATEGORY( CATEGORY_NAME VARCHAR(25) NOT NULL,BIKE_AGE INTEGER (10) NOT NULL,LUGGAGE_CAPACITY INTEGER (10) NOT NULL,COST_PER_DAY INTEGER(5	) NOT NULL,LATE_FEE_PER_HOUR INTEGER(5) NOT NULL')
def create_table_discount():
	c.execute('CREATE TABLE IF NOT EXISTS DISCOUNT_DETAILS( DISCOUNT_CODE VARCHAR(4) NOT NULL,DISCOUNT_NAME VARCHAR(25) NOT NULL,EXPIRY_DATE DATE NOT NULL,DISCOUNT_PERCENTAGE INT(4)  NOT NULL)')












def add_data_bike(REGISTRATION_NUMBER,MODEL_NAME,MAKE,MODEL_YEAR,MILEAGE,BIKE_CATEGORY_NAME,LOC_ID,AVAILABILITY_FLAG  ):
	c.execute('INSERT INTO bike(REGISTRATION_NUMBER,MODEL_NAME,MAKE,MODEL_YEAR,MILEAGE,BIKE_CATEGORY_NAME,LOC_ID,AVAILABILITY_FLAG ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(REGISTRATION_NUMBER,MODEL_NAME,MAKE,MODEL_YEAR,MILEAGE,BIKE_CATEGORY_NAME,LOC_ID,AVAILABILITY_FLAG))
	mydb.commit()

def add_data_bike_category(CATEGORY_NAME ,BIKE_AGE ,LUGGAGE_CAPACITY ,COST_PER_DAY ,LATE_FEE_PER_HOUR  ):
	c.execute('INSERT INTO BIKE_CATEGORY(CATEGORY_NAME ,BIKE_AGE ,LUGGAGE_CAPACITY ,COST_PER_DAY ,LATE_FEE_PER_HOUR  ) VALUES (%s,%s,%s,%s,%s)',(CATEGORY_NAME,BIKE_AGE,LUGGAGE_CAPACITY,COST_PER_DAY ,LATE_FEE_PER_HOUR))
	mydb.commit()


def add_data_bike_discount(DISCOUNT_CODE,DISCOUNT_NAME,EXPIRY_DATE,DISCOUNT_PERCENTAGE):
	c.execute('INSERT INTO DISCOUNT_DETAILS(DISCOUNT_CODE,DISCOUNT_NAME,EXPIRY_DATE,DISCOUNT_PERCENTAGE ) VALUES (%s,%s,%s,%s)',(DISCOUNT_CODE,DISCOUNT_NAME,EXPIRY_DATE,DISCOUNT_PERCENTAGE ))
	mydb.commit()


def add_data_bike_location(LOCATION_ID,LOCATION_NAME , STREET , CITY , STATE_NAME   ):
	c.execute('INSERT INTO LOCATION_DETAILS(LOCATION_ID,LOCATION_NAME , STREET , CITY , STATE_NAME  ) VALUES (%s,%s,%s,%s,%s)',(LOCATION_ID,LOCATION_NAME , STREET , CITY , STATE_NAME))
	mydb.commit()

def add_data_booking(BOOKING_ID,FROM_DT_TIME ,RET_DT_TIME,REG_NUM ,PICKUP_LOC,DROP_LOC):
	c.execute('INSERT INTO BOOKING_DETAILS(BOOKING_ID,FROM_DT_TIME,RET_DT_TIME,REG_NUM,BOOKING_STATUS,PICKUP_LOC,DROP_LOC) VALUES (%s,%s,%s,%s,%s,%s,%s)',(BOOKING_ID,FROM_DT_TIME ,RET_DT_TIME,REG_NUM,"B",PICKUP_LOC,DROP_LOC))
	mydb.commit()

def add_AMOUNT(BOOKING_ID):
	c.execute('CALL updateusingbill({})'.format(BOOKING_ID))
	mydb.commit()




# def add_data_upload(song_id,singer_id,song_name,song_format,singer_name,audio_file):
# 	c.execute('INSERT INTO upload_albums(song_id,singer_id,song_name,song_format,singer_name,audio_file) VALUES (%s,%s,%s,%s,%s,%s)',(song_id,singer_id,song_name,song_format,singer_name,audio_file))
# 	mydb.commit()


def view_all_regno():
	c.execute('SELECT DISTINCT REGISTRATION_NUMBER FROM bike')
	data = c.fetchall()
	return data
def view_all_category():
	c.execute('SELECT DISTINCT CATEGORY_NAME FROM BIKE_CATEGORY')
	data = c.fetchall()
	return data
def view_all_discount():
	c.execute('SELECT DISTINCT DISCOUNT_CODE FROM DISCOUNT_DETAILS')
	data = c.fetchall()
	return data
def view_all_location():
	c.execute('SELECT DISTINCT LOCATION_ID FROM LOCATION_DETAILS')
	data = c.fetchall()
	return data



def view_all_bike():
	c.execute('SELECT * FROM bike')
	data = c.fetchall()
	return data

def view_all_bike_category():
	c.execute('SELECT * FROM BIKE_CATEGORY')
	data = c.fetchall()
	return data
def view_all_bike_discount():
	c.execute('SELECT * FROM DISCOUNT_DETAILS')
	data = c.fetchall()
	return data
def view_all_bike_location():
	c.execute('SELECT * FROM LOCATION_DETAILS')
	data = c.fetchall()
	return data

def view_all_available():
	c.execute('SELECT * FROM bike where AVAILABILITY_FLAG ="A" ')
	data = c.fetchall()
	return data

def view_all_available_booked():
	c.execute('SELECT * FROM BOOKING_DETAILS where BOOKING_STATUS ="B" ')
	data = c.fetchall()
	return data

def view_all_available_booked1(BOOKING_ID):
	c.execute('SELECT * FROM BOOKING_DETAILS where BOOKING_ID ="{}" '.format(BOOKING_ID))
	data = c.fetchall()
	return data

# def view_all_data_favorite():
# 	c.execute('SELECT * FROM favorite_songs')
# 	data = c.fetchall()
# 	return data


def get_regno(REGISTRATION_NUMBER):
		c.execute('SELECT * FROM bike WHERE REGISTRATION_NUMBER="{}"'.format(REGISTRATION_NUMBER))
		data = c.fetchall()
		return data
def get_category(CATEGORY_NAME):
		c.execute('SELECT * FROM BIKE_CATEGORY WHERE CATEGORY_NAME="{}"'.format(CATEGORY_NAME))
		data = c.fetchall()
		return data

def get_discount(DISCOUNT_CODE):
		c.execute('SELECT * FROM DISCOUNT_DETAILS WHERE DISCOUNT_CODE="{}"'.format(DISCOUNT_CODE))
		data = c.fetchall()
		return data

def get_location(LOCATION_ID):
		c.execute('SELECT * FROM LOCATION_DETAILS WHERE LOCATION_ID="{}"'.format(LOCATION_ID))
		data = c.fetchall()
		return data


def edit_bike_data(new_id,new_MODEL_NAME,new_MAKE,new_MODEL_YEAR,new_MILEAGE,new_BIKE_CATEGORY_NAME,new_LOC_ID,new_AVAILABILITY_FLAG , REGISTRATION_NUMBER,MODEL_NAME,MAKE,MODEL_YEAR,MILEAGE,BIKE_CATEGORY_NAME,LOC_ID,AVAILABILITY_FLAG):
	c.execute("UPDATE BIKE SET  REGISTRATION_NUMBER=%s,MODEL_NAME=%s,MAKE=%s,MODEL_YEAR=%s,MILEAGE=%s,BIKE_CATEGORY_NAME=%s,LOC_ID=%s,AVAILABILITY_FLAG=%s WHERE REGISTRATION_NUMBER=%s AND MODEL_NAME=%s AND MAKE=%s AND MODEL_YEAR=%s AND MILEAGE=%s AND BIKE_CATEGORY_NAME=%s AND LOC_ID=%s AND AVAILABILITY_FLAG=%s",(new_id,new_MODEL_NAME,new_MAKE,new_MODEL_YEAR,new_MILEAGE,new_BIKE_CATEGORY_NAME,new_LOC_ID,new_AVAILABILITY_FLAG , REGISTRATION_NUMBER,MODEL_NAME,MAKE,MODEL_YEAR,MILEAGE,BIKE_CATEGORY_NAME,LOC_ID,AVAILABILITY_FLAG))
	mydb.commit()	



def edit_bike_category(new_CATEGORY_NAME,new_BIKE_AGE,new_LUGGAGE_CAPACITY,new_COST_PER_DAY,new_LATE_FEE_PER_HOUR,CATEGORY_NAME , BIKE_AGE, LUGGAGE_CAPACITY ,COST_PER_DAY, LATE_FEE_PER_HOUR):
	c.execute("UPDATE BIKE_CATEGORY SET CATEGORY_NAME=%s,BIKE_AGE=%s,LUGGAGE_CAPACITY=%s,COST_PER_DAY=%s,LATE_FEE_PER_HOUR=%s WHERE CATEGORY_NAME=%s and BIKE_AGE=%s and LUGGAGE_CAPACITY=%s and COST_PER_DAY=%s and LATE_FEE_PER_HOUR=%s ",(new_CATEGORY_NAME,new_BIKE_AGE,new_LUGGAGE_CAPACITY,new_COST_PER_DAY,new_LATE_FEE_PER_HOUR,CATEGORY_NAME , BIKE_AGE, LUGGAGE_CAPACITY ,COST_PER_DAY, LATE_FEE_PER_HOUR))
	mydb.commit()	


def edit_bike_discount(new_DISCOUNT_CODE,new_DISCOUNT_NAME,new_EXPIRY_DATE,new_DISCOUNT_PERCENTAGE,DISCOUNT_CODE,DISCOUNT_NAME,EXPIRY_DATE,DISCOUNT_PERCENTAGE):
	c.execute("UPDATE DISCOUNT_DETAILS SET DISCOUNT_CODE=%s,DISCOUNT_NAME=%s,EXPIRY_DATE=%s,DISCOUNT_PERCENTAGE=%s WHERE DISCOUNT_CODE=%s and DISCOUNT_NAME=%s and EXPIRY_DATE=%s and DISCOUNT_PERCENTAGE=%s",(new_DISCOUNT_CODE,new_DISCOUNT_NAME,new_EXPIRY_DATE,new_DISCOUNT_PERCENTAGE,DISCOUNT_CODE,DISCOUNT_NAME,EXPIRY_DATE,DISCOUNT_PERCENTAGE))
	mydb.commit()	


def edit_bike_location(new_LOCATION_ID,new_LOCATION_NAME,new_STREET,new_CITY,new_STATE_NAME,LOCATION_ID,LOCATION_NAME, STREET,CITY, STATE_NAME):
	c.execute("UPDATE LOCATION_DETAILS SET LOCATION_ID=%s,LOCATION_NAME=%s, STREET=%s,CITY=%s, STATE_NAME=%s WHERE LOCATION_ID=%s and LOCATION_NAME=%s and  STREET=%s and CITY=%s and  STATE_NAME=%s",(new_LOCATION_ID,new_LOCATION_NAME,new_STREET,new_CITY,new_STATE_NAME,LOCATION_ID,LOCATION_NAME, STREET,CITY, STATE_NAME))
	mydb.commit()	


def edit_data_booking(BOOKING_ID):
	c.execute('UPDATE BOOKING_DETAILS SET BOOKING_STATUS = "C" WHERE BOOKING_ID="{}" '.format(BOOKING_ID))
	mydb.commit()	
# def edit_data_booking(BOOKING_ID):
# 	c.execute('INSERT INTO BOOKING_DETAILS(BOOKING_STATUS) VALUES ("C") WHERE BOOKING_ID="{}"',(BOOKING_ID))




def delete_data_bike(REGISTRATION_NUMBER):
	c.execute('DELETE FROM bike WHERE REGISTRATION_NUMBER="{}"'.format(REGISTRATION_NUMBER))
	mydb.commit()	
def delete_data_category(CATEGORY_NAME):
	c.execute('DELETE FROM BIKE_CATEGORY WHERE CATEGORY_NAME="{}"'.format(CATEGORY_NAME))
	mydb.commit()	
def delete_data_discount(DISCOUNT_CODE):
	c.execute('DELETE FROM DISCOUNT_DETAILS WHERE DISCOUNT_CODE="{}"'.format(DISCOUNT_CODE))
	mydb.commit()	
def delete_data_location(LOCATION_ID):
	c.execute('DELETE FROM LOCATION_DETAILS WHERE LOCATION_ID="{}"'.format(LOCATION_ID))
	mydb.commit()	