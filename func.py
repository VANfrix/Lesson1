def discounted(price, discount):
<<<<<<< HEAD
    price_with_discount =price - (price * discount / 100)
    print(price_with_discount)
discounted(100, 50)
    
=======
    price = abs(price)
    discount = abs(discount)
    if discount >= 100:
        price_with_discount=price
    else:

        price_with_discount = price-(price * discount / 100)
    return(price_with_discount)

product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
product['with_discount'] = discounted(product['price'], product['discount'])
print(product)
>>>>>>> f909c5e43b59b54a58e96bdf42a7edcc6225b65a
