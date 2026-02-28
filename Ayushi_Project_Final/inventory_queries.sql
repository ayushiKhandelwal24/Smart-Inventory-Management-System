-- Database select karein
USE inventory_db;

-- Nayi table banayein (Purani tables ko kuch nahi hoga)
CREATE TABLE shops (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    shop_name VARCHAR(100) NOT NULL
);

-- Shops ke naam jodein taaki list khali na dikhe
INSERT INTO shops (shop_name) VALUES ('Sharma General Store');
INSERT INTO shops (shop_name) VALUES ('Verma Electronics');
INSERT INTO shops (shop_name) VALUES ('Gupta Stationery');