CREATE TABLE user_roles (
    id serial PRIMARY KEY,
    role_name VARCHAR (50) UNIQUE NOT NULL
);

CREATE TABLE users (
    id serial PRIMARY KEY,
    email VARCHAR(254) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    role_id INTEGER REFERENCES user_roles(id)
);