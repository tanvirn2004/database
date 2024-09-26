### 1 . Assignment: Join

Select country.name as "country name", airport.name as "airport name" from country join airport on country.iso_country = airport.iso_country where country.name = "Finland";

![join 1](https://github.com/user-attachments/assets/30aaf4c2-dbb6-4a29-8f7d-e47dbd15d01e)


## 2 .
select screen_name, airport.name from game inner join airport on location = ident;


![join2](https://github.com/user-attachments/assets/15447a1a-4353-4878-b9f8-b642e6f400db)



##3. select screen_name, country.name from game inner join airport on location = ident
inner join country on airport.iso_country = country.iso_country;


![join3](https://github.com/user-attachments/assets/c0d3d617-9147-46bc-b778-c76a8072d81e)


##4 
select airport.name, screen_name from airport left join game on ident = location where airport.name like "%Hels%";




![q4](https://github.com/user-attachments/assets/9ed09692-f576-4293-ae4e-828f81df11e6)


##5

select name, screen_name from goal left join goal_reached on goal.id = goal_id left join game on game.id = game_id;


![q5](https://github.com/user-attachments/assets/8ce8e68c-45e6-4666-9b61-6387634635ac)












