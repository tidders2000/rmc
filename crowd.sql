-- MySQL dump 10.13  Distrib 5.5.57, for debian-linux-gnu (x86_64)
--
-- Host: 0.0.0.0    Database: crowd
-- ------------------------------------------------------
-- Server version	5.5.57-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `badges`
--

DROP TABLE IF EXISTS `badges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `badges` (
  `badgeid` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `badgenomId` varchar(30) DEFAULT NULL,
  `badge` varchar(128) DEFAULT NULL,
  `badgegiver` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`badgeid`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `badges`
--

LOCK TABLES `badges` WRITE;
/*!40000 ALTER TABLE `badges` DISABLE KEYS */;
INSERT INTO `badges` VALUES (1,'84','money.png','84'),(2,'84','birthday-cake.png','84'),(3,'84','birthday-cake.png','84'),(4,'84','money.png','84'),(5,'89','birthday-cake.png','89'),(6,'89','money.png','89'),(7,'88','deal.png','88'),(8,'88','deal.png','88'),(9,'88','deal.png','88'),(10,'88','medal.png','88'),(11,'94','alcohol.png','94'),(12,'94','leaf.png','94'),(13,'94','alcohol.png','94'),(14,'95','deal.png','95'),(15,'95','deal.png','96'),(16,'98','medal.png','98'),(17,'98','deal.png','98'),(18,'98','birthday-cake.png','98'),(19,'98','alcohol.png','98'),(20,'98','leaf.png','95'),(21,'95','alcohol.png','98'),(22,'96','medal.png','99'),(23,'96','birthday-cake.png','95'),(24,'95','deal.png','99');
/*!40000 ALTER TABLE `badges` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `feedbackid` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `nominatedId` varchar(30) DEFAULT NULL,
  `feedbackTitle` varchar(128) DEFAULT NULL,
  `teamId` int(11) DEFAULT NULL,
  `feedbacktext` varchar(255) DEFAULT NULL,
  `nominatorId` int(11) DEFAULT NULL,
  `fbdate` date DEFAULT NULL,
  PRIMARY KEY (`feedbackid`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (11,'81','feedback',2,'here is some feedback',84,NULL),(12,'81','here is a test',2,'vgvgvgvgvgvgvgv',84,NULL),(13,'81','here is a test',2,'vgvgvgvgvgvgvgv',84,NULL),(14,'81','you are awesome',2,'Had to write as you are incredible',84,'0000-00-00'),(15,'81','more testing',2,'testing',84,'0000-00-00'),(16,'84','here is some feedback',1,'ifjdnvfijwnbvijwfnbvijnfrbvinrbvhwrnhvnrhnv',84,'0000-00-00'),(17,'84','another ththththt',1,'dnvndfsjvdfnjnvdjfnvjfdnvjdfnjvnfjinv',84,'0000-00-00'),(18,'84','dwvjdnsvjdnsvjdns',1,'mscdnscjjndsjcndjsnnc',84,'0000-00-00'),(19,'81','titledmvndkcnvdjkncvd',2,'samcdkscjd cjd c ',84,'0000-00-00'),(20,'84','dvnjfndvjfnjvn',1,'scjdsncjdnscjndscn',84,'0000-00-00'),(21,'81','titledscdjncjdncjndqwc',2,'sncjdwncjdwncjdwncjwqn',84,'2019-03-30'),(22,'84','titledvkdmcqkodmckmdw',1,'dnvjdnvjndcjs',84,'2019-03-30'),(23,NULL,NULL,NULL,NULL,NULL,'2019-03-30'),(24,'84','titledvkdmcqkodmckmdw',1,'dnvjdnvjndcjs',84,'2019-03-30'),(25,'86','Bong is fantastic',2,'Anabelle done some really great work with the G',84,'2019-03-31'),(26,'94','Here is some lovely feedback',2,'nvewfijvnijefnvwijefnvjefnvjwennwejinvjwenvjnewjvnjienv',89,'2019-04-02'),(27,'98','You were amazing',2,'When you helped that customer with the finance thing. So patient!',99,'2019-04-05'),(28,'98','You done a great job',2,'Thanks for covering last nights shift. It was great work.',95,'2019-04-05'),(29,'98','What a great job',2,'Completely amazed by the job you did of reorganising the stationary. So easy to find post its now. Well done',96,'2019-04-07'),(30,'98','Brilliant!',2,'Loving your enthusiasim',99,'2019-04-07'),(31,'95','You were great when I needed some help earlier',2,'Sometimes you just need a kind ear and what you said today really helped me. Thank you',98,'2019-04-09'),(32,'96','Smashing super great',2,'You are incredible when you start organising people. Never seen the office party so well organised.',99,'2019-04-10'),(33,'96','I really like your report',1,'Your report on the customer insights was really well written and so useful.',95,'2019-04-10'),(34,'95','Your the man',1,'Thanks for the training today. Feel really empowered',99,'2019-04-10'),(35,'95','Top job',1,'On clearing that old stock room. Rubbish job that you freely volunteered for',98,'2019-04-10'),(36,'95','I thought you were brave',1,'When you took on that angry customer today',100,'2019-04-11'),(37,'95','I thought you were brave',1,'When you took on that angry customer today',100,'2019-04-11');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `locationname` varchar(30) DEFAULT NULL,
  `addressline1` varchar(30) DEFAULT NULL,
  `addressline2` varchar(30) DEFAULT NULL,
  `addressline3` varchar(30) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `county` varchar(30) DEFAULT NULL,
  `postcode` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (3,'LocationA','1 London road','Barnes',NULL,'London','London','LN16TC'),(4,'Please add',NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teamname`
