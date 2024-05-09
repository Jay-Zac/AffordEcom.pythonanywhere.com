from django.shortcuts import render, redirect, get_object_or_404
from item.models import Category, Item
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Q


def index_view(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_item_sold=False)[::-2]
    categories = Category.objects.all()

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'core_html/index.html', {'categories': categories,
                                                    'items': items,
                                                    'query': query,
                                                    })


def contact_view(request):
    return render(request, 'core_html/contact.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "successfully signed in!")

            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'core_html/signup.html', {'form': form})


def logout_user_view(request):
    logout(request)
    messages.success(request, "You were logged out!")
    return redirect('index')


def detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_item_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'core_html/detail.html', {'item': item, 'related+items': related_items})


def about_view(request):
    return render(request, 'core_html/about.html')
