-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: barhop
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',3,'add_permission'),(6,'Can change permission',3,'change_permission'),(7,'Can delete permission',3,'delete_permission'),(8,'Can view permission',3,'view_permission'),(9,'Can add group',2,'add_group'),(10,'Can change group',2,'change_group'),(11,'Can delete group',2,'delete_group'),(12,'Can view group',2,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_profile'),(22,'Can change user',6,'change_profile'),(23,'Can delete user',6,'delete_profile'),(24,'Can view user',6,'view_profile'),(25,'Can add Reservation',7,'add_reservation'),(26,'Can change Reservation',7,'change_reservation'),(27,'Can delete Reservation',7,'delete_reservation'),(28,'Can view Reservation',7,'view_reservation'),(29,'Can add Seating',8,'add_seating'),(30,'Can change Seating',8,'change_seating'),(31,'Can delete Seating',8,'delete_seating'),(32,'Can view Seating',8,'view_seating'),(33,'Can add Table',9,'add_table'),(34,'Can change Table',9,'change_table'),(35,'Can delete Table',9,'delete_table'),(36,'Can view Table',9,'view_table'),(37,'Can add review',10,'add_review'),(38,'Can change review',10,'change_review'),(39,'Can delete review',10,'delete_review'),(40,'Can view review',10,'view_review'),(41,'Can add Amenity',11,'add_amenity'),(42,'Can change Amenity',11,'change_amenity'),(43,'Can delete Amenity',11,'delete_amenity'),(44,'Can view Amenity',11,'view_amenity'),(45,'Can add Bar Image',13,'add_barimage'),(46,'Can change Bar Image',13,'change_barimage'),(47,'Can delete Bar Image',13,'delete_barimage'),(48,'Can view Bar Image',13,'view_barimage'),(49,'Can add bar like',14,'add_barlike'),(50,'Can change bar like',14,'change_barlike'),(51,'Can delete bar like',14,'delete_barlike'),(52,'Can view bar like',14,'view_barlike'),(53,'Can add event',15,'add_event'),(54,'Can change event',15,'change_event'),(55,'Can delete event',15,'delete_event'),(56,'Can view event',15,'view_event'),(57,'Can add Bar',12,'add_bar'),(58,'Can change Bar',12,'change_bar'),(59,'Can delete Bar',12,'delete_bar'),(60,'Can view Bar',12,'view_bar');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bars_amenity`
--

DROP TABLE IF EXISTS `bars_amenity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bars_amenity` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(67) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bars_amenity`
--

