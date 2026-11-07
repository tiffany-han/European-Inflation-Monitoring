CREATE DATABASE if not exists eurostat;

#check data completeness
SELECT COUNT(*)
FROM HICP_data;

#add a composite unique key to prevent duplicate insertion
ALTER TABLE hicp_data
ADD CONSTRAINT uq_hicp
UNIQUE (country_code, `unit of measure`, category_code, `Time` );


