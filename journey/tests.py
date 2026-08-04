from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile
import json

class JourneyTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teststudent', password='testpassword123')
        self.profile = Profile.objects.create(user=self.user)

    def test_anonymous_journey_view(self):
        response = self.client.get(reverse('journey:index'))
        self.assertEqual(response.status_code, 200)
        # Check that Level 1 is unlocked / available
        self.assertContains(response, 'Level 1')
        self.assertContains(response, 'Create Account')

    def test_authenticated_journey_view(self):
        self.client.login(username='teststudent', password='testpassword123')
        response = self.client.get(reverse('journey:index'))
        self.assertEqual(response.status_code, 200)
        # For logged in users, Level 1 is completed automatically, Level 2 is unlocked
        self.assertContains(response, 'completed')
        self.assertContains(response, 'unlocked')

    def test_complete_level_success(self):
        self.client.login(username='teststudent', password='testpassword123')
        
        # User starts at current_level = 2 (Level 1 completed on login)
        self.assertEqual(self.profile.current_level, 2)
        self.assertEqual(self.profile.xp, 0)
        
        # Post level completion
        url = reverse('journey:complete_level')
        response = self.client.post(
            url,
            data=json.dumps({'level': 2}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['current_level'], 3)
        self.assertEqual(data['xp'], 100)
        
        # Reload profile and assert change
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.current_level, 3)
        self.assertEqual(self.profile.xp, 100)

    def test_complete_level_failure_wrong_level(self):
        self.client.login(username='teststudent', password='testpassword123')
        
        # Try to complete level 5 directly (locked)
        url = reverse('journey:complete_level')
        response = self.client.post(
            url,
            data=json.dumps({'level': 5}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['message'], 'Invalid level completion attempt.')
        
        # Verify profile hasn't changed
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.current_level, 2)
        self.assertEqual(self.profile.xp, 0)

    def test_complete_level_anonymous_blocked(self):
        url = reverse('journey:complete_level')
        response = self.client.post(
            url,
            data=json.dumps({'level': 2}),
            content_type='application/json'
        )
        # Should redirect to login since complete_level_view has @login_required
        self.assertEqual(response.status_code, 302)
