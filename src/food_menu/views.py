from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm

# Create your views here.

def index(request):
    item_list = Item.objects.all()
#     template = loader.get_template('food_menu/index.html')
    context = {
            'item_list': item_list,
            }
#    return HttpResponse(template.render(context, request))
    return render(request, 'food_menu/index.html', context)

# def item(request):
#     return HttpResponse('<h1>This is an item view</h1>')


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
#    template = loader.get_template('food_menu/detail.html')
    context = {
            'item': item,
            }
#    return HttpResponse(template.render(context, request))
    return render(request, 'food_menu/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food_menu:index')
    return render(request, 'food_menu/item_form.html',{'form':form})

def edit_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance = item)
    if form.is_valid():
        form.save()
        return redirect('food_menu:index')
    return render(request, 'food_menu/item_form.html', {'form':form, 'item': item})

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food_menu:index')
    return render(request, 'food_menu/item_delete.html', {'item': item})

