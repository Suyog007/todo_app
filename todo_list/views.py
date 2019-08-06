from django.shortcuts import HttpResponseRedirect, render, redirect
from todo_list.models import TodoItems

def todo(request):
    all_todo_items = TodoItems.objects.all()
    return render(request, 'home.html', {'all_items': all_todo_items})

def add(request):
    new_item = TodoItems(content=request.POST['todo'])
    new_item.save()
    return HttpResponseRedirect('..')

def delete(request,id):
    item_to_delete = TodoItems.objects.get(id=id)
    item_to_delete.delete()
    return redirect('todo')
