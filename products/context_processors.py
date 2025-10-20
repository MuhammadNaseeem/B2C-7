# products/context_processors.py
from .models import Category

def categories(request):
    """
    Returns all product categories for use in templates.
    Example usage: {% for category in categories %} ... {% endfor %}
    """
    return {
        'categories': Category.objects.all().order_by('name')  # Optional: order alphabetically
    }



