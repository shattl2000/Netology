

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCustomerCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='customer.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='customer.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='customer.ProductCustomer', to='shop.Product'),
        ),
        migrations.AddField(
            model_name='customer',
            name='products_in_cart',
            field=models.ManyToManyField(blank=True, related_name='customers', through='customer.ProductCustomerCart', to='shop.Product'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
    ]
