# Generated by Django 3.2 on 2022-01-29 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名前')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='説明')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真')),
                ('price', models.IntegerField(default=1000, verbose_name='価格')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
            ],
        ),
        migrations.CreateModel(
            name='line_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='数量')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cart', verbose_name='カートID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='商品ID')),
            ],
        ),
    ]
