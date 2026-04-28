import enum

class Order(enum.Enum):
    DRINK = "drink"
    FOOD = "food"

def value_pattern(subject):

    match subject:
        case Order.DRINK:
            return f"{Order.DRINK.value}の注文です。"
        case Order.FOOD:
            return f"{Order.FOOD.value}の注文です。"
        case drink, size:
            return f"{drink}の{size}です"

        case _:
            return "注文がありません"

print( value_pattern( Order.DRINK ) )
print( value_pattern( Order.FOOD ))
print( value_pattern( ("coffee", "large")))
print( value_pattern( ("coffee", "large", "aaa")))