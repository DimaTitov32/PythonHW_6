# Напишите программу, удаляющую из текста все слова, содержащие "абв".
def delete_abv(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text ='Ехал грека через реку,абв видит грека — в реке рак.Сунул грека рукуабв в реку, рак за абв руку греку — цап!' 

print(text)

print(delete_abv(text))