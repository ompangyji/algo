

for T in range(7, 201, +7):
    if T % 5 != 0:
        if(T > 195):
            print(T)
            break
        print(T, end = ',')
