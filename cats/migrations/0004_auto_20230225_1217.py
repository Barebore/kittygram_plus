# Generated by Django 3.2 on 2023-02-25 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_auto_20230222_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(choices=[('Gray', 'Серый'), ('Black', 'Чёрный'), ('White', 'Белый'), ('Ginger', 'Рыжий'), ('Mixed', 'Смешанный')], max_length=16),
        ),
        migrations.AlterField(
            model_name='cat',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cats', to='cats.owner'),
        ),
    ]
