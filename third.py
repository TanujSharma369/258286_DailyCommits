def longest_common_prefix(strings):
    if 0 == len(strings):
        return "Empty String"
    else:
        for prefix in range(0, len(strings[0])):
            to_match = strings[0][prefix]
            for i in range(1, len(strings)):
                if prefix >= len(strings[i]) or to_match != strings[i][prefix]:
                    return strings[0][0:prefix]
    return strings[0]


if __name__ == "__main__":
    test1 = ["flow", "flow", "flow"]
    test2 = ["dog", "cat", "bird"]
    test3 = ["class", "classes", "c"]
    print(longest_common_prefix(test1))

