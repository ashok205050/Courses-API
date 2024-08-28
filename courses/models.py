from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10, unique=True)  
    description = models.TextField()
    def __str__(self):
        return self.title

class CourseInstance(models.Model):
    instance_id = models.AutoField(primary_key=True)  
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.IntegerField()
    semester = models.CharField(max_length=10)

    class Meta:
        unique_together = ('course', 'year', 'semester')

    def __str__(self):
        return f"{self.course.title} - {self.year} - Semester {self.semester}"
