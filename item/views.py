from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewItemForm, EditItemForm
from .models import Item, Category


def item_view(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_item_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item_html/items.html', {'items': items,
                                                    'query': query,
                                                    'categories': categories,
                                                    'category_id': int(category_id)
                                                    })


def detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_item_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item_html/detail.html', {'item': item, 'related_items': related_items})


@login_required
def new_view(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

        return render(request, 'item_html/form.html', {'form': form,
                                                       'title': 'New Item'
                                                       })


@login_required
def edit_view(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

        return render(request, 'item_html/form.html', {'form': form,
                                                       'title': 'Edit Item'
                                                       })


@login_required
def delete_view(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:dashboard_index')
