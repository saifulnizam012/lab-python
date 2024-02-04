'''
Created on 22 MAY 2022

@author: MUHAMMAD NUR AKMAL BIN MOHAMAD RAZIF
'''

import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("green")


def langit(malzip):
    malzip.penup()
    malzip.goto(-400, -100)
    malzip.color("deepskyblue")
    malzip.speed(0)
    malzip.begin_fill()
    for i in range(2):
        malzip.forward(800)
        malzip.left(90)
        malzip.forward(500)
        malzip.left(90)
    malzip.end_fill()
    malzip.pendown()


def matahari(malzip):
    malzip.penup()
    malzip.goto(-280, 200)
    malzip.color("yellow")
    malzip.speed(0)
    malzip.begin_fill()
    malzip.circle(35)
    malzip.end_fill()
    malzip.pendown()


def rumah(malzip):
    malzip.penup()
    malzip.goto(-100, -100)
    malzip.pendown()
    malzip.color("black", "orange")
    malzip.speed(0)
    malzip.begin_fill()
    for i in range(2):
        malzip.forward(225)
        malzip.left(90)
        malzip.forward(170)
        malzip.left(90)
    malzip.end_fill()
    malzip.pendown()


def bumbung(malzip):
    malzip.penup()
    malzip.goto(-100, 70)
    malzip.pendown()
    malzip.color("black", "red")
    malzip.speed(0)
    malzip.begin_fill()
    malzip.forward(225)
    malzip.left(120)
    malzip.forward(90)
    malzip.left(60)
    malzip.forward(140)
    malzip.left(60)
    malzip.forward(90)
    malzip.end_fill()


def tingkap(malzip):
    x_axis = 60
    for i in range(2):
        malzip.penup()
        malzip.goto(x_axis, 0)
        malzip.pendown()
        malzip.color("black", "white")
        malzip.speed(0)
        malzip.begin_fill()
        for i in range(4):
            malzip.forward(50)
            malzip.left(90)
        malzip.end_fill()
        x_axis = x_axis - 145


def pintu(malzip):
    malzip.penup()
    malzip.goto(-10, -100)
    malzip.pendown()
    malzip.color("black", "chocolate")
    malzip.speed(0)
    malzip.begin_fill()
    for i in range(2):
        malzip.forward(50)
        malzip.left(90)
        malzip.forward(80)
        malzip.left(90)
    malzip.end_fill()


def tombol(malzip):
    malzip.penup()
    malzip.goto(0, -65)
    malzip.pendown()
    malzip.color("black")
    malzip.begin_fill()
    malzip.circle(5)
    malzip.end_fill()


def awan(malzip):
    malzip.penup()
    malzip.goto(200, 200)
    malzip.pendown()
    malzip.color("white")
    malzip.speed(0)
    malzip.begin_fill()
    malzip.circle(25)
    malzip.end_fill()

    malzip.penup()
    malzip.goto(180, 160)
    malzip.pendown()
    malzip.speed(0)
    malzip.begin_fill()
    malzip.circle(25)
    malzip.end_fill()

    malzip.penup()
    malzip.goto(160, 205)
    malzip.pendown()
    malzip.speed(0)
    malzip.begin_fill()
    malzip.circle(25)
    malzip.end_fill()

    malzip.penup()
    malzip.goto(140, 170)
    malzip.pendown()
    malzip.speed(0)
    malzip.begin_fill()
    malzip.circle(25)
    malzip.end_fill()


def gunung(malzip):
    malzip.penup()
    malzip.goto(-400, -100)
    malzip.pendown()
    malzip.speed(0)
    malzip.color("lightgreen")
    malzip.begin_fill()
    for i in range(3):
        malzip.forward(400)
        malzip.left(120)
    malzip.end_fill()

    malzip.penup()
    malzip.goto(50, -100)
    malzip.pendown()
    malzip.speed(0)
    malzip.color("lightgreen")
    malzip.begin_fill()
    for i in range(3):
        malzip.forward(400)
        malzip.left(120)
    malzip.end_fill()


def mainDraw():
    malzip = turtle.Turtle()
    langit(malzip)
    matahari(malzip)
    gunung(malzip)
    awan(malzip)
    rumah(malzip)
    tingkap(malzip)
    pintu(malzip)
    tombol(malzip)
    bumbung(malzip)


if __name__ == '__main__':
    mainDraw()

wn.exitonclick()
