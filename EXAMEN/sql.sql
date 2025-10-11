CREATE DATABASE examen;
USE examen;

CREATE TABLE Employes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    activo BOOLEAN DEFAULT TRUE
);

INSERT INTO Employes (id,nombre,activo)
VALUES
  (1, "Nombre1",true),
  (2, "Nombre2",true),
  (3, "Nombre3",true),
  (4, "Nombre4",true),
  (5, "Nombre5",true);

SELECT * FROM Employes

Select nombre FROM Employes WHERE activo = 1

UPDATE Employes SET activo = 0 WHERE id = 2