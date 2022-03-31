# Generated by Django 3.1.13 on 2021-10-13 22:53

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailmenus', '0023_remove_use_specific'),
        ('webapp_0', '0027_auto_20211013_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='consultas_Prod',
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
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Productos',
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
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_10',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_11',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_12',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_13',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_14',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_15',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_16',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_17',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_18',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_19',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_20',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_21',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_22',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_23',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_24',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_25',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_26',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_27',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_28',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_29',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_30',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_31',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_32',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_33',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_34',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_35',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_36',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_37',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_38',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_39',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_40',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_41',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_42',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_43',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_44',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_45',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_46',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_47',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_48',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_49',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_5',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_50',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_51',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_52',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_53',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_54',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_55',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_56',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_57',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_58',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_59',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_6',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_60',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_7',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_8',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='image_9',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes4',
            name='page',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_10',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_11',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_12',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_13',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_14',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_15',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_16',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_17',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_18',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_19',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_20',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_21',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_22',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_23',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_24',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_25',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_26',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_27',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_28',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_29',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_30',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_31',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_32',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_33',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_34',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_35',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_36',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_37',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_38',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_39',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_40',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_41',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_42',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_43',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_44',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_45',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_46',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_47',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_48',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_49',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_5',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_50',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_51',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_52',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_53',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_54',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_55',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_56',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_57',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_58',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_59',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_6',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_60',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_7',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_8',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='image_9',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='galeriadeimagenes5',
            name='page',
        ),
        migrations.RemoveField(
            model_name='landscape',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='product',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='Documentary',
        ),
        migrations.DeleteModel(
            name='GaleriadeImagenes4',
        ),
        migrations.DeleteModel(
            name='GaleriadeImagenes5',
        ),
        migrations.DeleteModel(
            name='Landscape',
        ),
        migrations.AddField(
            model_name='consultas_prod',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields_Prod', to='webapp_0.productos'),
        ),
        migrations.AlterField(
            model_name='galeriadeimagenes3',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleria_3', to='webapp_0.productos'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
