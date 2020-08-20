import gpt_2_simple as gpt2
import spacy

data = ''

with open('harry_potter_small.txt', 'r') as f:
    data = f.readlines()

nlp = spacy.load("en_core_web_sm")

doc = nlp(data[0])

# for ent in doc.ents:
#     print(ent.text, ent.label_)


x = []
for i in doc.ents:
    if i.label_ == "PERSON" or i.label_ == "ORG":
        x.append(i.text)

keywords = " ".join(x)
print(keywords)


sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

gpt2.generate(sess,
              temperature=0.7,
              top_k=40,
              nsamples=1,
              batch_size=1,
              length=200,
              prefix=f"~^{keywords}",   #Put keywords with space eg: wizard harry magic
              truncate="",
              include_prefix=False
              )