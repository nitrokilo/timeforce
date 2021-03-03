import time
import playsound


# convert seconds to minutes
def sec_min(val):
    val = int(val)
    new_val = val * 60
    return new_val

# Function to Convert time to second minute hour format
def convert(val):
    val = int(val)
    # val1 = sec_min(val)
    ty_res = time.gmtime(val)
    res = time.strftime("%H:%M:%S", ty_res)
    print(res)




# Introductions; beta version 0.91
print("Time for Timeforce")
print("Beta Version 0.91")
print("Ifeoluwa Adeosun 2021 All Rights Reserved")
print("Sounds provided by Ryan Lohse ; rdlohse@gmail.com")


# Main "Timeforce" class creation
class TimeForce:
    def __init__(self, hot_time, chill_time, ):
        self.hot_time = hot_time
        self.chill_time = chill_time

    # First Countdown; named "countdown1"
    @staticmethod
    def countdown1(hot_time):
        x = int(hot_time)
        while -1 < x:
            convert(x)
            time.sleep(1)
            x -= 1
            # playsound at end of countdown
            if x == -1:
                # initialize "wavfile" as sound for end of first timer
                wavfile = 'sounds/1.wav'
                playsound.playsound(wavfile)

    # Second Countdown; named "countdown2"
    @staticmethod
    def countdown2(chill_time):
        x = int(chill_time)
        while -1 < x:
            convert(x)
            time.sleep(1)
            x -= 1
            if x == -1:
                # initialize "wavfile" as sound for end of first timer
                wavfile = 'sounds/2.wav'
                playsound.playsound(wavfile)


# create function named "main" to allow reinitialization of variables
def main():
    # use global keyword to allow access outside of function
    global hot, chill, rotations, r1, hot1 , chill1
    hot = input("Input hot time")
    hot1 = str(hot)
    hot = sec_min(hot)
    chill = input("Input chill time")
    chill1 = str(chill)
    chill = sec_min(chill)
    rotations = input("Input number of rotations")

    # Insertion of variables into class
    r1 = TimeForce(hot, chill)


def timer():
    # confirmation message
    c = input("You've set your timer hot time for " + hot1 + " minutes, its chill time for " + chill1 + " minutes, "
                                                                                                        "with " +
              str(rotations) + " Rotations. Press y to start or n to restart")
    # if yes action
    if c == "y":
        repeat = int(rotations)
        while repeat > 0:
            r1.countdown1(hot)
            r1.countdown2(chill)
            repeat -= 1
            if repeat == 0:
                # repeat message or allow reinitialization
                k = input("Run it back? y for yes, n for no")
                if k == "y":
                    timer()
                if k == "n":
                    print("Done!")
                    print("Thank you for using Timeforce")
                    print("This program will close in")
                    z = 5
                    while -1 < z:
                        print(z)
                        time.sleep(1)
                        z -= 1
                        if z == 0:
                            exit()

                else:
                    print("Invalid input")
                    timer()
    if c == "n":
        main()
        timer()
    else:
        print("Invalid input")
        timer()


main()
timer()
