import re
def telugu_tokenizer(text):
    patterns = {
        "punctuation": r"[.,!?;:\"'()👦👦{}]",
        "date": r"\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{1,2} [A-Za-z]+ \d{2,4})\b",
        "url": r"https?://[^\s]+",
        "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "number": r"\b(?:\d{1,3}(?:,\d{2,3})*|\d+\.\d+|\d+/\d+|\d+)\b", 
        "telugu_number": r"[\u0C66-\u0C6F]+(?:[.,][\u0C66-\u0C6F]+)?",
        "social_media": r"[@#][\w]+",
        "telugu_word": r"[\u0C00-\u0C7F]+", 
    }
    combined_pattern = "|".join(f"(?P<{key}>{pattern})" for key, pattern in patterns.items())

    tokens = []
    
    for match in re.finditer(combined_pattern, text):
        for key, value in match.groupdict().items():
            if value:
                tokens.append((key, value))

    return tokens
text = """
నా పేరు వంశీ. నా ఇమెయిల్ test@example.com. నా సైట్ https://example.com.  
నా ఫోన్ 98456-78901. నా ట్విట్టర్ @vamsi_123. నిన్న నేను 10-03-2025న వెళ్లాను.  
దిగువ సంఖ్య ౩౩.౧౫ మరియు 3,22,243. 
"""

tokens = telugu_tokenizer(text)
for token_type, token_value in tokens:
    print(f"{token_type}: {token_value}")