# balance = 1100
# price = 500
# in_stock = 0

# print(bool(balance > price))
# print(bool(in_stock))

# if balance > price and in_stock:
#     print('одобрить покупку')
# elif not in_stock:
#     print('Такого товара нет в наличии')
# else:
#     print('Пополните баланс!')

# температура

# def check_weather(temperature):
#     if temperature<0:
#         return 'Cold on street'
#     elif temperature >=0 and temperature <15:
#         return 'Not cold'
#     elif temperature >=15 and temperature <25:
#         return 'Warm'
#     elif temperature >=25:
#         return 'Hot'
#     return "Not work"
# print(check_weather(-10))
# print(check_weather(8))
# print(check_weather(20))
# print(check_weather(-1))

def discounted(price, discount, max_discaunt=30, phone_name=''):
    price = abs(price)
    discount = abs(discount)
    max_discaunt = abs(max_discaunt)
    if max_discaunt >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discaunt:
        return price
    elif 'iphone' in phone_name.lower() or not phone_name:
        return price
    else:
        return price-(price * discount / 100)

new_price = discounted(100000, 10, phone_name='iphone12')
print(new_price)

new_price = discounted(40000, 10, phone_name='Samsung')
print(new_price)

new_price = discounted(5000, 20)
print(new_price)