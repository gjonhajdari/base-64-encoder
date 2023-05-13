class Base64:

    def __init__(self, file_name):
        self.file_name = file_name
        self.binary_data = self.read_contents()

    def read_contents(self):
        return

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
