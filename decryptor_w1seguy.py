import string

def solve_ctf_precise(hex_string):
    clean_hex = hex_string.strip()
    try:
        ct = bytes.fromhex(clean_hex)
    except ValueError:
        return [("Error")]

    known_prefix = "THM{"
    partial_key = ""
    
    # First 4 digits of key
    for i in range(4):
        partial_key += chr(ct[i] ^ ord(known_prefix[i]))


    alphabet = string.ascii_letters + string.digits
    valid_solutions = []

    for char in alphabet:
        candidate_key = partial_key + char
        
        decrypted_text = ""
        
        # Decyrpting message
        for i in range(len(ct)):
            decrypted_text += chr(ct[i] ^ ord(candidate_key[i % 5]))
            
        is_printable = all(32 <= ord(c) <= 126 for c in decrypted_text)
        ends_correctly = decrypted_text.endswith('}')
        
        if is_printable and ends_correctly:
            valid_solutions.append((candidate_key, decrypted_text))

    return valid_solutions

current_hex = input("HEX: ")

results = solve_ctf_precise(current_hex)

for key, text in results:
    print(f"KEY: {key}")
    print(f"FLAG: {text}")

