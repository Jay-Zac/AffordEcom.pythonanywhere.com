from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item
from item.models import Category


@login_required
def dashboard_index_view(request):
    categories = Category.objects.all()
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard_html/dashboard_index.html', {'items': items,
                                                                   'categories': categories, })
