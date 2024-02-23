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

# List of key words to extract
keywords_to_extract = ["জ্বর", "সর্দি", "কাশি", "ব্যাথা", "পায়ে ব্যাথা", "মাথা ব্যাথা", "মাথা যন্ত্রণা", "মাথা ঝিমঝিম"]

# Extract keywords from the summary
extracted_keywords = [keyword for keyword in keywords_to_extract if keyword in summary]

# Print the summary
print("\nআপনার প্রদানকৃত তথ্য:")
print(bangla_text)
print("\nসারাংশ:")
print(summary)
print("\nআপনার সমস্যাগুলো:")
print(extracted_keywords)
