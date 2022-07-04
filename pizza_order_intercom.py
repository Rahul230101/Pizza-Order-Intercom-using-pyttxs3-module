# PROJECT 3 PIZZA ORDERS WITH PYTTSX3
import pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Welcome to the Pizza Orders")
speak("Welcome to the Pizza Orders and I am Zira How can I help you ?")
speak("Enter the size of the Pizzas")
size = input("Enter a Size: S, M or L ").lower()
speak("If you want to add pepperoni to pizza Press Y or else Press N ")
add_pepperoni = input("Add pepperoni Press: Y or N ").lower()
speak("If you want extra Cheese Press Y else Press N")
extra_cheese = input("Want extra cheese: Press Y or N ").lower()
speak("What's your name Sir/madam")
user = input("Your name: ")

if size == 's':
    bill = 15
    if add_pepperoni == 'y':
        addbill = 2
    else:
        addbill = 0
    if extra_cheese == 'y':
        extbill = 1
    else:
        extbill = 0 
    total_bill = bill + addbill + extbill
    speak(f"{user} Your order was Small size pizza and your final bill is Rupees{total_bill}")
    print(f"{user} final bill is Rupees {total_bill}")
    

if size == 'm':
    bill = 20
    if add_pepperoni == 'y':
        addbill = 3
    else:
        addbill = 0
    if extra_cheese == 'y':
        extbill = 1
    else:
        extbill = 0 
    total_bill = bill + addbill + extbill
    speak(f"{user} Your order was medium size pizza and Your final bill is Rupees{total_bill}")
    print(f"{user} Your final bill is Rupees {total_bill}")


if size == 'l':
    bill = 25
    if add_pepperoni == 'y':
        addbill = 3
    else:
        addbill = 0
    if extra_cheese == 'y':
        extbill = 1
    else:
        extbill = 0 
    total_bill = bill + addbill + extbill
    speak(f"{user}Your order was large size pizza and Your final bill is Rupees{total_bill}")
    print(f"{user}Your final bill is Rupees {total_bill}")