row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure??")

X = int(position[0])#fila
Y = int(position[1])#columna

map[X - 1][Y - 1] = "X"

print(f"{row1}\n{row2}\n{row3}") 