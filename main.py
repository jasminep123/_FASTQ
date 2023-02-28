import os

#Reads the FASTQ file
def readFile(path):
    verifyFile(path)
    lines = []
    filename = os.path.basename(path)
    with open(filename) as fh:
        while True:
            line = fh.readline()# read base sequence
            if len(line) == 0:
                break
            lines.append(line)
    return lines

# checks that the path entered exists and it is a valid FASTQ file
def verifyFile(path):
    if not os.path.exists(path):
        raise FileNotFoundError
    root, ext = os.path.splitext(path)
    if not(ext == '.fastq' or ext == '.fq'):
        print("Not correct file type")

# Counts the number of sequences in a file
def countSeq(lines):
    numSeq = len(lines)/4
    print("number of Sequences: ", numSeq)


# counts the number of nucleotides in a file
def countNuc(lines):
    count = 0#
    lineNum = 1
    for line in lines:
        if lineNum %2 == 0 and lineNum%4 !=0:
            count += len(line.rstrip())
        lineNum += 1
    print("number of nucleotides: ", count)


    #TODO count number of nucleotides
    return

def gzip():
    #TODO add gzip compatability
    return


if __name__ == '__main__':
    print("Welcome to the FASTQ file reader \n")
    path = input("Enter the file path: ")
    lines = readFile(path)
    print("To count the number of sequences press 'S' \n")
    print("To count the number of nucleotides press 'N' \n")
    request = input()
    if request == 'S' or request == 's':
        print("Counting the number of sequences ... \n")
        countSeq(lines)
    elif request == 'n' or request == 'N':
        print("Counting the number of nucleotides ... \n")
        countNuc(lines)




