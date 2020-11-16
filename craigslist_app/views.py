from django.shortcuts import render

# homepage
def home(request):
    return render(request, 'base.html')

# 
def new_search(request):
    return render(request, 'craigslist_app/new-search.html')