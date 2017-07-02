-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: localhost    Database: userservice
-- ------------------------------------------------------
-- Server version	5.7.18-0ubuntu0.16.04.1

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
-- Table structure for table `userlogs`
--

DROP TABLE IF EXISTS `userlogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userlogs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `log` varchar(128) NOT NULL,
  `data` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `access` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userlogs`
--

LOCK TABLES `userlogs` WRITE;
/*!40000 ALTER TABLE `userlogs` DISABLE KEYS */;
INSERT INTO `userlogs` VALUES (2,'efrerg','2017-07-02 19:34:56',0),(6,'login: hhh password: ffff','2017-07-02 19:40:28',0),(7,'login: test password: test','2017-07-02 19:40:51',1),(8,'login: test password: test','2017-07-02 19:44:04',1),(9,'login: tr password: hd','2017-07-02 19:44:11',0),(10,'login: dsd password: sdsd','2017-07-02 19:47:22',0),(11,'login: tehhg password: jh','2017-07-02 19:48:55',0),(12,'login: test password: test','2017-07-02 19:49:05',1),(13,'login: test password: test','2017-07-02 19:50:35',1),(14,'login: test password: test','2017-07-02 19:55:34',1),(15,'login: test password: test','2017-07-02 19:56:08',1),(16,'login: test password: test','2017-07-02 19:56:48',1),(17,'login: test password: test','2017-07-02 20:08:29',1),(18,'login: test password: test','2017-07-02 20:08:42',1),(19,'login: test password: test','2017-07-02 20:08:58',1),(20,'login: test password: test','2017-07-02 20:10:16',1),(21,'login: test password: test','2017-07-02 20:11:44',1),(22,'login: test password: test','2017-07-02 20:12:31',1),(23,'login: test password: test','2017-07-02 20:13:13',1),(24,'login: test password: test','2017-07-02 20:13:30',1),(25,'login: test2 password: test2','2017-07-02 20:13:38',1),(26,'login: test password: test','2017-07-02 20:22:29',1),(27,'login: test password: test','2017-07-02 20:24:46',1),(28,'login: test password: test','2017-07-02 20:25:04',1),(29,'login: test password: test','2017-07-02 20:25:28',1);
/*!40000 ALTER TABLE `userlogs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-07-02 20:56:49
