#!/bin/python
# -*- coding: utf-8

import MySQLdb
import sys


def dbinit(host="localhost", user="root", passwd="root", db="userservice"):
    return MySQLdb.connect(host, user, passwd, db, charset='utf8')


def list(cursor):
    sql = """SELECT name FROM userservice.user;"""
    cursor.execute(sql)
    users = cursor.fetchall()
    for x in users:
        print x[0]


def adduser(db, newlogin, newpassword):
    sql = """INSERT INTO user(name,password) VALUES (%s, %s);"""
    try:
        db.cursor().execute(sql, (newlogin, newpassword))
        db.commit()
        print ("Пользователь " + newlogin + " добавлен")
    except MySQLdb.Error as e:
        print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
        db.rollback()


def deluser():
    sql = """delete from  userservice.user where name='test2';"""


login = str(raw_input("Login: "))
password = str(raw_input("Password: "))
db = dbinit()
cursor = db.cursor()

sql = """SELECT count(name) FROM user where name=%s AND password=%s;"""
cursor.execute(sql, (login.strip(), password.strip()))
row = cursor.fetchone()
name = row[0]
grant = False
if row[0]:
    grant = True

try:
    log = "login: " + login + " password: " + password
    sql = """INSERT INTO userlogs (log, access) VALUES (%s , %s);"""
    cursor.execute(sql, (log, grant))
    db.commit()
except MySQLdb.Error as e:
    print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
    db.rollback()
if grant is True:
    print "Доступ разрешен"
else:
    print "Доступ запрещен"
    sys.exit(1)
command = str(raw_input(">>> "))
command = command.strip()
if command == "list":
    list(cursor)
if command == "useradd":
    newlogin = str(raw_input("Login: "))
    newlogin = newlogin.strip()
    newpassword = str(raw_input("Password: "))
    newpassword = newpassword.strip()
    adduser(db, newlogin, newpassword)
if command == "deluser":
    dellogin = str(raw_input("login: "))
    accept = str(raw_input("Точно удалить " + dellogin + " y/N "))
    if accept == "y" or accept == "Y" or accept == "yes" or accept == "Yes" or accept == "YES":
        print "user deleted"
db.close()

