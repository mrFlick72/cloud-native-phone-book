CREATE TABLE PHONE_BOOK
(
    user_name    varchar NOT NULL,
    contact_name varchar NOT NULL,
    phone_number varchar NOT NULL,
    birth_date   date,

    primary key (user_name, contact_name)
);

CREATE TABLE ACCOUNT
(
    user_name  varchar NOT NULL primary key,
    password   varchar NOT NULL,
    first_name varchar,
    last_name  varchar
);