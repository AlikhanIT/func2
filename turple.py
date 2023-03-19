translit_tuple = (
    ('а', 'a'), ('ә', 'ä'), ('б', 'b'), ('в', 'v'), ('г', 'g'), ('ғ', 'ğ'), ('д', 'd'),
    ('е', 'e'), ('ё', 'yo'), ('ж', 'j'), ('з', 'z'), ('и', 'i'), ('й', 'i'), ('к', 'k'),
    ('қ', 'q'), ('л', 'l'), ('м', 'm'), ('н', 'n'), ('ң', 'ñ'), ('о', 'o'), ('ө', 'ö'),
    ('п', 'p'), ('р', 'r'), ('с', 's'), ('т', 't'), ('у', 'u'), ('ұ', 'ū'), ('ү', 'ü'),
    ('ф', 'f'), ('х', 'h'), ('һ', 'h'), ('ц', 'ts'), ('ч', 'ch'), ('ш', 'ş'), ('щ', 'sh'),
    ('ъ', ''), ('ы', 'y'), ('і', 'i'), ('ь', ''), ('э', 'e'), ('ю', 'yu'), ('я', 'ya')
)

text = input("Введите текст на казахском языке: ")

translit_text = ''
for char in text:
    found = False
    for pair in translit_tuple:
        if pair[0] == char.lower():
            translit_text += pair[1]
            found = True
            break
    if not found:
        translit_text += char

print("Текст на латинице: ", translit_text)