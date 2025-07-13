CREATE TABLE users (
    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    user_type_id INTEGER,
    name        TEXT NOT NULL,
    surname     TEXT NOT NULL,
    telephone   TEXT NOT NULL,
    email       TEXT NOT NULL,
    hourly_rate DOUBLE
);

CREATE TABLE user_types (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  role TEXT NOT NULL
);

CREATE TABLE batteries (
    id_battery INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT NOT NULL,
    type    TEXT NOT NULL,
    price   DOUBLE NOT NULL,
    stock   INTEGER NOT NULL
);

CREATE TABLE cases (
    id_case INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT NOT NULL,
    material TEXT NOT NULL,
    price   DOUBLE NOT NULL,
    stock   INTEGER NOT NULL
);

CREATE TABLE processors (
    id_processor INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT NOT NULL,
    chipset TEXT NOT NULL,
    price   DOUBLE NOT NULL,
    stock   INTEGER NOT NULL
);

CREATE TABLE phones (
    id_phone             INTEGER PRIMARY KEY AUTOINCREMENT,
    labour_intensity     INTEGER NOT NULL,
    name                 TEXT NOT NULL,
    type                 INTEGER NOT NULL,
    user_id_employee     INTEGER,
    processors_id_processor INTEGER,
    cases_id_case INTEGER,
    batteries_id_battery INTEGER,
    manufacture_price INTEGER,
    final_price INTEGER,
    img TEXT,
    FOREIGN KEY (processors_id_processor) REFERENCES users (id_processor)
    FOREIGN KEY (user_id_employee) REFERENCES users (id_user)
    FOREIGN KEY (cases_id_case) REFERENCES users (id_case)
    FOREIGN KEY (batteries_id_battery) REFERENCES users (id_battery)
);



-- Insert initial data

-- Hash references to 'password' with usage of salt; algorithm sha256

INSERT INTO user_types (id, role) VALUES (1, 'admin');
INSERT INTO user_types (id, role) VALUES (2, 'employee');
INSERT INTO user_types (id, role) VALUES (3, 'customer');

INSERT INTO users (id_user, login, password, user_type_id, name, surname, telephone, email, hourly_rate) 
VALUES (1, 'admin', '74baeb21265087ea11e1555f2b1489ae16c00cbdd5b78f0c3eedd6c0c8be3a41', 1, 'admin', 'adminu', '+42000056650000', 'testadmin@test.cz', 300);

INSERT INTO users (id_user, login, password, user_type_id, name, surname, telephone, email, hourly_rate) 
VALUES (2, 'jarda', '74baeb21265087ea11e1555f2b1489ae16c00cbdd5b78f0c3eedd6c0c8be3a41', 2, 'jarda', 'jarda', '+421262000000', 'tedadstuser@test.cz', 200);

INSERT INTO users (id_user, login, password, user_type_id, name, surname, telephone, email, hourly_rate) 
VALUES (3, 'hana', '74baeb21265087ea11e1555f2b1489ae16c00cbdd5b78f0c3eedd6c0c8be3a41', 2, 'hana', 'hana', '+4210000216120000', 'tedadstuser@test.cz', 200);

INSERT INTO users (id_user, login, password, user_type_id, name, surname, telephone, email, hourly_rate) 
VALUES (4, 'pepa', '74baeb21265087ea11e1555f2b1489ae16c00cbdd5b78f0c3eedd6c0c8be3a41', 2, 'pepa', 'pepa', '+42101500000', 'tesdatuser@test.cz', 200);

INSERT INTO users (id_user, login, password, user_type_id, name, surname, telephone, email, hourly_rate) 
VALUES (5, 'ING. Novak', '74baeb21265087ea11e1555f2b1489ae16c00cbdd5b78f0c3eedd6c0c8be3a41', 3, 'ING. Novak', 'ING. Novak', '+4210015100000', 'tesaatuser@test.cz', 200);


INSERT INTO batteries (id_battery,name,type,price,stock) 
VALUES (1, 'batteries.cz','li-ion', 2000, 5);

INSERT INTO batteries (id_battery,name,type,price,stock) 
VALUES (2, 'batteries.sk','li-ion', 1500, 5);

INSERT INTO processors (id_processor,name,chipset,price,stock) 
VALUES (1, 'AMD','WRX80', 5000, 5);

INSERT INTO processors (id_processor,name,chipset,price,stock) 
VALUES (2, 'Intel','H770', 10000, 5);

INSERT INTO cases (id_case,name,material,price,stock) 
VALUES (1, 'Case PRO','steel', 1500, 4);

INSERT INTO cases (id_case,name,material,price,stock) 
VALUES (2, 'Case normal','plastic', 500, 10);

INSERT INTO phones (id_phone, labour_intensity,name,type,user_id_employee,processors_id_processor,cases_id_case,batteries_id_battery,manufacture_price,final_price,img) 
VALUES (1, 5, 'I-phone', 8, 2, 1, 1, 1,10000,15000, 'https://cdn.alza.cz/Foto/f4/RI/RI044b4.jpg');
/*/
INSERT INTO phones (id_phone, labour_intensity,name,type,user_id_employee,processors_id_processor,cases_id_case,batteries_id_battery,img) 
VALUES (2, 4, 'Samsung', 9, 3, 2, 2,2, 'https://cdn.alza.cz/ImgW.ashx?fd=f4&cd=SAMO0233b3&i=1.jpg');
*/