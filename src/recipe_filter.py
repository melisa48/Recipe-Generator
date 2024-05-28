def filter_recipes(recipes, available_ingredients, dietary_requirements):
    filtered_recipes = []
    for recipe in recipes:
        if all(item in available_ingredients for item in recipe['ingredients']):
            # If no dietary requirements are provided, include the recipe
            if not dietary_requirements:
                filtered_recipes.append(recipe)
            # Otherwise, check if the recipe meets the dietary requirements
            elif all(req in recipe['dietary'] for req in dietary_requirements):
                filtered_recipes.append(recipe)
    return filtered_recipes
