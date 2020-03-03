--creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
name NOT NULL VARCHAR(256),
INDEX state_id (state_id),
FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id));
