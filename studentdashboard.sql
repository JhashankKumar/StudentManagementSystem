CREATE DATABASE student_dashboard;

USE student_dashboard;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'teacher') NOT NULL
);

CREATE TABLE results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    studentName VARCHAR(255) NOT NULL,
    telugu INT NOT NULL,
    hindi INT NOT NULL,
    english INT NOT NULL,
    maths INT NOT NULL,
    attendance FLOAT NOT NULL
);

