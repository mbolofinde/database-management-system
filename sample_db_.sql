CREATE DATABASE shopping_cart_db;

USE shopping_cart_db;

CREATE TABLE customer(
    customer_id INT,
    name varchar(100),
    address varchar(100),
    email varchar(100),
    phone varchar(10),
    PRIMARY KEY (customer_id)
);

CREATE TABLE product (
    product_id INT,
    name varchar(100),
    price numeric(8, 2),
    description varchar(255),
    PRIMARY KEY (product_id)
);
CREATE TABLE cart_order (
    order_id int,
    customer_id int,
    product_id int,
    quantity int,
    order_date DATE,
    status varchar(50),
    PRIMARY key(order_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);