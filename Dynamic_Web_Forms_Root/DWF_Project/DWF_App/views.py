# views.py
from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

def entry_list(request):
    entries = Entry.objects.all()
    return render(request, 'entries/entry_list.html', {'entries': entries})

def add_entry(request):
    if request.method == "POST":
        # Get the form data from the request
        name = request.POST.get('name')
        information = request.POST.get('information')
        
        # Create a new entry and save it to the database
        entry = Entry.objects.create(name=name, information=information)
        
        # After creating the entry, return the updated list of entries to replace the current content
        entries = Entry.objects.all()
        return render(request, 'entries/entry_list.html', {'entries': entries})
    
    # If it's a GET request, just render the entry list
    return redirect('entry_list')
