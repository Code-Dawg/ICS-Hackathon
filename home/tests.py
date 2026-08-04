from django.test import TestCase, override_settings
from django.urls import reverse


@override_settings(ALLOWED_HOSTS=["testserver"])
class HomePageTests(TestCase):
    def test_home_page_renders(self):
        response = self.client.get(reverse("home:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "EduPulse")

# Create your tests here.
