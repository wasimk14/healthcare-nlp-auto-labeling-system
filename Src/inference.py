import spacy

MODEL_PATH = "../Models/spacy_baseline/model-best"

nlp = spacy.load(MODEL_PATH)


def extract_entities(text):
    doc = nlp(text)

    entities = []

    for ent in doc.ents:
        entities.append(
            {
                "text": ent.text,
                "label": ent.label_
            }
        )

    return entities
