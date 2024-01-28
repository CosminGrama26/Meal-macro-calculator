from project import clean_input, load_foods, food_search
from food import Food
import pytest
import random


def test_clean_input():
    assert clean_input("apple pie 89") == ("apple pie", "89")
    assert clean_input("banans 200") == ("banans", "200")
    assert clean_input("283u9bc 83h fu") == None
    assert clean_input("     454") == None
    assert clean_input("ALMONDS 77") == ("almonds", "77")
    assert clean_input("900 90") == None
    assert clean_input("apples") == None
    assert clean_input("/apples") == None
    assert clean_input("almonds:80") == None
    assert clean_input("almonds 80g") == None


def test_load_foods():
    assert type(load_foods()) == list
    for _ in range(20):
        assert type(load_foods()[random.randint(0, len(load_foods()))]) == Food


def test_food_search():
    foods = load_foods()
    assert food_search("000", foods) == None
    assert food_search("apples", foods).name == "apples"
    assert food_search("apple", foods) == None
    assert food_search("apple pie", foods).name == "apple pie"
    assert food_search("appless", foods) == None
    assert food_search("plutonium", foods) == None
    assert food_search("1-1-1-2", foods) == None


def test_Food___init__():
    with pytest.raises(ValueError):
        food = Food("test", 90, 90, 90)
    with pytest.raises(ValueError):
        food = Food("test", 90, 1, -1)
    with pytest.raises(ValueError):
        food = Food("test", "dog", 90, 90)
