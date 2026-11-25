CREATE DATABASE if not exists eurostat;

#add a composite unique key to prevent duplicate insertion
ALTER TABLE hicp_data
ADD CONSTRAINT uq_hicp
UNIQUE (country_code, `unit of measure`, category_code, `Time` );

#check data completeness
SELECT DISTINCT country_code FROM hicp_data WHERE `value` IS NULL;

SELECT country_code, COUNT(*) AS record_count, COUNT(`value`) AS non_null_count, SUM(`value` IS NULL) AS null_count
FROM hicp_data
GROUP BY country_code
ORDER BY record_count;

#check data coverage period for each country
SELECT country_code, MIN(`Time`) AS first_period, MAX(`Time`) AS last_period, COUNT(DISTINCT `Time`) AS period_count
FROM hicp_data
GROUP BY country_code;


#query
SELECT * FROM hicp_data WHERE country_code IN (US);

#add monthly_hicp_trends view
CREATE OR REPLACE VIEW monthly_hicp_trends AS SELECT * FROM hicp_data 
WHERE country_code IN ('EU27_2020','EA21');


#add eu_members_data view
CREATE VIEW eu_members_data 
AS SELECT h.*
FROM hicp_data h
JOIN country_reference c ON c.country_code = h.country_code
WHERE c.is_eu_member=TRUE;



