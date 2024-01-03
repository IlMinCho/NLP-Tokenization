# NLP-Tokenization

– Tokenization (spaces or fancy)

– Stopping (not or with a list)

– Stemming (not or Porter steps 1a-1c)

– Input (gzip!): train, S&S

– Output: Prefix / Tokens, heaps, stats

-----------------------------------------

Analysis

1. Run your program with fancy tokenization, stopping, and Porter stemming on sense-and-sensibility.gz and look at the -tokens.txt -stats.txt file to see the most frequent terms from Sense and Sensibility. Are the top terms relevant to the story or do they seem like everyday words that aren't particularly to the novel? Support your answer with examples. You may find it useful to skim the summary on Wikipedia to know what words are part of the story.
Based on my data, the most frequently found word was her at number 2561. In fact, it is difficult to find a big connection because it is a word that appears in most novels, but in this novel, two sisters named Elinor and Marianne appear as the main characters, and considering this information, it can be inferred that a woman is the main character.

2.Are there any of those top terms that should have been stopwords? Do the top terms or the list of all tokens suggest any changes to the tokenizing or stemming rules? What are they and why should they be made?
Among the top terms, words such as i, not, you, had, but, have, all, so, my, which, could, no... are unnecessary words to grasp the contents of the novel. These are words that can appear in any novel you read, so we don't need them to get information about the content. However, stopwords need to be modified for the purpose you are trying to get via stat. If we add the stopwords mentioned above, we get a value that ranks the names of characters like Elinor and Marianne higher. In addition, it would be nice not to add additional tokenizing or stemming rules.

3.Figure 4.4. in the textbook (p. 82) displays a graph of vocabulary growth for the TREC GOV2 collection. Create a similar graph for Sense and Sensibility and upload an image of your graph. Note that you should be able to use the -heaps.txt file to generate the graph.
![image](https://github.com/IlMinCho/NLP-Tokenization/assets/73693697/72761bda-854b-420c-9d86-4ed3bbd75189)
This is a graph using the heap data of Sense and Sensibility, the x-axis is the number of tokens, and the y-axis shows the number of unique tokens.


4.Does Sense and Sensibility follow Heaps Law? Why do you think so or think not?
This follows the heap's law. Looking at the data, as the number of tokens increases, the number of unique tokens continues to increase. And since the increasing rate is gradually decreasing, it can be seen as a case of heap's law. Additionally, looking at the graph, it increases relatively steeply at the beginning and gradually flattens as the number of tokens increases, which is a model of heap's law.
