# Generated by Django 2.1.7 on 2019-02-22 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20190217_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
            options={
                'db_table': 'ArticleStatistic',
            },
        ),
    ]