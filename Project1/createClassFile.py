import conditionGenerator
writefile = open("___________MAINCLASS_______________.class", mode="wb")


def create_magical_number():
    text = b'\xCA\xFE\xBA\xBE'
    # writefile.write(text)
    return text


if __name__ == '__main__':
    create_magical_number()
