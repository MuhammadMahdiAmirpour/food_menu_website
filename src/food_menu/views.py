# from django.shortcuts import redirect
# from django.shortcuts import render
# from django.http import HttpResponse
from .models import Item
# from django.template import loader
# from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

# Create your views here.

# def index(request):
#     item_list = Item.objects.all()
# #     template = loader.get_template('food_menu/index.html')
#     context = {
#             'item_list': item_list,
#             }
# #    return HttpResponse(template.render(context, request))
#     return render(request, 'food_menu/index.html', context)

class IndexClassView(ListView):
    model = Item
    template_name = 'food_menu/index.html'
    context_object_name = 'item_list'

# def item(request):
#     return HttpResponse('<h1>This is an item view</h1>')

class FoodDetail(DetailView):
    model = Item
    template_name = 'food_menu/detail.html'

# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
# #    template = loader.get_template('food_menu/detail.html')
#     context = {
#             'item': item,
#             }
# #    return HttpResponse(template.render(context, request))
#     return render(request, 'food_menu/detail.html', context)

class EditItem(UpdateView):
    model = Item
    fields = [
            'item_name',
            'item_description',
            'item_price',
            'item_image',
            ]
    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


# def edit_item(request, id):
#     item = Item.objects.get(id=id)
#     form = ItemForm(request.POST or None, instance = item)
#     if form.is_valid():
#         form.save()
#         return redirect('food_menu:index')
#     return render(request, 'food_menu/item_form.html', {'form':form, 'item': item})

# This is a class based view for creating item
class CreateItem(CreateView):
    model = Item
    fields = [
            'item_name',
            'item_description',
            'item_price',
            'item_image',
            ]
    template_name='food_menu/item_form.html'
    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

# def create_item(request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('food_menu:index')
#     return render(request, 'food_menu/item_form.html',{'form':form})

class DeleteItem(DeleteView):
    model = Item
    success_url = 'food_menu:index'
    template_name = 'food_menu/item_delete.html'

# def delete_item(request, item_id):
#     item = Item.objects.get(id=item_id)
#     if request.method == 'POST':
#         item.delete()
#         return redirect('food_menu:index')
#     return render(request, 'food_menu/item_delete.html', {'item': item})


