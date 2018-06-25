def discount(price):
    '''
    Objective: To computer discount
    Input Parameter: price - numerice value
    Return Value : None
    '''
    pass


def sellingPrice(price):
    '''
    Objective: To compute selling price
    Input Parameter: price - numerice value
    Return Value: numeric value
    '''
    discountedPrice = discount(price)
    if discountedPrice == None:
        return price
    else:
        return discountedPrice

def main():
    '''
    Objective : To compute selling price
    Input Parameter : None
    Return Value: None
    '''
    price = float(input('Enter price :'))
    print('Selling Price is', sellingPrice(price))

if __name__=='__main__':
    main()
