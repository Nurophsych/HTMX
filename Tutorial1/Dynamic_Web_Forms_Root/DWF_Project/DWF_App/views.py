from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .forms import EntryForm
from .models import Entry

def entry_list(request):
    entries = Entry.objects.all().order_by('-created_at')
    form = EntryForm()
    return render(request, 'entries/entry_list.html', {
        'entries': entries,
        'form': form
    })

def add_entry(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry added successfully!')
            entries = Entry.objects.all().order_by('-created_at')

            if request.headers.get('HX-Request'):  # Check for HTMX request
                return render(request, 'entries/entries_list_partial.html', {
                    'entries': entries
                })
            return redirect('entry_list')
        else:
            messages.error(request, 'Please correct the errors below.')
            if request.headers.get('HX-Request'):
                return render(request, 'entries/entry_list.html', {
                    'entries': Entry.objects.all().order_by('-created_at'),
                    'form': form
                })
    return redirect('entry_list')


def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry updated successfully!')
            entries = Entry.objects.all().order_by('-created_at')
            return render(request, 'entries/entries_list_partial.html', {
                'entries': entries
            })
    else:
        form = EntryForm(instance=entry)

    return render(request, 'entries/edit_entry_partial.html', {
        'form': form,
        'entry': entry
    })

    
# DELETE ENTRY
def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    entry.delete()
    messages.success(request, 'Entry deleted successfully!')
    
    entries = Entry.objects.all().order_by('-created_at')
    return render(request, 'entries/entries_list_partial.html', {
        'entries': entries
    })