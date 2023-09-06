from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# The status flag determines whether a post is a draft or published.
# The default value is 0, which means the post is a draft, until the author
# (or admin) changes the status to 1, which means the post is published.
STATUS = ((0, "Draft"), (1, "Publish"))
WRITING_TYPE = ((0, "Comment"), (1, "Writing"))
GENRES = (('Action and Adventure', 'Action and Adventure'),
    ('Comedy', 'Comedy'), ('Crime and Mistery', 'Crime and Mistery'),
    ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('SciFi', 'SciFi'),
    ('Romance', 'Romance'), ('Poetry', 'Poetry'), ('Other', 'Other'))

class Writing(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writings')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    main_genre = models.CharField(choices=GENRES, max_length=20)
    sub_genre = models.CharField(choices=GENRES, max_length=20, blank=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    abstract = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='writing_likes', blank=True)
    approved_writing = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

# The Comment model is used to store comments on posts.
# But, this comments can turn into further writings for the already
# existing post.
class Comment(models.Model):
    writing = models.ForeignKey(Writing, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    writing_type = models.IntegerField(choices=WRITING_TYPE, default=0)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.content} by {self.author}"

    def total_likes(self):
        return self.likes.count()
