total_poin = 0
rata2Poin = 0
n = int(input("Jumlah pertandingan? "))
for i in range(n):
    i += 1
    poin = input(f"poin pertandingan ke-{i} : ")
    if poin == "W":
        total_poin += 3
    elif poin == "D":
        total_poin += 1
    elif poin == "L":
        total_poin += 0
    rata2Poin = total_poin / n
print("Total poin adalah:", total_poin)
print("Rata-rata poin adalah:" , rata2Poin)