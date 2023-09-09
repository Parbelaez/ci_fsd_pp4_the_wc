from django.shortcuts import render, redirect
# With this we are importing the generic class-based views
from django.views import generic
from .models import Writing, Comment

# From the generic class-based views we are importing the ListView
# which is used to display a list of objects (DB tables or content)
# in a specific order
class WritingListView(generic.ListView):
    model = Writing
    # This is Django's way of querying the database
    # for all writings with status 1 (published) and ordering them
    # by the created_on field in descending order.
    queryset = Writing.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # Paginate determines how many posts are shown per page.
    paginate_by = 10

    def home(request):
        return render(request, 'index.html')