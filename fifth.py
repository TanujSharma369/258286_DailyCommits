class RunLengthEncoding:
    def encoding(self, to_encode):
        consecutive_char_count = 1
        encoded_string = ""
        for current_char in range(1, len(to_encode)+1):
            if current_char == len(to_encode) or to_encode[current_char] != to_encode[current_char-1]:
                encoded_string += str(consecutive_char_count)
                encoded_string += to_encode[current_char-1]
                consecutive_char_count = 1
            else:
                consecutive_char_count += 1
        return encoded_string


if __name__ == "__main__":
    test1 = RunLengthEncoding()
    print(test1.encoding("aaabbbcccddeef"))
