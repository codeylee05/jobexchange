from django.test import TestCase, Client
from django.urls import reverse
import json
from django.contrib.auth.models import User

from jobsearch.models import Job, Application

class TestViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.index_url = reverse("index")
        self.explore_url = reverse("explore")
        self.register_url = reverse("register")
        self.search_url = reverse("search")
        self.login_url = reverse("login")

        '''self.user = User.objects.create(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")'''

    def test_index_GET(self):
        """
        Asserts that the status code is 200 for success and the correct template 'index' is used'
        """
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "jobsearch/base.html")
        self.assertTemplateUsed(response, "jobsearch/index.html")

    def test_explore_jobs_get(self):
        """
        Asserts that the status code is 200 for success and the correct template 'explore' is used'
        """
        response = self.client.get(self.explore_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "jobsearch/base.html")
        self.assertTemplateUsed(response, "jobsearch/explore.html") 


    def test_search_GET(self):
        """
        Asserts that the status code is 200 for success and the correct template 'search' is used'.git
        """
        response = self.client.get(self.search_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "jobsearch/base.html")
        self.assertTemplateUsed(response, "jobsearch/search.html")

    
    def test_login_GET(self):
        """
        Asserts that the status code is 200 for success and the correct template 'login' is used'.git
        """
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "jobsearch/base.html")
        self.assertTemplateUsed(response, "jobsearch/login.html")
