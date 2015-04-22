import random

## Yes i know.. I did not do the comments and docstring. I will do it, i promise.

def code_mangler(file_name):
    '''
    '''
    x = []
    return_str = []
    # Opens the given file
    file = open(str(file_name), 'r')
    # Read the file informations/ read the codes
    file_inf = file.readlines()
    i = 0
    for each in file_inf:
        if (each[:3] == 'def'):
            x.append(file_inf[i].replace('\n', ''))
            i += 1
        elif (each[:5] == 'class'):
            x.append(file_inf[i].replace('\n', ''))
            i += 1
        elif (each[0] == ' '):
            new_str = each
            while (new_str[0] == ' '):
                new_str = new_str[1:]
            x.append(str(new_str))
            i += 1
        else:
            x.append(str(each))
            i += 1
    i = 0
    for each_str in x:
        new_str = x[i]
        x.remove(new_str)
        while new_str in x:
            x.remove(new_str)
        return_str.insert(random.randint(0, len(x) - 1), new_str)
        i += 1
    fx = open('code_mangled.txt', 'w')
    for each in return_str:
        fx.write(str(each) + '\n')
    fx.close()   
    # Safely close the opened file.
    file.close()

if (__name__ == '__main__'):
    # Get the user defined file named.
    print('What file name would you like to open?')
    print('For example "my_file.txt"')
    file_name = input('>>> ')
    code_mangler(file_name)
