# Generated by Django 5.0.4 on 2024-04-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_employerprofile_email_jobseekerprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='employerprofile',
            name='company_name',
            field=models.CharField(default='Atlantis', max_length=50),
            preserve_default=False,
        ),
    ]
