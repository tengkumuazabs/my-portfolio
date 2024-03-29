# Airport Database Analyis

## Entity Relationship Diagram
<img width="577" alt="image" src="https://raw.githubusercontent.com/tengkumuazabs/my-portfolio/main/sql/erd%20diagram/ERD_Airlines.png">
This database contains 8 tables and the relations are shown above.

## Q1: How to obtain the ticket information that was ordered by ZULFIYA ZOTOVA and when she booked it?
````sql
select t.*, b.book_date
from tickets t
inner join bookings b on t.book_ref=b.book_ref
where passenger_name='ZULFIYA ZOTOVA';
````
**Answer:**
|ticket_no    |book_ref|passenger_id|passenger_name|contact_data                                                        |book_date             |
|-------------|--------|------------|--------------|--------------------------------------------------------------------|----------------------|
|0005434344902|5FC24D  |1382 788097 |ZULFIYA ZOTOVA|{"phone": "+70612043305"}                                           |2017-08-02 00:53:00+07|
|0005435132853|403D67  |0029 039458 |ZULFIYA ZOTOVA|{"email": "zotova-z.051987@postgrespro.ru", "phone": "+70305717265"}|2017-07-13 00:57:00+07|

She booked it two times at July 13rd and August 2nd 2017.

## Q2: How to obtain all aircrafts except SU9, 320, and 773?
````sql
select * 
from aircrafts
where aircraft_code not in ('SU9','320','773');
````
**Answer:**
|aircraft_code|model                                                   |range|
|-------------|--------------------------------------------------------|-----|
|763          |{"en": "Boeing 767-300", "ru": "Боинг 767-300"}         |7900 |
|321          |{"en": "Airbus A321-200", "ru": "Аэробус A321-200"}     |5600 |
|319          |{"en": "Airbus A319-100", "ru": "Аэробус A319-100"}     |6700 |
|733          |{"en": "Boeing 737-300", "ru": "Боинг 737-300"}         |4200 |
|CN1          |{"en": "Cessna 208 Caravan", "ru": "Сессна 208 Караван"}|1200 |
|CR2          |{"en": "Bombardier CRJ-200", "ru": "Бомбардье CRJ-200"} |2700 |

This result shows all aircrafts except SU9, 320, and 773.

## Q3: How many flights that weren't actually departed and arrived and vice versa and its difference? 
````sql
select 
(select count(*) as total from flights
where actual_departure isnull and actual_arrival isnull) as not_departed_arrived, 
(select count(*) as total from flights
where actual_departure is not null and actual_arrival is not null) departed_arrived, 
(select count(*) as total from flights
where actual_departure is not null and actual_arrival is not null) - (select count(*) as total from flights
where actual_departure isnull and actual_arrival isnull) as diff;
````
**Answer:**
|not_departed_arrived|departed_arrived                                                 |difference                      |
|--------------------|-----------------------------------------------------------------|--------------------------------|
|16348               |16715                                                            |367                             |

There were 16.715 flights that did departed and arrived and 16.348 didn't. The differences between them is 367.

## Q4: How to obtain all many airports in Moscow? 
````sql
select * from airports where city ->> 'en' = 'Moscow';
````
**Answer:**
|airport_code|airport_name                                                     |city                            |coordinates                          |timezone     |
|------------|-----------------------------------------------------------------|--------------------------------|-------------------------------------|-------------|
|SVO         |{"en": "Sheremetyevo International Airport", "ru": "Шереметьево"}|{"en": "Moscow", "ru": "Москва"}|(37.4146,55.972599)                  |Europe/Moscow|
|VKO         |{"en": "Vnukovo International Airport", "ru": "Внуково"}         |{"en": "Moscow", "ru": "Москва"}|(37.2615013123,55.5914993286)        |Europe/Moscow|
|DME         |{"en": "Domodedovo International Airport", "ru": "Домодедово"}   |{"en": "Moscow", "ru": "Москва"}|(37.90629959106445,55.40879821777344)|Europe/Moscow|

There are three airport in Moscow.

## Q5: How much range that each aircraft has in miles? (1 mile = 1.609 km)
````sql
select model,range,round(range/1.609,2) as miles from aircrafts;
````
**Answer:**
|model                                                     |range|miles  |
|----------------------------------------------------------|-----|-------|
|{"en": "Boeing 777-300", "ru": "Боинг 777-300"}           |11100|6898.69|
|{"en": "Boeing 767-300", "ru": "Боинг 767-300"}           |7900 |4909.88|
|{"en": "Sukhoi Superjet-100", "ru": "Сухой Суперджет-100"}|3000 |1864.51|
|{"en": "Airbus A320-200", "ru": "Аэробус A320-200"}       |5700 |3542.57|
|{"en": "Airbus A321-200", "ru": "Аэробус A321-200"}       |5600 |3480.42|
|{"en": "Airbus A319-100", "ru": "Аэробус A319-100"}       |6700 |4164.08|
|{"en": "Boeing 737-300", "ru": "Боинг 737-300"}           |4200 |2610.32|
|{"en": "Cessna 208 Caravan", "ru": "Сессна 208 Караван"}  |1200 |745.80 |
|{"en": "Bombardier CRJ-200", "ru": "Бомбардье CRJ-200"}   |2700 |1678.06|

