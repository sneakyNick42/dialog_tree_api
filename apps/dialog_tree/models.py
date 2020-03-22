"""`dialog_tree` app models."""
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from apps.dialog_tree.managers import DialogQuerySet


class Dialog(models.Model):
    """Dialog model."""

    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='dialogs',
                              verbose_name='User')
    slug = models.SlugField(default='', editable=False, max_length=255, unique=True)
    name = models.CharField(max_length=255, verbose_name='Dialog name')
    description = models.TextField(verbose_name='Dialog description', default='', blank='')
    finished = models.BooleanField(verbose_name='Finished', default=False)
    first_question = models.ForeignKey('Question',
                                       on_delete=models.PROTECT,
                                       verbose_name='First question',
                                       related_name='dialogs',
                                       null=True,
                                       blank=True)

    objects = DialogQuerySet.as_manager()

    class Meta:
        verbose_name = 'Dialog'
        verbose_name_plural = 'Dialogs'
        db_table = 'dialogs'

    def __str__(self):
        """String model representation."""
        return self.name

    def save(self, *args, **kwargs):
        """Creating slug before saving."""
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Question(models.Model):
    """Question model."""

    text = models.TextField(verbose_name='Text')

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        db_table = 'questions'

    def __str__(self):
        """String model representation."""
        return self.text


class Answer(models.Model):
    """Answer model."""

    text = models.TextField(verbose_name='Text')
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 verbose_name='Question',
                                 related_name='answers')
    next_question = models.ForeignKey(Question,
                                      on_delete=models.CASCADE,
                                      verbose_name='Next question',
                                      related_name='previous_answers',
                                      null=True,
                                      blank=True)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        db_table = 'answers'

    def __str__(self):
        """String model representation."""
        return self.text
