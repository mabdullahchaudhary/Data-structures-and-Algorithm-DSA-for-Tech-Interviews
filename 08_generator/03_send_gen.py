

def customer_order():
    print("Welcome! Here's your order list .")
    order=yield
    while True:
        print(f"Order in process: {order}")
        order=yield

stall=customer_order()
next(stall)
stall.send("Lemon Tea")
stall.send("Mango Juice")