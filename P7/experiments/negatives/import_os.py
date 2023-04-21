import os

directory = "./images"

i=1

for filename in os.listdir(directory):
    
    new_filename = 'image_00' + str(i) + (".jpg")
    i+=1

    # Create the full path for the old and new file names
    old_path = os.path.join(directory, filename)
    new_path = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(old_path, new_path)