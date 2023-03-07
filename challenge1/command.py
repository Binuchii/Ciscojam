
def hello(message):
    # When this command is used, everything after the word "hello" in the message will be sent to this function.
    # Example: "@Jam hello Ronan" -> this function receivces "Ronan" as the messsage.
    #
    # Your job is to process the message so that this function returns the correct outputs for challenge 1.
    # (for now, it just echoes back the same message)

    user_input = input("Enter something, could be your name: ")
    print(user_input)
    message_length = len(user_input)

    if message_length == 0:
        message = "Hello, Cisco"
        return message
    else:
        message = 'Hello, ' + user_input + '!'
        return message
