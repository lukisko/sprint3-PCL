import app.model as model
import psycopg2
import app.persistance.initials as initials



def createConnetction():
    conn = psycopg2.connect(
        host=initials.host,
        database=initials.database,
        user=initials.user,
        password=initials.password
    )
    cur = conn.cursor()
    return conn, cur


def getAllDrinks():
    conn, cur = createConnetction()
    cur.execute("SELECT * FROM Product")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    print(rows)

    drinks = []
    for row in rows:
        drinks.append(model.Product(row[0],row[1],row[2],row[3],row[4]))

    return drinks
    
def createDrink(product): # if succesfully created, return id other then 0
    conn, cur = createConnetction()
    cur.execute("INSERT INTO Product (title, category, size, price) VALUES (%s, %s, %s, %s) RETURNING id", (product.Title, product.Category, product.Size, product.Price))
    conn.commit()
    id = cur.fetchone()[0]
    cur.close()
    conn.close()

    product.id = id < 1 and 0 or id
    return product

def removeDrink(productId):
    conn, cur = createConnetction()
    cur.execute("DELETE FROM Product WHERE id = %s", (productId,))
    conn.commit()
    cur.close()
    conn.close()


def getDrink(id):
    conn, cur = createConnetction()
    cur.execute("SELECT * FROM Product WHERE id = %s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row is None:
        return None
    else:
        return model.Product(row[0],row[1],row[2],row[3],row[4])