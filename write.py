with open('files/write.txt', 'w') as write_file:
    write_file.write('Hey ninjas, Python is awesome')

# If you want to write in the file again after a chunk of code use 'a' wich means it adds extra text
# use \n (new line character) to jump to a new line
with open('files/write.txt', 'a') as write_file:
    write_file.write('\nI love it so much , I dream in Python')

quotes = [
    '\nI can resist everything except temptation',
    '\nWe are all in the gutter, but some of us are looking at the stars',
    '\nAlways forgive your enemies - nothing annoys them so much'
]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)
