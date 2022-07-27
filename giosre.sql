-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-07-2022 a las 18:38:54
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `giosre`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `juegos`
--

CREATE TABLE `juegos` (
  `id` int(11) UNSIGNED NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `precio` decimal(9,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `juegos`
--

INSERT INTO `juegos` (`id`, `nombre`, `descripcion`, `precio`) VALUES
(8, 'pes2022', 'fifa', '100.00'),
(11, 'jhelsin', 'juego', '50.00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `metodo_pago`
--

CREATE TABLE `metodo_pago` (
  `id` int(11) NOT NULL,
  `desc` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `metodo_pago`
--

INSERT INTO `metodo_pago` (`id`, `desc`) VALUES
(1, 'efectivo'),
(2, 'tarjeta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_comprobante`
--

CREATE TABLE `tipo_comprobante` (
  `id` int(1) NOT NULL,
  `descripcion` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipo_comprobante`
--

INSERT INTO `tipo_comprobante` (`id`, `descripcion`) VALUES
(1, 'Boleta'),
(2, 'Factura'),
(3, 'Nota de credito'),
(6, 'debito');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) UNSIGNED NOT NULL,
  `usuario` varchar(20) NOT NULL,
  `pws` varchar(20) NOT NULL,
  `nombres` varchar(60) NOT NULL,
  `admin` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `usuario`, `pws`, `nombres`, `admin`) VALUES
(8, 'jhelsin', 'astonmartinl70', 'jhelsin mijhael', 0),
(9, 'bndd', 'asison', 'mikaela', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `id` int(11) NOT NULL,
  `id_tipo_comprobante` int(1) NOT NULL,
  `fecha` date NOT NULL,
  `name_c` varchar(50) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `id_pj5` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`id`, `id_tipo_comprobante`, `fecha`, `name_c`, `direccion`, `id_pj5`, `cantidad`) VALUES
(7, 0, '2022-07-08', 'Rese', 'jr.Emancipacion', 12, 2),
(8, 1, '2022-07-14', 'Anna', 'Av.Mc', 13, 1),
(10, 1, '2022-07-14', 'd', 'jr maizales', 8, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `juegos`
--
ALTER TABLE `juegos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `metodo_pago`
--
ALTER TABLE `metodo_pago`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipo_comprobante`
--
ALTER TABLE `tipo_comprobante`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `juegos`
--
ALTER TABLE `juegos`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `metodo_pago`
--
ALTER TABLE `metodo_pago`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tipo_comprobante`
--
ALTER TABLE `tipo_comprobante`
  MODIFY `id` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
