import os, re, shutil


def modify_metatag():
    """
    REMOVE PREVIOUS METADATA AND EMBED NEW ONE
    """
    QARI_NAME = input("Enter qari name: ")
    
    for i in range(len(QARI_NAME)):
        try:
            i = str(i)
            i += QARI_NAME
            QARI+=QARI_NAME
            # Renaming file name
            # INSTEAD OF SPACE IN QARI NAME WE SHOULD HAVE DASH.
            #QARI.append(i)
            path = QARI + "-" + i + ".mp3"
            #i+= QARI
            #os.rename(i + ".mp3", path)
            # Remove previous metadata
            print(i)
            print(QARI)
            print(path)
        except:
           print("nokm")
   
    
    
modify_metatag()