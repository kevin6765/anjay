matriks = []
y = 0

# Matriks 1
for x in range (0,3):
    print(f"Baris ke-{x+1}")
    a = []
    while y < 1:
        a.append(int(input("Data : ")))
        y = y + 1
    matriks.append(a)
    y = 0
    x = x + 1

# Mencetak
for a in matriks:
    print(a)
print()

matriks2 = []
i = 0
j = 0

#Matriks 2
while i < 3:
    print(f"Baris ke-{i+1}")
    b = []
    while j < 1:
        b.append(int(input("Data : ")))
        j = j + 1
    matriks2.append(b)
    j = 0
    i = i + 1

# Mencetak
for b in matriks2:
    print(b)
print()

# # operasi A + B
c = [
    [0],
    [0],
    [0]
]
for i in range (len(matriks)):
    for j in range (len(matriks[0])):
        c [i][j]= matriks[i][j] + matriks2[i][j]

for k in c:
    print(k)
