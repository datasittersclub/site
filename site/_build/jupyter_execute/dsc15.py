#!/usr/bin/env python
# coding: utf-8

# ![DSC logo](_static/images/DSCLogo.png)
# 
# # Little Miss California Stereotype... and the BY Times
# 
# <div style='float: right; width: 200px;margin-left: 7px;margin-top: 0px;'>
# <img src='_static/images/bookcovers/dsc15_cover.jpg' alt='DSC 15 book cover' />
# </div>
# 
# by Dainy Bernstein, Quinn Dombrowski, and Mark Algee-Hewitt
# 
# September 15, 2022

# ## Quinn
# ### Prelude
# The miraculous thing about DH Twitter is how it can bring you the friends you don't even realize you're looking for. It's how I started the Data-Sitters Club (which you can read more about in [Chapter 2](https://datasittersclub.github.io/site/chapter-2.html)). I met [Dainy Bernstein](https://dainybernstein.wordpress.com/) shortly after the pandemic started.
# 
# Dainy is a Visiting Lecturer in Literature at the University of Pittsburgh, and has short, dark brown hair and brown eyes. Ey bounces back and forth between big-picture ideas and detail-focused ideas, sometimes writing about an entire collection of books and sometimes writing three pages about a single paragraph. Eir childhood and adolescence was spent in Brooklyn, New York, reading as many books a week as the public library let er borrow. Dainy writes about ultra-Orthodox Jewish children's literature and is the editor of the recently-published collection of essays *[Artifacts of Orthodox Jewish Childhoods](https://www.benyehudapress.com/books/artifacts-of-orthodox-childhoods/)*.
# 
# There's not that many people working on the intersection of DH methods and books for young readers, so I'm always excited to meet another one. When I realized eir specialty was Orthodox Jewish youth literature, I couldn't resist asking if ey'd heard of BY Times, the "[Jewish answer to the Baby-Sitters Club](https://the-toast.net/2015/03/05/the-b-y-times-jewish-answer-baby-sitters-club/)" as Mara Wilson described it on the Toast.
# 
# The resulting DSC 15 has taken over two years to write, between trying to build a corpus of BY Times books when libraries were closed and Inter-Library Loan wasn't operating (and used copies could run hundreds of dollars), trying to actually read these books with my eyeballs (making lists of questions to send to Dainy), settling on a research question (the depiction of the "California girl" in each series), and then trying a couple different methods to see if we could reliably identify what we felt was distinctive, stereotypical "California girl" speech.
# 
# Spoiler alert: it didn't work. Which is on point for book 15: Dawn's contestants in the Little Miss Stoneybrook beauty pageant didn't win, either. But come join us for this interdisciplinary digital humanities adventure anyway, where you'll see what happens when you combine an expert in a particular literature (Dainy), a curious and bewildered jack-of-all-trades (me), and a computational text analysis expert (Associate Data-Sitter Mark Algee-Hewitt, recently-tenured Director of the Stanford Literary Lab) to tackle a text-classification problem.

# ## Dainy
# 
# ### Childhood experience reading the BY Times
# 
# My introduction to the idea of the *B.Y. Times* as the "Orthodox Baby-Sitters Club" came from that same [Toast article by Mara Wilson](https://the-toast.net/2015/03/05/the-b-y-times-jewish-answer-baby-sitters-club/). Mara describes her experience reading these books as a young Conservative Jew, because her Orthodox friend wanted her to become more strictly Orthodox in her practice. She'd explain the series to her gentile friends by saying, "They're like a Jewish *Baby-Sitters Club*." That in itself is a fascinating experience, but my adolescent experience with the B.Y. Times books is entirely different. I had access to both the *Baby-Sitters Club* series via the public library and my school library, and the *B.Y. Times* series via my school library and the local neighborhood Jewish library. I can't say for sure, but I most likely read the *B.Y. Times series* before I read the *Baby-Sitters Club series*. To me, as to other pre-teens in my ultra-Orthodox community, the Orthodox books were not perceived as derivations. I didn't make the connection between the BYT and the BSC until Meira Levinson, an academic colleague who is Modern Orthodox, shared Mara Wilson's piece with me.
# 
# My lived experience is also not exactly like the girls in the B.Y. Times series, mainly because the series - like its sister series, The Baker's Dozen - is set in Bloomfield, an imaginary New York suburb. I grew up in Boro Park, in the heart of a Brooklyn Jewish community. In the fourth book of the series, War!, Batya Ben-Levi has a conversation with a girl from Boro Park which encapsulates the difference between the two environments as they talk about their respective Bais Yaakov schools (a generic name for Orthodox Jewish girls' schools): 
# 
# >"So your friends are all excited about having your own Bais Yaakov building. In Boro Park, we have two buildings, and soon maybe there'll be a new annex." 
# 
# <div style='float: right; width: 400px;margin-left: 7px;margin-top: 0px;'>
# <img src='_static/images/dsc15_pizza.jpg' alt='Gemarakup book cover' />
# </div>
# 
# Batya, from the suburban Bloomfield, is excited at the prospect of Bais Yaakov having its own building; her counterpart from the city scoffs at this as a marker of growth since her community passed that marker decades before. The existence of the Ben-Levi pizza shop in the *B.Y. Times* series is remarked upon as extraordinary within the books, because the infrastructure of a kosher community in a suburban environment was indeed extraordinary at the time, in the early 1990s. In 1990s Brooklyn, the existence of a thriving kosher pizza store was taken for granted.
# 
# The difference between Brooklyn Orthodox Jewish communities and the "out-of-town" communities depicted in the BYT - and in the Brookville C.C., a series for older teens similarly based on the BSC - is not always apparent to those who didn't grow up with these nuances. As Quinn read the series, we'd have exchanges like this:
# 
# >Quinn [after reading that the Rabbi's wife in the B.Y. Times series was an original student of Sarah Schenirer]: Who's Sarah Schenirer?
# >
# >Dainy: "mother of Bais Yaakov," [founder of the Bais Yaakov movement](https://thebaisyaakovproject.com/person/sarah-schenirer/).
# >
# >Quinn: Ohhhh. Yeah, that's another thing I understand badly. 😅 I was figuring it was the name of the school in BYT, like how my kid goes to Malcolm X Elementary in Berkeley. Then I figured it was some educational philosophy, like a Montessori school, since it showed up in both series. 
# >
# >Dainy: I think in BCC they actually go to Beis Rivkah, which is a typically Chabad / Lubavitch name. But Bais Yaakov is a generic name for "orthodox girls school" because of Sarah Schenirer.
# >
# >Quinn: Ohh, gotcha. The "Beis" is the part that stuck with me because of OCR errors.
# >
# >Dainy: (Bais/Beis = house, Yaakov = Jacob. It's from the verse "go tell the house of Jacob" in the Bible, usually interpreted as "go tell the women" in that context.)
# >
# >Quinn: Ohhhh, interesting.
# >
# >Dainy: I am so loving "reading" the books through your eyes.
# 
# I am rereading these books myself now as I write about the development of Orthodox children's publishing in America. The earliest Orthodox children's books from major publishers appeared in the 1980s, making the *B.Y. Times* series part of Haredi publishing's relative infancy. I interviewed series creator Miriam Stark Zakon (writing under the pseudonym Leah Klein), and she confirmed that the connections that Mara Wilson and others draw between the BSC and the BYT are deliberate. Zakon had been writing books for Haredi children for a while, and she wanted to get a sense of what was popular for children in mainstream America. Since she was living in Israel at the time, she asked her sister in America to go into a bookstore and take stock of titles and genres on the shelves in the children's sections. Her sister sent her copies of *The Baby-Sitters Club*, and Zakon set out to create a "kosher" version of the books for Orthodox children in which middle-school girls create a school newspaper.
# 
# <div style='float: right; width: 200px;margin-left: 7px;margin-top: 0px;'>
# <img src='_static/images/dsc15_gemarakup.jpg' alt='Gemarakup book cover' />
# </div>
# 
# A few other Orthodox series are also clearly based on popular mainstream series. The *Gemarakup* series (also written by Zakon), for example, is a riff on *Encyclopedia Brown*. In both, a young boy (Yisrael David Finkel and Leroy Brown, respectively) solves mysteries and crimes in his neighborhood using his extensive knowledge. Leroy (aka Encyclopedia) uses knowledge he gains from an encyclopedia; Yisrael David (aka Gemarakup, literally translatable as Talmud-Head) uses knowledge he gains from the Talmud.
# 
# When I first connected with Quinn over the connection between the BSC and the BYT, I hadn't managed to get hold of any *B.Y. Times* novels. Copies available for purchase from the publisher are new editions, and I wanted to make sure I was reading the books in their original forms. The used copies available online are prohibitively expensive, and while the Brooklyn Public Library used to carry the books, they have since been retired from circulation.
# 
# Once I started working with Quinn, I doubled my efforts to get hold of the books and tried some other channels.
# 
# The Jewish Youth Library was founded in February 1978 (according to a writeup in the children's magazine, Olomeinu / Our World) to fill a gap in the availability of Orthodox children's books. (This was before the Brooklyn Public Library started carrying Orthodox children's books.) It started out on 51st Street in Boro Park, Brooklyn, and has since moved to 46th Street, a few blocks over from its original location. As a pre-teen and teenager, I visited the basement library during girls' hours at least once a month, taking out the maximum of three books at once. It exists in my mind as belonging to another time, and it hadn't even occurred to me to check if it was still functioning until I mentioned it in passing to Quinn.
# 
# <div style='float: right; width: 200px;margin-left: 7px;margin-top: 0px;'>
# <img src='_static/images/dsc15_byt_war.jpg' alt='A beat-up BYT book cover entitled "War"' />
# </div>
# 
# So I called, and they are still functioning! At the start of the pandemic, they were observing social distancing, and all books had to be ordered ahead of time. The library now allows members to borrow five books at a time, extended to six during summer months when kids are not in school. The librarian I spoke to was very patient with me as she updated my decades-old analog membership card - still there along with my mother's, sister's, and brother's! - and listened to what I needed. I explained that I wanted to borrow all the BYT books, and if I could take six at a time, it would be best if I had the first six. She checked on the shelves, and found the second book was checked out by another patron. She pulled books \#1 and \#3-7 for me instead. A friend of mine offered to drive over and pick them up the next day during curbside pickup, and then drove over to deliver them to me.
# 
# Although the books are being reprinted with brand new covers by Menucha Publishers, a newer Haredi publishing house who inherited Targum Press's old titles, it was important to me to have the original copies of the books because of the extra-textual details often included in books. And the copies from the Jewish Youth Library are indeed the originals! Taped up and worn out from years and years of use... I scanned the books (noting fascinating details like a writing contest for readers announced at the back of some books), and sent them off to Quinn. Since then, Quinn has managed to get copies of the books held in Harvard's library via Inter-library Loan.

