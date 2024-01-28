from food import Food
from fuzzywuzzy import fuzz
from tabulate import tabulate, SEPARATING_LINE
import csv
import re
import sys


def main():
    # initialising
    meal = {"fat": 0, "grams": 0, "carbs": 0, "protein": 0, "calories": 0}
    meal_foods = []
    foods = load_foods()
    print()
    print("***********************************")
    print("MEAL CALORIES AND MACROS CALCULATOR")
    print("***********************************")
    print()
    print("Hello, this program helps you calculate nutritional values of your meal")
    print

    # prompting for valid input
    while True:
        try:
            inpt = clean_input(input("Insert a food and weight (in grams): "))
            if inpt == None:
                continue
            # dealing with potential multiple spaces in input
            raw_food, grams = inpt

            # find or add food
            food = food_search(raw_food, foods)
            if food == None:
                food = did_you_mean(raw_food, foods)
                if food == None:
                    continue
            # adding a food to the meal list and meal totals
            food.grams = grams
            meal_foods.append(food)
            meal["fat"] += food.fat * food.grams / 100
            meal["carbs"] += food.carbs * food.grams / 100
            meal["protein"] += food.protein * food.grams / 100
            meal["calories"] += food.calories * food.grams / 100
            meal["grams"] += food.grams
            print("(ctrl + D to quit)")
        except EOFError:
            print()
            break

    print_results(meal_foods, meal)


def load_foods():
    # loads foods from csv and puts them into an object list
    foods = []
    try:
        with open("foodlist.csv", "r") as input:
            reader = csv.DictReader(input)
            for row in reader:
                foods.append(Food(**row))
    except FileNotFoundError:
        print("Could not locate foodlist.csv")
        sys.exit(1)

    return foods


def clean_input(inpt):
    # checking input format
    inpt = inpt.strip().lower()
    if not re.search(r"^(\w| |-|\d)+ \d{1,4}$", inpt):
        print("Format: apples 80")
        return None
    # dealing with potential multiple spaces in input
    raw_food = ""
    for i in range(len(inpt.split(" ")) - 1):
        raw_food += inpt.split(" ")[i]
        raw_food += " "
    raw_food = raw_food.strip()
    if raw_food.isnumeric():
        print("Format: apples 80")
        return None

    grams = inpt.split(" ")[-1]
    return raw_food, grams


def food_search(inpt, foods):
    # looks for food in object list
    for row in foods:
        if inpt == row.name:
            return row
    return None


def did_you_mean(inpt, foods):
    # looking for similar results
    alt = set()
    for food in foods:
        if inpt in food.name or fuzz.ratio(inpt, food.name) > 75:
            alt.add(food)

    # in case no similar results were found.
    # "n" reponse goes back to main
    # "y" response sets "resp" to 0, to ensure add_food will be called
    if len(alt) == 0:
        while True:
            r = (
                input("Food not found. Would you like to add it to the list? y/n: ")
                .strip()
                .lower()
            )
            if r == "n":
                return None
            if r == "y":
                resp = 0
                break

    # in case similar results were found
    else:
        print("Did you mean:")
        alt = list(alt)
        for i in range(len(alt)):
            print(f" {i + 1}. {alt[i].name}")
        print("If the food is among the suggestions, type the suggestion #.")
        print("If you want to add the food to the list, type 0.")
        print("(ctr + D to go back)")

        # getting a valid index number
        while True:
            try:
                resp = int(input().strip())
                if not resp in range(0, len(alt) + 1):
                    print("Insert 0 or a number in the list:")
                    continue
                break
            except ValueError:
                print("Insert 0 or a number in the list:")
                continue
            except EOFError:
                return None

    # add food or return similar result
    if resp == 0:
        return add_food(foods)
    else:
        return alt[resp - 1]


def add_food(foods):
    # getting correct input for new food
    print("New food menu:")
    print("(ctrl + D to go back)")
    while True:
        try:
            name = input("Food name: ").strip().lower()
            if not food_search(name, foods) == None:
                print("Food already exists")
                print()
                continue
            fat = input("Fat for 100g: ").strip()
            carbs = input("Carbs for 100g: ").strip()
            protein = input("Protein for 100g: ").strip()
            food = Food(name, fat, carbs, protein)
            break
        except ValueError:
            print("Invalid data")
            print()
            continue
        except EOFError:
            print()
            return None

    # adding the food to the program list
    foods.append(food)
    # adding the food to csv file
    with open("foodlist.csv", "a") as output:
        writer = csv.writer(output)
        writer.writerow([food.name, food.fat, food.carbs, food.protein])
    # returning food to main
    print()
    print("Your food was added to the food list and to your meal!")
    return food


def print_results(foods, meal):
    # creating a list of lists to print as a table
    table = []
    # header row
    table.append(["Food name", "Grams", "Calories", "Carbs", "Protein", "Fat"])
    # foods row
    for food in foods:
        table.append(
            [
                food.name,
                food.grams,
                (food.calories * food.grams / 100),
                (food.carbs * food.grams / 100),
                (food.protein * food.grams / 100),
                (food.fat * food.grams / 100),
            ]
        )
    # adding row of totals
    table.append(
        [
            "Totals: ",
            meal["grams"],
            meal["calories"],
            meal["carbs"],
            meal["protein"],
            meal["fat"],
        ]
    )
    # final formatting and printing
    table.insert(-1, [SEPARATING_LINE])
    print()
    print(
        tabulate(
            table,
            headers="firstrow",
            tablefmt="fancygrid",
            floatfmt=".1f",
            intfmt=".1f",
        )
    )
    print()


if __name__ == "__main__":
    main()
