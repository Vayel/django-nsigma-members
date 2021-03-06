from django.db import models

from smart_selects.db_fields import ChainedManyToManyField


class Registration(models.Model):
    member = models.ForeignKey(
        'Member',
        on_delete=models.CASCADE,
        related_name='registrations',
    )
    date = models.DateField()
    foreigner = models.BooleanField(default=False,)
    documents = ChainedManyToManyField(
        'RegistrationDocument',
        related_name='registrations',
        chained_field='member',
        chained_model_field='member',
    )
    validated = models.BooleanField(default=False,)

    def __str__(self):
        return '{0} - {1}'.format(self.member, self.date)
