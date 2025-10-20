# accounts/signals.py
from django.contrib.auth.signals import user_logged_in

@receiver(user_logged_in)
def merge_cart(sender, request, user, **kwargs):
    session_cart = request.session.get('cart', {})
    db_cart, _ = Cart.objects.get_or_create(user=user)
    for product_id, qty in session_cart.items():
        item, created = db_cart.items.get_or_create(product_id=product_id)
        if not created:
            item.quantity += qty
        else:
            item.quantity = qty
        item.save()
    request.session['cart'] = {}



