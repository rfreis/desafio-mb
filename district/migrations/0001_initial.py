# Generated by Django 3.0.5 on 2020-09-17 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subprefecture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('sub_prefecture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='district', to='subprefecture.SubPrefecture')),
            ],
            options={
                'verbose_name': 'DISTRITO',
                'verbose_name_plural': 'DISTRITOS',
            },
        ),
    ]
