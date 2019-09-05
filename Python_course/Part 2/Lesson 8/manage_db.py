import psycopg2

conn = psycopg2.connect('dbname=netology_db user=netology_user')
cur = conn.cursor()


def create_db():  # создает таблицы
    cur.execute('CREATE TABLE IF NOT EXISTS Student ('
                'id int primary key not null,'
                'name varchar (100), '
                'gpa numeric(10,2), '
                'birth timestamp with time zone);')

    cur.execute('CREATE TABLE IF NOT EXISTS Course ('
                'id int primary key not null,'
                'name varchar (100));')

    cur.execute('CREATE TABLE IF NOT EXISTS Student_course ('
                'id serial primary key,'
                'student_id integer references Student(id),'
                'course_id integer references Course(id));')
    conn.commit()
    pass


def add_student(student):  # просто создает студента
    cur.execute('insert into student (name, gpa, birth) values (%s, %s, %s)',
                (student, '4.3', '1975-07-08'))
    conn.commit()
    cur.execute('select * from student;')
    pass


def get_student(student_id): # возвращает студента по id
    cur.execute('select * from student where student.id = (%s);', (student_id,))
    result = cur.fetchall()
    print(*result[0][:])
    pass


def get_students(course_id):  # возвращает студентов определенного курса
    cur.execute('select student.id, student.name, course.name from student_course'
                ' join student on student.id = student_course.student_id'
                ' join course on course.id = student_course.course_id'
                ' where course_id = (%s)', (course_id,))
    result = cur.fetchall()
    print(result)
    pass


def add_students(course_id, students):  # создает студентов и записывает их на курс
    for student in students:
        cur.execute('insert into student (name, birth) values (%s, %s)',
                    (student['name'], student['birth']))
        cur.execute('insert into student_course (student_id, course_id) '
                    'values ((select max(id) from student), %s)', (course_id,))
        conn.commit()
    pass
