# Generated by Django 4.2.8 on 2024-03-15 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MmoRPGAdv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_category', models.CharField(choices=[('Tanks', 'Танки'), ('Healers', 'Хилы'), ('DDs', 'ДД'), ('Traders', 'Торговцы'), ('GildMasters', 'Гилдмастеры'), ('QuestGivers', 'Квестгиверы'), ('Smiths', 'Кузнецы'), ('Tanners', 'Кожевники'), ('Potions', 'Зельевары'), ('SpellMasters', 'Мастера заклинаний')], default='Tanks', max_length=12)),
                ('text', models.TextField()),
                ('file', models.FileField(upload_to='uploads/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
                ('id_advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmorpgbb.mmorpgadv')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
