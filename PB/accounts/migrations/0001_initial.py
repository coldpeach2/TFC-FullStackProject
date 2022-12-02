# Generated by Django 4.1 on 2022-12-02 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=120, null=True)),
                ('last_name', models.CharField(max_length=120, null=True)),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('avatar', models.ImageField(null=True, upload_to='')),
                ('phone_num', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=120)),
                ('lon', models.FloatField(null=True)),
                ('lat', models.FloatField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_choices', models.CharField(choices=[('Free', 'Free'), ('149.99/year', '149.99/year'), ('14.99/month', '14.99/month')], default='Free', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_info', models.IntegerField(null=True)),
                ('_amount_paid', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('active', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(null=True)),
                ('_next_payment', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('subscription_plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.subscriptionplan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_subscription', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('next_payment', models.CharField(max_length=120, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersubscriptions_paymenthistory', to='accounts.usersubscription')),
            ],
        ),
        migrations.AddConstraint(
            model_name='paymenthistory',
            constraint=models.UniqueConstraint(fields=('payment_date', 'amount'), name='together'),
        ),
    ]
