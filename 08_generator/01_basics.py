

def serve_chai():
    yield "Cup 01 - Masala Chai"
    yield "Cup 02 - Ginger Chai"
    yield "Cup 03 - Elaichi Chai"
    yield "Cup 04 - Soft Chai"
    
    
stalls=serve_chai()

for stall in stalls:
    print(stall)