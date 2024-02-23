from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def generate_summary(bangla_text, stop_words):
    # Tokenize the Bengali text
    tokens = word_tokenize(bangla_text)

    # Remove stop words
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    # Join the tokens to form the summary
    summary = ' '.join(filtered_tokens)

    return summary

# Take input from the user
bangla_text = input("Enter your Bengali text: ")

# Example stop words (you can customize this list)
stop_words = set(stopwords.words('bengali'))

# Generate summary
summary = generate_summary(bangla_text, stop_words)

# Print the summary
print("\nOriginal Text:")
print(bangla_text)
print("\nSummary:")
print(summary)
