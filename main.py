from pygame import mixer
import time
from datetime import datetime
import sys


def terminate():
    now1 = datetime.now()
    current_time = now1.strftime("%H:%M:%S")
    if current_time >= "24:0:0":
        sys.exit()


terminate()
print("\t\t\t\t\t\t\t\tWelcome Programmer!! Make yourself healthy")
initial1 = time.time()
i = 0
while i == 0:
    terminate()
    time.sleep(30*60)
    terminate()
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.play(-1)
    terminate()
    drank = input("Type drank if you have drank a glass of water: ")
    if drank == 'drank':
        mixer.music.stop()
        with open("water.txt", "a") as f:
            f.write("[" + str(datetime.now()) + "] You drank a glass of water\n")
        print("Your action is recorded in water.txt")
    terminate()
    mixer.music.load("eyes.mp3")
    mixer.music.play(-1)
    terminate()
    eyes = input("Type eyes done if you have done your eyes exercise: ")
    if eyes == 'eyes done':
        mixer.music.stop()
        with open("eyes.txt", "a") as f:
            f.write("[" + str(datetime.now()) + "] You have done the eyes exercise\n")
        print("Your action is recorded in eyes.txt")
    terminate()
    time.sleep(15*60)
    terminate()
    mixer.music.load("physical.mp3")
    mixer.music.play(-1)
    terminate()
    physical = input("Type workout done if you have done your physical exercise: ")
    if physical == 'workout done':
        mixer.music.stop()
        with open("physical.txt", "a") as f:
            f.write("[" + str(datetime.now()) + "] You have done the physical exercise\n")
        print("Your action is recorded in physical.txt")
    terminate()
