# Generated by Django 3.1.7 on 2021-04-07 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlisting_bid_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='auction',
            field=models.ManyToManyField(related_name='bid', to='auctions.AuctionListing'),
        ),
    ]
