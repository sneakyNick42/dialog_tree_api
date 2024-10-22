# Generated by Django 3.0.4 on 2020-03-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dialog_tree', '0005_auto_20200310_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialog',
            name='first_question',
        ),
        migrations.AddField(
            model_name='answer',
            name='end',
            field=models.BooleanField(default=False, verbose_name='End'),
        ),
        migrations.AddField(
            model_name='dialog',
            name='questions',
            field=models.ManyToManyField(related_name='dialogs', to='dialog_tree.Question', verbose_name='Questions'),
        ),
    ]
