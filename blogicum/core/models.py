from django.db import models


class PublishedCreatedModel(models.Model):
    """Абстрактная модель. Добавляет флаг is_published."""
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано',
                                       help_text='Снимите галочку, чтобы '
                                       'скрыть публикацию.')
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        abstract = True
