![DSC logo](_static/images/DSCLogo.png)
# The Ghost in Anouk's Laptop

<div style='float: right; width: 200px;margin-left: 7px;margin-top: 0px;'>
<img src='_static/images/bookcovers/dsc9_cover.jpg' alt='DSC 9 book cover' />
</div>

by Anouk Lang and Quinn Dombrowski with Annie K. Lamar

February 17, 2021

## February 2020

### Anouk
February 2020. It was about as far as it was possible to be from the sunny nostalgia of kids-playing-out in 1980s Connecticut. Storms were raging up and down the British Isles, some unsettling news about a virus was just beginning to rear its head, the UK had initiated the process to leave the EU and a significant part of the British university sector, including my own institution, was on strike. But the Data-Sitters Club had just been nominated for the Best Use of DH for Fun in the annual [Digital Humanities Awards](http://dhawards.org/dhawards2019/results/) and if ever there was a time when the respite of data-play was needed to drown out the literal and figurative storms in the real world, it was now. I came home from a very cold stint on the picket line, thawed out my fingers, opened up my laptop and thought: if the world's going to end, what better thing to do than feed our Baby-Sitters Club corpus to GPT-2 to see what larfs it might deliver?

GPT-2 (short for Generative Pre-trained Transformer) is a large-scale model of language which, in the words of its creators at OpenAI, produces[  "conditional synthetic text samples of unprecedented quality, where we prime the model with an input and have it generate a lengthy continuation."](https://openai.com/blog/better-language-models/) In functional terms, it takes what it knows about how language behaves, at least according to a dataset of 8 million (mostly English) web pages considered to be useful by Reddit users, translates the relationships between words and phrases in that 8-million page corpus into a list of numbers, and then, if given a prompt to start it off, will automatically generate text that follows on from that prompt using what it has learnt from the larger corpus. OpenAI opted not to release the full GPT-2 model over concerns that it could be used maliciously, as it did such a good job of imitating human-generated text, so they released a smaller version of the model for everyone other than themselves to use. And use it they did: the months since GPT-2's release have seen a steady increase in the number of people experimenting with it, not just from computer science but also from the humanities and the cultural industries.

Some of this activity is due to[  Talk To Transformer](https://talktotransformer.com/), a handy web-based GUI requiring no technical expertise. Until recently, Talk To Transformer offered users the opportunity to divert themselves by typing in a few words or sentences, on the basis of which it would then generate chunks of text somewhere on the continuum from amusing incongruity to uncanny likeness. Janelle Shane used it, along with other neural networks, to compile a collection of AI-generated texts on her[  AI Weirdness](https://aiweirdness.com/) website, the funniest of which suggest that the process works best -- at least for the purposes of comedy -- when the prompts come from identifiable genres that the model can, so to speak, recognize and reproduce, such as[  names of cookies](https://aiweirdness.com/post/620645957819875328/this-is-the-openai-api-it-makes-spookily-good),[  tweets from WeRateDogs](https://aiweirdness.com/post/620645957819875328/this-is-the-openai-api-it-makes-spookily-good), or[  Christmas carols](https://aiweirdness.com/post/189845472982/the-ais-carol) (for extra laughs, listen to what happened when a voice actor[  recorded](https://twitter.com/JoeZieja/status/1209511648618172421) one of the creepier carols). Another of my favourite GPT-2 toys is[  AI Dungeon](https://play.aidungeon.io/), a text-based fantasy game which brings the "yes, and" of improv to bear on the genre of the Choose Your Own Adventure story, creating an interactive adventure game many orders of magnitude better than its[  print culture predecessor](https://www.software.ac.uk/blog/2016-10-07-choose-your-own-adventure). Here it is[  seamlessly incorporating instructions about installing software packages into a fantasy narrative](https://twitter.com/eturner303/status/1216476218603630592). Or, if you want to run something on your own machine, try[  the packages Robin Sloan put together to generate snippets of sci-fi](https://www.robinsloan.com/notes/writing-with-the-machine/).

So, like many DH folks, I'd had a play with, and a good chortle at, automatic text generators done with neural networks. For this more extended foray into GPT-2 using our BSC corpus, I decided to use an off-the-shelf application in beta. While I try wherever possible to use open-source code and freely available software, this can involve a serious investment of time in learning new tools, and like I said: mid-semester, strike, and the seismic rumblings of what Covid-19 would mean for teaching and assessment were beginning to shake the ground underfoot. An out-of-the-box application offered a way to see whether the results would be worth the time needed to figure out how to work with the model in a programming language. I fed our BSC corpus into the application, waited a few hours, and then watched as my screen began to fill up with neural-net-generated Baby-Sitters' Club fanfiction.

>"Okay, you guys. What kind of dad does he have?"
>
>"Yes," said Claudia. "I think he's outgoing. A lot of things. I think that's cool, just because I think it's a good family and he doesn't have much in common."
>
>"What is that?" I asked.
>
>"He loves it. He loves going to his house and I just think about it, like the teachers come and help out."
>
>"Oh. I love him."
>
>I didn't hear the answer. I was excited about working out next to him.

One of the interesting things to observe in neural-net generated text is the interaction between the thematic preoccupations and stylistic tics of the two datasets on which the model has been trained (in this case, GPT-2's training data selected according to its popularity with Reddit users, and the corpus of BSC books). The AI Dungeon example which incorporates the tedious steps of software installation into its fantasy narrative is one innocuous example of this kind of genre-mashing. Janelle Shane supplies another: when she fed Harry Potter fanfiction to a neural network that had previously been trained on recipes, she found that it had trouble keeping on track: hostile exchanges between Harry and Snape would tend to devolve into conversations about recipes. Even in the wholesome family-and-friends-oriented chunk of pseudo-BSC prose above, the murky adult world of the twenty-first century internet is beginning to seep through. I pulled the handle of my text generation slot machine and tried again.

>I don't like his dad. I like him, too. I don't like what he thinks of me. Not sure what he thinks of me. Not sure what he thinks. Not sure what I think of him. Not sure what his parents want me to know. Not sure what he wants.

If you are trying to distract yourself from the apocalypse, you've got to be pretty happy with a neural net that, trained on language from the era of the internet and given BSC texts to chew on, presents you with prose that sounds like Gertrude Stein if she was a boy-crazy teenager. (And also, I call dibs on training a neural net on Stein's collected works, if [Tanya Clement](https://academic.oup.com/dsh/article-abstract/23/3/361/937498) or [Natalia Cecire](https://muse.jhu.edu/article/576393) don't beat me to it.) This scrap of Steinese was not just pleasingly absurd but also curiously redolent of what it is like to be a teenager: anxious not only about what other people think of you, but about what other people think you think of them, and what the people connected to them think that you think of other people, and so on. While I wouldn't characterize this as revealing the latent structures of teen-speak, fictionally articulated inner monologues, or indeed anything else, it's hard to shake the feeling that it's nonetheless capturing something.

I'll also say that  though I'm sceptical about the inside-baseball character of "explainable AI" as it currently stands, I'm confident that scholars of literature, narrative and language have something to add to those conversations, and that there is something to be gained from attempts to identify the textual features a neural network is picking up on, and the ways it is recombining and conjoining those features by asking people who know something about the way texts work. The literary equivalent of being able to identify the node in an image classifier that is looking out for pointy ears in pictures of cats, perhaps. Except, where identifying pointy ears as a salient feature for classifying pictures of cats is not illuminating for photography, art history or veterinary science, it remains a tantalising possibility that literary studies might learn something non-trivial about texts generated by a neural net.

One of the things that neural nets have to "learn" when producing text longer than aphorisms is the capacity to keep track of what has previously occurred. This can range from the simple -- knowing that a parenthesis, once opened, must be closed -- to the more complex. Our BSC model still had, evidently, some way to go in this direction.

>"I'll call Claudia's room," said Claudia. "Don't you?"
>
>"Yeah." Claudia said.
>
>Claudia smiled at Claudia. "I'm going to call my parents tomorrow. They'll be all right now.
>
>"But, don't worry about it," said Claudia.
>
>"Oh, it's okay," she said. "Okay. I'll call Claudia.
>
>"Let's leave!" shouted Claudia.
>
>"Don't you call Claudia?" said Claudia, as she grabbed her arm.
>
>"I'm not!" she said. "I'm tired. I don't want to talk to Claudia anymore."
>
>"Call Claudia. Come, Claud."
>
>"Come, and tell me about the meetings."
>
>Claudia was lying in bed. She was shaking her head. "My mind is on you, too. I'm glad you won't be here. You're the right one, too. You don't belong to the BSC."
>
>Claudia didn't say anything. She nodded.

While a story peopled almost entirely by Claudias— who talk to each other, grab each other's arms, and hang out in each others' bedrooms— has its charms, it shows the neural network to still be at the point of blissful ignorance about the need to differentiate characters in a conversation. Not a feature of a narrative that any class or textbook on narrative will ever bother to mention, but a convention that, once revealed through its rupture, presents itself as non-negotiable: even Joyce's, B.S. Johnson's and, yes, Stein's characters remain stable and distinguishable from others in conversational exchange. And while the extract is hall-of-mirrors ridiculous, it also feels as if it captures something of the intense sociability of the BSC texts, where there is an enormous amount of talking with, emoting at, and being in close physical proximity to, one's friends.

>"We had some great parents. Mom and Dad had kids. Mom and Dad had our own little sister Stacey, who's two. She did a lot of big things and stuff like that."
>
>"What do you think, Stacey?" asked Claudia, shaking her head.
>
>"Well, it's important to remember that we're not living in an alternate world. You know, it's hard."
>
>"But it's a place where we can see. And we still live in an alternate world, so that you can see where you're born."
>
>"That's great. Right."
>
>"Or maybe, okay?" asked Stacey.
>
>"It's hard," I added. "Just not when you need to."
>
>"Yeah."
>
"That's right," agreed Claudia.
>
>"Yeah. Just not when you need to. You don't know that what you're born is on the outside, you know."
>
>"Sure, it's not that easy. Not when you need to. But it's hard to have at least one person or someone who can come and have you with you. That's also why you have to be best friends."
>
>"Well, I think you can just do a little thing," agreed Claudia.

By this point, a little further on in its training, the neural net has advanced to the point where it understands that conversations need to occur between different people. And, while the conversational swerve from friends and family to existential anxieties and back again isn't so typical of the books, the earnest verbal affirmations of the BSC members to one another are. There's lots of agreeing with and echoing each others' phrases, even as the characters happily contradict each other about the surprisingly metafictional question of whether they are living in an alternate world. (Does the term 'alternate world' even appear in the original corpus, I wondered? Reader, I checked: it does not. My guess is that here the model was reflecting parts of its training data -- fanfiction, to which the notion of alternate worlds is central -- that most resembled the BSC novels, and used the structures and phrases it found there.)

As the training went on, so the conversations between characters began to get more abstruse:

>"Well, I know that the way I feel about myself, the way I feel about myself. There's something good about myself, you know. I'm different than everyone else. Like you."
>
>"Not that. Not anything like that. It's just not the way I feel. I don't care about how I feel about myself, or what I'm trying to do."
>
>"Or what's in your heart?" I asked Claudia.
>
>"The way you feel about myself is that I always feel better," I reminded her.
>
>"That way, I feel better. And I feel better when I look at you in a different way. You think of myself differently. And that's why I know what I am."
>
>"You know what I'm trying to do? Maybe I am just trying to be bigger, too. But I don't have that kind of world. It's just you and I are people. Like you. When we didn't have one person who was older than me. Or something. But it's your own destiny. And what I've done. We see that I have a lot of self-control. I guess I think that's why I am stronger than you. I feel better now."
>
>"How about you?" I asked.
>
>"I like you a lot, and I don't see it. But I know that in your life you're better than me. And I really believe you can't be anybody."
>
>"But you never feel worse. Maybe you're better than you really are, and what else are you trying to do, too?"
>
>"I don't care." I looked around. I wasn't sure what I was trying to do, but I guess I could tell. If I had thought of it and tried to solve it, I could have made it easier.

This extract reads as an almost parodic depiction of self-obsessed teenagers trying to articulate who they are without having the vocabulary to do so. At the same time, though, it captures something of the intensity and almost romantic dimension of those all-important teenage friendships, where talking for hours to friends (old-school style on a landline telephone, if you were a teen in the 1980s or 90s) was a crucial part of working out who you were, what your place in the world was, and how you might navigate your relationships with others. The repeated circling-back to particular topics -- as a neural net sometimes does -- also contributed to making the extract reminiscent of those long and luxuriantly angsty conversations. I wondered to what extent the neural net's generation of the pronouns I and you according to their frequency in the BSC corpus might be contributing to the success of its pastiche, and which other features of language the neural net might be attending to as its learning went on.

After it got stuck in a loop where it began to generate streams of repeated terms, I gave the neural net a new prompt with the opening from our first DSC book, [Quinn's Great Idea](https://datasittersclub.github.io/site/dsc1/), and was soon rewarded with another example of teen-Steinese (*"I'm, of course, the only person I can describe, because I've come to such a great deal of difference in the way I am"*). Obligingly, the neural net then got onto the topic of clothes and how they are used to telegraph identity in the BSC:

>Claudia looks terrific, but is definitely not as quick and athletically as Claudia does. She dresses as a brat. She looks absolutely gorgeous, and looks glamorous. She wears perfect outfits, though.
>
>Kristy is the one who's more casual. For example, Kristy dresses all the way to Stoneybrook. I guess she looked a little sketchy, but Claudia is pretty casual. I think it's been a good thing she's more professional lately. I'll admit, I'm almost almost like Kristy. But I am actually my best friend, and Claudia is sort of like Kristy. She goes for things that don't fit the stereotype of young, shy, shy people. She's a strict style person and I don't see why I wouldn't like to be an associate member. My roommate, Stacey, is an associate member of the BSC.
>
>The BSC --- I mean, although I'm a member of my club --- was pretty much a complete mess. The conference was very organized, but the BSC was terrific. I decided to go out with Kristy.
>
>It took about two days to complete the first meeting, so I told her about the problems. I was wearing my Mom's jeans. But I think it was a bust out of something Claudia has.

What was striking about this was not so much the descriptions of clothing, but rather the way those descriptions were brought together with descriptions of who characters are and who they are trying to be. Though its referential cohesion leaves a fair bit to be desired, the extract also captures the way that the books introduce the characters in terms of their roles (members of the club, associate member) while simultaneously discussing their clothes and their appearance, most obviously in chapter 2 but also throughout the books.

As the training continued, the characterization felt like it was beginning  to stabilize: the neural net was now able to keep track of three members of a conversation, while continuing to do a fair job of echoing the tone of the books:

>"Okay, what happened?" I asked.
>
>"No," Kristy answered. "Let's move on. You have to figure out a way to make up what you want to do."
>
>"Okay." I was pretty sure Stacey might have asked. It's not as if I'd like to leave Kristy alone, but I hoped she wouldn't make a big deal out of it.
>
>"Okay, it's not exactly a great idea," Kristy began.
>
>"Well, I don't know, but I'm not going to throw it out. I can find out how to make up my mind about who I want to be on the next page."
>
>"Yes," Kristy said. "A lot of people are going to like to draw, but you need to figure out how to use your imagination."

Kristy's bossiness is an aspect of her character that the BSC books like to draw attention to (the term kristy falls in the top ten most frequent collocates for bossy and bossiness within a 5 to 10-word window either side). Here, though, the text doesn't use the term but instead telegraphs it through the dialogue, while simultaneously conveying the uncertainty of the unnamed narrator. The extract also brings out the underlying tension between Kristy and the narrator, and -- another feature of teenagehood -- how one often feels as if the more articulate, more socially powerful people in one's circle are getting everything their own way, while you stand on the sidelines self-censoring and suppressing your own feelings and desires.

Neural-net-generated-Kristy, meanwhile, started getting seriously bossy:

>Kristy nodded. "Look at the rules for the group, all the members. I found the idea of good ideas. And the reason I wrote these are just the ones I love."
>
>"Right," I said. "I guess I'll keep up with you."
>
>"Right," said Kristy. "Okay, now let me have an idea for you, if you ask. First, to do homework on how you should be aware of each of the decisions you have made. Then, if you're curious about how to find new ideas, I'll pick up what I'd like to teach you."
>
>"Okay, I know," I said.
>
>"And if I have a little creativity, I'll teach you the principle of taut and change."
>
>"Right. I mean, I try to do something different and know how you should feel about it, but not for anything I'm going to do it. Right. There's nothing to be confused about."
>
>"I guess I can't understand what I'm doing," said Kristy. "I just think I'll just come up with the best idea."

The terms "Right" and "Okay" do some interesting work here. While they suggest acquiescence in Kristy's unnamed interlocutor, coming from Kristy herself they work in combination with verbs in the imperative and declarative mood to convey cheerful imperiousness, signalling not so much Kristy's agreement as her marshalling of those around her. Veering from self-assurance (*"I found the idea of good ideas"*) to self-doubt (*"I guess I can't understand what I'm doing"*) also felt very plausibly BSC. Her interlocutor, meanwhile, is trying to assert herself without much success (*"I mean, I try to do something different and know how you should feel about it, but not for anything I'm going to do it*"), but Kristy continues to steamroll her. The premise that a queen bee might make all of her friends *"do homework on how you should be aware of each of the decisions you have made"* (note: not homework on the decisions you have made, but how you should be aware of those decisions) felt to me like something out of Judy Blume or Harriet the Spy: the discursive equivalent of a kid dressing up in her corporate mother's 80s-era shoulder-padded jacket and heels and trying out phrases she's heard the grown-ups use. The *"principle of taut and change"*, for instance, though it corresponds to nothing I know in the real world, sounds like an idea that might plausibly come of the mouth of a motivational speaker: an alternate universe's version of 'lean in' that it's easy to imagine Kristy subscribing to. In these various ways, it felt as if the output had managed to capture something of Kristy's character and was conveying it through textual features which went beyond the lexical.

Of course, cherry-picking excerpts from a longer piece of auto-generated output, as I'm indulging in here, and observing that some of these excerpts are a better match than others to the ways the BSC characters are portrayed is the kind of thing that gives work in the digital humanities a bad name. (Though I'm cheered by Katherine Elkins and Jon Chun's remark that ["reading sublime GPT text can transform one into the critic who, enamored of an author, can do nothing more than cite in full."](https://culturalanalytics.org/article/17212-can-gpt-3-pass-a-writer-s-turing-test)) I wasn't setting out to make definitive statements about what this particular neural net was doing with this particular training set, though. Rather, I was trying to see what kind of mimetic functions GPT-2 was exercising when faced with the genre of young adult fiction focused on a group of entrepreneurial young women, and attempting to understand the way it was imitating the original genre through some of the categories of literary analysis. I was, for instance, surprised to find even semi-coherent characterization occurring, let alone with a degree of regularity.

As the training went on, the output began to investigate the line between friends and frenemies (with a little of its previous failure to differentiate between the participants in a dialogue):

>"A lesson you need to learn is that you've already put out an ad campaign, and I want it to be a success," Kristy reminded me. "And I know that. This is the first big campaign. It's going to be like a baby-sitting project."
>
>"That's what I said," Kristy added. "And when you did that, you did it."
>
>"Great!" Kristy giggled. "But I guess I haven't figured out how you could be successful. You are, since you and all your friends are probably just doing stupid stuff."
>
>I took a deep breath and put down my pockets and started my hand toward Kristy.
>
>"We're going to start," she said.
>
>"Okay, we'll all move on!" I went on, breaking up.

Not for the first time, I was getting flashbacks to how subtly mean teenage girls can be to each other, which added a further degree of verisimilitude to the output (uncanny valley meets valley girls?). Then, as the discussion about the advertising campaign heated up, things began to get out of hand:

>"Woooohhh!" I shrieked. "We need lots of pictures of the old addresses and who knows if this is a good idea. Maybe we should take those. I mean, if we were to do that, the flyers would be too busy and we could get you to do something like that."
>
>"Okay, but we're not going to do anything like that," I said, pointing to the flyer posters we'd put up. We kept saying "Duhh, Stacey," and giggling for a while.
>
>I didn't know about the flyers, but I thought that maybe I could hold our nose and say "huh-huh-huh-huh-hauh-hauh-hauh-hauh-hauh" and become a freckle.

Right. The neural net had eaten one too many of Claudia's beloved Ring-Dings, or else had done some transmedial genre-hopping and landed in a stoner movie. It was time to see what Quinn had turned up in her own adventures with GPT-2.

## Six months later

### Quinn
The DSC meeting where Anouk brought her GPT-2 findings, and I laughed until my stomach hurt, was one of my very last meetings in the before-times, just days before the elementary school and preschool shut down, and time began to go slowly, then quickly, then morphed into something altogether confusing and surprising. Especially here in the Bay Area, where we rely on festivals and events to mark the year in the absence of notable seasons. Or, at least, we used to. Maybe someday we will again.

It was fall, and universities in the US were making last-minute decisions to go all-online with no students on campus (like my institution, Stanford, or the institution in the city where I live, Berkeley, following a COVID-19 outbreak stemming from a frat party), or they were bringing students back -- and quickly rethinking those plans as cases exploded. My oldest kid was doing first grade online for the indefinite future, and I didn't expect the preschool to get through the year without a closure. The election was on the horizon, everyone was bored with social distancing and masks, and there was no end in sight to the ever-increasing COVID-19 death toll and the ongoing dismantling of civil society and the infrastructure that helps keep it afloat. Reading through Anouk's description of February in Edinburgh from the perspective of late August 2020 in the United States, what I'd have given for icy fingers and a picket line.

It had been a very long time since I laughed the way I did when Anouk first shared her GPT-2 results. I needed a good laugh, but I also wanted to try to do it myself. So I dropped Jeff Tharsen a note.

Jeff Tharsen is like a cross between a Viking and a Confucian scholar. He's tall, with dark eyes and a long beard that once was blond and is now turning an off-white color like Mary Anne's blouses. He's the University of Chicago's resident expert in humanities-based research computing but spends much of his time thinking about sound systems in premodern rhetoric and poetry, social justice and savage inequities, playing guitar like Rico from the *California Diaries* series, Minecraft mods, and finding infinite combos for his *Magic: the Gathering* deck builds. He'd blown me away recently with the "Shakespeare sonnets" and "Blake poems" he'd coaxed GPT-2 into generating, and while I'm getting better at sorting out code myself, I was happy to have [some code and instructions to start from](https://github.com/rcc-uchicago/BERT-GPT2_tutorial_Summer2020) that I hoped might work.

Trying to plan ahead for releasing this DSC book as a Jupyter notebook, I put together a notebook that ran the external Python code from his repo. Next, I saw his tutorial recommended running the code not just on a computational resource larger than your laptop -- but, specifically, on Graphical Processing Unit (GPU) nodes as part of his university's high-performance computing cluster. I was impatient. I didn't want to try to figure out how to access the GPUs available on Sherlock, Stanford's high-performance computing cluster. My laptop, I figured, might be a little slower but I figured it'd work *fine*. I was so wrong.

But let's take a step back first.

#### What is machine learning anyway?

As Jeff reminded me when I kept venting my impatience at him because my model didn't seem to be learning anything at all, machine learning isn't a child you can coax into putting their shoes on faster because *we really have to go or else we'll miss our 5-minute social distancing drop-off window at the preschool and cause a backup for other families*.

It's math. It's just math.

If you're going to understand machine learning, it's time to summon your inner Stacey the Math Whiz, join the Machine Learning Mathletes, and dive on in.

Machine learning involves algorithms that are trying to predict an output, given an input, a lot of examples of input/output pairs, and some parameters you can fiddle with to improve the algorithm's guesses.

What if we tried to come up with an algorithm to predict Claudia's grade on a test? We could start with something simple, like assuming that her grade on a given test is going to be the same as her current grade in that class. If it's a test in art class, Claudia will get an A. If it's in English class, she'll get a C. One input (the class), one calculation based on that input (look up her current grade), one output (the grade). But everyone knows that grades don't work like that at all. There are so many more factors to take into consideration. How hard have Claudia's parents been on her about her grades lately? When did the test take place -- was it before Mimi's death, so Mimi could help Claudia study? How many baby-sitting jobs did Claudia have that week? Did she have art class the day before? Is there an art exhibition coming up? In a machine learning context, these questions are referred to as "features".

Knowing the answer to all those questions is one step towards improving our grade-prediction algorithm. But there's still another set of information that we're missing: how much does each of those things *matter* to the overall output? Maybe an upcoming art exhibition means that she'll be a little more distracted than usual when trying to study, but the effect overall might be negligible. On the other hand, if Claudia's parents are really cracking down on her, threatening to prevent her from participating in the Baby-Sitters Club until her grades improve, that's likely to have a *much bigger* impact on the test outcome. The impact of a given feature is called its "weight" in machine learning.

"Deep learning" refers to a kind of machine learning where features are organized into layers. Lower layers capture basic features, and higher layers capture more subtle things. This is a little easier to understand with an example for deep learning for computer vision: a low-level feature might enable an algorithm to recognize that something in an image is a line. A higher-level feature might be able to recognize that something is a giant dangly earring like Claudia might wear. In the image below, the layer on the left identifies recurrent patterns in the way black, white and grey pixels come together to form particular shapes like lines and curves. The layer in the middle spots patterns in the way those shapes typically fit together (what a human being can recognize as facial features like eyes and noses). Then the layer on the right finds patterns in the way those eyes and noses are put together with other things mouths, foreheads and ears to make faces.

Training a machine learning algorithm is like making the algorithm play a big guessing game. Your training data has all the "right" answers. The algorithm takes part of the training data, hides some of it from itself, and attempts to guess the right answer by changing the weights it assigns its features. Then it checks its work, and typically will report back to you about how it's doing, using something called "loss". High loss values (and what counts as "high" depends a lot on the context) mean that the algorithm made some bad decisions during that round, leading to a bunch of mistakes. Remember, it's a guessing game: sometimes an algorithm can get off on a wrong track for a turn or two, but it should be able to correct itself and keep improving by passing the right answers back through the network, updating weights along the way.

If your loss rate just keeps bouncing around the same numbers you started with for turn after turn, something has gone wrong. (And something **had** gone wrong when I tried it with Jeff's code -- more on that later.) But it's also a problem if your loss value goes all the way to 0. You might think that a 0 loss value is great -- perfect A+ right answer every time! But remember: you're not trying to train a model that will spit your training data back at you with perfect accuracy. What you want is a model that can handle, with reasonable accuracy, data that it **hasn't** seen before. When a model gets too good at predicting your training data, so good that it hurts its ability to handle new data, that's called "overfitting".

But back to Claudia's grades! And here's where things get a little spooky. The way I've described things so far suggests that you, the knowledgeable human who understands how the world works in general, and how Claudia's life works in particular, define the features that the algorithm uses. Maybe you can trust the algorithm to handle the weights, but you can't trust the ghost in your laptop to make the call on what features to use, can you?

Actually... yes? It turns out that in most cases, you're better off leaving the whole thing to the algorithm. You can see how this can feel irksome, particularly if you're like Kristy and want to be in control. How can you trust the ghost in the laptop to pick the right things if it's not an expert? The fact that you're not in there bossing the algorithm around contributes to the rhetoric around machine learning as a "black box". But here's the thing: hopefully you've already wrapped your head around the idea that computers just do things differently than humans. (If not, check out [DSC #8: Text-Comparison-Algorithm-Crazy-Quinn](https://datasittersclub.github.io/site/dsc8/).) With text comparison algorithms, it's harder to adjudicate how "right" the computer's determinations are compared to the decisions we'd make as humans. We just have to grapple with them as another perspective, take what insight we can, and sometimes agree to disagree. But machine learning is a little different because there often is, actually, a "right" answer. Without getting too worked up about how the algorithm comes up with its answer, we can evaluate how often it gets the answer right.

Which is not to say that we should pay no mind to how the ghost in the laptop makes decisions. Machine learning algorithms (often under the fancier title of "artificial intelligence" or AI) are getting adopted as an automated decision-making tool in [all kinds of contexts](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G), including ones with serious consequences, like courts attempting to determine [which defendants are "high risk" for committing future crimes](https://www.theguardian.com/inequality/2017/aug/08/rise-of-the-racist-robots-how-ai-is-learning-all-our-worst-impulses). Algorithms like to find [shortcuts to get to the answer](https://www.theguardian.com/technology/2015/jul/01/google-sorry-racist-auto-tag-photo-app), or [close enough](https://www.technologyreview.com/2021/01/29/1017065/ai-image-generation-is-racist-sexist/). Even if you've tried to set things up so that you don't tell the algorithm about race (in order to ensure that it's not making determinations based on race) you may discover that one of the features it picks up and uses is essentially a proxy for race. It's not for nothing that OpenAI chose not to release their full GPT-2 model, like Anouk mentioned, to avoid people using it for nefarious purposes. (That said, OpenAI reached [a deal with Microsoft](https://blogs.microsoft.com/blog/2020/09/22/microsoft-teams-up-with-openai-to-exclusively-license-gpt-3-language-model/) to give them exclusive access to the full GPT-3 model, allowing them to embed, adapt, and use the model however they please. And depending on how they vet **their** clients... 😬)

There are no lives at stake when we're using machine learning with literature. But you may still want to understand how the algorithm is making its determinations, especially when it's performing well. Is there anything we can learn about literature from the way an algorithm is able to classify it, or generate text that readers perceive as "similar" (like Anouk was trying to do in February)? Some algorithms (like k-means clustering) can easily give you the features that they're using; with others, particularly deep learning algorithms with a lot of layers, it's harder to determine. The features the algorithm is using may not be all that interesting, or might reflect things about your corpus that aren't actually what you're trying to get at (e.g. if you're looking for what characteristics differentiate books written by British vs. American authors, the presence of the word "whilst" is probably not what you want).

#### Fine-tuning GPT-2
Jeff's notebooks for fine-tuning GPT-2 were supposed to be run on a GPU (a Graphics Processing Unit -- I'll say more about those in a minute). But ever since I was a child reading the *Baby-Sitters Club* novels, I've tended to skip inconvenient instructions, cross my fingers, and hope for the best. Which is how I ended up running his notebook on my MacBook Pro (which does not have a GPU) for 24+ hours, without the model getting more BSC-like at all. It wasn't even just a problem of me using the wrong hardware for the job, I also had made a mistake with how I set up the fine-tuning code, which turned into an opportunity to learn about "learning rates."

##### Learning rates

Part of why the model wasn't learning anything was that I'd set the `learning_rate` hyperparameter too high. (In machine learning, a "hyperparameter" is just a setting that you, the squishy human, adjust; "parameters" are estimated from data automatically by the machine. You adjust hyperparameters by specifying their value when you run a task like fine-tuning a model.)

Sorting out `learning_rate` is kind of like the process of learning to drive a car -- or the difference between a driving video game (like my kids' favorite Mario Kart 8) and driving an actual car. When you're feeding in a large-ish data set for fine-tuning GPT-2, a "learning_rate" that is too high leads to a lot of overcompensating when fiddling with the different metaphorical steering wheels of machine learning to try to get the right answer. Not getting the right answer? **EEEEEEEEK! Turn it all the way to the right! Oh, wait, that didn't get you the right answer? OMG NO! Turn it all the way back to the left!** This wild vacillating left and right might barely keep you on Rainbow Road in *Mario Kart 8* (with machine learning, this looks like reliably getting the right answer, referred to as "convergence"), but it takes a lot longer and is more stressful than if you're driving the car of machine learning with some seasoned expertise. In a lot of cases, a small change in the orientation of the steering wheel can be all you need to stay on the road. But you don't want to be too hesitant, either! Because that also means it'll take longer to achieve convergence. And especially if you're paying for your GPUs (or waiting in line for relatively scarce GPU resources in an institutional High-Performance Computing cluster), you don't want that.

So I'd spent 24 hours careening back and forth between "NOT ENOUGH!!" and "TOO MUCH!!", but the `learning_rate` hyperparameter isn't something that can adjust itself on the fly based on the context, the way you'd actually drive a car. You have to specify it upfront. And I should have chosen a smaller one. (I didn't feel too bad, though. Adjusting learning rates is a huge and unsolved problem in machine learning and usually people just guess.)

The bigger problem was that, no seriously, you really do need GPUs to fine-tune GPT-2 at all effectively.

##### What's a GPU and why should you care?

GPU stands for Graphics Processing Unit. You can think of it as a cousin of the CPU (or Central Processing Unit), which you might be familiar with from your own computer, if you’ve ever looked at the Windows Task Manager or Mac Activity Monitor to figure out what runaway process is sucking down your battery and making your fan whir with its high CPU usage. (Looking at you, Adobe Creative Cloud!) Gaming laptops need good graphics performance in order to constantly render, update, and rotate the millions of polygons that make up modern game graphics, so they’re more likely to have GPUs to make that work. If you’re trying to render 3D models at tolerable speeds, you should also work on a machine with GPUs. But why do GPUs matter for GPT-2? We’re not using machine learning to try to cluster BSC book covers or anything! (Though actually… well, don’t be surprised if you see that in a future DSC book.)

So many things in the world of machine learning assume you share a particular set of cultural references used to explain things. CPUs vs GPUs commonly get explained through some variant of “Ferrari vs. cargo truck”. Neither of those vehicle specifications mean a whole lot to me. Let’s try it another way.

Stacey and Kristy are both contestants in a department store contest where they have ten minutes to bring all the clothing items they can up to the cash register, and they can keep everything as long as they correctly sum up the cost.

Stacey is like a CPU. She’s really good at math, but is also very concerned about always looking cool -- what if she bumped into a cute guy while her arms were piled high with clothes? That wouldn’t do. So she’ll speed-walk around the store, picking out a diverse set of expensive and stylish outfits, never holding more than a couple items at a time, and calculating the cost in her head.

Kristy, our GPU, is only average at math. She doesn’t care what impression she makes: she’s borrowing her brother Sam’s giant hiking backpack and is going to stuff it to the top. Kristy isn’t into fashion, so instead of putting a lot of thought into how different items of clothing might assemble into trendy outfits, she’s just going to fill the hiking backpack with multiple of the same jeans, t-shirts, turtlenecks, sweatshirts, underwear, and socks. She’s also bribing some of the elementary school kids on her Kristy’s Krushers baseball team to help her with this mall contest. Her plan is to stuff the backpack, bring it over to her team waiting by the cash register, and each kid will work on adding up the cost of a few items.

How does this work out? Stacey the CPU ends up darting back and forth around the department store, doing multiple different kinds of complex calculations (all the math to add up the price of all her items, plus the evaluation of how fashionable and combinable her choices are). This is why CPUs are probably what you use most of the time: you want something fast, nimble, and able to handle lots of different things.

For a while, it looks like Kristy the GPU has fallen far behind. Stacey the CPU already has lots of articles of clothing piled up at the cash register while Kristy is still filling the camping backpack. But in the three minutes remaining by the time Kristy makes it to the cash register with her backpack, she is able to divvy up the calculations among her team and still finish in time with the correct answer. Her team isn’t as mathematically capable as Stacey -- they are, after all, just elementary school kids -- but giving them each a simple task to work on (just adding up the cost for a few items), Kristy parallelizes that part of the process and it finishes quickly.

For this small task -- gathering clothes for 10 minutes and adding up the total cost -- maybe Stacey the CPU and Kristy the GPU finish at the same time, especially since Stacey the CPU was using some more complex calculations that might slow her down. Kristy the GPU spent most of the time loading up the camping backpack, and the actual calculation was fairly brief. But if the task were a lot bigger -- if there were many more small calculations that could be parallelized across all 9+ Kristy’s Krushers team members -- Kristy the GPU could easily leave Stacey the CPU in the dust.

And that’s what happened when I tried to try to fine-tune GPT-2 on the Baby-Sitters Club corpus using my laptop. Poor Stacey the CPU was running all over, trying to do the calculation to update the weights for all the features of GPT-2… while also running like 50 browser tabs… and probably more than a couple Adobe apps… plus my email, and probably like 12 other things. She wasn’t getting anywhere fast with this fine-tuning thing.


#### There's more to text generation than GPT-2

Around the time I was struggling with ways to fine-tune GPT-2 using the Baby-Sitters Club corpus, fall quarter had begun at Stanford, and I started teaching my biennial non-English DH course. (Online, asynchronously, and hastily reworked week-by-week, if I'm honest about it.) I was amazed at how many students I had: 16 registered, and another five or so auditors. (Side note: if you're teaching DH and have students who don't normally work with English, check out the [Multilingual DH](http://multilingualdh.org/en/) site or get in touch! I'd love to help you give them what they need to be able to apply what you're teaching to their language.)

When I learned more about of one of my students from the Classics department, I was thrown into self-doubt. Annie Lamar has warm gray eyes and an affinity for purple clothing. She has long hair that is almost always twisted and copiously pinned on the top of her head. She studies ancient languages and artificial intelligence, which-- although it sounds quite serious-- often results in the creation of chat bots so she can talk to her favorite ancient authors. Annie had a BA in Classics and a BS in Comp Sci from the University of Puget Sound (not far from where I grew up in the Seattle suburbs). Even before starting grad school in Classics at Stanford, she had done work on [creating network graphs of texts](http://mathcs.pugetsound.edu/projects/augustine/), [machine translation for a low-resource language](https://ieeexplore.ieee.org/document/9244794) while focusing on style, and [generating metrically accurate Homeric poetry](https://ieeexplore.ieee.org/document/8940426). Was there anything I could actually offer her with this class, as someone who was struggling to just get GPT-2 fine-tuned, myself?

By the end of the quarter, it turned out okay -- I learned that computer science departments have their own constraints about what it's acceptable to work on, and DH-as-such acculturation has some value. Annie's final check-in assignment, in response to the prompt "What is digital humanities?", was perfect: "In the words of Democritus, 'Αρχάς είναι των όλων ατόμους και κενόν, τα δ' άλλα πάντα νενομίσθαι.' The beginning of everything is atoms and emptiness, the rest is all perception." But towards the beginning of the quarter, when I wondered if I could teach anything close to what I might learn from Annie, I asked if she'd be up for talking with me and Anouk about machine learning and text generation.

### Anouk

From our Zoom boxes, Quinn and I talked Annie through where we'd gotten up to so far with our neural net attempts.

"... so, we're trying to understand what goes on under the hood when one takes a neural net like GPT-2 and retrains it on BSC text," finished Quinn.

"Yeah, we'd really like to crack open the black box to understand how it's working inside," I added. "You know how it's possible to find the individual node in a neural net that keeps track of the pointy ears in pictures of cats?" I asked.

Annie nodded.

"Well, could we do something like that? Find the nodes that have a kind of similarly identifiable function for texts. Only instead of telling us something that isn't interesting such as  the fact that cats have pointy ears, it might be able to tell us something we don't know about texts, like, um --". I was incoherent, weary after a week of dealing with failing institutional virtual learning environments and anxious students, and there was a lag in my connection with the others 5000 miles away. I was clearly not making much sense.

"-- like, what are the pointy ears of literary texts?" Quinn helpfully jumped in with.

"Hmm," Annie considered this. "You know in the movie Arrival there's an alien language? That alien language definitely means something to the aliens: it's just that no one else can know what it means. It's kind of the same with what's inside the black box of a neural net: it's just a bunch of ones and zeros in a multidimensional matrix that we have no chance of understanding. So what we have to do is to develop ways to evaluate it, for instance by using vocabulary graphing, which lets us see how well the vocabulary of a generated text matches up with the training data."

"Evaluation!" I thought. Maybe that would be where some background in literary studies might come in handy ...

Quinn, meanwhile, was trying out another conceptual metaphor. "What does it mean to take the strange sausage of GPT-2 and make it BSC-flavored?" she asked.

"Ew!" replied Annie. "I read the BSC books over and over when I was a kid but I don't ever remember coming across Claudia and the Strange Sausage." We giggled. "Anyway, here's one way to think of it. You take a deep recurrent neural network and you start training it. You train and you train, and it's all going well, and then you get to the point where you've overfitted and that means you've gone too far, as the model starts spitting out actual lines from real BSC books. So, you need to 'freeze' the training before that point to get it to the right level.'

"That's really helpful," Quinn mused, and I nodded. Neither of us had thought of neural net training like that before.

"So, what would be the difference between retraining something like GPT-2 on the BSC corpus, and training a neural net on the BSC corpus alone?" Quinn wanted to know.

"Yes!" I interrupted. "I thought neural nets needed seriously large corpora, and ours is pretty small as ML-training datasets go. Can you even use a neural net on something that size?"

"Funny you should ask," smiled Annie. "Small data is my thing. I work on Ancient Greek corpora that are typically about 2% of the optimal size for training neural nets. In general, a "good" neural network requires about 1,000,000 lines of training data. My datasets are usually composed of 20,000 lines or less.. So I'm interested in seeing how well neural nets do with data of that size, and I've used[  OpenNMT-py](https://opennmt.net/OpenNMT-py/) to train models of that sort."

I thought of the wealth of knowledge about the BSC among the members of the DSC. "Would it be possible to evaluate the outputs of different models -- some trained on GPT-2 and retrained on the BSC corpus, and some trained on the BSC corpus alone -- using the expertise of the members of the DSC?" Evaluation is important in CS but I wasn't sure if the judgments of people with literary training ... well, counted as proper evaluation.

"Completely!" was Annie's reassuring reply. It turns out that she has actually[  published on this very question](https://ieeexplore.ieee.org/document/8940426). "We give the model dialogue and ask it to fill in a section that you have removed -- the beginning, the middle or the end, say. Then we ask humans who are familiar with those texts to evaluate if they think there is any fake text, and if so where comes."

Quinn and I exchanged glances, or we would have had we not been on Zoom where looking someone in the eye involves looking away from their face to your webcam. This would be a way to involve the rest of the Data-Sitters, perhaps in a future book: use different models to generate a number of plausible chunks of BSC-esque prose and ask our fellow club members to evaluate which sounded the most real. Perhaps my dream about literary domain expertise actually coming in handy wasn’t such a ridiculous idea after all.

## Six months after that

### Quinn

It's been a year since we started writing this book. Or maybe on some level, we're still frozen in March. Maybe today is just March 337th in [Covid Standard Time](https://covidstandardtime.com/). I need a break. There is no way to take a break, at least, not while conscious. We're reaching the point where language for talking about this is breaking down. "Burned-out" was a while ago. The metaphor crumbles in the pandemic: when a candle burns out, it stops burning. But the sun keeps rising, the days keep happening, and we continue staggering along.

In short, laughter is harder to come by, and we need it more than ever. (I mean, actually what we need *is a break* -- I've had vivid fantasies of checking into a cheap motel and just spending 24 hours without anyone asking me to make them a sandwich. But that's not happening. So I'll take laughter.)

For the longest time, the Data-Sitters Club has been my escape from *everything*, but the weight of that *everything*, compounded by the everything coming from the rest of the world (Election! Election results! Holidays-Such-As-They-Were! 16-Day weekend for the kids! Attempted coup! State-wide stay-at-home order with minimal local ICU capacity! Another impeachment! Inauguration! California stay-at-home order lifted even though everything is still awful and there's nowhere near enough vaccines in the state for health workers and 75+! Giant storms and power outages! GameStop stock breaks the stock market! Waiting to find out what weird and probably awful thing will happen next!) turned this book into something akin to the apple cores my oldest kid has a penchant for stashing underneath the living room bean bags. I know it's there, but I'm afraid of what I'll find, so I don't look -- and weeks pass, turning procrastination into dread.

But during another nondifferentiable weekend at home, I finally sat down and reread this book. And I was surprised at how much I enjoyed it. An idea began to form in my head. Maybe I could at least give this book an ending, even as it's gotten hard to imagine we'll actually manage to escape this state of suspended animation for our own lives.

#### The return of text-comparison-algorithm-crazy Quinn

I loved Annie's idea of generating some Dawn-approved, organic *Baby-Sitters Club* plant-based meat substitute, made exclusively of text from the books, without the potentially unsavory admixture of GPT-2's unspecified source websites based on Reddit links. And I was really curious if it could trip up our expert evaluators (AKA my fellow Data-Sitters with encyclopedic knowledge of the series). But this book was already long enough, so it'd be another task for another book.

What I found myself wondering was whether the **computer** would be able to tell that something was amiss with the text that GPT-2 generated. And furthermore, whether the computer would judge the samples from early on in the training process to be less similar than the later ones.

I'd eventually found a notebook that allowed me to fine-tune GPT-2 using Google's GPU's for free. [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb) has some limitations (like timing out after a few hours), but if you've used [Jupyter notebooks](https://programminghistorian.org/en/lessons/jupyter-notebooks) before, it's a familiar environment, has easy integration with Google Drive, and has a free supply of shopping-contest Kristys with enormous backpacks (GPUs) who can get your job done in no time.

The notebook I modified for the occasion was created by [Max Woolf](https://minimaxir.com/). This notebook makes it easy to load in a text file from Google Drive with the training data, fine-tune GPT-2, and save the resulting model as well as samples from various stages in the training process.

The configuration I used saved sample output from GPT-2 every 10 rounds as it was being retrained using the *Baby-Sitters Club* corpus, and the model trained for 1000 rounds. Because things are a little different every time you train a model like this, I ran it five times, so we'd have 5 sets of samples from different training attempts. 495 samples is a lot of text to wrangle, so I pared it down to 50: one every 100 rounds.

I trained the model using just text from chapter 2's, rather than whole books. The chapter 2's have a core of predictability that I thought might be easy to get the machine to pick up on, but in addition to the reliable "describe all the characters and the club" prose, there's usually some plot-based stuff to give the computer something more than tropes. (Want to hear more about chapter 2's and some other things we've done with them? Check out [DSC #8: Text-Comparison-Algorithm-Crazy Quinn](http://datasittersclub.github.io/site/dsc8).)

One of the frustrating things is that you can't get GPT-2 to generate a chapter 2's length (any chapter 2's length, not even the short ones) of continuous text. 1,024 tokens (mostly words, but also counting punctuation) is a hard limit. This has always struck me as an arbitrary annoyance, and I was grateful when Annie dug into it and explained it to me:

>Transformer models are great because they are efficient and the training time is much less than that of a typical RNN. However, transformer models sacrifice information about sentence-level word-positioning in order to run every word in a sentence through the network in parallel. This means that in a naked transformer, there is no information about syntax. One way to solve that problem is to associate every word in the sentence with a number indicating its position; this number essentially becomes another feature associated with the word in the word embedding- hence, 'fixed positional embeddings.' 
>
>This also means that the longer the text you ask the model to generate, the less confident the model will be- if the positional embeddings only ever reached, say, 1000, then when you ask the model to generate a word at position 5,000, it has very little information to go on. Transformer models in general do much better when asked to generate shorter pieces of human-like text (e.g. chatbots). Here, it works extremely well for generating human/BSC-like conversation, but you are limited in length.

So there you have it. 1,024 tokens might be enough to get you a chapter 15's worth of text, but chapter 2's tend to be on the long side:

![Book and chapter 2 length](https://datasittersclub.github.io/site/_images/dsc8_length_measurements.png)

Using word **frequencies** rather than word **counts** is important in order to accommodate differences in length, but I didn’t think that was enough. Some of these chapter 2’s are *significantly longer* than 1,024 tokens (the word count viz above counts words, not tokens, so all the punctuation would increase the GPT-2 relevant length even more) -- and more total words means that even subjectively prominent words in the chapter will have a lower frequency. What I wanted was 50 random GPT-2 sized chunks of real chapter 2’s.

My first thought was to tokenize the text file (separate out words and punctuation) with all the chapter 2’s that I’d used to fine-tune GPT-2, and then grab some chunks of the right length. But then I realized that approach would probably leave me with some weird chimeras featuring the end of one chapter 2, and the beginning of the next one: there was no way to tell where one stopped and the next began.

Instead, I took the individual chapter 2 text files from my laptop, tokenized those, and fed them all into a Python dictionary that also included the source file (so we know where the sample comes from) and the total number of tokens (which I needed in order to know where to start my possible random chunks). The tokenizer returns the tokens in a list… and that list is inside a dictionary… and I’ve got another list containing all the dictionaries, so we’re creating a kind of Russian nesting doll of data.


#OS is for changing directories and listing files in those directories
import os
#NLTK tokenize is for tokenizing the text
from nltk.tokenize import word_tokenize
#Random is for generating random numbers
import random

#Here's the folder with all my chapter 2 files
ch2directory = '/Users/qad/Documents/dsc_chapters/ch2'
#Change to that directory
os.chdir(ch2directory)

#Create a list for the results
ch2examples = []
#For the files in the directory with all my ch. 2 files...
for file in os.listdir(ch2directory):
    #If the file is a .txt file
    if file.endswith('.txt'):
        #Open that file
        with open (file, 'r') as f:
            #Read the file
            ch2text = f.read()
            #Tokenize the file
            ch2tokenized = word_tokenize(ch2text)
            #Count the length of the tokenized file
            ch2length = len(ch2tokenized)
            #Create a dictionary with the filename, tokenized length, & text
            ch2data = {'book': file, 'length': ch2length, 'text': ch2tokenized}
            #Add that data to the list
            ch2examples.append(ch2data)
            #Write out the filename and the length
            print(ch2data['book'] + ' - ' + str(ch2data['length']))

The next piece I worked through step-by-step, with plenty of Googling to make sure I was getting the syntax right. First, I looked up how to get a random integer in a particular range. I needed it to be between 0 (Python starts counting with 0) and the length of the list of chapter 2’s.

I knew that putting the positional number of a list item in brackets after the name of the list (like `ch2examples[42]` would give you that particular item, but I wasn’t sure how to get the value of a specific dictionary key (like `length`), so I looked that up. I knew how to do basic arithmetic in Python, so I subtract 1,024 from the chapter length to get the largest number that could be the starting point for our sample, to make sure the result was 1,024 tokens. Once I got another random integer for the start point, I needed to figure out how to join a range of items in a list, so I Googled that too. Then I tried a couple different conventions for naming the output files, and settled on `samplename = 'sample_'+str(start)+'_'+ch2name` so we could see (and sort) by the book it came from, and also have a (hopefully) unique ID with the start index, in case there end up being multiple samples from the same book.

#Random number between 0 and the length of the list of chapter 2's
number = random.randint(0, len(ch2examples))
#ch2examples[number]['book']
#Define ch2name as the book name corresponding to the random number selected
ch2name = ch2examples[number]['book']
#Define maxstart as the length of the chosen chapter 2, minus 1024
maxstart = ch2examples[number]['length'] - 1024
#Define start as a random number between 0 and the maxstart
start = random.randint(0, maxstart)
#Define end as start + 1024
end = start + 1024
#Define sample as all the text between the start and end defined above
sample = ' '.join(ch2examples[number]['text'][start : end])
#Defines the filename for the output random selection
samplename = 'sample_'+ch2name.replace('.txt','_')+str(start)+'.txt'

Once I got all that working, I looked up the syntax for doing a loop a specific number of times, and ran the code cell. 50 GPT-2-sized samples suddenly appeared on my laptop. And you know what? That felt really good. 

#Iterates 50 times
for i in range(50):
    #All the below is the same as above, just iterated 50 times
    number = random.randint(0, len(ch2examples))
    ch2examples[number]['book']
    ch2name = ch2examples[number]['book']
    maxstart = ch2examples[number]['length'] - 1024
    start = random.randint(0, maxstart)
    end = start + 1024
    sample = ' '.join(ch2examples[number]['text'][start : end])
    samplename = 'sample_'+ch2name.replace('.txt','_')+str(start)+'.txt'
    #Creates and opens an ouptput file with the filename for the output random selection
    with open(samplename, 'w') as samplefile:
        #Writes the random selection to the filename
        samplefile.write(sample)

##### From child wrangling to data wrangling
There was more data wrangling to do before I could pull out my code from [DSC #8: Text-Comparison-Algorithm-Crazy Quinn](https://datasittersclub.github.io/site/dsc8.html). (Of course there was more data wrangling. This is DH. Is there ever NOT more data wrangling before we can get to the fun part?)

I downloaded the GPT-2 samples from Google Colab for each run in a zip file, and they didn’t have a file extension. So I wrote a little Python to add `.txt` plus a prefix indicating which run it was from.

#Define directory for a single run's samples from the Google Colab notebook
runfiles = '/Users/qad/Downloads/ch2samples_run5'
#Change to that directory
os.chdir(runfiles)
#For each file in that directory...
for file in os.listdir(runfiles):
    #Prefix it with the run number, and suffix with the file extension
    os.rename(file, 'run5_' + file + '.txt')

Then I put all the GPT-2 samples together in the same folder and did a little more cleanup. I tokenized the text so that punctuation would be separated from words just like in our GPT-2-length samples, and when I joined all the tokens together, I excluded the first five tokens (remember, Python starts counting with 0) which were always `======== SAMPLE 1 ========`.

#Define directory with all the GPT-2 samples
gpt2files = '/Users/qad/Documents/dsc_ch2_gpt2'
#Change to that directory
os.chdir(gpt2files)
#For each file in that directory
for file in os.listdir(gpt2files):
    #If it's a text file
    if file.endswith('.txt'):
        #Open the file
        with open(file, 'r') as gpt2file:
            #Read the file
            gpt2text = gpt2file.read()
            #Tokenize the file
            gpt2tokenized = word_tokenize(gpt2text)
            #Combine all the tokens except for the first 5 (start counting with 0, so 5=4)
            gpt2clean = ' '.join(gpt2tokenized[4:len(gpt2tokenized)])
            #Define output name by adding -c before .txt
            gpt2outname = file.replace('.txt', '-c.txt')
            #Open the output file name
            with open(gpt2outname, 'w') as gpt2out:
                #Write out the text to the output file name
                gpt2out.write(gpt2clean)

With that, I now had 50 GPT-2 samples from different training phases, and 50 GPT-2-sized samples from real chapter 2’s. Time to dig up my code from [DSC #8: Text-Comparison-Algorithm-Crazy Quinn](https://datasittersclub.github.io/site/dsc8.html) and rerun it on this new little corpus!

I decided to go with cosine similarity of term frequencies. I held my breath, crossed my fingers, and...

![Failed text comparison](_static/images/dsc9_textcomparisonfail.jpg)
<span style="font-size:400%;">🤬🤬🤬</span>

There should be exactly one black line running along the diagonal, where each text is being compared to itself. But instead, there are six additional smaller black lines, where some of the GPT-2 samples are being compared with one another. Somehow, only “run 1” and “run 2” were distinct: runs 3-5 were just copies of 2. Which is either an astronomically unlikely occurrence that GPT-2 managed to generate an identical set of samples on multiple different training runs and I should immediately run out to buy a lottery ticket and capitalize on this good luck… or failing to totally reset the notebook between runs meant it invisibly hung onto some variables, even though it looked like it was doing a new training run. (This happens sometimes with Jupyter notebooks, and that lack of transparency is one of the criticisms of notebooks.)

Since I needed to redo the runs and re-gather my files anyway, I realized I should make another change: the files get sorted alphabetically, and I want the sample numbers (not the run numbers) to cluster together, so they’re grouped by how far along they are in training. Time to revise the naming convention to something like `samples-11_run1.txt`.

#Define directory for a single run's samples from the Google Colab notebook
runfiles = '/Users/qad/Downloads/ch2samples_run5'
#Change to that directory
os.chdir(runfiles)
#For each file in that directory...
for file in os.listdir(runfiles):
    #This time put the run number after the original name, and suffix with the file extension
    os.rename(file, file + '_run5.txt')

And then re-run the comparison code.

#Imports the count vectorizer from Scikit-learn along with 
from sklearn.feature_extraction.text import CountVectorizer
#Glob is used for finding path names
import glob
#We need these to format the data correctly
from scipy.spatial.distance import pdist, squareform
#In case you're starting to run the code just at this point, we'll need os again
import os
import numpy as np
#In case you're starting to run the code just at this point, we'll need pandas again
import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)
#Import matplotlib
import matplotlib.pyplot as plt
#Import seaborn
import seaborn as sns

#Defines the directory with both original chapter 2 samples and GPT-2 samples
filedir = '/Users/qad/Documents/dsc9_gpt2comparison'
#Change to that directory
os.chdir(filedir)

from sklearn.feature_extraction.text import TfidfVectorizer

# Use the glob library to create a list of file names, sorted alphabetically
# Alphabetical sorting will get us the books in numerical order
filenames = sorted(glob.glob("*.txt"))
# Parse those filenames to create a list of file keys (ID numbers)
# You'll use these later on.
filekeys = [f.split('/')[-1].split('.')[0] for f in filenames]

# Create a CountVectorizer instance with the parameters you need
freqvectorizer = TfidfVectorizer(input="filename", stop_words=None, use_idf=False, norm='l1', max_features=1000)
# Run the vectorizer on your list of filenames to create your wordcounts
# Use the toarray() function so that SciPy will accept the results
wordfreqs = freqvectorizer.fit_transform(filenames).toarray()

cosine_distances_freq = pd.DataFrame(squareform(pdist(wordfreqs, metric='cosine')), index=filekeys, columns=filekeys)
cosine_distances_freq

#Defines the size of the image
plt.figure(figsize=(100, 100))
#Increases the label size so it's more legible
sns.set(font_scale=3)
#Generates the visualization using the data in the dataframe
ax = sns.heatmap(cosine_distances_freq)
#Displays the image
plt.show()

Well, then.

If I had assigned random filenames, so that not all the GPT-2 and original excerpts had clustered together, it would have been especially difficult to pick out which rows and columns were which. Sure, there are clearly runs that went off in a bit of an oddball direction (the light-colored rows), but it’s not like the real chapter 2’s are perfectly uniform, either. (Compare, for instance, *"Kristy and the Middle School Vandal"* and *"Kristy and the Cat Burglar"*, which are noticeably lighter than the other real chapter 2 columns/rows, on the far right of the horizontal axis.)

The excerpt from “Kristy and the Cat Burglar” is straight-up BSC mystery prose, e.g.:

>“I usually check the place out three times a day. But just as I was starting my rounds here today I had an emergency call about my wife being taken to the hospital. So I took off . Oh, man, I don't believe this!”
>
>“That's interesting,”' said Sergeant Johnson , who had climbed out of his car by then. “I had a call right around that time too. An anonymous call, telling me to check out this house.'' Have I mentioned that Sergeant Johnson has the clearest, bluest eyes I 've ever seen? Well, he does. But at that moment, they looked clouded, almost gray. There was something about that phone call that bothered him. 
>
>The security guard groaned. “I'm going to be out of a job,'' he said. “What was stolen? Have you checked the vault yet?"

One thing that surprised me was that the runs don’t get markedly more similar to original chapter 2’s once they train more. Sure, most of the run 11’s are noticeably less-similar, but by the run 101’s it depends more on the particular direction a particular run took (as a result of turning the metaphorical steering wheels of machine learning this way or that). It’s kind of funny how on multiple training runs, run 401 was a bit of an oddball. Run 401 from training attempt 2 gets at some of the same mystery-esque vibes:

>was a natural anyway; shs’s short, with brown hair and brown eyes. I guess she was worried about looks, maybe because her parents disapprove of her interest in sports (her hair is permed and she has no interest in anything else). Or maybe she had a good time with her older sister," Dawn added. "What else happened?"
>
>"I met these kids," I said.
>
>"Can't you imagine that?"
>
>"Me and my friends went to a concert in Stamford. We were wearing black shoes. Then the lights switched from blues to white."
>
>I smiled. "They were making a song called 'Duh-huh-huh' in which I"m the lead…. It wasn"t very good," I said. "Now guess what — the lights switched back to blues as the song ended and we played the entire concert again."
>
>"It went great," I said. "I could hear the blues playing in the background."
>
>"Dawn, that"s one of the things I hated about the school year." "How many more classes will this school be in?" she asked.
>
>"I think I’ll take a second to think about that." (Dawn has to sit a hundred different ways a day, and it seems like a long train ride) "Two hundred and fifteen," said Dawn slowly, quietly, "I think. Three hundred and eleven," she began slowly.
>
>"Great," said Kristy. "The music was good, but there was still just nothing left over."
>
>"We played the whole thing from about seventy-five to seventy-seven," I told her, with some rehearsal help from Mary Anne. "I hope I’re lucky to find some of that stuff."
>
>"If that is the case," Mal said, "you might want to go to Stoneybrook Manor and search there for some of that stuff."
>
>"Where did I tell you about it?" asked Dawn. "I wonder. I guess it looks like a haunted house."
>
>"It's a haunted house," I said.
>
>"What kind of place is that?" asked Mary Anne.
>
>"It's a haunted house," I said.
>
>"Well, it’s full of stories, you know, stuff that"s old, hearsay, ghosts, stuff like that."
>
>"Oh, I knew about that," said Dawn, smiling as hard as she could. "I don't know too much about horses." She pulled her hair back from her face. "I’ll just ask Dawn what happened."
>
>"Just telling the truth," Mary Anne said. "Who put that?"
>
>"You know your parents," said Mary Anne. "I meant what I said. Why did your dad bring them up?" (Their parents had been friends all their lives, and had fallen in love with Mary Anne and Richard.)
>
>"You meant it too, Dad!" I said sharply.
>
>"I know what," Mary Anne said. "I just wanted to tell you, Dad, all this."
>
>"It’s only fair," said Dawn, just as sharply, "I’m allowed to talk."
>
>Mary Anne lifted her eyebrows a couple of ways up. "Don't you want to talk?"
>
>"Oh, yes." I did. "It’s not fair." I didn't expect her to back away or anything, but she did. "
>
>"How old were you then?" asked Dawn.
>
>"I guess I was seventeen." She looked worried. "Did you want to talk about it?"
>
>"I"d like to talk about it," I said. "I don"t know how to talk." Mary Anne smiled and smiled back with some rehearsal help.
>
>I was disappointed. It wasn"t like "real," I realized. "There"s no real old-school."
>
>"Well, there was," I said. "I guess then, anyway." I was looking at Dawn. She was

"I guess then, anyway", indeed. Weird runs can happen anywhere -- even in the later rounds. One of the least-similar texts is round 901, attempt 3:

>a big family in our church (my dad is vice-president). He doesn’t attend many meetings because we have to attend only four regular men’s houses. Plus, we have an awful lot of pets. ’Well, you have two minutes to feed everybody a box of puppies,” Claudia cried.
>
>“Puppies!” cried all of the friends I didn’t touch.
>
>“Feed everybody a box of puppies,” Stacey said. “Hey, it’s not a bad thing to do. You can be friends too.”
>
>“Feed people,” Dawn remarked.
>
>Jessi said, “An awful lot of people are desperate for a kitten.”
>
>“The poor ones!” Logan said.
>
>“Feed people,” Stacey remarked.
>
>Mal said, “I’m starving!”
>
>“On a poor person!” Claudia said.
>
>“Poor people can’t go hungry sometimes,” Abby volunteered.
>
>“Poor people exist!” Logan exclaimed.
>
>“The planet you’re looking for could be yours!” Jessi chimed in.
>
>Everyone became fiercenessed.
>
>Claudia shrugged. “The punks never ate the punks,” she said. “It’s fine in the punks’ way.”
>
>“Yeah,” Abby laughed.
>
>“I could have stuck puppies on the box,” Claudia agreed.
>
>“Maybe some of the puppies would go to a puppy shop,” Dawn suggested.
>
>“Or just kids’ toys,” Claudia volunteered.
>
>Mary Anne frowned. “I’m not going to stick an adorable puppy on a box with puppies!”
>
>“I’ve already given up,” Mallory volunteered.
>
>Mallory squirmed up. “You have a lot of work, Mallory.”
>
>“I’m making major progress,” Jessica said.
>
>“Mallory’s been able to show progress,” Abby replied.
>
>“Well, Mallory and I are still in the middle of a seventh-grade romance,” Mary Anne began.
>
>“Yeah!” I blushed. “We were just picking up a cold that afternoon. Mallory’s practically freezing!”
>
>“I have lunch,” Abby said.
>
>“I just figured out a new way to survive,” Mary Anne said. “It’s called a jujube.”
>
>“Well … this morning it’s a meal.” I handed the phone to Mallory. “I take it you and Jessi have a baby and Mallory needs a litter?”
>
>Mallory nodded. “Okay. You and Jessi go talk to each other. Then we’re off.”
>
>Jessi nodded again. “It’s fine.”
>
>“I heard about the recycling program at the school,” Claudia said.
>
>I did some quick math, and then checked my friend list and voilà! A total of four kids was sitting for four families!
>
>“Not bad,” I said. “They’re so many kids I wish we had a whole bunch instead of just two.”
>
>Claudia waved her hand to let me in. “The We ♥ Kids Club!”
>
>“Great,” I said. “Good for me.”
>
>“I’m looking forward to sitting with you all day,” Mary Anne said. “Your shoulders will lift.”<|endoftext|>
>The sound of clacking on my ultrasonic Barbe radio could be heard all over town. (My ultrasonic barbe is old school, no pun intended.)
>
>"Yesss, this is Dawn Schafer," Claudia Kishi said. "I heard this new project going on today at your school headquarters, Aurora Elementary School."
>
>Shaking my head, I grinned. "Well, it's true," I said.
>
>"And it's nice to have you back," Mallory Pike said.
>
>Mary Anne Spier chirped in.
>
>Rrrring!
>
>I jumped sideways.
>
>No, this wasn't quite the crash that it seemed. All my left leg was mangled. I had landed on my stomach.

In order to quantitatively identify the most-different passages (instead of, you know, just relying on my eyeballs to differentiate colors on the graph), I summed up the cosine distance values for each row (remember that each row -- and each column -- corresponds to a text, and when two identical texts are compared, the value will be 0) and pulled out the 10 passages with the highest score:

#Adds sum column to spreadsheet with cosine distances
cosine_distances_freq['Sum'] = cosine_distances_freq.sum(axis=0)

#Display spreadsheet with cosine distances, including new Sum column at the end
cosine_distances_freq

#Shows the rows with the 10 largest values in the Sum column
#(i.e. the texts that are the least similar to the other ones)
cosine_distances_freq.nlargest(10, 'Sum')

7 of the top 10 most-different text excerpts were generated by GPT-2.

But what about the most-similar text excerpts? This time, I pulled out the ones with the lowest total values:

#Shows the rows with the 10 smallest values in the Sum column
#(i.e. the texts that are the most similar to the other ones)
cosine_distances_freq.nsmallest(10, 'Sum')

6 of the top 10 text excerpts that are most similar to everything else are original BSC text… but GPT-2 was still represented by 4 texts -- and the #1 most-similar text to everything else is GPT-2! It does make some intuitive sense: if GPT-2 fine-tuning is supposed to make regular GPT-2 sound “like” some other text, it looks like there were some really successful samples! And none of these most-similar GPT-2 samples were from the beginning of the run -- the earliest was run 401, there’s a 601, 801, and 901. Attempts 1, 4 (twice) and 5 are represented. But the totality makes me feel the randomness of the flailing-at-feature-knobs aspect of training a model.

Let’s compare the most-similar BSC sample (from “*Mary Anne and the Zoo Mystery*”) and the most-similar GPT-2 sample (run 801 from attempt 1):

| "Mary Anne and the Zoo Mystery"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | GPT-2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| the director's chair that she always sits in during club meetings. "If you guys want, we can organize the kids and help spread the word. Maybe we can even do a few projects to help raise money for Babar." I love it when Kristy gets excited about a project. She puts herself one hundred percent behind it and makes it happen.   Take the Baby-sitters Club, one of her greatest ideas of all time. She came up with the idea to form the club while sitting in her kitchen one day, listening to her mom try to find a baby-sitter. You see, Kristy's father walked out on her family when Kristy was six and never looked back. That left Kristy's mom to work and raise four kids. Anyway, on that afternoon last year, Mrs. Thomas (that was her name then) made phone call after phone call trying to find someone to take care of David Michael, Kristy's younger brother (he's seven and a half now). That's when the great idea hit Kristy like a bolt out of the blue. Why not form a club consisting of responsible, experienced sitters? Parents could make one call, to the club, and reach a whole bunch of good sitters at once. Brilliant, huh?   In the beginning, there were only four of us — me, Kristy, Claudia, and Stacey McGill. Claudia, who is a fantastic artist, designed our flyers and the club was on its way. We decided to meet three times a week, on Mondays, Wednesdays, and Fridays from five-thirty to six in Claud's room. Kristy and I used to live across the street from Claudia on Bradford Court. That's all changed now. I already told you that my dad married Sharon and we moved into their farmhouse. Well, Kristy's mom married Watson Brewer (a genuine millionaire) and Kristy and her three brothers — Charlie, age seventeen, Sam, age fifteen, and David Michael — moved into his big beautiful mansion on the other side of town. Watson has two kids from his first marriage, seven-year-old Karen and Andrew, who's four. After he married Mrs. Thomas (now Mrs. Brewer), they adopted Emily Michelle, a two-year-old from Vietnam. Then Nannie, Kristy's grandmother, moved in to help look after everybody. When Karen and Andrew are living at the big house (they call their mom's house the little house), which is every other month, there are ten people at the Brewer mansion. It's a good thing it's so huge.   But anyway, in the beginning, when the club was formed, Kristy and Claudia and Stacey and I were neighbors. We decided to hold our meetings at Claud's because she has a phone in her room and — are you ready for this? — it's not just an extension, it's her very own phone line. Kristy became president because the club was her idea and because she's a real leader. (Some people would say she's loud and bossy, but I prefer to call her strong-willed.) We can count on Kristy to be at every meeting in her jeans, sneakers, and a turtleneck shirt. She usually wears her baseball cap placed firmly on her brown hair, which is pulled into a ponytail. Since we were holding meetings at Claudia's, we elected her vice-president. Claud does a lot of things for the club, such as pick up calls when the club's not in session and supply us with snacks. She is also our resident artist and all-around cool, creative person.   In the looks category, I would say that Claudia is gorgeous with her shiny jet black hair and perfect clear complexion. Claudia does have a couple of flaws. (Don't we all?) One, she is a major junk food addict. I'm not kidding. She stashes cookies and candy bars all over her room. And two, although she is very smart, schoolwork is Claudia's nemesis. She can paint a picture of clouds soaring over a summer landscape with her eyes closed, but ask her to diagram a sentence and she freezes up completely. At one point her parents were so concerned about her falling behind in her studies that they asked her to consider quitting the BSC. It was awful. Fortunately, Claudia pulled her grades up so she didn't have to quit. But we understand that, for Claudia, homework has to come first. Stacey McGill, who is a real math whiz, was our first treasurer. She and Claudia are a lot alike. Both have the absolute coolest clothes — not because they're rich and can afford to buy a million outfits, but because they have a real sense of style. Claudia will go to a used clothing store and buy an old black vest, a beat-up derby, and an old-fashioned collarless shirt for a few dollars. Then she'll add some lace and beads to the vest to make it extra funky. She'll make a sequined headband for the derby and belt the big white shirt over some wild leggings and voilà! She looks like a million dollars.   Stacey's style is just as cool, but a little more sophisticated and sleek. I think it comes from the fact that she lived in New York City for such a long time | red one in her own clothes with black suspenders.  One thing that does tie up the club notebook is Claudia's homework. Claud is fantastic at it. She does it in such a professional, original way. I like that. I try to do what I can to improve every day.  We also have two sitters who are younger members of the club. They fill in when we have too many sitters. One of them is Jessi Ramsey, who lives in my new neighborhood. The other is Logan Bruno, who happens to be Mary Anne's boyfriend, and he is wonderful.  Jessi has curly golden hair and a flair for funny looks. She has two younger sisters, Claire and Andrew, so she likes clothing and makeup and all that junk. Jessi adores horse prints and the local kid-Kerr, and you can tell that she likes things like recycled baby-sitting materials, organic strawberries, and wildflowers. She also likes to think of herself as a ballerina, which is a classification system for performing arts arts arts (academic), creative, in which the dancer is the student and the choreographer is the professional. According to Jessi, ballet is the one she wants to do as much dance as she can, and that it will probably be a big success simply by practicing her dancing. I bet she'll do the trick just like David Michek does, and it's as graceful as the way a football player catches the ball and tries to make a dive in the air while taking a release from his foot just before his jump press.  Jessi's family life is more complicated than Claud's. Like Claud, her family lives in Stoneybrook, because Stacey's dad remarried, leaving Jessi ‘where's-you-going-to-meet-the-new-born-at-the-right-time basis.”  Jessi's mom grew up in New York City, which helps to explain why she is such a great ballet dancer. She moved to Stoneybrook when her dad was transferred back to New York City. And then, when her parents divorced, her mom went back to Stoneybrook to stay with her father. (Her move left her with a combined household income of almost four times what she made in New York.) So, at the beginning of seventh grade, her grandmother, Mimi, moved in with Jessi and her family. (Before Mimi, there was only one Charlie Thomas, the other one Yodel, and the last one Arnold Schwarzenegger, and they lived in a mansion across town.) There are two other members of the BSC, a girl named Dawn Schafer and one boy, a girl, a boy, and a girl, a dog, a cat, and a friend of the club called … my friend Stacey. Remember how I was telling you about Stacey? Well, she was the treasurer of the BSC. That's because she joined shortly after I went back to New York. She and Mary Anne Brewer, the president, hatched up around Mary Anne. Later when they were dating, they discovered that Mary Anne's dad and Dawn's mom had dated in high school. They got them fixed, and by the time they got married, they had a huge family. And the Thomases moved all the way back to New York, along with Dawn and her mom and two brothers. So now Stacey lives in the Big Apple. You see, our club was born out of this — the club we all came up with was Kristy's, not Stacey's, idea. Kristy thought the four main business functions would be business, club meetings, where the sitting kids could hang out, and club dues. Kristy thought that regular people would be busy: everybody can be club secretary (except Mary Anne's parents, whom they try to have sorted out).  Dues are necessary, though. We hold our meetings on Mondays, Wednesdays, and Fridays, from five-thirty to six. On Fridays, we close at five-thirty.  Besides meeting for five hours out-of-the-way, paying dues, and being nice, Stacey has a special talent. She's an artist. She paints, sculpts, sculpts. She makes jewelry and clay pottery. Her work takes shape almost like a work of art. She's in the process of putting together the most fascinating clay sculptures ever put up. They're so artistically created, they're almost unbelievable. I'm so impressed with her sculptures that I've even given her a performance onstage at my school's productions.   * * *  As anyone who has ever been in Stoneybrook knows knows, Kristy. She's my best |

The excerpt from *“Mary Anne and the Zoo Mystery”* is instantly recognizable as classic BSC chapter 2: we get the (oft-recounted) origin story of the club, and a detailed description of Kristy and Claudia.

GPT-2 is clearly going for something similar in this sample. Sure, it focuses on Jessi instead of Kristy and Claudia, but that narration includes a physical description, family background, and things about her personality and hobbies. It introduces other characters, as well as things about the club. And it happens to get some BSC facts right, like “Logan Bruno, who happens to be Mary Anne's boyfriend” and the fact that Jessi is one of the “younger members of the club”.

But even though, quantitatively, these two passages have nearly the same total cosine distance value (and GPT-2’s is slightly lower), no BSC fan would be confused about which was machine-generated. And any reader of English should be able to easily identify the machine-generated one, too. The word frequencies are right, but the result is… weird. “She also likes to think of herself as a ballerina, which is a classification system for performing arts arts arts (academic), creative, in which the dancer is the student and the choreographer is the professional.” And there’s the mixed sports references, plus a sequence of actions that are hard to imagine a human doing simultaneously:  “I bet she'll do the trick just like David Michek does, and it's as graceful as the way a football player catches the ball and tries to make a dive in the air while taking a release from his foot just before his jump press.” And then there are some issues with counting and getting into loops that remind me of talking with my very talkative 2-year-old: “There are two other members of the BSC, a girl named Dawn Schafer and one boy, a girl, a boy, and a girl, a dog, a cat, and a friend of the club called … my friend Stacey.”

As useful as text-comparison algorithms like those in [DSC 8: Text-Comparison Algorithm Crazy Quinn](https://datasittersclub.github.io/site/dsc8) can be, especially when working with a lot of text, these GPT-2 experiments really drive home the value (okay, I’ll go so far as to say “necessity”) of reading -- or at least spot-checking -- the texts with your very own eyeballs. You know, just to make sure there aren’t any ghosts in your laptop.

### Stochastic parrots

We've had a lot of good laughs at the expense of ghosts in various computers in this DSC book, but it's not all funny. Since we started writing this book, GPT-2 has been surpassed by [GPT-3](https://en.wikipedia.org/wiki/GPT-3). GPT-3 is a language model that's 116x bigger than the full GPT-2. It's so big, it would be unfeasibly costly to fine-tune it. And... you kinda don't need to? It has so much text that it can write in various genres and styles, including the style of particular authors like Dr. Seuss, often with surprising success. (Check out [GPT-3 Creative Fiction](https://www.gwern.net/GPT-3) for some examples.) What's it made of, you ask? Much more than just websites linked from Reddit. Its documentation gestures towards two data sets that may be relevant for our purposes: "Books1" and "Books2". [No one knows what those actually are](https://twitter.com/cases_les/status/1357412339499364353), but guesses include everything on Libgen and/or Google Books. Which means that the *Baby-Sitters Club* is probably floating around in there somewhere.

You have to request access to GPT-3, and the LitLab hasn't gotten it as of February 2021, so I haven't played with it myself. But I have taken note of the criticisms of GPT-3. That at the end of the day, it's still not -- and can't be -- "intelligent". I keep coming back to what Jeff told me last summer: "it's just math". And that's just it. It's [a big pile of data about the probability that one particular word will follow another](https://xkcd.com/1838/). Once you have a model, there are settings you can fiddle with regarding text generation, including the "temperature". The closer you set this value to 0, the more repetitive the results will be: the model will just repeat back things from its training data. A temperature of 1 is pretty common, requiring the model to be moderately "creative" without devolving into total nonsense. But the problem is that this ghost in the laptop doesn't know anything except word frequencies -- it doesn't know the axes along which it can be legitimately creative before things get weird. Combining new color- or style-adjectives with articles of clothing and accessories to generate new outfits for Claudia? Great! GPT-2 is on it:

-   Claudia was wearing a leopard print checkered scarf over a clear blue sundress.

-   Claudia was wearing an oversized purple backpack, a white short sleeved turtleneck, and a white polka dot under her black boots.

-   Claudia was wearing a baggy black shirt and jeans, which Claudia had painted in red, white, and green.

-   Claudia was wearing a wool coat and pearl-studded high-top sneakers. She had on black scrunchies and braided shoelaces under her clothes. (The top pair of her coat she made herself. She makes the main stuff.)

(Okay, even here, we see the limitations of GPT-2's understanding of how clothes typically get layered.)

But it also shows absolutely no hesitation in generating text that flies in the face of human anatomy:

>The front door flew open, and Kristy --- tall, graceful, and incredibly pretty with three legs and the most total body of skin I've ever seen --- burst into the room.

But even though OpenAI plasters their models with warnings (including not using it in medical contexts because ... you know... they don't actually know anything), "artificial intelligence" has gotten a lot of interest from business, government (including courts), and medicine, as Anouk mentioned above -- sometimes with terrible results. Because all the model actually knows is the word frequencies it learned from its sources... and not all those sources reflect humanity as we'd like it to be. A prototype of a [medical chatbot using GPT-3 told a patient to kill themselves](https://artificialintelligence-news.com/2020/10/28/medical-chatbot-openai-gpt3-patient-kill-themselves/). And Jerome Pesenti, head of the Facebook AI lab, [criticized the sexist, racist, and other derogatory language that GPT-3 produced](https://www.nytimes.com/2020/11/24/science/artificial-intelligence-ai-gpt3.html) when discussing Jews, women, Black people, and the Holocaust.

This made me morbidly curious -- what awfulness would our fine-tuned model spit out, given a prompt that might trigger some awful thing that it learned before we introduced it to the *Baby-Sitters Club*?

I tried "Anna is Jewish":

-   Anna is Jewish and has lived for over ten years. That's not a bad thing, just weird.

-   Anna is Jewish. Kristy's mom is the rabbi of our family.

-   Anna is Jewish and Mal is a true New Yorker --- a world away from Yankee Stadium.

-   Anna is Jewish, though she wasn't born that way.

-   Anna is Jewish.) It was Kristy's idea to bring Jewish kids together and to help to find table after table for Jewish weddings.

-   Anna is Jewish. (The rest of us are Caucasian.)

-   Anna is Jewish, while Kristy's mom is a Roman Catholic.

Some of these make me raise an eyebrow, but the vast majority of the 1,000 samples it generated treated this fact like any other in a list of facts about various characters in the BSC.

How about "Jessi is Black" (which, sans capitalization, is a common phrase in the *Baby-Sitters Club*)?

-   Jessi is Black. She is a truly talented artist and knows how to do just about everything she wants to do --- from packaging cookies to making hand-me-down jewelry.

-   Jessi is Black, and we all really like her. But she can be incredibly stubborn. She even argues with us!

-   Jessi is Black, with long, shiny black hair and gorgeous chocolate-brown eyes.

-   Jessi is Black, and we adore her. But her family is a worse bunch than mine.

-   Jessi is Black. Kristy is sometimes rude and even sad and doesn't understand how the kids in her neighborhood are affected by prejudice.

-   Jessi is Black. When we first met her, Claudia had to convince us that she was as pretty as a Black woman and, more important, could still wear her eyelets

-   Jessi is Black. It's sort of a gross, disgusting thing to do, even if the facts are true. 

-   Jessi is Black, not just plain ugly.

-   Jessi is Black, so she's usually pretty tactful.

😳 Yikes. Some of the examples just treat it as another fact (or catch onto the "Jessi is Black and Mal is white" trope from the Baby-Sitters Club books), but we're seeing a lot of negative bleed-through from the base GPT-2 data here. In case you're not familiar with the *Baby-Sitters Club* corpus, Jessi is a ballerina (and sometimes swimmer), not an artist (that's Claudia). Her family is great (not a "worse bunch" than anyone's), though early on there's some normal tensions with her aunt. No one calls her gross or ugly, and she's not particularly stubborn compared to the other BSC characters.

How about "What about the Holocaust?"

>"What about the Holocaust?"
>
>"The Kristy camp claims the whole thing is a cover-up," I said.

>"What about the Holocaust?" Jessi asked.
>
>"I don't know," I said.
>
>"You know what bothers you most? Not knowing the names of the people who did it."
>
>"Who did it?" Jessi guessed.
>
>"Nancy Drew," I said. "Dr. Jekyll and McBaron."

>"What about the Holocaust?" I asked.
>
>Stacey nodded. "No, no. It's a terrible idea. But what if the Jewish people did go on a killing spree? What would they do?"

>What about the Holocaust? Kristy has a BIG problem, and that's totally understandable. But we have to remember that not all of Kristy's ideas are the same. For example, there are her prejudiced ideas --- like the color-coded public school buildings so that African-American and Latino students can look the same, or the one-size-fits-all practices for boys (boys, in fact, are taught in these buildings by Kristy's boss, Richard.)

If this is the garbage we're seeing from the smallest release of GPT-2, I don't want to imagine what GPT-3 would produce.

Some of these issues are taken up in a paper called "[On the Dangers of Stochastic Parrots:  Can Language Models Be Too Big? 🦜](http://faculty.washington.edu/ebender/papers/Stochastic_Parrots.pdf)" by Dr. Timnit Gebru and Prof. Emily Bender (of whom I'm a huge fan, particularly for her "Bender Rule" which basically works out to "always name the language you're working on -- even/especially if it's just English"; I wish we'd universally adopt it in DH). The paper is notable not least for the fact that it led to Google firing Dr. Gebru from her position in AI Ethics after they tried to censor said paper, which triggered a [cavalcade of protests](https://twitter.com/labortechgroup/status/1360335807333232641), other members of the team quitting or being forced out, [Google messing with the search results](https://twitter.com/kareem_carr/status/1359316503200423939) for "Timnit Gebru", and generally surfacing all sorts of HR practices ranging from the dubious to racist. It's worth reading through the whole thing. [This interview with Prof. Bender](https://www.morningbrew.com/emerging-tech/stories/2021/02/01/inside-hotbutton-research-paper-dr-emily-m-bender-talks-large-language-models-future-ai-ethics) captures some of the major points, including the environmental costs of training ginormous models like GPT-3, the fact that these models really aren't "intelligent", in addition to the harm done by those creations generating text like I've described (and shown) above.

I love the "stochastic parrot" phrasing -- the implicit squawkiness, the fact that parrots produce poop that requires cleaning-up after. (Or maybe I'm just too far down the rabbit hole of potty training with the local toddler.) Next time you hear "artificial intelligence", I hope what you imagine is a "stochastic parrot" that is, fundamentally, "just math."

### Anouk
February 2021. Another cold day, with Edinburgh blanketed this time in an unusually deep snowfall whose fairytale prettiness was an eerie reminder of climate catastrophe. The university buildings were again deserted, though not because of a strike. While GPT-2 might have been having a good pandemic, bulking out and levelling up to GPT-3, for the rest of us it felt like we'd gone from a rather quaint fear of falling down a well to being in freefall for almost a year, with no idea at all of where the bottom was or what would happen to us when we hit it.

Mid-abyss, I mused on how far we'd come, or not. We'd neither cracked open the black box of machine-generated text nor vacuumed up the ghosts in our machines into a trap, Ghostbusters-style, in order to examine them. We did have some other things, though. We had a Model Of Our Own, fine-tuned by Quinn, and some conceptual metaphors for understanding it, courtesy of Annie. We had a little better of an understanding of which thematic preoccupations of the original BSC texts lent themselves particularly well to being reproduced by a machine learning model (the various permutations of family and romantic relationships amongst a set of characters, the ways an individual's identity is delineated by means of their appearance, clothes and hobbies) and which stylistic tics a model could most readily emulate (creative combinations of colors, styles and items of clothing, the relentless cheeriness and exuberance of BSC narrators, the way the narrative is driven through dialogue). We also had a more precise sense of how closely machine-generated texts matched the originals on which they were trained, and some ideas for future directions we could take which would take advantage of the expertise of our fellow Data-Sitters.

Most importantly, though, Quinn and I had had many good laughs, sorely needed and greatly valued over the past year. So we decided to put GPT-2 in its place, on Twitter, where we hoped it might bring occasional bursts of joy. We combed through the text files Quinn had generated, pulled out chunks of 280 characters or less, then used[  Zach Whalen's handy SSBot](https://github.com/zachwhalen/ssbot) to build a twitterbot,[  @daily_dsc](https://twitter.com/daily_dsc). As a final touch, I ran the cover of Claudia and the Phantom Phone Calls through[  a convolutional neural network](https://deepdreamgenerator.com/) (you can [try it too](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/generative/deepdream.ipynb)). It latched onto Claudia's almond-shaped eyes and, pleasingly, turned them for once not into code for exotic otherness but into[  puppy dog eyes](https://twitter.com/daily_dsc/photo) which it then also added to the phone, her hair, her hand, and the child she was babysitting.
 
Our bot began burbling happily away (“"Oh, my lord!" I shrieked, and flopped on her bed. I took her bag of potato chips out of my pocket, and stuffed each into my hair. The potato chips were one yellow potato chip wrapper with a picture of Stacey on one side and a picture of a woman holding potato chips in the other”) and I gazed out the window at the extravagant fluffiness of the once-in-a-childhood snowfall. There was sunshine and blue sky, an unusual sight in a Scottish winter, and eleven days and counting till primary schools were planning to reopen their doors to the youngest pupils.
 
I had written earlier that I was hopeful that scholars of literature, narrative, and language might have something to offer the conversations among computer scientists and ethicists around explainable AI. Annie, Katia & Quinn nudged me to change “hopeful” to “confident,” so I did, but with some unease: if there’s one thing the discourse around AI needs less of, it’s confidence. We didn’t have answers. We couldn’t identify the nodes producing racist bilge and simply zap them in order to generate an enchanted fictional world where “Jessi is Black and Mal is white” isn’t always already overdetermined by the crushing weight of historical inequities and ongoing violence whose eruptions had deepened the horror of the past year. Out the window, the cushiony puffs of white adorning the walls and roofs of my neighbourhood gave a serene roundedness to the sharp corners of the world, making it easy to forget the grime underneath.
 
Annie, looking over my virtual shoulder, remarked, “You know, it’s not AI—or math—that produces racist language. It reflects the racist thoughts that are encoded into the data we give it. Simply put, AI isn't racist: we are. That's why it's important for humanities scholars to be part of work on machine learning, and to be able to adequately evaluate training texts before using them to make decisions with, say, legal consequences.” She was right, of course. Busting the lid off the black box and rummaging around in it to try and fix things was a distraction, and about as feasible as prying open people’s heads to rearrange the neural networks in their brains to change the way they think. But I find it a helpful analogy to think of the billions of associations that a machine learning model makes as it assembles a mathematical model of the similarities between all the words in the language (and then some: *fiercenessed, I’re, shs’s*), and the associations that human beings form as we absorb information about the world from texts, especially the beloved, and frequently reread, texts from childhood. 

*The authors would like to thank Annie K. Lamar for her help with the preparation of this manuscript. (Really, seriously, we couldn't have done this without her!)*

## Suggested citation

Lang, Anouk and Quinn Dombrowski with Annie K. Lamar. "The Ghost in Anouk's Laptop". *The Data-Sitters Club*. February 18, 2021.