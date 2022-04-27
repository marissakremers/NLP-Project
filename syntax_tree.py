# Purpose: parse English sentences into PoS tags and form into a parse tree
# Lexicon provided: what, Mary, did, walks, walked, give, gave, me, a the, her, picture, man, dreams, boat, of

# Import required libraries
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser
# Only need downloads if running for first time
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# Example text (text that will be parsed into a tree)
# Within scope of lexicon provided
# sample_text = "Mary walks." #causes inaccurate output
sample_text = "Mary gave her a picture of the boat."
# sample_text = "The picture picture of Mary gave me a man."
# sample_text = "Mary did give a picture."
# sample_text = "Did Mary give a picture?" #causes inaccurate output
# sample_text = "did Mary give a picture?"
# sample_text = "What did Mary give the man of her dreams?"
# sample_text = "Give me a picture!"


# Outside of lexicon's scope
# sample_text = "Mary walks a lot."
# sample_text = "Frogs are nice."
# sample_text = "I am ready to leave."
# sample_text = "Please get me a matcha latte." #causes inaccurate output
# sample_text = "Who are you?"
# sample_text = "The food is hot!"
# sample_text = "What is your favorite color?"
# sample_text = "If I were a tree, oh, I would be a fantastic tree indeed"


# Find all parts of speech (PoS) in above sentence (and tokenize)
tagged = pos_tag(tokens=word_tokenize(sample_text), lang="eng")

#Get PoS from the text
chunker = RegexpParser(grammar=
                       """
					    NP: {<DT>?<JJ>*<NN>} #To get noun phrases
					    P: {<IN>}			 #To get prepositions
					    V: {<V.*>}			 #To get verbs
					    PP: {<P> <NP>}		 #To get prepositional phrases
					    VP: {<V> <NP|PP>*}	 #To get verb phrases
					    """)
# Get a tree of the PoS from the above rules
output = chunker.parse(chunk_struct=tagged, trace=0)

# Print tree results
print("Given sentence:\n", sample_text)

print("After Extracting:")
#Handle mood of the sentence
match output[-1]:
    case ('.', '.'):
        print("Mood = declarative")
    case ('?', '.'):
        print("Mood = interrogative")
    case ('!', '.'):
        print("Mood = exclamatory")
print(output) #prints parse tree in console
output.draw() #pulls up additional window to visualize the parse tree
