from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

#Get the password
userinfo = config_object["USERINFO"]
print("Username is {} and Password is {}".format(userinfo["username"],userinfo['password']))
