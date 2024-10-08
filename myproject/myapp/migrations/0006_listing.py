# Generated by Django 5.0.4 on 2024-05-22 05:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_delete_listing'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_type', models.CharField(choices=[('plot', 'Plot'), ('commercial', 'Commercial Space'), ('flat', 'Flat/Villa')], max_length=20)),
                ('project_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('plot_type', models.CharField(blank=True, max_length=255, null=True)),
                ('listing_address', models.CharField(max_length=255)),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_area', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('facing', models.CharField(blank=True, max_length=50, null=True)),
                ('open_side', models.CharField(blank=True, max_length=50, null=True)),
                ('transaction_type', models.CharField(max_length=50)),
                ('possession_status', models.CharField(max_length=50)),
                ('expected_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('price_per_sqft', models.DecimalField(decimal_places=2, max_digits=20)),
                ('amenities', models.JSONField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
