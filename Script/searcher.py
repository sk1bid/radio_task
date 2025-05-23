import sys

if len(sys.argv) != 3:
    print("Usage: python3 searcher.py <target_word> <filename>")
    sys.exit(1)

target_word = sys.argv[1]
filename = sys.argv[2]

f = open(filename, "r")
for line in f:
    if target_word in line:
        print(line.strip())