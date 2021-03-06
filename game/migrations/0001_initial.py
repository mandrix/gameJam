# Generated by Django 3.1 on 2020-10-11 07:21

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
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='game/')),
                ('rarity', models.CharField(choices=[('LGN', 'legend'), ('BS', 'basic')], default='BS', max_length=3)),
                ('background', models.CharField(choices=[('blue', 'src'), ('green', 'src')], default='blue', max_length=5)),
                ('label', models.CharField(choices=[('UB', 'Ubicación'), ('HR', 'Heroe')], default='a', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Efect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cards', models.ManyToManyField(blank=True, to='game.Card')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='deck', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
