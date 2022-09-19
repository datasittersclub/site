#!/usr/bin/env python
# coding: utf-8

# # DSC Multilingual Mystery 2: Beware, Lee and Quinn!
# 
# <div style='float: right; width: 200px;margin-left: 7px;margin-top: 0px;'>
# <img src='_static/images/bookcovers/dscm2_cover.jpg' alt='DSC M2 book cover' />
# </div>

# ```{index} single: *Book Topics ; Named Entity Recognition (DSC M2)
# ```
# 
# By Lee Skallerup-Bessette and Quinn Dombrowski
# 
# February 27, 2020

# ## Quinn
# 
# ```{index} single: Translations ; name adaptation
# ```
# 
# The differences leap out at you before you even open any of the books. "**Christine** a une idée géniale". Or was the Baby-Sitters Club "L'idée géniale de **Valérie**:? Does "**Bruno** aime **Mélanie**", or is he instead "Un amoureux pour **Anne-Marie**"? There's a case study on the Dutch translation of the Baby-Sitters Club books in [Babysitting the reader: translating English narrative fiction for girls into Dutch (1946-1995](https://www.worldcat.org/title/babysitting-the-reader-translating-english-narrative-fiction-for-girls-into-dutch-1946-1995/oclc/230991531&referer=brief_results)) by Mieke K T Desmet that gets into strategies for localizing a story that takes place in a different cultural context, and the article "[Cultural Understanding in the Indonesian Translation of The Baby-sitters Club](http://paradigma.ui.ac.id/index.php/paradigma/article/view/159)" by Halida Aisyah talk about how the Indonesian translation took a different approach, maintaining the protagonists' foreign names and locations, and only adopting Indonesian cultural references when the American equivalent would've been incomprehensible without some kind of extensive explanation. But I hadn't come across any scholarly literature on translation strategies for The Baby-Sitters Club in French (in any of the translations: Québécois, Belgian, or French from France).
# 
# 
# I had questions, and not just "what did they decide to call Mallory?" (Spoiler alert: in Québécois it's Marjorie, and just like in English, it's the most frequently screwed up name when OCRing the books.) The ghostwriters in the US were working with an extensive "BSC Bible" that had the description and background of every character in Stoneybrook, and further afield in the BSC universe. (This was adapted and published as [The complete guide to The Baby-sitters Club](https://www.worldcat.org/title/complete-guide-to-the-baby-sitters-club/oclc/35328788&referer=brief_results).) But in [DSC Mystery #1: Lee and the Missing Metadata](https://datasittersclub.github.io/site/dscm1/), Lee discovered that at least in Quebec, they were throwing Baby-Sitters Club books at multiple translators, who turned them around in no time at all. How careful were the translators about consistency, in terms of what they called various peripheral characters and places? This was the making of another Data-Sitters Club Multilingual Mystery. (Who are the data-sitters? So glad you asked. Check out [Chapter 2](https://datasittersclub.github.io/site/chapter-2/).)
# 
# 
# Lee and I put our heads together about how we'd start looking into this mystery. We needed a book that we had on hand in all the translations: Québécois, Belgian, French from France (the last of these being the source of the recent French re-releases). We settled on Jessi's Secret Language, on the thought that all the major characters had been established by that point, as well as many peripheral ones. We'd need to compare with some of the other translations, but that would be our starting point.
# 
# ```{index} single: Collaboration ; language knowledge
# ```
# 
# Here's the thing, though: Lee reads French. I don't. I mean, I could probably pick my way through the text and come up with a list of characters and places, but I had other ideas. I wanted to see how French named-entity recognition performed compared to English, when applied to The Baby-Sitters Club.

# ```{index} single: Named Entity Recognition ; explanation
# ```
# 
# ### What’s named-entity recognition?
# Named-entity recognition (often abbreviated NER) is a kind of information extraction task -- basically, trying to identify particular things (like names of people, places, and organizations) in unstructured text, like a novel. (Yeah, I know that novels have structure, but your average plain-text file of a novel's text -- even if it maintains chapter headers and such -- doesn't have the kind of structure that a computer can easily read. I mean, it's not like it's a spreadsheet or something.) There are two major technical approaches: one uses grammar-based rules to identify the things of interest, and the other uses statistical models like machine learning, and requires a ton of labeled data (e.g. texts where a human has already gone through and correctly identified all the things of interest) upfront. Particularly for statistical models, the more your texts resemble the example texts that the model was trained on, the better the NER will perform. These models are most commonly trained on news corpora, or Wikipedia -- not 80's and 90's girls' literature. This sort of thing is a problem in DH more broadly, not just for us Data-Sitters. David Bamman's [LitBank project](https://github.com/dbamman/litbank) (a dataset of annotated excerpts from public domain literature) is one example of how DH scholars can significantly improve the effectiveness of natural-language processing (NLP) by training models on data that looks more like what we're trying to apply it to. But I'll save the question of how, exactly, one goes about training a model for a future Data-Sitters Club Multilingual Mystery. For the moment, let's see how some commonly-used tools perform "out of the box".

# ```{index} single: Tools ; spaCy
# ```
# 
# ```{index} single: Tools ; StanfordNLP
# ```
# 
# ```{index} single: Named Entity Recognition ; spaCy vs Stanford NLP
# ```
# 
# ### The tools
# The two major NLP tools with multilingual coverage are [spaCy](https://spacy.io/) and [Stanford NLP](https://nlp.stanford.edu/software/). To use spaCy, you load it into Python and run it that way. While there's a Python version of Stanford NLP, as of February 2020 it doesn't cover everything -- and entities are one thing that's currently left out. To get entities with Stanford NLP, you have to run a memory-hungry Java program from the command line, with all the joy that comes from setting that up. To make matters worse, Stanford NLP doesn't have an NER model for French: just English, Spanish, German, and Chinese. It's a better comparison to look at English vs. French with the same tool, rather than English with one and French with the other, so for this mystery, we'll be using spaCy.

# ### The texts
# 
# To make it easier to compare the entities from each text, I split up each translation plus the English original into 15 plain text files, one from every chapter. Everything else I left as I got it from ABBYY FineReader (as discussed in [DSC #2: Katia and the Phantom Corpus](https://datasittersclub.github.io/site/dsc2/)), plus the corrections to my (often bad) attempt to transcribe the "handwritten text" portions. I didn't appreciate some implications of that -- I'll get back to it in a bit.

