	-- CREATE TABLE students (
--     id INT PRIMARY KEY,
--     first_name VARCHAR(100),
--     last_name VARCHAR(100),
--     email VARCHAR(100),
--     gender VARCHAR(10),
--     part_time_job BOOLEAN,
--     absence_days INT,
--     extracurricular_activities BOOLEAN,
--     weekly_self_study_hours INT,
--     career_aspiration VARCHAR(100),
--     math_score INT,
--     history_score INT,
--     physics_score INT,
--     chemistry_score INT,
--     biology_score INT,
--     english_score INT,
--     geography_score INT
-- );

-- COPY students(id, first_name, last_name, email, gender, part_time_job, absence_days, 
-- extracurricular_activities, weekly_self_study_hours, career_aspiration, math_score, history_score, 
-- physics_score, chemistry_score, biology_score, english_score, geography_score)
-- FROM 'D:\mis\student-scores.csv'
-- DELIMITER ','
-- CSV HEADER;

select * from students;

-- 1)Calculate the average math_score for each career_aspiration. 
-- Order the results by the average score in descending order.

select career_aspiration, round(avg(math_score), 2) as avg_math 
from students group by career_aspiration order by avg_math desc;



-- 2)Find the career_aspirations that have an average english_score greater than 75. 
-- Display the career aspiration and the average score.

select * from (
	select career_aspiration, round(avg(english_score), 2) as avg_english
	from students group by career_aspiration) as a
where avg_english > 75 order by avg_english desc;



-- 3)Identify students who have a math_score higher than the school's average math score. 
-- List their first_name, last_name, and math_score.

select first_name, last_name, math_score from students 
where math_score > (select avg(math_score) from students);



-- 4)Rank students within each career_aspiration category by their physics_score in descending order. 
-- Display the first_name, last_name, career_aspiration, physics_score, and the rank.

select first_name, last_name, career_aspiration, physics_score,
dense_rank() over(partition by career_aspiration order by physics_score desc)
from students;



-- 5) For each student, create a new column full_name by concatenating first_name and last_name 
-- with a space in between. Show the full_name and email columns where the email contains 
-- the string "academy".

select first_name || ' ' || last_name as full_name, email from students
where email like '%academy%';



-- 6)Calculate the lowest (FLOOR), highest (CEIL), and average (ROUND to two decimal places) 
-- chemistry_score for each career aspirant. Display the career aspirants, lowest score, 
-- highest score, and average score.

select career_aspiration, min(chemistry_score), max(chemistry_score), round(avg(chemistry_score), 2) 
from students
group by career_aspiration;



-- 7)Find career aspirations where the average history_score is above 85 and at least 5 students 
-- aspire to that career. List the career_aspiration and the average score.

select career_aspiration, round(avg(history_score)) as avg, count(career_aspiration) from students
group by career_aspiration
having round(avg(history_score)) > 85;



-- 8)Identify students who score above average in both biology and chemistry, 
-- compared to the school's average for those subjects. Display their id, first_name, last_name, 
-- biology_score, and chemistry_score.

select id, first_name, last_name, biology_score, chemistry_score from students 
where biology_score > (select avg(biology_score) from students)
and chemistry_score > (select avg(chemistry_score) from students);



-- 9)Calculate the percentage of absence days for each student relative to the total absence 
-- days recorded for all students. Display the id, first_name, last_name, and the calculated 
-- percentage, rounded to two decimal places. Order the results by the percentage in descending order

select id, first_name, last_name, 
round((absence_days::decimal / (select sum(absence_days) from students) * 100), 2) as absent_percentage
from students
order by 4 desc;



-- 10)Identify students who have scores above 80 in at least three out of the six subjects: 
-- math, history, physics, chemistry, biology, and English. Display their id, first_name, last_name, 
-- and the count of subjects where they scored above 80.

select id, first_name, last_name, 
math+history+physics+chemistry+biology+english as subject_count from (
	select id, first_name, last_name,
	case when math_score > 80 then 1 else 0 end as math,
	case when history_score > 80 then 1 else 0 end as history,
	case when physics_score > 80 then 1 else 0 end as physics,
	case when chemistry_score > 80 then 1 else 0 end as chemistry,
	case when biology_score > 80 then 1 else 0 end as biology,
	case when english_score > 80 then 1 else 0 end as english
from students)
where math+history+physics+chemistry+biology+english >= 3;













