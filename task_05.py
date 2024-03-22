# 1. Обов'язковий параметр
def text1(text):
    print(text)


# 2. Необов'язковий параметр
def text2(text, reverse=False):
    if reverse:
        text = text[::-1]
    print(text)


# 3. *args
def text3(text, *add_text, reverse=False):
    if reverse:
        text = text[::-1]

    for new_text in add_text:
        text += new_text
    print(text)


# 4. **kwargs
def process_text(text, *add_text, reverse=False, **kwargs):
    separator = kwargs["separator"]
    if reverse:
        text = text[::-1]

    for new_text in add_text:
        if separator:
            text += separator
        text += new_text
    print(text)


text1("Простая строка")
# Простая строка

text2("строка", reverse=True)
# акортс

text3("строка", "строка2", "строка3")
# Простая строка строка 2 строка 3

process_text("строка", "строка2", "строка3", separator="--", uppercase=True)
#строка--строка2--строка3

