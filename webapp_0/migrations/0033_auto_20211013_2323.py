# Generated by Django 3.1.13 on 2021-10-13 23:23

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webapp_0', '0032_consultas_doc_documentary_galeriadeimagenes5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultas_adv',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='webapp_0.advertising'),
        ),
    ]