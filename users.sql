/*
Navicat MySQL Data Transfer

Source Server         : 本机root
Source Server Version : 50713
Source Host           : localhost:3306
Source Database       : rubic

Target Server Type    : MYSQL
Target Server Version : 50713
File Encoding         : 65001

Date: 2022-12-29 14:46:58
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `birthday` datetime NOT NULL,
  `perfer` varchar(20) NOT NULL,
  `city` varchar(30) NOT NULL,
  `create_at` datetime NOT NULL,
  `update_at` datetime NOT NULL,
  `sys_role` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'admin', 'adminpass', '13525324211', '2022-07-07 20:32:02', 'WCA-速拧-连体-连拧', '11234567890765', '2022-07-04 20:32:17', '2022-07-04 20:32:20', 'admin');
INSERT INTO `users` VALUES ('2', 'zhangsan', 'zhangsanpass', '13525324211', '2022-06-06 00:00:00', 'WCA-速拧-连体', '山西省-长治市-上党区', '2022-07-04 21:28:14', '2022-07-04 21:28:14', 'dev');
INSERT INTO `users` VALUES ('4', 'wangwu', 'wangwupass', '13525324211', '2022-06-06 00:00:00', 'WCA-速拧-连体-连拧', '福建省-厦门市-思明区', '2022-07-04 22:03:33', '2022-07-04 22:03:33', 'dev');
INSERT INTO `users` VALUES ('5', 'zhaoliu', 'zhaoliupass', '13525324211', '2022-06-06 00:00:00', 'WCA-速拧-连体-连拧', '福建省-厦门市-思明区', '2022-07-04 22:05:56', '2022-07-04 22:05:56', 'dev');
INSERT INTO `users` VALUES ('6', 'tianqi', 'tianqipass', '15038479908', '2022-06-12 00:00:00', 'WCA-镜面', '江苏省-徐州市-云龙区', '2022-07-04 22:39:34', '2022-07-04 22:39:34', 'dev');
INSERT INTO `users` VALUES ('7', 'wangba', 'wangbapass', '13467832111', '2022-06-05 00:00:00', '异型-连拧', '台湾省-基隆市-南区', '2022-07-04 22:40:49', '2022-07-04 22:40:49', 'dev');
INSERT INTO `users` VALUES ('8', 'hello', 'hellopass', '13467890999', '2022-06-05 00:00:00', '镜面', '山西省-长治市-上党区', '2022-07-04 22:43:36', '2022-07-04 22:43:36', 'dev');
