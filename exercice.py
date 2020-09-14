#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    addition = a + b + c
    moy = addition / 3
    return moy


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    Valeur_rad = (angle_degs + (angle_mins + angle_secs/60)/60) * math.pi/180
    return Valeur_rad


def to_degrees(angle_rads: float) -> tuple:
    angle = (angle_rads)*(360 /2*math.pi)
    en_degres= math.floor(angle)
    en_mins = math.floor(angle/60)
    en_secs = math.floor(angle/ 3600)
    return en_degres , en_mins , en_secs


def to_celsius(temperature: float) -> float:
    de_faren = (temperature - 32) * (5/9)
    return de_faren


def to_farenheit(temperature: float) -> float:
    de_celcius = (temperature * (9/5)) +32
    return de_celcius


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
