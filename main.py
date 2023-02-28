import os

#Reads the FASTQ file
def readFile(path):
    verifyFile(path)
    sequences = []
    qualities = []
    filename = os.path.basename(path)
    with open(filename) as fh:
        while True:
            fh.readline() # skip name line
            seq = fh.readline().rstrip() # read base sequence
            if len(seq) == 0:
                break
            sequences.append(seq)
    return sequences

# checks that the path entered exists and it is a valid FASTQ file
def verifyFile(path):
    if not os.path.exists(path):
        raise FileNotFoundError
    root, ext = os.path.splitext(path)
    if not(ext == '.fastq' or ext == '.fq'):
        print("Not correct file type")

# Counts the number of sequences in a file
def countSeq():
    #TODO count number of sequences
    return

# counts the number of nucleotides in a file
def countNuc():
    #TODO count number of nucleotides
    return

def gzip():
    #TODO add gzip compatability
    return


if __name__ == '__main__':
    print("Welcome to the FASTQ file reader \n")
    path = input("Enter the file path: ")
    readFile(path)
    print("To count the number of sequences press 'S' \n")
    print("To count the number of nucleotides press 'N' \n")
    request = input()
    if request == 'S' or request == 's':
        print("Counting the number of sequences ... \n")
    elif request == 'n' or request == 'N':
        print("Counting the number of nucleotides ... \n")




