# MEAL CALORIES AND MACROS CALCULATOR
## Video Demo:  <https://youtu.be/7AQVHSunyyA>
## Description:
This Python program helps the user keep track of the macro nutrient values and calories of a meal. The user can search for a food type from an already existent list and add that food and quantity to the meal. If the food is not found in the list, the program proposes similar results, and the user can choose among them, or alternatively, he can choose to add a new type of food to the list and to his meal. At any point, the user can choose to go back or to quit the program. At the end, a table with the meal data will be printed.

### Project Components

The project is composed of multiple files:

- `project.py`: Contains all the functions.
- `food.py`: Defines the Food object class.
- `foodlist.csv`: Contains all the food data.
- `test_project.py`: Tests `project.py` and `food.py`.

### Functions in `project.py`

- `main()`: Coordinates all other functions and keeps track of the meal totals.
- `load_foods()`: Opens the csv file and loads all the data into a list of Food class objects.
- `clean_input()`: Ensures that the user types valid input; otherwise, it re-prompts for valid input. Additionally, the function splits the input into food type and quantity.
- `food_search()`: Looks for the food type in Food objects list. If the food is not found, the function will return None to the main.
- `did_you_mean()`: Called by main when `food_search()` returns None. This function looks for similar foods and asks the user to choose among them. The user can also choose to add a new type of food, and in this case, `add_food()` will be called. If the user changes his mind, he can always go back to the main food insertion menu by pressing `Ctrl + D`. Furthermore, even if no matching results are found, the function will still ask the user if he wants to add a new food. If the user answers "n", None will be returned to `main()`, which will keep prompting for new foods.
- `add_food()`: Prompts the user for the new food name and macro values. The function will then try to initialize a new Food class object. All the macro nutrient value setters of the class also contain validity checks. If the data inserted by the user is not valid, `food.py` will generate a `ValueError`, and `add_food()` will re-prompt the user for valid data. The object initializer takes care of calculating the calories value of the added food. If a food is valid, it will be added not only to the meal but also to `foodlist.csv`.
- `print_results()`: Creates a list with a breakdown of all the meal’s foods and totals. The list is then printed as a grid, with the decimals rounded to the first digit.

### Testing in `test_project.py`

`test_project.py` tests `clean_input()`, `load_foods()`, `food_search()`, as well as the Food object initializer.

### Libraries

The pip-installable libraries used in this project are:

- `fuzzywuzzy`: For finding similar results.
- `python-Levenshtein`: Required by `fuzzywuzzy`.
- `tabulate`: For printing the formatted grid.
- `pytest`: For the testing.

