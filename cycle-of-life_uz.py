import time

try:
    a = "tug'ilish"
    print("Siz hayotga keldingiz.")

    if a == "tug'ilish":
        while True:
            m = input('Bilim olishni xohlaysizmi? (y/n): ')

            if m == "y":
                print("Hayotingiz yaxshiroq bo'lishiga kafolat mavjud.")
                time.sleep(2)
                print("Siz 25 yil hayotingizni ta'lim olishga sarfladingiz.")

                s = input("Hayotingizni davom ettirishni xohlaysizmi? (y/n): ")
                time.sleep(3)
                if s == 'y':
                    print("Tabriklaymiz, siz oila qurdingiz va ishga kirdingiz.")
                    time.sleep(5)
                    print("Siz yana 35/45 yil davlatga ishladingiz. Barakalla.")
                    time.sleep(3)
                    d = input(
                        "Tabriklaymiz, siz hayotingizni 60 / 70 yilini tugatdingiz. \n O'yinni davom ettirmoqchimisiz? (y/n): ")

                    if d == 'y':
                        print(
                            "Tabriklaymiz, siz hayotingizni judayam ajoyib o'tkazdingiz va o'limingizni kutishingiz mumkin."
                        )

                        for i in range(11):
                            print(i)
                            time.sleep(1)
                        print("Siz o'ldingiz.")
                        break
                    elif d == "n":
                        print("Siz o'zizi o'ldirdiz.")
                        time.sleep(3)
                        break
                elif s == "n":
                    time.sleep(2)
                    print("Tabriklaymiz, 25 yil ta'lim va shu bilan o'ldiz.")
                    break

            elif m == "n":
                print("Siz hayotda hech kimsiz.")
                print("Va siz 5 soniyadan keyin hayotdan tark etasiz.")
                time.sleep(5)
                print("O'yin tugadi.")
                break

except:
    print("Tabriklaymiz, siz srazi hayotdan tark etdingiz.")
