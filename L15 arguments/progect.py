def shutdown(user_input):
    user_input = user_input.lower()  # transforme en minuscules

    if user_input == "yes":
        print("shutting down")
    elif user_input == "no":
        print("abort shut down")
    else:
        print("sorry")


answer = input("Do you want to shut down the system? ")
shutdown(answer)
