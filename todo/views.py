from django.shortcuts import render
from .models import Item
# Create your views here.


def get_todo(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "todo_list.html", context)


def add_todo(request):
    if request.method == "POST":
        name = request.POST.get("item_name")
        done = "done" in request.POST
        Item.objects.create(name=name, done=done)
        return redirect("get_todo")
    return render(request, "add_list.html")
