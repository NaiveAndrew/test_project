
my_file = open('namefile.txt','w')
my_file.write('something that i am printing on my keyboard right now ')
print('I am writing smth in file with function print', file=my_file)
my_file = open('namefile.txt','r')
print (my_file.read())