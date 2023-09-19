from django.test import TestCase

from jobsearch.models import Job, Application
from django.contrib.auth.models import User

class TestModels(TestCase):

    def setUp(self):

        self.job1 = Job.objects.create(
            job_name="job1", 
            job_level="JUNIOR", 
            job_hirer="hirer1", 
            job_location="location1", 
            job_salary=1000, 
            job_description="description1"
        )
        self.application1 = Application.objects.create(
            target_job=self.job1,
            job_applicant=User.objects.create(first_name="user1", password="user1pass")
        )

    def test_is_valid_job(self):

        self.assertEquals(self.job1.is_valid_job(), True)

    def test_is_valid_application(self):

        self.assertEquals(self.application1.is_valid_application(), True)