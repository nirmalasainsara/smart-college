# Generated by Django 3.1.2 on 2020-10-22 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Notes_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_paper', models.TextField(max_length=200)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.subject')),
            ],
        ),
    ]
