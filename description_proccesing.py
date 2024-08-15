import spacy
from extracting_data import extract_players, extract_playtime, extract_difficulty
import language_tool_python

tool = language_tool_python.LanguageTool('pl-PL')
nlp = spacy.load('pl_core_news_sm')




def normalize_text(text):
    # Process the text
    doc = nlp(text)
    # Normalize text by lemmatizing and converting to lowercase
    normalized_text = " ".join([token.lemma_.lower() for token in doc if not token.is_punct])
    return normalized_text


def parse_polish_description(description):
    # Process the text with spaCy
    normalized_description=normalize_text(description)
    print(normalized_description)
    matches = tool.check(normalized_description)
    corrected_description = tool.correct(normalized_description)
    
    print(corrected_description)
    
    doc = nlp(corrected_description)
    
    # Extract attributes
    players = extract_players(doc)
    playtime = extract_playtime(doc)
    difficulty = extract_difficulty(doc)
    
    # Return the parsed data as a dictionary
    return {
        "players": players,
        "playtime": playtime,
        "difficulty": difficulty,
    }

# Example usage
description = "SzuKam grya dla 4 graczy, niezbyt długiej, o śSrednim poziomie skomplikowania."
parsed_data = parse_polish_description(description)
print(parsed_data)
