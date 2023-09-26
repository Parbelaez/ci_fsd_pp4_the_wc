from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
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
    paginate_by = 6

class MyWritingsListView(WritingListView):
    # This is a method to override the queryset
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(author=self.request.user)
        return qs

class WritingDetailView(generic.View):
    model = Writing
    template_name = 'writing_detail.html'

    def get(self, request, slug, *args, **kwargs):
        # Variable to get only the published writings
        queryset = Writing.objects.filter(status=1)
        # Variable to get the published writing with the slug passed in the URL
        writing = get_object_or_404(queryset, slug=slug)
        # comments = writing.comments.filter(approved_comment=True).order_by('-created_on')
        comments = writing.comments.order_by('-created_on')
        # If the user is not the author of the post, only approved comments are shown
        if writing.author != request.user:
            comments = comments.filter(approved_comment=True)
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
    form_class = WritingForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

class UpdateWritingView(generic.UpdateView):
    model = Writing
    template_name = 'update_writing.html'
    form_class = WritingForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

class DeleteWritingView(generic.DeleteView):
    model = Writing
    template_name = 'delete_writing.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        writing = super().get_object()
        if not writing.author == self.request.user:
            raise Http404
        return writing

class ApproveCommentView(generic.View):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.approved_comment = True
        comment.save()
        return HttpResponseRedirect(reverse('writing_detail', args=[comment.writing.slug]))

class SelectCommentView(generic.View):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.selected = True
        comment.save()
        return HttpResponseRedirect(reverse('writing_detail', args=[comment.writing.slug]))

class AboutView(generic.TemplateView):
    template_name = 'about.html'
