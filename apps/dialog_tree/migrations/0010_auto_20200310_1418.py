# Generated by Django 3.0.4 on 2020-03-10 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dialog_tree', '0009_auto_20200310_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='next_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='previous_answers', to='dialog_tree.Question', verbose_name='Next question'),
        ),
    ]
