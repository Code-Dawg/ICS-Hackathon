from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from accounts.models import Profile


class DashboardRankingTests(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="player", password="test-password")
        Profile.objects.create(user=self.player, xp=100, current_level=3)

        leader = User.objects.create_user(username="leader", password="test-password")
        Profile.objects.create(user=leader, xp=500, current_level=7)

        challenger = User.objects.create_user(username="challenger", password="test-password")
        Profile.objects.create(user=challenger, xp=250, current_level=5)

    def test_rankings_are_ordered_by_highest_xp_first(self):
        self.client.force_login(self.player)

        response = self.client.get(reverse("dashboard:index"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            [profile.user.username for profile in response.context["rankings"]],
            ["leader", "challenger", "player"],
        )
