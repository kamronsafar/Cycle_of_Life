import time

try:
    a = "birth"
    print("You have come into existence.")

    if a == "birth":
        while True:
            m = input('Do you want to gain knowledge? (y/n): ')

            if m == "y":
                print("There is a guarantee that your life will be better.")
                print("You have spent 25 years of your life on education.")

                s = input("Do you want to continue with your life? (y/n): ")
                time.sleep(3)
                if s == 'y':
                    print("Congratulations, you have started a family and got a job.")
                    time.sleep(5)
                    print("You have spent another 35/45 years working for the government. Well done.")
                    time.sleep(3)
                    d = input(
                        "Congratulations, you have lived for 60 / 70 years. \n Do you want to continue the game? (y/n): ")

                    if d == 'y':
                        print("Congratulations, you have lived an amazing life and now you can wait for death.")

                        for i in range(11):
                            print(i)
                            time.sleep(1)
                        print("You have died.")
                        break
                    elif d == "n":
                        print("You ended your own life.")
                        time.sleep(3)
                        break
                elif s == "n":
                    time.sleep(2)
                    print("Congratulations, after 25 years of education, you have died.")
                    break

            elif m == "n":
                print("You are nothing in life.")
                print("And you will leave life in 5 seconds.")
                time.sleep(5)
                print("Game over.")
                break

except:
    print("Congratulations, you have left life immediately.")
