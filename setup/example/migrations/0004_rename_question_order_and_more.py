# Generated by Django 4.2 on 2023-04-20 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_remove_question_pub_date_delete_choice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Order',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='question_text',
            new_name='name',
        ),
    ]
