CREATE TABLE user_roles (
    id serial PRIMARY KEY,
    role_name VARCHAR (50) UNIQUE NOT NULL
);