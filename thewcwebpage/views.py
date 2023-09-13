from django.shortcuts import render, redirect, get_object_or_404
# With this we are importing the generic class-based views
from django.views import generic, View
from .models import Writing, Comment
from .forms import CommentForm

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

class WritingDetailView(generic.View):
    model = Writing
    template_name = 'writing_detail.html'

    def get(self, request, slug, *args, **kwargs):
        # Variable to get only the published writings
        queryset = Writing.objects.filter(status=1)
        # Variable to get the published writing with the slug passed in the URL
        writing = get_object_or_404(queryset, slug=slug)
        comments = writing.comments.filter(approved_comment=True).order_by('-created_on')
        liked = False
        if writing.likes.filter(id=request.user.id).exists():
            liked = True
        # This context can be created inside the return statement
        # but it is better to create it outside and then pass it
        # as an argument, so the code is easier to read.
        context = {
            'writing': writing,
            'comments': comments,
            'liked': liked,
            'comment_form': CommentForm(),
        }
        return render(request, 'writing_detail.html', context)