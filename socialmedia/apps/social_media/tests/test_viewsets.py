from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from social_media.models import Comment, Post


class PostsViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.post = Post.objects.create(
            title='Test Post', content='Test Content', author=self.user)

    def test_list_posts(self):
        url = reverse('posts-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        url = reverse('posts-list')
        data = {'title': 'Test Post', 'content': 'Test Content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.get(id=2).title, 'Test Post')

    def test_retrieve_post(self):
        url = reverse('posts-detail', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post')

    def test_update_post(self):
        url = reverse('posts-detail', args=[self.post.id])
        data = {'title': 'Updated Test Post',
                'content': 'Updated Test Content'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get(id=1).title, 'Updated Test Post')

    def test_delete_post(self):
        url = reverse('posts-detail', args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
