import random

def get_character_count():
    n = input("How many characters will the password require?  ")
    n = int(n)
    return n

def get_special_character_count():
    n = input("How many special characters (!, @, #, ect) will this password require?  ")
    n = int(n)
    return n

def password_generator(total, special):
    value_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
    special_list = ["!","@","#","$","%","^","&","*","~","_","-"]
    password_list =[]

    count = 0

    while (count < total):
        
        while (count < special):
            password_list.append(random.choice(special_list))
            count = count + 1
        
        password_list.append(random.choice(value_list))
        count = count + 1
    
    password_list = (random.sample(password_list, len(password_list)))
    password_list = ''.join(password_list)
    
    return password_list

# Password Paramaters
total_count = get_character_count()
special_count = get_special_character_count()

# Generate Password
password = password_generator(total_count, special_count)

print()
print(password)