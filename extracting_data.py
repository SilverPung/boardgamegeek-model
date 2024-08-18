def extract_players(doc):
    players = None
    for token in doc:
        # Check for numbers followed by words like 'graczy', 'osób'
        if token.like_num and token.head.lemma_ in ["gracz", "osoba"]:
            players = int(token.text)
            break
    return players

def extract_playtime(doc):
    playtime = None
    czas_lemmas = ["minuta", "godzina","minuty", "godziny","minut", "godzin" ]
    long_lemmas = ["długi", "długo", "długa", "długi", "długa", "długi", "długa"]
    short_lemmas = ["krótki", "krótko", "krótka", "krótki", "krótka", "krótki", "krótka"]
    for token in doc:
        # Look for keywords related to time
        if token.lemma_ in czas_lemmas:
            if token.head.lemma_ == "trwać":
                time = int(token.head.head.text)
                playtime = time if token.lemma_ == "minuta" else time * 60
        elif token.lemma_ in short_lemmas:
                playtime = "short"
        elif token.lemma_ in long_lemmas:
                playtime = "long"
        

    return playtime


def extract_difficulty(doc):
    difficulty_synonyms = {
        "łatwy": ["łatwe", "prosty", "łatwa", "łatwo", "łatwy", "łatna", "proste", "prosta", "prosty", "prosta","łatwiej"],
        "średni": ["średnie", "umiarkowany", "średnia", "średnio", "średni", "średnia", "umiarkowane", "umiarkowana", "umiarkowany", "umiarkowana","umiarkowanie","niezbyt"],
        "trudny": ["trudne", "skomplikowany", "trudna", "trudno", "trudny", "trudna", "skomplikowane", "skomplikowana", "skomplikowany", "skomplikowana"]
    }
    
    difficulty = None
    for token in doc:
        for key, synonyms in difficulty_synonyms.items():
            if token.lemma_ in synonyms:
                difficulty = key
                break
        if difficulty:
            break
    return difficulty

