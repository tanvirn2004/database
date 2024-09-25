### 1. Select * from goal;


![1](https://github.com/user-attachments/assets/27613340-5b53-4a04-9d54-614c3bd44ec5)

## 2. Select name, type from airport where iso_country = 'FI';

![2](https://github.com/user-attachments/assets/b302502f-2fad-47df-9a46-b0d514fb0fdf)



# 3 . select name from airport where iso_country = "FI" order by name;



![3](https://github.com/user-attachments/assets/8da1a087-1fe9-4de4-9ac8-e33b1cab3513)


# 4 . select name, type from airport where iso_country = "FI" order by type,name;


![4](https://github.com/user-attachments/assets/dea7fa4a-2efb-4818-b04c-33bc98882d62)

### 5. select name from country where name like "F%";

![5](https://github.com/user-attachments/assets/39c55353-c639-4ed3-a587-4fb7b7a5b7f6)


6.  select name from country where name like "%F%";


![6](https://github.com/user-attachments/assets/2b903507-ac55-457d-9491-17a1ad2ea7f4)

7. select location from game where screen_name = "Vesa";



![7](https://github.com/user-attachments/assets/7597319b-be59-4a72-9c36-0c849963efe5)

8.select co2_consumed from game where screen_name = "Ilkka";

![8](https://github.com/user-attachments/assets/dc790c48-8bfa-4655-83e3-83355f6cefa5)


9..select distinct co2_budget from game;




![9](https://github.com/user-attachments/assets/e508598d-14cd-42fe-960d-aec6b3d93b07)

10.. SELECT screen_name, co2_budget, co2_consumed, (co2_budget - co2_consumed) AS co2_left FROM game WHERE screen_name = 'Ilkka';






![10](https://github.com/user-attachments/assets/1997009b-d28d-4290-b93d-be68504dda44)














