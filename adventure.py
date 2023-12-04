import json
import sys

def room(id):
    #Command for character existing in a room 
    #   Make recursive
    #       -Exit called
    #       -Game finished

    # Printing out room information
    for item in id:
        if isinstance(id[item], dict):
            print("Go: ")
            for key in id[item]:
                print(key)

            print("\n")
        
        elif item == "name": 
            print("> ", id[item], "\n")

        elif isinstance(id[item], list):
            for key in id[item]:
                if key == "nan":
                    pass
                else:
                    print(key)

        else:
            print(id[item], "\n")

    
    # Handling Player Actions
    action = input()
    if action[:2] == "Go":
        if action[-4:] in id["exits"].keys():
            room(data[id["exits"][action[-4:]]])
        elif action[-5:] in id["exits"].keys():
            room(data[id["exits"][action[-5:]]])
        else:
            print("Please enter a valid direction/ make sure direction is all lower case")
            room(id)

    elif action == "Look":
        room(id)

    elif action == "Help":
        help()
        room(id)

    elif action == "Quit":
        print("Thank you for playing the game!")

    else: 
        print("Command unknown \n Please use 'Help' for a list of useful commands \n Also be sure to capitalise the first letter in all commands")
        help()
        room(id)

    return


def help():
    # EXTENSION
    #Show player list of commands
    print("The list of commands are as follows \n Go (north, south, east, or west) : Travel to a new room \n Look : reprints the room information \n Help : print out list of commands \n Quit : exits the game")
    return



if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf8") as map:
        data = json.load(map)
    room(data[0])
    