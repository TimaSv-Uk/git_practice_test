def add(a: int, b: int):
    return a + b


def look_and_say(data:str):
    newString = ""
    prev = ""
    sameCharInRow = -1

    for i in data:
        if i == prev:
            sameCharInRow += 1
        else:
            if sameCharInRow > 0:
                newString += str(sameCharInRow) + prev
            prev = i
            sameCharInRow = 1
    newString +=  str(sameCharInRow) + prev
    return newString

def main():
    data = "1113222113"
    print(look_and_say(data))
    add(1, 2)


if __name__ == "__main__":
    main()
