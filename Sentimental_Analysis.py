from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentences=["VADER is smart,handsome, and funny"]
paragraph="It was one of the worst movies I've seen, despite good reviews.\ Unbelievably bad acting!! Poor direction. VERY poor production.\ The movie was bad. Very bad movie. VERY bad movie. VERY BAD movie!"

from nltk import tokenize
lines_list=tokenize.sent_tokenize(paragraph)
sentences.extend(lines_list)
tricky_sentences=["Bad","Most automated sentiment analysis tools are shit","The movie was too good","Very Bad"]
sentences.extend(tricky_sentences)
sid = SentimentIntensityAnalyzer()
for sentence in sentences:
    print sentence
    ss=sid.polarity_scores(sentence)
    for k in sorted(ss):
        print '{0}:{1},'.format(k,ss[k])
    print''
