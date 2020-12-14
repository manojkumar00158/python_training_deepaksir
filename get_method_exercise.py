#1.get method using keys to get values
def get_function():

    dict_1 = {"fruit1" : "apple" , "fruit2" : "mango"}

    print(dict_1.get("fruit1"))

get_function()

#2
def get_function2():

    dict_2 = {
        "name" : "vishwanath anand",
        "occupation" : "chess GM"
        }
    
    print(dict_2.get("name"))

get_function2()

#3if keys does not present in get method it gives output none
def get_function3():

    dict_3 = {
        "name" : "kiran",
        "occupation" : "IAS"
        }
    
    print(dict_3.get("name1"))

get_function3()

#4 if key does not present in get method we assign some value to it but it does/
#not change in original dictionary
def get_function4():

    dict_4 = {
        "a" : 1,
        "b" : 2,
        "c" : 3
        }
    
    print(dict_4.get("d","not found"))

get_function4()

#5
def get_function5():

    dict_5 = {
        "name" : "adhiban bhaskaran",
        "occupation" : "Chess gm",
        "Rank" : "india no.4"
        }
    
    print(dict_5.get("Rank"))

get_function5()


#6
def get_function6():

    dict_6 = {
        "apple" : 1,
        "banana" : 2,
        "custered apple" : 3
        }
    
    print(dict_6.get("donkey","not found"))

get_function6()


#7
def get_function7():

    dict_7 = {
        "apache" : 1,
        "honda" : 2,
        "chethak" : 3
        }
    
    print(dict_7.get("ferari","not found"))

get_function7()

#8
def get_function8():

    dict_8 = {
        "name" : "srinath narayan",
        "occupation" : "Chess gm",
        "Rank" : "india no.25"
        }
    
    print(dict_8.get("Rank"))

get_function8()


#9
def get_function9():

    dict_9 = {
        "name" : "durga sai",
        "occupation" : "IAS"
        }
    
    print(dict_9.get("name2"))

get_function9()

#10
def get_function10():

    dict_10 = {
        "name" : "dhoni",
        "occupation" : "batsman"
        }
    
    print(dict_10.get("name1"))

get_function10()







    
    





    
