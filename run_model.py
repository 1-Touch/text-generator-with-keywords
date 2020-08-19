import gpt_2_simple as gpt2
from encode_keyword import encode_keywords

         
words = encode_keywords(csv_path='harry_potter_small.txt')

s = " "
s = s.join(words)
print(s)

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

gpt2.generate(sess,
              temperature=0.7,
              top_k=40,
              nsamples=1,
              batch_size=1,
              length=100,
              prefix=f"~^wizard",   #Put keywords with space eg: wizard harry magic
              truncate="",
              include_prefix=False
              )