# Generated by Django 3.1.2 on 2020-10-30 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_paper_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='college.year'),
            preserve_default=False,
        ),
    ]