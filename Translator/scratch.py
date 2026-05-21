def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiouAEIOU":
            translation = translation + 'r'
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a word: ")))