# ## Quinn
# 
# ### Baby-Sitters meets Sweet Valley, but make it Orthodox?
# 
# <div style='float: right; width: 200px;margin-left: 7px;margin-top: 0px;'>
# <img src='_static/images/dsc15_bytstack.jpg' alt='A stack of pristine BYT books' />
# </div>
# 
# Thanks to Harvard’s extensive Judaica collection, we finally pieced together the entire series – a project nearly 18 months in the making. A trip to Greece in April gave me the opportunity to sit down and read through them all, and thanks to Mara Wilson’s article, I brought a truckload of assumptions with me. Newspaper angle aside, this was going to be the Orthodox Jewish Baby-Sitters Club. I was on the lookout for Kristy, Claudia, Mary Anne, and Stacey, ready for whatever they looked like transposed into a new cultural context.
# 
# Except it turned out things were more complicated. *BY Times* isn’t just a spin-off of the BSC: it’s a culturally-shifted mashup of (at least) the two biggest girls’ series of the 90s, not just the BSC but *Sweet Valley* as well. Of the two series, *Sweet Valley* is the one that more obviously needs an overhaul to be appropriate for Orthodox Jewish readers. Even my mother, who was not usually very censorious, did not approve of me reading the *Sweet Valley High* books, which feature a pair of rich, blonde, beautiful California twins in a classic good-twin/bad-twin setup. There’s lots of mildly steamy romance, some adolescent drinking, sexual assault, car crashes, amnesia, and just about every other soap opera trope you can think of – and every book ended with a cliffhanger of some sort. I found them tedious, especially in their kid-friendly formulations, *Sweet Valley Twins* and *Sweet Valley Kids*, whose age-appropriate drama lacked the titillation of *Sweet Valley High*.
# 
# Let me introduce you to the initial staff of the BY Times, as I, a non-Jewish childhood reader of 90’s girls books, experienced them:
# 
# * Shani Baum: clearly identifiable as “the Kristy”: she’s short, loud, bossy, and started the newspaper.
# * Raizy Segal: a genius like Janine, but shy like Mary Anne
# * Batya Ben-Levi: an only child like Mary Anne, who wishes she had more siblings
# * Nechama Orenstein: Like Mallory, a redhead and the youngest in a big family, but she doesn’t like reading, is bad at school, and is generally wild and irresponsible
# * Chani Kaufman: honestly, it took me a lot of books to realize she was a separate character from Shani. Her distinctive feature, such as it is, is that she’s extremely short.
# * Pinky & Chinky Chinn: (yes, you read that right) are the rich twins. It wouldn’t do to have a “good” and “bad” twin, so instead we get a Claudia-type as the foil to a responsible, organized twin (much like Elizabeth, the “good” twin in Sweet Valley.) Pinky, the Claudia-type, is really into fashion and design, and also likes eating caramels constantly. Unlike Claudia, whose complexion and figure are unaffected by her sweet tooth, there’s a whole book about fat-shaming Pinky for weighing a couple pounds more than Chinky.
# 
# <div style='float: right; width: 400px;margin-left: 7px;margin-top: 0px;'>
# <img src='_static/images/dsc15_littleworld.jpg' alt="Batya's Search book cover and sick Dusty the computer with a virus" />
# </div>
# 
# I found these girls’ adventures to be fascinating and strange. Where the *Baby-Sitters Club* books are written in a way that now reads as “timeless”, that’s also another way to say that it’s disconnected from the time, place, and sociopolitical context in which it was written. In a talk we gave last year, Data-Sitter Maria Sachiko Cecire mused over how we could explore the ways in which the *Baby-Sitters Club* forms a sort of “small world” (as J.M. Barrie describes a “map of a child’s mind, which is not only confused, but keeps going round all the time”) that captures some things about the adult world (like capitalism and divorce and bra shopping and British palace guards) but leaves out others (collapse of the USSR, the Persian Gulf War, computer viruses, etc.) The *BY Times* offers a point of contrast where the author made a different set of choices about what made it into her narrative “small world”. On one hand, the characters live in an insular community with a specific set of rules: no one’s eating a bacon cheeseburger or wearing tie-dye leggings with overall shorts. But on another hand, no member of the *Baby-Sitters Club* learns how to correctly put on a gas mask, or survives a scud missile attack, or helps “Russian” Jewish refugees from Kyiv resettle in the US, or picks up the pieces when the club’s computer is infected with a virus.
# 
# I really wanted to do something to explore the scope and nature of the worldbuilding between the *BY Times* and the *Baby-Sitters Club*, but Russia’s invasion of Ukraine blew up the small world of multilingual and feminist DH projects that I’d created for myself at work, and tackling something that big felt out of reach. Dainy and I had talked about “how Jewish” vs “how American” these books were, but that also meant some hard decisions about how to model each of those things. I wanted something more straightforward, something that I could use to try out a new-to-me text analysis technique.
# 
# And I finally found it in the 9th *BY Times* book, *Here We Go Again*, which prominently features a new character: a blonde health-food fanatic who’s just moved to town from California.
# 
# Sound familiar?

# ### Ilana the California Girl
# With many *BY Times* characters, you can only see the shadows and contours of influence from the Baby-Sitters Club. Not so with Ilana Silver. Ilana is Dawn with valley girl stereotypes turned up all the way. (Also: Ilana is a **really hard name** to reliably OCR in the font they used to print BY Times books. She’s “Hana”, “Dana”, “Tiana”, or even “Bana” as often as “Ilana”.)
# 
# You’ll have to wait for DSC 17 to read about Junior Data-Sitter Cadence Cordell’s trip to visit the Ann M. Martin Papers at Smith College, but one major discovery was a repeated, explicit concern about Dawn and California stereotypes. At the top of the notes for *BSC \#23: Dawn on the Coast*, Martin wrote “No stereotyping CA kids”. In the folder for that same book, it notes that she had already received complaints about Dawn fitting the California stereotype of “blond-haired, blue-eyed, laidback, vegetarian health-nuts”. It comes up again in *Super Special \#11: Here Come the Bridesmaids!*, via Martin’s wanting Carol and Mr. Schafer’s wedding to “seem traditional without smacking of California stereotypes”.
# 
# Suffice it to say that Miriam Stark Zakon had no such qualms – either about her depiction of Ilana, or how the other characters interpreted her mannerisms. Ilana gets introduced as the cliffhanger of *BYT \#8: Summer Daze*, when Chani struggles to describe the new arrival from California who had been attending her summer camp:
# 
# >What could she write? Ilana was… was so… so…
# >
# >No, she couldn’t really describe her. Not without risking *lashon hara*[*](#footnote), that was for sure.
# 
# And so the book concludes:
# 
# >Why is Ilana Silver so indescribable? … Read all about it in the next edition of *The B.Y. Times*.
# 
# Ilana’s first appearance doesn’t come until about ⅓ of the way through book 9, where she makes quite the debut after failing to show up to the first BY Times meeting:
# 
# >“I’m super sorry, really,” Ilana said earnestly. “I was talking to this really amazing girl and she told me the most amazing things about her grandmother’s life. It was just so exciting! I hope I didn’t miss much at the meeting.” She flashed a sparkling smile at Nechama before pulling out a brown paper bag. Ilana held it out invitingly. “Sprouts, anyone?” she offered.
# >
# >\[...\]
# >
# >“Sprouts, huh?” \[Chani\] said loudly. “They’re from your mother’s health-food store, aren’t they?”
# >
# >“That’s right,” Ilana beamed. “It’s the first kosher health-food store in Bloomfield! It totally blows my mind that you’ve managed without one until now.”
# >
# >“Oh, we got by somehow,” said Chani with a smile as she mentally rolled her eyes. “Still, it’s so nice that we have one now!”
# >
# >“For sure,” said Ilana placidly, smiling brightly at the two girls. “I mean, like, there’s so much delicious food that’s healthy, too! It’s really much better for people to eat this way—and it’s better for the whole planet, too.” Ilana tossed a lock of blond hair over her shoulder. 
# 
# <div style='float: right; width: 400px;margin-left: 7px;margin-top: 0px;'>
# <img src='_static/images/dsc15_dusty.jpg' alt='Dusty the computer' />
# </div>
# 
# 
# The *BY Times* gets a free computer, and all the girls struggle to use it except for Ilana. As Chani puts it, “Ilana comes from California, and everyone probably has computers there. It’s no crime to know less than she does.”
# 
# The book concludes with a surprise birthday party catered by Ilana’s family’s kosher health-food store, where even Ilana’s mother makes fun of her manner of speech: “No problem,” said Mrs. Silver with a smile. “As my daughter would say”—she ruffled Ilana’s blond hair fondly—“It’s, like, no problem at all!”
# 
# Amazing! We, like, totally found something that we could measure: how distinctive was Ilana’s speech, compared to Dawn’s? 
# 
# ### Dialogue to Data
# How do we figure out if something is, like, totally distinctive? We test to see if you can reliably tell it apart from the thing you’re comparing it to. There’s lots of ways to do that, and not all of them involve computers. But all of them do involve turning the things you want to compare into something that looks like data. Even if you wanted a human (instead of a computer) to evaluate Ilana vs. non-Ilana quotes to see if they can reliably tell them apart, you couldn’t just hand that person a *BY Times* book, or even a *BY Times* book that you’ve covered with sticky notes pointing to relevant sections of dialogue. For starters, it’d be hard for them to avoid seeing text like “said Ilana” or “Chani exclaimed” that would give away the answer! What you need to do is take the quotes out of their narrative context and put them into something like a spreadsheet where you can view the quote by itself, but also connect it to metadata like speaker (Ilana/non-Ilana) and source (which book).
# 
# It may come as a surprise that automatic quote extraction and attribution is a pretty difficult computational task. There are systems that try to do it (like David Bamman’s [BookNLP](https://github.com/booknlp/booknlp), and I was thinking of trying it out when Dainy suggested a classic alternative that would almost certainly be more accurate: ey offered to read through the books and add all the Ilana quotes to a spreadsheet. 🥳 Usually I’d have protested more – let’s leave this to the computers, they’re imperfect but close enough! But I realized that we weren’t going to have a ton of data, since Ilana only appears in books 9-17. And a big part of what makes some degree of computer-error okay is scale: 10 mis-attributions are a much bigger problem if you have 100 examples than if you have 1,000, and by the time you get to 10,000 examples, I’d expect human labor to produce at least that many mistakes. So I took Dainy up on the offer, and ey found 673 instances of Ilana-speech and added them to the spreadsheet.
# 
# The process for finding non-Ilana quotes was much less precise. I wasn’t trying to find every quote, and I definitely wasn’t trying to figure out quote attribution. I just wanted stuff that non-Ilana characters said. So I wrote some code to go through the books and pull out everything between quotation marks.

# In[1]:


#Importing this to navigate directories
import os
#This lets us use regular expression syntax
import re
#This lets us randomly sample from things
import random

#Specifies the folder where my book text files are
filedirectory = '/Users/qad/Documents/dsc_byt'
#Changes to that folder
os.chdir(filedirectory)


