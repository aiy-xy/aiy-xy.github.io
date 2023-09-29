import random

# function to convert string to list of numbers
def string_to_nums(text):
    return [ord(c) for c in text]

# function to convert list of numbers to string
def nums_to_string(nums):
    return ''.join([chr(n) for n in nums])

key = random.randint(1, 9)
print (key)


def ROMEO():
    print("Which message to send?")
    message = input()
    nums = string_to_nums(message)
    encrypted_nums = [num*key for num in nums]
    print(f"Output1: {nums}")
    print ("E= ")
    print (encrypted_nums)

    received_input = input("Now insert the numbers received from your friend: ").rstrip(',')
    received_nums = list(map(int, received_input.split(',')))
    decrypted_nums = [int(num/key) if num%key == 0 else num/key for num in received_nums]
    print("Output2:", decrypted_nums)
    print ("Send to your friend")

def JULIET():          #756, 777, 826, 707
# Step D2: Receive numbers from friend
    received_input = input("Now insert the numbers received from your friend: ").rstrip(',')
    received_nums = list(map(int, received_input.split(',')))

    encrypted_nums = [num * key for num in received_nums]

    print("Output-1:", encrypted_nums)
    print("Now send them back to your friend.")

    received_input = input("Now insert the numbers received from your friend: ").rstrip(',')
    received_nums = list(map(int, received_input.split(',')))
    decrypted_nums = [int(num/key) if num%key == 0 else num/key for num in received_nums]
    print("Output2:", decrypted_nums)
    decrypted_message = nums_to_string(decrypted_nums)
    print(f"Decrypted message: {decrypted_message}")


print("If you are sending type ROMEO")
print("If you are receiving, type JULIET")
option = input()
if option == "ROMEO":
    ROMEO()
elif option == "JULIET":
    JULIET()
else:
    print("Invalid option, please try again.")
