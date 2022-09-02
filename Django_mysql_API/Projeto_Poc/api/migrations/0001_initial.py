# Generated by Django 3.2.4 on 2022-09-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProducerItem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('value', models.FloatField()),
            ],
            options={
                'db_table': 'produceritems',
            },
        ),
    ]