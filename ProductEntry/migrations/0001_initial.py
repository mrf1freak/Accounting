# Generated by Django 3.1.7 on 2022-03-18 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Party', '0001_initial'),
        ('Account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=120)),
                ('type', models.CharField(choices=[('Sale', 'Sale'), ('Purchase', 'Purchase')], max_length=40)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.account')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Party.party')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EntryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductEntry.productentry')),
                ('packing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Product.packing')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Product.product')),
            ],
        ),
    ]
