#!/usr/bin/python3
str = (
    "Python is an interpreted, interactive, object-oriented programming "
    "language that combines remarkable power with very clear syntax"
)
# Extraction des parties spécifiques de la chaîne
new_str = str[39:66] + str[106:112] + str[0:6]
print(new_str)