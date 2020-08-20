# text-generator-with-keywords

<h3>Training file</h3>
<p>Use <b>driver.py</b> to train the .txt file</p>

Training file should be of around 5000 chars atleast to train the model.<br><br>

<h3>Running the model to generate text</h3>
<p>Use <b>run_model.py</b> to get resulting text from <b>small.txt</b> file, configured in gpt2.generate function</p>

<br><br>
<h3>Code configuration in run_model.py</h3>
<code>gpt2.generate(sess,
              temperature=0.7,
              top_k=40,
              nsamples=1,
              batch_size=1,
              length=200,
              prefix=f"~^{keywords}",
              truncate="",
              include_prefix=False
              )</code><br><br>


<h3>Sample file</h3>
Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling. The novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry. The main story arc concerns Harry's struggle against Lord Voldemort, a dark wizard who intends to become immortal, overthrow the wizard governing body known as the Ministry of Magic and subjugate all wizards and Muggles (non-magical people).<br>
<h3>Sample generated<h3>
Harry becomes a student at Hogwarts School of Witchcraft and Wizardry, which is a wizarding academy in the wizarding world, and it is here where most of the events in the series take place. The main story arc concerns Harry's struggle against Lord Voldemort, a dark wizard who intends to become immortal, overthrow the wizard governing body known as the Ministry of Magic and subjugate all wizards and Muggles (non-magical people).

Since the release of the first novel, Harry Potter and the Philosopher's Stone, on 26 June 1997, the books have found immense popularity, critical acclaim and commercial success worldwide. They have attracted a wide adult audience as well as younger readers and are often considered cornerstones of modern young adult literature.[2] As of February 2018, the books have sold more than 500 million copies worldwide, making them the best-selling book series in history, and have been translated into
<br>