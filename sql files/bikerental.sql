-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 13, 2023 at 04:14 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bikerental`
--

-- --------------------------------------------------------

--
-- Table structure for table `bike`
--

CREATE TABLE `bike` (
  `REGISTRATION_NUMBER` char(7) NOT NULL,
  `MODEL_NAME` varchar(25) NOT NULL,
  `MAKE` varchar(25) NOT NULL,
  `MODEL_YEAR` int(4) NOT NULL,
  `MILEAGE` int(11) NOT NULL,
  `BIKE_CATEGORY_NAME` varchar(25) NOT NULL,
  `LOC_ID` char(4) NOT NULL,
  `AVAILABILITY_FLAG` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bike`
--

INSERT INTO `bike` (`REGISTRATION_NUMBER`, `MODEL_NAME`, `MAKE`, `MODEL_YEAR`, `MILEAGE`, `BIKE_CATEGORY_NAME`, `LOC_ID`, `AVAILABILITY_FLAG`) VALUES
('ABX1234', 'ACTIVA', 'HONDA', 2014, 10000, 'Scooter', 'L101', 'A'),
('AHK7325', 'RAV4', 'BAJAJ', 2022, 3400, 'Cruiser Elite', 'L103', 'A'),
('ASD9090', 'ACCORD', 'HONDA', 2022, 200, 'Cruiser', 'L103', 'A'),
('CFT1908', '328I', 'BMW', 2015, 10800, 'LUXURY BIKE', 'L104', 'A'),
('CXZ2356', 'AVENGER', 'DODGE', 2015, 5000, 'Cruiser', 'L102', 'A'),
('EDM8610', 'GLA', 'HARLEY', 2015, 12900, 'Cruiser Elite', 'L102', 'A'),
('EFB5427', 'WAYFARER', 'VESPA', 2014, 14350, 'Dirt bike', 'L105', 'A'),
('FKD8202', 'GOLF', 'DUCATI', 2022, 9000, 'Sport bike', 'L106', 'A'),
('GLS7625', 'FOCUS', 'VESPA', 2014, 12000, 'Sport bike', 'L107', 'A'),
('GLZ2376', 'COROLLA', 'BAJAJ', 2022, 5000, 'Scooter', 'L104', 'A'),
('HGF5628', 'TAURUS', 'VESPA', 2013, 15540, 'Adventure tourer', 'L106', 'A'),
('HJK1234', 'ACTIVA', 'HONDA', 2015, 20145, 'Scooter', 'L102', 'N'),
('HNX1890', 'PRIUS', 'BAJAJ', 2015, 15690, 'Sport bike', 'L105', 'N'),
('JSL7920', 'ODYSSEY', 'HONDA', 2013, 19320, 'mini bike', 'L106', 'A'),
('KJS1983', 'PRIUS', 'BAJAJ', 2014, 20900, 'Sport bike', 'L104', 'A'),
('LKJ7253', '200', 'KTM', 2014, 22300, 'Adventure tourer', 'L107', 'A'),
('MKU0172', 'TLX', 'ACURA', 2014, 12345, 'LUXURY BIKE', 'L103', 'A'),
('MNB8654', 'FALCON', 'VESPA', 2012, 10900, 'Dirt bike', 'L103', 'A'),
('MWO9296', 'ODYSSEY', 'HONDA', 2022, 2300, 'mini bike', 'L103', 'A'),
('OTY7293', 'CRUZE', 'ROYAL ENFIELD', 2022, 17800, 'Cruiser', 'L102', 'A'),
('PAJ5289', 'GRAND BIKEAVAN', 'DODGE', 2014, 23478, 'mini bike', 'L105', 'A'),
('PLM9873', 'IMPALA', 'ROYAL ENFIELD', 2015, 18900, 'Dirt bike', 'L106', 'A'),
('POI7281', '200', 'KTM', 2022, 18830, 'Adventure tourer', 'L102', 'N'),
('QIO7621', 'EQUINOX', 'ROYAL ENFIELD', 2013, 17560, 'Cruiser Elite', 'L107', 'A'),
('QSC8709', 'MKZ', 'HAYABUSA', 2012, 18700, 'LUXURY BIKE', 'L101', 'A'),
('QWE4562', 'LEGACY', 'HARLEY', 2012, 13420, 'Cruiser', 'L101', 'A'),
('SDF4567', 'VXL', 'VESPA', 2015, 15000, 'Scooter', 'L102', 'N'),
('SDL9356', 'FOCUS', 'VESPA', 2022, 10009, 'Sport bike', 'L103', 'A'),
('SHK7767', 'QUEST', 'AVENGER', 2012, 23478, 'mini bike', 'L107', 'A'),
('TGB8961', 'GENESIS', 'TVS', 2013, 17620, 'LUXURY BIKE', 'L102', 'A'),
('TRE9726', '200', 'KTM', 2012, 14320, 'Adventure tourer', 'L105', 'A'),
('TSJ6290', 'QUEST', 'AVENGER', 2015, 13200, 'mini bike', 'L104', 'A'),
('UHV9786', 'IMPALA', 'ROYAL ENFIELD', 2013, 11500, 'Dirt bike', 'L104', 'A'),
('UYT3981', 'LEGACY', 'HARLEY', 2013, 22750, 'Cruiser', 'L104', 'A'),
('VBN6283', 'TAURUS', 'VESPA', 2015, 17500, 'Adventure tourer', 'L101', 'A'),
('WDV2458', 'FALCON', 'VESPA', 2022, 5600, 'Dirt bike', 'L107', 'A'),
('WER3245', 'ACCENT', 'TVS', 2014, 12356, 'Scooter', 'L103', 'A'),
('WHM7619', 'AVALON', 'BAJAJ', 2022, 7800, 'LUXURY BIKE', 'L105', 'A'),
('WLZ8955', 'ESCAPE', 'VESPA', 2012, 19800, 'Cruiser Elite', 'L106', 'A'),
('YSN1927', 'PATHFINDER', 'AVENGER', 2014, 14390, 'Cruiser Elite', 'L101', 'A');

