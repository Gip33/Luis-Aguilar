DROP TABLE Customers;
DROP TABLE Shippings;
DROP TABLE Orders;

CREATE TABLE Students (
    stundents_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    fav_color VARCHAR(50)
);

ALTER TABLE Students
ADD COLUMN age INT;

ALTER TABLE Students
ADD COLUMN tlf INT;

--ALTER TABLE Students
--MODIFY COLUMN fav_color INT;

ALTER TABLE Students
DROP COLUMN last_name;

ALTER TABLE Students
ADD COLUMN last_name VARCHAR(50);

ALTER TABLE Students
INSERT INTO Students (students_id, first_name, last_name, fav_color, age, tlf)
VALUES
(29876819, 'Kevin'  , 'Rincon'  , 'Negro' , 24, 04246502632),
(29930382, 'Oswaldo', 'Tovar'   , 'Verde' , 24, 04146234927),
(31132817, 'Neyber' , 'Machado' , 'Negro' , 20, 04146195395),
(31825571, 'Angel'  , 'Neri'    , 'Negro' , 20, 04128296611),
(32280012, 'Josue'  , 'Delgado' , 'Azul'  , 18, 04246848519),
(32422845, 'Angel'  , 'Gomez'   , 'Azul'  , 17, 04226935611),
(32700110, 'Daniela', 'Bravo'   , 'Blanco', 17, 04129654145),
(32708787, 'Jose'   , 'Molina'  , 'Azul'  , 17, 04247017288),
(32756560, 'Roxibel', 'Castillo', 'Lila'  , 17, 04149679898),
(33272644, 'Luis'   , 'Aguilar' , 'Rojo'  , 17, 04146014406),
(33435489, 'Ana'    , 'Rubio'   , 'Azul'  , 18, 04126134253);