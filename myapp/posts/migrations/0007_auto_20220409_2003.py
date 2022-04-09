# Generated by Django 2.2.4 on 2022-04-09 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_item_ischecked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='deliveredBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deliveredBy', to='users.ProfileModel'),
        ),
        migrations.AlterField(
            model_name='item',
            name='ordering_organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordering_organization', to='users.ProfileModel'),
        ),
        migrations.AlterField(
            model_name='item',
            name='posting_organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posting_organization', to='users.ProfileModel'),
        ),
    ]
