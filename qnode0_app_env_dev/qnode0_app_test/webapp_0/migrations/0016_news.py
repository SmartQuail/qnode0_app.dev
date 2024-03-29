# Generated by Django 3.1.13 on 2021-10-02 00:57

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('webapp_0', '0015_galeriadeimagenes_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', models.CharField(max_length=250)),
                ('body', wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(icon='doc-full', label='Rich Text')), ('html', wagtail.core.blocks.RawHTMLBlock(icon='site', label='HTML'))])),
                ('main_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
