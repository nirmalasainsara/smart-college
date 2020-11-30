from django.db import models
from django.conf import settings


class Category(models.Model):
    BTECH = 'BTECH'
    BE = 'BE'
    BSC = 'BSC'
    BCOM = 'BCOM'
    BA = 'BA'
    FIELD_IN_COLLEGE_CHOICES  = [
        (BTECH, 'Btech'),
        (BE, 'Be'),
        (BSC, 'Bsc'),
        (BCOM, 'Bcom'),
        (BA, 'Ba'), 
    ]
    college_degree = models.CharField(max_length=200,
        choices = FIELD_IN_COLLEGE_CHOICES,
        default = BTECH, 
    )
    def __str__(self):
        return self.college_degree

class Year(models.Model):
    FIRST_YEAR = 'FYR'
    SECOND_YEAR = 'SYR'
    THIRD_YEAR = 'TYR'
    FOURTH_YEAR = 'FOYR'
    YEAR_IN_COLLEGE_CHOICES = [
        (FIRST_YEAR, 'first_year'),
        (SECOND_YEAR, 'second_year'),
        (THIRD_YEAR, 'third_year'),
        (FOURTH_YEAR, 'fourth_year'),
    ]
    year_in_college = models.TextField(max_length=200,
        choices = YEAR_IN_COLLEGE_CHOICES,
        default = FIRST_YEAR,
    )
    degree = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.year_in_college

class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    degree = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.subject_name


class Paper(models.Model):
    upload_paper = models.FileField(upload_to='uploads/%Y/%m/%d/')
    subject= models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    degree = models.ForeignKey(Category, on_delete=models.CASCADE)
    approved = models.BooleanField(default = False)

class Notes_file(models.Model):
    subject_paper = models.TextField(max_length=200)
    subject= models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    degree = models.ForeignKey(Category, on_delete=models.CASCADE)
    

class Video_url(models.Model):
    video = models.URLField(max_length=200)
    subject= models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    degree = models.ForeignKey(Category, on_delete=models.CASCADE)
    

class Material(models.Model):
    material = models.URLField(max_length=200)
    subject= models.ForeignKey(Subject, on_delete=models.CASCADE)


  