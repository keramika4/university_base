import random
from faker import Faker
from faker.providers import BaseProvider


class ScienceSubjectProvider(BaseProvider):
    def science_subject(self):
        subjects = [
            "Аэронавтика и астронавтика",
            "Биологическая инженерия",
            "Химическая инженерия",
            "Электротехника и компьютерные науки",
            "Инженерные системы",
            "Экономика",
            "Аналитика бизнеса",
            "Финансы",
            "Менеджмент",
            "Проектирование и управление системами",
            "Биология",
            "Химия",
            "Математика",
            "Физика",
            "Вычеслительная и системная биология",
            "Вычислительные науки и инженерия",
            "Науки о здоровье и технологии",
            "Интегрированный дизайн и управление",
            "Микробиология",
            "Энергетические исследования",
            "Лидерство и предпринимательство",
            "Искусственный интеллект",
            "Робототехника",
            "Квантовые вычисления",
            "Возобновляемая энергия",
            "Нанотехнология"
        ]

        return random.choice(subjects)


fake = Faker("ru_RU")
fake.add_provider(ScienceSubjectProvider)

Faker.seed(0)

num_students = 100
num_teachers = 10
num_lessons = 20
num_groups = 8

students_data = []
for studentid in range(1, num_students + 1):
    sex = random.choice(['male', 'female'])
    if sex == 'male':
        first_name = fake.first_name_male()
        second_name = fake.last_name_male()
    else:
        first_name = fake.first_name_female()
        second_name = fake.last_name_female()
    group_name = f"Г_{random.randint(1, num_groups)}"
    students_data.append((studentid, first_name, second_name, sex, group_name))

teachers_data = []
for teacherid in range(1, num_teachers + 1):
    sex = random.choice(['male', 'female'])
    if sex == 'male':
        first_name = fake.first_name_male()
        second_name = fake.last_name_male()
    else:
        first_name = fake.first_name_female()
        second_name = fake.last_name_female()
    teachers_data.append((teacherid, first_name, second_name, sex))

used_subjects = set()
lessons_data = []
while len(lessons_data) < num_lessons:
    name = fake.science_subject()
    if name not in used_subjects:
        used_subjects.add(name)
        group_name = f"Г_{random.randint(1, num_groups)}"
        teacherid = random.randint(1, num_teachers)
        lessons_data.append((len(lessons_data) + 1, name, group_name, teacherid))

students_sql = "insert into ub.students (studentid, first_name, second_name, sex, group) values\n"
students_sql += ",\n".join(
    [f"({studentid}, '{first_name}', '{second_name}', '{sex}', '{group_name}')" for
                            studentid, first_name, second_name, sex, group_name in students_data]) + ";"

teachers_sql = "insert into ub.teachers (teacherid, first_name, second_name, sex) values\n"
teachers_sql += ",\n".join(
    [f"({teacherid}, '{first_name}', '{second_name}', '{sex}')" for teacherid, first_name, second_name, sex in
     teachers_data]) + ";"

lessons_sql = "insert into ub.lessons (subjectid, name, group_name, teacherid) values\n"
lessons_sql += ",\n".join(
    [f"({subjectid}, '{name}', '{group_name}', {teacherid})" for subjectid, name, group_name, teacherid in lessons_data]) + ";"

print(students_sql + '\n')
print(teachers_sql + '\n')
print(lessons_sql)
