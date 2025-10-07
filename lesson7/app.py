# import do_somethings
# from do_somethings import add, sub, mul

# from fooditems.raw_food import check_freshness, check_quantity
from fooditems.snacks import get_snacks_available, add_snack_to_cart
import fooditems.snacks
import os, sys
from fooditems.localfoods import soup
from fooditems.snacks import food_order
# print(dir(fooditems.snacks))
# print(sys.path)
# print(os.getcwd())
# print(fooditems.snacks.__name__)
# avaliable_snacks = get_snacks_available()
# print("Available snacks:", avaliable_snacks)

# add_snack_to_cart("Nuts")
# print("Updated snacks:", get_snacks_available())


if __name__ == "__main__":
    print("Snacks module executed directly")
    print("Current snacks:", get_snacks_available())
    add_snack_to_cart("Nuts")
    print("Updated snacks:", get_snacks_available())