from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "todo_list.html", context)


def add_todo(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_todo")
    form = ItemForm()
    context = {
        "form": form
    }
    return render(request, "add_list.html", context)


def edit_todo(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("get_todo")
    form = ItemForm()
    form = ItemForm(instance=item)
    context = {
        "form": form
    }
    return render(request, "edit_list.html", context)


def toggle_todo(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect("get_todo")


def del_todo(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect("get_todo")
