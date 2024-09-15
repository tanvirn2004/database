#1 
SELECT country.name AS "country name", airport.name AS "airport name"  
FROM country JOIN airport ON country.iso_country = airport.iso_country  
WHERE country.name = 'Iceland';![Screenshot (77).png](..%2F..%2FOneDrive%2FPictures%2FScreenshots%2FScreenshot%20%2877%29.png)