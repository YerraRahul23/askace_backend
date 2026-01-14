import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("data.json", "r", encoding="utf-8") as f:
    KB = json.load(f)

QUESTIONS = []
ANSWERS = []

def flatten_data():
    for key, value in KB.items():
        if key == "placements":
            phrases = [
                "placements",
                "placement details",
                "highest package",
                "highest salary",
                "top package",
                "recruiters",
                "companies visiting campus"
            ]
            for p in phrases:
                QUESTIONS.append(p)
                ANSWERS.append(value)

        elif key == "fees":
            phrases = [
                "fees",
                "annual fee",
                "tuition fee",
                "fee of all branches",
                "cse fee",
                "aiml fee",
                "ds fee",
                "ece fee",
                "eee fee",
                "mech fee",
                "civil fee"
            ]
            for p in phrases:
                QUESTIONS.append(p)
                ANSWERS.append(value)

        elif key == "clubs":
            QUESTIONS.append("clubs")
            ANSWERS.append(value)

        else:
            QUESTIONS.append(key)
            ANSWERS.append(value)

flatten_data()

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(QUESTIONS)

def get_answer(question: str):
    q_vec = vectorizer.transform([question])
    scores = cosine_similarity(q_vec, X)
    best = scores.argmax()
    confidence = scores[0][best]

    if confidence < 0.15:
        return None

    return QUESTIONS[best], ANSWERS[best]
