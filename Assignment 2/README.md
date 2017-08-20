This assignment aims to make you familiar with the IMDb movie review dataset, and also make you comfortable with text processing in Python for a large dataset. When you complete task 1, you would have learnt how to use your learnings from assignment 1 on a big dataset (easy). Also, you would have practiced text processing in slightly more detail. On completion of task 2, you would have your own working Naive Bayes classifier for the dataset, thus completing your first milestone of the project.

So go ahead, and make your effort count!

Task 1
-------

http://ai.stanford.edu/~amaas/data/sentiment/ - this is hopefully a working link from where you can download the IMDb dataset. Use only the labelled reviews (labels being positive / negative) for all the tasks. Iterate over the reviews, and split them into individual words, the way you did in assignment 1, or using a tokenizer available in NLTK. Now, remove stopwords from the reviews using NLTK's stopwords list, and stem / lemmatize the words using some good stemmer (again, NLTK has some decent ones, though you could look up others on the internet). By this step, the reviews would only consist of individual words, all in lowercase, no non alphabetic character included, stopwords removed, and all reduced to their stems. We're good to go to Task 2.

Task 2
-------

Build a dictionary of words that looks like the following: {word: frequency}, e.g. {'apple' : 5, 'banana' : 7, ...}. Here, frequency of a word corresponds to the number of times that it has appeared in the whole dataset. Construct similar dictionaries individually for positive reviews and negative reviews (as in, you would have three dictionaries, 'all', 'positive', 'negative'). Now we have all the tools available to build a simple Naive Bayes classifier.

So look up a decent tutorial on the same (even the Wikipedia page would do) and implement it! It's quite easy at this point.
