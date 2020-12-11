-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8081
-- Generation Time: Dec 11, 2020 at 10:58 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `breizhibus`
--
CREATE DATABASE IF NOT EXISTS `breizhibus` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `breizhibus`;

-- --------------------------------------------------------

--
-- Table structure for table `arrets`
--

CREATE TABLE `arrets` (
  `id_arret` int(11) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `adresse` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `arrets`
--

INSERT INTO `arrets` (`id_arret`, `nom`, `adresse`) VALUES
(1, 'Korrigan', '1 impasse du Korrigan'),
(2, 'Morgana', '2 plage Morgana'),
(3, 'L\'Ankou', '3 place de la Morgue'),
(4, 'Ys', '4 rue de l\'ile d\'Ys'),
(5, 'Viviane', '5 avenu de Viviane'),
(6, 'Guénolé', '6 rue Saint Guénolé');

-- --------------------------------------------------------

--
-- Table structure for table `arrets_lignes`
--

CREATE TABLE `arrets_lignes` (
  `id_ligne` int(11) NOT NULL,
  `id_arret` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `arrets_lignes`
--

INSERT INTO `arrets_lignes` (`id_ligne`, `id_arret`) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 2),
(2, 4),
(2, 6),
(3, 4),
(3, 5),
(3, 6),
(3, 1),
(4, 5),
(4, 1),
(4, 3),
(5, 4),
(5, 6),
(5, 2);

-- --------------------------------------------------------

--
-- Table structure for table `bus`
--

CREATE TABLE `bus` (
  `id_bus` int(11) NOT NULL,
  `numero` varchar(7) NOT NULL,
  `immatriculation` varchar(11) NOT NULL,
  `nombre_places` int(11) NOT NULL,
  `id_ligne` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bus`
--

INSERT INTO `bus` (`id_bus`, `numero`, `immatriculation`, `nombre_places`, `id_ligne`) VALUES
(1, 'BB01', 'FD456QZ', 20, 2),
(2, 'BB02', 'NO123DD', 45, 3),
(3, 'BB03', 'AF483AZ', 18, 4),
(4, 'BB04', 'RT782ZV', 32, 5),
(5, 'BB06', 'GM122FC', 25, 1),
(6, 'BB07', 'ED593ZP', 40, 3),
(7, 'BB08', 'DE159KJ', 20, 5);

-- --------------------------------------------------------

--
-- Table structure for table `lignes`
--

CREATE TABLE `lignes` (
  `id_ligne` int(11) NOT NULL,
  `nom` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lignes`
--

INSERT INTO `lignes` (`id_ligne`, `nom`) VALUES
(1, 'Rouge'),
(2, 'Vert'),
(3, 'Bleu'),
(4, 'Rose'),
(5, 'Jaune');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `arrets`
--
ALTER TABLE `arrets`
  ADD PRIMARY KEY (`id_arret`);

--
-- Indexes for table `arrets_lignes`
--
ALTER TABLE `arrets_lignes`
  ADD KEY `id_arret` (`id_arret`),
  ADD KEY `id_ligne` (`id_ligne`);

--
-- Indexes for table `bus`
--
ALTER TABLE `bus`
  ADD PRIMARY KEY (`id_bus`),
  ADD KEY `id_ligne` (`id_ligne`);

--
-- Indexes for table `lignes`
--
ALTER TABLE `lignes`
  ADD PRIMARY KEY (`id_ligne`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `arrets`
--
ALTER TABLE `arrets`
  MODIFY `id_arret` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `bus`
--
ALTER TABLE `bus`
  MODIFY `id_bus` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `lignes`
--
ALTER TABLE `lignes`
  MODIFY `id_ligne` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `arrets_lignes`
--
ALTER TABLE `arrets_lignes`
  ADD CONSTRAINT `arrets_lignes_ibfk_1` FOREIGN KEY (`id_arret`) REFERENCES `arrets` (`id_arret`),
  ADD CONSTRAINT `arrets_lignes_ibfk_2` FOREIGN KEY (`id_ligne`) REFERENCES `lignes` (`id_ligne`);

--
-- Constraints for table `bus`
--
ALTER TABLE `bus`
  ADD CONSTRAINT `bus_ibfk_1` FOREIGN KEY (`id_ligne`) REFERENCES `lignes` (`id_ligne`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
