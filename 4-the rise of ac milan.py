total_poin = 0
rata2Poin = 0
n = int(input("Jumlah pertandingan? "))
for i in range(n):
    i += 1
    poin = int(input(f"poin pertandingan ke-{i} : "))
    total_poin += poin
    rata2Poin = total_poin / n
print("Total poin adalah:", total_poin)
print("Rata-rata poin adalah:" , rata2Poin)
    