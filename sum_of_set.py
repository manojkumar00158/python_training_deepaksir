def sum_two_iterables():
   set1 = set(input('enter number: ').split(' '))
   print(set1)
   total = 0
   for i in set1:
       total += int(i)
   print(total)

if __name__ == '__main__':
        sum_two_iterables()
