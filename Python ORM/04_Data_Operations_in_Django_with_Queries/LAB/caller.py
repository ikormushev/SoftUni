import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Student


# Run and print your queries
def add_students():
    Student.objects.create(
        student_id="FC5204",
        first_name="John",
        last_name="Doe",
        birth_date='1995-05-15',
        email="john.doe@university.com"
    )

    Student.objects.create(
        student_id="FE0054",
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@university.com"
    )

    student_alice = Student(
        student_id="FH2014",
        first_name="Alice",
        last_name="Johnson",
        birth_date='1998-02-10',
        email="alice.johnson@university.com"
    )
    student_alice.save()

    student_bob = Student(
        student_id="FH2015",
        first_name="Bob",
        last_name="Wilson",
        birth_date='1996-11-25',
        email="bob.wilson@university.com"
    )
    student_bob.save()


# add_students()
# print(Student.objects.all())

def get_students_info():
    students = Student.objects.all()
    result = []

    for st in students:
        result.append(f"Student №{st.student_id}: "
                      f"{st.first_name} {st.last_name}; "
                      f"Email: {st.email}\n")
    return ''.join(result)


# print(get_students_info())

def update_students_emails():
    students = Student.objects.all()

    for st in students:
        split_email = st.email.split("@")
        split_email[1] = "uni-students.com"
        st.email = "@".join(split_email)
        st.save()

        # # Other Way
        # new_email = st.email.replace("university.com", "uni-students.com")
        # st.email = new_email
        # st.save()


# update_students_emails()
#
# for student in Student.objects.all():
#     print(student.email)

def truncate_students():
    students = Student.objects.all()
    students.delete()

# truncate_students()
# print(Student.objects.all())
# print(f"Number of students: {Student.objects.count()}")
