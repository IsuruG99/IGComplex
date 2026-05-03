from django.test import TestCase
from django.urls import reverse

from .models import Article


class BlogListViewTests(TestCase):
	def test_blog_feed_orders_newest_first(self):
		older = Article.objects.create(
			title='Older entry',
			description='First note',
			start_date='2026-04-01',
		)
		newer = Article.objects.create(
			title='Newer entry',
			description='Second note',
			start_date='2026-05-01',
		)

		response = self.client.get(reverse('blog'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/blog.html')
		self.assertEqual(list(response.context['articles']), [newer, older])
		self.assertContains(response, f'ID: [{newer.id}]')
