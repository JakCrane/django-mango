from django.shortcuts import render
from .models import Item
# Create your views here.


def get_todo(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "todo_list.html", context)
