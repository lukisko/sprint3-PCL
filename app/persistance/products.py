import app.model as model

def getAllDrinks():
    return [model.Product(1,"latte",'coffe','Medium',25),
            model.Product(2,"black tea",'tea','Large',20)]
    
def createDrink(product): # if succesfully created, return id other then 0
    product.id = 1
    return product