def get_loss(w1, w2, w3, w4):
    try:
        y_part = 10 * w1 // w2
    except ZeroDivisionError:
        print("Error: Can't divide by zero")
    else:
        y = y_part - 5 * w2 * w3 + w4
        return y