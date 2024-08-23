CREATE TABLE Users (
    username VARCHAR(255),
    user_id INT PRIMARY KEY,
    password VARCHAR(255),
    section VARCHAR(255),
    user_type ENUM('Admin', 'Shop Floor', 'PCO')
);

CREATE TABLE Workorder (
    workorder_no INT PRIMARY KEY,
    workorder_date DATE,
    item_name VARCHAR(255),
    consignee VARCHAR(255),
    allocation_no VARCHAR(255),
    quantity INT,
    job_number VARCHAR(8),
    status ENUM('active', 'inactive') DEFAULT 'active',
    FOREIGN KEY (item_name) REFERENCES Item(item_name),
    FOREIGN KEY (consignee) REFERENCES Consignee(consignee)
);

CREATE TABLE Consignee (
    zone VARCHAR(255),
    division VARCHAR(255),
    indenter VARCHAR(255),
    consignee VARCHAR(255) PRIMARY KEY,
    consignee_type ENUM('Home Revenue', 'Projects', 'Construction')
);

CREATE TABLE Item (
    item_name VARCHAR(255) PRIMARY KEY,
    item_description TEXT,
    item_type ENUM('SG', 'NSG'),
    sg_number VARCHAR(255)
);
