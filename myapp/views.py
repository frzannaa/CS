import csv
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Lecturer

def home(request):
    search_term = request.GET.get('searchLecturer')
    lecturers = Lecturer.objects.all()

    if search_term:
        lecturers = lecturers.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        )

    return render(request, 'home.html', {'lecturers': lecturers, 'searchTerm': search_term})

def about(request):
    return render(request, 'about.html')

def signup(request):
    # Your signup view function implementation
    pass

def lecturer_detail(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, pk=lecturer_id)

    # Determine the CSV file path based on the lecturer's ID
    file_path = f'myapp/static/author{lecturer_id}_papers.csv'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            papers = list(reader)
    except FileNotFoundError:
        papers = []  # Handle the case when the file is not found

    # Pre-process 'Publication Date' to 'Publication_Date' (remove spaces)
    for paper in papers:
        paper['Publication_Date'] = paper.pop('Publication Date', '').strip()

    return render(request, 'lecturer_detail.html', {'lecturer': lecturer, 'papers': papers})


def authors_page(request):
    authors_data = []
    authors_files = {
        'author1': 'myapp/static/author1_papers.csv',
        'author2': 'myapp/static/author2_papers.csv',
        # Add file paths for all authors
    }

    for author, file_path in authors_files.items():
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            papers = list(reader)
            authors_data.append({'name': author, 'papers': papers})

    return render(request, 'author.html', {'authors': authors_data})

    # ... Rest of the code for the authors page view ...

def search_lecturer(request):
    # This view handles the search form in the navbar
    search_term = request.GET.get('searchLecturer')
    lecturers = Lecturer.objects.all()

    if search_term:
        lecturers = lecturers.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        )

    return render(request, 'home.html', {'lecturers': lecturers, 'searchTerm': search_term})


