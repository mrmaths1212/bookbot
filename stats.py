
def get_number_of_words(text):
    return len(text.split())

def get_character_counts(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def format_list(items):
    return [{"char": c, "num": n} for c, n in items.items()]

def sort_on(item):
    return item["char"]

def sort(items):
    items.sort(key=sort_on, reverse=False)
    return items
def pretty_print(text):
    counts = get_character_counts(text)
    items = format_list(counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_number_of_words(text)} total words")
    print("--------- Character Count -------")
    items = sort(items)
    for item in items:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
