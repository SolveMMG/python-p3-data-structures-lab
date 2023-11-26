spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_names = [n["name"] for n in spicy_foods]
    return spicy_names


def get_spiciest_foods(spicy_foods):
    heat_five = [obj for obj in spicy_foods if obj["heat_level"]>5]
    return heat_five

    
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_sum = sum (num["heat_level"] for num in spicy_foods )
    return total_sum / len(spicy_foods)


def create_spicy_food(spicy_foods, new_food):
    spicy_foods.append(new_food)
    return spicy_foods