By dividing all original ranges by 1,609. We can get the same range but in miles.

## Q6: How to obtain passengers that ordered ticket at least 500 times?
````sql
select passenger_name, count(*)
from tickets
group by passenger_name
having count(*) > 500 
order by count desc;
````
**Answer:**
|passenger_name                                            |count|
|----------------------------------------------------------|-----|
|ALEKSANDR IVANOV                                          |842  |
|ALEKSANDR KUZNECOV                                        |755  |
|SERGEY IVANOV                                             |634  |
|SERGEY KUZNECOV                                           |569  |
|VLADIMIR IVANOV                                           |551  |

Five passengers were ordered ticket at least 500 times. ALEKSANDR IVANOV ordered the most.

## Q7: How many seats of each aircraft?
````sql
select s.aircraft_code, a.model ->> 'en' as model, count(s.seat_no) as number_of_seats from seats s
inner join aircrafts a on s.aircraft_code=a.aircraft_code
group by 1,2 order by number_of_seats;
````
**Answer:**
|aircraft_code                                             |model|number_of_seats|
|----------------------------------------------------------|--------|---------------|
|CN1                                                       |Cessna 208 Caravan|12             |
|CR2                                                       |Bombardier CRJ-200|50             |
|SU9                                                       |Sukhoi Superjet-100|97             |
|319                                                       |Airbus A319-100|116            |
|733                                                       |Boeing 737-300|130            |
|320                                                       |Airbus A320-200|140            |
|321                                                       |Airbus A321-200|170            |
|763                                                       |Boeing 767-300|222            |
|773                                                       |Boeing 777-300|402            |

Cessna 208 Caravan has the least seats and Boeing 777-300 has the maximum seats capacity.

## Q8: How to obtain aircraft models with additional information of their ranges? (less than 2000 is short, between 2000 and 5000 is middle, more than 5000 is long)
````sql
select model ->> 'en' model, range,
case when range < 2000 then 'Short'
when range > 2000 and range < 5000 then 'Middle'
else 'Long' end range_info
from aircrafts order by model;
````
**Answer:**
|model                                                     |range|range_info|
|----------------------------------------------------------|-----|----------|
|Airbus A319-100                                           |6700 |Long      |
|Airbus A320-200                                           |5700 |Long      |
|Airbus A321-200                                           |5600 |Long      |
|Boeing 737-300                                            |4200 |Middle    |
|Boeing 767-300                                            |7900 |Long      |
|Boeing 777-300                                            |11100|Long      |
|Bombardier CRJ-200                                        |2700 |Middle    |
|Cessna 208 Caravan                                        |1200 |Short     |
|Sukhoi Superjet-100                                       |3000 |Middle    |

Five aircrafts are categorized as long, three aircrafts are categrorized as middle, and only one are categorized as short.

On sixth month, the amount of bookings was 523.346.200

## Q9: Who traveled from SVO to OVB on seat 1A on 27 July 2017, and when he booked it?
````sql
select bp.flight_id, f.departure_airport, f.arrival_airport, f.actual_departure, 
t.passenger_name, bp.seat_no, b.book_date from boarding_passes bp 
inner join flights f on bp.flight_id=f.flight_id
inner join tickets t on bp.ticket_no=t.ticket_no
inner join bookings b on t.book_ref=b.book_ref
where bp.seat_no='1A' and f.departure_airport='SVO' and f.arrival_airport='OVB' 
and date(f.actual_departure)='2017-7-27';
````
**Answer:**
|flight_no|departure_airport|arrival_airport|actual_departure      |passenger_name  |seat_no|book_date             |
|---------|-----------------|---------------|----------------------|----------------|-------|----------------------|
|PG0277   |SVO              |OVB            |2017-07-27 15:47:00+07|VLADIMIR SMIRNOV|1A     |2017-07-06 17:24:00+07|

VLADIMIR SMIRNOV traveled from SVO to OVB using flight PG0277 and he sat on seat 1A. He booked it on July 6th 2017.

## Q10: How to obtain total flights and total passengers for each hours which happened at August 2nd 2018 and departed from SVO?
````sql
select f.hour, total_flights, total_passengers from
(select date_part('hour', f.actual_departure) as hour, count(f.flight_no) total_flights 
from flights f 
where departure_airport='SVO'
and date(actual_departure)='2017-08-02' group by hour
order by hour asc) f
inner join 
(select date_part('hour', f.actual_departure) as hour, 
count(bp.seat_no) as total_passengers from flights f 
inner join boarding_passes bp on f.flight_id=bp.flight_id
where departure_airport='SVO'
and date(actual_departure)='2017-08-02' group by hour
order by hour asc) p
on f.hour=p.hour;
````
|hour|total_flights|total_passengers|
|----|-------------|----------------|
|13  |5            |484             |
|14  |5            |381             |
|15  |7            |518             |
|16  |7            |521             |
|17  |5            |157             |
|18  |6            |239             |
|19  |1            |13              |
|20  |5            |273             |
|21  |3            |421             |
|22  |4            |237             |
|23  |1            |30              |

On August 2nd 2018, flights that departed from SVO happened first at 13rd hour and ended at 23rd hour. Maximum flights happened at 15th and 16th hours (7 flights). Maximum passengers departed happened at 16th hour (521 passengers).
