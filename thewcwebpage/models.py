import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils import timezone
from cloudinary.models import CloudinaryField

# The status flag determines whether a post is a draft or published.
# The default value is 0, which means the post is a draft, until the author
# (or admin) changes the status to 1, which means the post is published.
STATUS = ((0, "Draft"), (1, "Publish"))
writing_type = ((0, "Comment"), (1, "Writing"))
GENRES = (('Action and Adventure', 'Action and Adventure'),
    ('Comedy', 'Comedy'), ('Crime and Mistery', 'Crime and Mistery'),
    ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('SciFi', 'SciFi'),
    ('Romance', 'Romance'), ('Poetry', 'Poetry'), ('Other', 'Other'))

class Genre(models.Model):
    name = models.CharField(choices=GENRES, max_length=20, default='Other')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")

class Writing(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null=False, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writings')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    main_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='main_genre')
    sub_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='sub_genre', blank=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    abstract = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='writing_likes', blank=True)
    approved_writing = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + '-' + str(self.author)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse("writing-detail", kwargs={"slug": self.slug})
        return reverse("home")

    @property
    def can_comment(self):
        if self.created_on > timezone.now() - datetime.timedelta(days=7):
            return True
    
    @property
    def total_comments(self):
        return self.comments.count()

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
    writing_type = models.IntegerField(choices=writing_type, default=0)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    approved_comment = models.BooleanField(default=False)
    selected = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.content} by {self.author}"

    def total_likes(self):
        return self.likes.count()
