with open('Jabberwocky.txt', 'r') as jabber:
    for line in jabber:
        print(line.rstrip())  # line.lstrip()
