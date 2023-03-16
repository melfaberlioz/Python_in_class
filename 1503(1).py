def is_vovel(letter):
    vovels = 'aouiey'
    return (letter.lower() in vovels)

def is_first_and_last_letters_are_consonant(list_of_letters):
    return (not is_vovel(list_of_letters[0]) and not is_vovel(list_of_letters[-1]))

def is_alternate(list_of_letters):
    for letter in list_of_letters[::2]:
        if is_vovel(letter):
            return False
    for letter in list_of_letters[1::2]:
        if not is_vovel(letter):
            return False
    return True

def find_longest_sequence(list_of_letters):
    longest = 0
    longest_sequence = []
    for i in range(len(list_of_letters)):
        if is_vovel(list_of_letters[i]):
            continue
        for j in range(i+2, len(list_of_letters), 2):
            if is_first_and_last_letters_are_consonant(list_of_letters[i:j+1]) and is_alternate(list_of_letters[i:j+1]):
                if len(list_of_letters[i:j+1]) > longest:
                    longest = len(list_of_letters[i:j+1])
                    longest_sequence = list_of_letters[i:j+1]
    return longest_sequence

def longest_sequences(list_of_list_of_letters):
    result_list = []
    for sequence in list_of_list_of_letters:
        result_list.append(find_longest_sequence(sequence))
    result_list.remove([])
    return result_list

L = [['s', 'o', 'f', 'i', 'a'], ['a', 'b'], ['a', 'b', 'u', 'd', 'f', 'I', 'R', 'e', 'h', 'a']]
print(longest_sequences(L))