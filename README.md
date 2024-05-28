# Recipe Generator
## Overview
- The Recipe Generator is a Python application that generates recipes based on the available ingredients and dietary requirements provided by the user.
- It helps users find suitable recipes quickly without manually searching through numerous recipes.

## Features
- Filter recipes based on available ingredients.
- Filter recipes based on dietary requirements (e.g., vegan, gluten-free, vegetarian, dairy-free, nut-free).
- Display matching recipes with their ingredients and instructions.

## 
### Files and Directories
- **data/**: Contains the `recipes.json` file with sample recipes.
- **src/**: Contains the source code for the application.
  - `__init__.py`: Marks the directory as a Python package.
  - `main.py`: Main script to run the application.
  - `recipe_loader.py`: Module to load recipes from the JSON file.
  - `recipe_filter.py`: This module filters recipes based on user input.
- **README.md**: Documentation and instructions for the project.
- **requirements.txt**: List of dependencies (if any).

## Setup
### Prerequisites
- Python 3.6 or higher

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/recipe_generator.git
   cd recipe_generator

## Usage
1. Add your recipes to the data/recipes.json file. Could you make sure to follow the structure provided in the example?
2. Run the main script:
python src/main.py

3. Follow the prompts:
- Enter available ingredients as a comma-separated list.
- Enter dietary requirements as a comma-separated list (e.g., vegan, gluten-free, vegetarian, dairy-free, nut-free). Leave blank if none.
  
## Example
$ python src/main.py
- Enter available ingredients (comma-separated): spaghetti, ground beef, tomato sauce, onion, garlic
- Enter dietary requirements (comma-separated, e.g., vegan, gluten-free, vegetarian, dairy-free, nut-free). Leave blank if none:
- Recipe: Spaghetti Bolognese
- Ingredients: spaghetti, ground beef, tomato sauce, onion, garlic
- Instructions: Cook spaghetti. Brown beef with onion and garlic. Add tomato sauce and simmer. Combine with spaghetti.

## Contributing
- Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.
