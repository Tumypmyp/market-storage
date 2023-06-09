# Generated by Django 4.2 on 2023-04-20 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('IN_PROCESS', 'In Process'), ('COMPLITED', 'Complited')], default='NEW', max_length=15)),
            ],
        ),
    ]
