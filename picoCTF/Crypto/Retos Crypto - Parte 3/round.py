def decode(number):
    r = number % 37
    return r

def main():
    f = open("message.txt", "r", encoding="UTF-8")
    lst = f.read().split()
    # print(lst[0])

    dec_lst = []

    for i in range(len(lst)):
        dec_lst.append(decode(int(lst[i])))

    abc="abcdefghijklmnopqrstuvwxyz0123456789_"
    print(len(abc))
    print(dec_lst)
    for letter in dec_lst:
        print(abc[letter],end="")

if __name__ == '__main__':
    main()
