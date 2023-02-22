# Generated by Django 4.1.4 on 2023-02-18 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swapt_Bundle_Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('swapt_bundle_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.swaptlistingmodel')),
            ],
        ),
    ]
