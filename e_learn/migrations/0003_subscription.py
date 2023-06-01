# Generated by Django 4.2.1 on 2023-06-01 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_learn', '0002_userinstitutionrelation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('currency', models.CharField(choices=[('CAD', 'CANADA'), ('USD', 'AMERICA')], default='CAD', max_length=3)),
                ('is_basic', models.BooleanField(default=False)),
                ('is_premium', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]