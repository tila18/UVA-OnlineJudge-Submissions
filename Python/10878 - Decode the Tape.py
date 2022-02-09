input_message = []
output_message = []
tapestarted = False;

while True:
    letter = input()
    if letter == '___________':
       if tapestarted:
            break
       else:
           tapestarted = True
    else:
        input_message.append(letter)

for x in input_message:
    newchar = input_message[input_message.index(x)]

    # convert string to binary number string
    newchar = newchar.translate({ord(i): None for i in '|.'})
    newchar = newchar.replace(' ', '0')
    newchar = newchar.replace('o', '1')

    # convert binary to decimal
    newchar = int(newchar, 2)
    # convert decimal to ASCII
    newchar = chr(newchar)

    output_message.append(newchar)
    

for c in output_message:
    print(c, end='')