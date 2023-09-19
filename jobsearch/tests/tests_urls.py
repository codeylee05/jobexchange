from django.test import SimpleTestCase
from django.urls import reverse, resolve

from jobsearch.views import index, register, search, applied_jobs, process_register, process_search, apply, process_apply, delete_application

class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        
        url = reverse("index")
        
        self.assertEqual(resolve(url).func, index)

    def test_register_url_resolves(self):

        url = reverse("register")

        self.assertEqual(resolve(url).func, register)

    def test_search_url_resolves(self):

        url = reverse("search")

        self.assertEqual(resolve(url).func, search)

    def test_applied_jobs_url_resolves(self):

        url = reverse("applied_jobs")

        self.assertEqual(resolve(url).func, applied_jobs)

    def test_process_register_url_resolves(self):

        url = reverse("process_register")

        self.assertEqual(resolve(url).func, process_register)

    def test_process_search_url_resolves(self):

        url = reverse("process_search")

        self.assertEqual(resolve(url).func, process_search)

    def test_apply_url_resolves(self):

        url = reverse("apply", args=["1"]) #the argument '1' is some default arg of an integer as is the required data type

        self.assertEqual(resolve(url).func, apply)

    def test_process_apply_url_resolves(self):

        url = reverse("process_apply", args=["1"])

        self.assertEqual(resolve(url).func, process_apply)

    def test_delete_application_url_resolves(self):

        url = reverse("delete_application", args=["1"])

        self.assertEqual(resolve(url).func, delete_application)