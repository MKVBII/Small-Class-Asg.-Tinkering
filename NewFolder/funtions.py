print('Initial global namespace: ')
print(globals())

my_var = "This is a variable"
print('\nCreated new variable')
print(globals())

def my_func():
    pass

print('\nCreated new function')
print(globals())


def display(product, options=[]):
    if 'monitor' in product:
        options.append('HDMI')


    print(product, options)


display('Acer monitor')
display('Samsung monitor')

num_list = [ 3, 8, 5, 15, 12, 32, 45 ]
for index, value in enumerate(num_list):
    if index > 0:
        if value < num_list[index-1]:
            print('*', end='')
    print(value, end=' ')

