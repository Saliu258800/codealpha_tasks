def request_username():
    print("Please, what is your name?")
    name = input("Enter your name: ")
    return name
    
def request_userage():
    print("How old are you?")
    try:       
        age = int(input("Reply: "))
        return age
    except Exception as e:
        print("Next time, make sure to enter just a number.")
        
def mini_chat():
    response = input("Reply: ")

    if "Yes".lower() in response:
        print("Okay, what is your favorite color?")
        color = input("Reply: ")
        print(f"{color} is a very nice color")
    elif "No".lower() in response:
        print("Okay. No problem. Once again it was nice to meet you. Bye!")
        
        
def main():
    while True:
        print("Hi, I'm a mini ChatBot.")
        name = request_username()
        print(f"{name}, Nice to meet you!")
             
        age = request_userage()
        if age < 0:
            print("Negative can't be an age")
            continue 
        elif age >= 0 and age <= 12:
            print(f"{name}, you are a child.")
        elif age > 12 and age < 18:
            print(f"{name}, you are in your teens.")
        elif age >= 18:
            print(f"{name}, you are an adult.")
        
        print(f"May I ask about your favorite things, {name}?")
        
    
        mini_chat()
        break 
    
if __name__ == "__main__":
    main()