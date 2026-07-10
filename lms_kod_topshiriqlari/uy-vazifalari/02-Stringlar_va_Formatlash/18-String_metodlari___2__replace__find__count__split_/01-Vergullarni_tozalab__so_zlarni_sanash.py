gap = input()

gap_vergulsiz = gap.replace(","," ")

sozlar = gap_vergulsiz.split()

yangi_gap = " ".join(sozlar)
print(yangi_gap)
print(len(sozlar))