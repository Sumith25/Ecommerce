# Generated by Django 3.1 on 2020-11-30 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryid', models.AutoField(primary_key=True, serialize=False)),
                ('categoryname', models.SlugField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.AutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='products')),
                ('price', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=500)),
                ('stock', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]
