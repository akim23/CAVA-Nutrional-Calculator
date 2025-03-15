class NutritionCalculator:
    def __init__(self):
        self.nutritional_data = {
            "Curated Bowls": {
                "greek salad": {"calories": 585, "protein": 37, "fat": 40, "carbs": 19},
                "harissa avocado": {"calories": 840, "protein": 42, "fat": 50, "carbs": 63},
                "chicken and rice": {"calories": 710, "protein": 40, "fat": 42, "carbs": 43},
                "steak and harissa": {"calories": 615, "protein": 36, "fat": 36, "carbs": 39},
                "spicy lamb and avocado": {"calories": 795, "protein": 43, "fat": 53, "carbs": 50},
                "falafel crunch": {"calories": 860, "protein": 24, "fat": 56, "carbs": 88},
            },
            "Curated Pitas": {
                "falafel pita": {"calories": 560, "protein": 24, "fat": 30, "carbs": 63},
                "chicken pita": {"calories": 490, "protein": 35, "fat": 16, "carbs": 45},
                "steak pita": {"calories": 525, "protein": 35, "fat": 25, "carbs": 40},
                "harissa avocado pita": {"calories": 680, "protein": 42, "fat": 45, "carbs": 53},
                "spicy lamb pita": {"calories": 650, "protein": 42, "fat": 50, "carbs": 45},
            },
            "Greens and Grains": {
                "brown rice": {"calories": 310, "protein": 7, "fat": 10, "carbs": 48},
                "saffron basmati rice": {"calories": 290, "protein": 5, "fat": 7, "carbs": 54},
                "black lentils": {"calories": 270, "protein": 18, "fat": 7, "carbs": 37},
                "supergreens": {"calories": 40, "protein": 3, "fat": 0.5, "carbs": 8},
                "arugula": {"calories": 20, "protein": 2, "fat": 0.5, "carbs": 3},
                "baby spinach": {"calories": 20, "protein": 3, "fat": 0, "carbs": 3},
                "romaine": {"calories": 20, "protein": 1, "fat": 0, "carbs": 4},
                "splendidgreens": {"calories": 20, "protein": 1, "fat": 0, "carbs": 4},
            },
            "Mains": {
                "braised lamb": {"calories": 210, "protein": 24, "fat": 12, "carbs": 2},
                "grilled chicken": {"calories": 250, "protein": 28, "fat": 13, "carbs": 3},
                "falafel": {"calories": 350, "protein": 6, "fat": 26, "carbs": 7},
                "grilled steak": {"calories": 170, "protein": 23, "fat": 9, "carbs": 1},
                "harissa honey chicken": {"calories": 260, "protein": 26, "fat": 14, "carbs": 7},
                "roasted vegetables": {"calories": 100, "protein": 3, "fat": 4.5, "carbs": 14},
                "spicy lamb meatballs": {"calories": 300, "protein": 24, "fat": 21, "carbs": 3},
            },
            "Toppings": {
                "shredded romaine": {"calories": 5, "protein": 0, "fat": 0, "carbs": 1},
                "pita crisps": {"calories": 70, "protein": 1, "fat": 11, "carbs": 6},
                "cabbage slaw": {"calories": 35, "protein": 0, "fat": 3, "carbs": 2},
                "tomato and onion": {"calories": 20, "protein": 0, "fat": 1.5, "carbs": 2},
                "persian cucumber": {"calories": 15, "protein": 0, "fat": 1, "carbs": 1},
                "tomato and cucumber": {"calories": 5, "protein": 0, "fat": 0, "carbs": 1},
                "kalamata olives": {"calories": 35, "protein": 0, "fat": 3, "carbs": 2},
                "fiery broccoli": {"calories": 35, "protein": 1, "fat": 2.5, "carbs": 2},
                "pickled onions": {"calories": 20, "protein": 0, "fat": 0, "carbs": 5},
                "salt brined pickles": {"calories": 5, "protein": 0, "fat": 0, "carbs": 0},
                "crumbled feta": {"calories": 35, "protein": 3, "fat": 2.5, "carbs": 0},
                "fire roasted corn": {"calories": 45, "protein": 1, "fat": 2.5, "carbs": 5},
                "avocado": {"calories": 110, "protein": 2, "fat": 11, "carbs": 7},
            },
            "Dips + Spreads": {
                "tzatziki": {"calories": 35, "protein": 2, "fat": 2.5, "carbs": 1},
                "traditional hummus": {"calories": 45, "protein": 2, "fat": 2.5, "carbs": 4},
                "roasted eggplant dip": {"calories": 50, "protein": 0, "fat": 5, "carbs": 2},
                "crazy feta": {"calories": 70, "protein": 4, "fat": 6, "carbs": 1},
                "harissa": {"calories": 70, "protein": 1, "fat": 6, "carbs": 5},
                "red pepper hummus": {"calories": 40, "protein": 2, "fat": 1.5, "carbs": 5},
            },
            "Dressings": {
                "balsamic date vinaigrette": {"calories": 60, "protein": 0, "fat": 4, "carbs": 7},
                "yogurt dill": {"calories": 30, "protein": 2, "fat": 2, "carbs": 1},
                "lemon herb tahini": {"calories": 70, "protein": 2, "fat": 6, "carbs": 4},
                "tahini caesar": {"calories": 90, "protein": 2, "fat": 8, "carbs": 3},
                "greek vinaigrette": {"calories": 130, "protein": 0, "fat": 14, "carbs": 1},
                "skhug": {"calories": 80, "protein": 0, "fat": 9, "carbs": 1},
                "hot harissa vinaigrette": {"calories": 70, "protein": 0, "fat": 7, "carbs": 1},
                "garlic dressing": {"calories": 180, "protein": 0, "fat": 20, "carbs": 0},
            },
            "Sides": {
                "free side pita": {"calories": 80, "protein": 3, "fat": 1.5, "carbs": 13},
                "side pita": {"calories": 310, "protein": 13, "fat": 6, "carbs": 53},
                "classic pita chips": {"calories": 270, "protein": 10, "fat": 8, "carbs": 40},
            }
        }

    def calculate_nutrition(self, selected_ingredients):
        total_nutrition = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}
        for ingredient, quantity in selected_ingredients.items():
            for category, items in self.nutritional_data.items():
                if ingredient in items:
                    nutrition = items[ingredient]
                    for key in total_nutrition:
                        total_nutrition[key] += nutrition[key] * quantity
        return total_nutrition
