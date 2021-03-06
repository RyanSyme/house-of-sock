# Generated by Django 3.1.7 on 2021-05-07 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_auto_20210422_0725'),
        ('products', '0005_auto_20210507_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='wishlist', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='wishlist_products', to='products.product')),
                ('wishlist', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='wishlist_items', to='wishlist.wishlist')),
            ],
        ),
    ]
