-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 29, 2022 at 05:35 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vagbat`
--

-- --------------------------------------------------------

--
-- Table structure for table `blog`
--

CREATE TABLE `blog` (
  `blogsno` int(11) NOT NULL,
  `title` varchar(10000) NOT NULL,
  `banite` varchar(1000) NOT NULL,
  `content` longtext NOT NULL,
  `user` varchar(40) NOT NULL,
  `date` date DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blog`
--

INSERT INTO `blog` (`blogsno`, `title`, `banite`, `content`, `user`, `date`) VALUES
(1, '“মাতৃঋণ কোনো সন্তানই কখনোই শোধ করতে পারে না।”', 'ভগবান শ্রীকৃষ্ণ', '“মা” হল পৃথিবীর সর্ব শ্রেষ্ঠ উপহার একজন সন্তানের কাছে। কথিত,ভগবান সবার সাথে থাকতে পারে না বলেই তিনি মায়ের সৃষ্টি করেছেন। “মা” তাই ভগবানের রূপ প্রতিটি সন্তানের কাছে। এই মায়ের অবদান শোধ তাই দূরের কথা কোনো সন্তান কখনো পৌঁছাতে পারবে না কারণ এটি ভালোবাসা,যত্ন,আত্মত্যাগ, যা মাপার উর্ধ্বে।', 'জনি ঘোষ', '2022-01-26'),
(17, 'dfsd', 'dfsd', 'sfdsf', 'wew', '2022-01-28'),
(18, 'd', 'd', 'efer', 'erer', '2022-01-28'),
(19, 'werrrrrrrrr', 'werrrrrrrrr', 'errrrrr', 'reeeeeee', '2022-01-28'),
(20, 'errrrrrrrrrrr', 'errrrrrrrrrrr', 'errrrrrr', 'reeeeeeee', '2022-01-28'),
(21, 'erer', 'erer', 'er', 'er', '2022-01-28'),
(22, 'dffdd', 'dffdd', '2', '1', '2022-01-28'),
(23, '23', '23', '3', '1', '2022-01-28'),
(24, '2343243', '2343243', 'dsfs', '1', '2022-01-28'),
(25, 'sdfsdr', 'sdfsdr', '11', 'sdfdsf', '2022-01-28'),
(26, 'lllalllllllllll', 'lllalllllllllll', 'ddd', 'dgdgdf', '2022-01-28'),
(27, '111111111111111111', '111111111111111111', '2', '2', '2022-01-28'),
(28, 'f21', 'f21', '3333', '3333333333333333', '2022-01-28');

-- --------------------------------------------------------

--
-- Table structure for table `chapter`
--