# In[2]:


#For each file in our directory of text files
for file in os.listdir(filedirectory):
    #If the file ends with .txt
    if file.endswith('.txt'):
        #Open the source file
        with open(file, 'r') as sourcebook:
            #Read the source file
            text = sourcebook.read()
            #Find all things between quotes
            quotes = re.findall(r'“(.*?)”', text)


# In[3]:


#Randomly samples our list of quotes for 300 quotes
randomquotes = random.sample(quotes, 300)

#Opens our output file
with open('/Users/qad/Documents/nonilana.csv', 'w') as out:
    #For each quote in our random sample
    for randomquote in randomquotes:
        #Write it to the output file
        out.write(randomquote + '\n')


# The problem is, that will get us Ilana quotes along with non-Ilana quotes. But thankfully, we have Dainy's comprehensive list of Ilana quotes and can use that to remove the Ilana quotes. There's a catch, though: it will also remove any non-Ilana quotes that are identical to Ilana quotes -- thereby increasing the distinctiveness of the two sets, because anything said by both Ilana and non-Ilana characters will only appear in the Ilana data set. In this corpus, that's only likely to happen with very short quotes, like "Oh?" and "Yes" so we're going to say it's not a big deal. But in other corpora, it might be a bigger problem: imagine you're looking at Star Wars novels to compare Luke Skywalker's speech vs. other characters. You could accidentally end up modifying your data in such a way that it looks like Luke is the only person who ever says "May the Force be with you." Collecting your data in a way where you won't run into this issue is harder, and would involve across-the-board quote attribution. That's why it really helps to know your data, or work with someone who does -- and why there's no one-size-fits-all workflow for most text analysis stuff. Depending on the particularities of your data, you may be able to take shortcuts that will cut down on labor or complicated algorithms, like we've done here.
# 
# ### Dawn's Dialogue
# 
# Unlike with Ilana, there's no shortage of Dawn dialogue -- even though she, similarly, shows up after the first book and doesn't stick around until the end of the series. We're not trying to comprehensively get all of Dawn's dialogue, just a quantity similar to what we have for Ilana. We don't have any particular reason to think that the way Dawn's dialogue is tagged (e.g. "said Dawn" / "Dawn said" vs. "Dawn exclaimed" vs. Dawn dialogue that isn't explicitly labeled with her name) has anything to do with the Dawn-ness of the dialogue -- though that is something we could test if we felt so inclined. (The BY Times books sometimes use "drawled" with Ilana's speech.) So I wrote some code to look for any line (i.e. paragraph) in any Baby-Sitters Club book that included "said Dawn" or "Dawn said", then extracted only the text within quotation marks from those lines.

# In[4]:


#File directory for BSC books
filedirectory = '/Users/qad/Documents/dsc_corpus_clean'
os.chdir(filedirectory)

#Create a list for Dawn quotes
dawnlines = []
#For each file in the file directory
for file in os.listdir(filedirectory):
    #If it ends with .txt
    if file.endswith('.txt'):
        #Open the text file
        with open(file, 'r') as book:
            #Read in each line into a list
            lines = book.readlines()
            #For each line
            for line in lines:
                #If it includes 'said Dawn'
                if 'said Dawn' in line:
                    #Add it to the list
                    dawnlines.append(line)
                #If it includes 'Dawn said'
                if 'Dawn said' in line:
                    #Add it to the list
                    dawnlines.append(line)
#Print how many Dawn lines we have
len(dawnlines)


# In[5]:


#Make a new list for just the Dawn quotes
dawnwords = []
#For each line we pulled out
for dawnline in dawnlines:
    #Get the part between quotation marks
    dawnquotes = re.findall(r'“(.*?)”', dawnline)
    #Fore each quote
    for dawnquote in dawnquotes:
        #Add it to the list
        dawnwords.append(dawnquote)


# In[6]:


#Randomly samples our list of Dawn quotes for 300 quotes
randomdawns = random.sample(dawnwords, 300)
#Opens our output file
with open('/Users/qad/Documents/dawn.csv', 'w') as dawnout:
    #For each quote in our random sample
    for randomdawn in randomdawns:
        #Write it to the output file
        dawnout.write(randomdawn + '\n')


# This is, once again, a hack for quote attribution and it could backfire, for instance, if Mary Anne said, “I heard that Dawn said I was a bad step-sister.” Thanks to [AntConc](dsc4.html), we can double-check to make sure there aren’t any examples like that:
# 
# <img src='_static/images/dsc15_antconc.jpg' alt='Antconc results for "Dawn said that"' />
# 
# Or we could check the text we get once we extract only the things in quotation marks and remove anything that includes the words “Dawn” (since Dawn doesn’t ever talk about herself in the third person).
# 
# Non-Dawn dialogue is also easier with the Baby-Sitters Club books. Again, we don’t need all non-Dawn dialogue, we just need a comparably-sized sample. Thanks to the narrative structure of the Baby-Sitters Club, any book with “Dawn” in the title is narrated by Dawn, which means she’s less likely to be speaking, and any tagged speech will use the pronoun “I”. There’s the possibility of some non-tagged Dawn speech (where she says something in quotation marks, but it isn’t labeled as such) getting through, but that’s an edge case that we won’t worry about too much.
# 

# ### Do You See Anything Weird Here?
# When you’re doing computational text analysis, following along with a tutorial or workflow you’ve found online, it’s easy to forget about one of the most important steps that you’ll almost never see written out. That major lifehack, one-weird-trick step is something I like to call “do you see anything weird here?” And sometimes you might not be the right person to do this step – you may need to call in your collaborator with the relevant disciplinary or language expertise. For this project, if something had changed with how Ilana was using Hebrew words, I wouldn’t notice it but Dainy would. But as luck would have it, there was something in the data that was obviously weird to even me: Ilana suddenly and completely drops her “California girl” speech habits in books 13-17. You could be generous and say that it’s a sign she’s adapted to her environment… but it’s harder to believe it would happen so suddenly and completely.
# 
# <img src='_static/images/dsc15_nocagirl.jpg' alt='Spreadsheet of Ilana quotes without any valley girl speak' />
# 
# It’s worth running the “do you see anything weird here” check often as you work on a text analysis project – and not every weird thing means you need to make a change! But don’t brush off your skepticism: even if you decide to carry on despite some weirdness, remember that you had questions. Those doubts might be helpful when you reach the point where you need to interpret the results.
# 
# In this case, it was clear that we needed to change the plan. We couldn’t use all 674 Ilana speech acts – the Ilana of the early books speaks noticeably differently than the Ilana of the later books. The “California girl” Ilana from books 9-12 only said 230 things according to Dainy’s list, so that’s all we had to work with. I brought this small data set, and a random sample of 230 non-Ilana quotes, to Associate Data-Sitter Mark Algee-Hewitt, to see what he’d suggest.

# ### Length and Normal Distribution
# "Okay, I have all the Ilana quotes and non-Ilana quotes ... now what?" I asked.
# 
# Mark pulled out his laptop and opened up RStudio. "Before we do anything about Ilana as such, we need to check to make sure any length differences between the samples aren't significant."
# 
# I looked at Mark quizzically. "I mean... it's not like there's a character who's super into speechifying or anything. And definitely not in the sample we generated. Why do we think length is going to be a problem?"
# 
# Mark laughed. "Okay, so this is one of those things that happens at DH conferences -- where, like, you'll walk into a room and we'll be playing with the BSC corpus, looking for ways to see if Ilana's dialogue is different than other dialogue, and some bearded guy with a scarf will say, 'excuse me, did you test for statistical significance in the difference in speech length, and did you assume a normal distribution?' And everyone's going to hate him, but he's not wrong."
# 
# I knew the type, and appreciated the value of preemptively heading off the bearded scarf-wearing guy type. I was in.
# 
#  "First, we need to run qqnorm to test for normality. We need to know if it has a normal distribution before we can use a t-test to make sure that differences in length aren't significant," said Mark.
# 
# Mark opened RStudio, and imported the data Dainy and I had prepared for Ilana and non-Ilana quotes.

# <div class="alert alert-block alert-warning"><b>Warning: R incoming</b><p>Mark mostly codes in R; I mostly work in Python, and the <em>Data-Sitters Club</em> is published as a <a href="https://jupyterbook.org/en/stable/intro.html">Jupyter Book</a> using a Python kernel – the thing that interprets and executes the code. So like we <a href="https://datasittersclub.github.io/site/dsc10.html#fitting-an-r-shaped-peg-into-a-jupyter-shaped-hole">discussed in DSC 10</a>, I have to put <code>%%R</code> at the top of each cell of R code that I want to be interpreted as R, rather than Python. If you’re just running R, you don’t need that part.</p>
# </div>

# In[7]:


#This installs rpy2, which is my Python-to-R adapter
import sys
get_ipython().system('{sys.executable} -m pip install rpy2')
#This loads the Jupyter Notebook extension that lets me
#run R code in a notebook that's otherwise Python by default
get_ipython().run_line_magic('load_ext', 'rpy2.ipython')


# <div class="alert alert-block alert-success">
# <b>Note:</b> We have more non-Ilana quotes than Ilana quotes, and random sampling will give you different results each time. In order to not have to change the text of this book every time we rerun the code, we’re importing a pre-sampled version of the non-Ilana quotes. If you need to sample data that you’ve imported, though, you can do it like this:
#     <code>length.nonilana.table&lt;-length.nonilana[sample(nrow(length.nonilana), 230),]</code>
# 
# </div>

# In[8]:


get_ipython().run_cell_magic('R', '', '#Sets the working directory (e.g. where it looks for files)\nsetwd("/Users/qad/Documents/GitHub/dsc15")\n#Reads the non-Ilana quotes CSV\nlength.nonilana<-read.csv(file=\'non_ilana_sample.csv\', header=T)\n#Reads the Ilana quotes CSV\nlength.ilana<-read.csv(file=\'ilana.csv\', header=T)\n#Sets the column names on the Ilana quotes to be attribution, source, quote\ncolnames(length.ilana)<-c("Attribution", "Source", "Quote")\n#Checks the dimensions (rows, columns) for the non-Ilana quotes\ndim(length.nonilana)')


# “Let’s limit the Ilana quotes to the ones in the books where she has the distinctive speech,” said Mark. “Once we do that, we can also drop the source column.”

# In[9]:


get_ipython().run_cell_magic('R', '', '#Book source for the quotes is in the second column in this data\n#This code only keeps quotes where the source is one of the books \nlength.ilana.table<-length.ilana[which(length.ilana[,2] %in% c("BYT9", "BYT10", "BYT11", "BYT12")),]\n#Keep only the first column (attribution, i.e. "Ilana") and third (the text)\nlength.ilana.table<-length.ilana.table[,c(1,3)]\n#Create a table with the non-Ilana quotes\nlength.nonilana.table<-length.nonilana\n#Rename the columns of the Ilana table to match the non-Ilana table\ncolnames(length.ilana.table)<-colnames(length.nonilana.table)\n#Check the dimensions of the Ilana table\ndim(length.ilana.table)')


