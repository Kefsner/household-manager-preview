# Generated by Django 5.0.6 on 2024-06-07 23:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_initial'),
        ('core', '0001_initial'),
        ('creditcard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='db',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.db'),
        ),
        migrations.AddField(
            model_name='creditcardinstallment',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='creditcardinstallment',
            name='db',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.db'),
        ),
        migrations.AddField(
            model_name='creditcardtransaction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categories.category'),
        ),
        migrations.AddField(
            model_name='creditcardtransaction',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='creditcardtransaction',
            name='credit_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='creditcard.creditcard'),
        ),
        migrations.AddField(
            model_name='creditcardtransaction',
            name='db',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.db'),
        ),
        migrations.AddField(
            model_name='creditcardtransaction',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.subcategory'),
        ),
        migrations.AddField(
            model_name='creditcardinstallment',
            name='credit_card_transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transaction_installments', to='creditcard.creditcardtransaction'),
        ),
    ]
