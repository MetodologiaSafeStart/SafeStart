# Generated by Django 3.0.6 on 2020-07-02 23:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0005_auto_20200630_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='foto_proyecto',
            field=models.ImageField(blank=True, help_text='Elije una foto', null=True, upload_to='media_root/proyectos/'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='foto_proyecto2',
            field=models.ImageField(blank=True, help_text='Elije una foto', null=True, upload_to='media_root/proyectos/'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(blank=True, help_text='Elije una foto', null=True, upload_to='media_root/perfiles/'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