# “Now, let’s create a table that combines both the Ilana and the non-Ilana quotes.”

# In[10]:


get_ipython().run_cell_magic('R', '', 'length.final.table<-rbind(length.ilana.table, length.nonilana.table)\ndim(length.final.table)')


# “There’s a cleaning function I always use,” said Mark. “It lower-cases the text, and removes punctuation and such. Since we’ll be using that when we look for distinctive words, let’s do that here before we look for the length; it can make a small difference in the word count.”
# 
# “Oh, like how ‘Baby-Sitters Club’ could be two or three words, depending on your code?”
# 
# “Exactly.”
# 

# In[11]:


get_ipython().run_cell_magic('R', '', '#Mark\'s cleaning function\nfullClean<-function(raw.text){\n  raw.text<-unlist(strsplit(raw.text, ""))\n  raw.text<-tolower(raw.text)\n  clean.text<-raw.text[which(raw.text %in% c(letters, LETTERS, " "))]\n  clean.text<-paste(clean.text, collapse="")\n  return(clean.text)\n}\n\n#Clean the Ilana quotes\nclean.length.ilana<-lapply(length.ilana.table$Text, function(x) fullClean(x))\n#Clean the non-Ilana quotes\nclean.length.nonilana<-lapply(length.nonilana.table$Text, function(x) fullClean(x))\n\n#Adds a CleanText column to the Ilana table\nlength.ilana.table$CleanText<-clean.length.ilana\n#Adds a CleanText column to the non-Ilana table\nlength.nonilana.table$CleanText<-clean.length.nonilana\n#Counts the length and adds a Length column to the Ilana table\ntext.length<-unlist(lapply(clean.length.ilana, function(x) length(unlist(strsplit(x, " ")))))\nlength.ilana.table$Length<-text.length\n#Counts the length and adds a Length column to the non-Ilana table\ntext.length<-unlist(lapply(clean.length.nonilana, function(x) length(unlist(strsplit(x, " ")))))\nlength.nonilana.table$Length<-text.length')


# “Let’s look at the mean length of the Ilana and non-Ilana quotes.”

# In[12]:


get_ipython().run_cell_magic('R', '', '#Average (mean) length of Ilana quotes\nmean(length.ilana.table$Length)')


# In[13]:


get_ipython().run_cell_magic('R', '', '#Average (mean) length of non-Ilana quotes\nmean(length.nonilana.table$Length)')


# “Now we’ll put all this data together in a single table.”

# In[14]:


get_ipython().run_cell_magic('R', '', '#Combine Ilana and non-Ilana tables in a single table\nlength.table<-rbind(length.ilana.table, length.nonilana.table)\ndim(length.table)')


# “Let’s check the mean of all the data together.”

# In[15]:


get_ipython().run_cell_magic('R', '', 'mean(length.table$Length)')


# "We know that the average length of the Ilana quotes is 9.1 words, and the average for non-Ilana quotes is 11.1 words. What we want to do is compare them, check on whether there's a meaningful difference between them. The statistical method we'd usually reach for is a *t-test* -- also known as the student's t-test -- which is a statistical test of whether or not the difference in the means of two distributions is significant. We compare the output to an *alpha*, which is a threshold value used to judge whether a test statistic is statistically significant. By convention, we use .05 -- if it's less than or equal to .05, we say it's statistically significant. But there's a catch: the t-test only works if the data is distributed *normally* -- normally in the statistical sense, where most of the values cluster in the central region, and they trail off equally in both directions. A normal distribution looks like a bell curve if you were to visualize it. For this data, that would mean that there'd be (roughly equally) few very long and very short quotes, and most of the quotes would be middle-length."
# 
# "How do we figure that out?" I asked. "There's got to be a better way than making a chart and eyeballing it, right?"
# 
# "Yes," said Mark. "We can use what's called a quantile-quantile plot, or qqplot, which is available as an R package. What it does is take two sets of data, and plots each quantile of one data set against the same quantile of the second data set. A quantile is just a way to break up data into chunks with the same probability -- you might have heard of *quartiles*, which break data into four pieces with equal probability: the second quartile is the *median* of the data, the first quartile is halfway between the starting point and the median, so that 25% of the data is below that point. The third quartile is the middle value between the median and the highest value, so that 75% of the data is below the third quartile. Anyhow, if the data follows a normal distribution, all the points should roughly fall along the reference line."

# In[16]:


get_ipython().run_cell_magic('R', '', '#Creates the qqnorm plot\nqqnorm(length.table$Length, pch=1, frame=F)\n#Adds the reference line\nqqline(length.table$Length, col="firebrick", lwd=2)')


# “It’s not normal. Look how not-normal it is!” Mark exclaimed. “This data is wonky at the ends – especially the long end. So we have some kind of funky-tail distribution. It’s not normal enough to do a t-test… which means, we have to use a… you know …” Mark gestured vaguely.
# 
# “Nope, definitely don’t know.”
# 
# It was gratifying to see Mark pull up a web browser and Google for the answer, the same way I do. “Test difference non-parametric data…” and then, scrutinizing the results, he added “in R”. Success, apparently! “That’s it – there’s Mann-Whitney U test, also known as Wilcoxon rank-sum test, two names for, in our case, effectively the same thing – they both allow us to test for the difference between two samples of non-parametric, or non-normal, data. Instead of using mean values like we would use in a t-test, the Mann-Whitney asks: if we choose two random data points from sample A (Ilana) and sample B (non-Ilana), is the probability that A>B equal to the probability that B>A?  This is for independent variables – if we had dependent variables, then we could use a Wilcoxon Signed Rank test.” 
# 
# “Wait a minute, I’m confused again,” I said. “If I’m remembering right, ‘independent’ variables are things that you change in an experiment like this, and ‘dependent’ variables are things that change as a result of how you’ve changed the independent variable. Why are we saying we’re looking at independent variables? Couldn’t we argue that length is a dependent variable resulting from the independent variable of Ilana vs. non-Ilana?”
# 
# “Yes, the length of both Ilana and non-Ilana quotes are dependent on who’s speaking them – that’s exactly the point of what we’re looking at,” said Mark. “But the question here is: are they dependent **on each other**? Does having short Ilana quotes mean that the length of the non-Ilana quotes will be affected, or vice-versa? Maybe if we knew the author had a very strict word-count limit or something, but the answer there is no, so we don’t have to worry about dependence.”
# 
# “When *would* you have to worry about it?” I angsted.
# 
# “Imagine if we had a data set where one feature is the number of times the word ‘a’ appeared in English-language texts, and another feature is the number of articles from a part-of-speech parse. Since increasing one increases the other, that means they are dependent.”
# 
# “That makes sense” I said, relieved.
# 
# Mark closed his browser and opened RStudio. “What we want to do is regress length onto attribution – a regression analysis helps us measure the influence of one or more independent variables – attribution, in this case – on a dependent variable, length.”
# 

# In[17]:


get_ipython().run_cell_magic('R', '', 'w.result<-wilcox.test(Length~Attribution, length.table)\nw.result')


# “The p-value is .14, so we can safely say that the fact that non-Ilana dialogue is slightly longer (11.1 vs 9.1 for Ilana dialogue) shouldn’t make a difference,” Mark concluded. “Length has a large effect – in fact, it tends to have an outsized effect on computational results. You can adjust for length, but it’s kind of difficult. So when you’re comparing two groups of things, if there’s a statistically significant difference in length between them, it’s probably going to have an effect and we don’t want it to. We don’t want to create a model that just says “not-Ilana dialogue is longer, so if it’s long, it’s not Ilana.” That’s not going to get us a kind of classification that helps answer our question. Sometimes it can be very accurate – for the LitLab’s short story project, we created a model that predicted with 100% accuracy whether something was a short story or a novel, because it turns out that short stories are shorter than novels. It was extremely accurate, but completely unhelpful. In this case, it’s important that we know whether or not there’s a significant difference in length, because that’s not a difference we’re interested in. Hopefully there are *other* differences that we *are* interested in. Sometimes length could end up being an interesting difference – if the p-value was low for that test, that could be a sign that her dialogue is shorter in a way that merits a second look. It’s not, but now we know that conclusively, and we can discount it as a potentially confounding factor.”

# ### Distinctive words
# Mark pulled out some more code. “Let’s look for some distinctive words. We’ll start by installing some R packages…”

# In[18]:


get_ipython().run_cell_magic('R', '', '\nsetwd("/Users/qad/Documents/GitHub/dsc15")\nif(!require(tm)){\ninstall.packages("tm")\n}\nif(!require(MASS)){\ninstall.packages("MASS")\n}\nif(!require(klaR)){\ninstall.packages("klaR")\n}\nif(!require(e1071)){\ninstall.packages("e1071")\n}\nif(!require(SnowballC)){\ninstall.packages("SnowballC")\n}\nif(!require(neuralnet)){\ninstall.packages("neuralnet")\n}')


# “Now, we’re going to import the data and make sure it looks right.”

# In[19]:


get_ipython().run_cell_magic('R', '', '#Import non-Ilana sample\nnon.ilana.mdws<-read.csv(file=\'non_ilana_sample.csv\', header=T)\n#Import Ilana quotes\nilana.mdws<-read.csv(file=\'ilana.csv\', header=T)\n#Label the columns for the Ilana quotes\ncolnames(ilana.mdws)<-c("Attribution", "Group", "Text")\n#Get the dimensions of the non-Ilana data\ndim(non.ilana.mdws)')


# In[20]:


get_ipython().run_cell_magic('R', '', '#Get the dimensions of the Ilana data\ndim(ilana.mdws)')


# “So far, so good,” said Mark. “Let’s make sure we’re seeing the right number for the different books with Ilana quotes.”

# In[21]:


get_ipython().run_cell_magic('R', '', '#Get Ilana quotes, grouped by book\ntable(ilana.mdws$Group)')


# “Now, we need to limit our Ilana quotes to just those books where she has the distinctive speech patterns.”

# In[22]:


get_ipython().run_cell_magic('R', '', '#Use only the Ilana quotes from books 9-12\nilana.quotes.mdws<-ilana.mdws$Text[which(ilana.mdws$Group %in% c(\'BYT9\', \'BYT10\', "BYT11", "BYT12"))]\n#Get the length of the Ilana quotes from the distinctive books\nlength(ilana.quotes.mdws)')


# “We’ve already imported the same sample as before for the non-Ilana quotes, so we have the same number as the Ilana quotes. Now, we’ll put all the quotes together into a single R vector.”

# In[23]:


get_ipython().run_cell_magic('R', '', '#Create a vector of just the text of non-Ilana quotes\nnon.ilana.quotes.mdws<-non.ilana.mdws$Text\n#Combine Ilana and non-Ilana quotes\nquotes.mdws<-c(ilana.quotes.mdws, non.ilana.quotes.mdws)\nlength(quotes.mdws)')


