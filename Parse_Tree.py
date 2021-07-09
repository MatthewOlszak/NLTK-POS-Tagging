from nltk import pos_tag, word_tokenize, RegexpParser

# Student 3
docText1 = "It was a quiet impressive essay regarding the content. It could have been more properly structured as there were fewer headings and bullets. Overall good work"
# Student 15
docText2 = "They gave a pretty good explanation of how bumpmapping works, but a shader algorithm would have been nice. Besides that I feel like they didn't focus on NPR as much as they could have."

tagged1 = pos_tag(word_tokenize(docText1))
tagged2 = pos_tag(word_tokenize(docText2))

chunk1 = RegexpParser("""
                        NP: {<DT>?<JJ>*<NN>}
                        P: {<IN>}
                        V: {<V.*>}
                        PP: {<P> <NP>}
                        VP: {<V> <NP|PP>*}
                        """)

chunk2 = RegexpParser("""
                        NP: {<DT>?<JJ>*<NN>}
                        P: {<IN>}
                        V: {<V.*>}
                        PP: {<P> <NP>}
                        VP: {<V> <NP|PP>*}
                        """)

output1 = chunk1.parse(tagged1)
output2 = chunk2.parse(tagged2)



print(output1)
print("\n\n\n")
print(output2)


# Separate progress
import nltk
from nltk import word_tokenize, pos_tag

text = "It was a quiet impressive essay regarding the content. It could have been more properly structured as there were fewer headings and bullets. Overall good work"

list = pos_tag(word_tokenize(text))

myword = list[0][0]
mypos = list[0][1]

print(mypos)
