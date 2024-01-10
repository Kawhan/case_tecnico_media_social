from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from social_media.models import Comment, Post

User = get_user_model()


class testModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            email="test@example.com",
            password="123",
            first_name="test",
            last_name="test",
        )

        self.post = Post.objects.create(
            title="test",
            content="test",
            author=self.user
        )

        self.comment = Comment.objects.create(
            content="test",
            post=self.post,
            author=self.user
        )

    def test_post_creation(self):
        # Teste para verificar se a criação do post foi bem-sucedida
        self.assertEqual(self.post.title, "test")
        self.assertEqual(self.post.content, "test")
        self.assertEqual(self.post.author, self.user)

    def test_comment_creation(self):
        # Teste para verificar se a criação do comentário foi bem-sucedida
        self.assertEqual(self.comment.content, "test")
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.author, self.user)

    def test_post_author_is_user(self):
        # Teste para verificar se o autor do post é o usuário criado
        self.assertEqual(self.post.author, self.user)

    def test_comment_post_association(self):
        # Teste para verificar se o comentário está associado ao post correto
        self.assertEqual(self.comment.post, self.post)
