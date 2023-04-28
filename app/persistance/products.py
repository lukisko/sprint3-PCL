import app.model as model
import os

def getAllDrinks():
    # just if you want to test env variables
    print('username',os.environ['USERNAME'])
    print('password',os.environ['PASSWORD'])
    return [model.Product(1,"latte",'coffe','Medium',25),
            model.Product(2,"black tea",'tea','Large',20)]
    
def createDrink(product): # if succesfully created, return id other then 0
    product.id = 1
    return product

def removeDrink(productId):
    pass

def getDrink(id):
    return model.Product(1,"latte",'coffe','Medium',25)