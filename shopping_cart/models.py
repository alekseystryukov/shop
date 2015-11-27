from django.db import models
from django.utils import timezone


CART_ID = 'CART-ID'


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return unicode(self.name)


class Product(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return unicode(self.name)


class Cart(models.Model):
    created = models.DateTimeField(default=timezone.now)

    @classmethod
    def get(cls, request):
        cart_id = cls.get_cart_id(request)
        if cart_id:
            cart, created = cls.objects.get_or_create(pk=cart_id)
        else:
            cart = cls.objects.create()
            created = True
        if created:
            request.session[CART_ID] = cart.id
        return cart

    @classmethod
    def get_cart_id(cls, request):
        return request.session.get(CART_ID)

    def __init__(self, *args, **kwargs):
        super(Cart, self).__init__(*args, **kwargs)
        self.all_set = None

    def __iter__(self):
        if self.all_set is None:
            self.all_set = self.purchase_set.select_related('product').all()
        for purchase in self.all_set:
            yield purchase

    @property
    def total_cost(self):
        summ = 0
        for purchase in self:
            summ += purchase.total_cost
        return summ


class Purchase(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        return u"Purchase: {} - {} x {}".format(self.product.name, self.product.price, self.quantity)

    @property
    def total_cost(self):
        return self.quantity * self.product.price
