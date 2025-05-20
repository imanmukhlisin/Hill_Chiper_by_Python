import numpy as np

def text_to_numbers(text):
    return [ord(char.upper()) - ord('A') + 1 for char in text if char.isalpha()]

def numbers_to_text(numbers):
    return ''.join([chr(num + ord('A') - 1) if num != 0 else 'Z' for num in numbers])

def get_key_matrix():
    """Input matriks kunci dari pengguna"""
    while True:
        try:
            rows = input("Masukkan matriks kunci (pisahkan baris dengan koma, contoh '3 2,5 7'): ").split(',')
            key_matrix = [list(map(int, row.strip().split())) for row in rows]
            
            # Validasi matriks persegi
            m = len(key_matrix)
            if any(len(row) != m for row in key_matrix) or m == 0:
                raise ValueError("Matriks harus persegi (m x m)")
                
            return key_matrix
        except ValueError as e:
            print(f"Error: {e}. Coba lagi!")

def encrypt_hill(plaintext, key_matrix):
    m = len(key_matrix)
    numbers = text_to_numbers(plaintext)
    
    # Padding 'X' jika perlu
    if len(numbers) % m != 0:
        padding = [24] * (m - (len(numbers) % m))
        numbers += padding
    
    key = np.array(key_matrix, dtype=int)
    cipher_numbers = []
    
    for i in range(0, len(numbers), m):
        block = np.array(numbers[i:i+m]).reshape(m, 1)
        encrypted_block = key.dot(block) % 26
        cipher_numbers.extend(encrypted_block.flatten().tolist())
    
    return numbers_to_text([num if num != 0 else 26 for num in cipher_numbers])

if __name__ == "__main__":
    # Input key
    print("=== Program Enkripsi Hill Cipher ===")
    key = get_key_matrix()
    
    plaintext = input("\nMasukkan plaintext: ").strip()
    
    ciphertext = encrypt_hill(plaintext, key)
    print(f"\nCiphertext: {ciphertext}")