from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from django.conf import settings.AUTH_USER_MODEL
from quiz_manager.models import UserScore, TestInstance, Subject  
from exams.waec_model import Subject 
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Populates the UserScore table with test data'

    def add_arguments(self, parser):
        parser.add_argument('start_date', type=str, help='Start date in YYYY-MM-DD format')
        parser.add_argument('end_date', type=str, help='End date in YYYY-MM-DD format')

    def handle(self, *args, **kwargs):
        start_date_str = kwargs['start_date']
        end_date_str = kwargs['end_date']

        start_date = make_aware(datetime.strptime(start_date_str, '%Y-%m-%d'))
        end_date = make_aware(datetime.strptime(end_date_str, '%Y-%m-%d'))

        if start_date > end_date:
            self.stdout.write(self.style.ERROR('End date must be after start date'))
            return

        self.stdout.write(f'Populating UserScore table from {start_date_str} to {end_date_str}...')

        # Clear existing data
        UserScore.objects.all().delete()

        # Fetch or create necessary instances
        user, _ = User.objects.get_or_create(username='test_user', defaults={'password': 'password'})
        exam, _ = Exam.objects.get_or_create(name='Sample Exam')
        subject, _ = Subject.objects.get_or_create(name='Sample Subject')

        # Create or fetch a TestInstance
        test_instance, created = TestInstance.objects.get_or_create(
            user=user,
            exam=exam,
            subject=subject,
            defaults={'start_time': start_date, 'end_time': end_date}
        )

        # Generate test data
        num_records = 100
        delta_days = (end_date - start_date).days

        for _ in range(num_records):
            date = start_date + timedelta(days=random.randint(0, delta_days))
            score = random.uniform(0, 1)  # Assuming score is a float between 0 and 1
            UserScore.objects.create(date=date, score=score, test_instance=test_instance)

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {num_records} UserScore records'))
