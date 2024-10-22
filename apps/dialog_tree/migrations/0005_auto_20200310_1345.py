# Generated by Django 3.0.4 on 2020-03-10 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dialog_tree', '0004_auto_20200310_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'db_table': 'answers',
            },
        ),
        migrations.AlterField(
            model_name='dialog',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='Finished'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('answers', models.ManyToManyField(related_name='questions', to='dialog_tree.Answer', verbose_name='Answers')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'db_table': 'questions',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='next',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='previous_answers', to='dialog_tree.Question', verbose_name='Next question'),
        ),
        migrations.AddField(
            model_name='dialog',
            name='first_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dialogs', to='dialog_tree.Question', verbose_name='First question'),
        ),
    ]
