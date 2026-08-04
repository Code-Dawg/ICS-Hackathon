"""
==============================================================================
JOURNEY TEST SUITE
Validates level data retrievals, completion submissions, streaks, & report views.
==============================================================================
"""

import json
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile
from journey.models import UserLevelProgress, Achievement, UserAchievement

class JourneyTests(TestCase):
    def setUp(self):
        # Disable signal or create profile directly since profile is created via signals/flows
        self.user = User.objects.create_user(username='teststudent', password='testpassword123')
        # Check if profile already exists due to receiver, if not create
        self.profile, _ = Profile.objects.get_or_create(user=self.user)

    def test_anonymous_journey_view(self):
        response = self.client.get(reverse('journey:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Level 1')
        self.assertContains(response, 'Create Account')

    def test_authenticated_journey_view(self):
        self.client.login(username='teststudent', password='testpassword123')
        response = self.client.get(reverse('journey:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'completed')

    def test_get_level_data(self):
        self.client.login(username='teststudent', password='testpassword123')
        # Load Level 2 (which is unlocked)
        url = reverse('journey:get_level_data', kwargs={'level_id': 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['level'], 2)
        self.assertEqual(data['type'], 'scenario')
        self.assertTrue(len(data['scenarios']) > 0)

    def test_get_any_level_data_unlocked(self):
        self.client.login(username='teststudent', password='testpassword123')
        # Load Level 5 (allowed even if user current_level is 2)
        url = reverse('journey:get_level_data', kwargs={'level_id': 5})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_submit_level_completion_success(self):
        self.client.login(username='teststudent', password='testpassword123')
        
        self.profile.current_level = 2
        self.profile.save()

        url = reverse('journey:submit_completion')
        payload = {
            'level': 2,
            'xp': 100,
            'coins': 20,
            'stars': 3,
            'correct_count': 5,
            'wrong_count': 0,
            'privacy_diff': 10,
            'security_diff': 5,
            'reputation_diff': 5,
            'trust_diff': 5
        }
        response = self.client.post(
            url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'success')
        
        # Verify db persistence
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.current_level, 3)
        self.assertTrue(self.profile.xp >= 100)
        self.assertEqual(self.profile.coins, 20)
        self.assertEqual(self.profile.stars, 3)
        self.assertEqual(self.profile.privacy_score, 95) # 85 + 10

    def test_wrong_answers_apply_negative_marking(self):
        self.client.login(username='teststudent', password='testpassword123')
        response = self.client.post(
            reverse('journey:submit_completion'),
            data=json.dumps({
                'level': 2,
                'xp': 100,
                'coins': 20,
                'correct_count': 3,
                'wrong_count': 2,
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['xp_earned'], 80)
        self.assertEqual(data['negative_marks'], 20)

    def test_submit_out_of_order_level_allowed(self):
        self.client.login(username='teststudent', password='testpassword123')
        
        self.profile.current_level = 2
        self.profile.save()

        url = reverse('journey:submit_completion')
        # Try completing level 5 when user is at level 2
        payload = {'level': 5, 'xp': 100, 'coins': 20}
        response = self.client.post(
            url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
        self.profile.refresh_from_db()
        # Since completed level 5, progression should set current_level to 6
        self.assertEqual(self.profile.current_level, 6)

    def test_final_report_view(self):
        self.client.login(username='teststudent', password='testpassword123')
        url = reverse('journey:report')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sovereignty')
        self.assertContains(response, 'Report Card')
