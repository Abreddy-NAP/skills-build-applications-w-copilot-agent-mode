from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **options):
        user1 = User.objects.create(email="alice@example.com", name="Alice", password="alicepass")
        user2 = User.objects.create(email="bob@example.com", name="Bob", password="bobpass")
        user3 = User.objects.create(email="carol@example.com", name="Carol", password="carolpass")

        team1 = Team.objects.create(name="Team Octopus")
        team2 = Team.objects.create(name="Team Kraken")
        team1.members.set([user1, user2])
        team2.members.set([user3])

        Activity.objects.create(user=user1, activity_type="run", duration=30, date=timezone.now())
        Activity.objects.create(user=user2, activity_type="walk", duration=45, date=timezone.now())
        Activity.objects.create(user=user3, activity_type="strength", duration=20, date=timezone.now())

        Leaderboard.objects.create(team=team1, points=150)
        Leaderboard.objects.create(team=team2, points=100)

        Workout.objects.create(name="Pushups", description="Do 20 pushups", difficulty="Easy")
        Workout.objects.create(name="Sprints", description="Run 100m sprints", difficulty="Medium")
        Workout.objects.create(name="Plank", description="Hold plank for 1 minute", difficulty="Hard")

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
