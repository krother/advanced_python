
# Example for neat program structure

def get_name():
    """Reads a name. Returns a string."""
    name = raw_input('Please enter your name: ')
    return name


def make_message(name):
    """Constructs a welcoming message. Input: string, Output:string."""
    message = "Good morning, %s! Nice to see you."%name
    return message


def print_message(msg):
    """Writes a message to screen. Input: string."""
    print msg


# main program:
if __name__ == '__main__':
    name = get_name()
    msg  = make_message(name)
    print_message(msg)

    
