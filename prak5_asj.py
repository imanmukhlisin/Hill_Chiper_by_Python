{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd6bbb97-57af-4db5-a68e-c6e7967c55e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=== Program Enkripsi Hill Cipher ===\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Masukkan matriks kunci (pisahkan baris dengan koma, contoh '3 2,5 7'):  2 1,2 8\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "def text_to_numbers(text):\n",
    "    return [ord(char.upper()) - ord('A') + 1 for char in text if char.isalpha()]\n",
    "\n",
    "def numbers_to_text(numbers):\n",
    "    return ''.join([chr(num + ord('A') - 1) if num != 0 else 'Z' for num in numbers])\n",
    "\n",
    "def get_key_matrix():\n",
    "    \"\"\"Input matriks kunci dari pengguna\"\"\"\n",
    "    while True:\n",
    "        try:\n",
    "            rows = input(\"Masukkan matriks kunci (pisahkan baris dengan koma, contoh '3 2,5 7'): \").split(',')\n",
    "            key_matrix = [list(map(int, row.strip().split())) for row in rows]\n",
    "            \n",
    "            # Validasi matriks persegi\n",
    "            m = len(key_matrix)\n",
    "            if any(len(row) != m for row in key_matrix) or m == 0:\n",
    "                raise ValueError(\"Matriks harus persegi (m x m)\")\n",
    "                \n",
    "            return key_matrix\n",
    "        except ValueError as e:\n",
    "            print(f\"Error: {e}. Coba lagi!\")\n",
    "\n",
    "def encrypt_hill(plaintext, key_matrix):\n",
    "    m = len(key_matrix)\n",
    "    numbers = text_to_numbers(plaintext)\n",
    "    \n",
    "    # Padding 'X' jika perlu\n",
    "    if len(numbers) % m != 0:\n",
    "        padding = [24] * (m - (len(numbers) % m))\n",
    "        numbers += padding\n",
    "    \n",
    "    key = np.array(key_matrix, dtype=int)\n",
    "    cipher_numbers = []\n",
    "    \n",
    "    for i in range(0, len(numbers), m):\n",
    "        block = np.array(numbers[i:i+m]).reshape(m, 1)\n",
    "        encrypted_block = key.dot(block) % 26\n",
    "        cipher_numbers.extend(encrypted_block.flatten().tolist())\n",
    "    \n",
    "    return numbers_to_text([num if num != 0 else 26 for num in cipher_numbers])\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    # Input key\n",
    "    print(\"=== Program Enkripsi Hill Cipher ===\")\n",
    "    key = get_key_matrix()\n",
    "    \n",
    "    plaintext = input(\"\\nMasukkan plaintext: \").strip()\n",
    "    \n",
    "    ciphertext = encrypt_hill(plaintext, key)\n",
    "    print(f\"\\nCiphertext: {ciphertext}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e32a303-46c7-44c0-9f1b-8feaf379b303",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}