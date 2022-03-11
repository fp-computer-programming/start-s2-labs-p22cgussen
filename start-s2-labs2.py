# Author: CCG 3/10/22

last_initials = ["B", "D", "H", "E", "G", "G", "H", "R", "M", "L", "I", "I", "N", "N", "O", "P", "P", "X", "T", "S", "S", "P"]

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]
initial_numb = 0

for row_numb, row in enumerate(rows): # get into nested lists
    for name_numb, name in enumerate(row): # get each name
        full_name = rows[row_numb][name_numb] # set varible for each name
        full_name += (" " + last_initials[initial_numb] + ".") # add the last initial for each name and a period
        rows[row_numb][name_numb] = full_name # replace each name with the full name
        initial_numb +=1 # make sure everyone gets their own last initials

print(rows)
