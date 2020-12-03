# Generated by Django 3.1 on 2020-11-30 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorVariant',
            fields=[
                ('colorid', models.AutoField(primary_key=True, serialize=False)),
                ('colorname', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QuantityVariant',
            fields=[
                ('quantityid', models.AutoField(primary_key=True, serialize=False)),
                ('quantityname', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SizeVariant',
            fields=[
                ('sizeid', models.AutoField(primary_key=True, serialize=False)),
                ('sizevalue', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('imageid', models.AutoField(primary_key=True, serialize=False)),
                ('productimage', models.ImageField(upload_to='products')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='colortype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.colorvariant'),
        ),
        migrations.AddField(
            model_name='product',
            name='quantitytype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.quantityvariant'),
        ),
        migrations.AddField(
            model_name='product',
            name='sizetype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.sizevariant'),
        ),
    ]