# In[24]:


get_ipython().run_cell_magic('R', '', '#Create a vector for groups, to label Ilana & non-Ilana data\ngroups.mdws<-c(rep("Ilana", 230), rep("nonIlana", 230))\nlength(groups.mdws)')


# “Finally, we’ll create a new table out of the corpus of quotes and the group designations.”

# In[25]:


get_ipython().run_cell_magic('R', '', '#make a new table out of the sampled corpus and group designations\nnew.ilana.table.mdws<-data.frame(groups.mdws, quotes.mdws)\nmetadata.table.mdws<-new.ilana.table.mdws')


# “Let’s clean our quotes next! We should also check to see if the default English stopwords list includes any of the ‘Ilana words’.”

# In[26]:


get_ipython().run_cell_magic('R', '', '#Extract the text from the table\nraw.corpus.mdws<-quotes.mdws\n#Apply the cleaning function\nclean.corpus.mdws<-lapply(raw.corpus.mdws, function(x) fullClean(x))\n#Create a vector with the clean corpus\nclean.corpus.mdws<-Corpus(VectorSource(clean.corpus.mdws))\n#Remove stopwords\nclean.corpus.mdws<-tm_map(clean.corpus.mdws, content_transformer(removeWords), stopwords("en"))\n#Create a vector with the default English stopwords list\nall.sw<-stopwords(\'en\')\n#check if stopwords contains Ilana-specific works\nall.sw')


# Mark skimmed the list, then frowned. “Let’s double-check that the major ‘Ilana words’ aren’t going to get caught in our stopwords list. We can search for them like this.”
# 

# In[27]:


get_ipython().run_cell_magic('R', '', 'which(all.sw=="like")')


# In[28]:


get_ipython().run_cell_magic('R', '', 'which(all.sw=="really")')


# “That means those words aren’t there,” said Mark. “Compared to this, if we pick a word that is on the list:”

# In[29]:


get_ipython().run_cell_magic('R', '', 'which(all.sw=="has")')


# “This shows that ‘has’ is the 47th word on the stopword list. All right, it’s good to know we won’t be dropping all the Ilana-specific words. Next, let’s make a document-term matrix.”

# In[30]:


get_ipython().run_cell_magic('R', '', 'corpus.dtm.mdws<-DocumentTermMatrix(clean.corpus.mdws, control=list(wordLengths=c(1,Inf)))\ncorpus.dtm.mdws')


# “Let’s see if we have any quotes that just get deleted entirely once we remove stopwords.”

# In[31]:


get_ipython().run_cell_magic('R', '', '#Get the document-term matrix as a matrix\ncorpus.matrix.mdws<-as.matrix(corpus.dtm.mdws)\n#Add up the word counts for each row (quote)\nall.sums.mdws<-rowSums(corpus.matrix.mdws)\n#Which ones have a total word count of zero (i.e. no words)\nwhich(all.sums.mdws==0)')


# “Hmm… what were those quotes before they got deleted?”
# 

# In[32]:


get_ipython().run_cell_magic('R', '', 'raw.corpus.mdws[which(all.sums.mdws==0)]')


# “Okay, we can live with that. Let’s remake our corpus matrix with only those quotes that don’t get deleted by the stopwords.”

# In[33]:


get_ipython().run_cell_magic('R', '', 'corpus.matrix.mdws<-as.matrix(corpus.dtm.mdws)\ncorpus.matrix.mdws<-corpus.matrix.mdws[-which(all.sums.mdws==0),]\ndim(corpus.matrix.mdws)')


# “And update our metadata table to remove the metadata for quotes that would be deleted by the stopwords.”

# In[34]:


get_ipython().run_cell_magic('R', '', 'metadata.table.mdws<-metadata.table.mdws[-which(all.sums.mdws==0),]\ndim(metadata.table.mdws)')


# “Now that we have that in order, we’re going to look for the 500 most frequent words, and sort them in descending order.”

# In[35]:


get_ipython().run_cell_magic('R', '', 'n=500\nword.sums.mdws<-colSums(corpus.matrix.mdws)\nword.sums.mdws<-sort(word.sums.mdws, decreasing=T)\nmfw.mdws<-names(word.sums.mdws[1:n])\nmfw.mdws')


# “Oh yeah, those top most-frequent words are VERY Ilana,” I said, looking at the list. 
# 
# “Let’s run the most distinctive word code that we usually use around the Lab,” said Mark. “We’ll use 0.05 as the cut-off – the usual threshold for statistical significance – though sometimes we use something much smaller to find highly distinctive words.”
# 
# “How does that code work?” I asked.
# 
# “Basically, we give it a vector of groups – in this case, we’ve got Ilana and Non-Ilana. For each group, we compare the text in that group to all the text in the other groups combined and ask, ‘What if we take the word frequencies in all the *other* groups as kind of like a default?’ Then we look at what words in the group text occur *statistically significantly more frequently* than in the other groups put together.”

# In[36]:


get_ipython().run_cell_magic('R', '', '#This code is called by the function below - don\'t run this by itself\n#Code takes two variables. \n#1. A document term matrix (rows as documents, columns as words, cells as counts of words in documents)\n#2. A vector of group assignments for the texts\nqdMDWs<-function(dtm.matrix, groups, alpha=0.05){\n  #let user know what\'s happening\n  print("MDWs")\n  #get all of the actual words from the columns in the document term matrix\n  all.terms<-colnames(dtm.matrix)\n  #figure out which columns in the DTM correspond to the target population\n  target.index<-which(groups=="Target")\n  #Assuming that there are more than one text in the target group\n  if(length(target.index)>1){\n    #get the total count of each word for all of the texts in the target group\n    target.sub<-colSums(dtm.matrix[target.index,])\n    #if not\n  } else {\n    #just get the counts for that text\n    target.sub<-dtm.matrix[target.index,]\n  }\n  #get the total count for all groups of each words\n  total.obs<-colSums(dtm.matrix)\n  #get the total word count for all of the words in the target subset of the corpus\n  target.words<-sum(target.sub)\n  #calculate frequencies of words in target group by dividing by total words in corpus\n  target.scaled<-target.sub/sum(target.sub)\n  #calculate frequencies of all words in the corpus (target and non-target)\n  total.scaled<-total.obs/sum(total.obs)\n  #find expected number of each words in the target sub-corpus by multiplying the total frequency across the entire corpus by the number of words in the target corpus\n  target.exp<-round((total.scaled*target.words), 0)\n  #find the difference between the expected number of words and the actual number of words in the target subcorpus\n  term.diff<-target.sub-target.exp\n  #find all of the words that show up less frequently than expected\n  keep.index<-which(term.diff>0)\n  #remove the words that show up less frequently than expected from the total corpus\n  all.terms<-all.terms[keep.index]\n  #remove the words that show up less frequently than expected from the target subcorpus\n  target.sub<-target.sub[keep.index]\n  #remove the words that show up less frequently than expected from the target expected subcorpus\n  target.exp<-target.exp[keep.index]\n  #find the total number of times for each word that it isn\'t in the target corpus\n  target.missing<-target.words-target.sub\n  #find the total number of times for each expected word that would would expect to not find it in the target corpus\n  target.missing.exp<-target.words-target.exp\n  #for every word, create a 2x2 contingency table of the number of times the word appears, the number of times it doesn\'t appear, the number of times we expect it to appear, the number of times we expect it not to appear\n  all.c.tables<-mapply(function(x,y,z,a) matrix(c(x,y,z,a), ncol=2, byrow=T), target.sub, target.exp, target.missing, target.missing.exp, SIMPLIFY=F)\n  #run a fisher\'s exact test on all of the contingency tables (1 ber word)\n  all.fishers<-lapply(all.c.tables, function(x) fisher.test(x))\n  #extract the p value from all of the fisher\'s tests\n  all.p<-unlist(lapply(all.fishers, function(x) x$p.value))\n  #figure out which ones are significantly more present\n  sig.index<-which(all.p<alpha)\n  #tell the user you are about to print out the number of significant mdws\n  print("Significant MDWs:")\n  #print the number of significant mdws\n  print(length(sig.index))\n  #if there are more than 0 mdws\n  if(length(sig.index)>0){\n    #create a vector of the words (the mdws)\n    Term<-all.terms[sig.index]\n    #create a vector of the number of times each word appears in the target corpus\n    Obs<-target.sub[sig.index]\n    #create a vector of the frequency of the words in the target corpus\n    ObsScaled<-Obs/target.words\n    #create a vector of the observed over expected for each word\n    Obs_Exp<-Obs/target.exp[sig.index]\n    #create a vector of the p.values for each word\n    pValue<-all.p[sig.index]\n    #merge all of these vectors into a dataframe\n    final.table<-data.frame(Term, Obs, ObsScaled, Obs_Exp, pValue)\n    #sort the data frame by the ObsScaled\n    final.table<-final.table[order(final.table[,3], decreasing=T),]\n    #create a column ranking the words by their scaled frequency\n    final.table$Rank<-seq(1, nrow(final.table), by=1)\n    #return the table\n    return(final.table)\n  } else {\n    #if there are no mdws, return an NA\n    return(NA)\n  }\n}\n\n#this is the code to run, it takes two variables\n#1) a document term matrix (words as columns, texts as rows, cells as individual counts (NOT FREQUENCIES))\n#2) a vector of group assignments for the texts - the code will find MDWs for each group\nallMDW<-function(dtm.matrix, group.vector, alpha=0.05){\n  #find the names of the unique groups\n  unique.groups<-unique(group.vector)\n  #find the number of unique groups\n  num.groups<-length(unique.groups)\n  #create an empty list to put the mdw tables in\n  all.mdws<-list()\n  #for each group\n  for(i in 1:num.groups){\n    #get the name of the current group\n    curr.group<-unique.groups[i]\n    #print out the name of the current group\n    print(curr.group)\n    #move group vector into a temporary variable\n    temp.groups<-group.vector\n    #rename all of the elements of that vector that correspond to the current target group as "Target"\n    temp.groups[which(temp.groups==curr.group)]<-"Target"\n    #run the code above, but sending the original dtm, by our modified group vector in which the ones we care about are now named "Target"\n    mdws<-qdMDWs(dtm.matrix, temp.groups, alpha)\n    #if there are any MDWs\n    if(!is.na(mdws)){\n      #On the resulting table from the code above, create a new column labeled by the name of the group\n      mdws$Group<-rep(curr.group, nrow(mdws))\n      #add that mdw table (the current one) to the list of all mdw tables\n      all.mdws<-c(all.mdws, list(mdws))\n    }\n  }\n  #collapse the list of all mdw tables into one big table\n  all.mdws<-do.call("rbind", all.mdws)\n  #return it\n  return(all.mdws)\n}')


# “Okay, let’s run it!” I said.

# In[37]:


