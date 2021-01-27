![DSC logo](../_static/images/DSCLogo.png)
# DSC Multilingual Mystery 2: Beware, Lee and Quinn!

Published February 27, 2020

v. 1.0

Full text of this Data-Sitters Club book is available at [http://datasittersclub.github.io/site/dscm2](http://datasittersclub.github.io/site/dscm2).


### Suggested citation:
Dombrowski, Quinn. "Jupyter notebook for *Data-Sitters Club Multilingual Mystery 2: Beware, Lee and Quinn!*". February 27, 2020. https://github.com/datasittersclub/dscm2.

## Quinn

The differences leap out at you before you even open any of the books. "**Christine** a une idée géniale". Or was the Baby-Sitters Club "L'idée géniale de **Valérie**:? Does "**Bruno** aime **Mélanie**", or is he instead "Un amoureux pour **Anne-Marie**"? There's a case study on the Dutch translation of the Baby-Sitters Club books in [Babysitting the reader: translating English narrative fiction for girls into Dutch (1946-1995](https://www.worldcat.org/title/babysitting-the-reader-translating-english-narrative-fiction-for-girls-into-dutch-1946-1995/oclc/230991531&referer=brief_results)) by Mieke K T Desmet that gets into strategies for localizing a story that takes place in a different cultural context, and the article "[Cultural Understanding in the Indonesian Translation of The Baby-sitters Club](http://paradigma.ui.ac.id/index.php/paradigma/article/view/159)" by Halida Aisyah talk about how the Indonesian translation took a different approach, maintaining the protagonists' foreign names and locations, and only adopting Indonesian cultural references when the American equivalent would've been incomprehensible without some kind of extensive explanation. But I hadn't come across any scholarly literature on translation strategies for The Baby-Sitters Club in French (in any of the translations: Québécois, Belgian, or French from France).


I had questions, and not just "what did they decide to call Mallory?" (Spoiler alert: in Québécois it's Marjorie, and just like in English, it's the most frequently screwed up name when OCRing the books.) The ghostwriters in the US were working with an extensive "BSC Bible" that had the description and background of every character in Stoneybrook, and further afield in the BSC universe. (This was adapted and published as [The complete guide to The Baby-sitters Club](https://www.worldcat.org/title/complete-guide-to-the-baby-sitters-club/oclc/35328788&referer=brief_results).) But in [DSC Mystery #1: Lee and the Missing Metadata](https://datasittersclub.github.io/site/dscm1/), Lee discovered that at least in Quebec, they were throwing Baby-Sitters Club books at multiple translators, who turned them around in no time at all. How careful were the translators about consistency, in terms of what they called various peripheral characters and places? This was the making of another Data-Sitters Club Multilingual Mystery. (Who are the data-sitters? So glad you asked. Check out [Chapter 2](https://datasittersclub.github.io/site/chapter-2/).)


Lee and I put our heads together about how we'd start looking into this mystery. We needed a book that we had on hand in all the translations: Québécois, Belgian, French from France (the last of these being the source of the recent French re-releases). We settled on Jessi's Secret Language, on the thought that all the major characters had been established by that point, as well as many peripheral ones. We'd need to compare with some of the other translations, but that would be our starting point.


Here's the thing, though: Lee reads French. I don't. I mean, I could probably pick my way through the text and come up with a list of characters and places, but I had other ideas. I wanted to see how French named-entity recognition performed compared to English, when applied to The Baby-Sitters Club.

## What’s named-entity recognition?
Named-entity recognition (often abbreviated NER) is a kind of information extraction task -- basically, trying to identify particular things (like names of people, places, and organizations) in unstructured text, like a novel. (Yeah, I know that novels have structure, but your average plain-text file of a novel's text -- even if it maintains chapter headers and such -- doesn't have the kind of structure that a computer can easily read. I mean, it's not like it's a spreadsheet or something.) There are two major technical approaches: one uses grammar-based rules to identify the things of interest, and the other uses statistical models like machine learning, and requires a ton of labeled data (e.g. texts where a human has already gone through and correctly identified all the things of interest) upfront. Particularly for statistical models, the more your texts resemble the example texts that the model was trained on, the better the NER will perform. These models are most commonly trained on news corpora, or Wikipedia -- not 80's and 90's girls' literature. This sort of thing is a problem in DH more broadly, not just for us Data-Sitters. David Bamman's [LitBank project](https://github.com/dbamman/litbank) (a dataset of annotated excerpts from public domain literature) is one example of how DH scholars can significantly improve the effectiveness of natural-language processing (NLP) by training models on data that looks more like what we're trying to apply it to. But I'll save the question of how, exactly, one goes about training a model for a future Data-Sitters Club Multilingual Mystery. For the moment, let's see how some commonly-used tools perform "out of the box".

## The tools
The two major NLP tools with multilingual coverage are [spaCy](https://spacy.io/) and [Stanford NLP](https://nlp.stanford.edu/software/). To use spaCy, you load it into Python and run it that way. While there's a Python version of Stanford NLP, as of February 2020 it doesn't cover everything -- and entities are one thing that's currently left out. To get entities with Stanford NLP, you have to run a memory-hungry Java program from the command line, with all the joy that comes from setting that up. To make matters worse, Stanford NLP doesn't have an NER model for French: just English, Spanish, German, and Chinese. It's a better comparison to look at English vs. French with the same tool, rather than English with one and French with the other, so for this mystery, we'll be using spaCy.

## The texts

To make it easier to compare the entities from each text, I split up each translation plus the English original into 15 plain text files, one from every chapter. Everything else I left as I got it from ABBYY FineReader (as discussed in [DSC #2: Katia and the Phantom Corpus](https://datasittersclub.github.io/site/dsc2/)), plus the corrections to my (often bad) attempt to transcribe the "handwritten text" portions. I didn't appreciate some implications of that -- I'll get back to it in a bit.

## Getting started with spaCy

SpaCy is run via Python, so it can seem a little intimidating if you've never worked with a programming language before. For this mystery, I set up a Jupyter notebook in the Data-Sitters Club GitHub repo that you can download and use for your own texts. (If you're not familiar with Jupyter notebooks, [here's a Programming Historian tutorial](https://programminghistorian.org/en/lessons/jupyter-notebooks).)

You can't run the exact same experiment I did without access to the same texts I have (which I can't share for copyright reasons), but the Jupyter notebook on GitHub has all the output I got running it on the Baby-Sitters Club corpus, so you can see the results of the process one step at a time.

### 1. Downloading spaCy models

The first step is to download the spaCy models. These models have been pre-trained on annotated French and English corpora, respectively. You only have to run these code cells below the first time you run the notebook; after that, you can skip right to step 2 and carry on from there. (If you run them again later, nothing bad will happen; it'll just download again.) You can also run spaCy in other notebooks on your computer in the future, and you’ll be able to skip the step of downloading the models.

#Imports the module you need to download and install the spaCy French and English models
import sys

#Installs the French spaCy model
!{sys.executable} -m pip install https://github.com/explosion/spacy-models/releases/download/fr_core_news_sm-2.2.0/fr_core_news_sm-2.2.0.tar.gz

#Installs the English spaCy model
!{sys.executable} -m pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz

### 2. Importing spaCy and setting up NLP
Run the code cell below to import the spaCy module, and create two functions: one which loads the French model and runs the NLP algorithms ( includes named-entity recognition), and one which does the same for the English. 

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

### 3. Importing other modules
There’s various other modules that will be useful in this notebook. The code comments explain what each one is for. This code cell imports all of those.

#io is used for opening and writing files
import io
#glob is used to find all the pathnames matching a specified pattern (here, all text files)
import glob
#os is used to navigate your folder directories (e.g. change folders to where you files are stored)
import os

### 4. Diretory setup
Assuming you’re running Jupyter Notebook from your computer’s home directory, this code cell gives you the opportunity to change directories, into the directory where you’re keeping your French text files. (This notebook is designed to deal with one language at a time, and assumes your French text files are in one folder, and English are in another.)

Replace `/Users/qad/Documents/dsc/dscm2` with the full path to the directory with your files.

For instance, the default path to the Documents directory is (substituting your user name on the computer for YOUR-USER-NAME):

- On Mac: '/Users/YOUR-USER-NAME/Documents'
- On Windows: 'C:\\\Users\\\YOUR-USER-NAME\\\Documents'

#Define the file directory here
filedirectory = '/Users/qad/Documents/dsc/dscm2'
#Change the working directory to the one you just defined
os.chdir(filedirectory)

## Running spaCy

### 5. French NER, first try

The code cell in step 5 in the Jupyter notebook iterates through the files in the folder you specified up in step 4, after sorting them alphabetically. For every file that ends in .txt (an important limitation -- you'll get an error if you try to have Python open a file that isn't a text file, including those pesky invisible .DS_STORE files in just about every Mac folder), the code defines an output file name that involves appending '_ner_per.txt' to the end of the input filename.

Opening the input file (i.e. each file in turn, one at a time) and the newly-created, empty output file, the code reads in the text of the input file, and runs the spaCy French NLP. Then, for every word recognized as an entity, as long as it's an entity labeled 'PER' (a person), the entity is written to the screen (with a print command) and to the output file. I thought it'd be easiest to work through the entities one type at a time, starting just with the character names.\
I wrote this code, a couple times pulling up previous notebooks I'd written that did similar things, and consulting the [spaCy documentation and examples](https://spacy.io/usage/linguistic-features#named-entities) for how to display the entities.

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
            

And it worked... mostly? It was super weird that *J'ai* kept getting listed, but I wasn't too worried. A quirk of the model, plus the source text! Probably the model wasn't trained on first-person narratives like The Baby-Sitters Club. Yeah, there was also an example of *C'* that was harder to explain, but it wasn't until I saw an example of a double-curly-quote character (") identified as an entity that I started getting suspicious. Could those be messing things up somehow?

### 6. Data cleaning
Time for some data cleaning! When Lee brought the ABBYY FineReader output .txt files into Word to correct my bad transcriptions, Word "helpfully" replaced all the regular, straight single and double quotes with their curly equivalents. 

I wrote some code that opened every text file in my folder, searched for opening and closing curly quotes and replaced them with the “straight quote” character (a quotation mark that doesn’t differentiate opening and closing quotes). While I was at it, I saw that some of the texts weren’t using the straight single quote for the apostrophe, so I put that in there, too. This code overwrites the text files in the folder (rather than creating a new version) so if you want to keep your originals, make sure you have a copy elsewhere.

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

### 7. French NER, second try
I didn’t make any changes to the code from step 5, but check out the difference in the results. Gone are those quotation marks as so-called entities -- along with all the examples of j’ai, c’, etc. All of those were showing up because they were using the curly single quote character, and that was messing up spaCy’s model.

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

It’s not perfect: chapter 1 of the Quebec translation flags “mange Julie” (Julie eats) as a person instead of a name and noun. But it’s a lot better.

### 8. French NER for places

I moved all the \_ner_per.txt files into their own folder, so that spaCy wouldn’t try to run NER on text files of its own NER results, and would instead just use the files with the chapter texts as the objects of investigation.

I changed the code from step 7 (and 5) to replace PER with LOC and ran it again to get location entities.


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

Skimming the results, it was interesting to see how much worse it performed than the person entity recognition. It feels like a minority of the results are legit places, and most of the results are people’s names.

### 9. French NER for orgs
I was curious what I'd get by looking for entities flagged as organizations. I mean, this entire book series is about an organization: would that get flagged correctly? (Once again, I moved the \_ner_loc.txt files into their own folder first.)

The verdict: *Club des Baby* (France-French translation) and Club des baby (Quebec translation) get marked as organizations; the "sitters" gets lost when "Baby-sitters" gets separated at the hyphen. There's also various things that are most definitely not organizations that get tagged, like "Bonjour!" in Belgian ch. 10, or "PLIÉ" in Quebec ch. 3 (maybe spaCy thought it was an acronym and not a yelling dance teacher?)

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

### 10. French NER for misc
The French entity model also has a “MISC” type, so for the sake of completeness, I couldn’t not try it. And the results are as advertised. Lots of names. Lots of “Ça”. There’s a “Tu es atroce” (You’re excruciating) from Ch. 5 of the France French version. “Le Langage Secret” in Ch. 6 of the Belgian translation gets flagged, and “P'tit” makes an appearance more than once. Only in the France French version do “Noirs” (Black people) and “Noire de mon école” (Black person in my school) get flagged.

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

## Let’s do it all again for English
The steps below in the notebook basically repeat the process described above, but using the spaCy model for English instead of French. At first, I just copied over the code cells from the French section (switching out `enfiledirectory` for `filedirectory` in the first line so it looked in the right place for the English files), but kept getting some bizarre output: namely, it wasn’t able to find any entities labeled PER or LOC.

To figure out what was going on, I removed the line `if ent.label_ == 'PER':` 
and un-indented the code nested inside it, to avoid Python indentation errors, then commented-out the following out.write lines by putting a # in front of them. I didn’t want to write any results, I just wanted to see what entities it found.

Lo and behold, there were lots of entities, with more different entity labels than available for French. There’s GPE (geopolitical entity, AKA location, but not any of the locations that are like “so-and-so’s room”), DATE, CARDINAL (number type), LANGUAGE (seems relevant for Jessi’s Secret Language), TIME (e.g. “the morning of the day”), DATE (things like “a few weeks”, or, strangely, “eight-year-old”), PERSON (not PER).

First, we have to put in the path to the English files, then change to that directory:

#Put in the path here, using the same conventions as described above in step 4
enfiledirectory = '/Users/qad/Documents/dsc/dscm2/en'

### 11. English NER for people

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

### 12. English NER for places

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

### 13. English NER for organizations
I think my favorite entity type is ORG, which gets you everything from Oakley Elementary to Swanilda to Mama. (Yes, friends, “Daddy” is a PERSON but “Mama” is an ORG.)

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

### 14. English NER for works of art
That said, there’s also a rare WORK_OF_ART entity type, exemplified by “Morning, Squirts”, “Hey, Jessi”, “On Top of Old Smoky” (depends on how you feel about folk music, I guess), and, my very favorite work of art, “Nope”.

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

## What now?
I reran the notebook for English, reluctantly limiting myself to the entity types held in common between the English and French models. So now I had, chapter-by-chapter, translation-by-translation (plus original English), all the person, location, and organization type entities.

That’s nice.

But that wasn’t my question: what I wanted to know was how the translators adapted people and place names. I had to figure out what to do with all these text files to get me closer to an answer.

I had some thinking to do.


## Read more

To find out how this *Data-Sitters Club Multilingual Mystery* ends, read the [full book on the Data-Sitters Club website](http://datasittersclub.github.io/site/dscm2).