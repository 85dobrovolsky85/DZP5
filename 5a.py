# задача 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def imput_dat(name):
    x = int(input(f'{name}, введите количество конфет, которое возьмете от 1 до 28:  '))
    while x < 1 or x > 28:
        x = int(input(f '{name}, введите корректное количество конфет:  " '))
    return x