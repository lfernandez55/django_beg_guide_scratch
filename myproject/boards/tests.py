# from django.test import TestCase
# from django.urls import resolve
# # Create your tests here.
# from django.urls import reverse
# from django.test import TestCase

# from django.test import TestCase
# from django.urls import resolve, reverse
#
# from .models import Board
# from .views import TopicListView
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, board_topics
from .models import Board



# class HomeTests(TestCase):
#     def test_home_view_status_code(self):
#         url = reverse('home')
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#
#     def test_home_url_resolves_home_view(self):
#         view = resolve('/')
#         self.assertEquals(view.func, home)
class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    # The new test here is the test_home_view_contains_link_to_topics_page.
    # Here we are using the assertContains method to test if the response body
    # contains a given text. The text we are using in the test, is the href part
    # of an a tag. So basically we are testing if the response body has the
    # text href="/boards/1/".
    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))


class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    # The test_board_topics_view_success_status_code method: is testing if
    # Django is returning a status code 200 (success) for an existing Board.
    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    #The test_board_topics_url_resolves_board_topics_view method: is testing
    #if Django is using the correct view function to render the topics.
    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
