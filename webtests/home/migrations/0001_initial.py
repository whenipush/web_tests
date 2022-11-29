# Generated by Django 4.1.1 on 2022-11-29 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Вопрос')),
                ('data_published', models.DateField(auto_now_add=True)),
                ('cover', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_active', models.BooleanField(verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200, verbose_name='Ответ')),
                ('votes', models.IntegerField(default=0, verbose_name='Голосов')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.question')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
