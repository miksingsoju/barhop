LOCK TABLES `user_management_profile` WRITE;
/*!40000 ALTER TABLE `user_management_profile` DISABLE KEYS */;
INSERT INTO `user_management_profile` VALUES (2,'2026-04-17 15:19:10.802178',0,0,1,'2026-04-17 15:00:10.895139','adararei','Adara Rei','Dimatulac','adara.dimatulac@student.ateneo.edu','pbkdf2_sha256$1200000$J2TILagAnlGxpMtVsVg3vU$xa32JH2Km9ot1UUP1VRqbse/gAkhmInaaz6ch+8oSnU=','2003-09-25','No bio yet.','','HOPPER'),(3,'2026-04-17 15:03:11.132667',0,0,1,'2026-04-17 15:03:09.733193','marcusjet','Marcus Jet','Esteban','marcus.esteban@student.ateneo.edu','pbkdf2_sha256$1200000$ANeo45gmQb2dhSDZ5YNu4Y$mVNVrUAq3Z2c8PN3yrktt4AccXkA+K7YNG7rvgXIpi4=','2026-04-01','No bio yet.','','HOPPER'),(4,'2026-04-17 15:03:40.041138',0,0,1,'2026-04-17 15:03:38.436163','david','David','Tormon','david.tormon@student.ateneo.edu','pbkdf2_sha256$1200000$U29pdGsretWlCBIbZpXq7J$di6vJEm8vy1ikd2SCD+/++inl02Illb23+nUiuaDYQw=','2026-04-01','No bio yet.','','HOPPER'),(5,'2026-04-17 15:04:50.238664',0,0,1,'2026-04-17 15:04:48.737457','miks','Mikylla Cherrizse','Cayago','mikylla.cayago@student.ateneo.edu','pbkdf2_sha256$1200000$lYzRF7CZOByVeMeQepBI8h$X3tInywhj9uxJh9Bbiyih7fH9loZ3P1ej5APaIJ6S9Y=','2026-04-01','No bio yet.','','HOPPER'),(6,'2026-04-17 15:06:00.162007',0,0,1,'2026-04-17 15:05:58.674225','hendrick','Hendrick','Paguio','hendrick.paguio@student.ateneo.edu','pbkdf2_sha256$1200000$lm1qtZjZN8Qod88RwTPdtJ$R+GqT+/i35Vq80aBzWSSVUsrTierkPDHOEDeBUs4jtM=','2026-04-01','No bio yet.','','HOPPER'),(7,'2026-04-17 15:20:13.751878',0,0,1,'2026-04-17 15:06:36.639019','johnsmith','John','Smith','john.smith@email.com','pbkdf2_sha256$1200000$Sdivv1aKZlgqHuPKZyobih$l7m/baW8B7flxku2+bA9dvC3tyAGa/95XiTWPeK3+fs=','2026-04-01','No bio yet.','','OWNER');
/*!40000 ALTER TABLE `user_management_profile` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `bars_amenity` WRITE;
/*!40000 ALTER TABLE `bars_amenity` DISABLE KEYS */;
INSERT INTO `bars_amenity` VALUES (1,'Free Wi-Fi');
/*!40000 ALTER TABLE `bars_amenity` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `bars_bar` WRITE;
/*!40000 ALTER TABLE `bars_bar` DISABLE KEYS */;
INSERT INTO `bars_bar` VALUES (1,0,'2026-04-17 15:12:23.554995','Blackbox Katipunan','Where the lights are low, the music hits just right, and every night feels like a story waiting to happen. 🍸✨\r\n\r\nWe’re your go-to spot for strong drinks, good company, and zero judgment—whether you’re here to celebrate, unwind, or just escape the usual. From signature cocktails to late-night chaos (the fun kind), we keep the vibes flowing till the last call.','299 Katipunan Ave','COLD','17:00:00.000000','02:00:00.000000',7);
/*!40000 ALTER TABLE `bars_bar` ENABLE KEYS */;
UNLOCK TABLES;


LOCK TABLES `bars_bar_bar_amenities` WRITE;
/*!40000 ALTER TABLE `bars_bar_bar_amenities` DISABLE KEYS */;
INSERT INTO `bars_bar_bar_amenities` VALUES (1,1,1);
/*!40000 ALTER TABLE `bars_bar_bar_amenities` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `bars_barimage` WRITE;
/*!40000 ALTER TABLE `bars_barimage` DISABLE KEYS */;
INSERT INTO `bars_barimage` VALUES (1,'bars/1/Blackbox-Katipunan-2.jpg','2026-04-17 15:12:23.594659',1);
/*!40000 ALTER TABLE `bars_barimage` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `bars_barlike` WRITE;
/*!40000 ALTER TABLE `bars_barlike` DISABLE KEYS */;
/*!40000 ALTER TABLE `bars_barlike` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `bars_event` WRITE;
/*!40000 ALTER TABLE `bars_event` DISABLE KEYS */;
INSERT INTO `bars_event` VALUES (1,'Katipunan Kembot','Head on over to Katipunan\'s Kembot Kapital and move like you never knew you could 💃🕺Spot the special treat in the flyer 👀','2026-04-17','21:00:00.000000','22:00:00.000000','2026-04-17 15:21:37.214164',1);
/*!40000 ALTER TABLE `bars_event` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2026-04-17 15:12:40.580694','1','Free Wi-Fi',1,'[{\"added\": {}}]',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `reservations_seating` WRITE;
/*!40000 ALTER TABLE `reservations_seating` DISABLE KEYS */;
INSERT INTO `reservations_seating` VALUES (1,'Standing',3,'',1),(2,'Booth',4,'',1);
/*!40000 ALTER TABLE `reservations_seating` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `reservations_table` WRITE;
/*!40000 ALTER TABLE `reservations_table` DISABLE KEYS */;
INSERT INTO `reservations_table` VALUES (1,1),(2,1),(3,1),(4,1),(5,1),(6,2),(7,2),(8,2),(9,2);
/*!40000 ALTER TABLE `reservations_table` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `reviews_review` WRITE;
/*!40000 ALTER TABLE `reviews_review` DISABLE KEYS */;
INSERT INTO `reviews_review` VALUES (1,'It\'s alright, bar food is mid and I\'ve had better drinks elsewhere though.','2026-04-17 15:19:40.397798',3.0,1,2);
/*!40000 ALTER TABLE `reviews_review` ENABLE KEYS */;
UNLOCK TABLES;
