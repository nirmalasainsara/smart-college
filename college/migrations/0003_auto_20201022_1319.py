# Generated by Django 3.1.2 on 2020-10-22 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_notes_file_paper_video_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='upload',
            new_name='upload_paper',
        ),
    ]