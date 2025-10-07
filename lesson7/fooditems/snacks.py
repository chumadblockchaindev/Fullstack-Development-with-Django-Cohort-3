db = {0: "Chips", 1: "Chocolate", 2: "Cookies"}

def get_snacks_available():
    return db

def add_snack_to_cart(snack):
    db.setdefault(len(db), snack)


class FoodOrder:
    def __init__(self):
        self.order = []

    def add_item(self, item):
        self.order.append(item)

    def view_order(self):
        return self.order

food_order = FoodOrder()

# if __name__ == "fooditems.snacks":
#     print("Snacks module executed directly")
#     print("Current snacks:", get_snacks_available())
#     add_snack_to_cart("Nuts")
#     print("Updated snacks:", get_snacks_available())