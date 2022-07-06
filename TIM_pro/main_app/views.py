from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from .models import ToDoList,Item
from .forms import CreateNewList
# Create your views here.

def index(response,id):
    ls = ToDoList.objects.get(id = id)
    # itemm = Item.objects.get(id=id)
    # return HttpResponse("<h1>HI THERE! : %s </h1><br></br><h2>%s</h2>"% (ls.name,str(itemm.text)))
    #response.POST  ::  'c1': ['clicked'], 'c5': ['clicked'], 'c6': ['clicked'], 'save': ['submit'], 'newItemName': ['call Mr.Tim']}
    if ls in response.user.todolist.all():
        if response.method =="POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id)) == "clicked":
                        # print("c"+str(item.id))
                        # print(response.POST.get("c"+str(item.id)))
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif response.POST.get("AddNewItem"):
                txt = response.POST.get("newItemName")
                if len(txt) > 2:
                    ls.item_set.create(text = txt , complete = False)
                else:
                    print("Please enter more than 2 text charc")


        return render(response,'list.html',{"ls":ls})
    else:
        return render(response,'list_view.html',{})

def home(reponse):
    return render(reponse,"home.html")

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n)
            t.save()
            response.user.todolist.add(t)
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()

    return render(response,"create.html",{"form":form})

def list_view(response):
    return render(response,"list_view.html",{})