LOCK TABLES `bars_amenity` WRITE;
/*!40000 ALTER TABLE `bars_amenity` DISABLE KEYS */;
INSERT INTO `bars_amenity` VALUES (1,'Free Wi-Fi');
/*!40000 ALTER TABLE `bars_amenity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bars_bar`
--

DROP TABLE IF EXISTS `bars_bar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bars_bar` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bar_draft` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `bar_name` varchar(67) NOT NULL,
  `bar_description` longtext NOT NULL,
  `bar_address` longtext NOT NULL,
  `bar_status` varchar(20) NOT NULL,
  `bar_start_time` time(6) NOT NULL,
  `bar_end_time` time(6) NOT NULL,
  `bar_owner_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bars_bar_bar_owner_id_27695410_fk_user_management_profile_id` (`bar_owner_id`),
  CONSTRAINT `bars_bar_bar_owner_id_27695410_fk_user_management_profile_id` FOREIGN KEY (`bar_owner_id`) REFERENCES `user_management_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bars_bar`
--

LOCK TABLES `bars_bar` WRITE;
/*!40000 ALTER TABLE `bars_bar` DISABLE KEYS */;
INSERT INTO `bars_bar` VALUES (1,0,'2026-04-17 15:12:23.554995','Blackbox Katipunan','Where the lights are low, the music hits just right, and every night feels like a story waiting to happen. 🍸✨\r\n\r\nWe’re your go-to spot for strong drinks, good company, and zero judgment—whether you’re here to celebrate, unwind, or just escape the usual. From signature cocktails to late-night chaos (the fun kind), we keep the vibes flowing till the last call.','299 Katipunan Ave','COLD','17:00:00.000000','02:00:00.000000',7);
/*!40000 ALTER TABLE `bars_bar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bars_bar_bar_amenities`
--

DROP TABLE IF EXISTS `bars_bar_bar_amenities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bars_bar_bar_amenities` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bar_id` bigint NOT NULL,
  `amenity_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bars_bar_bar_amenities_bar_id_amenity_id_a61d59ef_uniq` (`bar_id`,`amenity_id`),
  KEY `bars_bar_bar_amenities_amenity_id_e805bf9c_fk_bars_amenity_id` (`amenity_id`),
  CONSTRAINT `bars_bar_bar_amenities_amenity_id_e805bf9c_fk_bars_amenity_id` FOREIGN KEY (`amenity_id`) REFERENCES `bars_amenity` (`id`),
  CONSTRAINT `bars_bar_bar_amenities_bar_id_b43b5587_fk_bars_bar_id` FOREIGN KEY (`bar_id`) REFERENCES `bars_bar` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bars_bar_bar_amenities`
--

LOCK TABLES `bars_bar_bar_amenities` WRITE;
/*!40000 ALTER TABLE `bars_bar_bar_amenities` DISABLE KEYS */;
INSERT INTO `bars_bar_bar_amenities` VALUES (1,1,1);
/*!40000 ALTER TABLE `bars_bar_bar_amenities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bars_barimage`
--

DROP TABLE IF EXISTS `bars_barimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bars_barimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `bar_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bars_barimage_bar_id_0ff6c50d_fk_bars_bar_id` (`bar_id`),
  CONSTRAINT `bars_barimage_bar_id_0ff6c50d_fk_bars_bar_id` FOREIGN KEY (`bar_id`) REFERENCES `bars_bar` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bars_barimage`
--

LOCK TABLES `bars_barimage` WRITE;
/*!40000 ALTER TABLE `bars_barimage` DISABLE KEYS */;
INSERT INTO `bars_barimage` VALUES (1,'bars/1/Blackbox-Katipunan-2.jpg','2026-04-17 15:12:23.594659',1);
/*!40000 ALTER TABLE `bars_barimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bars_barlike`
--

DROP TABLE IF EXISTS `bars_barlike`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bars_barlike` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `expires_at` datetime(6) NOT NULL,
  `bar_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bars_barlike_user_id_bar_id_6eee1a4a_uniq` (`user_id`,`bar_id`),
  KEY `bars_barlike_bar_id_6786118f_fk_bars_bar_id` (`bar_id`),
  CONSTRAINT `bars_barlike_bar_id_6786118f_fk_bars_bar_id` FOREIGN KEY (`bar_id`) REFERENCES `bars_bar` (`id`),
  CONSTRAINT `bars_barlike_user_id_afa41674_fk_user_management_profile_id` FOREIGN KEY (`user_id`) REFERENCES `user_management_profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bars_barlike`
--

LOCK TABLES `bars_barlike` WRITE;
/*!40000 ALTER TABLE `bars_barlike` DISABLE KEYS */;
/*!40000 ALTER TABLE `bars_barlike` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bars_event`
--

DROP TABLE IF EXISTS `bars_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bars_event` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `event_date` date NOT NULL,
  `start_time` time(6) NOT NULL,
  `end_time` time(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `bar_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bars_event_bar_id_588c403f_fk_bars_bar_id` (`bar_id`),
  CONSTRAINT `bars_event_bar_id_588c403f_fk_bars_bar_id` FOREIGN KEY (`bar_id`) REFERENCES `bars_bar` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bars_event`
--

LOCK TABLES `bars_event` WRITE;
/*!40000 ALTER TABLE `bars_event` DISABLE KEYS */;
INSERT INTO `bars_event` VALUES (1,'Katipunan Kembot','Head on over to Katipunan\'s Kembot Kapital and move like you never knew you could 💃🕺Spot the special treat in the flyer 👀','2026-04-17','21:00:00.000000','22:00:00.000000','2026-04-17 15:21:37.214164',1);
/*!40000 ALTER TABLE `bars_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_user_management_profile_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_management_profile_id` FOREIGN KEY (`user_id`) REFERENCES `user_management_profile` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2026-04-17 15:12:40.580694','1','Free Wi-Fi',1,'[{\"added\": {}}]',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(11,'bars','amenity'),(12,'bars','bar'),(13,'bars','barimage'),(14,'bars','barlike'),(15,'bars','event'),(4,'contenttypes','contenttype'),(7,'reservations','reservation'),(8,'reservations','seating'),(9,'reservations','table'),(10,'reviews','review'),(5,'sessions','session'),(6,'user_management','profile');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-04-17 14:55:44.522424'),(2,'contenttypes','0002_remove_content_type_name','2026-04-17 14:55:44.710601'),(3,'auth','0001_initial','2026-04-17 14:55:45.803071'),(4,'auth','0002_alter_permission_name_max_length','2026-04-17 14:55:46.008963'),(5,'auth','0003_alter_user_email_max_length','2026-04-17 14:55:46.024474'),(6,'auth','0004_alter_user_username_opts','2026-04-17 14:55:46.037611'),(7,'auth','0005_alter_user_last_login_null','2026-04-17 14:55:46.051560'),(8,'auth','0006_require_contenttypes_0002','2026-04-17 14:55:46.064352'),(9,'auth','0007_alter_validators_add_error_messages','2026-04-17 14:55:46.078826'),(10,'auth','0008_alter_user_username_max_length','2026-04-17 14:55:46.095058'),(11,'auth','0009_alter_user_last_name_max_length','2026-04-17 14:55:46.111290'),(12,'auth','0010_alter_group_name_max_length','2026-04-17 14:55:46.149092'),(13,'auth','0011_update_proxy_permissions','2026-04-17 14:55:46.170027'),(14,'auth','0012_alter_user_first_name_max_length','2026-04-17 14:55:46.184166'),(15,'user_management','0001_initial','2026-04-17 14:55:47.194030'),(16,'admin','0001_initial','2026-04-17 14:55:47.630561'),(17,'admin','0002_logentry_remove_auto_add','2026-04-17 14:55:47.651990'),(18,'admin','0003_logentry_add_action_flag_choices','2026-04-17 14:55:47.669710'),(19,'bars','0001_initial','2026-04-17 14:55:48.439126'),(20,'bars','0002_initial','2026-04-17 14:55:49.385536'),(21,'reservations','0001_initial','2026-04-17 14:55:49.596376'),(22,'reservations','0002_initial','2026-04-17 14:55:50.677371'),(23,'reviews','0001_initial','2026-04-17 14:55:50.940167'),(24,'reviews','0002_initial','2026-04-17 14:55:51.154201'),(25,'sessions','0001_initial','2026-04-17 14:55:51.263220');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('83kepzuklwadaw9pxytsmytwv14nmi40','.eJxVizsOwjAQBe-yNYq88Sd2SiTOYe16HRyBXeCkQtwdgVJAOW_ePCHSvpW49_yIq8AMCKffjSndcvuIL1ZqdM01t204TB8uldb7-fj9xYV6gRl4MVbYOyYXvE46J22sEAelEUfHSgSZk-RJBcRkRnFmsV5NZBJ7dPB6AxzwNt0:1wDkoI:Y41474isA63V0oH8jUoTKNECoTuUjzlMU2iGKP7wADM','2026-05-01 15:08:46.640637');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations_reservation`
--

DROP TABLE IF EXISTS `reservations_reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations_reservation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `guests` int NOT NULL,
  `start_time` time(6) NOT NULL,
  `end_time` time(6) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `hopper_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reservations_reserva_hopper_id_652c8fdd_fk_user_mana` (`hopper_id`),
  CONSTRAINT `reservations_reserva_hopper_id_652c8fdd_fk_user_mana` FOREIGN KEY (`hopper_id`) REFERENCES `user_management_profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations_reservation`
--

LOCK TABLES `reservations_reservation` WRITE;
/*!40000 ALTER TABLE `reservations_reservation` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservations_reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations_reservation_tables`
--

DROP TABLE IF EXISTS `reservations_reservation_tables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations_reservation_tables` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `reservation_id` bigint NOT NULL,
  `table_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reservations_reservation_reservation_id_table_id_76e5b832_uniq` (`reservation_id`,`table_id`),
  KEY `reservations_reserva_table_id_569b559e_fk_reservati` (`table_id`),
  CONSTRAINT `reservations_reserva_reservation_id_d3233caa_fk_reservati` FOREIGN KEY (`reservation_id`) REFERENCES `reservations_reservation` (`id`),
  CONSTRAINT `reservations_reserva_table_id_569b559e_fk_reservati` FOREIGN KEY (`table_id`) REFERENCES `reservations_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations_reservation_tables`
--

LOCK TABLES `reservations_reservation_tables` WRITE;
/*!40000 ALTER TABLE `reservations_reservation_tables` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservations_reservation_tables` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations_seating`
--

DROP TABLE IF EXISTS `reservations_seating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations_seating` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `seating` varchar(255) NOT NULL,
  `capacity` int NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `bar_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reservations_seating_bar_id_3a0ff818_fk_bars_bar_id` (`bar_id`),
  CONSTRAINT `reservations_seating_bar_id_3a0ff818_fk_bars_bar_id` FOREIGN KEY (`bar_id`) REFERENCES `bars_bar` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations_seating`
--

LOCK TABLES `reservations_seating` WRITE;
/*!40000 ALTER TABLE `reservations_seating` DISABLE KEYS */;
INSERT INTO `reservations_seating` VALUES (1,'Standing',3,'',1),(2,'Booth',4,'',1);
/*!40000 ALTER TABLE `reservations_seating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations_table`
--

DROP TABLE IF EXISTS `reservations_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `table_type_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reservations_table_table_type_id_a668b0a2_fk_reservati` (`table_type_id`),
  CONSTRAINT `reservations_table_table_type_id_a668b0a2_fk_reservati` FOREIGN KEY (`table_type_id`) REFERENCES `reservations_seating` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations_table`
--

LOCK TABLES `reservations_table` WRITE;
/*!40000 ALTER TABLE `reservations_table` DISABLE KEYS */;
INSERT INTO `reservations_table` VALUES (1,1),(2,1),(3,1),(4,1),(5,1),(6,2),(7,2),(8,2),(9,2);
/*!40000 ALTER TABLE `reservations_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews_review`
--

DROP TABLE IF EXISTS `reviews_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `review_description` longtext,
  `review_date_created` datetime(6) NOT NULL,
  `review_rating` decimal(2,1) NOT NULL,
  `review_bar_id` bigint DEFAULT NULL,
  `review_user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reviews_review_review_bar_id_cf9644e4_fk_bars_bar_id` (`review_bar_id`),
  KEY `reviews_review_review_user_id_5d5efb2e_fk_user_mana` (`review_user_id`),
  CONSTRAINT `reviews_review_review_bar_id_cf9644e4_fk_bars_bar_id` FOREIGN KEY (`review_bar_id`) REFERENCES `bars_bar` (`id`),
  CONSTRAINT `reviews_review_review_user_id_5d5efb2e_fk_user_mana` FOREIGN KEY (`review_user_id`) REFERENCES `user_management_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews_review`
--

LOCK TABLES `reviews_review` WRITE;
/*!40000 ALTER TABLE `reviews_review` DISABLE KEYS */;
INSERT INTO `reviews_review` VALUES (1,'It\'s alright, bar food is mid and I\'ve had better drinks elsewhere though.','2026-04-17 15:19:40.397798',3.0,1,2);
/*!40000 ALTER TABLE `reviews_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_management_profile`
--

DROP TABLE IF EXISTS `user_management_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_management_profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(63) NOT NULL,
  `last_name` varchar(63) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(128) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `bio` longtext NOT NULL,
  `profile_image` varchar(100) DEFAULT NULL,
  `user_type` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_management_profile`
--

LOCK TABLES `user_management_profile` WRITE;
/*!40000 ALTER TABLE `user_management_profile` DISABLE KEYS */;
INSERT INTO `user_management_profile` VALUES (2,'2026-04-17 15:19:10.802178',0,0,1,'2026-04-17 15:00:10.895139','adararei','Adara Rei','Dimatulac','adara.dimatulac@student.ateneo.edu','pbkdf2_sha256$1200000$J2TILagAnlGxpMtVsVg3vU$xa32JH2Km9ot1UUP1VRqbse/gAkhmInaaz6ch+8oSnU=','2003-09-25','No bio yet.','','HOPPER'),(3,'2026-04-17 15:03:11.132667',0,0,1,'2026-04-17 15:03:09.733193','marcusjet','Marcus Jet','Esteban','marcus.esteban@student.ateneo.edu','pbkdf2_sha256$1200000$ANeo45gmQb2dhSDZ5YNu4Y$mVNVrUAq3Z2c8PN3yrktt4AccXkA+K7YNG7rvgXIpi4=','2026-04-01','No bio yet.','','HOPPER'),(4,'2026-04-17 15:03:40.041138',0,0,1,'2026-04-17 15:03:38.436163','david','David','Tormon','david.tormon@student.ateneo.edu','pbkdf2_sha256$1200000$U29pdGsretWlCBIbZpXq7J$di6vJEm8vy1ikd2SCD+/++inl02Illb23+nUiuaDYQw=','2026-04-01','No bio yet.','','HOPPER'),(5,'2026-04-17 15:04:50.238664',0,0,1,'2026-04-17 15:04:48.737457','miks','Mikylla Cherrizse','Cayago','mikylla.cayago@student.ateneo.edu','pbkdf2_sha256$1200000$lYzRF7CZOByVeMeQepBI8h$X3tInywhj9uxJh9Bbiyih7fH9loZ3P1ej5APaIJ6S9Y=','2026-04-01','No bio yet.','','HOPPER'),(6,'2026-04-17 15:06:00.162007',0,0,1,'2026-04-17 15:05:58.674225','hendrick','Hendrick','Paguio','hendrick.paguio@student.ateneo.edu','pbkdf2_sha256$1200000$lm1qtZjZN8Qod88RwTPdtJ$R+GqT+/i35Vq80aBzWSSVUsrTierkPDHOEDeBUs4jtM=','2026-04-01','No bio yet.','','HOPPER'),(7,'2026-04-17 15:20:13.751878',0,0,1,'2026-04-17 15:06:36.639019','johnsmith','John','Smith','john.smith@email.com','pbkdf2_sha256$1200000$Sdivv1aKZlgqHuPKZyobih$l7m/baW8B7flxku2+bA9dvC3tyAGa/95XiTWPeK3+fs=','2026-04-01','No bio yet.','','OWNER');
/*!40000 ALTER TABLE `user_management_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_management_profile_groups`
--

DROP TABLE IF EXISTS `user_management_profile_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_management_profile_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `profile_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_management_profile_groups_profile_id_group_id_fc6825b6_uniq` (`profile_id`,`group_id`),
  KEY `user_management_prof_group_id_2e949db0_fk_auth_grou` (`group_id`),
  CONSTRAINT `user_management_prof_group_id_2e949db0_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_management_prof_profile_id_23fac5f5_fk_user_mana` FOREIGN KEY (`profile_id`) REFERENCES `user_management_profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_management_profile_groups`
--

LOCK TABLES `user_management_profile_groups` WRITE;
/*!40000 ALTER TABLE `user_management_profile_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_management_profile_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_management_profile_user_permissions`
--

DROP TABLE IF EXISTS `user_management_profile_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_management_profile_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `profile_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_management_profile__profile_id_permission_id_dd7045b2_uniq` (`profile_id`,`permission_id`),
  KEY `user_management_prof_permission_id_a1a01e56_fk_auth_perm` (`permission_id`),
  CONSTRAINT `user_management_prof_permission_id_a1a01e56_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_management_prof_profile_id_8877beb9_fk_user_mana` FOREIGN KEY (`profile_id`) REFERENCES `user_management_profile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_management_profile_user_permissions`
--

LOCK TABLES `user_management_profile_user_permissions` WRITE;
/*!40000 ALTER TABLE `user_management_profile_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_management_profile_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-17 23:29:51
