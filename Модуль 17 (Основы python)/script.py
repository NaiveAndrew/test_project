import requests
import bs4
counter = 0
result = []
while counter < 30:
    if counter%2 == 1:
        result.append(str(counter))
    else:
        pass
    counter += 1
print (", ".join(result))
