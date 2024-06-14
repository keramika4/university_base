-- посмотрим на витрины
select *
from ub.students
limit 10;

select *
from ub.teachers
limit 10;

select *
from ub.lessons
limit 10;

-- список всех преподавателей и число их студентов
select
	t.teacherid
    , t.first_name
  	, t.second_name
    , case when sum(g.students_cnt) > 0 then sum(g.students_cnt) else 0 end as students_cnt
from (
	select
  		t.teacherid
  		, t.first_name
  		, t.second_name
  		, l.group_name
  	from ub.teachers t
  	left join ub.lessons l
  		on t.teacherid = l.teacherid
  	group by 1, 2, 3, 4
) t
left join (
    select
        distinct l.group_name
        , count(distinct s.studentid) as students_cnt
    from ub.lessons l
    left join ub.students s
        on l.group_name = s.group_name
    group by 1
) g
    on t.group_name = g.group_name
group by 1, 2, 3
;

-- список всех студентов и их преподавателей
select
	s.studentid
    , s.first_name as student_first_name
    , s.second_name as student_second_name
    , s.group_name
    , g.teacherid
    , g.first_name as teacher_first_name
    , g.second_name as teacher_second_name
from ub.students s
left join (
	select
		l.group_name
  		, t.teacherid
  		, t.first_name
  		, t.second_name
  	from ub.lessons l
  	left join ub.teachers t
  		on t.teacherid = l.teacherid
    group by 1, 2, 3, 4
) g
	on s.group_name = g.group_name
;
