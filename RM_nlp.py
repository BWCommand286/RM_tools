
import spacy

import RM_itertools as RMI

def load_models():
    #natural language processing
    import spacy
    global nlp
    nlp = spacy.load('en_core_web_lg')



def pos_tag_df(text):
    
    doc = nlp(text)
    
    dict_list = []
    
    
    for token in doc:
        output = {}
        output['text'] = token.text
        output['lemma'] = token.lemma_
        output['pos'] = spacy.explain(token.pos_)
        output['tag'] = spacy.explain(token.tag_)
        output['dep'] = spacy.explain(token.dep_)
        output['shape'] = token.shape_
        output['is_alpha'] = token.is_alpha
        output['is_stop'] = token.is_stop
        dict_list.append(output)   
            
    
    return RMI.dict_merge(dict_list)

test_sent = 'Michael Walter, CEO, Debil constulting'

test_sent =  'Michael was fired yesterday'

test_sent = 'Michael has helped Brian with school in his office in Dickdarm Road'

test_sent = 'Michael Toastman, works as Senior Data Consultant & CCO,  Strategic Solutions Inc., 5th Avenue, New York'




text_info = pos_tag_df(test_sent)

#text_info.to_csv('text_info.csv')

print(text_info['pos'])
print(text_info['tag'])
print(text_info['dep'])

ents = get_entities(test_sent)

print(ents)

for key in ents.keys():
    print(spacy.explain(key))