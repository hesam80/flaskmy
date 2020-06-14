import os, re, shutil


def modify_metatag():
    """
    REMOVE PREVIOUS METADATA AND EMBED NEW ONE
    """
    USErR_NAME = input("Enter USER name: ")
    print(len(USErR_NAME))
    
    for i in range(len(USErR_NAME)):
        
            i = str(i)
            i += USErR_NAME
            USErR+=USErR_NAME
            # Renaming file name
            # INSTEAD OF SPACE IN USER NAME WE SHOULD HAVE DASH.
            #USErR_NAME.append(i)
            #path = USER + "-" + i + ".mp3"
            #i+= USER
            #os.rename(i + ".mp3", path)
            # Remove previous metadata
            print(i)
            print(USErR)
            #print(path)
        
           #print("nokm")
   
    
    
modify_metatag()