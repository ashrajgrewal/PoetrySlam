#Ashraj Grewal PoetrySlam CS1.0
import random
def get_file_lines(filename):
    poem_file = open(filename, "r")
    poem_read = poem_file.readlines()
    return poem_read
poem_lines = get_file_lines("poem.txt")
print(poem_lines)

def lines_printed_backwards(lines_list):
        for i in reversed(lines_list):
            print(i)
lines_printed_backwards(poem_lines)

def lines_printed_random(lines_list):
    for line in lines_list:
        index = random.randint(0,len(lines_list)-1)
        print(lines_list[index])
lines_printed_random(poem_lines)
print("\n")

def lines_printed_custom(lines_list):
    for count, line in enumerate(lines_list, start=1):
        if count % 2 == 0:
            print(line)
lines_printed_custom(poem_lines)
#This cutsom code is to print every other line in the poem!