get_ipython().run_cell_magic('R', '', '#Get the group data from the metadata\ngroup.source.mdws<-metadata.table.mdws$Group\n#Run the allMDW function using the corpus, the groups, and a cut-off of 0.5\nmdw.table<-allMDW(corpus.matrix.mdws, group.source.mdws, 0.05)\n#Create a CSV for the MDWs\nwrite.csv(mdw.table, file="CorpusMDWs.csv", row.names=F)\nmdw<-unique(mdw.table[,1])')


# “Well, it looks like there are no distinctive words in Ilana quotes vs. non-Ilana,” said Mark.
# 
# “How can that be?” I asked. “What about ‘totally’, ‘like’, ‘amazing’...?”
# 
# “They’re a noticeable part of some of the Ilana quotes, sure, but they’re not so frequent across all the Ilana quotes to be picked up here,” Mark replied. “For fun, let’s double the cut-off, though the higher we raise this number the more dubious our results are as ‘most distinctive words’.”
# 

# In[38]:


get_ipython().run_cell_magic('R', '', 'group.source.mdws<-metadata.table.mdws$Group\n#Now we\'re using .1 as the cutoff\nmdw.table<-allMDW(corpus.matrix.mdws, group.source.mdws, 0.1)\nwrite.csv(mdw.table, file="CorpusMDWs-v2.csv", row.names=F)\nmdw<-unique(mdw.table[,1])')


# ### Trying PCA

# "Okay. Let's give the most distinctive words a miss. What if we see if there's any separation using PCA?"
# 
# PCA -- finally, that was a method I knew something about thanks to Heather Froehlich in [DSC 10: Heather Likes Principal Component Analysis](https://datasittersclub.github.io/site/dsc10.html). In that book, we used a couple different sets of word frequencies to see how the Baby-Sitters Club books -- and other young-reader series books -- clustered, in ways connected to author and topic.
# 
# "We're going to scale our corpus for length by turning word counts into word frequencies -- dividing each word count by the length of the document. We know that there is not a significant difference between Ilana and non-Ilana quotes, but there ARE some that are shorter. We don't want our model to just group these together and tell us they're one thing. So after we scale the corpus, we'll just keep the most frequent words we identified earlier."

# In[39]:


get_ipython().run_cell_magic('R', '', '#Sets the working directory (e.g. where it looks for files)\nsetwd("/Users/qad/Documents/GitHub/dsc15")\n#Reads the non-Ilana quotes CSV\nnonilana.pca<-read.csv(file=\'non_ilana_sample.csv\', header=T)\n#Reads the Ilana quotes CSV\nilana.pca<-read.csv(file=\'ilana.csv\', header=T)\n#Sets the column names on the Ilana quotes to be attribution, source, quote\ncolnames(length.ilana)<-c("Attribution", "Source", "Quote")\n#Checks the dimensions (rows, columns) for the non-Ilana quotes\ndim(length.nonilana)')


# In[40]:


get_ipython().run_cell_magic('R', '', 'ilana.quotes.pca<-ilana.mdws$Text[which(ilana.mdws$Group %in% c(\'BYT9\', \'BYT10\', "BYT11", "BYT12"))]')


# In[41]:


get_ipython().run_cell_magic('R', '', '#Turn word counts into word frequencies\nscaled.dtm.pca<-corpus.matrix.mdws/rowSums(corpus.matrix.mdws)\n#Get the most frequent words using the scaled corpus\nfeatures.to.keep.mdws<-mfw.mdws\n#Create the feature table\nfeature.table.pca<-scaled.dtm.pca[,which(colnames(scaled.dtm.pca) %in% features.to.keep.mdws)]\nfeature.names.pca<-colnames(feature.table.pca)\n\n#Do PCA to see if there is visual separation between the groups based on all 500 most frequent words\ncolnames(feature.table.pca)<-feature.names.pca\ntest.pca<-prcomp(feature.table.pca)\n#Load the biplot library\nlibrary(ggbiplot)\n#Generate the biplot\ntest.pca<-prcomp(feature.table.pca, scale=T)\nggbiplot(test.pca, ellipse=T, groups=metadata.table.mdws$Group)')


# “Nope. Nope, there is not,” said Mark. 
# 
# I could see what he meant, thanks to [DSC 10](https://datasittersclub.github.io/site/dsc10.html) – everything was all lumped together, rather than distributed across all the quadrants, or arranged in nice clumps. 
# 
# “Maybe the 500 most distinctive words is just too much. Let’s try PCA with just the top 50.”

# In[42]:


get_ipython().run_cell_magic('R', '', '#Try again with 50 words\ntop.mfw.pca<-mfw.mdws[1:50]\ntop.mfw.pca')


# In[43]:


get_ipython().run_cell_magic('R', '', '#Only keep the top 50 features\ntop.features.pca<-feature.table.pca[,which(colnames(feature.table.pca) %in% top.mfw.pca)]\n#Get the actual words\nfeature.names.pca<-colnames(feature.table.pca)\ndim(top.features.pca)')


# “We’ve got the 50 most frequent words occurring in our corpus of 448 quotes,” said Mark. “It’s 448 because we lost some to stopwords. Let's see if this does any better with PCA.”

# In[44]:


get_ipython().run_cell_magic('R', '', 'colnames(feature.table.pca)<-feature.names.pca\ntest2.pca<-prcomp(top.features.pca)\nlibrary(ggbiplot)\ntest2.pca<-prcomp(top.features.pca, scale=T)\nggbiplot(test2.pca, ellipse=T, groups=metadata.table.mdws$Group)')


# “Hmm… PC1 still only explains about 4% of the variation,” said Mark grimly. “Maybe we’re just looking at too many features. How about if we try a stepwise variable selection to see if we can find a better feature set for classification?”

# ### Stepwise variable selection
# “I was with you on PCA, but you’ve lost me again,” I said.
# 
# “Stepwise selection – sometimes it’s called stepwise regression – involves adding and removing predictors – things that you might use to differentiate one group from another – until you get the set of variables that get you the best-performing model.”
# 
# “Got it! Let’s see what it gives us!” I exclaimed.
# 
# “I’ll set the stop criterion to be an improvement of less than 0.1% – so if it doesn’t improve by that much, it will stop adding and subtracting predictors.”
# 

# In[45]:


get_ipython().run_cell_magic('R', '', 'setwd("/Users/qad/Documents/GitHub/dsc15")\nilana.sc<-read.csv("ilana.csv", header=T)\nnon.ilana.sc<-read.csv("non_ilana_sample.csv", header=T)\nilana.quotes.sc<-ilana.sc$Quote[which(ilana.sc$Source %in% c("BYT9", "BYT10", "BYT11", "BYT12"))]\nall.text.sc<-c(ilana.quotes.sc, non.ilana.sc$Text)\ngroups.sc<-c((rep("Ilana", 230)), rep("NonIlana", 230))')


# In[46]:


get_ipython().run_cell_magic('R', '', 'metadata.table.sc<-data.frame(all.text.sc, groups.sc)\ncolnames(metadata.table.sc)<-c("Text", "Group")\nraw.corpus.sc<-all.text.sc\nclean.corpus.sc<-lapply(raw.corpus.sc, function(x) fullClean(x))\n#Create a vector with the clean corpus\nclean.corpus.sc<-Corpus(VectorSource(clean.corpus.sc))\ncorpus.dtm.sc<-DocumentTermMatrix(clean.corpus.sc, control=list(wordLengths=c(1,Inf)))\ncorpus.matrix.sc<-as.matrix(corpus.dtm.sc)\ncorpus.dtm.sc')


# In[47]:


get_ipython().run_cell_magic('R', '', 'n=75\nword.sums.sc<-colSums(corpus.matrix.sc)\nword.sums.sc<-sort(word.sums.sc, decreasing=T)\nmfw.sc<-names(word.sums.sc[1:n])\nscaled.dtm.sc<-corpus.matrix.sc/rowSums(corpus.matrix.sc)\nfeatures.to.keep.sc<-mfw.sc\nfeature.table.sc<-scaled.dtm.sc[,which(colnames(scaled.dtm.sc) %in% features.to.keep.sc)]\nfeature.names.sc<-colnames(feature.table.sc)\ncolnames(feature.table.sc)<-feature.names.sc\ndim(feature.table.sc)')


# In[48]:


get_ipython().run_cell_magic('R', '', 'library(klaR)\nfeature.names.sc<-gsub("’", "\'", feature.names.sc)\ncolnames(feature.table.sc)<-feature.names.sc\nvars<-stepclass(feature.table.sc, metadata.table.sc$Group, method="lda", improvement=0.0001)')


# “This could be worse,” sighed Mark. “But 70% is still not great. Quotations are hard because they’re very short. We need to find the right feature set,” he concluded. “I’m not feeling it.”
# 
# “Is that it?” I asked, a note of despair creeping into the question. “We just can’t tell the difference computationally?”
# 
# “Oh no, we’ve only been playing with this for ten minutes,” laughed Mark. “I don’t usually give up this easily.” 

