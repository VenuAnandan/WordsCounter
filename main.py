def count_words(text):
    word_count = {}
    total_words = 0
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1
        total_words += 1
    return word_count, total_words

def main():
    text = input("Enter some text: ")
    if not text:
        print("Error: No text entered.")
        return
    word_counts, total_words = count_words(text.lower())
    print("\nWord Count:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
    print(f"\nTotal Words: {total_words}")

if __name__ == "__main__":
    main()
