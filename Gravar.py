#from doctest import master
from tkinter import *
from turtle import left
#import tkinter as tk
import requests

# Libs de bancos de dados
import mariadb
import sys
import pymysql
#import pymysql.connector as database
import os
#import mariadb.connector as database
#import mysql.connector as database

username = os.environ.get("username")
password = os.environ.get("password")

try:
    connection = mariadb.connect(
        user="root",
        password="Javeio2023*",
        host="localhost",
        port=3306)
    print ("abriu db")
except mariadb.Error as e:
            print(f"Erro de banco de dados: {e}")

cursor = connection.cursor()


def add_data(matricula, nome):
    try:

        entra_nome = input("Nome: ")
        entra_matricula = input("Matricula")
        #entra_idade = input ("Idade: ")
        statement = "INSERT INTO mysql.cadastrar_aluno (matricula, nome) VALUES = data"
        data = (entra_matricula, entra_nome)
        print(data)
        cursor.execute(statement, data)
        connection.commit()
        print("Gravado no banco de dados")
    except mariadb.Error as e:
        print(f"Erro de banco de dados: {e}")

def get_data(matricula):
    try:
      matbusca = input("Matricula buscado: ")
      statement = "SELECT matricula from mysql.cadastrar_aluno WHERE matbusca = matricula"
      data = (matbusca)
      cursor.execute(statement, data)
      for (matricula) in cursor:
        print(f"Recuperado {nome}")
    except mariadb.Error as e:
        print(f"Não encontrado: {e}")

add_data("32541", "Doe")
get_data( "Renato Moura")

connection.close()
