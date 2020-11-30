from django.shortcuts import render
from .models import Category, Year, Subject, Paper, Notes_file, Video_url
from .forms import PaperForm, NotesForm, VideoForm

from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def course_list(request):
    categories = Category.objects.all()
    return render(request, 'college/course_list.html', {'categories' : categories})

def year_list(request, category_id):
    degree = Category.objects.get(id=category_id)
    years = Year.objects.filter(degree=degree)
    return render(request, 'college/year_list.html', {'years' : years})

def subject_list(request, year_id):
    year = Year.objects.get(id=year_id)
    subjects = Subject.objects.filter(year=year)
    return render(request, 'college/subject_list.html', {'subjects' : subjects})

def paper_list(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    papers = Paper.objects.filter(subject=subject)
    return render(request, 'college/paper_list.html', {'papers' : papers})

def notes_list(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    notes = Notes_file.objects.filter(subject=subject)
    return render(request, 'college/notes_list.html', {'notes' : notes})

def video_list(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    videos = Video_url.objects.filter(subject=subject)
    return render(request, 'college/video_list.html', {'videos' : videos})
    
def subject_detail(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    context = {
        'subject': subject
    }
    return render(request, 'college/subject_detail.html', context)

def paper_create_view(request):
    if request.method == 'POST':
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PaperForm()
    context = {
        'form': form
    }
    return render(request, 'college/paper_create.html', context)

def notes_create_view(request):
    if request.method == 'POST':
        form_notes = NotesForm(request.POST or None)
        if form_notes.is_valid():
            form_notes.save()
    elif request.method == 'GET':
        form_notes = NotesForm()
        
    context = {
        'form_notes': form_notes
    }
    return render(request, 'college/notes_create.html', context)

def video_create_view(request):
    form_video = VideoForm(request.POST or None)
    if request.method == 'POST':
        if form_video.is_valid():
            form_video.save()
            
    context = {
        'form_video': form_video
    }
    return render(request, 'college/video_create.html', context)

def paper_list_view(request):
    paperlist = Paper.objects.all()
    return render(request, 'college/paper_list_view.html', {'paperlist' : paperlist})

def paper_approved_view(request, paper_id):
    paper = Paper.objects.get(id=paper_id)
    if 'accept' in request.POST:
        paper.approved = True
        paper.save()
        message = "paper accepted!"
    else:
        paper.delete()
        message = "paper deleted!"

    context = {
        'message': message
    }
    return render(request, 'college/paper_approved_view.html', context)




