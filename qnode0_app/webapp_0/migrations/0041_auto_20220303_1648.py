# Generated by Django 3.1.14 on 2022-03-03 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp_0', '0040_auto_20220302_0654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertising',
            name='consulta',
        ),
        migrations.RemoveField(
            model_name='advertising',
            name='from_address',
        ),
        migrations.RemoveField(
            model_name='advertising',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='advertising',
            name='thank_you_text',
        ),
        migrations.RemoveField(
            model_name='advertising',
            name='to_address',
        ),
        migrations.RemoveField(
            model_name='index',
            name='cliente_Navbar',
        ),
        migrations.DeleteModel(
            name='consultas_Adv',
        ),
    ]
