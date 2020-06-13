import os, re, shutil


def modify_metatag():
    """
    REMOVE PREVIOUS METADATA AND EMBED NEW ONE
    """
    USER_NAME = input("Enter USER name: ")
    
    for i in range(len(USER_NAME)):
        try:
            i = str(i)
            i += USER_NAME
            USER+=USER_NAME
            # Renaming file name
            # INSTEAD OF SPACE IN USER NAME WE SHOULD HAVE DASH.
            #USER.append(i)
            path = USER + "-" + i + ".mp3"
            #i+= USER
            #os.rename(i + ".mp3", path)
            # Remove previous metadata
            print(i)
            print(USER)
            print(path)
        except:
           print("nokm")
   
    
    
modify_metatag()