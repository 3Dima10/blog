from django.db import models


class Aweitr(models.Model):
    title = models.CharField(
        "Тема",
        max_length=50,
    )
    anons = models.CharField(
        "Анонс",
        max_length=250,
    )

    text = models.TextField("Текст")
    data = models.DateTimeField("Дата")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
