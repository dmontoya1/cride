# Generated by Django 3.2.8 on 2021-10-30 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('name', models.CharField(max_length=255, verbose_name='circle name')),
                ('slug_name', models.SlugField(max_length=40)),
                ('about', models.CharField(max_length=255, verbose_name='Circle description')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='circle/pictures/')),
                ('rides_offered', models.IntegerField(default=0)),
                ('rides_taken', models.IntegerField(default=0)),
                ('verified', models.BooleanField(default=False, help_text='Verified circle are also know as official communities', verbose_name='Verified circle')),
                ('is_public', models.BooleanField(default=True, help_text='Public circles are listed in the main page so every know about their existence')),
                ('is_limited', models.BooleanField(default=False, help_text='Limited circle can grown up to a fixed number of members', verbose_name='limited')),
                ('members_limited', models.PositiveIntegerField(default=0, help_text='If circle is limited, this will be the limit on the number of members')),
            ],
            options={
                'ordering': ['-rides_taken', '-rides_offered'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]