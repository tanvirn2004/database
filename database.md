#1 

![Screenshot (77)](https://github.com/user-attachments/assets/1fcc4788-7999-40a8-8e2b-c2015f24da5d)

SELECT country.name AS "country name", airport.name AS "airport name"  
FROM country JOIN airport ON country.iso_country = airport.iso_country  
WHERE country.name = 'Iceland';
2.


![Screenshot (78)](https://github.com/user-attachments/assets/676d89e8-5c9f-4ab3-8c7b-d81fa18e295c)

SELECT airport.name AS "airport name"  
FROM airport INNER JOIN country  
ON airport.iso_country = country.iso_country  
WHERE country.name = 'France' AND airport.type = 'large_airport';
3.


![Screenshot (79)](https://github.com/user-attachments/assets/47f05cd5-6a05-42f8-915e-72abe274ca81)
![Screenshot (80)](https://github.com/user-attachments/assets/a65cf107-0277-4458-839b-bcbda13c92f2)
SELECT country.name AS "country_name", airport.name AS "airport_name" 
FROM airport INNER JOIN country  
ON airport.iso_country = country.iso_country  
WHERE country.continent = 'an';
4.

![Screenshot (81)](https://github.com/user-attachments/assets/a523ad7c-23a5-44c5-b01d-61f8bad9b6fc)
![Screenshot (82)](https://github.com/user-attachments/assets/514e4ccb-5fbd-4e22-8c0a-cf9615698211)
select airport.elevation_ft from game, 
airport where airport.ident = game.location 
and game.screen_name = "heini";
5.

![Screenshot (83)](https://github.com/user-attachments/assets/2e6d2ed5-7bf6-4149-bbad-43e7c1a194b4)
![Screenshot (84)](https://github.com/user-attachments/assets/4791608a-ca58-4c87-8b87-78f069b732fc)
select airport.elevation_ft * 0.3048 as elevation_m from game,
airport where airport.ident = game.location  
and game.screen_name = "heini";
6,

![Screenshot (85)](https://github.com/user-attachments/assets/fd0dab5c-a655-44e6-8554-40c23e5fb000)
![Screenshot (86)](https://github.com/user-attachments/assets/d7a0fbad-5a98-48a1-a313-9a60b9111d15)
select airport.name from game,
airport where airport.ident = game.location 
and game.screen_name = "Ilkka";
7.

![Screenshot (90)](https://github.com/user-attachments/assets/813a67bf-75a8-4787-b1d8-c46383db19be)
SELECT country.name FROM game 
JOIN airport ON airport.ident = game.location 
INNER JOIN country ON country.iso_country = airport.iso_country 
WHERE game.screen_name = "Ilkka";

8.
![Screenshot (91)](https://github.com/user-attachments/assets/0134d8a2-5968-4467-ba83-3e516ae68c93)

select goal.name from goal
INNER JOIN goal_reached ON goal.id = goal_reached.goal_id 
INNER JOIN game on goal_reached.game_id = game.id
WHERE game.screen_name = "heini"
9. 

![Screenshot (92)](https://github.com/user-attachments/assets/b9e71133-3bfa-4f1c-af00-500868122f48)
select airport.name FROM airport 
INNER JOIN game ON airport.ident = game.location   
INNER JOIN goal_reached ON game.id = goal_reached.game_id 
INNER JOIN goal ON goal_reached.goal_id = goal.id 
WHERE goal.name = 'clouds' AND game.screen_name = 'Ilkka';
10.

![Screenshot (93)](https://github.com/user-attachments/assets/57fd6f10-53a0-42ba-97cb-9a23661b811c)
SELECT country.name FROM airport  
INNER JOIN game ON airport.ident = game.location  
INNER JOIN goal_reached ON game.id = goal_reached.game_id  
INNER JOIN goal ON goal_reached.goal_id = goal.id  
INNER JOIN country ON airport.iso_country = country.iso_country  
WHERE goal.name = 'clouds' AND game.screen_name = 'Ilkka';

