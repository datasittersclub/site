# DSC \#18: The Data-Sitters' HathiTrust Mistake

```{index} single: *Book Topics ; HathiTrust (DSC 18)

```

by Cadence Cordell, Quinn Dombrowski, and Glen Layne-Worthey

November 10, 2022

<img src='_static/images/doi_logo.png' alt='DOI logo' height="20px" /> https://doi.org/10.25740/wr486nr4873

<div style="float: right; width: 300px;margin-left: 7px;margin-top: 0px;">
<img src="_static/images/bookcovers/dsc18_cover.jpg" alt="DSC 18 book cover" />
</div>

## Dear Reader

```{index} single: HathiTrust ; as metaphorical New York City

```

_In BSC 18: Stacey’s Mistake, Stacey McGill – born and raised in New York City, who briefly moved to the suburbs of Connecticut, and recently returned to the city – invites her friends from Stoneybrook, Connecticut to visit her in NYC. It goes badly._

_The Baby-Sitters’ misadventures remind me of the parallels between New York City and [HathiTrust](https://www.hathitrust.org/). They’re both huge and famous, and the people who are from there (or who have done substantial work with HathiTrust, like [Ted Underwood](https://tedunderwood.com/ted-underwood/)) make it sound mind-blowingly cool._

_But if you’re not from there, you might have a different experience. Maybe, like Dawn, you’ll feel a little bit scared of it all. Or maybe, like Kristy showing up in her collie baseball cap, you’ll stick out like a sore thumb, looking for texts that HathiTrust doesn’t have. Maybe, like Claudia, you’ll arrive with a clunky wheeled suitcase – or the tool equivalent that doesn’t play well with the data capsule._

_The takeaway from Stacey’s Mistake isn’t that New York City is a terrible place – or that it’s just bad for certain people. The book grapples with the chasm between expectations and reality, from all sides. It’s in that spirit that we’ve written The Data-Sitters’ HathiTrust Mistake: to share what we found we could and couldn’t do, and leave you better-informed for future trips to the metaphorical NYC of HathiTrust._

## Quinn

### What's HathiTrust?

```{index} single: HathiTrust ; pronunciation

```

HathiTrust. For starters, it’s a DH shibboleth. The first word is pronounced like “haughty”, because the name comes from the Hindi word for elephant (हाथी), as depicted in the organization’s logo.

```{index} single: HathiTrust ; as legal benchmark for text analysis

```

HathiTrust is also a crucial benchmark for legally-permissible computational text analysis at scale. When we put together petitions for exemptions to the Digital Millennium Copyright Act, we're able to reference what HathiTrust is legally allowed to offer researchers (after winning the [Authors Guild vs. HathiTrust](https://en.wikipedia.org/wiki/Authors_Guild,_Inc._v._HathiTrust) case), in order to not have to make the case from scratch that computational text analysis and sharing derivatives that don't permit the reconstruction of the source text should be permissible at all. Reading through the copyright register's recommendation on our latest DMCA exemption petition (starting on [p. 105 of this giant PDF](https://cdn.loc.gov/copyright/1201/2021/2021_Section_1201_Registers_Recommendation.pdf) -- you can also read more about the new DMCA exemption in [DSC 14](https://datasittersclub.github.io/site/dsc14.html)), the analysis of the issues at hand made multiple references to how HathiTrust allows researchers to access in-copyright texts. The existence of HathiTrust is a boon to scholars doing computational text analysis in the US, whether or not they actually use it.

```{index} single: HathiTrust ; memories of its founding

```

I have fuzzy memories of the founding of HathiTrust, around the same time I was the most-junior member of the [program staff of Project Bamboo](https://doi.org/10.1093/llc/fqu026), a Mellon-funded DH cyberinfrastructure extravaganza that crashed and burned dramatically. I have much clearer memories of the launch of the HathiTrust Research Center (HTRC), a partnership between HathiTrust, the University of Illinois, and Indiana University in 2011.

```{index} single: HathiTrust ; reception for HTRC at DH 2011

```

![Image of HTRC logo and red tablecloth at DH 2011](_static/images/dsc18_htrc_reception.jpg)

There was a toast to this promising new venture at DH 2011 at Stanford University. I took a picture at that reception, where people with swag had claimed space on tables with bright red tablecloths, and the HathiTrust logo is there in the background.

```{admonition} Glen says...
   <div style="float: left; width: 100px;margin-left: 7px;margin-top: 0px;"><img src="_static/images/dsc18_glen_on_elephant.png" alt="Pixel art of Glen Layne-Worthey riding an elephant with books on its trunk" /></div>

   "Fun fact: As the organizer of DH 2011, I can tell you that not only was it a toast to HTRC, but John Unsworth -- then the dean of the Graduate School of Library and Information Science, and the founding co-director of HTRC -- sponsored that whole fancy reception precisely in order to stage the official launch!"
```

```{index} single: HathiTrust ; Emergency Temporary Access Service

```

```{index} single: HathiTrust ; use by Ted Underwood

```

And that's where HathiTrust and the HTRC have stayed in my life for the decade or so since. I know they're there. I'm happy about their existence. I know people who have used them. Sometimes they've crept closer: one of the final concepts for Project Bamboo involved retrieving texts from HathiTrust. And there was the pandemic lockdown, where the HathiTrust Emergency Temporary Access Service was both invaluable for accessing a number of books remotely, and also flat-out excruciating for the slow and tedious process that was involved. There was the time when I worked at Berkeley, where I knew a postdoc who had gotten a grant to try to develop a DIY version of HathiTrust's "data capsule" for enabling research on in-copyright texts without granting scholars access to the files directly. And probably two or three times, I tried to read through the documentation and actually do something useful with the data capsule myself -- if only to understand how exactly the thing worked. Every time I walked away befuddled and mildly irked, concluding that [this](https://doi.org/10.3115/v1/p14-1035) [thing](https://doi.org/10.1177/2053951715602494) [might](https://doi.org/10.1215/00267929-3570634) [work](https://doi.org/10.22148/16.005) [for](https://doi.org/10.22148/16.019) [Ted](https://doi.org/10.1353/elh.2018.0013) [Underwood](https://arxiv.org/abs/1807.00181) but it wasn't going to work for me.

When my friend and colleague Glen Layne-Worthey left Stanford after 20-some years for a new gig as the associate director for research support services at HTRC, I gave myself the New Year's Resolution that finally, I would put in the effort to figure out how this thing worked. Except the new year in question was 2020, and all plans lay smashed into glass shards of despair as of mid-March. But I didn't forget about it, and in the fall 2021 push towards the so-called "new normal", I seized the chance to sign up for the four-part, eight-hour workshop HTRC was offering.

It was time to face my fears and stare down the elephant.

### The corpus

```{index} single: HathiTrust ; corpus size

```

HathiTrust is massive: over 17.6 million volumes. Yeah, it's mostly English, but of the [volumes with language metadata](https://www.hathitrust.org/visualizations_languages), English is just barely a majority at 51%. There's over half a million volumes in French, about a quarter-million each of Italian and Japanese, nearly 3,000 volumes of Macedonian, 17,000 volumes of Ukrainian, and almost 30,000 volumes in each of Thai and Turkish. When I think of HathiTrust, novels are what I imagine first, but they also have serials, journals, scholarly monographs, books in all subject areas, directories, legal documents -- basically anything and everything you'd find in a large research library, because that's precisely where everything came from.

```{index} single: HathiTrust ; corpus sources

```

One of the nice things about the Data-Sitters Club is the way we've been able to mostly sidestep questions of corpus composition. What does our primary corpus have? All the _Baby-Sitters Club_ books by Ann M. Martin. All of them. The Mysteries, the Super Specials, California Diaries, Friends Forever -- if it has to do with Kristy Thomas and her friends, we have it. That's great for answering questions about that series (especially within the context of its own world-making), but for most computational text analysis and DH research, including any broader questions we want to ask to situate this series in different contexts, things aren't that simple. You need to put a lot of thought into how you construct your corpus, and it's very rare to be able to get all of **anything** the way we've gotten all the _Baby-Sitters Club_ books. The points Roopsi makes in her book _New Digital Worlds_ about the gaping holes, silences, and omissions in colonial archives shaped by the priorities and interests of empires also apply to HathiTrust. 17 million items feels so immense it's tempting to think it's got to be comprehensive. But you can't forget about how it came to be. HathiTrust is the recipient of data from the Google Books project, which scanned millions of books held by libraries at (mostly) US-based research institutions; from other mass-digitization projects like those of the Internet Archive (still active) and Microsoft (shuttered in 2008), as well as libraries' own local digitization workflows. The whole process was (and is) a bit of a hodge-podge, and there's tons of duplication . But before you start worrying about how Google decided to include this or that book, you shouldn't forget about another set of underlying selection factors that systematically disadvantage certain genres, such as romance, pulpy sci-fi, and children's and YA books: the books had to be held by a research university library. This has major implications, as we anticipated -- and our Junior Officer Cadence quickly discovered.

```{admonition} Glen says...
   <div style="float: left; width: 100px;margin-left: 7px;margin-top: 0px;"><img src="_static/images/dsc18_glen_on_elephant.png" alt="Pixel art of Glen Layne-Worthey riding an elephant with books on its trunk" /></div>
   "The books also had to be on the shelf when Google hoovered its way through the stacks picking up things to scan!  We believe this accounts for some very popular books that are held by libraries but are still missing from HathiTrust.  Octavia Butler's novels are maybe the most famous example of this."
```

You've probably already met [Cadence Cordell, our amazing summer intern in DSC 17](dsc17.md). (If not, check out her book on her first visit to the archives with the Ann M. Martin papers!) When she wasn't digitizing book synopses or making surprise discoveries in the correspondence, we asked her to see what she could find in HathiTrust that might be of interest to the Data-Sitters Club, after connecting her with my YRDL co-founder Nichole Nomura to talk through how to think about corpora.

## Cadence

```{index} single: HathiTrust ; lack of youth literature

```

As of summer 2022, there are only 6 books by Ann M. Martin in HathiTrust, and not a single one is a Baby-Sitters Club book. (One is ["Karen's Worst Day" from the Baby-Sitters Little Sisters](https://catalog.hathitrust.org/Record/003880848?type%5B%5D=author&lookfor%5B%5D=Martin%2C%20Ann%20M.&filter%5B%5D=authorStr%3AMartin%2C%20Ann%20M.%2C%201955-&ft=) spin-off -- shout-out to the University of Michigan for that one.) Considering other series contemporary to the BSC, there are 7 books by R. L. Stine (all post-2000), and 3 books by Francine Pascal: one Sweet Valley Twins book, one Sweet Valley University book, and one standalone novel from 1979.

The absence of these titles is initially surprising, considering how popular these series were and how many books were published. (There were over 200 BSC titles, not including the Little Sisters spinoff, close to 200 Sweet Valley titles, and over a 100 Goosebumps books). The BSC and Goosebumps series are both undergoing revivals, with television adaptations, comic adaptations, re-releases ...

```{index} single: Youth literature ; undervalued by academic institutions

```

But historically, children's and YA literature has been looked down on, or at least undervalued, by academic institutions. YA literature in particular has had a complicated history. The genre didn't exist until the 30s and grew massively in the 1940s, as the very idea of a "young adult" came into prominence and publishers' began treating teens as a market in their own right. (I recommend reading _Young Adult Literature: From Romance to Realism_ by Michael Cart if you're interested in learning more about the history of what is--debatably--a genre.) However, classrooms and libraries sought to curb the spread of YA. YA wasn't viewed as literature, but as cheap mass-marketable fodder. It was formulaic, repetitive, and uninteresting.  "Good literature" meant adult literature. This viewpoint persists today - while YA is recognized with more respect, children and teens are pushed to read older, "more adult" literature, even if that isn't what appeals to them, and college-age adults are criticized for reading "below their age".

This history is reflected in university libraries. Children's and YA literature are often excluded from collections, or are under-prioritized. Research libraries seek to keep their collections relevant and to keep materials circulating, and YA literature like the Baby-sitters' Club series seems much less relevant compared to updated textbooks, non-fiction, periodicals, and other literature. Plus, YA literature risks becoming outdated very quickly (think of how many books with the internet as a prominent theme or plot device are outdated today), and it can be a struggle for libraries to justify purchases that will become irrelevant in a matter of years. So it's not entirely surprising that books like the BSC series or Goosebumps are underrepresented - they were viewed as "formula fiction", and not super valuable purchases for a university library.

## Quinn

```{index} single: HathiTrust ; as future home for DSC corpus

```

There are other routes for books to get into HathiTrust, though it's not easy. The books still have to be owned and scanned by university libraries: there's no way for individuals or research groups to donate texts that they've painstakingly scanned and OCR'd. Researcher interest in popular culture has made it easier for libraries to invest resources in digitizing material that they may have previously seen as outside their scope. There's a big project underway, led by Temple University, to scan and accession into HathiTrust a large corpus of 20th century pulp sci-fi novels. And much as I love to bask in the glory of our multilingual Baby-Sitters Club corpus, we've decided its final home will be the University of Illinois, where we'll donate it with the condition that it be scanned and added to HathiTrust. When that day comes, anyone will be able to run the code we've written for the Data-Sitters club on our multilingual corpus[^*] -- but I can't promise even that will be comprehensive, due to real-world impositions of time, money, and book availability on the second-hand market.

[^*]: That said, you may not get exactly the same results. All the books will be re-scanned and re-OCR’d, and odds are there’ll be more OCR errors in the HathiTrust versions than in the ones we’ve proofread.

```{index} single: Corpora ; finding one for your research question

```

All of which is to say, one of the most important (and potentially time-consuming!) steps in doing this work is defining a corpus that is reasonable and makes sense to answer the question you're trying to ask. But there can be a chicken-and-egg problem here: sometimes you don't exactly know what question you want to ask. You might have a broad theme or topic, like "the reception of the Baby-Sitters Club". There's a lot of different paths you could take and specific questions you could ask under the broad umbrella of that topic! You could look at the [BSC Snark Livejournal](https://bsc-snark.livejournal.com/). You could look at [fanfic](https://archiveofourown.org/tags/Baby-Sitters%20Club%20-%20Ann%20M*d*%20Martin/works). You could look at recent news articles and reviews of the 2020-2021 Netflix series or graphic novel adaptations. The data for all of those angles is relatively easily available on the internet. But what if you want to go back in time, and look at how the books were initially received?

You might find yourself doing some exploratory work somewhere like HathiTrust.

```{index} single: Corpora ; importance of domain expertise

```

Now, if you don't know the landscape of the kinds of materials you might be looking for (e.g. journals with book reviews for school librarians), ideally, you should go find a collaborator who does. I've been lucky enough to work with Nichole Nomura, who's getting her PhD in English and Education at Stanford, and her advisor on the Education side, Jennifer Wolf. Our adventures trying to trace the Baby-Sitters Club in The Horn Book, a magazine and set of book reviews "to herald the best in children's literature" are a story for another DSC book. But what you don't have collaborators with a knowledge of the disciplinary landscape? You can still -- as an exploratory step towards formulating a question, at which point you may need to re-evaluate your corpus -- dip a toe in the waters of what you can find if you just search HathiTrust. We know we're not going to find the books, but there's a wide variety of other sources that might hint at their reception and speak to the cultural and historical context of their publication: things like book reviews, newsletters (e.g. [Access Library of Michigan](https://catalog.hathitrust.org/Record/002647339)), essays and critiques (e.g. _[American Families in Fact and Fiction: Decentering a Constrictive Ideal](https://catalog.hathitrust.org/Record/102463002)_ by Juli Barry , 1998). There's also bibliographies, like a New York Public Library publication entitled "[Books for the teen age](https://catalog.hathitrust.org/Record/000061341)", with issues from 1948 through 2007, or one geared towards young readers themselves, _[Book crush :
for kids and teens : recommended reading for every mood, moment, and interest](https://catalog.hathitrust.org/Record/009427343)_ by Nancy Pearl, 2007.

You just need to be very careful about any claims you make off a corpus that has been thrown together as haphazardly as "all the HathiTrust search results for this term". It's not a reason to **not** try out that approach, especially if your research project is still at the point where it can be summed up with the question "So what's the deal with X anyways?"

## Cadence

```{index} single: HathiTrust ; creating a workset

```

### Creating a workset

There are several ways to create a _workset_ in HathiTrust, but one of the simplest is to make a _collection_ first. Head on over to [the HathiTrust website](https://www.hathitrust.org/) and log in through your institution. (If you aren't a member of an institution with access, you can still search HathiTrust, create collections and worksets, and request data capsules, but only people at member institutions can access in-copyright texts as part of a Data Capsule.  More on that below.)

Once you're logged in, click on the Collections tab at the top of the page.

If you haven't made a collection yet, this tab will show you all the public collections currently available in HathiTrust.  (The display defaults to 32 "Featured Collections" that HathiTrust staff have identified, but if you choose "All Collections" in the filter on the left-hand side, you can see and interact with more than 7,700 different collections created by librarians, scholars, and basically anyone with a particular interest! These are completely unmediated and unremediated, so of course their quality, size, and seriousness varies widely.) Once you've made one collection, clicking this tab will show you "My Collections" first with the option of showing all other public collections. For now, right above the first collection listed, there is a bar with a search option on the left and a button for "new collection" on the right. Click the new collection button and a pop-up will appear.

![Screenshot of making a collection in HathiTrust](_static/images/dsc18_making_collection.png)

You’ll need to answer a couple short questions to create the collection - if you’re making your collection public, your answers will be visible to others, so if you want others interested in the same area of research to find your collection easily, make sure your responses are detailed. The questions include giving your collection a name, describing the purpose of the collection, and deciding whether or not the collection is public or private. (Note that, if you’re planning to use the collection to create a workset, you’ll need to make it _public_, at least during the workset creation step.) Save your answers, and you have your collection.

Now that we have a collection set up, let’s start adding sources to it. Either scroll up to the search bar at the very top of the page or return to HathiTrust’s home page. Before entering your first search term, make sure to turn off “full view only”, which limits your results to only out-of-copyright items. While that is useful for other forms of research or reading, our goal here is simply to pull as many references to the Baby-Sitters Club as possible, whether or not we have full access to those sources. Also, double-check that you’re searching full text and not catalog - you’re unlikely to find references to “Baby-Sitters Club” in the catalog records themselves, and this way you know for sure you’re looking for mentions of your keyword(s) in the full text of any source, not just in catalog records.

![HathiTrust search bar](_static/images/dsc18_search_bar.png)

When it comes to inputting the search term, make sure it’s in quotations (especially if, like us, you’re searching for some common phrases - “baby-sitters club” is a search term that can turn up plenty of unrelated results), and even consider experimenting with the search term itself. As it turns out, two slightly different spellings of “baby-sitters club” resulted in two distinct search terms: “baby-sitters club” and “babysitters club”. A hyphen was enough to alter my results, so depending on what you're searching, varying up your search terms can be extremely useful. At the same time, be careful! Without full-text access to many sources in HathiTrust (over 60% of which is in copyright, and for our topic closer to 100%!), you have to do a bit of work with blinders on. It becomes a guessing game - what kind of sources can I reasonably expect to discuss The Baby-sitters Club, and which are news articles about real-life baby-sitters’ clubs, and so less relevant for our topic? Luckily, search results for “baby-sitters club” are pretty easy to filter, as a lot of the results are tagged as children’s literature or publicity or so on, but even then I made a few errors. I made the (pretty foolish) mistake of initially forgetting to limit my search to everything published during and after 1986, and accidentally pulled in some of the aforementioned newspaper clippings about real-life clubs. Other search terms, depending on what they are, can create a much more difficult puzzle to solve.

There are options to control what types of sources you get as results. Clicking the “Advanced Full-Text Search” link below the search bar lets you input multiple search terms at a time (useful if you’re using a wide array of search terms), as well as allowing you to limit the date of publication to a particular time range, the language of the source, and even the format. Once you’ve entered your search term, you also see similar options along the left side of the page.

![Screenshot of HathiTrust fulltext search](_static/images/dsc18_fulltext_search.jpg)

Some of the options from the Advanced Full-Text Search are still present after you’ve entered the search term, such as language and date of publication (though the date of publication option is trickier to control on this page, as the filter limits options to ten-year or one-year time spans and doesn’t allow for the customization available in the Advanced Search). New filters allow you to control by subject (which, in the case of the BSC, helps us limit results to “literature” if we were just looking for the BSC books), by author, and by the location where the source is originally from. Combined, these filters give you more fine-grained control over your searches and should keep some unrelated results from creeping into your collection.

Once you’ve entered your search term and filtered out any unwanted results, you can start adding things to your collection. There are a couple ways we can add things, so let’s start with the slower method of adding sources. If you’re unsure what kind of source you’re looking at or if it’s relevant to the collection you’re making, this is the method you’ll want to start with.

When you scroll down through the list of results, you’ll notice each one has two links below it. These links vary depending on whether or not a text is in copyright, and if so, whether your institution has full-text access to it (which was generally only the case during pandemic-era library closures, when the “Emergency Temporary Access Service” was created for books of which your library owns a copy). If you don’t have full access, then the two links will read “Catalog record” and “Limited (search-only)”.

![Screenshot of HathiTrust limited access links](_static/images/dsc18_limited_links.jpg)

Start by clicking on the “Catalog record” link. You’ll be taken to a new page which includes a bunch of metadata about the item in question, including its author or authors, the language it’s written in, where and when it was published, the subject matter, its ISBN, its physical description, and what source library it was originally from. Out of all of these, I found the metadata for the subject to be the most helpful, as it included multiple subject tags referencing children’s literature, children’s libraries, and so forth, but your needs will vary depending on your research. To add the source to your collection, either scroll down to the Viewability section (sometimes known as the holdings statement) at the bottom of the screen, which includes both a “Limited (Search-only)” link and the original source. Either click on the “Limited (search only)” link here or return to your initial page of search results.

I should note - depending on the type of source, scrolling through the Viewability table might be challenging. While some sources like the one above have relatively short Viewability tables, others for periodical publications or reviews have extensive Viewability tables that are difficult to navigate for the exact source you initially clicked on.

![Viewability status of results](_static/images/dsc18_viewability.jpg)

This process is slightly different if the source in question lets you full view source. The “catalog record” link is largely the same, but the “limited (Search only)” link has been replaced by “full view”. Clicking on the link takes you to a different-looking page. [add photo of full view only image here] While the left-hand sidebar is still there, a digitized version of the source now fills the other 2/3rds of the screen, in a reading tool called “PageTurner”. In the left sidebar you can search for keywords in the text, as well as add the source to your collection by clicking on the corresponding drop-down menu, selecting the right collection, and clicking the add button.

As I’ve gone through these methods, you might have noticed a third, faster way to add sources to your collection. If you’re pretty sure a source is relevant to your research without checking its metadata, then you can add it to your collection right from the initial search results. You’ll notice that there is a checkmark box to the left of every result. If you click on this box and scroll to the top of the page, you’ll notice a dark gray bar across the screen with a drop-down menu to select a collection and an “Add” button to the right of it. Selecting a collection and clicking the “add” button also adds sources to your collection. If you want to add everything on that page of search results, you can click the “select all” box to the left in the gray bar, then again select a collection and click the “add” button. Just be careful and double-check that you haven’t included some erroneous sources, as that risks skewing your later findings.

Now that we have our [collection of BSC References](https://babel.hathitrust.org/cgi/mb?a=listis&c=727671049), we can use it as our workset - or at least, that’s the plan. We still need a couple more things, starting with the full text.

## Quinn

### Accessing text in HathiTrust

```{index} single: HathiTrust ; extracted features

```

#### Extracted features

Sometimes HathiTrust reminds me of a genie: you've got to be careful -- and moreover, **specific** -- with what you ask for. Did you know that anyone, whether or not they belong to a HathiTrust member institution, can download the text from every page of 17.1 million volumes in HathiTrust, including over 10 million in-copyright works? It's called the [HTRC Extracted Features Dataset](https://wiki.htrc.illinois.edu/pages/viewpage.action?pageId=79069329), and it comes in zip files. Each zip file has an _ids.txt_ that tells you what each file ID is. The file IDs appear as .json.bz2 files (which is another form of compression); unzipping one will get you a sizable json file with metadata about the file, and then information for each page. That information includes how many tokens (e.g. words) are on the page, how many lines there are, how many empty lines there are, how many sentences there are, and then you get all the words on the page, and their part-of-speech (using [Penn Treebank](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) tagging) as labeled by Apache OpenNLP. Sounds amazing, right? And it is! ... with a catch. The tokens are in a random order. The part-of-speech labels were added before the words were shuffled, so you can tell the difference between "play" the theater production and "play" the verb. But there's more to meaning than part-of-speech: we need some representation of **syntax** to be able to tell the difference between "_Stacey's Mistake_ by Ann M. Martin sucks and _Hatchet_ by Gary Paulsen is inspired" and "_Stacey's Mistake_ by Ann M. Martin is inspired and _Hatchet_ by Gary Paulsen sucks".

But the problem is that syntax is a key to reassembling the source text, and the only reason HathiTrust can legally put copyrighted materials in the extracted features dataset is because it's in a form where users **can't** reassemble that source text. There are questions that the extracted features dataset can answer, but "what did people have to say about _The Baby-Sitters Club_ when it was released" isn't really among them.

```{index} single: HathiTrust ; extracted feature algorithms

```

#### Algorithms

Instead of making everyone download the whole 4 TB (compressed) Extracted Features Dataset and wrangle it into submission, the good people at HathiTrust have put together a set of algorithms to make it easier to do common things with a subset of their data. There's one that lets you download the extracted features data for just the volumes you're interested in, there's a [topic model explorer](https://inpho.github.io/topic-explorer/) you can use with your workset, along with a named entity recognizer if you want to extract named entities (like people and places) from your workset (we've talked about named entity recognition in [DSC Multilingual Mystery 2](https://datasittersclub.github.io/site/dscm2.html)), and also a token count / word cloud creator algorithm for your workset.

To run any of these algorithms, you need to log into the [HathiTrust Analytics](https://analytics.hathitrust.org/) site with your institutional credentials, then select "Algorithms" from the top nav bar. (Independent scholars, or those whose institutions aren't members of HathiTrust, can still use these algorithms, but the process for creating a non-institutional account is a little more involved, and requires manual approval that can take up to 24 hours.)  Choose the algorithm you want to run, choose a workset (you can search by title and/or workset creator), and then do any additional algorithm-specific configurations. For instance, for named entity recognition, you need to choose the primary language of your data (if it's not English, French, Arabic, Chinese, German, or Spanish, you're out of luck). Then hit "submit", and it will take you to a "Jobs" page where you can see the status of your job. How long it takes depends on how big your workset is, and how busy the compute resources are.  You'll be notified when your job is complete, at which point you can log in again and retrieve your results.

```{index} single: HathiTrust ; data capsule

```

### Data capsule

If you want to access _text_ available through HathiTrust – and I mean _text-text_, what literature scholars think of when they think of text, not word frequencies with part-of-speech data – what you need is something called a “data capsule”. As Cadence noted above, anyone can request a data capsule, but you have to be affiliated with a HathiTrust member institution to access in-copyright texts in a data capsule.

A data capsule is a virtual machine -- just like how Anastasia and I used a virtual machine to run the 90's Baby-Sitters Club computer game in [DSC 16](dsc16.md). It's a little window that appears inside a browser tab, like a portal into another computer with its own file system, software, etc. Unlike our BSC computer game adventure which ran on vintage Windows, data capsules run on a version of Linux called Ubuntu. Don't let the "Linux" scare you: Ubuntu has a point-and-click interface that's a lot like what you'd get on a modern Windows machine, so it should be mostly familiar.

Once you've logged into HTRC Analytics click on "Data Capsules" in the menu bar, then click "Create a Capsule". If you just want to play around a little with public domain texts, choose the "Demo Capsule" and you'll get access immediately. If you want to do actual research, go for the "Research Capsule" option.

```{index} single: HathiTrust ; research capsule application form

```

### The Research Capsule form

To get access to a research capsule, you’ll need to fill out a form and wait for manual approval. Heads-up: it could take a week or more for turnaround, especially if you’re asking for access to in-copyright materials. So much of DH can (and does) happen at the last minute, but getting access to a HathiTrust research capsule with in-copyright texts is like needing to drive from Stoneybrook, Connecticut to NYC in heavy traffic, in a snowstorm: you need to plan ahead, and be patient.

The form asks a lot of questions about what you’re doing – both big-picture and specifics – so it’s worth thinking through how you’re going to answer in advance, and maybe jotting down some sentences rather than typing everything from scratch into the form.

Let’s work through the form:

- **Title**: This is whatever you want to call your project
- **Data capsule image**: Go with the default; as of October 2022, that’s ubuntu-16-04. This is an older version of Ubuntu that may cause some challenges when you’re installing software, but it’s your best option when filling out the form.
- **VCPUs**: choose the largest number available (currently 4)
- **Memory**: choose the largest number available (currently 16); the first time I requested a data capsule, I went for more modest specifications, and the virtual computer ground to a halt when I tried to import all the books I wanted to work with!
- **Description**: “What is the nature of your research project, including your research questions and primary methodology?” This is a big one! You don’t have to have all the details worked out, and you can make some vague gestures towards “distant reading” if you need to. But you should have some ideas about the kinds of questions you’re trying to answer. If you’re not even sure about the questions, exactly, you can write a few sentences using the word “exploring” – exploring phenomenon X in Y corpus, exploring how X gets represented in Y type of thing, etc.
- **What outside data (non-HathiTrust) do you plan to incorporate into your analysis in this capsule**: This may not apply to your project, but if there’s some data you already have (e.g. because you’ve scanned and OCR’d it like we described in DSC 2) and you want to analyze it together with materials from HathiTrust, you can describe them here. If you are using outside data, you’ll need to upload them to the HathiTrust data capsule.
- **Please provide links to web-accessible documentation, tools, and/or code you plan to incorporate into your analysis in order to facilitate the review of your data export requests**: So here’s the deal with this one: a real, live, overworked but very nice person is going to manually look through the files that you ask to export from HathiTrust, to ensure that your “export” isn’t just the full text of all the in-copyright books or anything else that might get them or you into trouble with rights holders. This doesn’t mean that you need to have all your code figured out and posted to GitHub in advance, they just want some idea of what they’ll be dealing with. What you can say here, especially if you’re not entirely sure, is some of the things you’ll be trying. For instance, you can point to [AntConc](https://www.laurenceanthony.net/software/antconc/), or any of the [Programming Historian tutorials](https://programminghistorian.org/en/lessons/) or even other [Data-Sitters club books](books.md) (we’ve covered a lot of different methods) as things that you’ll be trying.
- **Important checkbox alert!** The first time I filled out the form, I missed the checkbox above the “Results release” section and got all confused. Check the checkbox for “Request Capsule with computational access to the full HathiTrust Corpus”, which will open another text field for you to justify the request! (Note that access to the “full HathiTrust corpus” doesn’t actually mean that you want all 17.6 million volumes! Instead, it’s just the ability to include in-copyright works among your corpus. Also note that access to in-copyright works here is a HathiTrust member benefit, so if you’re affiliated with a member library, thank your local librarian! And if you’re not, time for some good old-fashioned advocacy to your library to join.) Honestly, this is one of the easiest questions on the whole form: you can simply state that you need access to the full text because some of your analyses depend on syntactic information that’s not available through extracted features, and that your research is focused on in-copyright works. Done.

![Hermes Conrad from Futurama writing on a clipboard, animated gif](_static/images/dsc18_bureaucrat-writing.gif)

- **What derived data files do you anticipate requesting to export from your capsule? Please describe the file format and data structure. (Required)**: Again, don’t read this like the scary gatekeeping it might look like. There’s no specific “right answer” you have to put down, and, like me, you can just be honest here and say you don’t know yet, but you will send them more information when you request that your results be released. There’s no DH bouncer here – it’s just your colleagues in infrastructure support trying to get some sense of what they’re in for here. “I expect to be exporting a giant set of complicated and hard to review files on a weekly basis” is a very different scenario than “I might be exporting some keywords in context after a couple months of research”. And it’s okay to not know yet when you’re starting.
- **Describe all the ways that you intend to use the results of the research conducted in your capsule, including plans for public dissemination of any derived data you are permitted to release from your capsule. (Required)**: This one feels less like bouncer and more like bureaucrat. Really, does any researcher actually know all the ways they intend to use the results of any research? Even after they’ve finished the research, let alone when they start it? Don’t get stuck on that word – just write down what you have in mind, assuming you get some kind of meaningful results! Are you thinking a conference talk, maybe a paper? Are you going to write about it as part of a tutorial, or on a blog? Are you thinking you’ll share anything you export from your HathiTrust data capsule? And if so, what? Excerpts of text, aggregate statistics, etc.? Maybe it’s too soon to know all the details, so just tell them what you’re thinking in terms of how you might share results from the project you’re working on, and what things you’re still not sure about.

And then wait a while. Without angsting about whether HathiTrust will consider you worthy and let you in. Because almost certainly, the approval process will go something like this:

![Hermes Conrad from Futurama saying ok, animated gif](_static/images/dsc18_bureaucrat-ok.gif)

And you’ll get an email from a ticketing system saying you’ve been granted access.

```{index} single: HathiTrust ; launching the data capsule

```

### Welcome to your data capsule

You can tell that your request has been granted when you log into HathiTrust Analytics, go to the [Data Capsules page](https://analytics.hathitrust.org/capsules), and see a data capsule ID with the label Type: RESEARCH-FULL. To get it started, click on the green “Start Capsule” button to the right of all the labels.

You’ll see the status change to “LAUNCH_PENDING”. If it takes a couple minutes, don’t panic or give up! You’re still going to New York City – there’s just someone taking a left turn at a busy intersection up ahead. Relax, you’ll be back on your way soon.

Click the data capsule ID. As soon as the data capsule has launched, you should see a page where you have the option to “Connect via Terminal” and “Connect via Remote Desktop”. Here, we’ll be using the remote desktop option, which lets you point and click your way through your data capsule as if it were a regular computer.

Once you click through the pop-up box confirming that you’ll only use it for non-consumptive use (i.e. you’re not some kind of masochist who would want to try to actually read through sources using your eyeballs and the plain-text files available through a HathiTrust data capsule – which, truly, is one of the most unpleasant reading experiences I can imagine), you should see a screen like this.

![The desktop of a new data capsule instance](_static/images/dsc18_data-capsule-desktop.png)

When your mouse is hovering over the virtual desktop, it represents the cursor on that virtual desktop, though sometimes there can be a little bit of lag. But you’ve made it! You’re in the data capsule. So what’s next? Where are those texts you want to work with?

Learning to use the data capsule is a little bit like learning to navigate the New York City subway if you’ve never used public transit before. It’s not that it’s fundamentally _hard_, but if all you’ve ever experienced is cars driving you from point A to point B, you have to shift your perspective a little to wrap your head around it. It’s time to talk about data capsule modes.

```{index} single: HathiTrust ; data capsule maintenance mode

```

### Maintenance mode

By default, your data capsule starts in “maintenance mode”. Maintenance mode might sound like something you’d only need to upgrade the operating system or something, but you can think of it as something like “internet mode”. Do you need the internet to do something? If so, you need to be in maintenance mode. Some examples of things you’d need the internet for include downloading or installing software, or adding data to the data capsule from outside of HathiTrust’s collections – like if you’re doing research on HathiTrust and non-HathiTrust data together. If your software sometimes accesses the internet, e.g. for things like documentation or help files, that functionality will only work in maintenance mode.

What’s the downside of maintenance mode? You can’t access the HathiTrust data. The only way to download, view, or run any computation on data from HathiTrust is in “secure mode”. But there’s a catch: the command for downloading the data depends on your collection ID… which you need the internet to access. So let’s do some planning ahead before we switch to secure mode.

Click on the Firefox icon on the desktop’s left sidebar, and log in to hathitrust.org from within the data capsule. Because the data capsule is running on Indiana University servers, it’ll assume you’re from Indiana University when you try to log in, but you can easily change that by selecting your institution from the drop-down.

Once you’ve logged in, click on “Collections” in the top menu, and you’ll see the list of your collections. Choose the one you want to download texts from, and click on it. On the left side of the page that appears, you’ll see a box labeled “Link to this collection”. Double-click inside that box to highlight the text, then right-click (or ctrl + click) on the highlighted text, and choose “Copy”. Don’t confuse this link with the URL in the browser, which won’t work for this purpose!

![Getting the collection link within the data capsule](_static/images/dsc18_collection-link.jpg)

Next, click on the blue vertical desktop sidebar icon that looks like a word processing document to launch LibreOffice. (It’s like open-source Microsoft Word.) Right-click or control-click inside the new document that comes up to paste the URL that you just copied.

![Getting the collection link within the data capsule](_static/images/dsc18_collection-link.jpg)

Next, click on the blue vertical desktop sidebar icon that looks like a word processing document to launch LibreOffice. (It’s like open-source Microsoft Word.) Right-click or control-click inside the new document that comes up to paste the URL that you just copied.

![Getting the collection link within the data capsule](_static/images/dsc18_libreoffice.png)

Save the document to your data capsule desktop to make it easy to find.

Now that we have that URL in a way that we can access it even without network connectivity, it’s time to switch to secure mode.

```{index} single: HathiTrust ; data capsule secure mode

```

### Secure mode

Once your data capsule is running, right above the remote desktop window, you’ll see the option “Switch to Secure Mode”. Click on it. A pop-up will appear warning you about the limits to network access, the fact that you’ll only be able to access the HTRC data API (i.e. to download the texts you want) along with the standard warning about only doing non-consumptive research. Hit “Agree & Switch Mode”. You may have to wait a few minutes while you see “SWITCH*TO_SECURE_PENDING” displayed, but when you can once again access the virtual desktop, you’ll notice some changes: there will be two folders open, one called \_secure_volume* and one called _release_spool_.

_Secure_volume_ is where you save the texts that you download from your collection. Once you do your analysis, things that you want to get access to outside the data capsule go into _release_spool_.

```{index} single: HathiTrust ; downloading texts to the data capsule

```

### Downloading texts in secure mode

To download the texts from your collection and make them available in the data capsule in secure mode, choose the Terminal (black square) icon. This will pop up a command line window.

![Getting the terminal in the data capsule](_static/images/dsc18_terminal-command-line.png)

The template for the command we’re going to run to download the texts is this:
`htrc download [-hfc] [-o OUTPUT] [-c] [WORKSET PATH]`

Here’s how to break this down:

- Adding -f removes sub-folders, otherwise each volume (book) will be put in its own folder, which results in an awful lot of folders with a single file inside. You don’t want that.
- Adding -o and a path lets you define where the data will go. If you don’t include this, the data will go into /media/secure_volume/workset/
- Adding -c will concatenate the pages into a single text file, otherwise you’ll get one text file for each page in each book. An even better version is adding -hfc, which combines the pages into a single text file and tries to get rid of running headers and footers.
- Workset path: this is the collection URL we copied from the HathiTrust site

Putting it all together, this is what we’ll type (then paste, for the workset path) into the terminal:

`htrc download -f -o /media/secure_volume/workset/YOUR_PROJECT_NAME -hfc "YOUR_COLLECTION_URL"`

Be sure to put your actual project name instead of YOUR_PROJECT_NAME, and paste your collection URL from the OpenOffice document you created between the quotes.

Then hit enter, and once again… wait. If it’s working, you’ll see the number of megabytes tick upward. At some point, it will switch over to a more transparent accounting system, showing you how many texts out of how many in the collection it is downloading. You should expect this to take a while, even if you don’t feel like you have that many texts. Look, it’s just another New York thing. Just like how it takes a while to wait in line for Broadway tickets (especially for Stacey’s favorite show, “Paris Magic”), it takes a while to get access to the content you want in HathiTrust. At the end, you might see that some of the volumes aren’t available, but hopefully it’s a small enough number that it doesn’t particularly impact your project.

Once it’s finally done, go to the /media/secure_volume folder. It should be one of the icons in the left vertical sidebar. Click on it, and you should see a worksets folder, then the folder you created. Inside that folder should be a bunch of text files with cryptic names. That’s your data!

```{admonition} Glen says...
   <div style="float: left; width: 100px;margin-left: 7px;margin-top: 0px;"><img src="_static/images/dsc18_glen_on_elephant.png" alt="Pixel art of Glen Layne-Worthey riding an elephant with books on its trunk" /></div>
   "In case you need step-by-step driving directions on your way to the show, all of these steps are helpfully documented in a series of <a href="https://wiki.htrc.illinois.edu/display/COM/HTRC+Data+Capsule+Tutorial">bite-sized tutorials on the HTRC documentation website</a>"
```

### What do you do now?

Once you have your data, you're done with the HathiTrust-specific steps of your analysis. You have plain text files, just like we described as the starting place for this kind of work in [DSC #2](dsc2.md). The only difference is that you're not supposed to open the plain-text files and start reading them, but besides that, you can do pretty much anything we've described in any of the Data-Sitters Club books. (You're of course allowed to look at the text files to verify that the right books came through, or to do reality checks on your analysis, or to understand the context of whatever your algorithms are telling you!  Just don't use the data capsule for your book club reading. You're on your honor, and nobody is peeking over your shoulder!)  Jupyter Notebook comes pre-installed on the data capsules, so you could even download the code directly from the Data-Sitters Club site, and modify it to run on your files (located in /media/secure_volume/workset/YOUR_PROJECT_NAME).

Not sure where to start? Voyant comes pre-installed, and is a wonderful exploratory interface. If you've got some specific words where you want to look for the context, and export the results as text files that you can export from the data capsule, you might want to download and install AntConc.

Did you catch that word, though? "Download". Download means network connectivity, which means we have to switch back to maintenance mode. Arguably, it'd be more streamlined to get your tools set up as part of the first step when you were already in maintenance mode, but personally, I always make sure I can successfully get my data before I put in the time setting everything else up. Your mileage may vary, though.

```{index} single: AntConc ; installing on HathiTrust data capsule

```

### Downloading and installing AntConc

Switch back to maintenance mode; the data you've downloaded will disappear. (In case you're curious about what's up with where the data is located, it works like a USB drive that only can be "plugged in" when you're in secure mode.)

Open Firefox within the data capsule and head to the [AntConc website](https://www.laurenceanthony.net/software/antconc/). There's a totally new version since Anouk wrote [DSC #4](dsc4.md), but at the moment, the data capsule operating system isn't compatible with it. (It'll be upgraded eventually, but just like the subway system, sometimes these big infrastructures take some time to install all the shiniest new train cars across the whole system!) Instead, click on the Linux release of the AntConc 3.x series. The data capsule will ask if you want to open it with Archive Manager. Say yes, then in the window that pops up, click the "Extract" button. Choose the data capsule Desktop as the location; you should see that the extraction completed successfully. Click the "Show the files" button.

Double-click the AntConc icon, and AntConc will open. Switch the capsule back into secure mode. When it reloads in secure mode, within AntConc, go to File → Open file(s). Navigate to /media/secure_volume/workset/YOUR_PROJECT_NAME, and select all the files you want to open in AntConc. Then start querying! And... waiting some more. Because even once you've made it to New York, and gotten your tickets to "Paris Magic", you're still going to be in line for the bathroom during the intermission.

## Cadence

```{index} single: AntConc ; running queries in a HathiTrust data capsule

```

### Running queries

After inputting the term "Baby-sitters club" and running a query, I found the sources appearing were pretty much what I had guessed earlier on. The sources were primarily book catalogs, reviews, and references to the BSC in critiques or essays (either specifically discussing the BSC series or mentioning them in the context of other popular series of the 80s and 90s).

My results for "baby-sitters club" were interesting, though not unexpected. Most of the results were for catalogs or reviews focused on plot summaries or character descriptions. Some critiques or essays appeared to focus on the gendering of not just the BSC series, but other popular YA literature, and how the books were viewed by children and publishers alike. Another line of critique was focused on the series as "popular fiction" or "formula series", and how to push young readers to "better" content, mainly adult fiction.

```{index} single: Youth literature ; series books

```

The Baby-Sitters Club wasn't the most frequently mentioned book series in the workset. After running several queries for other series I thought were mentioned fairly frequently alongside "the baby-sitters club" (including Goosebumps, American Girl, Sweet Valley High, Boxcar Children, and Nancy Drew), as well as for different spellings of the Baby-sitters Club and its spinoff titles, I found the below statistics:

- "baby-sitters club" = 5039 references
- "babysitters club" = 640 references
- "California diaries" = 217 references
- "goosebumps" = 4657 references
- "Sweet valley" = 8846 references
- "American girl" = 2892 references
- "Nancy Drew" = 7757 references
- "Boxcar children" = 2992 references
- "Matt Christopher" = 1931 references

Nancy Drew and Sweet Valley in particular both had thousands more references than the Baby-Sitters' Club, and Goosebumps was a similarly popular reference. My curiosity was piqued - why these titles? Is it primarily because they featured so prominently in catalogs? Were the Sweet Valley High series and its spinoffs frequent sellers, or were there also essays and reviews deriding the books? Is Nancy Drew so prominent because of its age as a series, or is something else in play? I couldn't help but dive down the rabbit hole.

It turned out to be a mix of factors. Sweet Valley High's prominence seems to be entirely due to its quick publication rate and heavy marketing - most of the AntConc results were a wall of text of different catalog plot overviews.

Nancy Drew as a search query, on the other hand, seemed to be featured in more analytical pieces. Sifting through the AntConc results revealed a variety of attitudes toward the series. Some attitudes tended toward nostalgia, discussing reading the series as a child and its influence. Others deride the series and dismiss it as "popular" or "formula fiction" - both terms that would be used frequently in discussing most of the series I would search for in AntConc.

```{index} single: Youth literature ; Goosebumps

```

Goosebumps, surprisingly, had a number of references dealing with how the series handles rebellion. References moved between seeing the series as dangerous and fomenting rebellious behavior in children, to seeing the series as using the language of rebellion to control such behavior. It's an interesting line of thought, but unfortunately I didn't have access to the sources in question, so it wasn't a question I could explore much further.

That brings us to one of the difficulties using HathiTrust and AntConc for research - ultimately, you do not have full access to these sources.

```{admonition} Glen says...
   <div style="float: left; width: 100px;margin-left: 7px;margin-top: 0px;"><img src="_static/images/dsc18_glen_on_elephant.png" alt="Pixel art of Glen Layne-Worthey riding an elephant with books on its trunk" /></div>
   "More like you agree not to use data capsule for close reading, only for computational analysis - you do have access to whole file/source and can technically access the whole text, but you have already agreed only to do 'non-consumptive' research when you requested and entered your data capsule, and 'reading' is clearly consumptive!"
```

While this is fine for gauging attitudes toward a text or trying to gain a historical perspective on how something like the Baby-sitters Club was treated, it means you have no way of following up immediately on a source that seems interesting or useful. Without full access to the source in question, you have to hope it's one your university library might have (as not all libraries have donated their collections to HathiTrust, and even those who have donated parts of collections haven't donated everything) or you might be out of luck. You have to go off of what context you can glean from AntConc results and the source's metadata.  (There's always interlibrary loan, though!)

```{index} single: AntConc ; installing on HathiTrust data capsule

```

Furthermore, the limitations to access mean it's a struggle to search for any terminology not directly linked to the keywords you used to formulate your collection in the first place. One of the questions I was interested in researching was mentions of "diabetes" or "anorexia" in the BSC references collection, or other super special themes the series was known to bring up in certain issues. I quickly realized such a search was impossible. Diabetes was mentioned thousands of times in the context of other books in the same catalogs as Baby-Sitters Club titles, and it was impossible to tell if some references were about the BSC or other series. I struggled to find even a single instance where "diabetes" was mentioned in the same sentence as "baby-sitters club". This is the sort of situation where I would want full access to a title to find both search terms and see if there was a connection between them, but such a connection was impossible to establish using HathiTrust and AntConc.

```{admonition} Glen says...
   <div style="float: left; width: 100px;margin-left: 7px;margin-top: 0px;"><img src="_static/images/dsc18_glen_on_elephant.png" alt="Pixel art of Glen Layne-Worthey riding an elephant with books on its trunk" /></div>
   "There are some truly advanced search options that actually could get you pages like this in yet another HTRC tool called "Workset Builder" -- which does the same sort of workset building we described above, but in a more fine-grained fashion using a search tool with a somewhat steeper learning curve -- but that's a topic for another Data-Sitters Club book!  If you can't wait for that, you can try it out right now at <a href="https://worksetbuilder.htrc.illinois.edu/">https://worksetbuilder.htrc.illinois.edu/</a>."
```

## Quinn

```{index} single: Questions ; necessity of making compromises

```

### Research questions and compromises

I had some ideas for what I could do to get a better sense of whether "diabetes" and "baby-sitters club" occurred anywhere near each other in these texts. This would be easy enough to do with a little Python. But there's often this point in DH projects where you need to step back and ask yourself if you're still on the path you started on, and if not... do you care about this new set of questions enough for it to be worth continuing? This isn't just about HathiTrust: with any kind of text analysis project, you may find yourself making compromises. You can't access the data set you actually want? Well, there's this other one that has some things in common with what you were looking for. What about the question that you're trying to answer? Well, it turns out to be computationally very hard, and the alternative is to spend months going through your text manually. But here's a computationally-feasible proxy that sort of gets at some similar themes. Each compromise may seem like a reasonable and worthwhile one, but once you add them all up, you might realize you're quite far from anything that you actually care about. And let's face it: a DH project is a ton of work, and if you aren't actually interested in the outcome once you've made all the compromises ... it's okay to stop.

And that's what we did.

```{index} single: HathiTrust ; releasing results

```

### The eject button and the release spool

It’s not that the Data-Sitters Club isn’t interested in the reception of the series. I could try to make sense of the hodge-podge of Baby-Sitters Club references in assorted things that did make it into HathiTrust as a way into the question of reception, but doing that well would involve doing more research than I really wanted to into what the deal was with these sources anyway. Just because sources are available doesn’t mean it’s the right corpus for answering your question. And the lack of other middle-grade and YA texts also meant that HathiTrust was fundamentally limited in the kinds of questions we’ve been looking at with the Data-Sitters Club.

I didn’t want to lose the work that Cadence had done. Who knows, it might make for some interesting comparison down the road! And let’s be honest: storing your data in digital files (instead of physical papers and books that take up real-world space) makes it easy to be something of a hoarder. It’s not a great data management practice, but as long as you stash it in some kind of reasonable folder structure, I wouldn’t feel too bad about it.

Before angsting too much about where exactly to store the data, first we need to get it out of the data capsule. For each of the queries, we went to _File → Save_ output, and exported the results, saving the .txt files to the secure volume (/media/secure_volume).

To get the files from the secure volume into the release spool, open up a new command line and use this command with each file you want to get access to:

`releaseresults add /media/secure_volume/example_file.txt`

When you’re done adding all the files you want access to, in that same command line window, use the command:

`releaseresults done`

After some period of time (did I mention there's also a line for retrieving your coat from the coat check on the way out of a Broadway show?) for the HathiTrust staff to review your results, you’ll get a link in your email that you can use for 12 hours to download your results.

### Heading home from New York

What have we learned here? Well, the Data-Sitters are no Stacey McGill. HathiTrust – the New York City of text analysis corpora and environments – is **a lot**. But not necessarily in the ways we need. We leave this DSC book with a more realistic understanding of what it’s like to work with HathiTrust, to complement our respect for it as a legal precedent and as a piece of DH infrastructure. It’s still our best hope for making the Baby-Sitters Club – particularly in translation – more accessible to more people. If your research questions align reasonably enough with what HathiTrust has, be brave and make your own trip to NYC. But if not… well, we won’t judge you if you metaphorically just order your “I ❤️ NYC” t-shirt online, to show your support in principle without tackling the traffic yourself.

## Suggested citation

Cordell, Cadence, Quinn Dombrowski, and Glen Layne-Worthey. "DSC #18: The Data-Sitters' HathiTrust Mistake." _The Data-Sitters Club._ November 10, 2022. https://doi.org/10.25740/wr486nr4873.
