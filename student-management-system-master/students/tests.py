import random
from django.test import TestCase
from .models import Student


class StudentModelUnitTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            student_number=random.randint(10000, 99999),
            first_name='Deepak',
            last_name='Tyagi',
            email='deepak.tyagi@student.com',
            field_of_study='Cloud Computing',
            gpa=3.92
        )

    def test_student_model(self):
        data = self.student
        self.assertIsInstance(data, Student)