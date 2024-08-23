-- Create Users Table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    section VARCHAR(50),
    user_type ENUM('Admin', 'Shop Floor', 'PCO') NOT NULL
);

-- Create Consignees Table
CREATE TABLE consignees (
    consignee_id INT AUTO_INCREMENT PRIMARY KEY,
    zone VARCHAR(50) NOT NULL,
    division VARCHAR(50) NOT NULL,
    indenter VARCHAR(100) NOT NULL,
    consignee VARCHAR(100) NOT NULL,
    consignee_type ENUM('Home Revenue', 'Projects', 'Construction') NOT NULL
);

-- Create Items Table
CREATE TABLE items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    item_description TEXT,
    item_type ENUM('SG', 'NSG') NOT NULL,
    sg_number VARCHAR(50)
);

-- Create Workorders Table
CREATE TABLE workorders (
    workorder_no INT AUTO_INCREMENT PRIMARY KEY,
    workorder_date DATE NOT NULL,
    item_id INT NOT NULL,
    consignee_id INT NOT NULL,
    allocation_no VARCHAR(100),
    quantity INT NOT NULL,
    job_number VARCHAR(8) NOT NULL UNIQUE,
    status ENUM('Active', 'Inactive') DEFAULT 'Active',
    FOREIGN KEY (item_id) REFERENCES items(item_id),
    FOREIGN KEY (consignee_id) REFERENCES consignees(consignee_id)
);