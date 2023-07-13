DELIMITER $$
CREATE FUNCTION `total_amount`(`regno` VARCHAR(11), `booked_date` DATE, `ReturnDateTime` DATE) RETURNS int(11)

BEGIN
DECLARE amt int;
DECLARE amount int;

SELECT COST_PER_DAY INTO amt FROM BIKE_CATEGORY CC INNER JOIN BIKE C ON CC.CATEGORY_NAME = C.BIKE_CATEGORY_NAME WHERE C.REGISTRATION_NUMBER = regno;

set @amount=amt * datediff(booked_date,ReturnDateTime);

return amt;

  
END$$
DELIMITER ;


-- latefee PROCEDURE
DELIMITER $$
CREATE PROCEDURE `LATE_FEE`(IN `actualReturnDateTime` TIMESTAMP, IN `ReturnDateTime` TIMESTAMP, IN `BILLNO` VARCHAR(11), IN `regNum` VARCHAR(11))


BEGIN 

DECLARE lateFeePerHour INT ; 
DECLARE totalLateFee INT ; 
DECLARE hourDifference DECIMAL(10,2);

SELECT LATE_FEE_PER_HOUR INTO lateFeePerHour FROM BIKE_CATEGORY AS CC INNER JOIN BIKE AS C ON CC.CATEGORY_NAME = C.BIKE_CATEGORY_NAME WHERE C.REGISTRATION_NUMBER = regNum; 
IF actualReturnDateTime > ReturnDateTime THEN SELECT DATEDIFF(actualReturnDateTime, ReturnDateTime) into hourDifference; 


END IF; 

CALL LATE(actualReturnDateTime, ReturnDateTime,BILLNO);
UPDATE billing_details SET LATE_FEE=(hourDifference *  lateFeePerHour) WHERE BILL_ID=BILLNO;

END$$
DELIMITER ;

-- UPDATEAMOUNT PROCEDURE
DELIMITER $$
CREATE  PROCEDURE `updateamount`(IN `regno` VARCHAR(11), IN `booked_date` DATE, IN `ReturnDateTime` DATE, IN `billid` VARCHAR(11))

BEGIN
DECLARE amt int;


SELECT total_amount(regno,booked_date,ReturnDateTime) into amt; 
 
UPDATE booking_details SET AMOUNT=amt WHERE BOOKING_ID = billid;

END$$
DELIMITER ;


-- UPDATEBIKE TRIGGER
CREATE TRIGGER ` UPDATE_BIKE_DETAILS` AFTER UPDATE ON `booking_details`
 FOR EACH ROW BEGIN
    IF NEW.BOOKING_STATUS ='C' THEN
      UPDATE BIKE SET AVAILABILITY_FLAG = 'A'  WHERE REGISTRATION_NUMBER = NEW.REG_NUM;
    ELSE 
      IF NEW.BOOKING_STATUS ='R' THEN
        UPDATE BIKE SET LOC_ID = NEW.DROP_LOC ,AVAILABILITY_FLAG = 'A' WHERE REGISTRATION_NUMBER = NEW.REG_NUM;
      END IF;
    END IF;
END


-- TRIGGER `BOOK_BIKE`
CREATE TRIGGER `BOOK_BIKE` AFTER INSERT ON `booking_details`

 FOR EACH ROW BEGIN
   
 UPDATE BIKE SET AVAILABILITY_FLAG = 'N'  WHERE REGISTRATION_NUMBER = NEW.REG_NUM;
   
END


