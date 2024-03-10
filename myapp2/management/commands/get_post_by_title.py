from django.core.management.base import BaseCommand
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = "Get all posts by title name."
    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Title')
    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        post = Post.objects.filter(title=title).first()
        # intro = f'All posts\n'
        # text = '\n'.join(post.content for post in posts)
        self.stdout.write(f'{post}')