-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: wordpress
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `wp_users`
--

DROP TABLE IF EXISTS `wp_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_users` (
  `ID` bigint unsigned NOT NULL AUTO_INCREMENT,
  `user_login` varchar(60) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `user_pass` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `user_nicename` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `user_email` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `user_url` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `user_registered` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `user_activation_key` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `user_status` int NOT NULL DEFAULT '0',
  `display_name` varchar(250) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`ID`),
  KEY `user_login_key` (`user_login`),
  KEY `user_nicename` (`user_nicename`),
  KEY `user_email` (`user_email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_users`
--

LOCK TABLES `wp_users` WRITE;
/*!40000 ALTER TABLE `wp_users` DISABLE KEYS */;
INSERT INTO `wp_users` VALUES (1,'admin','$P$BOsRbFUfY9zLkYaESOWREADWbjX8yU/','admin','purbey.santosh@hotmail.com','http://107.174.205.151:8000','2021-02-09 17:26:31','',0,'admin'),(2,'santosh1','$P$B8YXijc.aAJztDGNmLN9iRgYSA6wn/0','santosh1','santosh@gmail.com','','2021-02-09 17:36:57','',0,'Santosh1 Purbey1'),(3,'santosh2','$P$Bza.BatwbKDcIzyreKxBJ7DHLuvFNt1','santosh2','santosh2@hotmail.com','','2021-02-09 17:37:56','',0,'Santosh2 Purbey2'),(4,'santosh3','$P$BvEQmQyDe/T529Y3EzRDPRLK/hh3Hr.','santosh3','santosh3@gmail.com','','2021-02-09 17:38:56','',0,'Santosh3 Purbey'),(5,'santosh4','$P$Bfjx40n2SFT7RJ2YfaO0xfCFtjOkRx0','santosh4','santosh4@gmail.com','','2021-02-09 17:40:27','',0,'Santosh4 Purbey4'),(6,'santosh5','$P$BlQncO9CnyYLTtmIPF/twvcVnNr8dG0','santosh5','santosh5@gmail.com','','2021-02-09 17:41:14','',0,'santosh5 Purbey');
/*!40000 ALTER TABLE `wp_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_wc_customer_lookup`
--

DROP TABLE IF EXISTS `wp_wc_customer_lookup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_wc_customer_lookup` (
  `customer_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint unsigned DEFAULT NULL,
  `username` varchar(60) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `first_name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `last_name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `date_last_active` timestamp NULL DEFAULT NULL,
  `date_registered` timestamp NULL DEFAULT NULL,
  `country` char(2) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `postcode` varchar(20) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `city` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `state` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_wc_customer_lookup`
--

LOCK TABLES `wp_wc_customer_lookup` WRITE;
/*!40000 ALTER TABLE `wp_wc_customer_lookup` DISABLE KEYS */;
INSERT INTO `wp_wc_customer_lookup` VALUES (1,2,'santosh1','Santosh1','Purbey1','santosh@gmail.com','2021-02-09 00:00:00','2021-02-09 17:36:57','NP','44600','Kathmandu','BAG'),(2,3,'santosh2','Santosh2','Purbey2','santosh2@hotmail.com','2021-02-09 00:00:00','2021-02-09 17:37:56','NP','44600','Lalitpur','BAG');
/*!40000 ALTER TABLE `wp_wc_customer_lookup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_wc_order_coupon_lookup`
--

DROP TABLE IF EXISTS `wp_wc_order_coupon_lookup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_wc_order_coupon_lookup` (
  `order_id` bigint unsigned NOT NULL,
  `coupon_id` bigint NOT NULL,
  `date_created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `discount_amount` double NOT NULL DEFAULT '0',
  PRIMARY KEY (`order_id`,`coupon_id`),
  KEY `coupon_id` (`coupon_id`),
  KEY `date_created` (`date_created`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_wc_order_coupon_lookup`
--

LOCK TABLES `wp_wc_order_coupon_lookup` WRITE;
/*!40000 ALTER TABLE `wp_wc_order_coupon_lookup` DISABLE KEYS */;
INSERT INTO `wp_wc_order_coupon_lookup` VALUES (65,60,'2021-02-09 20:09:09',64.4),(66,62,'2021-02-09 20:14:21',100);
/*!40000 ALTER TABLE `wp_wc_order_coupon_lookup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_wc_order_product_lookup`
--

DROP TABLE IF EXISTS `wp_wc_order_product_lookup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_wc_order_product_lookup` (
  `order_item_id` bigint unsigned NOT NULL,
  `order_id` bigint unsigned NOT NULL,
  `product_id` bigint unsigned NOT NULL,
  `variation_id` bigint unsigned NOT NULL,
  `customer_id` bigint unsigned DEFAULT NULL,
  `date_created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `product_qty` int NOT NULL,
  `product_net_revenue` double NOT NULL DEFAULT '0',
  `product_gross_revenue` double NOT NULL DEFAULT '0',
  `coupon_amount` double NOT NULL DEFAULT '0',
  `tax_amount` double NOT NULL DEFAULT '0',
  `shipping_amount` double NOT NULL DEFAULT '0',
  `shipping_tax_amount` double NOT NULL DEFAULT '0',
  PRIMARY KEY (`order_item_id`),
  KEY `order_id` (`order_id`),
  KEY `product_id` (`product_id`),
  KEY `customer_id` (`customer_id`),
  KEY `date_created` (`date_created`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_wc_order_product_lookup`
--

LOCK TABLES `wp_wc_order_product_lookup` WRITE;
/*!40000 ALTER TABLE `wp_wc_order_product_lookup` DISABLE KEYS */;
INSERT INTO `wp_wc_order_product_lookup` VALUES (1,65,16,0,1,'2021-02-09 20:09:09',1,14.4,14.4,3.6,0,0,0),(2,65,24,0,1,'2021-02-09 20:09:09',2,24,24,6,0,0,0),(3,65,33,0,1,'2021-02-09 20:09:09',3,43.2,43.2,10.8,0,0,0),(4,65,17,0,1,'2021-02-09 20:09:09',4,176,176,44,0,0,0),(7,66,21,0,2,'2021-02-09 20:14:21',1,37.93,37.93,7.07,0,0,0),(8,66,14,0,2,'2021-02-09 20:14:21',2,75.86,75.86,14.14,0,0,0),(9,66,22,0,2,'2021-02-09 20:14:21',4,71.69,71.69,28.31,0,0,0),(10,66,25,0,2,'2021-02-09 20:14:21',4,0,0,8,0,0,0),(11,66,19,0,2,'2021-02-09 20:14:21',6,497.52,497.52,42.48,0,0,0);
/*!40000 ALTER TABLE `wp_wc_order_product_lookup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_wc_order_stats`
--

DROP TABLE IF EXISTS `wp_wc_order_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_wc_order_stats` (
  `order_id` bigint unsigned NOT NULL,
  `parent_id` bigint unsigned NOT NULL DEFAULT '0',
  `date_created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `date_created_gmt` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `num_items_sold` int NOT NULL DEFAULT '0',
  `total_sales` double NOT NULL DEFAULT '0',
  `tax_total` double NOT NULL DEFAULT '0',
  `shipping_total` double NOT NULL DEFAULT '0',
  `net_total` double NOT NULL DEFAULT '0',
  `returning_customer` tinyint(1) DEFAULT NULL,
  `status` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `customer_id` bigint unsigned NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `date_created` (`date_created`),
  KEY `customer_id` (`customer_id`),
  KEY `status` (`status`(191))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_wc_order_stats`
--

LOCK TABLES `wp_wc_order_stats` WRITE;
/*!40000 ALTER TABLE `wp_wc_order_stats` DISABLE KEYS */;
INSERT INTO `wp_wc_order_stats` VALUES (65,0,'2021-02-09 20:09:09','2021-02-09 20:09:09',10,257.6,0,0,257.6,0,'wc-on-hold',1),(66,0,'2021-02-09 20:14:21','2021-02-09 20:14:21',17,683,0,0,683,0,'wc-on-hold',2);
/*!40000 ALTER TABLE `wp_wc_order_stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_wc_product_meta_lookup`
--

DROP TABLE IF EXISTS `wp_wc_product_meta_lookup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_wc_product_meta_lookup` (
  `product_id` bigint NOT NULL,
  `sku` varchar(100) COLLATE utf8mb4_unicode_520_ci DEFAULT '',
  `virtual` tinyint(1) DEFAULT '0',
  `downloadable` tinyint(1) DEFAULT '0',
  `min_price` decimal(19,4) DEFAULT NULL,
  `max_price` decimal(19,4) DEFAULT NULL,
  `onsale` tinyint(1) DEFAULT '0',
  `stock_quantity` double DEFAULT NULL,
  `stock_status` varchar(100) COLLATE utf8mb4_unicode_520_ci DEFAULT 'instock',
  `rating_count` bigint DEFAULT '0',
  `average_rating` decimal(3,2) DEFAULT '0.00',
  `total_sales` bigint DEFAULT '0',
  `tax_status` varchar(100) COLLATE utf8mb4_unicode_520_ci DEFAULT 'taxable',
  `tax_class` varchar(100) COLLATE utf8mb4_unicode_520_ci DEFAULT '',
  PRIMARY KEY (`product_id`),
  KEY `virtual` (`virtual`),
  KEY `downloadable` (`downloadable`),
  KEY `stock_status` (`stock_status`),
  KEY `stock_quantity` (`stock_quantity`),
  KEY `onsale` (`onsale`),
  KEY `min_max_price` (`min_price`,`max_price`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_wc_product_meta_lookup`
--

LOCK TABLES `wp_wc_product_meta_lookup` WRITE;
/*!40000 ALTER TABLE `wp_wc_product_meta_lookup` DISABLE KEYS */;
INSERT INTO `wp_wc_product_meta_lookup` VALUES (12,'woo-vneck-tee',0,0,15.0000,20.0000,0,NULL,'instock',0,0.00,0,'taxable',''),(13,'woo-hoodie',0,0,42.0000,45.0000,0,NULL,'instock',0,0.00,0,'taxable',''),(14,'woo-hoodie-with-logo',0,0,45.0000,45.0000,0,NULL,'instock',0,0.00,2,'taxable',''),(15,'woo-tshirt',0,0,18.0000,18.0000,0,NULL,'instock',0,0.00,0,'taxable',''),(16,'woo-beanie',0,0,18.0000,18.0000,1,NULL,'instock',0,0.00,1,'taxable',''),(17,'woo-belt',0,0,55.0000,55.0000,1,NULL,'instock',0,0.00,4,'taxable',''),(18,'woo-cap',0,0,16.0000,16.0000,1,NULL,'instock',0,0.00,0,'taxable',''),(19,'woo-sunglasses',0,0,90.0000,90.0000,0,NULL,'instock',0,0.00,6,'taxable',''),(20,'woo-hoodie-with-pocket',0,0,35.0000,35.0000,1,NULL,'instock',0,0.00,0,'taxable',''),(21,'woo-hoodie-with-zipper',0,0,45.0000,45.0000,0,NULL,'instock',0,0.00,1,'taxable',''),(22,'woo-long-sleeve-tee',0,0,25.0000,25.0000,0,NULL,'instock',0,0.00,4,'taxable',''),(23,'woo-polo',0,0,20.0000,20.0000,0,NULL,'instock',0,0.00,0,'taxable',''),(24,'woo-album',1,1,15.0000,15.0000,0,NULL,'instock',0,0.00,2,'taxable',''),(25,'woo-single',1,1,2.0000,2.0000,1,NULL,'instock',0,0.00,4,'taxable',''),(26,'woo-vneck-tee-red',0,0,20.0000,20.0000,0,NULL,'instock',0,0.00,0,'taxable',''),(27,'woo-vneck-tee-green',0,0,20.0000,20.0000,0,NULL,'instock',0,0.00,0,'taxable',''),(28,'woo-vneck-tee-blue',0,0,15.0000,15.0000,0,NULL,'instock',0,0.00,0,'taxable',''),(29,'woo-hoodie-red',0,0,42.0000,42.0000,1,NULL,'instock',0,0.00,0,'taxable',''),(30,'woo-hoodie-green',0,0,45.0000,45.0000,0,NULL,'instock',0,0.00,0,'taxable',''),(31,'woo-hoodie-blue',0,0,45.0000,45.0000,0,NULL,'instock',0,0.00,0,'taxable',''),(32,'Woo-tshirt-logo',0,0,18.0000,18.0000,0,NULL,'instock',0,0.00,0,'taxable',''),(33,'Woo-beanie-logo',0,0,18.0000,18.0000,1,NULL,'instock',0,0.00,3,'taxable',''),(34,'logo-collection',0,0,18.0000,45.0000,0,NULL,'instock',0,0.00,0,'taxable',''),(35,'wp-pennant',0,0,11.0500,11.0500,0,NULL,'instock',0,0.00,0,'taxable',''),(36,'woo-hoodie-blue-logo',0,0,45.0000,45.0000,0,NULL,'instock',0,0.00,0,'taxable','');
/*!40000 ALTER TABLE `wp_wc_product_meta_lookup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_wc_tax_rate_classes`
--

DROP TABLE IF EXISTS `wp_wc_tax_rate_classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_wc_tax_rate_classes` (
  `tax_rate_class_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `slug` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`tax_rate_class_id`),
  UNIQUE KEY `slug` (`slug`(191))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_wc_tax_rate_classes`
--

LOCK TABLES `wp_wc_tax_rate_classes` WRITE;
/*!40000 ALTER TABLE `wp_wc_tax_rate_classes` DISABLE KEYS */;
INSERT INTO `wp_wc_tax_rate_classes` VALUES (1,'Reduced rate','reduced-rate'),(2,'Zero rate','zero-rate');
/*!40000 ALTER TABLE `wp_wc_tax_rate_classes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_woocommerce_attribute_taxonomies`
--

DROP TABLE IF EXISTS `wp_woocommerce_attribute_taxonomies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_woocommerce_attribute_taxonomies` (
  `attribute_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `attribute_name` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `attribute_label` varchar(200) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `attribute_type` varchar(20) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `attribute_orderby` varchar(20) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `attribute_public` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`attribute_id`),
  KEY `attribute_name` (`attribute_name`(20))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_woocommerce_attribute_taxonomies`
--

LOCK TABLES `wp_woocommerce_attribute_taxonomies` WRITE;
/*!40000 ALTER TABLE `wp_woocommerce_attribute_taxonomies` DISABLE KEYS */;
INSERT INTO `wp_woocommerce_attribute_taxonomies` VALUES (1,'color','Color','select','menu_order',0),(2,'size','Size','select','menu_order',0);
/*!40000 ALTER TABLE `wp_woocommerce_attribute_taxonomies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_woocommerce_order_itemmeta`
--

DROP TABLE IF EXISTS `wp_woocommerce_order_itemmeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_woocommerce_order_itemmeta` (
  `meta_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `order_item_id` bigint unsigned NOT NULL,
  `meta_key` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `meta_value` longtext COLLATE utf8mb4_unicode_520_ci,
  PRIMARY KEY (`meta_id`),
  KEY `order_item_id` (`order_item_id`),
  KEY `meta_key` (`meta_key`(32))
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_woocommerce_order_itemmeta`
--

LOCK TABLES `wp_woocommerce_order_itemmeta` WRITE;
/*!40000 ALTER TABLE `wp_woocommerce_order_itemmeta` DISABLE KEYS */;
INSERT INTO `wp_woocommerce_order_itemmeta` VALUES (1,1,'_product_id','16'),(2,1,'_variation_id','0'),(3,1,'_qty','1'),(4,1,'_tax_class',''),(5,1,'_line_subtotal','18'),(6,1,'_line_subtotal_tax','0'),(7,1,'_line_total','14.4'),(8,1,'_line_tax','0'),(9,1,'_line_tax_data','a:2:{s:5:\"total\";a:0:{}s:8:\"subtotal\";a:0:{}}'),(10,2,'_product_id','24'),(11,2,'_variation_id','0'),(12,2,'_qty','2'),(13,2,'_tax_class',''),(14,2,'_line_subtotal','30'),(15,2,'_line_subtotal_tax','0'),(16,2,'_line_total','24'),(17,2,'_line_tax','0'),(18,2,'_line_tax_data','a:2:{s:5:\"total\";a:0:{}s:8:\"subtotal\";a:0:{}}'),(19,3,'_product_id','33'),(20,3,'_variation_id','0'),(21,3,'_qty','3'),(22,3,'_tax_class',''),(23,3,'_line_subtotal','54'),(24,3,'_line_subtotal_tax','0'),(25,3,'_line_total','43.2'),(26,3,'_line_tax','0'),(27,3,'_line_tax_data','a:2:{s:5:\"total\";a:0:{}s:8:\"subtotal\";a:0:{}}'),(28,4,'_product_id','17'),(29,4,'_variation_id','0'),(30,4,'_qty','4'),(31,4,'_tax_class',''),(32,4,'_line_subtotal','220'),(33,4,'_line_subtotal_tax','0'),(34,4,'_line_total','176'),(35,4,'_line_tax','0'),(36,4,'_line_tax_data','a:2:{s:5:\"total\";a:0:{}s:8:\"subtotal\";a:0:{}}'),(37,5,'method_id','free_shipping'),(38,5,'instance_id','1'),(39,5,'cost','0.00'),(40,5,'total_tax','0'),(41,5,'taxes','a:1:{s:5:\"total\";a:0:{}}'),(42,5,'Items','Beanie &times; 1, Beanie with Logo &times; 3, Belt &times; 4'),(43,6,'discount_amount','64.4'),(44,6,'discount_amount_tax','0'),(45,6,'coupon_data','a:24:{s:2:\"id\";i:60;s:4:\"code\";s:8:\"2xfy3ffd\";s:6:\"amount\";s:2:\"20\";s:12:\"date_created\";O:11:\"WC_DateTime\":4:{s:13:\"\0*\0utc_offset\";i:0;s:4:\"date\";s:26:\"2021-02-09 17:46:51.000000\";s:13:\"timezone_type\";i:1;s:8:\"timezone\";s:6:\"+00:00\";}s:13:\"date_modified\";O:11:\"WC_DateTime\":4:{s:13:\"\0*\0utc_offset\";i:0;s:4:\"date\";s:26:\"2021-02-09 17:46:51.000000\";s:13:\"timezone_type\";i:1;s:8:\"timezone\";s:6:\"+00:00\";}s:12:\"date_expires\";N;s:13:\"discount_type\";s:7:\"percent\";s:11:\"description\";s:0:\"\";s:11:\"usage_count\";i:0;s:14:\"individual_use\";b:0;s:11:\"product_ids\";a:0:{}s:20:\"excluded_product_ids\";a:0:{}s:11:\"usage_limit\";i:0;s:20:\"usage_limit_per_user\";i:0;s:22:\"limit_usage_to_x_items\";N;s:13:\"free_shipping\";b:0;s:18:\"product_categories\";a:0:{}s:27:\"excluded_product_categories\";a:0:{}s:18:\"exclude_sale_items\";b:0;s:14:\"minimum_amount\";s:0:\"\";s:14:\"maximum_amount\";s:0:\"\";s:18:\"email_restrictions\";a:0:{}s:7:\"virtual\";b:0;s:9:\"meta_data\";a:0:{}}'),(46,7,'_product_id','21'),(47,7,'_variation_id','0'),(48,7,'_qty','1'),(49,7,'_tax_class',''),(50,7,'_line_subtotal','45'),(51,7,'_line_subtotal_tax','0'),(52,7,'_line_total','37.93'),(53,7,'_line_tax','0'),(54,7,'_line_tax_data','a:2:{s:5:\"total\";a:0:{}s:8:\"subtotal\";a:0:{}}'),(55,8,'_product_id','14'),(56,8,'_variation_id','0'),(57,8,'_qty','2'),(58,8,'_tax_class',''),(59,8,'_line_subtotal','90'),(60,8,'_line_subtotal_tax','0'),(61,8,'_line_total','75.86'),(62,8,'_line_tax','0'),(63,8,'_line_tax_data','a:2:{s:5:\"total\";a:0:{}s:8:\"subtotal\";a:0:{}}'),(64,9,'_product_id','22'),(65,9,'_variation_id','0'),(66,9,'_qty','4'),(67,9,'_tax_class',''),(68,9,'_line_subtotal','100'),(69,9,'_line_subtotal_tax','0'),(70,9,'_line_total','71.69'),(71,9,'_line_tax','0'),(72,9,'_line_tax_data','a:2:{s:5:\"total\";a:0:{}s:8:\"subtotal\";a:0:{}}'),(73,10,'_product_id','25'),(74,10,'_variation_id','0'),(75,10,'_qty','4'),(76,10,'_tax_class',''),(77,10,'_line_subtotal','8'),(78,10,'_line_subtotal_tax','0'),(79,10,'_line_total','0'),(80,10,'_line_tax','0'),(81,10,'_line_tax_data','a:2:{s:5:\"total\";a:0:{}s:8:\"subtotal\";a:0:{}}'),(82,11,'_product_id','19'),(83,11,'_variation_id','0'),(84,11,'_qty','6'),(85,11,'_tax_class',''),(86,11,'_line_subtotal','540'),(87,11,'_line_subtotal_tax','0'),(88,11,'_line_total','497.52'),(89,11,'_line_tax','0'),(90,11,'_line_tax_data','a:2:{s:5:\"total\";a:0:{}s:8:\"subtotal\";a:0:{}}'),(91,12,'method_id','free_shipping'),(92,12,'instance_id','1'),(93,12,'cost','0.00'),(94,12,'total_tax','0'),(95,12,'taxes','a:1:{s:5:\"total\";a:0:{}}'),(96,12,'Items','Hoodie with Zipper &times; 1, Hoodie with Logo &times; 2, Long Sleeve Tee &times; 4, Sunglasses &times; 6'),(97,13,'discount_amount','100'),(98,13,'discount_amount_tax','0'),(99,13,'coupon_data','a:24:{s:2:\"id\";i:62;s:4:\"code\";s:8:\"ra6nr9yw\";s:6:\"amount\";s:3:\"100\";s:12:\"date_created\";O:11:\"WC_DateTime\":4:{s:13:\"\0*\0utc_offset\";i:0;s:4:\"date\";s:26:\"2021-02-09 17:48:07.000000\";s:13:\"timezone_type\";i:1;s:8:\"timezone\";s:6:\"+00:00\";}s:13:\"date_modified\";O:11:\"WC_DateTime\":4:{s:13:\"\0*\0utc_offset\";i:0;s:4:\"date\";s:26:\"2021-02-09 17:48:07.000000\";s:13:\"timezone_type\";i:1;s:8:\"timezone\";s:6:\"+00:00\";}s:12:\"date_expires\";N;s:13:\"discount_type\";s:10:\"fixed_cart\";s:11:\"description\";s:0:\"\";s:11:\"usage_count\";i:0;s:14:\"individual_use\";b:0;s:11:\"product_ids\";a:0:{}s:20:\"excluded_product_ids\";a:0:{}s:11:\"usage_limit\";i:0;s:20:\"usage_limit_per_user\";i:0;s:22:\"limit_usage_to_x_items\";N;s:13:\"free_shipping\";b:1;s:18:\"product_categories\";a:0:{}s:27:\"excluded_product_categories\";a:0:{}s:18:\"exclude_sale_items\";b:0;s:14:\"minimum_amount\";s:0:\"\";s:14:\"maximum_amount\";s:0:\"\";s:18:\"email_restrictions\";a:0:{}s:7:\"virtual\";b:0;s:9:\"meta_data\";a:0:{}}');
/*!40000 ALTER TABLE `wp_woocommerce_order_itemmeta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_woocommerce_order_items`
--

DROP TABLE IF EXISTS `wp_woocommerce_order_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_woocommerce_order_items` (
  `order_item_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `order_item_name` text COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `order_item_type` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `order_id` bigint unsigned NOT NULL,
  PRIMARY KEY (`order_item_id`),
  KEY `order_id` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_woocommerce_order_items`
--

LOCK TABLES `wp_woocommerce_order_items` WRITE;
/*!40000 ALTER TABLE `wp_woocommerce_order_items` DISABLE KEYS */;
INSERT INTO `wp_woocommerce_order_items` VALUES (1,'Beanie','line_item',65),(2,'Album','line_item',65),(3,'Beanie with Logo','line_item',65),(4,'Belt','line_item',65),(5,'Free shipping','shipping',65),(6,'2xfy3ffd','coupon',65),(7,'Hoodie with Zipper','line_item',66),(8,'Hoodie with Logo','line_item',66),(9,'Long Sleeve Tee','line_item',66),(10,'Single','line_item',66),(11,'Sunglasses','line_item',66),(12,'Free shipping','shipping',66),(13,'ra6nr9yw','coupon',66);
/*!40000 ALTER TABLE `wp_woocommerce_order_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_woocommerce_shipping_zone_locations`
--

DROP TABLE IF EXISTS `wp_woocommerce_shipping_zone_locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_woocommerce_shipping_zone_locations` (
  `location_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `zone_id` bigint unsigned NOT NULL,
  `location_code` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `location_type` varchar(40) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`location_id`),
  KEY `location_id` (`location_id`),
  KEY `location_type_code` (`location_type`(10),`location_code`(20))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_woocommerce_shipping_zone_locations`
--

LOCK TABLES `wp_woocommerce_shipping_zone_locations` WRITE;
/*!40000 ALTER TABLE `wp_woocommerce_shipping_zone_locations` DISABLE KEYS */;
INSERT INTO `wp_woocommerce_shipping_zone_locations` VALUES (1,1,'NP','country');
/*!40000 ALTER TABLE `wp_woocommerce_shipping_zone_locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_woocommerce_shipping_zone_methods`
--

DROP TABLE IF EXISTS `wp_woocommerce_shipping_zone_methods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_woocommerce_shipping_zone_methods` (
  `zone_id` bigint unsigned NOT NULL,
  `instance_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `method_id` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `method_order` bigint unsigned NOT NULL,
  `is_enabled` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`instance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_woocommerce_shipping_zone_methods`
--

LOCK TABLES `wp_woocommerce_shipping_zone_methods` WRITE;
/*!40000 ALTER TABLE `wp_woocommerce_shipping_zone_methods` DISABLE KEYS */;
INSERT INTO `wp_woocommerce_shipping_zone_methods` VALUES (1,1,'free_shipping',1,1),(0,2,'flat_rate',1,1);
/*!40000 ALTER TABLE `wp_woocommerce_shipping_zone_methods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_woocommerce_shipping_zones`
--

DROP TABLE IF EXISTS `wp_woocommerce_shipping_zones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_woocommerce_shipping_zones` (
  `zone_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `zone_name` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `zone_order` bigint unsigned NOT NULL,
  PRIMARY KEY (`zone_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_woocommerce_shipping_zones`
--

LOCK TABLES `wp_woocommerce_shipping_zones` WRITE;
/*!40000 ALTER TABLE `wp_woocommerce_shipping_zones` DISABLE KEYS */;
INSERT INTO `wp_woocommerce_shipping_zones` VALUES (1,'Nepal',0);
/*!40000 ALTER TABLE `wp_woocommerce_shipping_zones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_woocommerce_tax_rate_locations`
--

DROP TABLE IF EXISTS `wp_woocommerce_tax_rate_locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_woocommerce_tax_rate_locations` (
  `location_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `location_code` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `tax_rate_id` bigint unsigned NOT NULL,
  `location_type` varchar(40) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`location_id`),
  KEY `tax_rate_id` (`tax_rate_id`),
  KEY `location_type_code` (`location_type`(10),`location_code`(20))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_woocommerce_tax_rate_locations`
--

LOCK TABLES `wp_woocommerce_tax_rate_locations` WRITE;
/*!40000 ALTER TABLE `wp_woocommerce_tax_rate_locations` DISABLE KEYS */;
INSERT INTO `wp_woocommerce_tax_rate_locations` VALUES (1,'12345',5,'postcode'),(2,'123456',5,'postcode');
/*!40000 ALTER TABLE `wp_woocommerce_tax_rate_locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wp_woocommerce_tax_rates`
--

DROP TABLE IF EXISTS `wp_woocommerce_tax_rates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wp_woocommerce_tax_rates` (
  `tax_rate_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `tax_rate_country` varchar(2) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `tax_rate_state` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `tax_rate` varchar(8) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `tax_rate_name` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `tax_rate_priority` bigint unsigned NOT NULL,
  `tax_rate_compound` int NOT NULL DEFAULT '0',
  `tax_rate_shipping` int NOT NULL DEFAULT '1',
  `tax_rate_order` bigint unsigned NOT NULL,
  `tax_rate_class` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`tax_rate_id`),
  KEY `tax_rate_country` (`tax_rate_country`),
  KEY `tax_rate_state` (`tax_rate_state`(2)),
  KEY `tax_rate_class` (`tax_rate_class`(10)),
  KEY `tax_rate_priority` (`tax_rate_priority`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_woocommerce_tax_rates`
--

LOCK TABLES `wp_woocommerce_tax_rates` WRITE;
/*!40000 ALTER TABLE `wp_woocommerce_tax_rates` DISABLE KEYS */;
INSERT INTO `wp_woocommerce_tax_rates` VALUES (1,'GB','','20.0000','VAT',1,1,1,0,''),(2,'GB','','5.0000','VAT',1,1,1,1,'reduced-rate'),(3,'GB','','0.0000','VAT',1,1,1,2,'zero-rate'),(4,'US','','10.0000','US',1,1,1,3,''),(5,'US','AL','2.0000','US AL',2,1,1,4,'');
/*!40000 ALTER TABLE `wp_woocommerce_tax_rates` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-18 12:42:45
