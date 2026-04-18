def top_unli(matn):
    unli_harflar = 'aeiouAEIOU'
    son = 0
    for harf in matn:
        if harf in unli_harflar:
            son += 1
    return son

matn = input("Matn kiriting: ")
print("Matndagi unli harflar soni:", top_unli(matn))
