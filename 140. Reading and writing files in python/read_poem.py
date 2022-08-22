jabber = open('Jabberwocky.txt', 'r')

for line in jabber:
    # print(line, end='')
    # print(line.strip(), end='')  # it will appear as one line
    print(line.strip())  # not included: spaces, tab
    # print(len(line))

jabber.close()
