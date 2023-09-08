CREATE ROLE shuru WITH superuser;

ALTER ROLE shuru WITH LOGIN PASSWORD 'password';

CREATE DATABASE mql WITH OWNER shuru;

CREATE DATABASE mql_test WITH OWNER shuru;

\c mql

CREATE EXTENSION vector;

\c mql_test

CREATE EXTENSION vector;