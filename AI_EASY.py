
STOP_WORDS = ["the", "is", "at", "which", "and", "to", "a", "an", "for", "my", "i"]


def clean_and_tokenize(text):
    cleaned_txt = text.lower().split(" ")
    tokenized = []
    
    for w in cleaned_txt:
        if w not in STOP_WORDS:
            tokenized.append(w)
    return tokenized

def classify_message(text):
    tokens = clean_and_tokenize(text)
    
    if ("crash" in tokens or
        "bug" in tokens or
        "broken" in tokens or
        "error" in tokens or
        "crashes" in tokens or
        "errors" in tokens or
        "break" in tokens):
        return "Technical Support"

    elif ("bill" in tokens or
        "charged" in tokens or
        "payment" in tokens or
        "subscription" in tokens or
        "subscribe" in tokens or
        "charge" in tokens or
        "billing" in tokens or
        "paid" in tokens):
        return "Billing Support"
    
    else:
        return "General Inquiry"



print(classify_message("the app crashes every time I open it"))