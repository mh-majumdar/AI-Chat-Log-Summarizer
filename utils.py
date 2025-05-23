from collections import Counter
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import word_tokenize, pos_tag, FreqDist

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')
STOPWORDS = set(stopwords.words('english'))

# Parses the chat log and returns a list of messages
# Example: [{"speaker": "User", "message": "Hi"}, {"speaker": "AI", "message": "Hello"}]
def parse_chat_log(text):
    messages = []
    lines = text.strip().split('\n')
    for line in lines:
        if line.startswith('User:'):
            messages.append({"speaker": "User", "message": line[5:].strip()})
        elif line.startswith('AI:'):
            messages.append({"speaker": "AI", "message": line[3:].strip()})
    return messages

def extract_messages(messages):
    return [msg['message'] for msg in messages]

def get_statistics(messages):
    total = len(messages)
    user_count = sum(1 for msg in messages if msg['speaker'] == 'User')
    ai_count = sum(1 for msg in messages if msg['speaker'] == 'AI')
    return {"total": total, "user": user_count, "ai": ai_count}

def get_keywords(messages):
    all_text = ' '.join([msg['message'] for msg in messages])
    tokens = re.findall(r'\b\w+\b', all_text.lower())
    filtered = [word for word in tokens if word not in STOPWORDS and word not in string.punctuation]
    return Counter(filtered).most_common(5)

def generate_summary(stats, keywords, messages):
    keyword_str = ', '.join([word for word, _ in keywords])

    summary = (
        f"The chat contains {stats['total']} messages: "
        f"{stats['user']} from the user and {stats['ai']} from the AI. "
        f"Top discussed keywords include: {keyword_str}. "
        f"This indicates that the conversation focused on these core topics. "
        f"The exchange reflects a natural interaction where the user raised queries and the AI responded accordingly."
    )

    return summary