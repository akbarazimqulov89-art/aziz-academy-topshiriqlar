# O'rtacha hosili
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

sonlar = [a, b, c, d, e]

sonlar.remove(max(sonlar))
sonlar.remove(min(sonlar))

print(sum(sonlar) // 3)