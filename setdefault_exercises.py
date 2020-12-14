#1 using setdefault method to get values from keys
def set_default1():
    
    dict_1 = {"fruit1" : "apple" , "fruit2" : "mango"}
    
    print(dict_1.setdefault('fruit1'))
    print(dict_1)

set_default1()

#2
def set_default2():
    
    dict_2 = {
        "name" : "vishwanath anand",
        "occupation" : "chess GM"
        }
    
    print(dict_2.setdefault('name'))

set_default2()

#3 here when we try print the key which is not present in the dictionary/
#it shows none and the key is added in the original dictionary with the value none
def set_default3():
    
    dict_3 = {
        "name" : "vishwanath anand",
        "occupation" : "chess GM"
        }
    
    print(dict_3.setdefault('name1'))
    print(dict_3)

set_default3()

#4 here i have tried to a value to the new key using setdefault method
def set_default4():

    dict_4 = {
        "name" : "adhiban bhaskaran",
        "occupation" : "Chess gm",
        "Rank" : "india no.4"
        }
    
    print(dict_4.setdefault('rating' , '2607'))
    print(dict_4)

set_default4()

#5
def set_default5():

    dict_5 = {
        "name" : "vidit gujrathi",
        "occupation" : "Chess gm",
        "Rank" : "india no.3"
        }
    
    print(dict_5.setdefault('rating' , '2725'))
    print(dict_5)

set_default5()
    
#6
def set_default6():

    dict_6 = {
        "name" : "anish giri",
        "occupation" : "Chess gm",
        "Rank" : "world no.10"
        }
    
    print(dict_6.setdefault('rating' , '2780'))
    print(dict_6)

set_default6()

#7
def set_default7():

    dict_7 = {
        "name" : "magnus carksen",
        "occupation" : "Chess gm",
        "Rank" : "world no.1"
        }
    
    print(dict_7.setdefault('rating' , '2874'))
    print(dict_7)

set_default7()

#8
def set_default8():

    dict_8 = {
        "name" : "hikaru nakamura",
        "occupation" : "Chess gm",
        "Rank" : "world no.3"
        }
    
    print(dict_8.setdefault('rating' , '2841'))
    print(dict_8)

set_default8()

#9
def set_default9():

    dict_9 = {
        "name" : "samay raina",
        "occupation" : "Chess bm",
        "Rank" : "india no.10,000"
        }
    
    print(dict_9.setdefault('rating' , '1500'))
    print(dict_9)

set_default9()

#10
def set_default10():

    dict_10 = {
        "name" : "audi",
        "machine" : "car",
        "Rank" : "world no.3"
        }
    
    print(dict_10.setdefault('price' , 'somelakshs'))
    print(dict_10)

set_default10()



