def frequency(FileName):
    Alpha='abcdefghijklmnopqrstuvwxyz'
    with open(FileName, 'r') as file:
        data = file.read()
        for char in Alpha:
            print('Frequency of',char,'is:',data.count(char))

frequency('abc.txt')