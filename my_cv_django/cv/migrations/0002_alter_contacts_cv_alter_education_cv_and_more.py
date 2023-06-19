# Generated by Django 4.2.2 on 2023-06-19 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='cv.cv'),
        ),
        migrations.AlterField(
            model_name='education',
            name='cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='cv.cv'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='cv.cv'),
        ),
        migrations.AlterField(
            model_name='skil',
            name='cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='cv.cv'),
        ),
    ]
