-- Sabse pehle apne purane database ko select karein
USE inventory_db;

-- Ab ye nayi table banayein (Purani tables ko kuch nahi hoga)
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Ek default login detail add karein
-- Username: admin | Password: password123
INSERT INTO users (username, password) VALUES ('admin', 'password123');