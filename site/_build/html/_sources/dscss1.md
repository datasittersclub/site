---
layout: default
title: "DSC Super Special #1: The Data-Sitters Debate at Dartmouth"
coverart: "dscss1_cover.jpg"
bookseries: superspecial
permalink: /dscss1/
---

# DSC Super Special \#1: The Data-Sitters Debate at Dartmouth

```{index} single: *Book Topics ; Is the DSC working as a project?

```

by Lee Skallerup Bessette, Katherine Bowers, Maria Sachiko Cecire, Quinn Dombrowski, Anouk Lang, and Roopika Risam

September 23, 2024


<div style="float: right; width: 300px;margin-left: 7px;margin-top: 0px;">
<img src="_static/images/bookcovers/dscss1_cover.jpg" alt="DSC SS1 book cover" />
</div>

## Quinn 
*March 16, 2023*

We arranged ourselves on the fluffy blue couches of the Dartmouth Film and Media Studies faculty lounge and took a commemorative photo: the first-ever in-person meeting of the Data-Sitters Club, a group I started while [on vacation in Las Vegas in September 2019](https://datasittersclub.github.io/site/dsc1.html). (For more on the Data-Sitters Club, check out [Chapter 2](https://datasittersclub.github.io/site/chapter-2.html).) 

![The Data-Sitters sitting on a couch, recreating more or less the pose in the DSC art](/_static/images/dscss1_group_photo.jpg)

Roopsi began a new job at Dartmouth last year, and used some of her funds from the [Digital Humanities and Social Engagement](https://dhse.dartmouth.edu) cluster to arrange this retreat, bringing all six of us together -- in some cases, to meet for the first time. On this first morning of the retreat, Roopsi and Maria had driven up from Massachusetts while the rest of us got to know each other over breakfast, and we were finally all sitting down together to talk about what we might do with the time we had together.

"I now call this meeting of the Data-Sitters Club to order," I declared.

"It's so nice to be here with you all," said Katia. "I'm just vibing on that. Maria Cecire, Program Officer, what do you think?"

"We have a 10-page limit," Maria joked, and we all laughed. One of the joys of writing for the DSC is having fewer rules and constraints than any other context in our academic lives.

"Let's step back and do some strategic thinking," said Anouk.

"It'd also be nice to go over what we're working on and what's coming out in the near future," added Katia.

"I had that draft about 'Roopsi and 3D visualizations' a year ago," Roopsi chimed in.

## The Argument

"But what are the questions?" asked Maria. "I think there's some people who might be into the DSC, but aren't into tools. What are the questions we're trying to answer here?"

"So here's the thing about questions.... I'm not sure if I fully understand what text analysis can do to help us answer questions. So I would love to know," said Roopsi.

I heard alarm bells going off in the back of my head. Roopsi's thoughtfully-crafted schedule for this retreat had scheduled *DSC Family Feud* for 3:30-5:45 pm on the second day. Were we really going to start things off with our fight instead?

"You sent me the whole thing about newspapers, and proximity of words, and racism and I'm like... yes," Roopsi said to Anouk. "But I struggle with understanding --  if we wanted to ask a question that's **not** about the structure of a text..."

"To me, the answer is always an interaction between tools and the stuff you can only do with your brain," interjected Maria. "But for that, you need to model for other people how you bring tools and your brain together. The things we've been looking at don't necessarily get us to answering questions without that second part. Why would I do this thing, if at best it'll confirm something I already thought? So why do I need it to confirm that? Or at worst give me something I don't understand."

"I think we've modeled that a little bit in all our pieces, especially the Multilingual Mysteries," Lee  chimed in. "We didn't learn anything about the Baby-Sitters Club, but--thinking about how we [explored the French spaCy NLP model in Multilingual Mystery 5](https://datasittersclub.github.io/site/dscm5.html)--we found that it's highly problematic because the French language model is trained on a type of French that's so different from what the books were actually written in. So you see the gap -- it's not necessarily a problem with translations, but a problem with the data set underlying the tools."

"That's a DH finding," remarked Maria.

"That's the thing: I feel super comfortable with DH findings," said Roopsi. "And this is why I'm skeptical about the value of computational text analysis as a literary tool. I haven't seen anyone who can show me what I can get by using any one of these tools that I couldn't figure out some other way. The only example that comes to mind is when I was teaching Frederick Douglass's "What to the Slave is the Fourth of July?" And when I stuck it into Voyant, 'God' appeared so much, even though it's not a religious text. But then I had my students think about the genre --- the jeremiad --- so that does make sense."

"I mean... you also could've just read it," Maria added.

"Yeah, but I probably wouldn't have noticed because I don't notice God-things."

"But that's the jumping-off point of research."

"Agreed -- I don't know of a good example for someone who's like, 'I have this question about literature that I am now going to see if this tool can help me answer,'" said Roopsi.


Engaging with Computer Science
------------------------------

"I'm also super interested in this question," added Anouk. "One important thing DH can do is intervene in how computer science people talk about bias in terms of the notion of 'ground truth', which drives me bonkers. I'd be laughed out of my field if I suggested there was a 'ground truth' with which I could validate my findings. It's an epistemological question. Computer scientists use that framework, but in the humanities we don't operate in that model, and I think there are things that humanities research can teach those whose research is anchored in ideas of ground truth, for instance by designing something to show how you might start from the Baby-Sitters Club corpus and then go beyond it. In a world of large language models we need to be looking at larger corpora, which is where something like [YRDL](http://yrdl.org/) comes in. You might get some hints about things in the Baby-Sitters Club corpus that seem like they might be interesting at scale but can't be meaningfully investigated with machine learning because the Baby-Sitters Club corpus is just too small. But you could still use it as a starting point for exploring those same phenomena in larger corpora such as YRDL, BERT, ChatGPT, and bigger language models where particular words can be shown to have wider metaphorical resonances. And you can take those findings a step further to connect them back to work in computer science."

"You're still talking about a mode of using the tools themselves, though," replied Maria.

"I'm making a claim," Anouk stated.

Roopsi attempted to paraphrase: "You're making a claim about the BSC books, but you need a larger corpus to compare?"

Anouk tried again. "We have extraordinary domain expertise about the Baby-Sitters Club here. When a word appears in our corpus, we can be pretty confident that we know the resonances behind it, and what it's signaling. And we can leverage that specialist knowledge to point to the other meanings that attach to a specific word, and we could then go on to test those intuitions, say, with YRDL. Like how Tressie McMillan Cottom drew attention to the racialised meanings[ that attach to the word 'blonde', and was attacked by people who don't understand](https://www.nytimes.com/2023/01/19/opinion/the-enduring-invisible-power-of-blond.html)."

"Or who don't want to understand," added Maria.

"Right. Tressie has the expertise of a sociologist, pointing out the covert meanings that the word carries. I'm not sure 'blonde' operates the same way in the Baby-Sitters Club, but it's a word that, on the surface, operates as quite a neutral, bland descriptor."

"Not if you're brown," Maria replied.

"That's what I mean -- it's a word that can look generic, but it carries other meanings, and you can find those if you have a massive corpus!"

"But if you have the lived experience, you can just say 'that's not how it works'. Anyone who's grown up not blond has to think about it, and would know that's what's coded by blond."

"But that's where computational text analysis comes in," Anouk said emphatically. "You can make those points based on lived experience and the tech world is unlikely to hear you. But they might pay attention if you can show those associations occurring in a large language model."

## New Discoveries or Rehashing Past Debates?

"I'm not sure if we're going to convince computer science people of anything. But what does studying words get us in terms of understanding language, or culture?" Roopsi asked.

"We've been struggling with this a lot in our [Fyodor] Dostoevsky project," Katia spoke up. "We're nerdy, kind of in-the-weeds Dostoevsky scholars, we consider ourselves to be formalists, and DH goes very well with formalism, and structuralism, but at the end of the day, 100 years ago some formalists said the same stuff we're finding now. And our project wants to use these methods to find **new** things, but instead we're using it to..."

"Say [Vladimir] Propp was right?" joked Roopsi.

"Propp doesn't have a lot to say about Dostoevsky, but he was right," replied Katia. "It's more like -- our project has become something a little superficial almost, because, within our field, our findings aren't that new. What we're finding is how computers answer questions people were arguing about for 150 years. The computer comes up with an answer and we argue about it."

"That's cute," Roopsi said.

"It's cute and it's going to be a monograph and we're excited about that," said Katia. "But we've failed to do a deeper analysis so far, although we're working on that."

"But this is why the only DSC book I ever wrote was me being in a fight with everybody here!" exclaimed Maria.

"Me too, actually, for that matter," Roopsi added.

"I was like, I don't think we **should** do it this way, but everyone else was okay with doing it this way, and that was the book," Maria said. "This whole mode of working, DH -- it's not my way. The center I ran at Bard was Experimental Humanities, not DH. We used digital tools, sure, but we also made giant spider webs out of beads if that was the right method for the questions we were asking. I don't understand the mode of working that's just messing about with a data set. The point of studying texts is that they're cultural materials, they have so much attached to them. You can find meaning by diving through all that nuance -- and tools are interesting and can contribute to that! But just using a tool and moving on like we've been doing, it's a very partial thing, not an answer."

"I think of the food nouns from [Multilingual Mystery 4: Isabelle and the Missing Spaghetti-Os](https://datasittersclub.github.io/site/dscm4.html)," offered Anouk. "Lee, Quinn and Isabelle discovered something about the way food was 'culturally translated' across different language, and that opened up some real humanities questions. It made me want to know, for instance, about what the forces were in the publishing house that nudged translators to do this or that. I think it's fine if DH is the starting step in that process, pulling out something you wouldn't have found otherwise."

"I don't know if we've gone further in what we produced to the world, though," Maria sighed. "And that can be fine, it's a way for people to get a sense of what the starting steps might look like. But for me, I don't have this kind of tech expertise, and I'm not especially motivated to develop it, because I'm not using it. So I feel like I just sit on the sidelines and nag."

"What would it be like if we were to come up with a question that we could pursue together? We could pick a question, and take it through its paces, and see where we land?" suggested Roopsi. And then she turned to me. ".... Are you... taking notes? Because you're typing so fast."

I nodded.

"Here, I've got Otter AI, I can just record it and it'll transcribe..." offered Lee.

"Yeah, but that's always harder to clean up afterwards. I'm good, really," I said. I hadn't done much live notetaking since I'd left Twitter, and I kinda missed it.

"I want to hear you talk, too!" Maria said encouragingly.

"No, really, if there's something I need to say, I'll say it. But this is good stuff," I insisted, and went back to typing furiously as my friends talked.

## Linear or Playful?

“Maria, I feel like I’m positioned between where you are and where Anouk is – not that you’re on sides, but I actually am generally interested in technical problems and DH-y pieces, even if I’m not invested in the specific tool and what it can do for me and my research,” Roopsi resumed. “But I know at the same time, I don’t have the capacity to explore how you’d develop a method to pursue a specific literary question. I think it could be really interesting.”

“It’s so much about play,” Anouk added. “One of the many reasons this project is awesome is because it’s playful, it’s iterative, and that isn’t generally the way literary studies is presented in its published form, which is this fairly linear thing with an argument. What I almost always find in my DH work is that the most interesting things to emerge are the ones I don’t expect.”

“Literary studies is supposed to be about playful surprises too,” objected Maria. “This could be totally unfair because I went to Oxford, which is a very traditional place, but my experience of doing English literature in the UK is vastly different than in the US. In the UK, it was like, books in the canon. In the US, you can write about the Olympic opening ceremony, or blog posts, or…”

“That’s **you**, Maria – and you’re not usual,” Roopsi replied.

“That’s American studies,” said Maria.

“And cultural studies,” added Roopsi. 

“I worry there’s a false dichotomy being proposed here about how literary studies operates in a linear way,” Maria frowned. “DH can also be very prescriptive.”

“There’s some prescriptivism in how things get written up,” agreed Anouk. “But in our DSC books we’re at pains to show in our final write-up how many false steps we’ve taken, as we find our way through to see what works.”

“And sometimes nothing works!” laughed Lee.

“And English literary studies has just been around for longer, so it’s easier to find your way through the forest,” said Anouk.

“It’s a discipline,” said Lee. “I’m from Comp Lit, which is very **disciplined** in that sort of way. Russian is formalism…”

“Russia isn’t **all** formalism,” objected Katia.

“For me, I’ve done the same sorts of things you’ve done and was always told it wasn’t scholarship. Within my field, and even when teaching writing, it’s always ‘that’s not scholarship,’” continued Lee.

“But that’s just prejudice. It’s a social question, more than a disciplinary or scholarly question,” Maria protested. “It doesn’t mean you’re doing substantively different things.”

“In a lot of cases, when we’re doing the multilingual mysteries, what we really need is archival research. I’ve been desperately trying to get in touch with some of the publishers in Quebec to get their archives. In our books, I think we show some of the limitations we face – it’s more than just asking literary questions. It’s ‘if you don’t have institutional support, how do you approach this research’? What if you don’t have funding to travel to archives?” Lee asked.

## Why Do DH?

"The cost makes it an existential question," added Maria. "If we can't show that you can get this very expensive thing called 'DH' to answer some questions, why would we do it?"

"Even if it can't answer literary questions, what CS thinks and does is increasingly influential in how the world is run, how capitalism operates, and how power flows. An intervention into that is an important thing the humanities should be doing," Anouk objected.

"I totally agree," said Maria. "One of the reasons I've been involved in digital stuff at all is because the humanities have so much to bring to many different fields, including digital and tech spaces. People with the capacity to think like a humanist and talk enough like a tech person that the tech person feels like you get them have the power to embark on shared projects. It's not about particular tools or sets of technical expertise."

"I've had those same conversations around responsible computing, trying to find people on the CS side who recognize that we care about similar things but talk about them in very different ways, and trying to find a shared language where we can talk to industry and different stakeholders," said Roopsi.

"Yes!" said Maria. "Like when the thing you're making is something everyone agrees is important, something like diversifying tech. You can't necessarily bring literary questions as your contribution to that conversation, but you can bring historical context, theoretical knowledge, experience working with communities, gathering ethnographic information -- and in return, they bring the tech skills around coding, understanding the market, and you need everyone to be able to talk about it together at the same time."

"To some extent, it's that the epistemologies are so different," mused Anouk. "Establishing a shared vocabulary is one thing, but wrapping your head around another epistemology can take you a decade."

"It's so hard to get CS folks to really think about their data set, what it is, what it can and can't do..." sighed Roopsi, "...when they think they've fixed it by running sentiment analysis on the free Google News API which only goes back for the last 30 days anyway."

"They need to read [Katia and the Sentiment Snobs](https://datasittersclub.github.io/site/dsc11.html)!" Anouk interjected.

"What **are** sentiments?" Maria pondered, before pivoting to the big question. "What's the purpose of what we're doing? Maybe it's for ourselves, or for our field... but what we're making is for people who are already in DH."

"Or who want to try it out," chimed in Anouk.

"Or who are curious," suggested Roopsi.

"Curious with a lot of time and patience," Maria corrected.

"As a relatively new person, my experience with DH is that we come up with a question," Katia said. "Then we need to figure out what kind of tool we're going to use to try to figure out how to answer the question. Then we go to the DH librarian -- who's wonderful -- and she's like 'here are 7 tools you could learn and use!' And we're all 'OMG, 7 tools, what are we going to do?!' So we have to narrow it down, and some don't work, and we try to do a tutorial for another of them and it's written for CS and none of it makes any sense. And then it's like, OMG, command line, Python again, maybe getting it to work in some roundabout way, and it spits out an answer -- maybe, if your computer doesn't crash. But the answer isn't at all useful and you're like, 'OMG, I just spent 20 years doing this thing and it was worthless.' But what I like about the Data-Sitters Club book we've been writing is that Quinn helps me use the tools, and also, if I came across this tutorial while Googling for the tool, it'd actually be useful. That being said, I'm not sure I'd know how to Google for the tool if I was at the level of trying to even find out if any tools exist."

"But already you're a person Googling for a tool, which is such a tiny sliver of people," Maria pointed out. "And yes, they deserve to be served, and if that's our audience, I guess that's fine, but I also think..."

"When we go to the librarian we're not at the point of Googling for the tool, just after that consultation, the DSC books can help us translate," Katia replied.

"Maybe we need more librarians to know about the DSC," suggested Roopsi.

"But even if you find them at the right moment, reading our books is *many hours of reading*, which just isn't realistic unless you're already invested," Maria objected.

## Audience

“I think there are a lot of things going on here,” said Roopsi. “For me, the answer to my question about audience is totally different if we were using a different method than computational text analysis. Computational text analysis eliminates the possible audience of regular people. Prove me wrong someday, I’ll happily retweet you. But I don’t think random people walking across the street would actually be into this.”

“Can confirm,” Katia chimed in. “People who are excited about the Baby-Sitters Club in general go to our website and see what we’re doing and it’s like, WTF.”

“It’s for people who care about DH, and want to teach DH,” Roopsi added.

“That’s it, people trying to teach these tools for a specific audience,” Katia agreed.

“That’s what we’ve done so far, “ said Roopsi.

“Yes, very usefully,” confirmed Maria.

“Are there other avenues to pursue?” asked Roopsi. “I mean, what is our purpose? I have no interest in convincing anybody to use any particular kind of method, or that DH is important. Everyone’s like ‘OMG everything will be DH.’ No. Just stay in your lane, it’s fine. I’m happy to just be here and read my things and write my things and play with my things and write half-baked stuff about some of my methods. That’s what I write about. It may not be ‘real scholarship’ because it’s ‘just method.’ But is there a different kind of audience we need to reach? Is there somebody who’s ‘DH curious’ but not at the point where what we published would be useful? What would be useful to that person? What if we walked them through from the beginning what it’s like to have a question, then consult with friends about what to use?”

“What if it’s something that explodes out?” Maria proposed. “Something with a clear argument that demonstrates something rich, nuanced, and beautiful. Because maybe you don’t want to read the whole narrative because you don’t care until you’ve got a demonstration of what it can do.”

“There’s the way the process happens, then there’s the way you narrate that process,” Lee noted. “Usually we start with a question, we walk through a process, then further questions. We could write the book in a different way: a question, tl;dr, pointer to computational things, conclusion.”

“We can do it any way we want, it’s not like this is going to be peer reviewed and published in PMLA,” Roopsi noted.

“But it goes to the question of why we’re here,” said Maria. “For me, what’s interesting are equity issues. Who’s going to be in a position to read and engage with different kinds of tech tutorials? How many institutions have a digital librarian who can offer you tools? Certain ones. Certain elite ones. For people who are curious or who want to think about DH, most places are very under-resourced. People want to see if it works for things they care about, and if they’re interested, **then** figure out how to do it.”

“We need a Little Sister series,” Roopsi concluded.

“Ugh, no one likes Karen. Let’s just do Super Specials,” I muttered, but Roopsi continued.

“We can show what’s possible in a way that whets people’s appetite, linking to other things we’ve written.”

“Yeah, what if we take some books that have done really good walkthroughs,” Maria started, “take the things we’ve found at the end, and turn them into a short post that…” 

“I think we should do this, but I also want to say that I don’t think the value is to say to, like, a literary scholar over in the English department, ‘Look, this method would do a thing for you’,” Roopsi interjected. “I think the value of DH is the fact that when you’re engaging with the tools, that actually generates new ways of thinking and new questions about the **text**.”

“Yeah,” added Anouk. “The tools can distort and deform the text in a way that gives you a new vision of that text, and can actually show you what a prejudiced close reader you are, like when the things that jump out at you from a text turn out to be the things you happen to care about.”

“You’re making this argument, but you also can’t give an example of how computational text analysis is a good tool for literary studies,” Maria said firmly.

“I’m not sure it is,” Roopsi shot back.

“We’re going in a circle, people,” Maria sighed.

“People come to DH and they bring their own expectations about the study of culture and literature, and they expect there’s some way to operationalize it,” said Roopsi. “And I did this with my Pan-African project: I got all this data, and tried to make a network visualization of people involved in different conventions, but it turned out that most people went only once. And I called up Quinn and was all ‘Boohoo, I spent so long working on this data set and it didn’t work’, and Quinn reframed the question and solved my problem and it’s all good now. I remember in grad school where there were people who cared about theory first, who wanted to take theory around and theory everything with whatever theory they cared about. But then there were people who were interested in text, and big questions, and would see which routes of theory the text led them to as a way to get there. Neither approach is better than the other. But people want to treat DH as a tool hammer, sort of like a theory hammer.”

“I hate both of them,” said Maria. “What’s useful is the interaction in-between the theory and the text, or the tool and the text.” 

“I think we have a handle on the DH-curious audience, or people who are trying to teach DH. The question is, who are the other audiences that could or should be served better by the project?” asked Roopsi, getting back to the big question.

“My thought would be humanities faculty and admins, especially at less-resourced places, who are anxious that their students need to learn ‘tech’ but want them to learn humanities. Many think DH can help with that, but most have no concrete sense of what that would look like,” Maria said.

“That’s it, but how can we show that?” Roopsi asked. “As Lee mentioned, our books mimic the structure of a book, with a plot. What would be effective communication with that other audience? ‘Here’s how it went, would you like a longer story with a plot’?”

“I think we should put the exciting knowledge and analysis that comes out of the interaction between computational findings and more traditional humanistic methods first. That’s what gets humanists, it’s why most of us do this. And then maybe ‘here’s an activity you can try in your class, with an out-of-the-box tool to think about what a digital tool even is.’ Like a super-simple Voyant project where you pull off headers and footers of a text to understand, ‘Oh, that’s what it means to prepare data for a digital tool,” Maria proposed. “I’m thinking about reaching undergrads, and people who have zero idea of what DH work looks like. Can we help them understand the very basics of what these things mean – which would then put them light years ahead of most other humanists in terms of talking to people in engineering and tech.”

“Like, can we get them to slow down enough to think about structuring data before batch uploading?” lamented Lee. “It’s always rush rush rush because ‘I want to start doing the work,’ when that **is** the work.”

“It takes a decade to get that data structuring is an intellectual task,” sighed Anouk.

“I’m talking about copying and pasting stuff into a box in Voyant,” said Maria. “Deep dives are great, but there’s people who need the most basic connections, just enough to decide if they want to go further with it. That already is an enormous service.”

“So what if we do a Data-Sitters Little Sister and rebrand it, with Karen as the feckless example?” proposed Katia.

“Let’s not treat our primary audience like Karen,” said Maria, warily.

“Karen is the test subject?” Katia tried.

“Also, **Karen**,” Roopsi grimaced, and we all did the same. Obviously that slang for a certain kind of entitled, pushy white woman wasn’t around when Ann M. Martin created that character, but it was a prescient choice of name. Karen would have totally grown up to be a Karen.

“So this is for people who have bought into DH on some level. It’s an intro to the intro,” Roopsi attempted to recap.

“But no one wants tutorials unless they’ve decided they want to be connected to this,” Maria added. “There’s still a gap here: most people in this room already want to do this and are naturally excited about it. But most people outside this room are stressed about tech, and worried, and they want this for their students – how many of them are brilliant but claim to be tech-stupid and can’t even with something like DH?”

“All of them,” said Katia.

“All of them,” Lee agreed. “Dealing with the consequences of that is literally my job.”

“Is it that they can’t though?” offered Maria. “They’ve decided it isn’t interesting, plus it’s intimidating, so they won’t invest the time. If you’re scared and interested, you’ll probably still try. But if you’re scared and not interested, it’s easier to say, ‘I’m dumb, you do it.’”

“It’s ‘here’s what this can help you do’,” suggested Roopsi. “More than ‘this is how to do it.’”

"Miriam Posner had that ['How Did They Make That?' series](https://miriamposner.com/blog/how-did-they-make-that/), but even those were challenging when I first started," noted Katia. "What about if we do something that riffs on our other books, but even more basic? How would we make it more accessible?"

“I think we may have some books we’ve already written that could be turned into something like that – we can remix them, without redoing the whole method,” Roopsi suggested.

“I like that,” said Lee. “When I read the DSC books, I skip over the tech part. My eyes glaze over – like, I’m with you on the first step, second step, third step I’m lost… I trust Quinn, I basically know what she’s doing there, and then I can take a step back and say yeah, the French NLP data is problematic, what even is a French name? Let’s do a massively condensed version where we don’t bury the lede.”

“Like Lee was saying before, ‘tl;dr’ is a good way to describe the Baby-Sitters Little Sisters series,” Katia quipped. “Let’s run with that!”

## Meet Data-Sitters Little Tl;dr
And that – with some refinement over the 32 hours that followed – was how the Data Sitters Tl;dr was born. If you are (or know someone who is) part of the audience we were describing, where you’re not so committed to DH or any particular tool or method that you want to read through our books or work through in-depth technical tutorials, go check it out and let us know what you think.


## Suggested citation

Bessette, Lee Skallerup et al. "DSC Super Special \#1: The Data-Sitters Debate at Dartmouth". September 23, 2024.