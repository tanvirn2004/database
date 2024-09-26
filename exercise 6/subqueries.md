##1.  select name from country where iso_country in (select iso_country from airport where name like "Satsuma%");



![sub1](https://github.com/user-attachments/assets/2ad8bea4-6003-4d94-b718-96a81105fc5b)


##2. select name from airport where iso_country in (select iso_country from country where country.name = "Monaco");

![subq2](https://github.com/user-attachments/assets/673113a8-0716-4378-b331-a1a9036bcd5f)

##3.Select screen_name from game where id in(select game_id from goal_reached where goal_id in(select id from goal where name ="CLOUDS"));

![subq3](https://github.com/user-attachments/assets/1d0ecd21-4497-4449-bdbb-bbc97c39e174)

##4.

Select country.name from country where iso_country not in (select airport.iso_country from airport);


![subq4](https://github.com/user-attachments/assets/c215c77b-b51f-4caa-9586-86b05cee456c)


##5.select name from goal where id not in (select goal.id from goal, goal_reached, game where game.id = game_id and goal.id = goal_id and screen_name = "Heini");

![subq5](https://github.com/user-attachments/assets/ac013afa-5f6c-4a60-ac7b-df0be43cbacb)


