# ```{index} single: spaCy ; getting started
# ```
# 
# ### Getting started with spaCy
# 
# SpaCy is run via Python, so it can seem a little intimidating if you've never worked with a programming language before. For this mystery, I set up a Jupyter notebook in the Data-Sitters Club GitHub repo that you can download and use for your own texts. (If you're not familiar with Jupyter notebooks, [here's a Programming Historian tutorial](https://programminghistorian.org/en/lessons/jupyter-notebooks).)
# 
# You can't run the exact same experiment I did without access to the same texts I have (which I can't share for copyright reasons), but the Jupyter notebook on GitHub has all the output I got running it on the Baby-Sitters Club corpus, so you can see the results of the process one step at a time.

# ```{index} single: spaCy ; downloading models
# ```
# 
# #### 1. Downloading spaCy models
# 
# The first step is to download the spaCy models; this notebook has been updated for spaCy 3. These models have been pre-trained on annotated French and English corpora, respectively. You only have to run these code cells below the first time you run the notebook; after that, you can skip right to step 2 and carry on from there. (If you run them again later, nothing bad will happen; it'll just download again.) You can also run spaCy in other notebooks on your computer in the future, and you’ll be able to skip the step of downloading the models.

# In[1]:


#Imports the module you need to download and install the spaCy French and English models
import sys


# In[2]:


#Installs the French spaCy model
get_ipython().system('{sys.executable} -m spacy download fr_core_news_sm')


# In[3]:


#Installs the English spaCy model
get_ipython().system('{sys.executable} -m spacy download en_core_web_sm')


# #### 2. Importing spaCy and setting up NLP
# Run the code cell below to import the spaCy module, and create two functions: one which loads the French model and runs the NLP algorithms ( includes named-entity recognition), and one which does the same for the English. 

# In[4]:


#Imports spaCy
import spacy
#Imports the French model
import fr_core_news_sm
#Sets up a function so you can run the French model on texts
frnlp = fr_core_news_sm.load()
#Imports the English model
import en_core_web_sm
#Sets up a function so you can run the English model on texts
ennlp = en_core_web_sm.load()


# #### 3. Importing other modules
# There’s various other modules that will be useful in this notebook. The code comments explain what each one is for. This code cell imports all of those.

# In[5]:


#io is used for opening and writing files
import io
#glob is used to find all the pathnames matching a specified pattern (here, all text files)
import glob
#os is used to navigate your folder directories (e.g. change folders to where you files are stored)
import os


# #### 4. Diretory setup
# Assuming you’re running Jupyter Notebook from your computer’s home directory, this code cell gives you the opportunity to change directories, into the directory where you’re keeping your French text files. (This notebook is designed to deal with one language at a time, and assumes your French text files are in one folder, and English are in another.)
# 
# Replace `/Users/qad/Documents/dsc/dscm2` with the full path to the directory with your files.
# 
# For instance, the default path to the Documents directory is (substituting your user name on the computer for YOUR-USER-NAME):
# 
# - On Mac: '/Users/YOUR-USER-NAME/Documents'
# - On Windows: 'C:\\\Users\\\YOUR-USER-NAME\\\Documents'

# In[6]:


#Define the file directory here
filedirectory = '/Users/qad/Documents/dsc/dscm2'
#Change the working directory to the one you just defined
os.chdir(filedirectory)


# ### Running spaCy

# ```{index} single: Named Entity Recognition ; for French
# ```
# 
# ```{index} single: spaCy ; French named entity recognition
# ```
# 
# #### 5. French NER, first try
# 
# The code cell in step 5 in the Jupyter notebook iterates through the files in the folder you specified up in step 4, after sorting them alphabetically. For every file that ends in .txt (an important limitation -- you'll get an error if you try to have Python open a file that isn't a text file, including those pesky invisible .DS_STORE files in just about every Mac folder), the code defines an output file name that involves appending '_ner_per.txt' to the end of the input filename.
# 
# Opening the input file (i.e. each file in turn, one at a time) and the newly-created, empty output file, the code reads in the text of the input file, and runs the spaCy French NLP. Then, for every word recognized as an entity, as long as it's an entity labeled 'PER' (a person), the entity is written to the screen (with a print command) and to the output file. I thought it'd be easiest to work through the entities one type at a time, starting just with the character names.\
# I wrote this code, a couple times pulling up previous notebooks I'd written that did similar things, and consulting the [spaCy documentation and examples](https://spacy.io/usage/linguistic-features#named-entities) for how to display the entities.

# In[7]:


#Sort all the files in the directory you specified above, alphabetically.
#For each of those files...
for filename in sorted(os.listdir(filedirectory)):
    #If the filename ends with .txt (i.e. if it's actually a text files)
    if filename.endswith('.txt'):
        #Write out below the name of the file
        print(filename)
        #The file name of the output file adds _ner_per to the end of the file name of the input file
        outfilename = filename.replace('.txt', '_ner_per.txt')
        #Open the input filename
        with open(filename, 'r') as f:
            #Create and open the output filename
            with open(outfilename, 'w') as out:
                #Read the contents of the input file
                chaptertext = f.read()
                #Do French NLP on the contents of the input file
                chapterner = frnlp(chaptertext)
                #For each recognized entity
                for ent in chapterner.ents:
                    #If that entity is labeled as a person
                    if ent.label_ == 'PER':
                        #Print the entity, and the label (which should be PER)
                        print(ent.text, ent.label_)
                        #Write the entity to the output file
                        out.write(ent.text)
                        #Write a newline character to the output file
                        out.write('\n')
            


# And it worked... mostly? It was super weird that *J'ai* kept getting listed, but I wasn't too worried. A quirk of the model, plus the source text! Probably the model wasn't trained on first-person narratives like The Baby-Sitters Club. Yeah, there was also an example of *C'* that was harder to explain, but it wasn't until I saw an example of a double-curly-quote character (") identified as an entity that I started getting suspicious. Could those be messing things up somehow?
# 
# *(Note from July 19, 2021: these were errors that the spaCy 2 French model made. Almost all disappeared by spaCy 3, which is the source of the results you see above.)*

# ```{index} single: Data; data cleaning for NER
# ```
# 
# #### 6. Data cleaning
# Time for some data cleaning! When Lee brought the ABBYY FineReader output .txt files into Word to correct my bad transcriptions, Word "helpfully" replaced all the regular, straight single and double quotes with their curly equivalents. 
# 
# I wrote some code that opened every text file in my folder, searched for opening and closing curly quotes and replaced them with the “straight quote” character (a quotation mark that doesn’t differentiate opening and closing quotes). While I was at it, I saw that some of the texts weren’t using the straight single quote for the apostrophe, so I put that in there, too. This code overwrites the text files in the folder (rather than creating a new version) so if you want to keep your originals, make sure you have a copy elsewhere.

