# FTC - Fuzzy Text Classifier

A fuzzy classifier library for natural language text.
[Github-Repo](https://github.com/raffaellopaletta/ftc)


### Simple usage example

```python
#import library
from fuzzy_text_classifier import TextClassifier  

#instantiate class
tc = TextClassifier()

#train the classifier with some documents
doc1 = 'some text document about sport'
doc2 = 'another text document about cinema'
doc3 = 'another one text document music'

tc.train(doc1, 'sport')
tc.train(doc1, 'cinema')
tc.train(doc1, 'music')

#classify a document
doc = 'a document to classify'
ranking = tc.classify(doc)
```

ranking** will be an object like 

`[{'sport': 0.95}, {'cinema': 0.3}, {'music': 0.2}]
`

a list ordered by similarity where the key is the category and the value is the degree of similarity between 
the document and the category. 