CREATE TABLE PHONE_BOOK
(
    user_name    varchar NOT NULL,
    contact_name varchar NOT NULL,
    phone_number varchar NOT NULL,
    birth_date   date,

    primary key (user_name, contact_name)
)