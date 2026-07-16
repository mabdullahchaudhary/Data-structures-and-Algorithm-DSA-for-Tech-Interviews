
grocery_prices = {
    "Cheeni": 150,
    "Chaye Patti": 800,
    "Doodh": 220,
    "Bread": 180,
    "Anda": 30,
    "Chawal": 250,
    "Daal": 300,
    "Ghee": 600
}

final_price_after_10_discount={item: price * 0.9  for item,price in grocery_prices.items()}

print(final_price_after_10_discount)