-- --------------------------------------------------------

--
-- Table structure for table `bike_category`
--

CREATE TABLE `bike_category` (
  `CATEGORY_NAME` varchar(25) NOT NULL,
  `BIKE_AGE` int(10) NOT NULL,
  `LUGGAGE_CAPACITY` int(10) NOT NULL,
  `COST_PER_DAY` decimal(5,2) NOT NULL,
  `LATE_FEE_PER_HOUR` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bike_category`
--

INSERT INTO `bike_category` (`CATEGORY_NAME`, `BIKE_AGE`, `LUGGAGE_CAPACITY`, `COST_PER_DAY`, `LATE_FEE_PER_HOUR`) VALUES
('Adventure tourer', 3, 5, '38.00', '1.14'),
('Cruiser', 3, 5, '35.00', '1.05'),
('Cruiser Elite', 2, 5, '36.00', '1.08'),
('Dirt bike', 4, 5, '40.00', '1.20'),
('LUXURY BIKE', 5, 5, '75.00', '2.25'),
('mini bike', 5, 7, '70.00', '2.10'),
('Scooter', 2, 5, '30.00', '0.90'),
('Sport bike', 3, 5, '32.00', '0.96');

-- --------------------------------------------------------

--
-- Table structure for table `billing_details`
--

CREATE TABLE `billing_details` (
  `BILL_ID` char(6) NOT NULL,
  `BILL_DATE` date NOT NULL,
  `BILL_STATUS` char(1) NOT NULL,
  `DISCOUNT_AMOUNT` decimal(10,2) NOT NULL,
  `TOTAL_AMOUNT` decimal(10,2) NOT NULL,
  `TAX_AMOUNT` decimal(10,2) NOT NULL,
  `BOOKING_ID` char(5) NOT NULL,
  `TOTAL_LATE_FEE` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `billing_details`
--

INSERT INTO `billing_details` (`BILL_ID`, `BILL_DATE`, `BILL_STATUS`, `DISCOUNT_AMOUNT`, `TOTAL_AMOUNT`, `TAX_AMOUNT`, `BOOKING_ID`, `TOTAL_LATE_FEE`) VALUES
('BL1001', '2022-01-25', 'P', '24.36', '138.03', '12.38', 'B1001', '0.00'),
('BL1002', '2022-01-15', 'P', '0.00', '487.13', '12.38', 'B1003', '0.00'),
('BL1003', '2022-04-24', 'P', '10.39', '41.57', '3.96', 'B1004', '0.00');

-- --------------------------------------------------------

--
-- Table structure for table `booking_details`
--

CREATE TABLE `booking_details` (
  `BOOKING_ID` char(5) NOT NULL,
  `FROM_DT_TIME` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `RET_DT_TIME` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `AMOUNT` decimal(10,2) NOT NULL,
  `BOOKING_STATUS` char(1) NOT NULL,
  `PICKUP_LOC` char(4) NOT NULL,
  `DROP_LOC` char(4) NOT NULL,
  `REG_NUM` char(7) NOT NULL,
  `DL_NUM` char(8) NOT NULL,
  `INS_CODE` char(4) DEFAULT NULL,
  `ACT_RET_DT_TIME` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `DISCOUNT_CODE` char(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking_details`
--

INSERT INTO `booking_details` (`BOOKING_ID`, `FROM_DT_TIME`, `RET_DT_TIME`, `AMOUNT`, `BOOKING_STATUS`, `PICKUP_LOC`, `DROP_LOC`, `REG_NUM`, `DL_NUM`, `INS_CODE`, `ACT_RET_DT_TIME`, `DISCOUNT_CODE`) VALUES
('B1001', '2022-01-20 04:30:00', '2022-01-25 04:30:00', '150.00', 'R', 'L101', 'L101', 'ABX1234', 'F1234554', NULL, '2022-01-25 04:30:00', 'D756'),
('B1002', '2022-01-21 05:30:00', '2022-01-24 04:30:00', '90.00', 'C', 'L102', 'L102', 'SDF4567', 'T0981237', NULL, '2022-11-15 13:33:37', NULL),
('B1003', '2022-02-10 07:30:00', '2022-01-15 07:30:00', '450.00', 'R', 'L101', 'L101', 'QSC8709', 'R8763578', 'I201', '2022-01-15 07:30:00', NULL),
('B1004', '2022-04-24 07:30:00', '2022-04-25 15:00:00', '48.00', 'R', 'L106', 'L106', 'WLZ8955', 'F0091266', 'I202', '2022-04-23 15:00:00', 'D234'),
('B1005', '2022-04-18 03:30:00', '2022-04-25 03:30:00', '266.00', 'B', 'L102', 'L106', 'POI7281', 'P1234567', NULL, '2022-11-15 13:33:37', 'D972'),
('B1006', '2022-04-21 11:30:00', '2022-04-25 11:30:00', '228.00', 'B', 'L105', 'L107', 'HNX1890', 'V5690245', 'I203', '2022-11-15 13:33:37', 'D234'),
('B1007', '2022-04-22 02:30:00', '2022-04-25 11:30:00', '405.00', 'B', 'L102', 'L102', 'SDF4567', 'I3478953', 'I201', '2022-11-15 13:33:37', 'D756'),
('B1008', '2022-04-11 02:30:00', '2022-04-25 11:30:00', '630.00', 'B', 'L102', 'L102', 'HJK1234', 'T0981237', 'I201', '2022-11-15 13:33:37', 'D756');

-- --------------------------------------------------------

--
-- Table structure for table `customer_details`
--

CREATE TABLE `customer_details` (
  `DL_NUMBER` char(8) NOT NULL,
  `FNAME` varchar(25) NOT NULL,
  `MNAME` varchar(15) DEFAULT NULL,
  `LNAME` varchar(25) NOT NULL,
  `PHONE_NUMBER` int(10) NOT NULL,
  `EMAIL_ID` varchar(30) NOT NULL,
  `STREET` varchar(30) NOT NULL,
  `CITY` varchar(20) NOT NULL,
  `STATE_NAME` varchar(20) NOT NULL,
  `ZIPCODE` int(5) NOT NULL,
  `MEMBERSHIP_TYPE` char(1) NOT NULL DEFAULT 'N',
  `MEMBERSHIP_ID` char(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_details`
--

INSERT INTO `customer_details` (`DL_NUMBER`, `FNAME`, `MNAME`, `LNAME`, `PHONE_NUMBER`, `EMAIL_ID`, `STREET`, `CITY`, `STATE_NAME`, `ZIPCODE`, `MEMBERSHIP_TYPE`, `MEMBERSHIP_ID`) VALUES
('E7521097', 'MITA', NULL, 'RANA', 2147483647, 'mitarana@gmail.com', '367 MEANDERING WAY', 'HOUSTON', 'TEXAS', 76245, 'N', NULL),
('F0091266', 'MIKE', NULL, 'BOYEAR', 2147483647, 'mikeboy@gmail.com', '1007 DALLAS PARKWAY', 'DALLAS', 'TEXAS', 72212, 'N', NULL),
('F1234554', 'KEERTHIKUMAR', NULL, 'RAVICHANDRAN', 2147483647, 'keerthi@gmail.com', '700 CAMPBELL RD', 'RICHARDSON', 'TEXAS', 75080, 'M', 'M1001'),
('F2345611', 'SURESH', 'KUMAR', 'GOPALAKRISHNAN', 2147483647, 'suresh2234@gmail.com', '6547 CANOGA AVE', 'CANOGA PARK', 'CALIFORNIA', 91303, 'N', NULL),
('F9764521', 'NIVEDITHA', NULL, 'VARADHA CHANDRASEKARAN', 2147483647, 'nivi07@gmail.com', '800 RENNER RD', 'RICHARDSON', 'TEXAS', 75080, 'M', 'M1002'),
('I3478953', 'MARK', 'S', 'TOWNSEND', 2147483647, 'markstown@gmail.com', '7825 MCCALLUM BLVD', 'DALLAS', 'TEXAS', 75252, 'M', 'M1003'),
('P1234567', 'CHRIS', NULL, 'ALEXANDER', 9902489, 'chrisalex@gmail.com', '2256 WALL STREET', 'NEWARK', 'NEW JERSEY', 65289, 'M', 'M1005'),
('R8763578', 'MARK', NULL, 'HUFF', 2147483647, 'markhuff@gmail.com', '1445 ROSS AVE', 'DALLAS', 'TEXAS', 75202, 'N', NULL),
('T0981237', 'DANISH', NULL, 'HASSAN', 2147483647, 'danishhasan@gmail.com', '888 PRESTON ROAD', 'DULLES', 'VIRGINIA', 92367, 'M', 'M1004'),
('V5690245', 'VELA', 'R', 'REYNALDO', 2147483647, 'reyvela@gmail.com', '0099 ALMA ROAD', 'DULLES', 'VIRGINIA', 97325, 'N', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `discount_details`
--

CREATE TABLE `discount_details` (
  `DISCOUNT_CODE` char(4) NOT NULL,
  `DISCOUNT_NAME` varchar(25) NOT NULL,
  `EXPIRY_DATE` date NOT NULL,
  `DISCOUNT_PERCENTAGE` decimal(4,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `discount_details`
--

INSERT INTO `discount_details` (`DISCOUNT_CODE`, `DISCOUNT_NAME`, `EXPIRY_DATE`, `DISCOUNT_PERCENTAGE`) VALUES
('D109', 'WEEKLY RENTALS', '2020-11-09', '25.00'),
('D234', 'CTS CORPORATE', '2019-09-02', '20.00'),
('D297', 'UPGRADE SPECIAL', '2018-02-18', '20.00'),
('D678', 'IBM CORPORATE', '2018-01-25', '25.00'),
('D756', 'HOLIDAY SPECIAL', '2017-10-29', '10.00'),
('D972', 'ONE WAY SPECIAL', '2022-12-15', '20.00');

-- --------------------------------------------------------

--
-- Table structure for table `location_details`
--

CREATE TABLE `location_details` (
  `LOCATION_ID` char(4) NOT NULL,
  `LOCATION_NAME` varchar(50) NOT NULL,
  `STREET` varchar(30) NOT NULL,
  `CITY` varchar(20) NOT NULL,
  `STATE_NAME` varchar(20) NOT NULL,
  `ZIPCODE` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `location_details`
--

INSERT INTO `location_details` (`LOCATION_ID`, `LOCATION_NAME`, `STREET`, `CITY`, `STATE_NAME`, `ZIPCODE`) VALUES
('L101', 'DALLAS LOVE FIELD AIRPORT', 'Herb Kelleher Way', 'Dallas', 'Texas', 75235),
('L102', 'LOS ANGELES INTL AIRPORT', 'World Way', 'Los Angeles', 'California', 90045),
('L103', 'DALLAS/ FORT WORTH INTL AIRPORT', 'International Pkwy', 'DFW Airport', 'Texas', 75261),
('L104', 'WEST HOUSTON AIRPORT', 'Groschke Rd', 'Houston', 'Texas', 77094),
('L105', 'WASHINGTON DULLES INTL AIRPORT', 'Saarinen Cir', 'Dulles', 'Virginia', 20226),
('L106', 'NEWARK LIBERTY INTL AIRPORT', 'Brewster Rd', 'Newark', 'New Jersey', 7114),
('L107', 'SALT LAKE CITY INTL AIRPORT', 'N Terminal Dr', 'Salt Lake City', 'Utah', 84122);

-- --------------------------------------------------------

--
-- Table structure for table `rental_bike_insurance`
--

CREATE TABLE `rental_bike_insurance` (
  `INSURANCE_CODE` char(4) NOT NULL,
  `INSURANCE_NAME` varchar(50) NOT NULL,
  `COVERAGE_TYPE` varchar(200) NOT NULL,
  `COST_PER_DAY` decimal(4,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rental_bike_insurance`
--

INSERT INTO `rental_bike_insurance` (`INSURANCE_CODE`, `INSURANCE_NAME`, `COVERAGE_TYPE`, `COST_PER_DAY`) VALUES
('I201', 'COLLISION DAMAGE WAIVER', 'Covers theft and total damage to the rental BIKE', '15.00'),
('I202', 'SUPPLEMENTAL LIABILITY PROTECTION', 'Covers damage done to others', '12.00'),
('I203', 'PERSONAL ACCIDENT INSURANCE', 'Covers medical costs for driver and passengers', '10.00'),
('I204', 'PERSONAL EFFECTS COVERAGE', 'Covers theft of personal belongings', '5.00');

-- --------------------------------------------------------

--
-- Stand-in structure for view `table1`
-- (See below for the actual view)
--
CREATE TABLE `table1` (
`LOCATIONID` char(4)
,`CATNAME` varchar(25)
,`NOOFBIKES` bigint(21)
);

-- --------------------------------------------------------

--
-- Structure for view `table1`
--
DROP TABLE IF EXISTS `table1`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `table1`  AS SELECT `lc`.`LID` AS `LOCATIONID`, `lc`.`CNAME` AS `CATNAME`, count(`c`.`REGISTRATION_NUMBER`) AS `NOOFBIKES` FROM ((select `l`.`LOCATION_ID` AS `LID`,`cc`.`CATEGORY_NAME` AS `CNAME` from (`bike_category` `cc` join `location_details` `l`)) `lc` left join `bike` `c` on(`lc`.`CNAME` = `c`.`BIKE_CATEGORY_NAME` and `lc`.`LID` = `c`.`LOC_ID`)) GROUP BY `lc`.`LID`, `lc`.`CNAME` ORDER BY `lc`.`LID` ASC ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bike`
--
ALTER TABLE `bike`
  ADD PRIMARY KEY (`REGISTRATION_NUMBER`),
  ADD KEY `BIKEFK1` (`BIKE_CATEGORY_NAME`),
  ADD KEY `BIKEFK2` (`LOC_ID`);

--
-- Indexes for table `bike_category`
--
ALTER TABLE `bike_category`
  ADD PRIMARY KEY (`CATEGORY_NAME`);

--
-- Indexes for table `billing_details`
--
ALTER TABLE `billing_details`
  ADD PRIMARY KEY (`BILL_ID`),
  ADD KEY `BILLINGFK1` (`BOOKING_ID`);

--
-- Indexes for table `booking_details`
--
ALTER TABLE `booking_details`
  ADD PRIMARY KEY (`BOOKING_ID`),
  ADD KEY `BOOKINGFK1` (`PICKUP_LOC`),
  ADD KEY `BOOKINGFK2` (`DROP_LOC`),
  ADD KEY `BOOKINGFK3` (`REG_NUM`),
  ADD KEY `BOOKINGFK4` (`DL_NUM`),
  ADD KEY `BOOKINGFK5` (`INS_CODE`),
  ADD KEY `BOOKINGFK6` (`DISCOUNT_CODE`);

--
-- Indexes for table `customer_details`
--
ALTER TABLE `customer_details`
  ADD PRIMARY KEY (`DL_NUMBER`);

--
-- Indexes for table `discount_details`
--
ALTER TABLE `discount_details`
  ADD PRIMARY KEY (`DISCOUNT_CODE`),
  ADD UNIQUE KEY `DISCOUNTSK` (`DISCOUNT_NAME`);

--
-- Indexes for table `location_details`
--
ALTER TABLE `location_details`
  ADD PRIMARY KEY (`LOCATION_ID`);

--
-- Indexes for table `rental_bike_insurance`
--
ALTER TABLE `rental_bike_insurance`
  ADD PRIMARY KEY (`INSURANCE_CODE`),
  ADD UNIQUE KEY `INSURANCESK` (`INSURANCE_NAME`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bike`
--
ALTER TABLE `bike`
  ADD CONSTRAINT `BIKEFK1` FOREIGN KEY (`BIKE_CATEGORY_NAME`) REFERENCES `bike_category` (`CATEGORY_NAME`),
  ADD CONSTRAINT `BIKEFK2` FOREIGN KEY (`LOC_ID`) REFERENCES `location_details` (`LOCATION_ID`);

--
-- Constraints for table `billing_details`
--
ALTER TABLE `billing_details`
  ADD CONSTRAINT `BILLINGFK1` FOREIGN KEY (`BOOKING_ID`) REFERENCES `booking_details` (`BOOKING_ID`);

--
-- Constraints for table `booking_details`
--
ALTER TABLE `booking_details`
  ADD CONSTRAINT `BOOKINGFK1` FOREIGN KEY (`PICKUP_LOC`) REFERENCES `location_details` (`LOCATION_ID`),
  ADD CONSTRAINT `BOOKINGFK2` FOREIGN KEY (`DROP_LOC`) REFERENCES `location_details` (`LOCATION_ID`),
  ADD CONSTRAINT `BOOKINGFK3` FOREIGN KEY (`REG_NUM`) REFERENCES `bike` (`REGISTRATION_NUMBER`),
  ADD CONSTRAINT `BOOKINGFK4` FOREIGN KEY (`DL_NUM`) REFERENCES `customer_details` (`DL_NUMBER`),
  ADD CONSTRAINT `BOOKINGFK5` FOREIGN KEY (`INS_CODE`) REFERENCES `rental_bike_insurance` (`INSURANCE_CODE`),
  ADD CONSTRAINT `BOOKINGFK6` FOREIGN KEY (`DISCOUNT_CODE`) REFERENCES `discount_details` (`DISCOUNT_CODE`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