--

DROP TABLE IF EXISTS `teamname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teamname` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `teamname` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teamname`
--

LOCK TABLES `teamname` WRITE;
/*!40000 ALTER TABLE `teamname` DISABLE KEYS */;
INSERT INTO `teamname` VALUES (1,'Accounting'),(2,'Audit'),(3,'Hr'),(4,'Sales'),(5,'IT'),(6,'Executive');
/*!40000 ALTER TABLE `teamname` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `profileImage` varchar(60) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `startdate` date DEFAULT NULL,
  `biog` varchar(255) DEFAULT NULL,
  `teamId` int(11) DEFAULT NULL,
  `locationId` int(11) DEFAULT NULL,
  `reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (93,'Simon Tidman','nyc.jpg','simon.tid@btinternet.com',NULL,NULL,2,3,'2019-04-05 09:47:44','pbkdf2:sha256:50000$Fpjtksj4$99090b90b8897ae4d55c6a5530ae9ce6938190a7403525d1b2eedffb4f332831'),(95,'testuserone','monk_prof.png','testuserone@email.com','2019-08-04','None',1,3,'2019-04-10 22:06:24','pbkdf2:sha256:50000$JMYbu9hC$3f93cd9037357f00161f4a0036c26b53e716566a891a07bf2a0b5588991c73bf'),(96,'testusertwo','girlprofile.jpeg','testusertwo@email.com','2019-06-01','I love working in audit',1,3,'2019-04-11 19:39:23','pbkdf2:sha256:50000$fCrIVQTb$b2f3b2e9f68b7e14c3d5d00b5df75416bef187b54413c8f5fe28b5714892692e'),(98,'testuserfour','cartoon_girl.jpg','testuserfour@email.com','2018-02-12','I am a great person and I want you all to let me know how amazing I am!',1,3,'2019-04-10 22:09:57','pbkdf2:sha256:50000$sGUPmhZD$853a1778ba02dd85c20c13f6a7c96b3b3555625000525e942a8e264ba3cc0c71'),(99,'testuserthree','powerpuff.jpg','testuserthree@email.com','2019-04-03','None',1,4,'2019-04-10 22:05:43','pbkdf2:sha256:50000$ZFFys3R8$024d3df540bf6a1fc61cef7b3145e7dccf12763b57ab87055e977eb04e56e001'),(100,'testuserfive','pink_girl.jpg','testuserfive@email.com',NULL,NULL,1,4,'2019-04-11 19:44:22','pbkdf2:sha256:50000$SPSNItmF$4fdbaa1f2b5d257fae492fb65d94660e848f874168fdf36e50e7256bcc073bd2');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-12 20:12:35
