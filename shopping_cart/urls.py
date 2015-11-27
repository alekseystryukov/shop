from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^products/(?P<category_id>\d*)/$', 'shopping_cart.views.products', name='products'),
    url(r'^product/(?P<product_id>\d*)$',   'shopping_cart.views.product', name='product'),
    url(r'^cart/$',   'shopping_cart.views.cart', name='cart'),
    url(r'^$', 'shopping_cart.views.home', name='home'),
)