# In[8]:


# Look for files in the source directory that end in .txt
for filename in os.listdir(filedirectory):
    if filename.endswith(".txt"):
        
        #Open each file that ends in .txt
        f = open(filename, 'r')
        #Read the text
        text = f.read()
        #Replace curly double-quote with straight double-quote
        lines = text.replace("“", '"')
        lines = lines.replace('”', '"')
        #Replace curly singl-quote with straight single-quote
        lines = lines.replace('’', "'")

        #Write output to a new file with the same name as the original, overwriting the original file.
        with open(filename, 'w') as out:
            out.writelines(lines)


# ```{index} single: Named Entity Recognition ; for French
# ```
# 
# ```{index} single: spaCy ; French named entity recognition
# ```
# 
# #### 7. French NER, second try
# I didn’t make any changes to the code from step 5, but check out the difference in the results. Gone are those quotation marks as so-called entities -- along with all the examples of j’ai, c’, etc. All of those were showing up because they were using the curly single quote character, and that was messing up spaCy’s model.

# In[9]:


#Sort all the files in the directory you specified above, alphabetically.
#For each of those files...
for filename in sorted(os.listdir(filedirectory)):
    #If the filename ends with .txt (i.e. if it's actually a text files)
    if filename.endswith('.txt'):
        #Write out below the name of the file
        print(filename)
        #The file name of the output file adds _ner_per to the end of the file name of the input file
        outfilename = filename.replace('.txt', '_ner_per.txt')
        #Open the infput filename
        with open(filename, 'r') as f:
            #Create and open the output filename
            with open(outfilename, 'w') as out:
                #Read the contents of the input file
                chaptertext = f.read()
                #Do French NLP on the contents of the input file
                chapterner = frnlp(chaptertext)
                #For each recognized entity
                for ent in chapterner.ents:
                    #If that entity is labeled as a person
                    if ent.label_ == 'PER':
                        #Print the entity, and the label (which should be PER)
                        print(ent.text, ent.label_)
                        #Write the entity to the output file
                        out.write(ent.text)
                        #Write a newline character to the output file
                        out.write('\n')


# It’s not perfect: chapter 1 of the Quebec translation flags “mange Julie” (Julie eats) as a person instead of a name and noun. But it’s a lot better.

# ```{index} single: Named Entity Recognition ; for French places
# ```
# 
# ```{index} single: spaCy ; French named entity recognition for places
# ```
# 
# #### 8. French NER for places
# 
# I moved all the \_ner_per.txt files into their own folder, so that spaCy wouldn’t try to run NER on text files of its own NER results, and would instead just use the files with the chapter texts as the objects of investigation.
# 
# I changed the code from step 7 (and 5) to replace PER with LOC and ran it again to get location entities.
# 

# In[10]:


#Sort all the files in the directory you specified above, alphabetically.
#For each of those files...
for filename in sorted(os.listdir(filedirectory)):
    #If the filename ends with .txt (i.e. if it's actually a text files)
    if filename.endswith('.txt'):
        #Write out below the name of the file
        print(filename)
        #The file name of the output file adds _ner_lov to the end of the file name of the input file
        outfilename = filename.replace('.txt', '_ner_loc.txt')
        #Open the infput filename
        with open(filename, 'r') as f:
            #Create and open the output filename
            with open(outfilename, 'w') as out:
                #Read the contents of the input file
                chaptertext = f.read()
                #Do French NLP on the contents of the input file
                chapterner = frnlp(chaptertext)
                #For each recognized entity
                for ent in chapterner.ents:
                    #If that entity is labeled as a person
                    if ent.label_ == 'LOC':
                        #Print the entity, and the label (which should be PER)
                        print(ent.text, ent.label_)
                        #Write the entity to the output file
                        out.write(ent.text)
                        #Write a newline character to the output file
                        out.write('\n')


# Skimming the results, it was interesting to see how much worse it performed than the person entity recognition. It feels like a minority of the results are legit places, and most of the results are people’s names.

# ```{index} single: Named Entity Recognition ; for French organizations
# ```
# 
# ```{index} single: spaCy ; French named entity recognition for organizations
# ```
# 
# #### 9. French NER for orgs
# I was curious what I'd get by looking for entities flagged as organizations. I mean, this entire book series is about an organization: would that get flagged correctly? (Once again, I moved the \_ner_loc.txt files into their own folder first.)
# 
# The verdict: *Club des Baby* (France-French translation) and Club des baby (Quebec translation) get marked as organizations; the "sitters" gets lost when "Baby-sitters" gets separated at the hyphen. There's also various things that are most definitely not organizations that get tagged, like "Bonjour!" in Belgian ch. 10, or "PLIÉ" in Quebec ch. 3 (maybe spaCy thought it was an acronym and not a yelling dance teacher?)

# In[11]:


#Sort all the files in the directory you specified above, alphabetically.
#For each of those files...
for filename in sorted(os.listdir(filedirectory)):
    #If the filename ends with .txt (i.e. if it's actually a text files)
    if filename.endswith('.txt'):
        #Write out below the name of the file
        print(filename)
        #The file name of the output file adds _ner_org to the end of the file name of the input file
        outfilename = filename.replace('.txt', '_ner_org.txt')
        #Open the infput filename
        with open(filename, 'r') as f:
            #Create and open the output filename
            with open(outfilename, 'w') as out:
                #Read the contents of the input file
                chaptertext = f.read()
                #Do French NLP on the contents of the input file
                chapterner = frnlp(chaptertext)
                #For each recognized entity
                for ent in chapterner.ents:
                    #If that entity is labeled as a person
                    if ent.label_ == 'ORG':
                        #Print the entity, and the label (which should be PER)
                        print(ent.text, ent.label_)
                        #Write the entity to the output file
                        out.write(ent.text)
                        #Write a newline character to the output file
                        out.write('\n')


# ```{index} single: Named Entity Recognition ; for French misc entities
# ```
# 
# ```{index} single: spaCy ; French named entity recognition for misc entities
# ```
# 
# #### 10. French NER for misc
# The French entity model also has a “MISC” type, so for the sake of completeness, I couldn’t not try it. And the results are as advertised. Lots of names. Lots of “Ça”. There’s a “Tu es atroce” (You’re excruciating) from Ch. 5 of the France French version. “Le Langage Secret” in Ch. 6 of the Belgian translation gets flagged, and “P'tit” makes an appearance more than once. Only in the France French version do “Noirs” (Black people) and “Noire de mon école” (Black person in my school) get flagged.
# 
# *(July 19, 2021 note: this is clearly another area where there's been a lot of improvement between spaCy 2 and spaCy 3. There's still some weird stuff, like "Oh!" and "Salut", but overall a lot fewer results and a lot less garbage.)*

