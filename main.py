def freq_finder(string):
    dictn = {}
    for i in string:
        if i in dictn:
            dictn[i]+=1
        else:
            dictn[i] = 1
    dictn = dict(sorted(dictn.items(), key=lambda item: item[1]))
    return dictn


def huffman_coding(freq_dict):
    # Convert the sorted frequency dictionary into a list
    tree = [[freq, [char, ""]] for char, freq in freq_dict.items()]

    # Build the Huffman Tree
    while len(tree) > 1:
        # Pop the two nodes with the lowest frequency (first two elements)
        low1 = tree.pop(0)
        low2 = tree.pop(0)
        
        # Assign '0' to left and '1' to right
        for pair in low1[1:]:
            pair[1] = '0' + pair[1]
        for pair in low2[1:]:
            pair[1] = '1' + pair[1]

        # Combine the two nodes
        new_node = [low1[0] + low2[0]] + low1[1:] + low2[1:]
        # Append the new node and sort the list
        tree.append(new_node)
        tree.sort(key=lambda x: x[0])  # Sort by frequency to maintain order

    # Final list contains the root of the Huffman Tree
    return dict(sorted(tree[0][1:], key=lambda x: x[0]))


def encrypt(text):
    codebook = huffman_coding(freq_finder(text))
    encrypted_string=""
    for char in text:
        # Look up the character in the codebook
        if char in codebook:
            encrypted_string += codebook[char]
        else:
            # Raise an error if the character is not found
            raise ValueError(f"Character '{char}' not found in the codebook.")
    return encrypted_string
