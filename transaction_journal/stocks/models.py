from django.db import models
import uuid


class Stock(models.Model):

    stock_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    currensy_id = models.ForeignKey('Currency', on_delete=models.SET_NULL, null=True)
    stock_name = models.CharField(max_length=255)
    purchase_price = models.IntegerField()
    amount = models.IntegerField()
    day_of_purchase = models.DateField()
    cost = models.IntegerField()
    broker_fee = models.IntegerField()
    asset_portfolio_id = models.IntegerField()

    etf_id = models.ForeignKey('ETF', blank=True, null=True, on_delete=models.SET_NULL)
    share_is = models.ForeignKey('Share', blank=True, null=True, on_delete=models.SET_NULL)
    bond_id = models.ForeignKey('Bond', blank=True, null=True, on_delete=models.SET_NULL)
    target_for_date_id = models.ForeignKey('TargetForDate', blank=True, null=True, on_delete=models.SET_NULL)
    price_target_id = models.ForeignKey('PriceTarget', blank=True, null=True, on_delete=models.SET_NULL)


class ETF(models.Model):
    etf_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    etf_code = models.CharField(max_length=255)


class Share(models.Model):
    share_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    share_code = models.CharField(max_length=255)


class Bond(models.Model):
    bond_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    bond_code = models.CharField(max_length=255)
    coupon_percent = models.IntegerField()
    coupon_price = models.IntegerField()
    yield_to_maturity = models.IntegerField()


class TargetForDate(models.Model):
    target_for_date_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    description = models.CharField(max_length=1063)
    target_date = models.DateField()


class PriceTarget(models.Model):
    price_target_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    description = models.CharField(max_length=1063)
    target_price = models.IntegerField()


class Currency(models.Model):
    currency_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    currensy_name = models.CharField(max_length=60)

    def __str__(self):
        return self.currensy_name
