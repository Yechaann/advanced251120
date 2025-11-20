from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo
import pdb

# Create your views here.
def index(request):
    print("Oasis Don't look back in anger")
    todos = Todo.onjects.all()
    content  = {'todos': todos}
    #pdb.set_trace()

    return render(request, 'my_to_do_app/index.html', content)

    #return render(request, 'my_to_do_app/index.html')
    #return HttpResponse("My first page")

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content=user_input_str)
    new_todo.save()

    #return HttpResponse('Done' + user_input_str)
    return HttpResponseRedirect(reverse('index'))