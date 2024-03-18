from django.db import models

from django.contrib.auth.models import User

from django.contrib.auth.models import Group

# Проверяем существование группы 'mmorpgusers', и создаем ее, если она не существует
group, created = Group.objects.get_or_create(name='mmorpgusers')

class MmoRPGAdv(models.Model):
    CATEGORY = [
        ('Tanks', 'Танки'),
        ('Healers', 'Хилы'),
        ('DDs', 'ДД'),
        ('Traders', 'Торговцы'),
        ('GildMasters', 'Гилдмастеры'),
        ('QuestGivers', 'Квестгиверы'),
        ('Smiths', 'Кузнецы'),
        ('Tanners', 'Кожевники'),
        ('Potions', 'Зельевары'),
        ('SpellMasters', 'Мастера заклинаний')
    ]

    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_category = models.CharField(max_length=12, choices=CATEGORY, default='Tanks')
    text = models.TextField()
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        string = self.text[0:20]
        if len(self.text) > len(string):
            string += "..."
        return string


class Response(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_advert = models.ForeignKey(MmoRPGAdv, on_delete=models.CASCADE)
    text = models.TextField()
    accepted = models.BooleanField(default=False)
