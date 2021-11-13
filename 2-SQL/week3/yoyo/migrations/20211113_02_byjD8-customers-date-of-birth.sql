-- customers date_of_birth
-- depends: 20211113_01_xevv9-customers-table
ALTER TABLE customers
    ADD COLUMN date_of_birth TIMESTAMP;
