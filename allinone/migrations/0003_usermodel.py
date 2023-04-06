# Generated by Django 4.1.7 on 2023-04-01 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allinone', '0002_alter_student_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