# In[12]:


#Sort all the files in the directory you specified above, alphabetically.
#For each of those files...
for filename in sorted(os.listdir(filedirectory)):
    #If the filename ends with .txt (i.e. if it's actually a text files)
    if filename.endswith('.txt'):
        #Write out below the name of the file
        print(filename)
        #The file name of the output file adds _ner_misc to the end of the file name of the input file
        outfilename = filename.replace('.txt', '_ner_misc.txt')
        #Open the infput filename
        with open(filename, 'r') as f:
            #Create and open the output filename
            with open(outfilename, 'w') as out:
                #Read the contents of the input file
                chaptertext = f.read()
                #Do French NLP on the contents of the input file
                chapterner = frnlp(chaptertext)
                #For each recognized entity
                for ent in chapterner.ents:
                    #If that entity is labeled as a person
                    if ent.label_ == 'MISC':
                        #Print the entity, and the label (which should be PER)
                        print(ent.text, ent.label_)
                        #Write the entity to the output file
                        out.write(ent.text)
                        #Write a newline character to the output file
                        out.write('\n')


# ```{index} single: Named Entity Recognition ; for English
# ```
# 
# ```{index} single: spaCy ; English named entity recognition
# ```
# 
# ### Let’s do it all again for English
# The steps below in the notebook basically repeat the process described above, but using the spaCy model for English instead of French. At first, I just copied over the code cells from the French section (switching out `enfiledirectory` for `filedirectory` in the first line so it looked in the right place for the English files), but kept getting some bizarre output: namely, it wasn’t able to find any entities labeled PER or LOC.
# 
# To figure out what was going on, I removed the line `if ent.label_ == 'PER':` 
# and un-indented the code nested inside it, to avoid Python indentation errors, then commented-out the following out.write lines by putting a # in front of them. I didn’t want to write any results, I just wanted to see what entities it found.
# 
# Lo and behold, there were lots of entities, with more different entity labels than available for French. There’s GPE (geopolitical entity, AKA location, but not any of the locations that are like “so-and-so’s room”), DATE, CARDINAL (number type), LANGUAGE (seems relevant for Jessi’s Secret Language), TIME (e.g. “the morning of the day”), DATE (things like “a few weeks”, or, strangely, “eight-year-old”), PERSON (not PER).
# 
# First, we have to put in the path to the English files, then change to that directory:

# In[15]:


#Put in the path here, using the same conventions as described above in step 4
enfiledirectory = '/Users/qad/Documents/dsc/dscm2/en'
os.chdir(enfiledirectory)


# #### 11. English NER for people
# 
# ```{index} single: Named Entity Recognition ; for English people
# ```
# 
# ```{index} single: spaCy ; English named entity recognition for people
# ```

# In[16]:


#Sort all the files in the directory you specified above, alphabetically.
#For each of those files...
for filename in sorted(os.listdir(enfiledirectory)):
    #If the filename ends with .txt (i.e. if it's actually a text files)
    if filename.endswith('.txt'):
        #Write out below the name of the file
        print(filename)
        #The file name of the output file adds _ner_per to the end of the file name of the input file
        outfilename = filename.replace('.txt', '_ner_per.txt')
        #Open the infput filename
        with open(filename, 'r') as f:
            #Create and open the output filename
            with open(outfilename, 'w') as out:
                #Read the contents of the input file
                chaptertext = f.read()
                #Do English NLP on the contents of the input file
                chapterner = ennlp(chaptertext)
                #For each recognized entity
                for ent in chapterner.ents:
                    #If that entity is labeled as a person
                    if ent.label_ == 'PERSON':
                        #Print the entity, and the label (which should be PER)
                        print(ent.text, ent.label_)
                        #Write the entity to the output file
                        out.write(ent.text)
                        #Write a newline character to the output file
                        out.write('\n')


# #### 12. English NER for places
# ```{index} single: Named Entity Recognition ; for English places
# ```
# 
# ```{index} single: spaCy ; English named entity recognition for places
# ```

# In[17]:


#Sort all the files in the directory you specified above, alphabetically.
#For each of those files...
for filename in sorted(os.listdir(enfiledirectory)):
    #If the filename ends with .txt (i.e. if it's actually a text files)
    if filename.endswith('.txt'):
        #Write out below the name of the file
        print(filename)
        #The file name of the output file adds _ner_loc to the end of the file name of the input file
        outfilename = filename.replace('.txt', '_ner_loc.txt')
        #Open the infput filename
        with open(filename, 'r') as f:
            #Create and open the output filename
            with open(outfilename, 'w') as out:
                #Read the contents of the input file
                chaptertext = f.read()
                #Do English NLP on the contents of the input file
                chapterner = ennlp(chaptertext)
                #For each recognized entity
                for ent in chapterner.ents:
                    #If that entity is labeled as a person
                    if ent.label_ == 'GPE':
                        #Print the entity, and the label (which should be PER)
                        print(ent.text, ent.label_)
                        #Write the entity to the output file
                        out.write(ent.text)
                        #Write a newline character to the output file
                        out.write('\n')


# ```{index} single: Named Entity Recognition ; for English organizations
# ```
# 
# ```{index} single: spaCy ; English named entity recognition for organizations
# ```
# 
# #### 13. English NER for organizations
# I think my favorite entity type is ORG, which gets you everything from Oakley Elementary to Swanilda to Mama. (Yes, friends, “Daddy” is a PERSON but “Mama” is an ORG.)

# In[18]:


#Sort all the files in the directory you specified above, alphabetically.
#For each of those files...
for filename in sorted(os.listdir(enfiledirectory)):
    #If the filename ends with .txt (i.e. if it's actually a text files)
    if filename.endswith('.txt'):
        #Write out below the name of the file
        print(filename)
        #The file name of the output file adds _ner_org to the end of the file name of the input file
        outfilename = filename.replace('.txt', '_ner_org.txt')
        #Open the infput filename
        with open(filename, 'r') as f:
            #Create and open the output filename
            with open(outfilename, 'w') as out:
                #Read the contents of the input file
                chaptertext = f.read()
                #Do English NLP on the contents of the input file
                chapterner = ennlp(chaptertext)
                #For each recognized entity
                for ent in chapterner.ents:
                    #If that entity is labeled as a person
                    if ent.label_ == 'ORG':
                        #Print the entity, and the label (which should be PER)
                        print(ent.text, ent.label_)
                        #Write the entity to the output file
                        out.write(ent.text)
                        #Write a newline character to the output file
                        out.write('\n')


