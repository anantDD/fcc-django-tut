from django.shortcuts import render

from .forms import ProductForm, RawProductForm
from .models import Product


def product_list_view(request):
    object_list = Product.objects.all()
    context = {
        'object_list': object_list
    }
    return render(request, "products/product_list.html", context)


def dynamic_lookup_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()  # rerendering the form after success

    context = {
        'form': form
    }

    return render(request, "products/product_create.html", context)


def render_initial_data(request):
    initial_data = {
        'title': "inital title"
    }
    print(request.POST)
    obj = Product.objects.get(id=7)
    form = ProductForm(request.POST or None,
                       initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }

    return render(request, 'products/product_create.html', context)


# MAKING OUR OWN FORM AND DEALING WITH DATA
# def product_create_view(request):
#     # print(request.GET, 'get')
#     # print(request.POST)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Product.objects.create(title=my_new_title)
#     context = {}

#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_from.errors)
#     context = {
#         "form": my_form
#     }

#     return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
