#!/bin/python
# -*- coding: utf-8

import MySQLdb
import sys
import getpass


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


def deluser(db, dellogin):
    sql = """delete from  userservice.user where name=%s;"""
    try:
        db.begin()
        db.cursor().execute(sql, (dellogin,))
        db.commit()
        print("Пользователь " + dellogin + " удален")
    except MySQLdb.Error as e:
        print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
        db.rollback()


def help():
    print "Список команд: "
    print "    'list' - список участников"
    print "    'useradd' - Добавить нового участника"
    print "    'deluser' - Удалить участника"


def isadmin(db, login):
    sql = """SELECT isadmin FROM userservice.user where name =%s;"""
    cursor = db.cursor()
    cursor.execute(sql, (login, ))
    raw = cursor.fetchone()
    return raw[0]


def sudo(db, user):
    sql = """update userservice.user set isadmin=1 where name=%s;"""
    try:
        db.cursor().execute(sql, (user,))
        db.commit()
    except MySQLdb.Error as e:
        print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
        db.rollback()


def checkuser(db, name):
    sql = """SELECT COUNT(name) FROM userservice.user WHERE name=%s"""
    cursor.execute(sql, (name.strip(), ))
    row = cursor.fetchone()
    return row[0]


login = str(raw_input("Login: "))
password = getpass.getpass()
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
while True:
    command = str(raw_input(">>> "))
    command = command.strip()
    if command == "list":
        list(cursor)
    elif command == "useradd":
        if isadmin(db, login):
            newlogin = str(raw_input("Имя пользователя: "))
            newlogin = newlogin.strip()
            while True:
                newpassword = getpass.getpass("Новый пароль: ")
                newpassword = newpassword.strip()
                newpassword2 = getpass.getpass("Повторите пароль: ")
                newpassword2 = newpassword2.strip()
                if newpassword == newpassword2:
                    break
                else:
                    print "Пароли не совпадают. Повторите ввод "
            adduser(db, newlogin, newpassword)
        else:
        	print "Недостаточно прав!"
    elif command == "deluser":
    	if isadmin(db, login):
            dellogin = str(raw_input("login: "))
            if checkuser(db, dellogin):
                accept = str(raw_input("Точно удалить " + dellogin + " y/N "))
                if accept == "y" or accept == "Y" or accept == "yes" or accept == "Yes" or accept == "YES" or accept == "да" or accept == "Да" or accept == "ДА":            
                    deluser(db, dellogin)
            else:
                print "Пользователь не найден"
        else:
            print "Недостаточно прав!"
    elif command == "quit":
        sys.exit(0)
    elif command == "help":
        help()
    elif command == "admin":
        print isadmin(db, login)
    elif command == "sudo":
        if isadmin(db, login):
            newadmin = str(raw_input("Введите имя пользователя: "))
            if checkuser(db, newadmin):
                sudo(db, newadmin)
                print "Пользователь " + newadmin + " теперь администратор"
            else:
                print "Пользователь не найден"
        else:
            print "Недостаточно прав!"
    else:
        help()
db.close()
