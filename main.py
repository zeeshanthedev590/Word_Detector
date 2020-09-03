import os


find = input("Enter A Word You Want To Find : ")
def isDetected(filename):
    with open(filename,'r') as f:
       file_Content =  f.read()
       if find in file_Content.lower():
           return True

       else:
         return False  



# ---------------------------------------#    



# Main Function


if __name__ == "__main__":
    contents = os.listdir()
    for item in contents:
        if item.endswith('txt'):
            print(f"Detecting {find} in {item}")
            flag =  isDetected(item)
            if flag:
                print(f"{find} found in {item}" )

            else:
                print(f"{find} not Found")    