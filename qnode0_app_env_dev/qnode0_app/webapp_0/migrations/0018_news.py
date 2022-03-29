# Generated by Django 3.1.13 on 2021-10-02 04:05

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('webapp_0', '0017_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('intro', models.CharField(max_length=250)),
                ('body', wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(icon='doc-full', label='Rich Text')), ('html', wagtail.core.blocks.RawHTMLBlock(icon='site', label='HTML'))])),
                ('main_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='webapp_0.index')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]