from django.db import models


class DialogQuerySet(models.QuerySet):
    def finished(self):
        return self.filter(finished=True)
