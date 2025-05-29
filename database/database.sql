CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('admin', 'secretary', 'coordinator') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE scholarship (
    id INT AUTO_INCREMENT PRIMARY KEY,
    concession_year INT NOT NULL,
    ies_code VARCHAR(20) NOT NULL,
    ies_name VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    campus VARCHAR(255) NOT NULL,
    scholarship_type VARCHAR(50) NOT NULL,
    education_mode VARCHAR(50) NOT NULL,
    course VARCHAR(150) NOT NULL,
    shift VARCHAR(50) NOT NULL,
    beneficiary_cpf VARCHAR(14) NOT NULL,
    gender VARCHAR(20) NOT NULL,
    race VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    has_disability BOOLEAN NOT NULL,
    region VARCHAR(50) NOT NULL,
    state CHAR(2) NOT NULL,
    beneficiary_city VARCHAR(100) NOT NULL
);