CREATE TABLE `chapter` (
  `srlno` int(2) NOT NULL,
  `chapno` varchar(100) NOT NULL,
  `chapname` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chapter`
--

INSERT INTO `chapter` (`srlno`, `chapno`, `chapname`) VALUES
(1, 'প্রথম', 'অর্জুন বিষাদ যোগ'),
(2, 'দ্বিতীয়', 'সাংখ্য যোগ'),
(3, 'তৃতীয়', 'কর্ম যোগ'),
(4, 'চতুর্থ', ' জ্ঞান যোগ');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `sno` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`sno`, `username`, `pass`) VALUES
(1, 'jony', 'jony11');

-- --------------------------------------------------------

--
-- Table structure for table `massage`
--

CREATE TABLE `massage` (
  `sno` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phoneno` varchar(16) NOT NULL,
  `massage` varchar(9998) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `massage`
--

INSERT INTO `massage` (`sno`, `name`, `email`, `phoneno`, `massage`, `date`) VALUES
(26, 'jony', 'jony@gmail.com', '01303403231', 'Hare krishna', '2022-01-03 09:13:54'),
(27, 'jony', 'jony@gmail.com', '01303403231', 'Hare krishna', '2022-01-03 09:15:46'),
(28, 'Jony Ghosh', 'jony@gmail.com', '01303403231', 'Hare krishna hare krishna krishna krishna hare hare hare ramo hare ramo ramo ramo hare hare.......', '2022-01-03 09:16:38'),
(29, 'jony', 'jony@gmail.com', '01303403231', 'Hare krishna', '2022-01-03 09:17:35'),
(30, 'Jony Ghosh', 'jony@gmail.com', '01303403231', 'Hare krishna hare krishna \r\nkrishna krishna hare hare\r\nhare ramo hare ramo \r\nramo ramo hare hare', '2022-01-03 09:18:28'),
(31, 'Jony Ghosh........', 'jony@gmail.com', '01303403231', 'Hare krishna hare krishna \r\nkrishna krishna hare hare\r\nhare ramo hare ramo \r\nramo ramo hare hare', '2022-01-03 09:20:10'),
(32, 'Jony Ghosh........', 'jony@gmail.com', '01303403231', 'Hare krishna hare krishna \r\nkrishna krishna hare hare\r\nhare ramo hare ramo \r\nramo ramo hare hare', '2022-01-03 09:20:44'),
(33, 'Jony Ghosh........', 'jony@gmail.com', '01303403231', 'Hare krishna hare krishna \r\nkrishna krishna hare hare\r\nhare ramo hare ramo \r\nramo ramo hare hare', '2022-01-03 09:21:41'),
(34, 'Jony Ghosh', 'jonyghosh444@gmail.com', '01792558996', 'Hare krishna', '2022-01-03 12:38:21'),
(35, 'Jony Ghosh', 'jonyghosh444@gmail.com', '01792558996', 'Hare krishna', '2022-01-03 12:39:56'),
(36, 'Jony Ghosh', 'jonyghosh444@gmail.com', '01792558996', 'Jay sree krishna', '2022-01-03 20:07:27'),
(37, 'Saikat', 'saikat@gmail.com', '01760037851', 'hello bro', '2022-01-12 22:10:23'),
(38, 'df', 'df', '01792558996', 'hare krishna', '2022-01-15 21:18:41'),
(39, 'df', 'df', '01792558996', 'hare krishna', '2022-01-15 21:19:24'),
(40, 'Jony Ghosh', 'jonyghosh444@gmail.com', '01792558996', 'Jay shree krishna', '2022-01-15 21:19:47'),
(41, 'Jony Ghosh', 'jonyghosh444@gmail.com', '01792558996', 'Jay shree krishna', '2022-01-15 21:22:37');

-- --------------------------------------------------------

--
-- Table structure for table `slok`
--

CREATE TABLE `slok` (
  `allslkno` int(20) NOT NULL,
  `chapnoen` int(20) NOT NULL,
  `chapnobn` varchar(200) NOT NULL,
  `chapnamebn` varchar(2000) NOT NULL,
  `slksnoen` int(2) NOT NULL,
  `slksnobn` varchar(200) NOT NULL,
  `slok` longtext NOT NULL,
  `anubad` longtext NOT NULL,
  `tatporjo` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `slok`
--

INSERT INTO `slok` (`allslkno`, `chapnoen`, `chapnobn`, `chapnamebn`, `slksnoen`, `slksnobn`, `slok`, `anubad`, `tatporjo`) VALUES
(27, 1, 'প্রথম', 'অর্জুন বিষাদ যোগ', 1, '১', 'ধর্মক্ষেত্রে কুরুক্ষেত্রে সমবেতা যুযুৎসবঃ।\r\nমামকাঃ পান্ডবাশ্চৈব কিমকুর্বত সঞ্জয়।।', 'ধৃতরাষ্ট্র জিজ্ঞাসা করলেন- হে সঞ্জয়! ধর্মক্ষেত্রে যুদ্ধ করার মানসে সমবেত হয়ে আমার পুত্র এবং পান্ডুর পুত্রেরা তারপর কি করল? ', 'ধৃতরাষ্ট্র জিজ্ঞাসা করলেন- হে সঞ্জয়! ধর্মক্ষেত্রে যুদ্ধ করার মানসে সমবেত হয়ে আমার পুত্র এবং পান্ডুর পুত্রেরা তারপর কি করল? '),
(28, 1, 'প্রথম', 'অর্জুন বিষাদ যোগ', 2, '২', 'দৃষ্ট্বা তু পাণ্ডবানীকং ব্যূঢ়ং দুর্যোধনস্তদা। \r\nআচার্যমুপসঙ্গম্য রাজা বচনমব্রবীৎ।।', 'সঞ্জয় বললেন-হে রাজন্! পান্ডবদের সৈন্যসজ্জা দর্শন করে রাজা দুর্যোধন দ্রোণাচার্যের কাছে গিয়ে বললেন', 'সঞ্জয় বললেন-হে রাজন্! পান্ডবদের সৈন্যসজ্জা দর্শন করে রাজা দুর্যোধন দ্রোণাচার্যের কাছে গিয়ে বললেন..........');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blog`
--
ALTER TABLE `blog`
  ADD PRIMARY KEY (`blogsno`);

--
-- Indexes for table `chapter`
--
ALTER TABLE `chapter`
  ADD PRIMARY KEY (`srlno`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `massage`
--
ALTER TABLE `massage`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `slok`
--
ALTER TABLE `slok`
  ADD PRIMARY KEY (`allslkno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blog`
--
ALTER TABLE `blog`
  MODIFY `blogsno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `massage`
--
ALTER TABLE `massage`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `slok`
--
ALTER TABLE `slok`
  MODIFY `allslkno` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