# ### Measuring the human success rate
# 
# Mark considered the data for another moment. A little smile crept over his face. “Let’s play a game. I’m going to read you a quote, and you’ll tell me if it’s Ilana or non-Ilana.”
# 
# “Same way as yesterday.” - “Not Ilana.”
# 
# “Mellow out, Pinky!” - “Maybe?”
# 
# “I told you something would come up.” - “Not Ilana.”
# 
# “Winter, yuk.” - “Oh, that’s Ilana – New York winters are rough if you’re coming from California.”
# 
# “I wish you’d come with us, Pinky.” - “Not Ilana.”
# 
# “Could you run down to the grocery and pick up some for me?” - “Not Ilana.”
# 
# “What size is your sign going to be?” - “Not Ilana! I remember that part, I’m pretty sure that was something with the twins.”
# 
# “Nechama, look! That’s amazing!” - “Definitely Ilana.”
# 
# “We have to be able to do things openly.” - “Not Ilana.”
# 
# We went on in that fashion for a while.
# 
# Mark tallied the results. “So you got 9 right out of 15 – and of the wrong ones, you said that 6 were not Ilana when, in fact, they were. 60% is better than chance, but not by a whole lot – and that’s you who’s read the books and has the knowledge of the plot. The computer won’t have that, so teaching it to do any better than you is going to be tricky.”
# 
# That’s a good point to remember when you’re doing this work. Things like narrative context? That’s still pretty much a human-exclusive thing. There are algorithms that “understand” (don’t understand like a human) “context” (a window of words around the word you’re looking at) – things like word vectors, which we’ll cover in a future book. But remembering that something must be a quote from a particular character because of where or how it appeared in a story? That’s a job for squishy human brains.
# 
# “There are two classic problems with text analysis here,” mused Mark. “One is that I don’t think we have enough text in our examples. Classifying at the dialogic level is not going to be useful. Or possible!”
# 
# “It’s funny,” I said. “Reading these books as a human, the differences in her speech style are *really prominent*. And the text even brings it up explicitly, through her mother teasing her. But is this one of those cases where it’s just human perception being about more than just frequency?”
# 
# “I think you’re right, the things that pop out to us as readers or the characters listening to her are just not frequent enough for a computer,” said Mark. “The fact that you have false negatives is telling. When you saw a ‘California girl sentence’, you recognize it as Ilana, but she’s not saying a lot of sentences all the time. If we take this as a representative sample, you only identified 60% of the Ilana sentences – which means around 40% of the time, what Ilana is saying isn’t a ‘California girl sentence’. Which is not to say she doesn’t have a distinctive discourse…”
# 
# Mark pulled up RStudio.
# 
# “Based on our stepwise variable selection,” said Mark, “The best three words for differentiating Ilana and non-Ilana are ‘like’, ‘amazing’, and ‘right’. There's 33 Ilana quotes with 'like'... and 11 non-Ilana quotes with it."
# 
# "And realistically, those 11 are probably mostly verbs," I added. "Or maybe prepositions. But no one's using 'like' like Ilana."
# 
# "True," Mark smiled. "And I know it's a little uncomfortable, comparing things this way. All we're doing is looking at the frequency of the word 'like', however it's being used. But there's something to that: when it's used as a discourse particle, like Ilana uses it, 'like' appears with a different frequency than when it's used as a verb of preposition. When we see a lot of 'like', odds are it's being used as a discourse particle. Now, if we wanted to be absolutely certain, in theory we have the tools for it: we could use natural-language processing algorithms, like Stanford NLP, to try to parse the syntax of these quotes and identify where 'like' is being used as a verb, vs. preposition, vs. discourse particle. But even for English, I don't think the NLP models are trained on data that would reliably identify the discourse particle usage of 'like' -- a lot of it is news sources!"
# 
# We'd been down this road before, with [DSC Multilingual Mystery 2: Beware, Lee and Quinn!](https://datasittersclub.github.io/site/dscm2.html) The French model struggled to identify and categorize entities in French that it could easily do in English. So it's a similar problem here, even if it gets further into the nuances of the model than just named entities.
# 
# "What all this shows is what I was thinking when I saw this data," concluded Mark. "Based on words, and trying to classify quotes, Ilana's discourse is just not distinctive enough across all her utterances. Only 40% of the sentences are 'California girl sentences', and that's it. There are three possibilities here: one, we could try moving on to a classifier that's better or more precise... but I don't know how close we're going to get. If you can't do it, I don't think the best neural net is going to do it. Two, we could stop trying to classify sentences and knit this into larger blocks of text. That'd be a little artificial, but if it's all glued together we'll see differences in discourse. Three, we try non-word features. Part-of-speech is one option, punctuation is another, and strings of three characters are another one."

# ### Three-character sequences
# 
# I fixed Mark with a hard stare. “I don’t like that last one. Why would you break up words?”
# 
# “It gets you more things to count, especially when you don’t have a lot of text. And three-character sequences have proven to be more reliable than words for forensic analysis in cases where we have very little text.”
# 
# “Fine, but… they’re … not … words. Like, we’re getting into English morphology here, but not even rigorously, because you’re going to end up with three-character sequences like ‘ing’ where, okay, that’s a gerund, but you’re going to get other ones that span the root/inflection boundary, and… *I DON’T LIKE IT*,” I sputtered.
# 
# “Words have their downsides, too,” Mark nudged. “Andrew Piper’s been arguing for years that characters aren’t distinctive, that we the readers bring the distinctiveness of characters to the characters. Insofar as stylometry is ‘right’ – which is to say, if ‘style’ is the product of authorial unconscious word usage – it’s impossible for an author to lose their own ‘style’ to the point where characters can assume distinctive voices. So I could write a California girl, but she’s going to sound like the Mark version of a California girl, and the second I write a sentence for her that doesn’t include ‘like’, ‘totally’, or ‘amazing’... then it’s going to sound like me.”
# 
# I was very reluctantly willing to try this. We considered the different options together. There was some data we had to throw out because the whole thing was less than three characters (e.g. “Hi”). We decided punctuation might be important here– Ilana likes exclamation marks.
# 
# Mark picked up on my ongoing anxiety about this approach. “The way I see it, when we do this kind of work, our questions are guided by humanistic inquiry, but our interpretation should be guided by … results. So, if it works, that means that there’s something that’s happening at a differentiable level. Just because strings of three characters aren’t meaningful for us as readers doesn’t mean they’re not meaningful, period.” Mark continued to type away at the R code. “I still don’t think this is going to work…” he said. “On these things, I sit in a weird place between the scarf-wearing crowd…” – and it’s true, Mark does also have a beard – “... and the people who want results to be human-readable. This is a problem at a deep level, like neural nets that create math proofs that work, but we can’t really trace the path to see how. But I think it’s interesting that there’s something about these things that we don’t see as readers, but is legible at a different level.”
# 
# Mark re-imported all the data, limited Ilana’s quotes to the books where she has distinctive dialogue, used the sample of the non-Ilana dialogue, and added it to a new text vector.

# In[49]:


get_ipython().run_cell_magic('R', '', 'setwd("/Users/qad/Documents/GitHub/dsc15")\nilana.tg<-read.csv("ilana.csv", header=T)\nnon.ilana.tg<-read.csv("non_ilana_sample.csv", header=T)\nnon.ilana.tg<-non.ilana.tg[,2]\nilana.quotes.tg<-ilana.tg$Quote[which(ilana.tg$Source %in% c("BYT9", "BYT10", "BYT11", "BYT12"))]\nall.text.tg<-c(ilana.quotes.tg, non.ilana.tg)\nall.groups.tg<-c(rep("Ilana", length(ilana.quotes.tg)), rep("NonIlana", length(non.ilana.tg)))\nlength(all.groups.tg)')


# “And now, let’s write out the code for creating trigrams.”
# 

# In[50]:


get_ipython().run_cell_magic('R', '', '#Function for creating trigrams\n#Subs spaces with an underscore, finds start and end points, and applies it to text\nmakeCharacterTrigrams<-function(dialogue, str.length=3){\n  dialogue<-gsub(" ", "_", dialogue)\n  dialogue.sep<-unlist(strsplit(dialogue, ""))\n  starting.points<-seq(1,(length(dialogue.sep)-(str.length-1)), by=1)\n  ending.points<-starting.points+(str.length-1)\n  all.str<-mapply(function(x,y) dialogue.sep[x:y], starting.points, ending.points, SIMPLIFY = F)\n  all.str<-unlist(lapply(all.str, function(x) paste(x, collapse="")))\n  return(all.str)\n}')


# “Next, let’s create the trigrams.”

# In[51]:


get_ipython().run_cell_magic('R', '', '#Lower-cases all text\nall.text.tg<-tolower(all.text.tg)\nall.text.length.tg<-unlist(lapply(all.text.tg, function(x) length(unlist(strsplit(x, "")))))\n#Identifies quotes with fewer than 3 characters & removes it\nbadtext.tg<-which(all.text.length.tg < 3)\nif (length(badtext.tg) > 0) {\n  all.text.tg<-all.text.tg[-badtext.tg]\n  all.groups.tg<-all.groups.tg[-badtext.tg]\n}                      \n#Applies trigram-making code to the text\nall.trigrams.tg<-lapply(all.text.tg, function(x) makeCharacterTrigrams(x))\nall.trigrams.tg<-unlist(lapply(all.trigrams.tg, function(x) paste(x, collapse=" ")))\n#Print quote 60 in its trigram form\nall.trigrams.tg[60]')


# There they were. Mark’s trigrams. “Let's see,” re-formatted into nearly 30 trigrams– the underscore represents a space. Our quotes were looking even more data-ish and even less like literature than ever, separated into three-character strings. I was feeling edgy as we built the new corpus.

# In[52]:


get_ipython().run_cell_magic('R', '', '#Create a metadata table with all the texts and all the groups\nmetadata.table.tg<-data.frame(all.groups.tg, all.text.tg)\n#Label the columns\ncolnames(metadata.table.tg)<-c("Group", "Text")\n#Create a corpus with the trigrams\nraw.corpus.tg<-all.trigrams.tg\nclean.corpus.tg<-Corpus(VectorSource(raw.corpus.tg))\n#Create document-term matrix\ncorpus.dtm.tg<-DocumentTermMatrix(clean.corpus.tg, control=list(wordLengths=c(1,Inf)))\ncorpus.matrix.tg<-as.matrix(corpus.dtm.tg)\ncorpus.dtm.tg')


# “We’ve got 460 ‘docs’ – that’s the quotes – and 2933 ‘terms’.” I squirmed slightly at the use of ‘term’ to refer to these three-character strings. “We’ve also got 98% sparsity – which is to say, most trigrams don’t appear in 98% of the quotes.” 
# 
# That made sense, because of the length of these quotes, if nothing else: a quote like “hi” contains (not even) one three-character string.
# 
# “A rule of thumb for doing classification: the number of variables you include should not be more than 1/3 the number of observations for the smallest group. You’ve got two groups, and they both have 230 things – so 1/3 of 230 is roughly 76. You shouldn’t be using more than 76 features, as an upper limit. DH folks love to make models with giant numbers of features, and we should not do that because it becomes less significant, the more features you use. It’s why social scientists laugh at us,” Mark commented dryly.
# 
# “Let’s go with 75 features,” said Mark as he typed away at the R code. “One nice thing about doing subwords is that they solve a lot of problems. Words are collinear with each other, because they’re words and have syntax.”
# 
# “What does collinear mean?” I asked.
# 
# “It’s when you have two variables that move in concert with each other. An easy example would be ‘Queen Elizabeth’ – those words are probably always going to appear together, and having words that always appear together will throw weird stuff into the model. The three-character sequences break up those relationships: ‘Queen’ might only appear with ‘Elizabeth’, but once you split it up into three-character sequences, you could also get ‘que’ with ‘question’.”
# 
# I was starting to appreciate the upside of these three-character sequences, though I still struggled to imagine what I would say as the conclusion if this worked. “Ilana’s speech isn’t reliably distinguishable from the other characters on any level but the three-letter-sequence level, where it is!” For better or worse, though, I didn’t have that problem.
# 
# “Let’s see how badly they did…”
# 

# In[53]:


get_ipython().run_cell_magic('R', '', 'n=75\nword.sums.tg<-colSums(corpus.matrix.tg)\nword.sums.tg<-sort(word.sums.tg, decreasing=T)\nmfw.tg<-names(word.sums.tg[1:n])\ngroup.source.tg<-metadata.table.tg$Group\nmdw.table.tg<-allMDW(corpus.matrix.tg, group.source.tg, 0.05)\nmdw.table.tg')


# Once again, MDWs for Ilana were coming up short. How about trying the stepwise variable selection, but for trigrams? We replaced the underscores with spaces again, and set up the feature table.

# In[54]:


