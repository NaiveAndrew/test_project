
#Рекурсивная функция для разворота строки

def reverse_str(string):
   if len(string) == 0:
       return ''
   else:
       return string[-1] + reverse_str(string[:-1])

print (reverse_str('test'))  # tset

print (reverse_str("python"))