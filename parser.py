import sys

keymap = {59: ",", 60: ".", 61: "/", 47: ";", 48: "'", 34: "[", 35: "]", 51: "\\", 20: "-", 21: "=", 23: "", 64: "", 10: '1', 11: '2', 12: '3', 13: '4', 14: '5', 15: '6', 16: '7', 17: '8', 18: '9', 19: '0', 65: " ", 105: '[RCTRL]', 37: '[LCTRL]', 36: '[RETURN]', 38: 'a', 56: 'b', 54: 'c', 40: 'd', 26: 'e', 41: 'f', 42: 'g', 43: 'h', 31: 'i', 44: 'j', 45: 'k', 46: 'l', 58: 'm', 57: 'n', 32: 'o', 33: 'p', 24: 'q', 27: 'r', 39: 's', 28: 't', 30: 'u', 55: 'v', 25: 'w', 53: 'x', 29: 'y', 52: 'z'}
symbols = {10: '!', 11: '@', 12: '#', 13: '$', 14: '%', 15: '^', 16: '&', 17: '*', 18: '(', 19: ')', 59: "<", 60: ">", 61: "?",  47: ":", 48: "\"", 34: "{", 35: "}", 51: "|", 20: "_", 21: "+" }

if (len(sys.argv) == 1):
    print("Need a file to parse. Syntax: python3 parser.py <log_file>")
    sys.exit()

file = sys.argv[1]
f = open(file, "r")
line = f.readline()

message = ""
upperCase = False

while line:
    line = line.strip()
    x = line.split(" ")
    key = int(x[len(x)-1])
    if(x[1] == "press"):
        if key in [66,50,62]:
            upperCase = not upperCase
        elif key == 22:
            message = message[:-1]
        else:
            if upperCase:
                if (key >= 10 and key <= 21) or (key in [34,35,47,48,51,59,60,61]):
                    message += symbols.get(key,'')
                else:
                    message += keymap.get(key,'').upper()
            else:
                message += keymap.get(key,'')

    elif(x[1] == "release"):
        if key == 50 or key == 62:
            upperCase = not upperCase


    line = f.readline()

print(message)
