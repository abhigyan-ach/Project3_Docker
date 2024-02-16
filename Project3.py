#!/usr/bin/env python3

import os
import socket
from collections import Counter

# Directory containing text files
data_dir = '/home/data'

# Function to list files and their word count
def list_files_and_word_count():
    files = os.listdir(data_dir)
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(data_dir, file), 'r') as f:
                words = f.read().split()
                print(f"File: {file}, Word Count: {len(words)}")

# Function to count words in a text file
def count_words(filename):
    with open(os.path.join(data_dir, filename), 'r') as f:
        words = f.read().split()
        return len(words)

# Function to find top 3 words with counts in a text file
def top_words(filename, n=3):
    with open(os.path.join(data_dir, filename), 'r') as f:
        words = f.read().split()
        word_counts = Counter(words)
        return word_counts.most_common(n)

# Function to get local machine's IP address
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

# Main function
def main():
    # List all text files and their word counts
    list_files_and_word_count()

    # Count total words in both files
    total_words = sum(count_words(filename) for filename in ['IF.txt', 'Limerick-1.txt'])
    print(f"Grand Total Number of Words: {total_words}")

    # List top 3 words with counts in IF.txt
    top_words_list = top_words('IF.txt')
    print("Top 3 words in IF.txt:")
    for word, count in top_words_list:
        print(f"Word: {word}, Count: {count}")

    # Get local machine's IP address
    ip_address = get_ip_address()
    print(f"IP Address: {ip_address}")

    # Write output to result.txt
    with open('/home/data/result.txt', 'w') as f:
        f.write(f"List of files and their word counts:\n")
        list_files_and_word_count()
        f.write(f"\nGrand Total Number of Words: {total_words}\n")
        f.write(f"\nTop 3 words in IF.txt:\n")
        for word, count in top_words_list:
            f.write(f"Word: {word}, Count: {count}\n")
        f.write(f"\nIP Address: {ip_address}\n")

if __name__ == "__main__":
    main()