# ```{index} single: Named Entity Recognition ; for English works of art
# ```
# 
# ```{index} single: spaCy ; English named entity recognition for works of art
# ```
# 
# #### 14. English NER for works of art
# That said, there’s also a rare WORK_OF_ART entity type, exemplified by “Morning, Squirts”, “Hey, Jessi”, “On Top of Old Smoky” (depends on how you feel about folk music, I guess), and, my very favorite work of art, “Nope”.
# ![Grumpy Cat says nope](_static/images/dscm2_nope.jpg)
# 
# *(July 19, 2021 note: Alas, spaCy 3 has learned that 'nope' isn't a work of art. 😔 It was fun while it lasted.)*

# In[19]:


#Sort all the files in the directory you specified above, alphabetically.
#For each of those files...
for filename in sorted(os.listdir(enfiledirectory)):
    #If the filename ends with .txt (i.e. if it's actually a text files)
    if filename.endswith('.txt'):
        #Write out below the name of the file
        print(filename)
        #The file name of the output file adds _ner_art to the end of the file name of the input file
        outfilename = filename.replace('.txt', '_ner_art.txt')
        #Open the infput filename
        with open(filename, 'r') as f:
            #Create and open the output filename
            with open(outfilename, 'w') as out:
                #Read the contents of the input file
                chaptertext = f.read()
                #Do English NLP on the contents of the input file
                chapterner = ennlp(chaptertext)
                #For each recognized entity
                for ent in chapterner.ents:
                    #If that entity is labeled as a person
                    if ent.label_ == 'WORK_OF_ART':
                        #Print the entity, and the label (which should be PER)
                        print(ent.text, ent.label_)
                        #Write the entity to the output file
                        out.write(ent.text)
                        #Write a newline character to the output file
                        out.write('\n')


# ### What now?
# I reran the notebook for English, reluctantly limiting myself to the entity types held in common between the English and French models. So now I had, chapter-by-chapter, translation-by-translation (plus original English), all the person, location, and organization type entities.
# 
# That’s nice.
# 
# But that wasn’t my question: what I wanted to know was how the translators adapted people and place names. I had to figure out what to do with all these text files to get me closer to an answer.
# 
# I had some thinking to do.
# 

