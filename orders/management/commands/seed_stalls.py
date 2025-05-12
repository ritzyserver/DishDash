from django.core.management.base import BaseCommand
from orders.models import Stall, MenuItem

class Command(BaseCommand):
    help = 'Seeds the database with stall data and menu items'

    def handle(self, *args, **kwargs):
        
        # Empty the database
        Stall.objects.all().delete()
        
        # Sample stalls data with menu items
        stalls_data = [
            {
                'name': 'NESCAFÉ',
                'description': 'Your favorite coffee destination',
                'contact_number': '+91931231321',
                'instagram': 'https://www.instagram.com/nescafe',
                'menu_items': [
                    {'name': 'Cappuccino', 'price': 60, 'description': 'Classic Italian coffee with frothy milk'},
                    {'name': 'Cold Coffee', 'price': 80, 'description': 'Refreshing cold coffee with ice cream'},
                    {'name': 'Espresso', 'price': 50, 'description': 'Strong and pure coffee shot'},
                    {'name': 'Cookie', 'price': 30, 'description': 'Chocolate chip cookie'},
                    {'name': 'Croissant', 'price': 45, 'description': 'Butter croissant'}
                ]
            },
            {
                'name': 'Dada ki CHAI',
                'description': 'Authentic Indian tea experience',
                'contact_number': '+91512331321',
                'instagram': 'https://www.instagram.com/dadakichai',
                'menu_items': [
                    {'name': 'Masala Chai', 'price': 20, 'description': 'Traditional Indian spiced tea'},
                    {'name': 'Ginger Tea', 'price': 25, 'description': 'Tea with fresh ginger'},
                    {'name': 'Samosa', 'price': 15, 'description': 'Crispy pastry with spiced potato filling'},
                    {'name': 'Pakora', 'price': 30, 'description': 'Assorted vegetable fritters'},
                    {'name': 'Bun Maska', 'price': 25, 'description': 'Soft bun with butter'}
                ]
            },
            {
                'name': 'yummyYUM',
                'description': 'Delicious snacks and treats',
                'contact_number': '+91943512321',
                'instagram': 'https://www.instagram.com/yummyYum',
                'menu_items': [
                    {'name': 'Burger', 'price': 90, 'description': 'Classic veg burger with fries'},
                    {'name': 'Pizza', 'price': 120, 'description': 'Medium size margherita pizza'},
                    {'name': 'Sandwich', 'price': 70, 'description': 'Grilled veg cheese sandwich'},
                    {'name': 'French Fries', 'price': 60, 'description': 'Crispy salted french fries'},
                    {'name': 'Cold Drink', 'price': 40, 'description': 'Choice of soft drinks'}
                ]
            }
        ]

        # Clear existing data
        MenuItem.objects.all().delete()
        Stall.objects.all().delete()

        # Create stalls and their menu items
        for stall_data in stalls_data:
            menu_items = stall_data.pop('menu_items')
            stall, created = Stall.objects.get_or_create(
                name=stall_data['name'],
                defaults={
                    'description': stall_data['description'],
                    'contact_number': stall_data['contact_number'],
                    'instagram': stall_data['instagram']
                }
            )

            # Add menu items for the stall
            for item_data in menu_items:
                MenuItem.objects.get_or_create(
                    stall=stall,
                    name=item_data['name'],
                    defaults={
                        'price': item_data['price'],
                        'description': item_data['description']
                    }
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded stalls and menu items'))