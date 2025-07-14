text = ["apple", "34", "banana", "100", "abc", "75"]

def faqat_sonlar(item):
    return item.isdigit()

natija = list(filter(faqat_sonlar,text))
print(natija)