'''
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)
    def test_home_page_returns_correct_html(self):
        request=HttpRequest()
        response=home_page(request)
        html=response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))
# Create your tests here.
'''
from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


class HomePageTest(TestCase):

    def test_use_home_template(self):
        response = self.client.get('/')
     #   self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows),'New To-Do item did not appear in table')

        self.assertTemplateUsed(response, 'home.html')

'''
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')      #解析url，映射到响应的视图函数
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        response=self.client.get('/')
        html=response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response,'home.html')
        '''
'''
        request=HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        expected_html=render_to_string('home.html')
        self.assertEqual(html,expected_html)
   
     
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))
'''