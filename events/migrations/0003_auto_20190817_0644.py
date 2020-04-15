# Generated by Django 2.2.2 on 2019-08-17 06:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_auto_20190807_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('url', models.URLField(null=True)),
                ('show', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='eventregister',
            unique_together={('user', 'event')},
        ),
    ]
