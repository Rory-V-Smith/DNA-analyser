import sys   # sys.argv
import csv   # reader (for lists); dictreader (for dictionaries)
import re


def main():

    # if incorrect argc - print error message
    if len(sys.argv) != 3:
        print("Usage: incorrect usage of command-line arguments ")
        sys.exit()

    # main program:
    # first command line argument name of CSV file of individuals
    # second command line argument DNA sequence
    database = sys.argv[1]
    sample = sys.argv[2]
    header = []
    STR = []

    # open CSV file containing STR sequences for individuals
    with open(database, newline="") as csvfile:
        reader = csv.reader(csvfile)
        line = 0
        for row in reader:
            if line == 0:
                header = row
                header.pop(0)   # remove name item
                line += 1
            else:
                STR.append(row)
            
#        x = next(reader)
#        STR = [None] * len(x)
#        for index, x in enumerate(x):
#            STR[index] = x

    # open DNA sequence and read contents onto memory
    with open(sample, "r") as textfile:
        DNA = textfile.read()

    # dictionary to store STR count
    STR_count = {}

    # make dictionary of STR count for DNA sample
    for i in range(len(header)):
        STR_count[header[i]] = count(DNA, header[i])
    
    match = False
    # compare STR count with database
    for i in range(len(STR)):
        counter = 0
        for j in range(len(STR[i])):
            if j != 0:
                if int(STR[i][j]) == int(STR_count.get(header[j - 1])):  # if match
                    counter += 1
                
        if counter == len(header):
            match = True
            name = (STR[i][0]) 
            print(name)  # name
         
    if match == False:
        print("No match")
        
        
def count(DNA, STR):
    max = 0
    count = 0
    for i in range(len(DNA)):
        j = i + len(STR)    # or j = len(STR)??
        while count > 0:
            count -= 1
            continue
        # if STR match
        if DNA[i:j] == STR:
            # if match is sequential:
            while DNA[i - len(STR): i] == DNA[i: i + len(STR)]:  # STR
                count += 1
                i += len(STR)
            if count > max:
                max = count
    return max + 1
    

"""
def count(s, c):
    p = rf'({c})\1*'
    pattern = re.compile(p)
    match = [match for match in pattern.finditer(s)]
    print(match)
    max = 0
    for i in range(len(match)):
        print(max)
        if match[i].group().count(c) > max:
            max = match[i].group().count(c)
    return str(max)

"""

if __name__ == "__main__":
    main()