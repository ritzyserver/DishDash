from django.core.management.base import BaseCommand
from orders.models import Stall, Recipe


class Command(BaseCommand):
    help = "Seeds the database with sample recipes"
    

    def handle(self, *args, **kwargs):
        
        # Empty the database
        Recipe.objects.all().delete()
        
        # Get or create stalls
        stall1, _ = Stall.objects.get_or_create(
            name='Dada ki CHAI',
            defaults={
                'description': 'Authentic Indian tea experience',
                'contact_number': '+91512331321',
            },
        )

        stall2, _ = Stall.objects.get_or_create(
            name='yummyYUM',
            defaults={
                'description': 'Delicious snacks and treats',
                'contact_number': '+91943512321',
            },
        )

        # Sample recipes
        recipes_data = [
            {
                "title": "Homestyle Mac and Cheese",
                "description": "Creamy, cheesy, and absolutely comforting classic mac and cheese",
                "ingredients": """- 500g macaroni pasta
- 2 cups cheddar cheese
- 1 cup mozzarella
- 2 cups milk
- 3 tbsp butter
- 3 tbsp flour
- Salt and pepper to taste""",
                "instructions": """1. Cook pasta according to package instructions
2. Make a roux with butter and flour
3. Add milk and whisk until smooth
4. Add cheese and stir until melted
5. Mix with cooked pasta
6. Top with extra cheese and bake until golden""",
                "cooking_time": 30,
                "stall": stall1,
            },
            {
                "title": "Vegetable Biryani",
                "description": "Aromatic rice dish loaded with fresh vegetables and authentic Indian spices",
                "ingredients": """- 2 cups basmati rice
- Mixed vegetables (carrots, peas, beans)
- 2 onions, sliced
- 2 tomatoes, chopped
- Biryani spices
- Fresh mint and coriander
- Ghee or oil as needed""",
                "instructions": """1. Soak rice for 30 minutes
2. Prepare biryani masala
3. Saute vegetables with spices
4. Layer rice and vegetables
5. Dum cook for 20 minutes
6. Garnish with fried onions and serve""",
                "cooking_time": 60,
                "stall": stall2,
            },
            {
                "title": "Chocolate Brownie",
                "description": "Rich, fudgy brownies with a perfect crackly top",
                "ingredients": """- 200g dark chocolate
- 200g butter
- 200g sugar
- 3 eggs
- 100g flour
- 30g cocoa powder
- Vanilla extract""",
                "instructions": """1. Melt chocolate and butter together
2. Mix in sugar and eggs
3. Fold in flour and cocoa powder
4. Pour into lined baking tin
5. Bake at 180°C for 25 minutes
6. Let cool before cutting""",
                "cooking_time": 35,
                "stall": stall1,
            },
            {
                "title": "Paneer Tikka",
                "description": "Grilled paneer marinated in spices and yogurt, served with mint chutney",
                "ingredients": """- 250g paneer
- 1 cup yogurt
- 2 tbsp tikka masala
- 1 tbsp ginger-garlic paste
- 1 bell pepper, cubed
- 1 onion, cubed
- Skewers (wooden or metal)
- Salt to taste""",
                "instructions": """1. Marinate paneer and vegetables in yogurt and spices
2. Thread onto skewers
3. Grill or bake until charred
4. Serve with mint chutney
5. Enjoy with naan or rice""",
                "cooking_time": 25,
                "stall": stall2,
            },
        ]

        # Create recipes
        for recipe_data in recipes_data:
            Recipe.objects.get_or_create(
                title=recipe_data["title"],
                defaults={
                    "description": recipe_data["description"],
                    "ingredients": recipe_data["ingredients"],
                    "instructions": recipe_data["instructions"],
                    "cooking_time": recipe_data["cooking_time"],
                    "stall": recipe_data["stall"],
                },
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded recipes"))
