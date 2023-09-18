from django.shortcuts import render, redirect, get_object_or_404, reverse
# With this we are importing the generic class-based views
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Writing, Comment
from .forms import CommentForm, WritingForm

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
            'commented': False,
            'liked': liked,
            'comment_form': CommentForm(),
        }
        return render(request, 'writing_detail.html', context)

    def post(self, request, slug, *args, **kwargs):
        # Variable to get only the published writings
        queryset = Writing.objects.filter(status=1)
        # Variable to get the published writing with the slug passed in the URL
        writing = get_object_or_404(queryset, slug=slug)
        comments = writing.comments.filter(approved_comment=True).order_by('-created_on')
        liked = False
        if writing.likes.filter(id=request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST or None)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            # In Django, when calling the user object, it is actually the ID on the table
            # that is being called. So, we need to pass the user object to the author field
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.writing = writing
            comment.save()
        else:
            comment_form = CommentForm()

        # This context can be created inside the return statement
        # but it is better to create it outside and then pass it
        # as an argument, so the code is easier to read.
        context = {
            'writing': writing,
            'comments': comments,
            'commented': True,
            'liked': liked,
            'comment_form': CommentForm(),
        }
        return render(request, 'writing_detail.html', context)

class WritingLike(View):
    def post(self, request, slug):
        # Get the specific writing
        writing = get_object_or_404(Writing, slug=slug)

        # Check if the user has already liked the post
        if writing.likes.filter(id=request.user.id).exists():
            # If so, unlike the post
            writing.likes.remove(request.user)
        else:
            # If not, like the post
            writing.likes.add(request.user)
        # Redirect the user to the same page
        return HttpResponseRedirect(reverse('writing_detail', args=[slug]))

class NewWritingView(generic.CreateView):
    model = Writing
    template_name = 'new_writing.html'
    fields = ('title', 'main_genre', 'sub_genre', 'content', 'featured_image', 'abstract')

    def post(self, request):
        writing_form = WritingForm(data=request.POST or None)

        if writing_form.is_valid():
            writing = writing_form.save(commit=False)
            writing.save()
        else:
            writing_form = writingForm()
        return render(request, 'new_writing.html', {'writing_form': WritingForm()})
