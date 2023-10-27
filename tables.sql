/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - belleza
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`belleza` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `belleza`;

/*Table structure for table `barbershop` */

DROP TABLE IF EXISTS `barbershop`;

CREATE TABLE `barbershop` (
  `barbershopid` int(11) NOT NULL AUTO_INCREMENT,
  `shopname` varchar(20) DEFAULT NULL,
  `shoptype` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `state` varchar(10) DEFAULT NULL,
  `pincode` int(10) DEFAULT NULL,
  `about` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `phone` int(15) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `loginid` int(11) DEFAULT NULL,
  PRIMARY KEY (`barbershopid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `barbershop` */

insert  into `barbershop`(`barbershopid`,`shopname`,`shoptype`,`place`,`city`,`state`,`pincode`,`about`,`email`,`phone`,`photo`,`status`,`loginid`) values 
(1,'Orange','Men','Thikkodi','Kozhikode','Kerala',673529,'Cutomer Is Our King','orange@gmail.com',2147483647,'/static/photo/20221002124745.jpg','approved',3),
(2,'Waves','Men','Thikkodi','Kozhikode','Kerala',673543,'High class services','waves@gmail.com',2147483647,'/static/photo/20221008103240.jpg','approved',4),
(3,'Lionco','Hair Saolon','Thikkodi','Kozhikode','Kerala',672235,'Style Sense','lionco@gmail.com',2147483647,'/static/photo/20221008104413.jpg','approved',5),
(4,'Gentleman','Salon','Thikkodi','Kozhikode','Kerala',672234,'Fashion Republic','gentleman@gmail.com',2147483647,'/static/photo/20221008110251.jpg','approved',6);

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `bookingid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `barbershopid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `total amount` int(10) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`bookingid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`bookingid`,`userid`,`barbershopid`,`date`,`time`,`total amount`,`status`) values 
(1,2,5,'2022-10-08','11:17:29',370,'pending');

/*Table structure for table `bookingsub` */

DROP TABLE IF EXISTS `bookingsub`;

CREATE TABLE `bookingsub` (
  `bookingsubid` int(11) NOT NULL AUTO_INCREMENT,
  `bookingid` int(11) DEFAULT NULL,
  `serviceid` int(11) DEFAULT NULL,
  PRIMARY KEY (`bookingsubid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `bookingsub` */

insert  into `bookingsub`(`bookingsubid`,`bookingid`,`serviceid`) values 
(1,1,7),
(2,1,9);

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complantid` int(11) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(40) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `reply` varchar(20) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `barbershopid` int(11) DEFAULT NULL,
  PRIMARY KEY (`complantid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `usertype` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`loginid`,`uname`,`password`,`usertype`) values 
(1,'admin@gmail.com','admin','admin'),
(2,'savad@gmail.com','savad123','user'),
(3,'orange@gmail.com','orange123','barbershop'),
(4,'waves@gmail.com','waves123','barbershop'),
(5,'lionco@gmail.com','lionco123','barbershop'),
(6,'gentleman@gmail.com','gent123','barbershop');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `ratingid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `barbershopid` int(11) DEFAULT NULL,
  `review` varchar(40) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`ratingid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`ratingid`,`userid`,`barbershopid`,`review`,`rating`,`date`) values 
(1,2,3,'Good\r\n',1,'2022-10-02'),
(2,2,3,'Bad',1,'2022-10-02'),
(3,2,3,'jggj',1,'2022-10-02'),
(4,2,3,'  cccccc',1,'2022-10-02'),
(5,2,3,'  cccccc',2,'2022-10-02'),
(6,2,5,'Customer friendly atmosphere',4,'2022-10-08');

/*Table structure for table `services` */

DROP TABLE IF EXISTS `services`;

CREATE TABLE `services` (
  `serviceid` int(11) NOT NULL AUTO_INCREMENT,
  `servicename` varchar(25) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `servicerate` int(10) DEFAULT NULL,
  `description` varchar(25) DEFAULT NULL,
  `barbershopid` int(11) DEFAULT NULL,
  PRIMARY KEY (`serviceid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `services` */

insert  into `services`(`serviceid`,`servicename`,`photo`,`servicerate`,`description`,`barbershopid`) values 
(1,'Hair cutting','/static/photo/20221002154813.jpg',100,'Cutomized Service',3),
(2,'Hair Cutting','/static/photo/20221008103405.jpg',100,'Custom Styling',4),
(3,'Beard Styling','/static/photo/20221008103501.jpg',80,'Beard Shaping',4),
(4,'Flame styling','/static/photo/20221008103646.jpg',200,'Grooming hair wit fire.',4),
(5,'Hair Straightening','/static/photo/20221008104025.jpg',1000,'Solution for tangled hair',4),
(6,'Hair Cutting','/static/photo/20221008104818.jpg',100,'Hair Styling.',5),
(7,'Beard Styling','/static/photo/20221008105544.jpg',120,'Stylish beard',5),
(8,'Hair Straighting','/static/photo/20221008105713.jpg',800,'Amazing hair styles',5),
(9,'Buzz Cut','/static/photo/20221008110002.jpg',250,'Fading in the sides and S',5),
(10,'Hair Styling','/static/photo/20221008110510.jpg',120,'Customized styling accord',6),
(11,'Beard Styling','/static/photo/20221008110643.jpg',90,'Beard trimming asper cust',6),
(12,'Head Massage','/static/photo/20221008110819.jpg',500,'Relaxing head massage',6),
(13,'Facial','/static/photo/20221008111028.jpg',1000,'Nourishing face mask for ',6);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `place` varchar(25) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `state` varchar(10) DEFAULT NULL,
  `pincode` int(11) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `phone` int(15) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `loginid` int(11) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`uid`,`name`,`gender`,`place`,`city`,`state`,`pincode`,`email`,`phone`,`photo`,`loginid`) values 
(1,'Savad','male','Thikkodi','Kozhikode','Kerala',673529,'savad@gmail.com',2147483647,'/static/photo/20221002115408.jpg',2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
