import os
import django
from django.db.models import Q, Count, F
from psycopg2._psycopg import DECIMAL

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Import your models here
from main_app.models import Profile, Product, Order


# Django Queries I
def get_profiles(search_string=None):
    if search_string is None:
        return ""

    query = ((Q(full_name__icontains=search_string)
             | Q(phone_number__icontains=search_string))
             | Q(email__icontains=search_string))

    profiles = (Profile.objects.
                annotate(orders_num=Count('orders')).
                filter(query).order_by('full_name'))

    if not profiles:
        return ''

    return '\n'.join([f"Profile: {p.full_name}, "
                      f"email: {p.email}, "
                      f"phone number: {p.phone_number}, "
                      f"orders: {p.orders_num}" for p in profiles])


def get_loyal_profiles():
    profiles = (Profile.objects.
                annotate(orders_num=Count('orders')).
                filter(orders_num__gt=2).order_by('-orders_num'))

    if not profiles:
        return ''

    return "\n".join([f"Profile: {p.full_name}, orders: {p.orders_num}" for p in profiles])


def get_last_sold_products():
    latest_order = Order.objects.prefetch_related('products').last()

    if not latest_order or not latest_order.products:
        return ""

    return "\n".join([f"Last sold products: "
                      f"{', '.join([p.name for p in latest_order.products.all().order_by('name')])}"])


# Django Queries II
def get_top_products():
    most_sold_products = (Product.objects
                          .annotate(orders_num=Count('orders'))
                          .filter(orders_num__gt=0)
                          .order_by('-orders_num', 'name'))[:5]

    if not most_sold_products:
        return ""

    result = "Top products:\n"
    result += "\n".join([f"{p.name}, sold {p.orders_num} times" for p in most_sold_products])

    return result


def apply_discounts():
    wanted_orders = ((Order.objects
                     .annotate(products_num=Count('products'))
                     .filter(products_num__gt=2, is_completed=False))
                     .update(total_price=F('total_price') * 0.9))

    return f"Discount applied to {wanted_orders} orders."


def complete_order():
    oldest_order = (Order.objects
                    .filter(is_completed=False)
                    .order_by('creation_date').first())

    if oldest_order is None:
        return ''

    oldest_order.is_completed = True
    oldest_order.save()

    for product in oldest_order.products.all():
        product.in_stock -= 1

        if product.in_stock == 0:
            product.is_available = False

        product.save()

    return "Order has been completed!"
