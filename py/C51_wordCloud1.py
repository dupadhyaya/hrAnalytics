# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Word Cloud
# -  https://www.analyticsvidhya.com/blog/2021/05/how-to-build-word-cloud-in-python/
# -  https://www.datacamp.com/tutorial/wordcloud-python

# +
# # !pip install wordcloud
# -

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import wikipedia
from PIL import Image

# +
# #!pip install wordcloud wikipedia pillow
#stop words - is, as, the, which are not to be analysed
# -

#stop words
stop_w = set(STOPWORDS)
#print(stop_w)

# ## Example 1
# -  wordcloud from Text

text1 = 'The quick brown fox jumps over the lazy little dog  Dhiraj Dhiraj Python Python Python'

print(text1)

word_cloud = WordCloud().generate_from_text(text1)

plt.imshow(word_cloud)

img = word_cloud.to_image()
img.show();

# ## Example 2
# -  Load from text file in web
# -  Contains list of words

textFile = 'E:/analytics/projects/hrAnalytics/data/misc/sampleWords.txt'
sampleText = open(textFile, "r").read()

# +
#sampleText
# -

#maskArray = npy.array(Image.open("cloud.png")) #mask = maskArray, 
cloudModel = WordCloud(background_color = "white", max_words = 20, stopwords = set(STOPWORDS))

sampleTextLower = sampleText.lower()
cloudModel.generate(sampleTextLower)

img = cloudModel.to_image()
img.show();

cloudModel.to_file("wordCloud1.png")
#save to file

# ## Example 3
# -  wc = WordCloud( background_color="white", height=300, width=500,  include_numbers = True, min_word_length=6,  max_words = 50, margin = 8).generate(data)
# -  minimum length of word
# -  margin between words

cvFile = 'E:/analytics/projects/hrAnalytics/data/text/sampleCV.txt'
cvSample = open(cvFile , "r").read()

wcCVmodel = WordCloud(background_color="white", height=400, width=800,  min_word_length=3,  max_words = 20, margin = 8)
cvLower = cvSample.lower()
wcCVmodel.generate(cvLower)

img = wcCVmodel.to_image()
img.show();

# plot the WordCloud image                      
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wcCVmodel)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show();

# # word Cloud from frequences

word = ['beautiful', 'lovely', 'efficient','play', 'growth','vulgar']
freq  = np.random.randint(low=30, high=100, size=6)
#wordFreq = pd.DataFrame({'word':word, 'freq':freq})
#word, freq
dict = {'word':word, 'freq':freq}
dict
#stopword Ignored if using generate_from_frequencies.

words = pd.DataFrame(dict)
words

tuples1 = [ tuple(x) for x in words.values]
tuples1
#words.to_dict()

dictWords = {}
for key, val in tuples1:    dictWords.setdefault(key, val)
print(dictWords)
##enumerate(tuples, start=0)

wcF1 = WordCloud(scale=.8, prefer_horizontal=.5, font_step=2, min_font_size=10, max_font_size=100,  include_numbers = True,\
                background_color="white", stopwords=['vulgar'])
wcF1.generate_from_frequencies(frequencies=dictWords)
wcF1

plt.figure(figsize=(10,7))
plt.imshow(wcF1, interpolation="bilinear")
plt.axis("off")
plt.show();

# # Interactive
#

sheet_id = '1INLfAoJsnO6eWxUL1B23EcNIyVYY5GZnqXsJLiSGS6w'
sheet_name = 'pl2'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

dfPL = pd.read_csv(url)
dfPL= dfPL.set_index('language')
dfPL

Y2021 = dfPL['Y2021'].to_dict()
Y2022 = dfPL['Y2022'].to_dict()
Y2023 = dfPL['Y2023'].to_dict()
print(Y2021, Y2022, Y2023)

import ipywidgets as widgets

dropDown = widgets.Dropdown(options=[('2021',Y2021), ('2022',Y2022), ('2023',Y2023)], value=Y2023, description='Year')


def update_WC(choice):
    wcIPY = WordCloud(colormap='tab10').generate_from_frequencies(choice)
    plt.figure(figsize=(8,8))
    plt.imshow(wcIPY)
    plt.axis('off')
    plt.show();


widgets.interact(update_WC, choice=dropDown)

# ## Word Cloud from text

pmText = " Today, all Indians in the country and also abroad are celebrating the festival of independence. On this day of sacred festival of independence, the prime servant of India extends greetings to all dear countrymen.I am present amidst you not as the Prime Minister, but as the Prime Servant. The freedom struggle was fought for so many years, so many generations laid down their lives, innumerable people sacrificed their lives and youth, spent their entire lives behind bars. Today, I pay my respect, greetings and homage to all those who laid their lives for the country's independence. I also pay my respects to the crores of citizens of this country on the pious occasion of India's independence, and recall all those martyrs who had laid down their lives in India's struggle for freedom. The day of independence is a festival when we take a solemn pledge of working for the welfare of mother India, and also for the welfare of the poor, oppressed, dalits, the exploited & the backward people of our country.  My dear countrymen, a national festival is an occasion to refine and rebuild the national character. This National festival inspires us to resolve ourselves to lead a life where our character gets refined further, to dedicate ourselves to the nation and our every activity is linked to the interest of the nation and only then this festival of freedom can be a festival of inspiration to take India to newer heights."

len(pmText)

counts = WordCloud().process_text(pmText)
sorted(counts.items())[1:5]
#print(dict(sorted(counts.items(), key = lambda item: item[1], reverse=True)))

wc5 = WordCloud(colormap='coolwarm').generate(pmText)
wc5

plt.figure(figsize=(10,7))
plt.imshow(wc5)
plt.axis('off')
plt.show();
#save to file : #wc5.to_file('./images/pmSpeech.png')

# +
#end here
# -

# # Links
# -  Example 
#     -  https://www.kaggle.com/datasets/datasnaek/youtube
#     -  https://blog.devgenius.io/text-data-analysis-youtube-sentiment-wordcloud-and-emojis-analysis-c65657bfa2b8
#     -  https://github.com/shubhamringole/Text-Data-Analysis-YouTube-Sentiment-WordCloud-and-Emojis-Analysis
