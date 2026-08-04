from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from home.models import PlayerProfile, Scenario, Choice, UserAnswer, Achievement, UserAchievement

class DigitalFootprintGameTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testplayer', password='password123')
        self.profile = PlayerProfile.objects.create(user=self.user)

        # Create test scenario and choices
        self.scenario1 = Scenario.objects.create(
            order=1,
            title='Tagged Photo Test',
            category='Tagged Photos',
            situation_text='Friend tagged you in photo.'
        )
        self.choice_good = Choice.objects.create(
            scenario=self.scenario1,
            text='Untag yourself and ask friend to remove it.',
            score_impact=10,
            quality_type='EXCELLENT',
            explanation='Breaks link to profile.',
            consequences='Clean footprint.',
            tip='Act immediately.'
        )
        self.choice_bad = Choice.objects.create(
            scenario=self.scenario1,
            text='Leave it public.',
            score_impact=-10,
            quality_type='DANGEROUS',
            explanation='Public indexed photo.',
            consequences='Search engine records.',
            tip='Do not leave public tags.'
        )

        # Create achievement
        self.achievement = Achievement.objects.create(
            title='First Digital Step',
            description='Completed your first scenario.',
            icon_emoji='👣',
            badge_code='FIRST_STEP',
            criteria_type='SCENARIO_1'
        )

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newplayer',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        })
        self.assertEqual(response.status_code, 302) # Redirects to start_journey
        self.assertTrue(User.objects.filter(username='newplayer').exists())
        self.assertTrue(PlayerProfile.objects.filter(user__username='newplayer').exists())

    def test_scenario_view_requires_login(self):
        response = self.client.get(reverse('scenario_detail', kwargs={'order': 1}))
        self.assertEqual(response.status_code, 302) # Redirect to login

    def test_submit_choice_updates_score_and_records_answer(self):
        self.client.login(username='testplayer', password='password123')
        
        response = self.client.post(reverse('submit_choice', kwargs={'order': 1}), {
            'choice_id': self.choice_good.id
        })
        self.assertEqual(response.status_code, 302) # Redirects to explanation
        
        # Check answer recorded
        answer = UserAnswer.objects.get(user=self.user, scenario=self.scenario1)
        self.assertEqual(answer.choice, self.choice_good)
        self.assertEqual(answer.score_delta, 10)

        # Check profile score updated
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.current_score, 10)

        # Check achievement unlocked
        self.assertTrue(UserAchievement.objects.filter(user=self.user, achievement=self.achievement).exists())

    def test_final_report_generation(self):
        self.client.login(username='testplayer', password='password123')
        UserAnswer.objects.create(
            user=self.user,
            scenario=self.scenario1,
            choice=self.choice_good,
            score_delta=10
        )
        self.profile.current_score = 10
        self.profile.save()

        response = self.client.get(reverse('final_report'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Final Digital Footprint Report')
        self.assertContains(response, 'Tagged Photo Test')

