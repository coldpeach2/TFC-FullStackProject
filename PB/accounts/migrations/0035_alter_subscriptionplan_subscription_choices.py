# Generated by Django 4.1 on 2022-12-02 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_alter_subscriptionplan_subscription_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='subscription_choices',
            field=models.CharField(choices=[('Free', 'Free'), ('149.99/year', '149.99/year'), ('14.99/month', '14.99/month')], default='Free', max_length=120),
        ),
    ]
