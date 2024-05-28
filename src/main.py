from recipe_loader import load_recipes
from recipe_filter import filter_recipes

def get_user_input():
    ingredients = input("Enter available ingredients (comma-separated): ").split(',')
    dietary_requirements_input = input("Enter dietary requirements (comma-separated, e.g., vegan, gluten-free, vegetarian, dairy-free, nut-free). Leave blank if none: ")
    dietary_requirements = dietary_requirements_input.split(',') if dietary_requirements_input else []
    return [item.strip() for item in ingredients], [req.strip() for req in dietary_requirements]
def main():
    # Load recipes from the JSON file
    recipes = load_recipes('data/recipes.json')
    
    # Get user input
    available_ingredients, dietary_requirements = get_user_input()

    # Filter recipes
    matching_recipes = filter_recipes(recipes, available_ingredients, dietary_requirements)
    
    # Print matching recipes
    if matching_recipes:
        for recipe in matching_recipes:
            print(f"Recipe: {recipe['name']}")
            print(f"Ingredients: {', '.join(recipe['ingredients'])}")
            print(f"Instructions: {recipe['instructions']}\n")
    else:
        print("No matching recipes found.")

if __name__ == "__main__":
    main()
