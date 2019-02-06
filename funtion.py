def inc_vat(price):
    return price+(price*7/100)

def exc_vat(price):
    return price - (price * 7 / 100)

if __name__ == '__main__':
    print("Price with VAT will be " + str(inc_vat(sell_price)))
    print("Price without VAT will be " + str(exc_vat(100)))