get_ipython().run_cell_magic('R', '', "scaled.dtm.tg<-corpus.matrix.tg/rowSums(corpus.matrix.tg)\nfeatures.to.keep.tg<-mfw.tg\nfeature.table.tg<-scaled.dtm.tg[,which(colnames(scaled.dtm.tg) %in% features.to.keep.tg)]\nfeature.names.tg<-colnames(feature.table.tg)\nfeature.names.tg<-gsub('_', ' ', feature.names.tg)\ncolnames(feature.table.tg)<-feature.names.tg\ndim(feature.table.tg)")


# In[55]:


get_ipython().run_cell_magic('R', '', 'library(klaR)\nfeature.names.tg<-gsub("’", "\'", feature.names.tg)\ncolnames(feature.table.tg)<-feature.names.tg\nvars<-stepclass(feature.table.tg, metadata.table.tg[,1], method="lda", improvement=0.0001)')


# "... Looks like the trigrams are just slightly better than Quinn."

# ### What have we learned here?
# 
# Classification is one of those computational methods that often gets whipped out as something that's pretty basic, especially in data science contexts. You've got all this data, and you just wave a magic wand and the computer will give you its idea of how it should be grouped. And especially with all the AI hype (which we've also debunked in [DSC 9](https://datasittersclub.github.io/site/dsc9.html)), it's tempting to think that surely all these algorithmic advances mean that computers should be able to easily tell the difference between groups of things you've identified for it, especially if you as a human can recognize the groups.
# 
# But there may be a difference between your impression of how well you can identify the groups, and what happens when you actually try it out. I think it's fair to say that, overall, Ilana's speech makes a different impression on readers than the other characters. But that doesn't mean that every one of her utterances contributes equally to that impression -- only around 60% have identifiable "California girl" traits. That said, even 60% is more than enough to get the message across.
# 
# But what, exactly, is the message? Growing up in the Seattle suburbs, the "California girl" was an archetype that didn't feel as distant -- and was certainly more accessible to my imagination, thanks to things like the movie Clueless -- as Dainy's life in an Orthodox Jewish community on the other side of the country. What was the deal with Ilana, anyway? Is there an embedded joke about hippies and tree-hugging in her name (which means "tree")? How much would the readers of these books recognize the stereotype she embodies? And why did her mannerisms change so completely after book 12? And also, what was the deal with Ilana anyway? It didn't seem too weird for Dawn's divorced mom to move back to her Connecticut hometown from California, but what was up with a family of Orthodox Jews running a kosher health-food store in California to begin with? And then deciding to move to an Orthodox Jewish suburb of New York?
# 
# The algorithms had come up short on classification, but I knew I could count on Dainy for some context.

# ## Dainy
# 
# ### What's up with Ilana anyway?
# Much like the distinction between the Brooklyn girls and the Bloomfield girls, within the world of the BYT, Ilana’s being from California holds specific Jewish cultural connotations in addition to the American stereotypes of blonde, laid-back, health-food nut. Interestingly, while the Orthodox East Coast girls don't have the same stereotypes as their non-Orthodox or non-Jewish East Coast counterparts, Ilana carries both the broader California stereotypes and specific Orthodox connotations. The Orthodox connotations show up more subtly, but Ilana's association with broader American culture is in itself a symptom. 
# 
# In the last decade of the twentieth century, Orthodox Jewish communities across America were being strengthened. The major hubs of American Jewish life, however, remained in the New York metropolitan area. The slight tension between the Brooklyn girls and the Bloomfield girls in War! is true to real-life dynamics between high school girls of that era. (At the 2006 national convention of Bais Yaakov seniors in Baltimore, my classmates and I - from the largest Bais Yaakov high school in Brooklyn - got a laugh from everyone else when a faculty organizer asked all "out of towners" to move to one side of the dining room and we didn't move. We were too used to calling others "out of towners," meaning anyone not from New York City.) Being from "out of town" was associated with a somewhat more lenient Jewish religious observance and a porousness between Orthodox and American culture. The smaller the Orthodox community infrastructure, after all, the more its members would need to interact with people outside their community - and the end of the twentieth century was characterized by an increasing push toward as much insularity as possible, leading these smaller, more porous communities to be viewed as somewhat inferior in religious observance by the larger, more insular communities.
# 
# Los Angeles had a growing Orthodox community, which is rich and vibrant today. But in the 1990s, it seemed like a completely foreign country to Orthodox teens on the East Coast. We didn't watch TV or movies (except for some rebellious kids, of course), but the California stereotype still filtered into our consciousness. Combining these factors - the idea of someone as far away as California being more connected to non-Jewish cultures and the idea of the laid back Californian health nut - explains why Ilana, in this cultural remix of the BSC, retains the mainstream American cultural stereotypes while the other characters are more ambiguously connected to their BSC counterparts.
# 
# <div style='float: right; width: 400px;margin-left: 7px;margin-top: 0px;'>
# <img src='_static/images/dsc15_healthfood.jpg' alt='Gemarakup book cover' />
# </div>
# 
# As to Quinn's question about why the Silvers would move from California to open a health food store in Bloomfield, I have only conjecture based on these cultural considerations. One of the big Orthodox cultural movements of the 90s and the decades preceding the 90s was the kiruv (religious outreach) movement. Efforts to bring unaffiliated or non-religious Jews into the Orthodox fold dominated quite a bit of time and energy. We get a glimpse of this through the character of Jen Farber, whose American name very clearly labels her a "returnee" to religious Judaism. We also see it through the "Russian" girls from Kyiv (as people from all Soviet countries were called “Russian” in Orthodox circles) who are rescued from behind the Iron Curtain and brought to America to live freely as religious Jews. 
# 
# Ilana's characterization is built around her California stereotypes, not her status as a ba'alas teshuvah, someone who became frum, a term used by the BYT girls to mean Orthodox, later in life. In Book 10, *The New Kids*, we're introduced to Jen Farber, whose characterization is focused on her status as a ba'alas teshuvah. When the girls of the BYT talk about the newest member of their newspaper, we get an internal thought from Ilana:
# 
# >"Okay." Chani took a deep breath. "It seems that Jack Farber himself only became frum very recently, and he sort of persuaded Jen to be frum too. Neither of her parents are frum at all. They're not anti-religious or anything like that, but they're definitely not Orthodox."
# >"Wow," breathed Batya. "That's tough."
# >"Yes, it is," said Ilana quietly.. None of the girls knew it, but her family, too, were *b'alei teshuvah*. She knew exactly how hard it could be.
# 
# So we know that Ilana's family used to be non-observant. It makes sense then that her family lived in California, assimilated the typical Californian mannerisms and attitudes, and ran a health shop there. In fact, I would venture to guess that their health shop in California was not kosher! Part of efforts to bring unaffiliated Jewish adults into Orthodoxy involve encouraging them to continue using their talents and expertise within the community. (An extreme example of this is Matisyahu, who began his musical career as a non-observant Jew, then took Orthodoxy upon himself and continued writing reggae but now with a more religious flavor.) It makes perfect sense for the Silvers to use their knowledge and expertise in the health food business as part of building their new lives. It wouldn't even take much - plants are all kosher, so nuts and sprouts wouldn't even need to be sourced differently. The only major change would have been making sure the juices and other processed snacks were produced with a Jew's supervision, making sure no non-kosher ingredients were added. 
# 
# Names are also important in marking Ilana as different. Jen and her brother Jack, whose main characteristics are being *ba'alei teshuvah*, are clearly marked as an outsider in this ultra-Orthodox enclave - the names Jen and Jack are unheard of in ultra-Orthodox communities, where names are generally drawn from the Bible or from Yiddish-speaking ancestors. Most of the BYT girls' names are shortened versions of Biblical names: Shani is Shoshana, Chani is Chana (Hannah), Pinky is Penina, Chinky is Chaya Rochel. Raizy is the nickname for Raizel, a Yiddish name meaning rose (like the Hebrew Shoshana). Nechama and Batya are both Hebrew, but not shortened. Batya's name also identifies her as slightly different: the Ashkenazic pronunciation of her name is Basya, not Batya, and her last name (Ben-Levi) is either Sephardic or Mizrachi. We know she has family in Israel, so that makes sense. She's accepted in the mostly-Ashkenazic ultra-Orthodox community because her background doesn't make her life experiences differ that much from the others.
# 
# Ilana's family name, Silver, identifies her as Ashkenazi, with European ancestry. Her first name, Ilana, however, is non-Biblical Hebrew, which is unusual in ultra-Orthodox Ashkenazi circles. Non-Biblical Hebrew names, in ultra-Orthodox Ashkenazi perception, signify a more "modern" lifestyle and religious identity. Jen's American name situates her more firmly as an outsider on account of her status as a *ba'alas teshuvah*, but Ilana's modern-Hebrew name situates her slightly closer to the BYT girls' lives on the spectrum of religiosity.
# 
# But we're not told that Ilana was once not Orthodox until the main *ba'alas teshuva* character is introduced. My reading of this is that Zakon wanted to introduce a "Dawn" character, for whom an Orthodox parallel does not readily exist, so she colored outside the lines of Orthodox experience and ret-conned Ilana's character as a *ba'alas teshuvah* to make things fit. This would also explain the sudden drop in human-reader-identifiable "Californian" speech after Book 12 - Ilana had been sufficiently identified as the outsider, and the focus on her not fitting in was no longer yielding interesting plot points. Besides, Book 13, *Flying High*, introduces yet another character who lives outside the American Orthodox community. The BYT girls find out about a young fan of their school newspaper who is sick, and her rich parents fly the girls to Zurich so she can meet them. There is in fact an Orthodox community in Zurich, but the book spends lots of time talking about how different Swiss people are from Americans. Including Ilana's Californian difference while focusing on the Swiss-American differences may have been too much. This book provided a good moment to drop the focus on Ilana's speech, which might also have become tedious for the readers.
# 
# I'll admit, I was disappointed to learn that the computer could not distinguish meaningfully between Ilana's speech and the others', and I still have a hard time accepting that what seems so obvious to us as human readers can be statistically not verifiable. Her speech stands out, but maybe that's because the stereotypical phrases are used in ways that sound foreign to the typical American ear: "Like, hi!" is not something we expect to hear even from the most stereotypical Californian. "Like" is just not used that way, and is clearly inserted by an author with only passing familiarity with stereotypical Californian speech patterns. 
# 
# Markers of insiders and outsiders are like that, though. They rely on minute details like names, verbal tics, clothing, food, etc., all of which is legible only to the insiders who are intimately familiar with community norms. For my own work, this is not a negative result - it's confirmation of the way communal identity is formed and the way that these kids' books strengthen that communal identity.
# 

# ## Suggested citation
# Suggested citation: Bernstein, Dainy, Quinn Dombrowski, and Mark Algee-Hewitt. “DSC \#15: Little Miss California Stereotype... and the BY Times.” *The Data-Sitters Club*, September 15, 2022. https://datasittersclub.github.io/site/dsc15.html.

# <a name="footnote" />&#42; 
# Saying something negative about a person even if it’s true. There’s a lot of concern about *lashon hara* in the *BY Times* books, as you might imagine for a series about a newspaper at a girls’ school.
