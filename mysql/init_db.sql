CREATE SCHEMA `newsAPI` ;

CREATE TABLE `newsAPI`.`sources` (
  `source_id` INT NOT NULL AUTO_INCREMENT,
  `source_name` VARCHAR(45) NULL,
  `source_description` MEDIUMTEXT NULL,
  PRIMARY KEY (`source_id`));

CREATE TABLE `newsAPI`.`sort` (
  `source_id` INT NOT NULL,
  `sort_id` INT NOT NULL,
  PRIMARY KEY (`source_id`, `sort_id`));
  
CREATE TABLE `newsAPI`.`sort_list` (
  `sort_id` INT NOT NULL AUTO_INCREMENT,
  `sort_name` VARCHAR(45) NULL,
  PRIMARY KEY (`sort_id`));

CREATE TABLE `newsAPI`.`articles` (
  `article_id` INT NOT NULL AUTO_INCREMENT,
  `source_id` INT NOT NULL,
  `publishedAt` timestamp NULL,
  `title` VARCHAR(255) NULL,
  `description` MEDIUMTEXT NULL,
  `url` MEDIUMTEXT NULL,
  `urlToImage`MEDIUMTEXT NULL,
  PRIMARY KEY (`article_id`));
  
CREATE TABLE `newsAPI`.`author` (
  `article_id` INT NOT NULL,
  `author_id` INT NOT NULL,
  PRIMARY KEY (`article_id`, `author_id`));

CREATE TABLE `newsAPI`.`author_list` (
  `author_id` INT NOT NULL AUTO_INCREMENT,
  `author_name` VARCHAR(255) NULL,
  PRIMARY KEY (`author_id`));

CREATE TABLE `newsAPI`.`logo_url` (
  `logo_url_id` INT NOT NULL AUTO_INCREMENT,
  `logo_url_sm` INT NULL,
  `logo_url_med` INT NULL,
  `logo_url_lg` INT NULL,
  PRIMARY KEY (`logo_url_id`));
  
CREATE TABLE `newsAPI`.`category` (
  `source_id` INT NOT NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`source_id`, `category_id`));
  
CREATE TABLE `newsAPI`.`category_list` (
  `category_id` INT NOT NULL AUTO_INCREMENT,
  `category_name` VARCHAR(45) NULL,
  PRIMARY KEY (`category_id`));
  
CREATE TABLE `newsAPI`.`language` (
  `source_id` INT NOT NULL,
  `language_id` INT NOT NULL,
  PRIMARY KEY (`source_id`, `language_id`));
  
CREATE TABLE `newsAPI`.`language_list` (
  `language_id` INT NOT NULL AUTO_INCREMENT,
  `language_name` VARCHAR(45) NULL,
  PRIMARY KEY (`language_id`));

CREATE TABLE `newsAPI`.`country` (
  `source_id` INT NOT NULL,
  `country_id` INT NOT NULL,
  PRIMARY KEY (`source_id`, `country_id`));
  
CREATE TABLE `newsAPI`.`country_list` (
  `country_id` INT NOT NULL AUTO_INCREMENT,
  `country_name` VARCHAR(45) NULL,
  PRIMARY KEY (`country_id`));
  
INSERT INTO newsAPI.language_list (language_name) VALUES ('en');
INSERT INTO newsAPI.language_list (language_name) VALUES ('de');
INSERT INTO newsAPI.language_list (language_name) VALUES ('fr');
INSERT INTO newsAPI.sort_list (sort_name) VALUES ('top');
INSERT INTO newsAPI.sort_list (sort_name) VALUES ('latest');
INSERT INTO newsAPI.sort_list (sort_name) VALUES ('popular');
INSERT INTO newsAPI.country_list (country_name) VALUES ('au');
INSERT INTO newsAPI.country_list (country_name) VALUES ('de');
INSERT INTO newsAPI.country_list (country_name) VALUES ('gb');
INSERT INTO newsAPI.country_list (country_name) VALUES ('in');
INSERT INTO newsAPI.country_list (country_name) VALUES ('it');
INSERT INTO newsAPI.country_list (country_name) VALUES ('us');
INSERT INTO newsAPI.category_list (category_name) VALUES ('business');
INSERT INTO newsAPI.category_list (category_name) VALUES ('entertainment');
INSERT INTO newsAPI.category_list (category_name) VALUES ('gaming');
INSERT INTO newsAPI.category_list (category_name) VALUES ('general');
INSERT INTO newsAPI.category_list (category_name) VALUES ('music');
INSERT INTO newsAPI.category_list (category_name) VALUES ('science-and-nature');
INSERT INTO newsAPI.category_list (category_name) VALUES ('sport');
INSERT INTO newsAPI.category_list (category_name) VALUES ('technology');
INSERT INTO newsAPI.author_list (author_id, author_name) VALUES (1, 'None');