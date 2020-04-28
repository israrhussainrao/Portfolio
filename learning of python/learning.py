# it is a simple car logic game 

command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("the car already started...")
        else:
            started = True
            hel = True
            print("car started")
    elif command == "stop":
        if not started:
            print("the car already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print('''
start - car start
stop - car stop
quit - to quit
        ''')
    elif command == "quit":
        break
    else:
        print("i don't understand write 'help' to understand the command")
