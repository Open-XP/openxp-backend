from django.core.management.base import BaseCommand
from django.db import transaction
from exams.waec_model import Questions, Subject, Year, WAEC
from django.shortcuts import get_object_or_404

class Command(BaseCommand):
    help = 'Load questions from a provided text file into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the text file containing the questions')
        parser.add_argument('subject_name', type=str, help='Name of the subject these questions belong to')
        parser.add_argument('year_value', type=int, help='Year these questions are associated with')

    def handle(self, *args, **options):
        file_path = options['file_path']
        subject_name = options['subject_name']
        year_value = options['year_value']

        # Create a new WAEC instance
        waec_instance = WAEC.objects.get(pk=1)

        # Get or create the Subject and Year
        subject, _ = Subject.objects.get_or_create(name=subject_name, exam=waec_instance)
        year, _ = Year.objects.get_or_create(year=year_value)

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()

        questions = []
        question = {}

        for line in content:
            line = line.strip()
            # Adjusted the regex to recognize numbers from 1 to 60
            if line.startswith(tuple(f'{i}. ' for i in range(1, 61))):
                if question:
                    questions.append(question)
                question_text = line.split('.', 1)[1].strip()
                question = {'question': question_text}
            elif line and any(line.startswith(option) for option in ['A. ', 'B. ', 'C. ', 'D. ', 'E. ']):
                option_key, option_text = line.split('.', 1)
                question[option_key.strip()] = option_text.strip()
            elif line.startswith('Answer:'):
                answer = line.split(':')[1].strip().upper()
                question['answer'] = answer

        if question:  # To save the last question if any
            questions.append(question)

        with transaction.atomic():  # Use atomic transactions to ensure all-or-nothing save
            for q in questions:
                Questions.objects.update_or_create(
                    question=q['question'],
                    defaults={
                        'option_A': q.get('A', ''),
                        'option_B': q.get('B', ''),
                        'option_C': q.get('C', ''),
                        'option_D': q.get('D', ''),
                        'option_E': q.get('E', ''),
                        'answer': q['answer'],
                        'subject': subject,
                        'year': year
                    }
                )

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(questions)} questions into the database.'))
        
        
        
#Example of usage python manage.py load_questions exams\management\commands\waec_appended_multiple_choice_questions.txt "Agriculture" "2000"

# python manage.py load_questions exams\management\commands\waec_agric_2000.txt "Agriculture" "2000"
