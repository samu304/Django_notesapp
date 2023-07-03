from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.contrib import messages

# Create your views here.
def index(request):
    notes = Note.objects.all()
    return render(request, 'index.html', {'notes':notes})


def new_note(request):
    form = NoteForm()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request,'update.html', {'form':form})

def update_note(request,id):
    note = Note.objects.get(id=id)
    form = NoteForm(instance=note)
    if request.method == "POST":
        form = NoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'update.html',{'form':form})

def delete_note(request,id):
    note = Note.objects.get(id=id)
    form = NoteForm(instance=note)
    if request.method=="POST":
        note.delete()
        messages.info(request, "Notes has been deleted successfully!")

    return render(request,'delete.html',{'form':form})
    

def search_note(request):
    if request.method == "POST":
        search_value = request.POST['search']
        notes = Note.objects.filter(title__icontains = search_value) | Note.objects.filter(text__icontains = search_value)
        return render(request, 'search.html',{'notes':notes})
    return redirect('index')