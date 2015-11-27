from models import Cart, Purchase


def cart_count(request):
    cart_id = Cart.get_cart_id(request)
    return {'cart_count': Purchase.objects.filter(cart_id=cart_id).count() if cart_id else 0}
