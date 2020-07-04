# Here we are reading files
# f = open("../Exercise Files/inputFile.txt", 'r')
# for i in f:
#     LINE_SPLIT = i.split()
#     if LINE_SPLIT[2] == 'P':
#         print(i)
# f.close()

# Here we will write on files

f = open("../Exercise Files/inputFile.txt", 'r')
PASS_FILE = open("PassFile.txt", 'w')

for i in f:
    LINE_SPLIT = i.split()
    if LINE_SPLIT[2] == 'P':
        PASS_FILE.write(i)
PASS_FILE.close()
f.close()
