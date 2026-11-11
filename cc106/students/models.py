from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    contact_no = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'registration'  # <--- This is your custom table name!

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"