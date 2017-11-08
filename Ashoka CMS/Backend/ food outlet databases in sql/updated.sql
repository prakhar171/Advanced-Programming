-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: FOODOUTLET
-- ------------------------------------------------------
-- Server version	5.7.20

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
-- Table structure for table `THC`
--

DROP TABLE IF EXISTS `THC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `THC` (
  `Category` char(20) DEFAULT 'food',
  `Fooditem` char(30) DEFAULT NULL,
  `Price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `THC`
--

LOCK TABLES `THC` WRITE;
/*!40000 ALTER TABLE `THC` DISABLE KEYS */;
INSERT INTO `THC` VALUES ('protein','Afghani Cream',160),('fries','belgian fries',110),('omelette','cheese',50),('fries','cheesy fries',80),('omelette','chicken sausage',70),('omelette','chicken tikka',80),('protein','Herb Roast',140),('omelette','hummus',60),('omelette','paneer',70),('omelette','plain',30),('fries','Ranch fries',130),('protein','Roast chicken',80),('Red Pasta','classic',80),('Red Pasta','farmhouse',100),('Red Pasta','sausage',100),('Red Pasta','shred chicken',120),('Red Pasta','extra cheesy',100),('Red Pasta','hummus',110),('white Pasta','classic white',90),('white Pasta','farmhouse white',130),('white Pasta','sausage white',120),('white Pasta','shred chicken white',140),('white Pasta','extra cheesy and white sauce',150),('white Pasta',' white sauce',120),('Hot dogs','Chicken sausage',50),('Hot dogs','Bacon and Sausage',110),('Hot dogs','Masala Paneer',50),('Hot dogs','Chicken and Cheeae',70),('Hot dogs','Jalapeno Sausage',70),('Grilled Sandwhiches','coleslaw',30),('Grilled Sandwhiches','cheese',50),('Grilled Sandwhiches','sausage',60),('Grilled Sandwhiches','pizza cheese',60),('Grilled Sandwhiches','paneer',60),('Pizza','Margherita',100),('Pizza','Chicken sausage',130),('Pizza','Tangy paneer and jalapeno',140),('Pizza','Bacon and chicken seekh',160),('Pizza','onion capsicum',120),('Pizza','farmhouse',130),('Pizza','Chicken Tikka',150),('Pizza','Hawaiian vaaru',140),('kathi rolls','Chicken seekh',130),('kathi rolls','paneer',130),('kathi rolls','paneer cheese',140),('kathi rolls','southwest',160),('kathi rolls','Chicken tikka',150),('kathi rolls','hummus',110),('kathi rolls','shiv roll',230),('kathi rolls','dream roll',370),('French Toast','plain',40),('French Toast','butter honey',70),('French Toast','cheese',60),('French Toast','blueberry',80),('waffles','butter and honey',60),('waffles','fudge and ice creme',100),('waffles','bomb waffle',120),('pancakes','butter and honey',60),('pancakes','fudge and ice creme',80),('pancakes','bomb waffle',120),('pancakes','peanut butter',100),('maggi/wai wai','masala',30),('maggi/wai wai','cheese',50),('maggi/wai wai','egg',50),('maggi/wai wai','hummus',60),('maggi/wai wai','seekh',70),('maggi/wai wai','bacon',90),('maggi/wai wai','chicken tikka',80),('maggi/wai wai','butter chicken',100),('bakes cheese nachos','El classico',80),('bakes cheese nachos','cowboy veggie',100),('bakes cheese nachos','meat overload',150),('bakes cheese nachos','Bacon Fiesta',140),('Pav(sliders)','Anda pav',20),('Pav(sliders)','chicken seekh',40),('Pav(sliders)','chipotle',40),('Pav(sliders)','chicken tikka',40),('Pav(sliders)','paneer',40),('Pav(sliders)','hummus',40),('Marshmallow bun','Chocolate fudge',30),('Marshmallow bun','Peanut butter',30),('Marshmallow bun','Mix up',50),('Marshmallow bun','Ice cream n fudge Sandhwhich',50),('Thick milk shakes','Oreo',80),('Thick milk shakes','Chocolate/mango/banana',50),('Thick milk shakes','blueberry/kiwi',70),('Thick milk shakes','butterscotch/strawberry',50),('Thick milk shakes','kit kat loaded',90),('Thick milk shakes','Honey lemon ginger',30),('Thick milk shakes','cold coffee',50),('Thick milk shakes','lemon soda',30),('Thick milk shakes','nestea ice tea',30),('Thick milk shakes','Bournvita marshmallow',40),('Thick milk shakes','Cold drinks',20),('momos','chicken',80),('momos','vegetable',60),('burgers','veggie',60),('burgers','chicken patty',90),('burgers','Egg bacon cheese',110),('burgers','chicken cheese',100),('burgers','jenga tower',200),('combo','mine fries+burger',100),('combo','mini fries+chicken burger',130);
/*!40000 ALTER TABLE `THC` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chicago`
--

DROP TABLE IF EXISTS `chicago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chicago` (
  `category` char(20) DEFAULT NULL,
  `fooditem` char(40) DEFAULT NULL,
  `price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chicago`
--

LOCK TABLES `chicago` WRITE;
/*!40000 ALTER TABLE `chicago` DISABLE KEYS */;
INSERT INTO `chicago` VALUES ('pizza(slice)','cheese',90),('pizza(slice)','double cheese',110),('pizza(slice)','onion capsicum',120),('pizza(slice)','olive jalapeno',120),('pizza(slice)','pineapple jalapeno',130),('pizza(slice)','onion capsicum mushroom',135),('pizza(slice)','corn jalapeno red paprika',135),('pizza(slice)','chicken ham',110),('pizza(slice)','pepperoni',120),('pizza(slice)','mutton',120),('pizza(slice)','pepperoni jalapeno',135),('pizza(slice)','onion capsicum mutton',140),('pizza(slice)','BBQ smoked chicken corn',145),('pizza(slice)','chicken tikka BBQ ham onion',165),('maggi','masala',30),('maggi','veg maggi',45),('maggi','cheese maggi',50),('garlic bread','cheese',40),('garlic bread','vegetarian',60),('garlic bread','non vegetarian',70),('beverages','virgin mohito',60),('beverages','friut beer',60),('beverages','lemon fizz',50),('beverages','coke',35),('beverages','mineral water',40),('beverages','ice tea',30),('extra topping','cheese',20);
/*!40000 ALTER TABLE `chicago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chitchat`
--

DROP TABLE IF EXISTS `chitchat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chitchat` (
  `Category` char(30) NOT NULL,
  `Fooditem` char(30) NOT NULL,
  `price` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chitchat`
--

LOCK TABLES `chitchat` WRITE;
/*!40000 ALTER TABLE `chitchat` DISABLE KEYS */;
INSERT INTO `chitchat` VALUES ('snacks','Paneer bread pakoda','N/A'),('snacks','studded patties','N/A'),('snacks','bread cheese rolls','N/A'),('snacks','French Fries','N/A'),('snacks','Chicken hot dog','N/A'),('beverages','Mocktail','N/A'),('beverages','Ice tea','N/A'),('beverages','flavoured tea','N/A'),('beverages','lassi','N/A'),('beverages','cold coffee','N/A'),('Deserts','Pastries','N/A'),('Deserts','brownie','N/A'),('indian chaat','Aloo tikki','n/a'),('indian chaat','Dahi Bhalla','n/a'),('indian chaat','Papdi chaat','n/a'),('indian chaat','Samosa','n/a'),('indian chaat','Raj Kachori','n/a'),('indian chaat','bhel puri','n/a'),('indian chaat','Gol gappe','n/a'),('indian chaat','Dahi puri','n/a'),('indian chaat','Palak patta chaat','n/a'),('indian chaat','Khasta kachori/Aloo bhaji','n/a'),('continental','sub style sandwhich','n/a'),('continental','burger','n/a'),('continental','cheese garlic bread','n/a'),('continental','Sandwhich(veg)','n/a'),('continental','Sandwhich(Chicken)','n/a'),('continental','Pizza','n/a');
/*!40000 ALTER TABLE `chitchat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `juicebar`
--

DROP TABLE IF EXISTS `juicebar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `juicebar` (
  `category` char(20) NOT NULL,
  `fooditem` char(20) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juicebar`
--

LOCK TABLES `juicebar` WRITE;
/*!40000 ALTER TABLE `juicebar` DISABLE KEYS */;
INSERT INTO `juicebar` VALUES ('beverages','carrot juice',60),('beverages','mousambi juice',60),('beverages','orange juice',60),('beverages','pineapple juice',60),('beverages','banana shake',70),('beverages','mango shake',70),('beverages','mix fruit juice',80),('beverages','beetroot juice',80),('beverages','pomengranate juice',100),('beverages','oreo shake',80),('beverages','butterscotch shake',80),('beverages','green apple shake',80),('beverages','kiwi shake',80),('beverages','strawberry shake',80),('beverages','chocoolate shake',80),('beverages','vanilla shake',80),('beverages','pine apple shake',80),('beverages','guava shake',80),('beverages','litchi shake',80),('beverages','blackcurrent shake',80),('beverages','kaju kishmish shake',80),('beverages','protein shake',80),('beverages','masala tea',30),('beverages','coconut water',50),('beverages','nimbu pani',60),('beverages','suger cane juice',60),('beverages','cold coffee',70),('ice creme','butter scotch',50),('ice creme','chocolate',50),('ice creme','vanilla',50),('ice creme','american bite',50),('ice creme','mango',50),('ice creme','jaffrani pista',50),('ice creme','kaju kishmish',50),('ice creme','black current',50),('ice creme','tooti fruiti',50),('others','shai kheer',100),('others','popcorn',100),('others','hot chocolate fudge',100),('others','fresh fruit sundae',120),('others','fruit salad',70);
/*!40000 ALTER TABLE `juicebar` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-08 17:08:48
