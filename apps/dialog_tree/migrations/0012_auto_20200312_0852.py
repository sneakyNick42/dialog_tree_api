# Generated by Django 3.0.4 on 2020-03-12 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dialog_tree', '0011_remove_answer_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialog',
            name='questions',
        ),
        migrations.AddField(
            model_name='dialog',
            name='first_question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='dialogs', to='dialog_tree.Question', verbose_name='First question'),
            preserve_default=False,
        ),
    ]
