import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "cengiz1235",
    database = "testdatabase"
    )
mycursor = db.cursor()
#mycursor.execute("CREATE DATABASE testdatabase")
#mycursor.execute("CREATE TABLE Car (title VARCHAR(50), brand VARCHAR(50), year YEAR, price VARCHAR(50), color VARCHAR(50), transmission VARCHAR(50), imgurl VARCHAR(200))")

def insert_db(data):
    """Apiden gelen verileri önceden kayitli olup olmadigini kontrol edip veritabanina kaydeder

    Args:
        data ([list]): Veritabanina kaydekmek icin alinan liste
    """
    for i in data:
        mycursor.execute("SELECT EXISTS(SELECT * FROM Car WHERE imgurl = %s)", (i["Img_url"], ))
        for test in mycursor:
            if test[0] == 0:
                mycursor.execute("INSERT INTO Car (title, brand, year, price, color, transmission, imgurl) VALUES (%s, %s, %s, %s, %s, %s, %s)", (i["Title"], i["Brand"], i["Year"], i["Price"], i["Exterior"], i["Transmission"], i["Img_url"]))
    db.commit()
    
def show_db(): 
    """Verileri verideposundan cekip liste olusturur ve bunu json olarak kullanmak icin return eder

    Returns:
        list: Json formati icin kullanilacak liste
    """
    mycursor.execute("SELECT * FROM Car")
    sql_data = []
    for i in mycursor:
       sql_data.append({"Title": i[0], "Brand": i[1], "Year": i[2], "Price": i[3], "Color": i[4], "Trans": i[5], "İmg_url": i[6]})
    return sql_data

def delete_db():
    """Veritabaninindeki verileri siler
    """
    mycursor.execute("DELETE FROM Car")
    db.commit()
    return "DB deleted"