###1
select max(elevation_ft) from airport; 





![update1](https://github.com/user-attachments/assets/817cf551-8e2a-4d1b-b336-21ffa7b3f805)





2. Select continent, count(*) from country group by continent;




![update 2 s](https://github.com/user-attachments/assets/a87f3d50-7789-4094-9b6a-cf50001dc6a4)





3. select screen_name, count (*) from game, goal_reached where id = game_id group by screen_name;




![update 3](https://github.com/user-attachments/assets/ffc26d8d-0d28-4347-bb27-867300bfe64c)




4.select screen_name from game where co2_consumed in(select min(co2_consumed) from game);



![update 4](https://github.com/user-attachments/assets/e121eb21-ce01-46ff-af29-3a2fc907f54a)




5.select country.name, count() from airport, country where airport.iso_country = country.iso_country group by country.iso_country order by count() desc limit 50;




![upgrade 5](https://github.com/user-attachments/assets/f7b7abb4-2706-45b7-9b70-8fcfe8b1f7b2)





6. select country.name from airport, country where airport.iso_country = country.iso_country group by country.iso_country having count(*) > 1000;

![update 6](https://github.com/user-attachments/assets/d006e776-542d-4c29-b2d4-fb01f1c5e127)





7.
select name from airport where elevation_ft in (select max(elevation_ft) from airport;




![update 7](https://github.com/user-attachments/assets/2c6ab92c-d856-491e-84fa-95185099bfbb)




8.select name from country where iso_country in (select iso_country from airport where elevation_ft in( select max(elevation_ft) from airport));




![update8](https://github.com/user-attachments/assets/0a4956d1-ef81-4839-a230-8b3b27e91720)




9.select count(*) from game, goal_reached where id = game_id and screen_name = "Vesa" group by screen_name;



![update 9](https://github.com/user-attachments/assets/f884d919-5907-4ab8-8088-fe6c4e9b337b)


10. select name from airport where latitude_deg in(select min(latitude_deg) from airport;



![update 10](https://github.com/user-attachments/assets/1f0d70fb-7c32-45ec-bde9-03f3c0b3d765)























