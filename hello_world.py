import pandas as pd
#import function as fn
from function import print_descending_number_list
#cosi ho creato una funzione nel file function e la importo con from 


print('hello world')
print('a second line')

for i in range(10):
    print(i, ':', i%2 == 0)

print(pd.DataFrame)

#fn.descending_number_list(3,8,2)
print_descending_number_list(3,8,2)

