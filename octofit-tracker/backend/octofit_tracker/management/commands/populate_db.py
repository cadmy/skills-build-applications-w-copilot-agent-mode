from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(username='tony', email='tony@marvel.com', password='ironman', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@marvel.com', password='cap', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@marvel.com', password='hulk', team=marvel)
        clark = User.objects.create_user(username='clark', email='clark@dc.com', password='superman', team=dc)
        diana = User.objects.create_user(username='diana', email='diana@dc.com', password='wonderwoman', team=dc)
        barry = User.objects.create_user(username='barry', email='barry@dc.com', password='flash', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, distance=5)
        Activity.objects.create(user=steve, type='cycle', duration=60, distance=20)
        Activity.objects.create(user=bruce, type='swim', duration=45, distance=2)
        Activity.objects.create(user=clark, type='run', duration=50, distance=10)
        Activity.objects.create(user=diana, type='cycle', duration=70, distance=25)
        Activity.objects.create(user=barry, type='swim', duration=40, distance=3)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='A quick morning cardio session', duration=30)
        Workout.objects.create(name='Strength Training', description='Full body strength workout', duration=60)

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, points=100)
        Leaderboard.objects.create(user=steve, points=90)
        Leaderboard.objects.create(user=clark, points=110)
        Leaderboard.objects.create(user=diana, points=95)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
