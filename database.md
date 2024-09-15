#1 ![Screenshot (77)](https://github.com/user-attachments/assets/1fcc4788-7999-40a8-8e2b-c2015f24da5d)

SELECT country.name AS "country name", airport.name AS "airport name"  
FROM country JOIN airport ON country.iso_country = airport.iso_country  
WHERE country.name = 'Iceland';
2.![Screenshot (77)](https://github.com/user-attachments/assets/b3124480-1c76-4761-994e-b90142d6ff16)
SELECT airport.name AS "airport name"  
FROM airport INNER JOIN country  
ON airport.iso_country = country.iso_country  
WHERE country.name = 'France' AND airport.type = 'large_airport';
3.