# ## Lee
# 
# ```{index} single: Disability; as depicted in Jessi's Secret Language
# ```
# 
# So, before getting into the finer differences between the various translations and the approaches taken by the translators, can we just take a second to appreciate the narrative of this BSC story? Now, far from perfect as a disability narrative -  for instance, the main deaf character never gets to "speak" for himself, with instead his older sister "speaking" both for him and for herself - this is a really nuanced portrayal of difference and empathy. All I remember from when I read the book (sigh) 30 years ago was the dancing J sign for Jessi's name, but now I'm struck by how Jessi/Jessie/Justine/Jessica is wise beyond her years, a reflection of her own experiences with being different in her new hometown. I got a little choked up as I read (at least the first of the four different times I read it) her efforts to bring the deaf schoolkids to the show, and how her frenemy at ballet finally connects with her own deaf sister.
# 
# ```{index} single: Race ; as depicted in Jessi's Secret Language
# ```
# 
# 
# And when Jessi said that her performance could never be perfect because "There was no way Swanilda could have been black, so I wasn't perfect, but I knew I was dancing very well"? Gutted. In every French version(s).
# 
# ```{index} single: Translations ; handling sign language
# ```
# 
# There's another layer to this discussion of translation as there is another language in the text: sign language. As pointed out in the narrative(s), there are many different variations of sign language, which means that the translators had to accurately "translate" the signs that were being done, as it wasn't the same in the various French dialects.
# 
# So, a fun little close-reading exercise on my part, once I stopped crying, I mean, YOU'RE CRYING NOT ME.
# 
# ```{index} single: Translation ; localization for Europe
# ```
# 
# In order of levels of translation/cultural adaptation, it goes: Belgium, Quebec, France. The Belgium translation takes great pains to situate the narrative in an environment that would be familiar to a European reader: the names have all been francisized (even Claudia Kishi becomes Julie Kishi), and the places have been localized as well. Justine and her family are not from New Jersey but Burkina Faso. Interestingly, they move to Neuville, France, and not Belgium. Sophie Lambert (aka Stacey McGill) moves back to Paris and not New York City, while Carole (aka Dawn) is "une vraie Provençale" rather than a California girl. These localized adaptations extend to any cultural reference (such as books and board games) and particularly in this volume, the gross-out songs Mallory/Marjorie's brothers sing at dinner about spaghetti.
# 
# At least I think it is. I'm not so up on Franco-Belgium gross-out songs about pasta dishes.
# 
# ```{index} single: Translation ; localization for Quebec
# ```
# 
# In the Quebec translation, the names are all again mostly francisized (seriously, though, I knew kids with like ¾ of the last names chosen for the kids here), and the place names stay also mostly the same: Jessie Raymond is from New Jersey and Diane Dubreuil is from California, but Sophie Ménard moves back to Toronto. The cultural references are either rendered local (OH GOD LOOK HERE IS A REFERENCE TO FREAKING CAILLOU) or completely neutralized (like Claudia's stash of now non-brand name snacks - a missed opportunity to get some local references to Vachon snack cakes). They sing the same spaghetti song in the Quebec translation as the Belgium one, but there is one really interesting difference choice that the Quebec translators make in multiple (ok, the two that I've read) volumes: if it is a question of how to translate something, they just ignore it and erase it.
# 
# For example, in this volume, in the original English, Jessi's new ballet teacher keeps getting her name wrong. That is preserved in both the French from France and French from Belgium translations, but not the Quebec one, where Jessie just gets confused that she is being called Madame Raymond rather than by her first name. This might just be a result of the initial name-choice for Jessie in Quebec: it's kinda hard to mess up Raymond. So rather than force the issue, it was just tweaked.
# 
# More interestingly, when reading of the mysteries in Quebec translation, California figured prominently (it's one of the ones featuring the child actor from their hometown), but other than one reference to the kid coming home, all other references to California or things that may or may not have happened in California in other volumes are just simply removed and erased.
# 
# (Not to mention that having a FRANCOPHONE child star starring in a FRANCOPHONE show for FRANCOPHONE kids be recorded in California when OH I DON'T KNOW THERE IS A LOCAL FRANCOPHONE TV/MOVIE INDUSTRY IN MONTREAL and then remove all other references to California seems to me like a missed opportunity, but I digress. Seriously. Have them live in a suburb outside of Quebec City or Sherbrooke and then send him to Montreal to be a star. It works. It makes sense. I mean, there is no movie industry that I know of in Provençal so having the other Baby-Sitters visit Provençal and run into said child star unless that's where he summers now makes zero sense but it didn't stop the Belgium translators...)
# 
# Ok, wait, what were we talking about...
# 
# ```{index} single: Translation ; lack of localization for France
# ```
# 
# So, Belgium goes all-in on translation and adaptation, Quebec splits the difference (it would make sense that a kid from New Jersey or California would end up at a French school because THANKS BILL 101!), while France makes zero effort to mask that these are American kids doing American things and that while the story is in French, the references and names and such remain firmly American.
# 
# Most of the names remain largely English (although bizarrely Claudia Kishi becomes Claudia Koshi), as do the place names, except for Stoneybrooke (which would almost be like a sci-fi or fantasy place name that you see and have no idea how to pronounce for any French audience), which becomes Stamford, Connecticut, unlike Neuville, France or Quebec's generic Nouville with no province/state/country associated with it. Even a cultural reference, in this case a book, gets changed to a more recognizable American title: Bambi. It is a different gross-out spaghetti song sung at dinner, which is not recognizable to me either, and may be the only notable instance of adaptation in the French-from-France translation.
# 
# The varying approaches to translating/adapting the text is perhaps most noticeable in how the three different translations deal with sign language. The Belgium translation goes into great detail about which version of sign language that is being used and taught. The Quebec translation drops in a mention of Québécois sign language, while the French-from-France translation is like, meh, it's sign language, you get it. I don't know enough about the different sign languages to know if the adaptations are accurate or not for the various different sign languages, but the French-from-France translation explains sign language even less than the original English text (which does identify that they are learning and using American Sign Language as opposed to Signed English or British Sign Language, which is actually based off of French Sign Language).
# 
# I didn't notice (so thank-you Quinn for that helpful chart below!) that the reference to the architect of the neighborhood isn't mentioned in the France or Belgium translations, which again, makes cultural sense. These "planned communities" and post-WWII suburbs are a uniquely North American phenomenon, but one that wouldn't have been foreign to a Quebec audience (my grandparent's neighborhood was like that, for instance) but wouldn't have made much sense to a European audience, so even with France going all-in on the Americanness of the books, they still took care to ensure that the references weren't so foreign as to be unrecognizable to a reader.
# 
# So, to recap, Belgium goes all-in on a European adaptation of the book, Quebec splits the difference, and France doesn't seem to care, and in fact would seem to emphasize the americanness of the text. This all makes sense from a marketing perspective. Belgium is a smaller market, and so making the books hyper-local would limit the sales appeal to other Francophone readers. Quebec had a basically captured market, and their efforts reflect real efforts to appeal to the local market, while also not trying to make things too complicated for the army of translators they were employing to churn out these translations. France, well, France is France and France is gonna France, and probably figured who cares, you know it's the USA, we know it's the USA, you're going to buy the books in part for that reason, so...let's just make sure you can pronounce all the names.
# 
# I realize that this is probably not the level of cultural analysis that you all are expecting from this. But when you ask someone from Quebec to reflect on cultural/linguistic choices that France makes...we in Quebec have an Office de la langue française, one of whose tasks is to make up new French words every time there is a new English word that comes along. France says things like "stopping" and "shopping" where in Quebec WE DO NOT SAY SUCH THINGS USE THE PROPER FRENCH VERBS NOT SOME BASTARDIZED ENGLISH GERUND SAID WITH A PARISIAN ACCENT.
# 
# So that France goes all-in on the Americanness of the series isn't surprising. That Quebec didn't go more all-in in the adaptation to a local audience was, but given the limitations due to pressures to produce, it is understandable.
# 
# ## Quinn
# 
# ```{index} single: Reading with your eyeballs
# ```
# 
# Lee's take on BSC names in translation had got me thinking. For starters, score one for close reading! If you've got four variations of a children's novel, and want to say something about some aspect of that novel, you should not start by opening a Jupyter notebook. Put down your laptop, find a comfy chair, and just read the books with your own eyeballs. It definitely took Lee less time to do that than it took me to scan and OCR the books, reformat them into individual chapters, clean up the punctuation characters, and write some Python code. And by the end, she could sit down and write something. I, on the other hand, had 180 additional small text files on my laptop to show for it, and nothing new to say yet. Woot.
# 
# ```{index} single: Collaboration ; domain expertise vs computation
# ```
# 
# But then I thought about what Lee didn't do there. Knowledgeable humans are great at providing a synthesis of the interesting things they've noticed in a text. What they're less great at is being comprehensive, pulling out details that aren't individually interesting, but may become interesting in the aggregate. It's tedious work, and it's only possible with a lot of manual labor -- unless you use digital tools. (And even still, let's face it, there's a lot of manual work that goes into getting your text ready for digital tools.)
# 
# ```{index} single: BSC Bible
# ```
# 
# 
# ![BSC Bible cover](_static/images/bsc_bible.jpg)
# 
# In my moment of doubt, I turned to the Bible -- the BSC Bible, that is. Smith College's Special Collections finding aid for the Ann M. Martin papers actually [includes that as an alternate title for The Complete Guide to The Baby-Sitters Club](https://findingaids.smith.edu/repositories/3/archival_objects/331319), the complete (through 1996) compendium of all information about all people (my PER/PERSON entities), places (LOC/GPE), and things (including ORGs) in the Baby-Sitters Club universe. And by all, I mean all. Find any arbitrary character, however niche, and this book has all the information in the canon. Does anyone remember Nicole Lavista, one of the "Battle of the Bakers" daycare kids in BSC Mystery #21: Claudia and the Recipe for Danger? Me, neither. But she's six years old, has "hair in black curls", is "full of tricks", and "loves to draw and paint". There's even page-level citations, though they do me no good since we chose to remove page numbers from the text file output of our OCR. All this information is already compiled for the English series through the BSC Bible, originally as a resource for the ghostwriters. But what might we learn from trying to recreate something similar from the ground up, for the universe of each of the French translations? In addition to the question of how much localization has been done, the question of consistency intrigues me. If you're not localizing much of anything, it's less of an issue, but was the pool of translators in Montreal comparing notes about how they adapted the names of peripheral but at least occasionally-recurring characters?
# 
# ### Rethinking NER
# 
# ```{index} single: Named Entity Recognition ; future steps
# ```
# 
# I wanted to write up NER for this book because, hey, names! And I've done it before, and it seemed like a fun opportunity to compare the performance of spaCy's French and English models. Ultimately, though, NER makes more sense as the primary method of finding names and places when you're dealing with a much larger corpus, and/or a much more heterogenous one than Baby-Sitters Club books. It's feasible to make a list of characters and places within a single fictional universe, like what you can find in the BSC Bible, even if you have all 200ish novels in translation. It's much less feasible if you have 200 novels, each in its own universe -- let alone 2,000 or more.
# 
# So where to go from here? It'd be fun to try to annotate some texts and see if I can train a better NER model for the Baby-Sitters Club (especially the French), but that's a topic for another DSC Multilingual Mystery. Instead, what I have now for locations, I can use to cross-check with the English, for an easy and interesting source of likely localizations and differences. With names, I can hopefully use NER to identify characters that are newly-introduced in each book (or perhaps re-introduced under a different localized name?), and then add those names to the list of known characters in that translated universe. That curated list, rather than NER itself, will be the basis for checking translations for references to characters. And another thing: for best chances of identifying new characters, I think I'll stop limiting the NER results to just the entities flagged PER. Too many character names are showing up as LOC or ORG to trust the classification. As for the ORG entities specifically, they're almost all errors of one sort or another. I can't think of any good research questions offhand that deal with organizations in this universe, so I think I won't worry about them.
# 
# ### Close-reading some distant-reading outputs
# 
# For lulz, I threw the location NER per-chapter output for the Belgian corpus into Voyant, and even the word cloud was mostly a testament to how badly the model performed at classifying entities as locations.
# 
# ![Voyant visualization of allegedly location named entities, but it's mostly names](_static/images/dscm2_ner_voyant.png)
# 
# So in the end, I deleted all those little NER output files I'd generated with the Jupyter notebook, with aspirations of somehow comparing them programmatically. Instead, those Python print() statements in the notebook were what I consulted -- using my own eyeballs. Because the chapters are so short, it's not hard to trace place names back to the context, and then find that same context in the original. I'm about halfway there to imagining how I'd implement something more scalable in Python for checking at least the entities that refer to people (whether or not they're tagged that way). But honestly, for my own process, I find that I need to spend time cleaning data manually before I feel like I understand it well enough to come up with a workable programmatic approach.
# 
# Here's some things I found following up on some of the words tagged as locations in the NER:
# 
# ```{index} single: Translation ; localization of Jessi's origins
# ```
# 
# * In the Belgian translation, Justine Victoire is from Ouagadougou, Burkina Faso (as Lee mentioned). Her best friend / cousin in Ouagadougou is named Johanna. Neuville is a small town not far from Aubrives, where her father works. Justine's linguistic aptitude was put to the test on a family trip to Spain. Her sister's name is adapted as Roseline, and her brother is Victor, AKA Gringalet.
# 
# ```{index} single: Translation ; localization of where Jessi learned Spanish
# ```
# 
# * In the Quebec translation, like in the English original and France French translation, Jessie picked up Spanish in Mexico. Jessi's best friend/cousin Keisha becomes Kara. Her sister is still Becca, but her brother becomes Jean-Philippe, AKA Jaja. To Lee's point of the Quebec translation just deleting things when they complicate matters too much: there's no mention of Jessi's father working in another city. They moved to Nouville for his job, end of discussion.
# 
# * In the France French translation... well, see Lee's section for details. It's just like the English original, just in French. The only exception of note is that her little brother, John Philip Ramsey Junior (yes, that whole thing is his name in French too, including the "Junior"), is nicknamed "P'tit Bout" instead of Squirt. (Sorry for being baffled by your inclusion of "P'tit" among the entities, spaCy. You were right.)
# 
# * As of Belgian BSC #16, Sophie Lambert has moved back with her family to Paris. Meanwhile, Carole Leroy has moved to Neuville from Provence along with her brother (still named David). Both the Belgian and the France-French versions take a "just-the-facts" approach to Dawn's situation, but the translators in Montreal were willing to take on Jessi's compassionate editorializing: "Comme le dit si souvent Diane, sa famille est déchirée en deux, mais je suis certaine qu'elle va s'en sortir." / "As Dawn pointed out, her family is now ripped in half. I think Dawn is a survivor, though."
# 
# * In the Belgian translation, Jessi's ballet school is in Aubrives (consistent with her father also working there).
# 
# ```{index} single: Translation ; soccer vs football
# ```
# 
# * Belgian Mathieu thinks that Marseille will beat Monaco in soccer, rather than the Patriots winning the Super Bowl. In Quebec, Matthieu talks about the "Patriotes" winning the soccer eliminations -- a sort of mixed-reference there. The French are all in for the Patriots and the Super Bowl.
# 
# And here's some notes and a list of the name correspondences, working from the PER tags:
# 
# * Chapter 5 starts with "Brat, brat, brat." in English. All the French translations skip that part and go straight into the next sentence about how everyone agrees that Jenny Prezzioso is spoiled and a little bratty (Lee adds: She really, really is. Reading it four times really drives that point home. How many synonyms in French for "spoiled brat"? A lot and it is amazing).
# 
# ```{index} single: Translation ; name inconsistency within a book
# ```
# 
# * Even without having to compare across books, I managed to find a naming inconsistency! One of Jessi's dance colleagues, Mary Bramstedt, is given the role of a villager. In the Quebec version, her name is first translated as Marie Brazeau. Later, there's a reference to Mademoiselle Croteau, which Jessi explains: "(c'est Marie, une citoyenne dans le ballet)". So either the Quebec translator innovated a second Marie, dancing the same part as the first one, or... the translator forgot the surname they used earlier.
# 
# ```{index} single: Translation ; localized names
# ```
# 
# 
# | English                               | Quebec                           | Belgium                                                     | France                       |
# | ------------------------------------- | -------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
# | Kristy Thomas                         | Christine Thomas                 | Valérie Demoulin                                            | Kristy Parker                                               |                                          |
# | Mary-Anne Spier                       | Anne-Marie Lapierre              | Mélanie Moreau                                              | Mary Anne Cook                                              |                                          |
# | Claudia Kishi                         | Claudia Kishi                    | Julie Kishi                                                 | Claudia Koshi                                               |                                          |
# | Stacey McGill                         | Sophie Ménard                    | Sophie Lambert                                              | Lucy MacDouglas                                             |                                          |
# | Dawn Schafer                          | Diane Dubreuil                   | Carole Leroy                                                | Carla Schafer                                               |                                          |
# | Mallory Pike                          | Marjorie Picard                  | Marjorie Levêque                                            | Mallory Pike                                                |                                          |
# | Jessi Ramsay                          | Jessie Raymond                   | Justine Victoire                                            | Jessica Ramsey                                              |                                          |
# | Becca Ramsay                          | Becca Raymond                    | Roseline                                                    | Rebecca Ramsey                                              |                                          |
# | John Philip Ramsey Jr. (“Squirt”)                    | Jean-Philippe (“Jaja”) Raymond                   | Victor “Gringalet”                              | John Philip Ramsey Junior (“P’tit Bout”)                                          | John Philip Ramsey Junior (“P’tit Bout”) |
# | Keisha (Jessi’s cousin)               | Kara                             | Johanna                                                     | Keisha                                                      |                                          |
# | Sam Thompson                          | Sébastien Thompson               | Stéphane Demoulin                                           | Samuel Parker                                               |                                          |
# | Charlie Thompson                      | Charles Thompson                 | Nicolas Demoulin                                            | Charlie Parker                                              |                                          |
# | David Michael Thompson                | David Thompson                   | Sébastien Demoulin                                          | David Michael Parker                                        |                                          |
# | Watson Brewer                         | Guillaume Marchand               | Yvan Arnould                                                | Jim Lelland                                                 |                                          |
# | Karen Brewer                          | Karen Marchand                   | Coralie Arnould                                             | Karen Lelland                                               |                                          |
# | Andrew Brewer                         | André Marchand                   | Arnaud Arnould                                              | Andrew Lelland                                              |                                          |
# | Janine Kishi                          | Josée Kishi                      | Laurence Kishi                                              | Jane Koshi                                                  |                                          |
# | Jeff Schafer                          | Julien Dubreuil                  | David Leroy                                                 | David Schafer                                               |                                          |
# | Tigger (Mary-Anne’s cat)              | Tigrou                           | N/A                                                         | Tigrou                                                      |                                          |
# | Logan Bruno                           | Louis Brunet                     | Bruno Lejeune                                               | Logan Rinaldi                                               |                                          |
# | Shannon Kilbourne                     | Chantal Chrétien                 | Cécile Gauthier                                             | Louisa Kilbourne                                            |                                          |
# | Matthew Braddock                      | Matthieu Biron                   | Mathieu Brinbeuf                                            | Matthew Braddock                                            |                                          |
# | Haley Braddock                        | Hélène Biron                     | Agnès Brinbeuf                                              | Helen Braddock                                              |                                          |
# | Madame Noelle                         | Mademoiselle Noëlle              | Madame Dillon                                               | Mme Noelle                                                  |                                          |
# | Hilary (dancer)                       | Élizabeth                        | Hélène                                                      | Hilary                                                      |                                          |
# | Katie Beth Parsons (dancer/frenemy)   | Élizabeth Pellerin               | Catherine                                                   | Katie Parson                                                |                                          |
# | Mary Bramstedt (dancer)               | Marie Brazeau (Croteau in ch. 8) | Marie Bernstein                                             | Mary Bramstedt                                              |                                          |
# | Lisa Jones (dancer)                   | Lise Jordan                      | Lise Jacqué                                                 | Lisa Jones                                                  |                                          |
# | Carrie Steinfeld (dancer)             | Carole St-Onge                   | Carine Schmitt                                              | Carrie Steinfeld                                            |                                          |
# | Mr. Geiger (architect in Stoneybrook) | monsieur Gougeon                 | N/A (omits paragraph about all the houses looking the same) | N/A (omits paragraph about all the houses looking the same) |                                          |
# | Jenny Prezzioso                       | Jeanne Prieur                    | Aurélie Precisio                                            | Jenny Prezzioso                                             |                                          |
# | Charlotte Johanssen                   | Charlotte Jasmin                 | Charlotte Cuvelier                                          | Charlotte Johanssen                                         |                                          |
# | Nicky Pike                            | Nicolas Picard                   | Laurent Levêque                                             | Nicky Pike                                                  |                                          |
# | Vanessa Pike                          | Vanessa                          | Vanessa Levêque                                             | Vanessa Pike                                                |                                          |
# | Buddy Barrett                         | Bruno Barrette                   | Antoine Godefroid                                           | Buddy Barrett                                               |                                          |
# | Suzi Barrett                          | --                               | Elodie Godefroid                                            | Liz Barrett                                                 |                                          |
# | Margo Pike                            | Margot Picard                    | Anaïs Levêque                                               | Margot Pike                                                 |                                          |
# | Claire Pike                           | Claire Picard                    | Juliette Levêque                                            | Claire Pike                                                 |                                          |
# | Byron Pike                            | Bernard Picard                   | Alain Levêque                                               | Byron Pike                                                  |                                          |
# | Adam Pike                             | Antoine Picard                   | Loïc Levêque                                                | Adam Pike                                                   |                                          |
# | Jordan Pike                           | Joël Picard                      | Samuel Levêque                                              | Jordan Pike                                                 |                                          |
# | Adele Parson (Katie Beth’s sister)    | Adèle Pellerin                   | Adeline                                                     | Adèle Parson                                                |                                          |
# | Ben Brewer (ghost)                    | vieux Ben                        | Benoît Arnould                                              | Ben Lelland                                                 |                                          |
# | Mrs. Porter                           | Madame Portai                    | madame Rensonnet                                            | Mme Porter                                                  |                                          |
# | Morbidda Destiny                      | Destinée Morbide                 | Vieille Sorcière                                            | Morbidda Destiny                                            |                                          |
# | Moosie (Karen’s stuffed cat)          | N/A                              | Flocon                                                      | Moosie                                                      |                                          |
# | Mrs. Frank (Matt’s teacher)           | France                           | madame Franck                                               | Mme Franck                                                  |                                          |
# | Carolyn Braddock (Matt’s mother)      | Caroline Biron                   | Caroline Brinbeuf                                           | Carolyn Braddock                                            |                                          |
# | Christopher Gerber (dancer)           | Christophe Baril                 | Christophe Gélin                                            | Christopher Gerber                                          |                                          |
# 
# ### Where to next?
# 
# I find it tantalizing that my idea about the translators getting sloppy with peripheral character names already seems to be playing out even over the course of a single book. The risks are biggest for the Belgian and Quebec translations, which do more by way of localization, and we know that at least in Quebec they had multiple different translators. Lee made some progress in [DSC Multilingual Mystery #1](https://datasittersclub.github.io/site/dscm1/) on identifying the translators of all the French translations, using national library metadata. I think it's time we clean up the metadata mess and make a clean spreadsheet we can use to support further inquiry.
# 
# To be continued...

# ## Suggested Citation
# Skallerup Bessette, Lee and Quinn Dombrowski. "DSC Multilingual Mystery 2: Beware, Lee and Quinn!". February 27, 2020. https://datasittersclub.github.io/site/dscm2.html.
