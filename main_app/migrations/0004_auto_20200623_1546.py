# Generated by Django 3.0.5 on 2020-06-23 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[(1, 'One - Terrible'), (2, 'Two - Ehh'), (3, 'Three - Average'), (4, 'Four - Good'), (5, 'Five - Amazing')], default=(3, 'Three - Average'), max_length=1),
        ),
    ]
