import sys


def multi_arguments():
    arguments = sys.argv
    print("Параметры командной строки: ")
    for arg in arguments:
        print(arg)


multi_arguments()