CREATE TABLE IF NOT EXISTS proveedores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(120) NOT NULL,
  ruc VARCHAR(20) NOT NULL UNIQUE,
  telefono VARCHAR(30) NULL,
  email VARCHAR(120) NULL,
  direccion VARCHAR(200) NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- (Opcional) Datos de prueba
INSERT INTO proveedores (nombre, ruc, telefono, email, direccion) VALUES
('Proveedor Uno', '12345678901', '999111222', 'uno@proveedor.com', 'Av. Principal 123'),
('Proveedor Dos', '10987654321', '999333444', 'dos@proveedor.com', 'Calle Secundaria 456');
