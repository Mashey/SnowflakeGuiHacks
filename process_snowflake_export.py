# Using readline()
file1 = open('data/grants_to_roles.csv', 'r')
count = 0

# clear previous file
open('data/grants_to_roles.json', 'w')

with open('data/grants_to_roles.json', 'a') as file2:
    while True:
        count += 1
    
        # Get next line from file
        line = file1.readline()
    
        # if line is empty
        # end of file is reached
        if not line:
            file2.write(']')
            break
        
        if count == 1:
            file2.write('[')
            continue

        line = line.replace('"{', '{')
        line = line.replace('""', '"')
        line = line.replace('}"', '},')
        file2.write(line)

file1.close()