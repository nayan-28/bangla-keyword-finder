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

# Example Bangla text
bangla_text = "বাংলা ভাষার প্রসার দুনিয়ায় উচ্চ মানের একটি কাজ। বাঙালি ভাষা, সাহিত্য, সংস্কৃতি এবং ইতিহাসে ঐতিহ্যবাহী। বাংলা ভাষায় লেখা বই, কবিতা, গান অত্যন্ত সমৃদ্ধ।"

# Example stop words (you can customize this list)
stop_words = set(stopwords.words('bengali'))

# Generate summary
summary = generate_summary(bangla_text, stop_words)

# Print the summary
print("Original Text:")
print(bangla_text)
print("\nSummary:")
print(summary)
