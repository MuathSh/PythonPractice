#practice using match
def check_cart(user_input):
    cart1 = ['oranges', 'apples', 'bananas']
    cart2 = ['papaya', 'watermelon', 'melon']
    
    match user_input.lower().strip():
        case 'oranges' | 'apples' | 'bananas':
            print(f"The item is in the first cart: {cart1}")
        case 'papaya' | 'watermelon' | 'melon':
            print(f"The item is in the second cart: {cart2}")
        case _:
            print("Not in any cart")

item_input = input("Enter an item: ")
check_cart(item_input)