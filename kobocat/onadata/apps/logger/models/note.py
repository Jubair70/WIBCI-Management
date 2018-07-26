from django.db import models
from .instance import Instance


class Note(models.Model):
    note = models.TextField()
    user_id = models.CharField(max_length=200, null=True, default='', blank=True)
    instance = models.ForeignKey(Instance, related_name='notes')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'logger'
        permissions = (
            ('view_note', 'View note'),
        )
