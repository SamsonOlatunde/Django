from django.shortcuts import render


def note_home(request):
    return render(request, 'note/note.html', {})


