import pymysql

# def connection(valeur):
conn = pymysql.connect("localhost", "root", "", "Jeu" )

user_cursor=conn.cursor()
monstres_cursor=conn.cursor()

Users = ("SELECT * FROM {0}".format("Users"))
user_cursor.execute(Users)

all_monstres = ("SELECT * FROM {0}".format("Monstres"))
monstres_cursor.execute(all_monstres)