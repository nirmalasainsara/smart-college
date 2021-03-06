# Generated by Django 3.1.1 on 2020-10-20 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_degree', models.CharField(choices=[('BTECH', 'Btech'), ('BE', 'Be'), ('BSC', 'Bsc'), ('BCOM', 'Bcom'), ('BA', 'Ba')], default='BTECH', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_college', models.TextField(choices=[('FYR', 'first_year'), ('SYR', 'second_year'), ('TYR', 'third_year'), ('FOYR', 'fourth_year')], default='FYR', max_length=200)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.category')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.category')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.year')),
            ],
        ),
    ]
