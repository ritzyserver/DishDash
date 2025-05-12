from django.core.management.base import BaseCommand
from orders.models import Stall

class Command(BaseCommand):
    help = 'Seeds the database with stall data'

    def handle(self, *args, **kwargs):
        # Empty the Stall table
        Stall.objects.all().delete()
        
        # Sample stalls data
        stalls_data = [
            {
                'name': 'NESCAFÉ',
                'description': 'Your favorite coffee destination',
                'contact_number': '+91931231321',
                'instagram': 'https://www.instagram.com/nescafe',
            },
            {
                'name': 'Dada ki CHAI',
                'description': 'Authentic Indian tea experience',
                'contact_number': '+91512331321',
                'instagram': 'https://www.instagram.com/dadakichai',
            },
            {
                'name': 'yummyYUM',
                'description': 'Delicious snacks and treats',
                'contact_number': '+91943512321',
                'instagram': 'https://www.instagram.com/yummyYum',
            }
        ]

        # Create stalls
        for stall_data in stalls_data:
            Stall.objects.get_or_create(
                name=stall_data['name'],
                defaults={
                    'description': stall_data['description'],
                    'contact_number': stall_data['contact_number'],
                    'instagram': stall_data['instagram']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded stalls data'))