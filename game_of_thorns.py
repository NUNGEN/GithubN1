import os
import random

characters = [

"Jon Snow","Daenerys Targaryen","Tyrion Lannister","Arya Stark","Sansa Stark","Cersei Lannister","Jaime Lannister","Bran Stark","Theon Greyjoy","Sandor Clegane"
]

#with open("character_list","r", newline ="") as file:
#readline(character_list.txt)

f = open("character_list.txt", "r")
print(f.readline())
