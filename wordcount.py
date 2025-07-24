import re
from collections import Counter

def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    text_lower = text.lower()
    words = re.findall(r'\b\w+\b', text_lower)
    total_words = len(words)
    word_freq = Counter(words)

    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    total_sentences = len(sentences)
    avg_sentence_length = total_words / total_sentences if total_sentences > 0 else 0

    print(f"Total words: {total_words}")
    print(f"Total sentences: {total_sentences}")
    print(f"Average sentence length (words): {avg_sentence_length:.2f}")
    print("\nWord Frequency (top 10):")
    for word, freq in word_freq.most_common(10):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file to analyze: ")
    analyze_text(file_path)
