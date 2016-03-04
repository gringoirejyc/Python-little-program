import os

def rename_files():
    #find file name
   file_list = os.listdir(r"/Users/Ji/Documents/prank")
   #print(file_list)
   saved_path = os.getcwd()
   print(saved_path)
   os.chdir(r"/Users/Ji/Documents/prank")

    #rename file
   for file_name in file_list:
       os.rename(file_name,file_name.translate(None,"0123456789"))
   os.chdir(saved_path)

   
rename_files()
      
