CREATE DATABASE  IF NOT EXISTS `irs` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `irs`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: irs
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `agent`
--

DROP TABLE IF EXISTS `agent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agent` (
  `Agent_ID` int NOT NULL AUTO_INCREMENT,
  `Agent_Name` varchar(100) NOT NULL,
  `Department` varchar(100) DEFAULT NULL,
  `Agent_Rank` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Agent_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agent`
--

LOCK TABLES `agent` WRITE;
/*!40000 ALTER TABLE `agent` DISABLE KEYS */;
INSERT INTO `agent` VALUES (1,'Ethan Blake','Cyber Security','Senior Agent'),(2,'Sophia Evans','Financial Crimes','Junior Agent'),(3,'Liam Foster','Counterterrorism','Senior Agent'),(4,'Ava Mitchell','Field Operations','Field Agent'),(5,'Noah Hayes','Cyber Security','Senior Agent'),(6,'Emma Collins','Financial Crimes','Junior Agent'),(7,'Mason Clark','Counterterrorism','Field Agent'),(8,'Olivia Davis','Field Operations','Senior Agent'),(9,'Jacob Turner','Cyber Security','Junior Agent'),(10,'Charlotte Lewis','Financial Crimes','Field Agent'),(11,'Henry Scott','Counterterrorism','Senior Agent'),(12,'Isabella Reed','Field Operations','Junior Agent'),(13,'Lucas Parker','Cyber Security','Field Agent'),(14,'Amelia Carter','Financial Crimes','Senior Agent'),(15,'James Morgan','Counterterrorism','Junior Agent');
/*!40000 ALTER TABLE `agent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audit`
--

DROP TABLE IF EXISTS `audit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `audit` (
  `Audit_ID` int NOT NULL AUTO_INCREMENT,
  `Return_ID` int NOT NULL,
  `Audit_Date` date DEFAULT NULL,
  `Notes` text,
  `Outcome` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Audit_ID`),
  KEY `Return_ID` (`Return_ID`),
  CONSTRAINT `audit_ibfk_1` FOREIGN KEY (`Return_ID`) REFERENCES `tax_return` (`Return_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit`
--

LOCK TABLES `audit` WRITE;
/*!40000 ALTER TABLE `audit` DISABLE KEYS */;
INSERT INTO `audit` VALUES (1,1,'2023-02-05','Checked eligibility for child tax credit','Approved'),(2,2,'2023-03-12','Found missing documentation for deductions','Further Review'),(3,3,'2023-04-25','Income statements verified without issues','Approved'),(4,4,'2023-01-30','Identified potential errors in capital gains reporting','Further Review'),(5,5,'2023-05-08','Reviewed charitable donation receipts','Approved'),(6,6,'2023-06-20','Uncovered inconsistent income reporting','Further Review'),(7,7,'2023-07-15','W-2 forms reviewed and validated','Approved'),(8,8,'2023-03-18','Discrepancies found in business expense claims','Further Review'),(9,9,'2023-08-21','Examined rental property income','Approved'),(10,10,'2023-09-05','Found overreported business expenses','Further Review'),(11,11,'2023-10-11','Reviewed foreign earned income','Approved'),(12,12,'2023-07-01','Investigated excessive medical deductions','Further Review'),(13,13,'2023-04-28','Examined significant retirement withdrawals','Approved'),(14,14,'2023-02-19','Potential fraud detected in claimed income','Further Review'),(15,15,'2023-03-06','Confirmed deductions for home office use','Approved');
/*!40000 ALTER TABLE `audit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employer`
--

DROP TABLE IF EXISTS `employer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employer` (
  `Employer_ID` int NOT NULL AUTO_INCREMENT,
  `Employer_Name` varchar(100) NOT NULL,
  `Employer_TIN` char(9) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Phone_Number` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`Employer_ID`),
  KEY `idx_employer_id` (`Employer_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employer`
--

LOCK TABLES `employer` WRITE;
/*!40000 ALTER TABLE `employer` DISABLE KEYS */;
INSERT INTO `employer` VALUES (2,'MedLink Healthcare','312098745','620 Horizon Ave','555-9810'),(3,'Prime Auto','742310856','84 Motorway Blvd','555-1234'),(4,'Urban Retailers','893127056','505 Midtown Mall','555-5678'),(5,'Equity Capital','230876591','47 Finance Square','555-3456'),(6,'Solaris Energy','412389765','92 Greenway Ln','555-7899'),(7,'NextGen Media','782349012','712 Media Hub','555-6754'),(8,'Venture Global','518720349','239 Corporate Way','555-5645'),(9,'Bright Minds Academy','394861205','152 University Ave','555-2389'),(10,'Gourmet Foods Inc','657213840','1001 Culinary St','555-4721'),(11,'BuildSmart Construction','847109632','98 Contractor Ln','555-9832'),(12,'CityLine Transport','127890654','489 Commute Ave','555-2378'),(13,'WellCare Pharmaceuticals','931057846','204 Wellness Dr','555-7845'),(14,'LegalPath Partners','780345621','331 Barrister Rd','555-1998'),(15,'Skyline Real Estate','546781230','701 Skyline Blvd','555-4637'),(31,'ABC Corp',NULL,'123 Main St','555-5555');
/*!40000 ALTER TABLE `employer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `filing_status`
--

DROP TABLE IF EXISTS `filing_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `filing_status` (
  `Status_ID` int NOT NULL AUTO_INCREMENT,
  `Status_Name` varchar(50) NOT NULL,
  PRIMARY KEY (`Status_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filing_status`
--

LOCK TABLES `filing_status` WRITE;
/*!40000 ALTER TABLE `filing_status` DISABLE KEYS */;
INSERT INTO `filing_status` VALUES (1,'Single'),(2,'Married - Joint Return'),(3,'Married - Separate Return'),(4,'Head of Household with Dependent'),(5,'Widow(er) with Dependent Child'),(6,'Married - Filing Separately'),(7,'Qualifying Widow(er)'),(8,'Single Parent with Dependent Child'),(9,'Married - Joint Taxpayer'),(10,'Nonresident Alien'),(11,'Resident Alien Married to U.S. Citizen'),(12,'Nonresident Alien Filing Jointly'),(13,'Filing for Dependent Child'),(14,'Dual-Status Alien'),(15,'Taxpayer Living Abroad');
/*!40000 ALTER TABLE `filing_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `Payment_ID` int NOT NULL AUTO_INCREMENT,
  `Return_ID` int NOT NULL,
  `Payment_Amount` decimal(15,2) NOT NULL,
  `Payment_Date` date DEFAULT NULL,
  `Payment_Type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Payment_ID`),
  KEY `idx_return_id` (`Return_ID`),
  CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`Return_ID`) REFERENCES `tax_return` (`Return_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (17,1,5000.00,'2024-10-01','Credit Card');
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tax_form`
--

DROP TABLE IF EXISTS `tax_form`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tax_form` (
  `Form_ID` int NOT NULL AUTO_INCREMENT,
  `Form_Description` varchar(255) NOT NULL,
  `Form_Type` varchar(50) NOT NULL,
  PRIMARY KEY (`Form_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tax_form`
--

LOCK TABLES `tax_form` WRITE;
/*!40000 ALTER TABLE `tax_form` DISABLE KEYS */;
INSERT INTO `tax_form` VALUES (1,'Form W-2G: Certain Gambling Winnings','W-2G'),(2,'Form 1040-SR: U.S. Tax Return for Seniors','1040-SR'),(3,'Form 1099-NEC: Nonemployee Compensation','1099-NEC'),(4,'Form 1065-B: U.S. Return of Income for Electing Large Partnerships','1065-B'),(5,'Form 1120S: U.S. Income Tax Return for an S Corporation','1120S'),(6,'Form 7004: Application for Automatic Extension of Time To File Certain Business Income Tax','7004'),(7,'Form 944-X: Adjusted Employer’s Annual Federal Tax Return or Claim for Refund','944-X'),(8,'Form 945: Annual Return of Withheld Federal Income Tax','945'),(9,'Form 1098-E: Student Loan Interest Statement','1098-E'),(10,'Form 1099-SA: Distributions from an HSA, Archer MSA, or Medicare Advantage MSA','1099-SA'),(11,'Form 5498: IRA Contribution Information','5498'),(12,'Form 1099-B: Proceeds From Broker and Barter Exchange Transactions','1099-B'),(13,'Form 1099-Q: Payments from Qualified Education Programs','1099-Q'),(14,'Form 8832: Entity Classification Election','8832'),(15,'Form 8889: Health Savings Accounts (HSAs)','8889');
/*!40000 ALTER TABLE `tax_form` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tax_return`
--

DROP TABLE IF EXISTS `tax_return`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tax_return` (
  `Return_ID` int NOT NULL AUTO_INCREMENT,
  `Taxpayer_ID` int NOT NULL,
  `Filing_Year` int DEFAULT NULL,
  `Total_Income` decimal(15,2) DEFAULT NULL,
  `Total_Tax_Paid` decimal(15,2) DEFAULT NULL,
  `Due_Amount` decimal(15,2) DEFAULT NULL,
  `Refund_Amount` decimal(15,2) DEFAULT '0.00',
  `Return_Type` varchar(50) DEFAULT NULL,
  `Filing_Status` int DEFAULT NULL,
  PRIMARY KEY (`Return_ID`),
  KEY `Taxpayer_ID` (`Taxpayer_ID`),
  KEY `Filing_Status` (`Filing_Status`),
  CONSTRAINT `tax_return_ibfk_1` FOREIGN KEY (`Taxpayer_ID`) REFERENCES `taxpayer` (`Taxpayer_ID`),
  CONSTRAINT `tax_return_ibfk_2` FOREIGN KEY (`Filing_Status`) REFERENCES `filing_status` (`Status_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tax_return`
--

LOCK TABLES `tax_return` WRITE;
/*!40000 ALTER TABLE `tax_return` DISABLE KEYS */;
INSERT INTO `tax_return` VALUES (1,1,2022,110000.00,22000.00,1800.00,0.00,'Individual',1),(2,2,2022,115000.00,7600.00,1200.00,0.00,'Joint Return',2),(3,3,2021,93000.00,7400.00,0.00,7400.00,'Individual',3),(4,4,2022,63000.00,3100.00,600.00,0.00,'Head of Household',4),(5,5,2021,89000.00,6200.00,1000.00,0.00,'Widow(er)',5),(6,6,2021,102000.00,5800.00,2200.00,0.00,'Individual',1),(7,7,2022,47000.00,2600.00,800.00,0.00,'Joint Return',2),(8,8,2021,128000.00,9200.00,0.00,9200.00,'Individual',3),(9,9,2022,112000.00,7900.00,500.00,0.00,'Head of Household',4),(10,10,2021,96000.00,5000.00,0.00,5000.00,'Widow(er)',5),(11,11,2021,87000.00,6100.00,900.00,0.00,'Individual',1),(12,12,2022,122000.00,8700.00,300.00,0.00,'Joint Return',2),(13,13,2021,46000.00,2900.00,500.00,0.00,'Individual',3),(14,14,2022,118000.00,7800.00,700.00,0.00,'Head of Household',4),(15,15,2021,92000.00,4700.00,1100.00,3600.00,'Widow(er)',5),(31,1,2023,100000.00,20000.00,NULL,0.00,NULL,1);
/*!40000 ALTER TABLE `tax_return` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taxpayer`
--

DROP TABLE IF EXISTS `taxpayer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taxpayer` (
  `Taxpayer_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Social_Security_Number` char(9) DEFAULT NULL,
  `Phone_Number` varchar(15) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Taxpayer_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taxpayer`
--

LOCK TABLES `taxpayer` WRITE;
/*!40000 ALTER TABLE `taxpayer` DISABLE KEYS */;
INSERT INTO `taxpayer` VALUES (1,'Jane Doe','581047219','555-6732','jane.doe@example.com','32 Evergreen Ln'),(2,'Jessica Ramirez','901235647','555-7893','j.ramirez@outlook.com','852 Sunset Blvd'),(3,'Benjamin Price','672198304','555-2135','ben.price@example.com','44 Cedar Ave'),(4,'Sophia Henderson','341298765','555-8421','s.henderson@gmail.com','920 Willow St'),(5,'Lucas Bennett','854197602','555-5643','l.bennett@live.com','11 Birch Hill Ct'),(6,'Emily Morgan','672345890','555-9934','em.morgan@outlook.com','78 Pinecrest Rd'),(7,'James Russell','753210968','555-2346','jrussell@xyzmail.com','625 Bluebird Dr'),(8,'Grace Sullivan','438901672','555-7345','grace.sully@abc.com','1020 Lakeview Cir'),(9,'David Chapman','798542361','555-9811','d.chapman@myemail.com','309 Poplar Ln'),(10,'Avery Mitchell','123897456','555-5273','avery.mitch@gmail.com','1419 Elm St'),(11,'Olivia Fisher','561349028','555-1872','olivia.fisher@outlook.com','233 Maple Ridge Rd'),(12,'William Ward','327489156','555-9095','will.ward@example.com','310 Valley View Ave'),(13,'Hannah Grant','982356741','555-2217','h.grant@gmail.com','508 Lincoln St'),(14,'Nathaniel Hughes','763214590','555-3301','nate.hughes@outlook.com','786 Orchard Way'),(15,'Lily Turner','540189327','555-9876','lily.turner@abcmail.com','712 Forest Dr');
/*!40000 ALTER TABLE `taxpayer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `taxpayer_summary`
--

DROP TABLE IF EXISTS `taxpayer_summary`;
/*!50001 DROP VIEW IF EXISTS `taxpayer_summary`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `taxpayer_summary` AS SELECT 
 1 AS `Taxpayer_ID`,
 1 AS `Name`,
 1 AS `Total_Income`,
 1 AS `Total_Tax_Paid`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `taxpayer_summary`
--

/*!50001 DROP VIEW IF EXISTS `taxpayer_summary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `taxpayer_summary` AS select `t`.`Taxpayer_ID` AS `Taxpayer_ID`,`t`.`Name` AS `Name`,`tr`.`Total_Income` AS `Total_Income`,`tr`.`Total_Tax_Paid` AS `Total_Tax_Paid` from (`taxpayer` `t` join `tax_return` `tr` on((`t`.`Taxpayer_ID` = `tr`.`Taxpayer_ID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-25  4:32:12
