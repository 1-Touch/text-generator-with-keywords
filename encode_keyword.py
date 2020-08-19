import multiprocessing
import spacy
import re

DELIMS = {
    'section': '~',
    'category': '`',
    'keywords': '^',
    'title': '@',
    'body': '}'
}

PRONOUN_LIST = ['I', 'Me', 'We', 'You', 'He', 'She',
                'It', 'Him', 'Her', 'Them', 'They']

PRONOUNS = set(PRONOUN_LIST + [x.lower() for x in PRONOUN_LIST])


nlp = spacy.load('en_core_web_sm')

def encode_keywords(csv_path, model='en_core_web_sm'):
    data_list = ''


    with open("shakespeare_small.txt", 'r', encoding='utf8', errors='ignore') as f:
        data_list = f.readlines()

    a = generate_encoded_text(data_list)
    print(a)
    return a

keyword_length_max = 5

def generate_encoded_text(row):
    # Generate the keywords using spacy
    # replace smart quotes first for better tokenization
    text = row[0]
    doc = nlp(text)
    print(doc)
    keywords_pos = [chunk.text if chunk.pos_ == 'NOUN'
                    else chunk.lemma_ if chunk.pos_ in ['VERB', 'ADJ', 'ADV']
                    else 'I'
                    for chunk in doc
                    if not chunk.is_stop
                    ]
    keywords_ents = [re.sub(' ', '-', chunk.text)
                     for chunk in doc.ents]
    keywords_compounds = [re.sub(' ', '-', chunk.text)
                          for chunk in doc.noun_chunks
                          if len(chunk.text) < keyword_length_max]
    keywords = list(set(keywords_pos +
                        keywords_ents +
                        keywords_compounds) - PRONOUNS)  # dedupe
    return keywords
