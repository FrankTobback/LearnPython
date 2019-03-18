# ONE WAY TO OPEN READ AND CLOSE A FILE
# ipsum_file = open('files/ipsum.txt')
#
#
# # #Reading file using For loop
# # for line in ipsum_file:
# #     print(line.rstrip())
#
#
# # #reset cursor in the text file to read it again using seek()
# # ipsum_file.seek(0)
# #
# # lines = ipsum_file.readlines()
# # print(lines)
#
#
# #starting from the 50th character and read 100 characters after that
# ipsum_file.seek(50)
# file_text = ipsum_file.read(100)
# print(file_text)
#
#
# ipsum_file.close()


#ANOTHER WAY TO OPEN READ A FILE, DOESN'T REQUIRE CLOSING THE FILE
def sequence_filter(line):
    return '>' not in line

with open('files/dna_sequence.txt') as dna_file:
    lines = dna_file.readlines()
    print(list(filter(sequence_filter, lines)))
