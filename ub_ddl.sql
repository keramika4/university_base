drop table if exists ub.students;
drop table if exists ub.teachers;
drop table if exists ub.lessons;

drop schema if exists ub;
create schema ub; -- university base

CREATE TABLE ub.students(
    studentid        SERIAL                 NOT NULL,
    first_name       VARCHAR(100)           NOT NULL,
    second_name      VARCHAR(100)           NOT NULL,
    sex              VARCHAR(10)            NOT NULL,
    group_name       VARCHAR(10)            NOT NULL,

    CONSTRAINT students_pk PRIMARY KEY (studentid),

    CONSTRAINT sex_ch CHECK (sex in ('male', 'female'))
);

CREATE TABLE ub.teachers(
    teacherid      SERIAL                 NOT NULL,
    first_name     VARCHAR(100)           NOT NULL,
    second_name    VARCHAR(100)           NOT NULL,
    sex            VARCHAR(10)            NOT NULL,

    CONSTRAINT teachers_pk PRIMARY KEY (teacherid),

    CONSTRAINT sex_ch CHECK (sex in ('male', 'female'))
);

CREATE TABLE ub.lessons(
    subjectid           SERIAL                  NOT NULL,
    name                VARCHAR(100)            NOT NULL,
    group_name          VARCHAR(10)             NOT NULL,
    teacherid           SERIAL                  NOT NULL,

    CONSTRAINT lessons_pk PRIMARY KEY (subjectid),

    CONSTRAINT fk_lessons_teacherid FOREIGN KEY (teacherid) REFERENCES ub.teachers(teacherid)
);