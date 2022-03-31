# Generated by Django 3.1.13 on 2021-10-13 22:59

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('webapp_0', '0029_auto_20211013_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landscape',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, verbose_name='to address')),
                ('from_address', models.CharField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('Ad_info1', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-1 info')),
                ('Ad_date1', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-1')),
                ('Ad_info2', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-2 info')),
                ('Ad_date2', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-2')),
                ('Ad_info3', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-3 info')),
                ('Ad_date3', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-3')),
                ('Ad_info4', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-4 info')),
                ('Ad_date4', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-4')),
                ('Ad_info5', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-5 info')),
                ('Ad_date5', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-5')),
                ('Ad_info6', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-6 info')),
                ('Ad_date6', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-6')),
                ('Ad_info7', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-7 info')),
                ('Ad_date7', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-7')),
                ('Ad_info8', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-8 info')),
                ('Ad_date8', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-8')),
                ('Ad_info9', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-9 info')),
                ('Ad_date9', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-9')),
                ('Ad_info10', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-10 info')),
                ('Ad_date10', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-10')),
                ('Ad_info11', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-11 info')),
                ('Ad_date11', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-11')),
                ('Ad_info12', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-12 info')),
                ('Ad_date12', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-12')),
                ('Ad_info13', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-13 info')),
                ('Ad_date13', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-13')),
                ('Ad_info14', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-14 info')),
                ('Ad_date14', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-14')),
                ('Ad_info15', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-15 info')),
                ('Ad_date15', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-15')),
                ('Ad_info16', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-16 info')),
                ('Ad_date16', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-16')),
                ('Ad_info17', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-17 info')),
                ('Ad_date17', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-17')),
                ('Ad_info18', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-18 info')),
                ('Ad_date18', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-18')),
                ('Ad_info19', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-19 info')),
                ('Ad_date19', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-19')),
                ('Ad_info20', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-20 info')),
                ('Ad_date20', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-20')),
                ('Ad_info21', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-21 info')),
                ('Ad_date21', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-21')),
                ('Ad_info22', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-22 info')),
                ('Ad_date22', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-22')),
                ('Ad_info23', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-23 info')),
                ('Ad_date23', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-23')),
                ('Ad_info24', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-24 info')),
                ('Ad_date24', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-24')),
                ('Ad_info25', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-25 info')),
                ('Ad_date25', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-25')),
                ('Ad_info26', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-26 info')),
                ('Ad_date26', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-26')),
                ('Ad_info27', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-27 info')),
                ('Ad_date27', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-27')),
                ('Ad_info28', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-28 info')),
                ('Ad_date28', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-28')),
                ('Ad_info29', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-29 info')),
                ('Ad_date29', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-29')),
                ('Ad_info30', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-30 info')),
                ('Ad_date30', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-30')),
                ('Ad_info31', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-31 info')),
                ('Ad_date31', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-31')),
                ('Ad_info32', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-32 info')),
                ('Ad_date32', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-32')),
                ('Ad_info33', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-33 info')),
                ('Ad_date33', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-33')),
                ('Ad_info34', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-34 info')),
                ('Ad_date34', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-34')),
                ('Ad_info35', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-35 info')),
                ('Ad_date35', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-35')),
                ('Ad_info36', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-36 info')),
                ('Ad_date36', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-36')),
                ('Ad_info37', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-37 info')),
                ('Ad_date37', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-37')),
                ('Ad_info38', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-38 info')),
                ('Ad_date38', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-38')),
                ('Ad_info39', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-39 info')),
                ('Ad_date39', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-39')),
                ('Ad_info40', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-40 info')),
                ('Ad_date40', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-40')),
                ('Ad_info41', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-41 info')),
                ('Ad_date41', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-41')),
                ('Ad_info42', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-42 info')),
                ('Ad_date42', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-42')),
                ('Ad_info43', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-43 info')),
                ('Ad_date43', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-43')),
                ('Ad_info44', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-44 info')),
                ('Ad_date44', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-44')),
                ('Ad_info45', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-45 info')),
                ('Ad_date45', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-45')),
                ('Ad_info46', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-46 info')),
                ('Ad_date46', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-46')),
                ('Ad_info47', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-47 info')),
                ('Ad_date47', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-47')),
                ('Ad_info48', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-48 info')),
                ('Ad_date48', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-48')),
                ('Ad_info49', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-49 info')),
                ('Ad_date49', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-49')),
                ('Ad_info50', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-50 info')),
                ('Ad_date50', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-50')),
                ('Ad_info51', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-51 info')),
                ('Ad_date51', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-51')),
                ('Ad_info52', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-52 info')),
                ('Ad_date52', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-52')),
                ('Ad_info53', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-53 info')),
                ('Ad_date53', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-53')),
                ('Ad_info54', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-54 info')),
                ('Ad_date54', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-54')),
                ('Ad_info55', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-55 info')),
                ('Ad_date55', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-55')),
                ('Ad_info56', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-56 info')),
                ('Ad_date56', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-56')),
                ('Ad_info57', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-57 info')),
                ('Ad_date57', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-57')),
                ('Ad_info58', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-58 info')),
                ('Ad_date58', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-58')),
                ('Ad_info59', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-59 info')),
                ('Ad_date59', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-59')),
                ('Ad_info60', models.CharField(blank=True, max_length=150, null=True, verbose_name='Advertising-60 info')),
                ('Ad_date60', models.DateField(blank=True, null=True, verbose_name='Fecha de Advertising-60')),
                ('consulta', wagtail.core.fields.RichTextField(blank=True, verbose_name='Mensaje para que nos consulten por el formulario')),
                ('thank_you_text', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GaleriadeImagenes4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 1')),
                ('image_10', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 10')),
                ('image_11', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 11')),
                ('image_12', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 12 ')),
                ('image_13', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 13')),
                ('image_14', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 14')),
                ('image_15', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 15')),
                ('image_16', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 16')),
                ('image_17', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 17')),
                ('image_18', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 18')),
                ('image_19', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 19')),
                ('image_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 2')),
                ('image_20', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 20')),
                ('image_21', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 21')),
                ('image_22', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 22')),
                ('image_23', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 23')),
                ('image_24', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 24')),
                ('image_25', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 25')),
                ('image_26', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 26')),
                ('image_27', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 27')),
                ('image_28', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 28')),
                ('image_29', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 29')),
                ('image_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 3')),
                ('image_30', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 30')),
                ('image_31', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 31')),
                ('image_32', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 32')),
                ('image_33', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 33')),
                ('image_34', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 34')),
                ('image_35', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 35')),
                ('image_36', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 36')),
                ('image_37', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 37')),
                ('image_38', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 38')),
                ('image_39', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 39')),
                ('image_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 4')),
                ('image_40', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 40')),
                ('image_41', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 41')),
                ('image_42', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 42 ')),
                ('image_43', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 43')),
                ('image_44', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 44')),
                ('image_45', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 45')),
                ('image_46', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 46')),
                ('image_47', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 47')),
                ('image_48', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 48')),
                ('image_49', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 49')),
                ('image_5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 5')),
                ('image_50', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 50')),
                ('image_51', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 51')),
                ('image_52', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 52')),
                ('image_53', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 53')),
                ('image_54', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 54')),
                ('image_55', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 55')),
                ('image_56', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 56')),
                ('image_57', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 57')),
                ('image_58', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 58')),
                ('image_59', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 59')),
                ('image_6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 6')),
                ('image_60', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 60')),
                ('image_7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 7')),
                ('image_8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 8')),
                ('image_9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Foto 9')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Logotipo de Juan Silva Photo')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleria_4', to='webapp_0.landscape')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='consultas_Land_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.CharField(blank=True, help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields_Land_2', to='webapp_0.landscape')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
