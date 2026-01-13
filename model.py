import json

with open("data.json", "r", encoding="utf-8") as f:
    KB = json.load(f)

def get_answer(question: str) -> str:
    q = question.lower()

    # FEES
    if "fee" in q or "fees" in q:
        for dept in KB["fees"]:
            if dept in q:
                return KB["fees"][dept]
        return "Fees vary by department. Please specify CSE, AIML, ECE, etc."

    # PLACEMENTS
    if "placement" in q or "placements" in q:
        p = KB["placements"]
        return (
            f"Programs: {', '.join(p['programs'])}\n"
            f"{p['highest_package']}\n"
            f"Recruiters: {', '.join(p['partners'])}"
        )

    # CLUBS
    if "club" in q or "clubs" in q:
        return "Technical Clubs:\n" + "\n".join(KB["clubs"])

    # HOSTEL
    if "hostel" in q:
        return KB["hostel"]

    # BUS
    if "bus" in q or "transport" in q:
        return KB["bus"]

    # SPORTS
    if "sport" in q or "games" in q:
        return KB["sports"]

    # FEST
    if "fest" in q or "event" in q:
        return KB["fest"]

    return "Sorry, I couldn’t understand your question 🤖"
