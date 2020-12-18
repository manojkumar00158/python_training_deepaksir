

from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

#Assume we need an object which holds userinfo we   
config_object["USERINFO"] = {
    
    'username': '******',
    'password': '*******'
}



#Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)

