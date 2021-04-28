# Program to encode words into military words

mil_dict = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf',
            'H': 'Hotel', 'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November',
            'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
            'V': 'Victor', 'W': 'Whiskey', 'X': 'X-Ray', 'Y': 'Yankee', 'Z': 'Zulu'
            }
key = mil_dict.keys()


def encoder(s):
    encode_str = ''
    for i in s:
        if i in key:
            encode_str = encode_str + mil_dict[i] + " "
    return encode_str


s = input("Enter text to encoded: ")
s = s.upper()
print(encoder(s))
