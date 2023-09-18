from django.contrib import admin
from .models import Writing, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Writing)
class WritingAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'main_genre', 'sub_genre')
    list_display = ('title', 'slug', 'author', 'created_on', 'updated_on', 'main_genre', 'sub_genre', 'status', 'total_likes')
    search_fields = ['title', 'content', 'author', 'main_genre', 'sub_genre']
    summernote_fields = ('content',)
    actions = ['publish_writings', 'approve_writings']

    # This method is used to publish writings from the admin panel.
    def publish_writings(self, request, queryset):
        queryset.update(status=1)

    # This method is used to approve writings from the admin panel.
    def approve_writings(self, request, queryset):
        queryset.update(approved_writing=True)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('writing', 'author', 'created_on', 'updated_on', 'status', 'comment_type', 'total_likes', 'approved_comment')
    list_filter = ('status', 'created_on', 'comment_type', 'approved_comment')
    search_fields = ['writing', 'content', 'author', 'comment_type']
    actions = ['approve_comments']

    # This method is used to approve comments from the admin panel.
    def approve_comments(self, request, queryset):
        queryset.update(approved_comment=True)
