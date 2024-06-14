# Физическая модель

---

Таблица `students`:

| Название      | Описание                       | Тип данных     | Ограничение   |
|---------------|--------------------------------|----------------|---------------|
| `studentid`   | Идентификатор студента         | `SERIAL`       | `PRIMARY KEY` |
| `first_name`  | Имя студента                   | `VARCHAR(100)` | `NOT NULL`    |
| `second_name` | Фамилия студента               | `VARCHAR(100)` | `NOT NULL`    |
| `sex`         | Пол студента (male или female) | `VARCHAR(10)`  | `NOT NULL`    |
| `group_name`  | Номер группы                   | `VARCHAR(10)`  | `NOT NULL`    |

Таблица `teachers`:

| Название       | Описание                             | Тип данных     | Ограничение   |
|----------------|--------------------------------------|----------------|---------------|
| `teacherid`    | Идентификатор преподавателя          | `SERIAL`       | `PRIMARY KEY` |
| `first_name`   | Имя преподавателя                    | `VARCHAR(100)` | `NOT NULL`    |
| `second_name`  | Фамилия преподавателя                | `VARCHAR(100)` | `NOT NULL`    |
| `sex`          | Пол преподавателя (male или female)  | `VARCHAR(10)`  | `NOT NULL`    |

Таблица `lessons`:

| Название      | Описание                    | Тип данных     | Ограничение   |
|---------------|-----------------------------|----------------|---------------|
| `subjectid`   | Идентификатор предмета      | `SERIAL`       | `PRIMARY KEY` |
| `name`        | Название предмета           | `VARCHAR(100)` | `NOT NULL`    |
| `group_name`  | Номер группы                | `VARCHAR(10)`  | `NOT NULL`    |
| `teacherid`   | Идентификатор преподавателя | `SERIAL`       | `FOREIGN KEY` |

---
Таблица `students`:
```postgresql
CREATE TABLE ub.students(
    studentid        SERIAL                 NOT NULL,
    first_name       VARCHAR(100)           NOT NULL,
    second_name      VARCHAR(100)           NOT NULL,
    sex              VARCHAR(10)            NOT NULL,
    group_name       VARCHAR(10)            NOT NULL,

    CONSTRAINT students_pk PRIMARY KEY (studentid),
                     
    CONSTRAINT sex_ch CHECK (sex in ('male', 'female'))
);
```
Таблица `teachers`:
```postgresql
CREATE TABLE ub.teachers(
    teacherid      SERIAL                 NOT NULL,
    first_name     VARCHAR(100)           NOT NULL,
    second_name    VARCHAR(100)           NOT NULL,
    sex            VARCHAR(10)            NOT NULL,

    CONSTRAINT teachers_pk PRIMARY KEY (teacherid),

    CONSTRAINT sex_ch CHECK (sex in ('male', 'female'))
);
```
Таблица `lessons`:
```postgresql
CREATE TABLE ub.lessons(
    subjectid           SERIAL                  NOT NULL,
    name                VARCHAR(100)            NOT NULL, 
    group_name          VARCHAR(10)             NOT NULL,
    teacherid           SERIAL                  NOT NULL,
                        
    CONSTRAINT lessons_pk PRIMARY KEY (subjectid),
    
    CONSTRAINT fk_lessons_teacherid FOREIGN KEY (teacherid) REFERENCES ub.teachers(teacherid)
);
```
