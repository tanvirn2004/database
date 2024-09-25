## 1 select country.name as "country name", airport.name as "airport name" from country, airport where airport.iso_country = country.iso_country and country.name = "Iceland";


![Screenshot (135)](https://github.com/user-attachments/assets/1e265e1a-394d-4222-b10b-c5ebbb11fff8)



###2  select airport.name as "Airport Name" from airport,country where airport.iso_country = country.iso_country and country.name = "France" and airport.type = "large_airport";




![Capture](https://github.com/user-attachments/assets/013af419-6491-43a8-8aa4-ea8fe2627732)


## 3 Select country.name as "country_name", airport.name as "airport_name" from airport,country where airport.iso_country = country.iso_country and country.continent = "AN"; 


![4](https://github.com/user-attachments/assets/80d1d23f-5107-4181-97c2-c9a6ba59c8f9)


## 4  select elevation_ft from airport,game where game.location = ident and screen_name ="Heini";


![5](https://github.com/user-attachments/assets/154e80af-e6b0-4d8e-803d-e9e6e6238a0d)


## 5 select elevation_ft * 0.3048 as "elevation_m" from airport,game where game.location = ident and screen_name ="Heini";




![6](https://github.com/user-attachments/assets/4e62640d-86b7-4ea7-af7a-2604353da25c)


## 6 select name from airport,game where location = ident and screen_name = "Ilkka";




![7](https://github.com/user-attachments/assets/807ec835-e151-4fad-a03b-ab765c0ae7b5)


## 7 select country.name from airport,country,game where airport.iso_country = country.iso_country and location = ident and screen_name = "Ilkka";




![8](https://github.com/user-attachments/assets/f87ebaa6-bd59-43b8-920c-8cb1615d2f36)


## 8 select name from goal, goal_reached, game where game_id and goal.id = goal_id and screen_name = "Heini";


![9](https://github.com/user-attachments/assets/2d16d9f6-49ad-4567-8d02-0aa40233e667)




### 9 .select airport.name from game, goal_reached, goal, airport where ident = location and game.id = game_id and goal.id = goal_id and screen_name = "Ilkka" and goal.name = "CLOUDS";

 



![10](https://github.com/user-attachments/assets/843a7c55-4e52-45bc-9bea-6bf81b714135)

### 10 . select country.name from game, goal_reached, goal, country, airport where airport.iso_country = country.iso_country and ident = location and game.id = game_id and goal.id = goal_id and screen_name = "Ilkka" and goal.name = "CLOUDS";


![11](https://github.com/user-attachments/assets/0572c1a3-11e4-468c-8661-04bd1c7e5eb0)




