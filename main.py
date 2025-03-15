import streamlit as st
from function import NutritionCalculator

nutrition_calculator = NutritionCalculator()

st.title("Nutrition Calculator")

# Inject custom CSS for styling
st.markdown("""
    <style>
        .ingredient-name {
            font-weight: bold;
            font-size: 18px;
        }
        .ingredient-data {
            font-size: 14px;
        }
        .number-input input {
            width: 50px !important;
            padding: 5px !important;
        }
    </style>
""", unsafe_allow_html=True)

selected_ingredients = {}
half_portions = {}

# Display ingredients with checkboxes and quantity input
for category, items in nutrition_calculator.nutritional_data.items():
    st.subheader(category)
    for ingredient, nutrition in items.items():
        checkbox_label = f"**{ingredient.capitalize()}** - Calories: {nutrition['calories']} | Protein: {nutrition['protein']}g | Fat: {nutrition['fat']}g | Carbs: {nutrition['carbs']}g"
        checkbox = st.checkbox(checkbox_label, key=ingredient)

        if checkbox:
            quantity = st.number_input(
                f"Qty of {ingredient.capitalize()}",
                min_value=1, max_value=5, value=1, step=1, key=f"quantity_{ingredient}",
                format="%d", help="Adjust the quantity",
                label_visibility="collapsed",
            )

            half_portion = st.checkbox(f"Half Portion of {ingredient.capitalize()}", key=f"half_{ingredient}")

            selected_ingredients[ingredient] = (quantity, half_portion)

# Button to calculate nutrition
if st.button("Calculate Nutrition"):
    if selected_ingredients:
        total_nutrition = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}

        for ingredient, (quantity, half) in selected_ingredients.items():
            for category, items in nutrition_calculator.nutritional_data.items():
                if ingredient in items:
                    nutrition = items[ingredient]
                    factor = 0.5 if half else 1  # Apply halving factor
                    for key in total_nutrition:
                        total_nutrition[key] += nutrition[key] * quantity * factor

        st.write("### Total Nutritional Facts:")
        for nutrient, value in total_nutrition.items():
            st.write(f"{nutrient.capitalize()}: {value}")
    else:
        st.write("Please select at least one ingredient.")