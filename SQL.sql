CREATE TABLE Products(
  'product_id' INT PRIMARY KEY, 
  'product_name' VARCHAR(150), 
  'price' DECIMAL(10, 2), 
  'stock' INT
);

INSERT INTO Products (product_id, product_name, price, stock)
VALUES
(1, 'Laptop Pro', 1200.00, 50), 
(2, 'Mouse Gamer', 75.50, 150), 
(3, 'Teclado Mecánico', 150.99, 100);

CREATE TABLE Customers(
  customer_id INT PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  age INT,
  country VARCHAR(100),
  email VARCHAR(100)
);

INSERT INTO Customers (customer_id, first_name, last_name, age, country, email) VALUES
(1, 'Juan', 'Perez', 28, 'Mexico', 'juan.perez@email.com'),
(2, 'Ana', 'García', 34, 'España', 'ana.garcia@email.com'),
(3, 'Carlos', 'Rodriguez', 45, 'Argentina', 'carlos.r@email.com'),
(4, 'Maria', 'Lopez', 22, 'Colombia', 'maria.lopez@email.com'),
(5, 'Luis', 'Martinez', 52, 'Mexico', 'luis.martinez@email.com');

SELECT first_name, last_name, email FROM Customers;

SELECT * FROM Customers WHERE country = 'Mexico';

UPDATE Customers
SET email = 'ana.g.nuevo@email.com'
WHERE customer_id = 2;

SELECT * FROM Customers WHERE country = 'Mexico' AND age > 30;

SELECT * FROM Orders ORDER BY order_id DESC;

SELECT COUNT(*) AS total_pedidos FROM Orders;

SELECT customer_id, COUNT(order_id) AS orders FROM Orders GROUP BY customer_id;

DELETE FROM Shippings WHERE status = 'Pending';

SELECT
	Orders.order_id,
	Orders.item,
    Customers.first_name,
	Customers.last_name
FROM Orders
INNER JOIN Customers ON Customers.customer_id = Orders.customer_id;

SELECT customer_id, COUNT(*) AS orders
FROM Orders
GROUP BY customer_id
HAVING COUNT(*) >= 2;

-- No pude hacer los demas :'v
/*
*1️⃣3️⃣ Búsqueda de Clientes sin Pedidos (LEFT JOIN)*
- _Enunciado:_ ¿Hay algún cliente que no nos ha comprado nada? ¡Encuéntralo!
- _Requerimientos:_
  1. Usar `LEFT JOIN` de `Customers` a `Orders`.
  2. Filtrar con `WHERE` donde el `order_id` sea `NULL`.

*1️⃣4️⃣ Subconsulta para Filtrado*
- _Enunciado:_ Traer toda la info de los clientes que han comprado un 'Mouse'.
- _Requerimientos:_
  1. Consulta principal sobre `Customers`.
  2. Usar `WHERE customer_id IN (...)`.
  3. La subconsulta debe devolver los `customer_id` que compraron un 'Mouse'.

*1️⃣5️⃣ Consulta Completa de Tres Tablas*
- _Enunciado:_ ¡El reporte final! Mostrar nombre de cliente, ítem del pedido y estado del envío.
- _Requerimientos:_
  1. Hacer `JOIN` entre `Customers`, `Orders`, y `Shippings`.
  2. Unir todas las tablas usando el `customer_id`.
/*
-- Esto pa la casa