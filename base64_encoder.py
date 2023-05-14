bin_to_character_table = {
    "000000": "A", "000001": "B", "000010": "C", "000011": "D",
    "000100": "E", "000101": "F", "000110": "G", "000111": "H",
    "001000": "I", "001001": "J", "001010": "K", "001011": "L",
    "001100": "M", "001101": "N", "001110": "O", "001111": "P",
    "010000": "Q", "010001": "R", "010010": "S", "010011": "T",
    "010100": "U", "010101": "V", "010110": "W", "010111": "X",
    "011000": "Y", "011001": "Z", "011010": "a", "011011": "b",
    "011100": "c", "011101": "d", "011110": "e", "011111": "f",
    "100000": "g", "100001": "h", "100010": "i", "100011": "j",
    "100100": "k", "100101": "l", "100110": "m", "100111": "n",
    "101000": "o", "101001": "p", "101010": "q", "101011": "r",
    "101100": "s", "101101": "t", "101110": "u", "101111": "v",
    "110000": "w", "110001": "x", "110010": "y", "110011": "z",
    "110100": "0", "110101": "1", "110110": "2", "110111": "3",
    "111000": "4", "111001": "5", "111010": "6", "111011": "7",
    "111100": "8", "111101": "9", "111110": "+", "111111": "/",
}

character_to_bin_table = {
    'A': '000000', 'B': '000001', 'C': '000010', 'D': '000011',
    'E': '000100', 'F': '000101', 'G': '000110', 'H': '000111',
    'I': '001000', 'J': '001001', 'K': '001010', 'L': '001011',
    'M': '001100', 'N': '001101', 'O': '001110', 'P': '001111',
    'Q': '010000', 'R': '010001', 'S': '010010', 'T': '010011',
    'U': '010100', 'V': '010101', 'W': '010110', 'X': '010111',
    'Y': '011000', 'Z': '011001', 'a': '011010', 'b': '011011',
    'c': '011100', 'd': '011101', 'e': '011110', 'f': '011111',
    'g': '100000', 'h': '100001', 'i': '100010', 'j': '100011',
    'k': '100100', 'l': '100101', 'm': '100110', 'n': '100111',
    'o': '101000', 'p': '101001', 'q': '101010', 'r': '101011',
    's': '101100', 't': '101101', 'u': '101110', 'v': '101111',
    'w': '110000', 'x': '110001', 'y': '110010', 'z': '110011',
    '0': '110100', '1': '110101', '2': '110110', '3': '110111',
    '4': '111000', '5': '111001', '6': '111010', '7': '111011',
    '8': '111100', '9': '111101', '+': '111110', '/': '111111'
}


class Base64:

    def __init__(self, file_name):
        self.file_name = file_name
        self.binary_data = self.read_contents()

    def read_contents(self):
        # Open image in read binary mode (returns a byte object)
        with open(self.file_name, 'rb') as image:
            content = image.read()

        binary_string = ""
        for byte in content:
            # Convert the byte to a binary string, remove the 'Ob' prefix and fill with padding if needed
            binary_value = bin(byte)[2:].zfill(8)
            # Add byte to our string
            binary_string += binary_value

        return binary_string

    def encode(self):
        # Store the binary string into an array with strings that are 6 characters long
        binary_chunks = [self.binary_data[i:i + 6] for i in range(0, len(self.binary_data), 6)]
        encoded_string = ""
        for binary_string in binary_chunks:
            if len(binary_string) != 6:
                continue
            else:
                # Map the binary chunk to an ASCII character
                encoded_string += bin_to_character_table[binary_string]

        return encoded_string

    def decode(self, encoded_string):
        return
