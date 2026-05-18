

# 2. Decoding
decoded_img = Image.open("output.png")
flat_decoded = np.array(decoded_img).flatten()

bits = ""
extracted_text = ""
for i in range(len(flat_decoded)):
    bits += str(flat_decoded[i] & 1)
    if len(bits) == 8:
        char = chr(int(bits, 2))
        extracted_text += char
        bits = ""
        if delimiter in extracted_text:
            print(extracted_text.replace(delimiter, ""))
            break