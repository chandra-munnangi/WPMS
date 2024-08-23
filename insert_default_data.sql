-- Insert default users
INSERT INTO users (username, password, section, user_type) 
VALUES 
('admin', 'hashed_password', 'Admin Section', 'Admin'),
('shop_user', 'hashed_password', 'Shop Section', 'Shop Floor'),
('pco_user', 'hashed_password', 'PCO Section', 'PCO');

-- Insert default consignees
INSERT INTO consignees (zone, division, indenter, consignee, consignee_type)
VALUES
('SCR', 'Guntakal', 'Indenter 1', 'Consignee 1', 'Home Revenue'),
('SCR', 'Secunderabad', 'Indenter 2', 'Consignee 2', 'Projects'),
('CR', 'Mumbai', 'Indenter 3', 'Consignee 3', 'Construction');

-- Insert default items
INSERT INTO items (item_name, item_description, item_type, sg_number)
VALUES
('Item A', 'Description A', 'SG', 'SG12345'),
('Item B', 'Description B', 'NSG', NULL),
('Item C', 'Description C', 'SG', 'SG67890');