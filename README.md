# Building Software at Scale in the AI & Cloud Era

*The System That Builds the System*

<small>© 2026 Oleksiy Pylypenko · Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — share and adapt freely, non-commercially, with attribution. Source on [GitHub](https://github.com/oleksiyp/buildsoftware-book). Also in the series: [*Software Architecture in the AI & Cloud Era*](https://oleksiyp.github.io/arch-book/), [*Building Products in the AI & Cloud Era*](https://oleksiyp.github.io/buildproducts-book/), [*Building Resilient Systems in the AI & Cloud Era*](https://oleksiyp.github.io/resilienteng-book/) and [*Operating Production Systems in the AI & Cloud Era*](https://oleksiyp.github.io/prodsys-book/).</small>

## Preface

Every software company runs two systems. The first is the one its customers see: the pages, the apps, the services and the data that do the work they pay for. The second is the one that builds the first, and almost nobody outside the company ever sees it. It is made of the code and its tests, the build and the pipeline, the platform that services run on, the teams that own each part, the habits of review and the plans and budgets that decide what gets worked on next. When a company is small, the second system hardly needs a name, because it lives in the heads of a few people who sit together and can answer any question by turning around. When the company grows to hundreds of engineers, the second system decides how fast and how safely the first can change, and it does so whether or not anyone has designed it.

This book is about that second system. Its thesis is that the engineering system, the code, tools, platforms, teams and practices through which an organization turns an intention into running software and keeps changing it, deserves to be designed with the same care as the product it produces, and that at scale it is the larger determinant of what the company can do. A company of 400 engineers can attempt far more than a company of nine. Yet each of its changes tends to be harder, because each crosses more code that nobody fully understands, more teams that must agree and more queues where work waits. None of that happens by decision. It is the sum of thousands of defaults, each sensible on the day it was taken, and the work of this book is to find those defaults and replace the costly ones with practices that have been shown to work.

Our field has been asking how to do this for as long as it has had a name. In October 1968 the NATO Science Committee gathered more than 50 people at Garmisch, in the Bavarian Alps, and called the meeting *software engineering* precisely because the practice of the day did not deserve the word. Its participants argued over whether their predicament was a crisis, and they agreed that large systems built by large groups were arriving late, costing too much and failing in use. They also saw, more clearly than they are usually given credit for, that the trouble grew with the number of people as much as with the number of lines. What they lacked was a method. The half-century since has supplied a good deal of one: version control and automated tests, continuous integration, refactoring, internal platforms, team designs and forecasts drawn from what teams actually finish. The gap Garmisch named has narrowed. It has also moved. Writing code that works is no longer where large organizations mostly fail. They fail in understanding the code they already have and who depends on it, in the queue between two teams that no plan can see, and in the patience to delete what has been replaced. The last chapter of this book follows one change through all of that, and arrives at the view that the crisis named in 1968 has moved from construction to comprehension, and from the program to the organization that changes it.

AI assistance sharpens that view instead of overturning it. Code has become cheaper to produce than at any time in the history of the craft, and the cheapening is real; assistants write functions, tests and migrations in minutes, and agents carry out changes across many repositories that would once have taken a team a quarter. The cost of changing software, though, was never mostly the cost of typing it. Most of it lies in understanding the code that is already there, deciding what to change, reviewing and testing the change, integrating it with everyone else's and owning it for years, and those costs have not fallen with the cost of writing. Some have risen, because there is now more code to review and more of it was written by something that will not be on call when it fails. The evidence so far, which Chapter 5 examines and labels where it is young, finds the gains real, uneven and largest where the engineering system around the tools is already sound. That is why AI has one chapter of eleven here, and why the rest of the book is about the system that decides whether cheaper code becomes faster change.

The book is written for the people who build and shape that system: the engineer who has inherited a module nobody else understands, the tech lead whose team waits on three others for every release, the platform engineer whose portal stands half-used, the staff engineer asked to settle who owns what, and the engineering manager who must plan a quarter across a dozen teams and forecast its outcome to someone who wants a date. Each will find the practices they need, the history that explains why those practices work, and an honest account of where the evidence is strong and where it is thin.

The book belongs to a series that follows one fictional company from several sides. *Software Architecture in the AI & Cloud Era*, which these pages call the Architecture book{% include xref.html to="architecture" %}, asks how to shape a system. *Building Products in the AI & Cloud Era*, the Products book{% include xref.html to="products" %}, asks how to decide what the system should do. This book, the Software book, asks how an organization of 40 teams builds and keeps changing what has been decided. *Building Resilient Systems in the AI & Cloud Era*, the Resilience book{% include xref.html to="resilience" %}, and *Operating Production Systems in the AI & Cloud Era*, the Operations book{% include xref.html to="operations" %}, ask how the result is engineered for production and kept running. Each book stands on its own, and they were written to be read together.

### Influences & Attribution

Much of this book's method comes from others, and I want to be plain about where. Each chapter's references point to the original works, which are always the better read; this book's job is to connect them and to show them working together on one change at one company. The opening frame rests on the reports of the NATO conferences at Garmisch and Rome, edited by Peter Naur, Brian Randell and John Buxton, and on Edsger Dijkstra's Turing lecture, while the idea that software engineering is programming integrated over time comes from Titus Winters, Tom Manshreck and Hyrum Wright's *Software Engineering at Google*, a book this one leans on in nearly every chapter. Meir Lehman's laws of software evolution and Melvin Conway's paper on committees supply the forces the engineering system works against.

The chapters on code and change draw on Ward Cunningham's WyCash report, John Ousterhout's *A Philosophy of Software Design*, Martin Fowler's *Refactoring* and his writing on branches, feature toggles and the strangler fig, Kent Beck's *Tidy First?*, Michael Feathers's *Working Effectively with Legacy Code*, Adam Tornhill's *Your Code as a Crime Scene*, and Marianne Bellotti's *Kill It with Fire*. Testing follows Vladimir Khorikov, Steve Freeman and Nat Pryce's *Growing Object-Oriented Software, Guided by Tests*, Ian Robinson on consumer-driven contracts, Koen Claessen and John Hughes's QuickCheck, the Amazon S3 team's work on lightweight formal methods, Davide Fucci and colleagues on test-driven development, and, for evaluating language models, Hamel Husain, Shreya Shankar and Chip Huyen. The development loop draws on Jez Humble and David Farley's *Continuous Delivery*, Caitlin Sadowski and colleagues, Alberto Bacchelli and Christian Bird on code review, Michael Fagan's inspections, and the published engineering of Google, Meta, Uber and Lyft. The chapter on AI assistance weighs the field experiments of Kevin Zheyuan Cui and colleagues, METR's randomized trials, DORA's reports, Google's papers on migrations with language models, and the work of Hao He, Judy Hanwen Shen and Alex Tamkin, read against Grace Hopper's 1952 paper, John Backus's memoir and Lisanne Bainbridge's *Ironies of Automation*.

The platform chapters draw on the Programmer's Workbench papers of Evan Ivie and of T. A. Dolotta, R. C. Haight and J. R. Mashey, on Camille Fournier and Ian Nowland's *Platform Engineering*, Gregor Hohpe's *Platform Strategy*, the developer-experience research of Abi Noda, Margaret-Anne Storey, Nicole Forsgren and Michaela Greiler, the SPACE framework, and Spotify's accounts of golden paths and migrations. The SaaS chapter follows Craig Weissman and Steve Bobrowski's account of Salesforce's multitenant design, Tod Golding's *Building Multi-Tenant SaaS Architectures*, Google's Zanzibar and Facebook's configuration papers, and the SCIM standards. Ecosystems draw on David Evans and Richard Schmalensee's *Matchmakers*, Geoffrey Parker, Marshall Van Alstyne and Sangeet Paul Choudary's *Platform Revolution*, Michael Cusumano, Annabelle Gawer and David Yoffie's *The Business of Platforms*, and Danese Cooper and Klaas-Jan Stol's *Adopting InnerSource*.

The organization chapters rest on Tracy Kidder's *The Soul of a New Machine*, Tom DeMarco and Timothy Lister's *Peopleware*, Matthew Skelton and Manuel Pais's *Team Topologies*, Will Larson's books on engineering management and staff engineering, Camille Fournier's *The Manager's Path*, Tanya Reilly's *The Staff Engineer's Path*, Heidi Helfand's *Dynamic Reteaming* and Lara Hogan's *Resilient Management*, with Frank Schmidt, John Hunter, Paul Sackett and their colleagues on what predicts success in hiring. Planning and flow follow Donald Reinertsen's *The Principles of Product Development Flow*, Daniel Vacanti's *Actionable Agile Metrics for Predictability*, Dominica DeGrandis's *Making Work Visible*, Mik Kersten's *Project to Product*, Bent Flyvbjerg's work on why large projects overrun, and the DORA research of Nicole Forsgren, Jez Humble and Gene Kim, with Sylvain Lenfle and Christoph Loch and Harvey Sapolsky on what the Polaris program really owed to PERT. The capstone draws on the US General Accounting Office's Year 2000 assessment guide, the final report of the US Senate's Year 2000 committee, Martyn Thomas's account of what really happened in Y2K and John Quiggin's dissent, together with David Parnas on information hiding and Vicent Martí's account of GitHub's parallel run. The real cases (Garmisch, WyCash, Ariane 5, the BitKeeper license and Git, Hopper's A-0, the Programmer's Workbench, Salesforce, the founding of the Visa network, the Data General Eagle, Polaris, Year 2000, Netscape's rewrite, the TSB migration and Atlassian's outage of 2022) are described as history, from the public record.

Several terms used in this book as common vocabulary were coined by specific people or groups, and they deserve the credit: technical debt (Ward Cunningham), deep modules (John Ousterhout), tidyings (Kent Beck), characterization tests, seams and sprouts (Michael Feathers), the strangler fig (Martin Fowler), branch by abstraction (Paul Hammant, crediting Stacy Curl), Hyrum's law (Hyrum Wright), hotspots (Adam Tornhill), the walking skeleton (Alistair Cockburn), consumer-driven contracts (Ian Robinson), stream-aligned teams, interaction modes, the team API and the thinnest viable platform (Matthew Skelton and Manuel Pais), the four pillars of platform engineering (Camille Fournier and Ian Nowland), golden paths (Spotify), the DevEx framework (Abi Noda, Margaret-Anne Storey, Nicole Forsgren and Michaela Greiler), the SPACE framework (Nicole Forsgren and colleagues), InnerSource (Tim O'Reilly) and the trusted committer (the InnerSource Commons), the isolation pattern of reteaming (Heidi Helfand), cost of delay and weighted shortest job first (Donald Reinertsen), CD3 (Joshua Arnold), work item age (Daniel Vacanti), flow metrics (Mik Kersten), and Goodhart's law (Charles Goodhart, in the phrasing Marilyn Strathern gave it in 1997).

### Authorship & Disclaimer

This book was written and directed by Oleksiy Pylypenko, with AI assistance (Anthropic's Claude). The judgment in it comes from twenty-plus years of practice: platform engineering inside a large bank, API architecture in fintech, and a decade of maintaining a widely used open-source library. The author chose the thesis, the structure, the examples and the trade-offs, edited every chapter, and takes responsibility for every claim, errors included. Encore and every kata company are fictional, and historical events are described from the public record. The content is provided as-is, without warranty of any kind. It is educational material, not professional, legal or financial advice for any specific system or organization, and the license's full disclaimer of warranties applies.

## How to Read This Book

One company runs through all eleven chapters. **Encore** sells tickets to live concerts across the European Union, and its traffic can rise 500× in minutes when a major tour goes on sale, which makes it a demanding place to learn how to build software at scale. Readers of the Architecture book watched Encore grow from nine engineers in one team to 400 in 40, and readers of the Resilience and Operations books watched it prepare for, fight and learn from one bad Friday morning. This book picks the company up in its ninth year, at about the same size, and looks at what none of the earlier books looked at directly: the engineering system inside it, with its oldest repository, its 31-minute build, its platform group of nine teams and its quarterly survey of what slows its engineers down. Chapter 1 introduces Encore for readers meeting it for the first time, each later chapter adds the parts of the company it needs, and an appendix gathers all of them on one page for reference.

One change runs through the book. **Verified Resale** lets fans resell tickets they bought through Encore, at no more than face value, through authorized partners, and it reissues every resold ticket under a new identity while the old one is revoked at every gate. To the product it is a bet; to engineering it is a change to the oldest code Encore owns, a barcode issuance module written in the company's first year and understood today by one person, which must learn that a ticket's identity can change. The change touches 12 teams through 23 dependencies at the first quarterly plan. Part II prepares the old code, tests the new and shortens the loop through which every change passes, and it asks what AI assistance does to that work. Part III builds the platforms the change needs, inside Encore and out, and Part IV designs the teams that carry it and the plans and funding that pace it. Chapter 11 then follows the one change from the first characterization test in the barcode core to the first resold ticket scanned at a gate in Lyon, and to the engineering review held a year after launch.

This book tells only half of Verified Resale's story. The Products book follows the same months from the product side: why Encore made the bet, how it learned what fans, organizers and partners needed, how it set the fee and designed the screens, and whether, at the month-18 review, the bet had paid. Its capstone traces the same first resold ticket through the product that this book's Chapter 11 traces through the code. Where the two books meet, each points to the other and does not repeat it, so a reader of both will find two views of one change, and a reader of either will find a complete book.

Each chapter closes with a **kata**, a practice brief for a different company with its own scale and constraints, together with a rubric to check your work against. The word comes from the martial arts, where a kata is a set form practiced until it becomes second nature, and the value lies in rehearsing the moves where mistakes are cheap, so that they are familiar when mistakes are expensive. Every section ends with a short recap and an exercise. The exercises are best done against the engineering system you work in, with its real repositories, queues and teams, because the point is to see the idea in your own organization rather than in Encore's. Each chapter's references list the field's standard works, and those marked *free online* cost nothing to read.

The chapters build on one another, but each can be read on its own. A reader whose builds take most of an hour may start with Chapter 4, a reader whose portal nobody visits with Chapter 6, and a reader asked for a date on work that crosses a dozen teams with Chapter 10. Chapters 1 and 2 are the ones I would ask every reader to make time for. The first draws the map of the engineering system that the rest of the book works on, and the second teaches how to change code that nobody fully understands, which is where most large changes are decided.

## The Arc

The eleven chapters fall into four parts and a capstone. They move from the engineering system as a whole, through the code and the loop that changes it, to the platforms beneath the teams and the organization that builds on them, and they end with one change followed through all of it.

**The engineering system (Chapter 1):** the two systems every software company runs, Encore at 400 engineers, Verified Resale as engineering first sees it, the levers, and what AI changes for building.

**Code and change (Chapters 2–5):** the codebase, its debt and its legacy core; testing strategy, from characterization to evals; the development loop from laptop to main; and building with AI assistance.
{: .flush}

**Platforms (Chapters 6–8):** the internal platform as a product; the SaaS control plane of tenants, identity and administration; and ecosystems of partners, marketplaces and InnerSource.
{: .flush}

**The organization that builds (Chapters 9–10):** growing, designing and leading teams; and the economics, forecasts and funding that let 40 of them act together.
{: .flush}

**The capstone (Chapter 11):** one change, the reissue of a ticket under a new identity, from the legacy core to production and the review a year after launch.
{: .flush}

## Contents

1. [Building Software at 400 Engineers — The System That Builds the System](#ch1)
2. [The Codebase — Design, Debt, and Change](#ch2)
3. [Testing Strategy](#ch3)
4. [The Development Loop — From Laptop to Main](#ch4)
5. [Building with AI Assistance](#ch5)
6. [The Internal Platform as a Product — Paths, Adoption, and Developer Experience](#ch6)
7. [Building the SaaS Platform — Tenants, Identity, and Administration](#ch7)
8. [Ecosystems — Business Platforms, Partners, and InnerSource](#ch8)
9. [Teams at Scale — Growing, Designing, and Leading the Organization That Builds](#ch9)
10. [Planning and Flow — Economics, Forecasts, and Funding](#ch10)
11. [Capstone — One Change, from Legacy Core to Production](#ch11)

[Appendix: Encore at a Glance](#encore-glance)
{: .toc-appendix}

---

## Chapter 1: Building Software at 400 Engineers — The System That Builds the System {#ch1}

> "Software engineering is programming integrated over time." — Titus Winters, Tom Manshreck and Hyrum Wright

Nine engineers can build a remarkable amount of software. They sit within earshot of one another, each of them has read most of the code, and a question about why something works the way it does can be answered by turning a chair around. Four hundred engineers can build far more, and yet a curious thing happens as a company grows from the first number to the second: each change becomes harder to make. A modification that once took an afternoon now takes a fortnight, crosses three teams, waits in two queues and needs a meeting to find out who owns the code it must touch. Nobody decided that this should happen. It is the cumulative result of thousands of reasonable decisions, each made by default, about how code is organized, how changes reach production and how people are arranged around both. The question of this chapter, and of this book, is what it takes for an organization of hundreds to keep changing a large, old and valuable piece of software quickly and safely, and why that is so much harder than it was for the few who wrote its first version.

The question is as old as the name of our discipline. In October 1968, at Garmisch in the Bavarian Alps, the North Atlantic Treaty Organization (NATO) brought together more than 50 people to talk about the trouble they were having with large software systems, and its organizers gave the meeting a deliberately provocative title: *software engineering*. The participants were candid about how far their practice fell short of that name, and they saw, more clearly than they are usually given credit for, that the trouble grew with the number of people as much as with the number of lines. What they lacked was a method. Section 1.1 tells their story, because the next half-century of our field can be read as a long search for the practices they knew they needed, and this book is about the ones that were found and proven.

Encore is where we will watch those practices at work. It sells concert tickets across Europe, it reached 400 engineers in its seventh year, and it has stayed at about that size since. Now, in the late spring of its ninth year, it has decided to build **Verified Resale**: a way for fans to resell tickets they bought through Encore, at no more than face value, through authorized partners, with every resold ticket reissued under a new barcode. The Products book follows that bet as a product, from its memo to its launch and review. This book follows the building. The bet's engineering needs are plain enough to state and hard to meet: it must change the oldest code Encore owns, a barcode issuance module written when the company had nine engineers and understood today by exactly one of them; it must coordinate 12 teams across 23 dependencies; and it must do both without slowing the rest of Encore's teams, most of which have nothing to do with resale. Each chapter that follows takes one part of that work and teaches the practice that makes it possible.

This chapter sets the stage: the two systems every software company runs, Encore at its present size, Verified Resale as engineering first sees it, the four levers the rest of the book pulls, and what assistance from artificial intelligence (AI) changes about all of this.

### 1.1 Two Systems

#### The product and the system that builds it {#c1-two-systems}

Every software company runs two systems. The first is the one its customers use: at Encore, the waiting room, the seat map, the checkout and the ticket on the fan's phone. The second is the one that produces the first. It consists of the code and its tests, the build tools and pipelines, the platform that services run on, the teams that own each piece, the review habits, the plans and the budgets, and the unwritten rules about who may change what. I will call this second system the **engineering system**: the code, tools, platforms, teams and practices through which an organization turns an intention into running software, and goes on changing that software for as long as it lives. This book is about the engineering system. The Architecture book was about the shape of the first system, and the Products book{% include xref.html to="products" %} about deciding what it should do next; here we study the machinery that makes and remakes it.

The distinction is easy to state and easy to forget, because the second system is mostly invisible to anyone outside it. A touring concert production makes the point better than any diagram. The audience sees a show: two hours of music, light and sound in a particular hall on a particular night. Behind it travels another organization entirely, with riggers, trucks, a production manager, a stage plot, a load-in schedule and a crew that has rehearsed the order in which the stage goes up. That second organization decides how many cities the tour can play, how quickly it can move between them, and what happens when a truck breaks down in the Alps. No one buys a ticket to see it, yet it sets the limits of every show. The analogy breaks in a way that teaches. A touring crew builds the same stage every night, and its virtue is repetition. An engineering system builds a different product every day, because each change alters the thing being built, and it must also change itself as it goes, since the tools and habits that suited 70 engineers will not suit 400.

The authors of *Software Engineering at Google* put the same idea in a sentence that serves as this chapter's epigraph: software engineering is "programming integrated over time." They go on to name three differences between programming and software engineering, which are time, scale and the trade-offs at play. A program written once and thrown away needs only a programmer. A program that must be changed for years, by people who did not write it, while it carries money and reputations, needs an engineering system, and the quality of that system decides how fast and how safely the program can change.

The engineering system is sociotechnical, which is to say it is made of people and machinery that shape each other. The first sign of this is Conway's law, which the Architecture book's Section 1.3{% include xref.html to="architecture:1.3" %} introduced and its Section 5.5 turned into a design tool: the structure of a system tends to mirror the structure of the organization that builds it. The law runs in both directions through the engineering system. The way teams are drawn shapes the code, and the way the code is drawn shapes which teams must talk to one another before anything can change. Neither half can be improved for long without the other, and much of this book is about pulling on both at once.

#### Garmisch, 1968 {#c1-garmisch}

In late 1967 the NATO Science Committee's Study Group on Computer Science recommended a conference on the problems of building software, and it met at Garmisch, in Bavaria, from 7 to 11 October 1968. Its chairman was Friedrich L. Bauer of Munich. The report records that it "was attended by more than fifty people, from eleven different countries," drawn from the users and manufacturers of computers and from the universities. It was a working conference, divided into three groups that studied the design, the production and the service of software, and among those present were Edsger Dijkstra, Alan Perlis, Peter Naur, Doug McIlroy and Brian Randell. (The Architecture book's Chapter 13 recalls McIlroy's argument there for mass-produced software components; we need not retell it.)

The name was chosen with intent. The report's preface explains that "the phrase 'software engineering' was deliberately chosen as being provocative, in implying the need for software manufacture to be based on the types of theoretical foundations and practical disciplines, that are traditional in the established branches of engineering." Randell later wrote that the idea of the conference, and of its title, came, he believed, from Bauer. The provocation lay in the gap between the word and the practice. Civil engineers had codes, calculations and a professional memory of bridges that fell down; software in 1968 had, by the participants' own account, a habit of arriving late, costing far more than planned and failing in use. The figures discussed were large even by later standards. Ed David relayed that, according to T. J. Watson, IBM's OS/360 operating system had cost over $50 million a year during its preparation, with at least 5,000 man-years invested. Alexander d'Agapeyeff observed that a European manufacturer that had employed fewer than 50 programmers in 1958 probably employed between 1,000 and 2,000 a decade later.

The participants did not agree on what to call their predicament. The report speaks of a debate over "what some members chose to call the 'software crisis' or the 'software gap'." Kolence objected that "crisis" was too emotional a word. Douglas Ross took the other side, observing that a heart attack is a crisis even when every other organ is in fine working order. Others pointed out that most computers worked tolerably well most of the time. Dijkstra welcomed the open admission of failure as the precondition for improving on it. The phrase "software crisis" became canonical only four years later, when Dijkstra, in his 1972 Turing Award lecture "The Humble Programmer," called Garmisch "the turning point," the conference at which "there occurred the first open admission of the software crisis." It is worth keeping that history straight, because the word has since been repeated so often that it sounds like a finding. At Garmisch it was a contested description, offered by people who disagreed about how bad things were and agreed only that they were bad enough to need a discipline.

A common reading of Garmisch holds that its participants thought of scale as a matter of code and underrated the problem of people. The report shows the opposite. Alan Perlis told the meeting that "we must learn how to build software systems with hundreds, possibly thousands of people." John Buxton warned that more than 20 programmers on one project was usually a disaster, and Opler said he knew how to organize communication for projects of 10 to 50 people and was sure he did not know how to do it for much larger ones. Ed David's position paper cautioned that scale did not refer only to the size of the code. Randell cited Melvin Conway's paper, published in *Datamation* that April, and proposed out loud what we now call the inverse Conway manoeuvre: since a system will tend to mirror the structure of the group that builds it, the group's structure should be designed deliberately to produce the system we want. Garmisch, in other words, already understood that the hard part of large software lies in the many people who must change it together.

What it did not have was a method. Peter Naur and Brian Randell wrote the report in Munich in the week after the meeting, from rapporteurs' notes and tape recordings, and published it in January 1969. A second conference followed, near Rome, from 27 to 31 October 1969, and its report, edited by Buxton and Randell, is unusually frank. The meeting "bore little resemblance to its predecessor," the editors wrote; the sense of shared urgency had faded, and "a lack of communication between different sections of the participants became, in the editors' opinions at least, a dominant feature." No attempt was made to continue the series. Randell later recalled that at Garmisch it had been "fully accepted that the term software engineering expressed a need rather than a reality," and Rome had shown how far the field still was from agreeing on how to meet that need. Figure 1.1 draws the meeting in outline and places it among the years around it.

{% include diagrams/fig-1-1.svg %}

*Figure 1.1 — Garmisch in outline: three constituencies, three working groups and a report, and on the timeline below, the short distance from Conway's paper to the meeting and the long one to the phrase "software crisis."*

I find this the most useful way to read the conference. Garmisch named the problem this book addresses: a gap between what organizations needed to build and what their methods could build, a gap that opened wherever systems and the groups building them became large. Its participants even distrusted easy answers; Ross warned that there was "no worse word than 'breakthrough'" in discussing solutions, 18 years before Fred Brooks's "No Silver Bullet." The decades since have been spent finding practices that close the gap a little, testing them and keeping the ones that work. Some were found quickly and some took 40 years. Some, like version control and automated testing, became so ordinary that we forget they once had to be invented. The engineering system of a company like Encore is the accumulated answer to the question Garmisch asked, and the last chapter of this book will return to that Alpine meeting to ask how much of the gap has closed.

#### What scale changes {#c1-what-scale-changes}

Growth from nine engineers to 400 does three things to the cost of building software, and it is worth separating them because they call for different remedies. The first is coordination. Brooks showed, in *The Mythical Man-Month*, that the possible paths of communication in a group grow with roughly the square of its size, and the Architecture book's Chapter 5{% include xref.html to="architecture:5" %} works through that arithmetic for Encore's growth to 70 engineers. At 400 people the paths among individuals are far too many to use, so organizations group people into teams and route communication through team boundaries, which turns a problem of people into a problem of structure. Coordination is the one cost we can say with confidence grows faster than headcount, because the arithmetic guarantees it.

The second cost is comprehension. When Encore had nine engineers, most of them had read most of the code. At 400 nobody has read most of the code, and nobody could; the codebase has grown past what one mind can hold, and each team understands its own part and a thin margin around it. There is no single canonical result that measures how comprehension decays with size, so I offer this as an argument from observation. It has, however, a well-studied cousin. Matthew Skelton and Manuel Pais's *Team Topologies* treats a team's **cognitive load**, the amount a team must hold in mind to change its software safely, as the limit on how much a team can own, and developer-experience research has made it one of the three dimensions it measures. Comprehension is the reason a change at 400 so often begins with archaeology: before anyone can modify the code, someone must find out what it does and who still knows.

The third cost is the cost of change itself. Meir Lehman's laws of software evolution, whose first law the Architecture book's Section 13.3{% include xref.html to="architecture:13.3" %} takes up, have a second law that matters more here. In Lehman's 1980 wording, "as an evolving program is continually changed, its complexity, reflecting deteriorating structure, increases unless work is done to maintain or reduce it." The final clause carries the weight. Complexity is the default outcome of change, and only deliberate work holds it back. Brooks's distinction between essential and accidental complexity, which the Architecture book makes its starting point, sharpens the claim. The essential complexity of selling each seat exactly once to a fan who is not a bot does not change whether Encore has nine engineers or 400. The accidental complexity does: the extra layers, the duplicated libraries, the three ways of doing one thing, the code whose purpose nobody remembers. Accidental complexity accumulates with every change unless the engineering system removes it, and an organization of 400 makes a great many changes. That work of removal is much of what this book describes.

Comprehension and the cost of change tend to grow faster than headcount, though I cannot give a rate for either. Coordination provably does. Together they explain the curious fact this chapter began with, that adding people to a growing company makes each of its changes harder even while it makes the company able to attempt more of them.

#### What a good engineering system produces {#c1-good-system-produces}

If the engineering system is a product in its own right, we should be able to say what it is for, and to judge it by results instead of by activity. Three results matter most.

The first is delivery: how quickly and how safely changes reach users. The research program that began as the State of DevOps surveys, and continues as DORA (DevOps Research and Assessment), has studied this more carefully than anyone. Nicole Forsgren, Jez Humble and Gene Kim's *Accelerate* (2018), drawing on survey data from 2014 to 2017 and more than 23,000 responses, reported the finding that has shaped the field since: speed and stability go together, so the organizations that deliver most often also fail least and recover fastest. DORA's delivery metrics, long known as the "four keys," became five in 2024. They are change lead time, deployment frequency, change failure rate, failed deployment recovery time and, newly, rework rate, which DORA groups into throughput and stability. The Architecture book's Section 11.2 defines them and the Resilience book's Section 4.2{% include xref.html to="resilience:4.2" %} shows why throughput and stability do not trade off; this book uses them in Chapter 10 to measure delivery across Encore's teams.

The second result is the ability to change old code safely. No standard metric captures it, and it is easy to neglect because new code is where the excitement is. Yet a company's most valuable code is usually its oldest, since it encodes years of decisions about how the business really works, and an engineering system that can only change new code has a short future. Chapters 2 and 3 are about this capacity, and Verified Resale will test it severely.

The third result is people who can do their best work. Abi Noda, Margaret-Anne Storey, Nicole Forsgren and Michaela Greiler, in "DevEx: What Actually Drives Productivity" (2023), proposed three dimensions of developer experience: **feedback loops**, how quickly a developer learns whether a change works; **cognitive load**, as above; and **flow state**, the ability to work without interruption on something absorbing. It is a framework for measuring, derived from earlier research, and Chapter 6 uses it as one lens on whether Encore's platform is helping.

These measures have limits, and it is honest to state them at the start. None of them says whether the right thing was built; a team can deliver quickly and stably a feature nobody wanted, which is the Products book's subject. All of them can be gamed once they become targets, which is Chapter 10's warning. And none can be improved by someone who has not first looked at how work actually flows. The proven way to look is **value-stream mapping**: drawing the path a change takes from idea to production, with every step, handoff and wait marked and timed. It comes from lean manufacturing, where Mike Rother and John Shook's *Learning to See* (1998) set out the method, and DORA lists value-stream management among the capabilities that predict delivery performance. The exercise at the end of this section asks for one.

#### Where this book sits in the series {#c1-series}

This is the third of five books that follow Encore. The Architecture book shaped the system: its styles, boundaries, data, interfaces and platform. The Products book decided what to build and why, and followed Verified Resale from a memo to a launch. This book builds it, and in doing so studies the engineering system that does the building. The Resilience book hardens the system against load and failure, and the Operations book{% include xref.html to="operations" %} runs it on the day the load arrives. Each book leaves the others' subjects alone. Here that means we take the architecture of Encore's services as given, take the product decisions about Verified Resale as settled, and leave progressive delivery, service level objectives and incident response to the books that own them, pointing to them where a reader needs the thread.

**Recap.** Every software company runs a product and an engineering system that builds it, and the second sets the limits of the first. Garmisch named the problem of building software with many people in 1968 and lacked the methods to solve it; the field has spent the decades since finding them. Scale raises the costs of coordination, comprehension and change, and complexity rises unless deliberate work holds it back, so a good engineering system is judged by delivery, by the safety of changing old code and by the experience of the people who use it.

**Exercise 1.1.** Draw the value stream for one recent change in your organization, from the moment someone decided it should happen to the moment a user could see it. Mark every team it passed through, every tool, and every wait, with the time spent waiting. Then add up the hours of work and the hours of waiting separately, and compare them.

### 1.2 Encore at 400

Readers who know Encore from the earlier books may skim this introduction. Encore sells concert tickets across the European Union (EU), priced in euros, and also sells its platform to venues as software as a service (SaaS). Three facts define its engineering. When a famous artist's tour goes on sale, nearly always at 10:00 on a Friday, traffic rises 500× within minutes. Every seat must be sold exactly once, never lost and never sold twice. And the bots arrive before the fans. It has four kinds of customer: fans; event organizers; partners such as venues, resale partners and a festival app, which call its public application programming interface (API) at `api.encore.com`; and venues that run Encore as SaaS. Each of the services named below, from the Sale Gate to Seat Inventory, is described where it first matters in the Architecture book, and the appendices of the Resilience and Operations books keep the whole company on one page. What follows is Encore seen from inside its engineering system, which none of those books looked at directly.

#### How Encore got here {#c1-how-encore-got-here}

Encore's engineering system was never designed as a whole. It grew in three stages, and at each stage the people building it made choices by default that were reasonable for their size and became constraints at the next. Figure 1.2 sets them side by side.

{% include diagrams/fig-1-2.svg %}

*Figure 1.2 — Encore's engineering system at three sizes. The outlined row, the decision each size made by default, is the one nobody wrote down at the time.*

The bottom row deserves a slower reading than the others, because it holds the engineering system's history in compressed form. At nine people, ownership is unnecessary; everyone knows who wrote what, and anyone can change anything. At 70, the split into services (the Architecture book's Chapter 5{% include xref.html to="architecture:5" %}) gave each service a team, but some code belonged to no service in particular, and it stayed in the old repository with no clear owner. At 400, the golden path made new services easy to build well, and the old code that still worked was, sensibly, left alone. Each default was a good decision on its own day. Taken together they produced a company with excellent paths for new code and a quiet reluctance to touch old code, and Verified Resale needs to change the oldest code of all.

The fuller story of how Encore's organization grew, including what broke at each size, belongs to Chapter 9. Here we need only the engineering system as it stands now.

#### The codebase {#c1-codebase}

Encore's backend code lives in two kinds of repository. The **shared repository**, `encore-core`, grew from the year-one monolith and still holds several of the services that were split from it, Seat Inventory & Ticketing and the Orders & Payments saga among them, along with the shared libraries that several services use. Newer services, created from the platform's template since the golden path arrived, each have a repository of their own. Chapter 4 examines this arrangement and why Encore keeps it; for now it is enough to know that the oldest code and the slowest builds live in the same place.

On the frontend, the fan storefront on the web is a modular monolith built on one design system, and the organizer console is a separate application on the same design system, as the Architecture book's Chapter 8{% include xref.html to="architecture:8" %} explained. The fan app is native, on iOS and Android, and it consists of a shell and 14 feature modules, each owned by a team: Discover, Search, Event, Waiting Room, Seat Map, Checkout, Payment Completion, My Tickets, Account, Inbox & Preferences, Help & Refunds, Presales, Festivals and Following. Verified Resale will add a fifteenth.

Inside the shared repository, inside the Seat Inventory & Ticketing service, sits the module this book will keep returning to. **Barcode issuance** turns a sold seat into a ticket identity and the entry credential that a venue's scanners accept. It was written in Encore's first year, in Kotlin like the rest of the original monolith, and it runs to about 11,000 lines. Every ticket Encore has ever sold has passed through it. Section 1.3 explains why Verified Resale cannot avoid it.

#### The path to production {#c1-path-to-production}

A change at Encore travels a route that most of its engineers no longer notice. The engineer works on a short-lived branch and integrates into the main line at least daily, which is **trunk-based development**, one of the capabilities DORA's research associates with high delivery performance. The change is reviewed by an engineer from the owning team, and by the owners of any other code it touches. Continuous integration (CI) builds and tests it; on the shared repository that takes 31 minutes, on most newer repositories under 10. It then follows the **golden path**, the supported route from a service template to production that the Architecture book's Section 15.2{% include xref.html to="architecture:15.2" %} described: the template, the provisioning workflow, the registry entry and the scorecard. Deployment is progressive, through canaries at 1, 5, 25 and 100% of traffic, never during an on-sale, and unfinished features hide behind some 2,300 feature flags. The Resilience book's Sections 4.2 and 4.3 own the mechanics of that last stretch.

The numbers are good by the standards of the industry. Encore makes about 180 production deploys on an ordinary working day. Its median lead time for changes, from commit to production, is about 26 hours. The median hides the shape of the distribution, though. Most of those hours are spent waiting for a reviewer, and for changes that cross team boundaries the wait stretches to days. A change confined to one team's new service can reach production before lunch. A change that touches the shared repository and two teams' code routinely takes most of a week. Verified Resale consists almost entirely of the second kind.

#### The teams {#c1-teams}

Encore has 40 stream-aligned teams, about 360 engineers averaging nine a team, and each owns a flow of business change: a part of the fan app, a piece of the organizer console, a partner API, a service in the purchase path. Beneath them sits a platform group of nine teams and 40 people, about 10% of engineering and at the top of the 5–10% band that the Architecture book's Section 15.2{% include xref.html to="architecture:15.2" %} called a common rule of thumb. The platform teams own the runtime, the developer portal and its templates, the paths for APIs and web frontends, the event backbone, the data platform, the AI gateway, security engineering and reliability. The stream-aligned teams fall into five groups: nine for the fan storefront and app, seven for the organizer console, three for partner and public APIs, seven for the SaaS that venues buy, and 14 for the shared domains that everything depends on, from the Sale Gate and Bot Screening to Seat Inventory, Orders & Payments and Notifications. Chapter 9 explains how the map came to look like this and how Encore redraws it.

A map of teams says who is responsible. It does not say who owns which lines of code, and at 400 engineers that question cannot be answered from memory. Encore answers it the way most large engineering organizations now do, with **ownership metadata**: a record, kept in the repository and the service registry, that names the team responsible for each directory and service. Google's OWNERS files, described in *Software Engineering at Google*, are the best-known version, and the CODEOWNERS file that most code hosts support is the commonest. An excerpt from the shared repository's file shows both what such a record does and what it cannot do.

```
# CODEOWNERS — shared repository (excerpt)
/services/seat-inventory/                   @encore/inventory
/services/seat-inventory/issuance/barcode/  @encore/inventory
/services/orders/                           @encore/orders-payments
/services/orders/saga/                      @encore/orders-payments
/libs/ticket-id/                            @encore/inventory
/libs/money/                                @encore/finance-platform
/libs/http-client/                          # no owner since year 5
```

The file says that the Inventory team owns barcode issuance, and the review history says that one person on that team has approved every change to it for three years. The file records accountability; it cannot record understanding. The last line is a different kind of gap. A shared library that every service in the repository uses has had no owner since its author moved teams, and changes to it are reviewed by whoever happens to be changing it. Chapter 4 makes the repository's ownership match the team map, and Chapter 8 asks how shared code like this should be run.

#### What engineers say hurts {#c1-what-hurts}

Encore asks its engineers every quarter how their work is going. The survey has 10 core items that never change, so that answers can be compared across years, and a free-text question about the single thing that most slows them down. About 68% of engineers answered the most recent one. The practice of a regular, stable survey is well established. Google's engineering productivity researchers have described a quarterly Engineering Satisfaction survey that samples about a third of the company's engineers each quarter, and Chapter 6 discusses how to design one properly. What matters here is what Encore's engineers said, and Figure 1.3 shows it.

{% include diagrams/fig-1-3.svg %}

*Figure 1.3 — The six most common answers in Encore's latest developer survey, with the chapter that addresses each. Fear of old code is not the commonest complaint, but it is the one Verified Resale meets first.*

A physician learns early that a patient's complaint is precious evidence and a poor diagnosis. "My chest hurts" is true and important, and it might mean a heart, a lung, a rib or anxiety; the doctor takes the symptom seriously by refusing to treat it at face value. Developer complaints work the same way. "CI is slow" is true, and the cause might be the size of the repository, the absence of caching, a test suite that runs everything for every change, or a build system that cannot tell what a change affects. "Review takes forever" might mean too few reviewers, changes that are too large, or ownership drawn so that every change crosses a team boundary. The analogy fails at one point, and the failure is useful. A patient has one body, while an engineering system's symptoms often share a cause across several complaints. Encore's slow review and its fear of old code turn out, in Chapter 2, to be partly the same problem, because changes to code nobody understands are hard to review as well as hard to write.

One answer in the table points to a fact we will meet again. Three teams, in the course of integrating with partners, each built their own sender for webhooks, the messages Encore pushes to a partner's system when something happens, with different retry rules and different signing. Engineers named the waste themselves, and Chapter 6 shows the platform group finding and replacing all three.

**Recap.** Encore's engineering system grew in three stages, each leaving behind a default that was sensible at the time: no owners at nine, orphaned code at 70, old code left alone at 400. It now delivers well on new code and hesitates on old code, and its own engineers name the symptoms in its survey. Ownership metadata, a stable survey and a value-stream map are the first instruments for seeing such a system as it is.

**Exercise 1.2.** List the five complaints you hear most often from engineers in your organization. For each, write down at least two different causes that could produce it, and name the part of the engineering system (code, tests, tools, platform, teams or plans) where each cause would live. Then check one of them.

### 1.3 Verified Resale Arrives in Engineering

#### The bet, from the engineering side {#c1-the-bet}

Encore already lets partners advertise resale. Since its sixth year, under an arrangement called Partner Listings, authorized partners have been able to read Encore's event listings and post resale offers that appear as links on sold-out event pages. The ticket itself changes hands outside Encore, as the original pass is forwarded from seller to buyer, and Encore checks nothing beyond the partner's word. That arrangement allows the same barcode to be sold to several buyers, gives organizers neither control nor a share of the fee, and lets buyers through who were never screened. The Products book tells how Encore diagnosed those weaknesses and decided, in the late spring of year nine, to replace Partner Listings with something better. In brief, the product it decided on works as follows. A fan lists a ticket they bought through Encore's Sale Gate. The listing appears in Encore's own app and on authorized partners, Rowmate at launch and Tessera second. Another fan, screened like any primary buyer, buys it at no more than face value plus a 10% service fee, split four points to the partner through which the buyer purchased (Encore keeps those four when the buyer uses Encore's own app), three to the organizer and three to Encore; on a €60 ticket the buyer pays €66, and the seller receives the full €60 five days after the event. Encore then **reissues** the ticket: the seller's ticket identity is revoked and a new one is issued to the buyer. Mobile tickets at Encore have used rotating barcodes since the eighth year, generated on the phone from a per-ticket secret so that a screenshot is worthless. Reissue gives the buyer a new secret, and the old ticket identity joins the revocation lists that every venue gate holds for offline validation. Organizers may tighten the resale rules for their events but never loosen them, and they can write those rules in plain language through an assistant that drafts the typed rule set for them to confirm.

To engineering, that paragraph is a list of changes to code that already exists, plus some code that does not. A new Resale service must hold listings, rules and the resale purchase flow; a new Resale team, formed in month four from people in Orders & Payments and Partner APIs, with a product trio and a staff engineer, will own it. The partner API needs new endpoints, webhooks, a sandbox and a certification process. Seat Inventory must be able to reissue a ticket. Orders & Payments needs a resale purchase saga. Billing & Payouts must meter the fee split and pay sellers. Notifications must replace passes and tell sellers their ticket has sold. The fan app needs its fifteenth module, and the gate scanners must learn to refuse the revoked identity. The plan aims for a working path end to end by month nine, before the autumn tour season, and a staged launch in France, with three organizers and Rowmate, at month 12.

#### The 12 teams and the 23 dependencies {#c1-dependencies}

When the first quarterly plan for Verified Resale was drawn in month four, it touched 12 teams. They are the new Resale team; Inventory, which owns barcode issuance; Venue Entry, which owns the gate scanners and their revocation lists; Orders & Payments; Billing & Payouts; Partner APIs; Bot Screening; Organizer Console, for the rules console; Mobile App, for the release train and the wallet ticket view; Fan Messaging, which owns Notifications; Design System; and Security Engineering, for partner credentials. Eight more teams, among them Trust & Safety, Catalog and the Finance platform team, were consulted but given no planned work. The plan listed every place where one team needed something from another before its own work could finish, and there were 23 of them. Figure 1.4 groups them by the team that must deliver.

| Team that must deliver | What Verified Resale needs from it | Count | Oldest code touched |
|---|---|---|---|
| Inventory | Void and reissue in one step; proof a ticket was bought through the Gate within the per-fan limit; a new ticket-identity format | 3 | Year 1 |
| Venue Entry | Revocation lists that carry reissued identities; scanners that accept the new format; a feed of revocations from Inventory | 3 | Year 2 |
| Orders & Payments | A resale purchase saga; a void-and-refund path for a resold ticket | 2 | Year 1 |
| Bot Screening | Screening of resale buyers on every channel; per-buyer limits | 2 | Year 2 |
| Billing & Payouts | The fee split metered per sale; seller payouts after the event; split entries for the ledger | 3 | Year 4 |
| Partner APIs | Listing endpoints; webhooks to partners; sandbox and certification | 3 | Year 6 |
| Organizer Console | The resale rules console | 1 | Year 5 |
| Mobile App | The Resale module on the release train; the reissued-ticket view and a version floor | 2 | Year 8 |
| Fan Messaging | Wallet pass replacement; "your ticket sold" and "your new ticket" messages | 2 | Year 7 |
| Design System | A Verified badge, a capped-price display and reissue status | 1 | Year 5 |
| Security Engineering | Partner credentials with resale scopes | 1 | Year 8 |

*Figure 1.4 — The 23 dependencies of Verified Resale's first plan, grouped by the team that must deliver. Of these, 10 land in code written in Encore's first two years.*

The last column was not in the original plan. An engineer on the new Resale team added it during the first planning session, and it changed the conversation. Dependencies on recent code, such as Partner APIs or Mobile App, were the ordinary business of planning: the delivering team knew its code, could estimate the work and could say when. The 10 dependencies on code from the first two years were different. Nobody could estimate them with confidence, because nobody fully understood the code they touched, and every one of them sat on the path to the month-nine milestone. That is Encore's finding, and I do not offer it as a general law. It is common enough, though, that a planner should expect it: the dependencies most likely to hold up a large change are those on code that the organization has, by its long-standing defaults, learned to leave alone.

Encore records each dependency as a small entry in a file kept beside the plan, so that it can be reviewed, assigned and closed like any other piece of work. The entry for the most worrying of the 23 reads like this.

```yaml
# plans/verified-resale/dependencies.yaml (excerpt)
- id: VR-01
  needed_by: resale
  provided_by: inventory
  what: void a ticket identity and issue a new one in a single transaction
  code: services/seat-inventory/issuance/barcode (written year 1)
  needed_for: month-9 walking skeleton
  risk: one engineer understands this code; no meaningful tests
  status: open
```

A record like this is ordinary project hygiene, and its value lies in the field most plans leave out. The `risk` line ties a scheduling dependency to the condition of the code beneath it, which is where the schedule will actually be decided. Chapter 10 shows how Encore plans across the 12 teams, and what it does about dependencies it would rather not have.

#### The legacy core {#c1-legacy-core}

Barcode issuance is about eight years old. It was written in the months when Encore had nine engineers and one monolith, by people who were also building checkout, the seat map and the first pipeline, and it shows the marks of that time: long functions, a handful of tests that check little beyond whether the code compiles, and assumptions that were true when they were made and are now held up by nothing but habit. Of its original authors, one remains at Encore. She is Lena, one of the first nine engineers, now a senior engineer on the Inventory team, and she is the person every reviewer waits for when anything in the module changes.

There is a name for this condition. The **truck factor** of a body of code is the smallest number of people whose departure would leave nobody who understands it. (The Architecture book's Section 13.3 calls the same idea the bus factor; this book uses the other name throughout.) Barcode issuance has a truck factor of one. The condition is common. When Guilherme Avelino and his colleagues estimated truck factors for 133 popular open-source projects on GitHub in 2016, they found that 65% had a truck factor of two or less. I spent a decade maintaining a widely used open-source library, and the number does not surprise me; most code that many people depend on is understood in depth by very few, and those few are seldom chosen for the role; they are usually the people who happened to stay.

Why can reissue not be added beside the module, as so much of Encore's newer work has been? The answer lies in an assumption buried in the year-one code. When barcode issuance was written, a ticket's identity was permanent: once issued, it belonged to that seat and that order for as long as the ticket existed. The code derives the identity from the order and the seat, and four other places in the codebase, written later, rely on recomputing it the same way. When rotating barcodes were added in year eight, the team built the per-ticket secret around the existing identity without changing it, and that was the right decision for rotation, because rotation never needed an identity to change. Reissue needs exactly that. A resold ticket must stop being the seller's and become the buyer's, under an identity that every scanner, every revocation list and every one of those four other places will treat as new. The assumption of permanence is not confined to one function. It is spread through the module and beyond it, and reissue must change it at the root.

An architect renovating an old building faces a similar problem with load-bearing walls. A partition can be moved in an afternoon, but a wall that carries the floor above must be shored up before it is touched, and the first job is to find out which walls are which. The analogy holds well in one respect: the work of shoring up, which in software means getting the code under tests that describe what it does today, comes before any change, and Chapter 2 teaches that work. It fails in another, and the failure is worth stating. A builder can see a load-bearing wall, or at least find it on the drawings. In old code the load-bearing assumptions are invisible until something leans on them, and the drawings, if they ever existed, were never updated. Michael Feathers's definition of legacy code as code without tests, which Chapter 2 takes up, fits this reading: until the code is under test, nobody can say which of its assumptions bear load.

#### The five invariants as an engineering contract {#c1-invariants}

The Products book made Verified Resale a promise of fairness, and fairness at Encore has a precise form. Five rules govern the product, and they are worded the same way everywhere they appear in this book.

1. Partners never buy primary tickets.
2. Only tickets bought through the Gate, within the per-fan limit, can be listed.
3. Organizer caps and rules can only tighten.
4. Every resale buyer passes Bot Screening and the per-buyer limits.
5. Partners never see sales-velocity data.

To a product manager these are commitments. To an engineer they are **invariants**: properties that must hold in every state the system can reach, whatever sequence of requests arrives and whatever fails along the way. The difference matters. A commitment is kept by people paying attention; an invariant is kept by code that makes violating it impossible, and by tests that would fail if the code ever allowed it. The fifth rule shows how much care the translation needs. Resale partners already read Encore's availability endpoints during on-sales, as the Resilience book's Section 9.5{% include xref.html to="resilience:9.5" %} noted, and the rule survives only because the availability they read is the same coarsened view that every caller gets, from which velocity cannot be derived. The third rule shows where enforcement must live. The organizer rule assistant can propose any rule it likes, but the typed rule set it produces cannot express a loosening, so the platform enforces the rule, and neither the partner nor the AI can break it.

Chapter 3 turns the five invariants into tests that run on every build, and Chapter 8 asks how they shape Verified Resale as a marketplace. Here the point is simpler. The invariants are the part of the bet that engineering must guarantee absolutely, and every one of them passes through code in Figure 1.4's oldest rows.

#### What could go wrong {#c1-what-could-go-wrong}

Large changes that cross many teams fail in a small number of recognizable ways, and naming them early lets each chapter address one. Each has a well-documented public case.

The first is the rewrite that never ends. Faced with old code that nobody wants to change, it is tempting to write new code that replaces it. Netscape released version 4.0 of its browser in 1997 and then rewrote the browser from scratch; there was never a version 5.0, and version 6.0 did not ship until November 2000. Joel Spolsky, writing in April 2000 as the 6.0 beta appeared, called the decision to rewrite from scratch "the single worst strategic mistake that any software company can make." A rewrite discards the knowledge encoded in old code along with its defects, and it must reproduce years of behavior before it can ship anything. Chapter 2 explains why Encore changes barcode issuance in place.

The second is the big-bang integration. In April 2018 the British bank TSB moved about 5.2 million customers from the systems of its former parent, Lloyds, to a new platform over a single weekend. Up to about 1.9 million customers lost access to online banking, some for weeks. The independent review by the law firm Slaughter and May, published in November 2019, found that the new platform had not been ready and its testing had been inadequate. When 12 teams' work meets for the first time at the end, every misunderstanding surfaces at once; Chapters 3 and 4 show how Encore's teams integrate continuously instead.

The third is the dependency that blocks for a quarter. One team, busy with its own priorities, holds up 11 others because the work they need from it never reaches the top of its backlog. Chapter 10 treats this as a matter of planning and economics, and Chapter 11 tells what happened to Verified Resale's.

The fourth is code generated with AI assistance that nobody understands. The Architecture book's Section 15.4 and the Resilience book's Section 4.5{% include xref.html to="resilience:4.5" %} told of Encore's Notification rewrite, in which a coding agent rebuilt a service overnight and one engineer caught a path that would have issued duplicate tickets. Verified Resale will use such tools, and Chapter 5 asks how a team owns what a machine wrote.

The fifth is a platform gap that every team patches alone. The Architecture book's Section 15.1 described what happens when teams carry more than they can: some sink into infrastructure, some skip it, and some solve it their own way. Encore's three webhook senders are an example already in its code, and Verified Resale, which needs partner credentials and partner webhooks, would add more if nothing changed. Chapter 6 is about the platform group's answer.

**Recap.** Verified Resale reaches engineering as a set of changes to existing code across 12 teams and 23 dependencies, and the hardest of them land in the oldest code, where a truck factor of one and an assumption of permanent ticket identity stand in the way. The five fairness rules become invariants that code must enforce and tests must prove. The failure modes of such a change are well documented, and each of the following chapters is, in part, a defense against one of them.

**Exercise 1.3.** Take the largest change your organization plans for this year. List every team it touches and, for each, the oldest code that team must change, with the year that code was written and the number of people who understand it well. Mark any dependency where that number is one.

### 1.4 The Levers

An engineering system has many moving parts, but the practices that improve it fall into four groups, each acting on a different part of the system. I will call them **levers**: places where deliberate effort changes how fast and how safely the whole system can change software. The four are design, flow, leverage and organization, and the chapters that follow are arranged around them. Figure 1.5 lays them out.

| Lever | Chapters | What it acts on | What happens if it is pulled alone |
|---|---|---|---|
| Design: keep code changeable | 2–3 | The codebase and its tests | Clean code that waits in slow queues |
| Flow: shorten the loop | 4–5 | The development loop, review and AI assistance | Faster changes piling up behind a constraint elsewhere |
| Leverage: build platforms | 6–8 | Shared capabilities for teams, tenants and partners | A platform nobody adopts |
| Organization: design the builders | 9–10 | Teams, leadership, planning and funding | A tidy org chart drawn over code that does not match it |

*Figure 1.5 — The four levers of an engineering system, the chapters that teach each, and the way each fails when it is used without the others.*

#### Design: keep code changeable {#c1-lever-design}

The first lever acts on the code itself. Lehman's second law says that complexity rises unless work is done to hold it back, and the design lever is that work: keeping the code's structure coherent, refactoring as understanding grows, recording technical debt as data so that it can be weighed against other work, and building the tests without which no change to old code is safe. Chapter 2 treats the codebase and Chapter 3 the testing strategy that makes change possible. For Verified Resale this lever decides whether barcode issuance can be changed at all.

#### Flow: shorten the loop {#c1-lever-flow}

The second lever acts on the path a change travels from an engineer's editor to the main line. Small changes, fast feedback, review that keeps up and continuous integration that people can trust are DORA capabilities with measured effects on delivery, and the reason is the economics of batch size, which Donald Reinertsen worked out for product development and which Chapter 10 takes up. Chapter 4 covers the development loop and Chapter 5 the AI assistance now part of it. For Verified Resale this lever decides whether 12 teams' changes reach the main line in hours or in days.

#### Leverage: build platforms {#c1-lever-leverage}

The third lever solves a problem once for many teams. An internal platform takes on what every team would otherwise build for itself, a SaaS platform does the same for tenants, and an ecosystem extends it to partners; Chapters 6, 7 and 8 take them in turn. This lever comes with a condition, and it is fair to state it now. Platforms pay off when teams adopt them and when someone measures whether they help. DORA's 2024 report found, as the Architecture book's Section 15.5{% include xref.html to="architecture:15.5" %} recounts, that teams using an internal platform at first saw their delivery throughput and stability fall, by roughly 8% and 14%, even as individuals reported feeling more productive. A platform adds steps before it removes them, and Chapter 6 is about getting through that dip.

#### Organization: design the builders {#c1-lever-organization}

The fourth lever acts on people: how teams are drawn, how leaders lead, how work is planned across teams and how it is funded. It is the lever Randell pointed at in 1968 when he proposed designing the group to get the system we want, and *Team Topologies* gave it a modern vocabulary of team types and interaction modes. Chapter 9 covers teams and leadership, and Chapter 10 planning, forecasting and funding. For Verified Resale this lever decides whether the Resale team exists in the right shape and whether the 23 dependencies are managed or designed away.

#### Why all four {#c1-why-all-four}

In 1984 Eliyahu Goldratt and Jeff Cox published *The Goal*, a novel about a plant manager trying to save a failing factory, and its argument has outlived the factory. Every system that turns work into output has a constraint, a step slower than the others, and the throughput of the whole system is set by that step. Improving any other step improves nothing; work simply arrives sooner at the constraint and waits there. In one of the book's best-known scenes the manager takes his son's scout troop on a hike and notices that the line of boys moves at the pace of its slowest member, a boy named Herbie, however fast the boys at the front walk. When he puts Herbie at the head of the line and shares out the contents of Herbie's overloaded pack among the stronger boys, the troop reaches camp together. The remedy is to find the constraint, make the most of it, arrange everything else around it, and then, once it is relieved, look for the new constraint, because there always is one. Goldratt developed this theory of constraints for manufacturing, where it is well proven; in software delivery it is widely used as a way of reasoning, and value-stream mapping is its usual instrument. I know of no controlled study showing that it holds for software teams, so I offer it as reasoning, supported by examples.

The reasoning explains why the four levers must be pulled together. Each acts on a different part of the engineering system, and each, pulled alone, tends to move the constraint somewhere the others act. Encore's own history has two examples. In year five the fan-app team cut its build from 40 minutes to 12, a real achievement, and its median time from opening a change to merging it did not move, because the changes now reached review sooner and sat there just as long. The flow lever had been pulled in the tooling while review practice stayed as it was, and review was the constraint. In year six the platform team of the day built a shared deployment pipeline, announced it, and found 18 months later that two teams used it. The pipeline was good. Moving to it cost each team weeks that nobody had planned or funded, so the leverage lever had been pulled without the organization lever, and the constraint moved from tooling to adoption.

The clearest public case is recent, and it involves AI. DORA's 2024 report found that as AI adoption rose, individuals and teams reported better documentation, better code quality and faster code review, while delivery throughput fell by an estimated 1.5% and delivery stability by 7.2% for every 25% increase in adoption. DORA's own reading is that "improving the development process does not automatically improve software delivery—at least not without proper adherence to the basics of successful software delivery, like small batch sizes and robust testing mechanisms." That is a lever pulled alone. Writing code got faster; the work moved downstream, to review, testing and integration, and the system as a whole did not speed up. It leads directly to the last section of this chapter.

**Recap.** Four levers improve an engineering system: design keeps code changeable, flow shortens the loop, leverage solves problems once for many teams, and organization shapes the people who build. Every system has a constraint, and a lever pulled alone moves work to the constraint faster without relieving it. That is why this book pulls all four, and why each chapter points to the others.

**Exercise 1.4.** Name the last significant improvement your organization made to how it builds software. Say which of the four levers it pulled, then find out where work waited longest before the improvement and where it waits longest now. If the answer to both is the same place, say why.

### 1.5 What the AI Era Changes for Building

#### Code got cheaper; change did not {#c1-code-got-cheaper}

On Alphabet's earnings call of 29 October 2024, Sundar Pichai said that "more than a quarter of all new code at Google is generated by AI, then reviewed and accepted by engineers." The sentence has been quoted widely as evidence that writing code has become cheap, and in one sense it is. A competent engineer with a good assistant can produce a working function, a test, a migration script or a first draft of a service far faster than a few years ago, and the cost of producing code continues to fall. The Architecture book's Section 15.4 argued what this means for architecture. This book takes the engineering consequence, which is less comfortable.

The second half of Pichai's sentence carries that consequence: the code is "reviewed and accepted by engineers." Writing code was never most of the cost of changing software. Understanding the code that is already there, deciding what to change, reviewing the change, testing it, integrating it with everyone else's, deploying it safely and then owning it for years: these were always the larger part, and AI assistance has made the smallest part cheaper while leaving the larger parts where they were, or making them larger, because there is now more code to review, test and own. Dijkstra, in the same Turing lecture that made Garmisch's crisis famous, gave its cause as machines that had "become several orders of magnitude more powerful," so that the programs people attempted outran their ability to reason about them. The echo is hard to miss. When the means of producing software become much more powerful, the limit moves to the means of understanding it. Encore's Notification rewrite showed this on a small scale: the agent wrote a service overnight, and its safety rested on one engineer who read it closely enough to find a path that issued duplicate tickets.

#### The evidence in one paragraph {#c1-ai-evidence}

The research on AI-assisted development is young and its results disagree, which is itself informative; Chapter 5 examines it in detail. Controlled experiments on small, self-contained tasks have found large speedups, and field experiments inside companies have found smaller, though still real, gains. The most careful study of experienced developers working in their own mature repositories points the other way: in METR's (Model Evaluation and Threat Research) randomized trial, published in July 2025, 16 experienced open-source developers working on 246 real issues took 19% longer when AI tools were allowed, although they had forecast a 24% speedup and afterwards believed they had been about 20% faster. METR has since described that result as out of date and published a follow-up in February 2026, so the specific figure should not be leaned on; the gap between how fast people felt and how fast they were is the more durable lesson. At the level of delivery, DORA's 2024 report found modest gains in organizational and team performance as AI adoption rose, alongside the falls in throughput and stability described in Section 1.4. Read together, the studies suggest that the gains are real, uneven and largest where the surrounding engineering system is ready to absorb them.

#### What becomes more valuable {#c1-what-becomes-valuable}

If code is cheaper and change is not, the parts of the engineering system that turn code into safe change become more valuable. Tests that pin down behavior let a machine-written change be checked against what the system must do. Review keeps pace only when changes are small enough to review. Clear design lets an assistant's context and a reviewer's understanding cover the same ground, fast builds tell both of them quickly whether a change works, and platform paths make the safe way the easy way for every change, whoever or whatever wrote it. DORA's 2025 report on AI-assisted software development, drawn from about 5,000 respondents, frames AI as an amplifier: it strengthens what an organization already does well and magnifies what it does badly. That is a finding about the engineering system, and it is the reason this book gives AI assistance one chapter of its 11. Chapter 5 covers the practice, and the Resilience book's Section 4.5{% include xref.html to="resilience:4.5" %} covers the policy for machine-written changes on their way to production.

An analogy from aviation is tempting here. As cockpits gained autopilots, the pilot's work shifted from flying to monitoring, a history the Operations book's Chapter 3{% include xref.html to="operations:3" %} takes up, and as assistants write more code, the engineer's work shifts in the same way toward reading, judging and integrating. The analogy breaks where it matters most. An autopilot flies a known aircraft through a known envelope, while an assistant writes new code into a system whose envelope is years of accumulated complexity, and the engineering system is what gives the person reviewing that code a fighting chance.

#### The rule for this book {#c1-rule-for-this-book}

This book recommends only practices with evidence behind them: practices that are widely used, with research or long industry experience to show that they work. Where a practice is young, as much of AI-assisted development still is, the book labels it **emerging**, says so plainly, and gives the best real account of its use. Where Encore does something the evidence does not yet support, the book says that too. The Products book follows the same rule with the same labels, so that the two books, and the series, can be read as one argument.

**Recap.** AI assistance has made writing code cheaper and left the larger costs of changing software, understanding, review, testing, integration and ownership, where they were or heavier. The evidence so far shows real but uneven gains, a persistent gap between perceived and measured speed, and a strong dependence on the engineering system around the tools. Practices that turn code into safe change gain value as code gets cheaper, and this book recommends only those that are proven, labelling the rest.

**Exercise 1.5.** Find one change in your codebase from the last month that was largely written with AI assistance. Trace what checked it before it reached production: which tests, which reviewer, which pipeline stages. Then ask the reviewer how long the review took and how confident they were, and compare that with a change of similar size written by hand.

### Kata: The Tariff Deadline

> **Your brief: "Northgrid."** Northgrid sells software to energy retailers: billing, metering, customer accounts and switching, run as SaaS for 30 retailers in four EU countries. It has 250 engineers in 28 teams, including a platform team of 12. Its billing core was written in the company's first year, nine years ago, by a team of six; it calculates every invoice Northgrid's customers send, about 11 million a month, and two of its original authors remain, one of whom is about to retire. The core lives in a shared repository whose CI takes 48 minutes, and changes to it wait a median of four days for review. A regulator in one of Northgrid's countries has published a new dynamic tariff, priced by the hour from the wholesale market, that every retailer must be able to offer within 14 months. Northgrid's first plan shows the change touching nine teams with 19 cross-team dependencies, and its last developer survey named flaky end-to-end tests, review waits and "nobody understands billing" as the top three pains. The leadership team has proposed two answers: rewrite the billing core, or buy an AI coding assistant for every engineer.

**Deliverables:**

1. **Value-stream map** — Draw the path a change to the billing core takes from idea to production, with every team, tool, handoff and wait, and estimate the time at each step. Mark where work waits longest.
2. **Engineering-system profile** — In one page, describe Northgrid's engineering system as Section 1.2 described Encore's: the codebase and its oldest parts, the path to production, the teams and their ownership metadata, and what engineers say hurts. Note which default decisions from earlier stages still shape it.
3. **Dependency map with code age** — List the 19 dependencies of the tariff change as Figure 1.4 lists Verified Resale's, adding the age of the oldest code each one touches and its truck factor. Identify the dependencies most likely to stall the change.
4. **Invariants** — Write the rules the dynamic tariff must never break, such as an invoice that always reconciles with metered consumption, as invariants a test could check.
5. **The first lever** — Choose which of the four levers to pull first, and say where the constraint will move once it is pulled and which lever you will need next. Address both of leadership's proposals directly, with evidence.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Seeing the system | Does the value-stream map show waits as well as work, and does it cover people and plans as well as tools? |
| Honest about old code | Does the profile name the billing core's truck factor and the assumptions in it that the new tariff must change? |
| Dependencies with risk | Does the dependency map tie each dependency to the condition of the code beneath it, and not only to a team and a date? |
| Invariants as properties | Could each invariant be turned into a test that would fail if the code ever allowed it to be broken? |
| Constraint thinking | Does the chosen lever act on the actual constraint, and does the answer predict where the constraint moves next? |
| Evidence over enthusiasm | Are the rewrite and the AI assistant judged on documented cases and evidence, with emerging practice labelled as such? |

#### Where you now stand

You can now see the engineering system as a system in its own right: the code, tools, platforms, teams and plans that decide how fast and how safely a product can change. You can map how a change travels through it, read the defaults its history left behind, tie a large change's dependencies to the condition of the code beneath them, and choose among four levers knowing that each pulled alone moves the constraint somewhere else. You have also met the change this book will follow, Verified Resale, and the module at its center, barcode issuance, with its one remaining author and its assumption that a ticket's identity never changes. Before any of the new code can be written, that old code must be understood, put under test and made safe to change. Chapter 2 begins there, with the codebase: what complexity is, how debt accumulates and is measured, and how an organization changes code it did not write and does not fully understand.

### References

- Peter Naur, Brian Randell (eds.) — [*Software Engineering: Report on a Conference Sponsored by the NATO Science Committee, Garmisch, Germany, 7th to 11th October 1968*](http://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1968.PDF). NATO Scientific Affairs Division, 1969 — free online.
- J. N. Buxton, B. Randell (eds.) — [*Software Engineering Techniques: Report on a Conference Sponsored by the NATO Science Committee, Rome, Italy, 27th to 31st October 1969*](http://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1969.PDF). NATO Scientific Affairs Division, 1970 — free online.
- Brian Randell — [*The 1968/69 NATO Software Engineering Reports*](http://homepages.cs.ncl.ac.uk/brian.randell/NATO/NATOReports/index.html). Dagstuhl Seminar 9635, History of Software Engineering, 1996 — free online.
- Edsger W. Dijkstra — [*The Humble Programmer*](https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html). Communications of the ACM 15(10), 1972 — free online.
- Titus Winters, Tom Manshreck, Hyrum Wright — [*Software Engineering at Google: Lessons Learned from Programming Over Time*](https://abseil.io/resources/swe-book). O'Reilly, 2020 — free online.
- Nicole Forsgren, Jez Humble, Gene Kim — [*Accelerate: The Science of Lean Software and DevOps*](https://itrevolution.com/product/accelerate/). IT Revolution, 2018.
- Google Cloud and DORA — [*Accelerate State of DevOps Report 2024*](https://dora.dev/research/2024/dora-report/). Google Cloud, 2024 — free online.
- Abi Noda, Margaret-Anne Storey, Nicole Forsgren, Michaela Greiler — [*DevEx: What Actually Drives Productivity*](https://queue.acm.org/detail.cfm?id=3595878). ACM Queue 21(2), 2023 — free online.
- M. M. Lehman — [*Programs, Life Cycles, and Laws of Software Evolution*](https://doi.org/10.1109/PROC.1980.11805). Proceedings of the IEEE 68(9), 1980.
- Melvin E. Conway — [*How Do Committees Invent?*](https://www.melconway.com/Home/Committees_Paper.html). Datamation, April 1968 — free online.
- Joel Becker, Nate Rush, Beth Barnes, David Rein — [*Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). METR, 2025 — free online.
- Guilherme Avelino, Leonardo Passos, André Hora, Marco Tulio Valente — [*A Novel Approach for Estimating Truck Factors*](https://arxiv.org/abs/1604.06766). Proceedings of the 24th IEEE International Conference on Program Comprehension, 2016 — free online.
- Matthew Skelton, Manuel Pais — [*Team Topologies: Organizing Business and Technology Teams for Fast Flow*, 2nd ed.](https://teamtopologies.com/book). IT Revolution, 2025.
- Eliyahu M. Goldratt, Jeff Cox — *The Goal: A Process of Ongoing Improvement*. North River Press, 1984.
- Joel Spolsky — [*Things You Should Never Do, Part I*](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/). Joel on Software, 2000 — free online.
- Slaughter and May — *Independent Review of the TSB IT Migration*. TSB Bank, 2019 — free online.

---

## Chapter 2: The Codebase — Design, Debt, and Change {#ch2}

> "Shipping first time code is like going into debt." — Ward Cunningham

Every codebase begins as a record of what its authors understood on the day they wrote it. The understanding was always partial, because nobody knows a domain fully before building software for it, and it was always local to a handful of people, because a young company is a handful of people. Then the company lives on. The domain turns out to be stranger than anyone thought, new people arrive who never shared the original understanding, and the code is asked to do things its authors could not have imagined. The question of this chapter is how a codebase stays changeable through all of that: how we keep its complexity within what people can hold in their heads, how we tell which of its imperfections actually cost us something, and how we change old code that nobody fully understands and every customer passes through.

The most famous answer to part of that question was given in two pages. In 1992 Ward Cunningham was director of research and development at Wyatt Software, which built WyCASH+, a portfolio management system for cash securities, the short-dated instruments that treasurers hold for months rather than years. It was written in Smalltalk by a small team, each member of which kept, in Cunningham's words, "general knowledge of all aspects of the roughly four megabytes of source code". He wrote up the experience for the Object-Oriented Programming, Systems, Languages and Applications conference (OOPSLA) held in Vancouver that October, and in the middle of an otherwise modest report he set down a passage the industry has been quoting ever since: "Shipping first time code is like going into debt. A little debt speeds development so long as it is paid back promptly with a rewrite. … The danger occurs when the debt is not repaid. Every minute spent on not-quite-right code counts as interest on that debt. Entire engineering organizations can be brought to a stand-still under the debt load of an unconsolidated implementation, object-oriented or otherwise."

Two details of that passage are easy to miss. The first is the instrument of repayment: in 1992 Cunningham wrote "a rewrite", meaning revising and consolidating code until it matched what the team had since learned; the word "refactoring", which his later retellings use, was only then being defined in a doctoral thesis at Illinois. The second sits two sentences earlier, where he names the cost of debt that is never repaid: immature code in excess makes a program "unmasterable, leading to extreme specialization of programmers and finally an inflexible product." He named the human cost of debt, the knowledge that concentrates in too few heads, before the industry had a name for its cost in code. We will meet both halves of that cost at Encore.

Encore is four months into Verified Resale. The bet has been made, discovery is done, and the Resale team has formed out of people from Orders & Payments and Partner APIs. Every resold ticket must be reissued under a new barcode, and the old one revoked at every gate. That puts the work on the oldest code Encore owns. Barcode issuance was written in the first year, when the company was nine engineers in one team, and it is now about eight years old. It sits inside Seat Inventory & Ticketing and belongs to the Inventory team. One person still understands it: Lena, one of the original nine, now on the Inventory team. It has no tests worth the name, and every ticket Encore has ever sold has passed through it. This chapter follows the Inventory and Resale teams as they measure that code, get it under test, and change it, and it draws from their work the practices that keep any large codebase changeable.

### 2.1 Complexity and Conceptual Integrity

#### What complexity is {#c2-what-complexity-is}

Complexity is a word engineers use loosely, often to mean nothing more than "code I did not write". John Ousterhout, who built systems such as the Tcl language and the Sprite operating system before writing *A Philosophy of Software Design*, gives a definition precise enough to work with: "Complexity is anything related to the structure of a software system that makes it hard to understand and modify the system." The definition is about structure and about people: a system is complex to the degree that those who must change it find it hard to change, whatever its size. In the terms the Architecture book{% include xref.html to="architecture" %} took from Fred Brooks, this is mostly accidental complexity: the kind we add through the shape of our solution, as distinct from the essential complexity that the domain itself imposes.

Ousterhout sees complexity through three symptoms. The first is **change amplification**: a seemingly simple change requires modifications in many places. The second is **cognitive load**: how much a developer must know to complete a change safely. (The Architecture book used the phrase in the *Team Topologies* sense, for what a whole team must hold in mind; Ousterhout means the knowledge one person needs for one change.) The third symptom is the worst: **unknown unknowns**, where it is not obvious which code must change, or what one must know, so that a developer can follow every rule and still break something. Behind all three he finds two causes. **Dependencies** mean a piece of code cannot be understood or changed in isolation. **Obscurity** means important information is not obvious, because a name is vague, a convention is undocumented, or a value means something different in two places.

Encore's checkout code showed all three symptoms in one change earlier this year, when an order needed to record whether it came from a resale. Adding a value to the order's origin enumeration touched nine files across the purchase saga, the order history projection and the fan app's receipt view: change amplification. The engineer had to know that the saga's compensation step, which undoes a reservation when payment fails, reads the same enumeration to decide whether seats return to the public or to a seller: cognitive load. And nothing in the code said that the Finance platform team's nightly reconciliation grouped orders by origin, so resale orders would have dropped out of it had a reviewer from that team not happened to see the pull request: an unknown unknown. Figure 2.1 sets the symptoms beside their causes.

| Symptom | What it feels like | Typical cause | Encore's example |
|---|---|---|---|
| Change amplification | One idea, many edits | Dependencies duplicated across modules | A new order origin touched nine files |
| Cognitive load | Much to know before a small change | Leaky interfaces, shared enumerations | The compensation step reads the same origin |
| Unknown unknowns | Nothing says what else must change | Obscurity: an undocumented consumer | Finance's reconciliation grouped by origin |

*Figure 2.1 — Ousterhout's three symptoms of complexity and their causes, with the order-origin change at Encore. The third row is the dangerous one, because it does not announce itself.*

Ousterhout adds that "Complexity is more apparent to readers than writers." The author of a change knows why each line is there, while the reader six months later has only the code, so the best judges of a change's complexity are the people who must change it next.

#### Deep modules {#c2-deep-modules}

If dependencies and obscurity cause complexity, the main tool against it is the module that hides things. Parnas made the decisive argument in 1972, that a module should be defined by the design decision it hides, and the Architecture book's Section 1.3{% include xref.html to="architecture:1.3" %} develops it, so we take it as given. What Ousterhout adds is a test we can apply to a single class or library. A **deep module** is one whose interface is small compared with the functionality it provides; its depth is the ratio between what it does for us and what we must know to use it. His favorite example is Unix file input and output. Five calls, `open`, `read`, `write`, `lseek` and `close`, stand in front of an implementation that manages disk layout, caching, permissions, devices and concurrent access, and a program can use files for years without learning any of that. A **shallow module** has an interface nearly as complicated as its implementation, so it costs almost as much to learn as it saves.

Shallow modules multiply in codebases that follow "small classes, small methods" as a rule. Ousterhout calls the condition "classitis" and describes it plainly: "Classitis may result in classes that are individually simple, but it increases the complexity of the overall system." Each class adds an interface to learn and a boundary to cross, and a reader chasing one behavior through seven three-line classes has paid seven times for something one class could have hidden. This is contested ground: in 2024 Ousterhout and Robert C. Martin published a long written debate on method length, comments and decomposition, in which two experienced designers disagree in good faith. What survives the debate is the test itself: for each module, compare what its users must know with what it spares them.

A theater box office is a good picture of a deep module. The fan sees a window and a person; behind them sit the seating plan, the promoter's holds, the house seats, the accessible places, the band's guest list and the rules about each. The fan asks for two seats and gets two seats. The analogy breaks where software differs from people: a clerk can explain an exception in words, while a module that hides too much leaves its callers baffled when something unusual happens, which is why depth is measured as a ratio.

Applied to Encore's barcode issuer, the test gave an uncomfortable answer. Its public surface had grown to 23 methods over eight years, several of them variants of one another with a flag for a festival pass, a box-office sale or a ticket from before the year-four split into services. Callers chose the variant, so every caller had to understand the distinctions the issuer should have hidden, and that shallowness was one reason its last author was consulted on so many changes.

#### Pulling complexity downward {#c2-pull-complexity-down}

A module's author usually understands its hard cases better than any caller does, and there is one author and many callers. Ousterhout draws the consequence: it is better for a module to absorb a difficult case once, inside, than to make every caller deal with it. He calls this pulling complexity downward. Its sharpest form is what he calls defining errors out of existence, which means designing an operation so that a situation that would otherwise be an error is simply part of its normal meaning. Unix, in his best example, lets a program delete a file that another program has open: the name disappears at once and the storage is reclaimed when the last user closes it, whereas Windows long refused such deletions and pushed the problem back onto users and programs.

The everyday version of this idea is idempotence. The Architecture book's Section 4.1 gave the network reason for it: any operation that crosses a network will be retried, so it must be safe to receive twice. The design reason is just as strong. An idempotent operation removes a whole class of error paths from every caller, because a caller that is unsure whether its request arrived can simply send it again.

The Reissue operation that Verified Resale needs shows both the power of the idea and its limit. A resale purchase triggers a reissue, and the caller may time out and retry; if the retry produced a second new barcode, the buyer would hold two tickets. So a retried reissue request carrying the same idempotency key returns the original result, and every caller is spared the question of whether its first attempt landed. It would be easy to go further and say that reissuing a ticket twice is a no-op, and that would be wrong, because a ticket bought on resale can legitimately be resold again, and the second resale needs a second reissue under a new identity. Ousterhout is careful here too: an error should be defined away only when the caller has nothing to decide. A request naming a ticket identity already revoked by another resale is a genuine conflict about which the caller must tell the buyer something, so the interface returns it. The Inventory team's interface came out at a dozen lines:

```kotlin
/** Reissues a sold ticket to a new holder under a new, opaque identity.
 *  The old identity is revoked at every gate in the same transaction. */
interface Reissue {
    fun reissue(request: ReissueRequest): ReissueOutcome
}

data class ReissueRequest(
    val idempotencyKey: IdempotencyKey, // one per resale; a retry reuses it
    val ticketId: TicketId,             // the identity the seller holds now
    val newHolder: FanId,
    val resaleId: ResaleId,
)

sealed interface ReissueOutcome {
    data class Reissued(val newTicketId: TicketId, val revoked: TicketId) : ReissueOutcome
    data class Conflict(val currentTicketId: TicketId) : ReissueOutcome // already resold
}
```

Everything a caller does not need to decide, from check digits to revocation lists, stays behind that interface, and the one thing a caller must decide is returned as a value it cannot ignore.

#### Strategic and tactical programming {#c2-strategic-tactical}

Why do codebases accumulate shallow modules and leaked cases in the first place? Ousterhout's answer is a habit of mind he calls tactical programming: the goal is to get the next feature working, and any design thought that does not serve that goal is postponed. Each postponement is small and defensible, and their sum is what the next team inherits. He describes its extreme form, the "tactical tornado", a prolific programmer who turns out features faster than anyone else and leaves the code a little worse with each one; "They are rarely considered heroes by the engineers who must work with their code in the future." The opposite habit, strategic programming, treats working code as necessary but insufficient, and treats the structure of the system as the main thing being built.

Ousterhout puts a number on the habit: "I suggest spending about 10–20% of your total development time on investments." The figure is a seasoned designer's advice, without measurement behind it, and since he expects the investment to pay back "within a few months", it fits code that will be thrown away sooner poorly. Its main use is as a standard against which a team can notice that its real figure is zero. David Farley makes the broader point in *Modern Software Engineering* (2021): engineering, as he frames it, means becoming expert at two things, at learning and at managing complexity, and the second is impossible for a team that never spends time on structure.

It would be unfair to call Encore's year-one barcode code tactical in this sense. Nine engineers wrote it to fit what they understood about tickets, and they understood a ticket as something issued once to one fan and scanned once at one door. Nobody then imagined a ticket changing owners. The code is debt in Cunningham's sense, faithful to an understanding that has since moved on. Code written carelessly calls for a conversation about habits; code written well for a world that has since changed calls for consolidation, and for the help of its authors, who know best what the world used to be.

#### Conceptual integrity across forty teams {#c2-conceptual-integrity}

Brooks wrote in *The Mythical Man-Month*: "I will contend that conceptual integrity is the most important consideration in system design." He meant that a system should reflect one set of design ideas, so that a person who has learned one part can predict the rest, and he argued that such integrity comes from a few minds. That is easy at nine engineers, where the few minds are the whole company. At 400 engineers in 40 teams it cannot be done literally, and any attempt to route every design question through a small group of architects produces a queue, which the Architecture book's last chapter argued against at length.

The mechanisms that do work at scale are humbler than a chief architect, and *Software Engineering at Google* describes them well in its chapter on style guides. A rule earns its place only if it pulls its weight; the rules optimize for the reader rather than the writer; they favor consistency; they forbid constructs that are error-prone or surprising; and they concede to practicalities. Two lines from that chapter capture the spirit: "It's the consistency of having one answer rather than the answer itself that is the valuable part," and "Documenting the reasoning behind a given decision gives us the advantage of being able to recognize when things need to change." A rule with its reason beside it can be argued with and retired when the reason lapses; a rule without one becomes folklore.

Publishing has long worked this way. A publishing house keeps a style sheet, often built on a reference such as *The Chicago Manual of Style*, so that many authors and copy editors produce books that read as if one careful person had prepared them all, and readers spend their attention on the argument and none on the commas. The analogy breaks at enforcement. A copy editor reads every page, while no person can read every change at Encore, so Encore's style guides, one per language, each with an owning group and a reason beside every rule, are enforced wherever possible by formatters and linters that run before a human reviewer sees the code. The mechanics of owners and automated review belong to Sections 4.2 and 4.3. To these rules we add the habit Ousterhout calls "design it twice": sketching a second, different design before committing to the first, which is cheap and often shows the first design's weaknesses while they are still cheap to fix.

**Recap.** Complexity is whatever in a system's structure makes it hard to understand and change, felt as change amplification, cognitive load and unknown unknowns, and caused by dependencies and obscurity. Deep modules, which hide much behind a small interface, and operations that absorb hard cases once instead of in every caller, are the main defenses. At forty teams, conceptual integrity survives through written rules that carry their reasons and are applied by tools.

**Exercise 2.1.** Pick one module your team owns. List its interface, then list what it hides. Is it deep or shallow? Name one error its callers handle that the module could define away, and one it must keep returning because callers have a real decision to make.

### 2.2 Refactoring and Tidying

#### Behavior-preserving change in small steps {#c2-small-steps}

Design is never finished, so most design happens to code that already exists. The discipline for doing it safely has a name and a lineage. **Refactoring** is a change to the internal structure of software that makes it easier to understand or cheaper to modify without changing its observable behavior. William Opdyke gave the idea its first thorough academic treatment in his 1992 doctoral thesis at the University of Illinois, *Refactoring Object-Oriented Frameworks*, written under Ralph Johnson in the same year as Cunningham's experience report, and Martin Fowler's *Refactoring* (1999, second edition 2018) turned it into a working vocabulary. Each refactoring in Fowler's catalog, such as Extract Function, Move Field or Replace Conditional with Polymorphism, is a named sequence of small steps, each of which leaves the code compiling and its tests passing.

The value of small steps is that each can be checked. A large restructuring done in one stroke may be correct, but nobody can tell; a sequence of named steps can be verified one at a time, by the tests and by a reviewer who recognizes the name. Kent Beck put the strategy into one sentence: "for each desired change, make the change easy (warning: this may be hard), then make the easy change." It divides work into a structural part and a behavioral part, and suggests that the first is often the larger. Named refactorings also make changes legible to reviewers when a machine has made them, which matters more now that assistants propose so many of them, a matter Chapter 5 takes up.

The evidence that refactoring pays is real but qualified. Miryung Kim, Thomas Zimmermann and Nachiappan Nagappan surveyed engineers at Microsoft in 2012 and found that they used the word far more loosely than "behavior-preserving", and that many saw refactoring as risky. In Windows 7, the modules a dedicated team had refactored ended up with fewer dependencies between modules and fewer defects after release. The authors' later journal version qualifies that result, and we should hold it accordingly: deliberate refactoring of code that matters has measurable benefits, while the loose sense of the word promises nothing.

#### Two hats {#c2-two-hats}

Fowler credits Beck with the metaphor of two hats. When we add behavior, we wear one hat: we add tests and make them pass, and we do not restructure. When we refactor, we wear the other: we change structure, add no behavior, and expect every existing test to keep passing. We may swap hats every few minutes, but we wear only one at a time. Beck's *Tidy First?* (2023) carries the idea into how changes are submitted: structure changes and behavior changes go into separate pull requests, so that each can be reviewed for what it is.

Publishing again offers the picture. A structural edit moves chapters, cuts sections and changes an argument's order; a copy edit corrects grammar and house style. A good editor does not do both in one pass on the same pages, because an author reviewing the marked-up manuscript cannot tell whether a changed sentence was moved, cut or corrected, and so cannot judge any of the changes well. The same is true of a reviewer facing a pull request that renames 40 identifiers and also changes how refunds are calculated. The refund change, which is the one that matters, hides in the noise of the renames.

The cost of mixing reaches further than review. Kim Herzig and Andreas Zeller studied bug fixes in five Java projects in 2013 and found that up to 15% of them were tangled with unrelated changes, which caused at least 16.6% of source files to be wrongly associated with bugs by the tools that mine version history. Tangled commits damage the history itself, and every analysis built on that history, including the hotspot and coupling analyses of Section 2.3, inherits the damage. Encore's review guide therefore asks for structure and behavior in separate pull requests on the purchase path, and gives its reason in one line: so that a reviewer can see the behavior change on its own.

#### Tidyings {#c2-tidyings}

Not every structural change deserves the word refactoring. Beck's book names a smaller unit. A **tidying** is a structural change small enough to be done in minutes and safe enough to need no special justification. His catalog is modest on purpose: guard clauses that return early instead of nesting, deleting dead code, normalizing symmetries so that similar things look similar, reading order and cohesion order, explaining variables and explaining constants, explicit parameters, chunking statements, extracting a helper, and deleting comments that repeat the code. Their point is to make the next change easier to read, and they are done just before it, by the person about to make it.

Dead code is the tidying people most often skip, because it seems harmless: it is not called, so it cannot hurt. The Resilience book's Chapter 4 tells how Knight Capital lost more than $460 million in about 45 minutes in 2012 when a repurposed flag woke code that had been unused for years, so dead code carries a risk of its own, which deleting it removes.

The Inventory team's first changes to the barcode issuer were tidyings of exactly this kind. The issuer computed its check digit with three unexplained integers; an explaining constant named each one, and Lena, reading the pull request, wrote a sentence beside the constants explaining which scanner vendor's firmware had required them in year one. Two of the 23 public methods had had no callers since the year-four split, and were deleted. A deeply nested branch for festival passes became three guard clauses. Each pull request took less than an hour and changed no behavior, and together they turned a file that only one person could read into one that several people could begin to.

#### First, after, later, never {#c2-tidy-economics}

When should we tidy? Beck's answer is a question with four possible answers: first, before the behavior change; after it; later, as separate work; or never. Tidy first when the tidying makes the change cheaper and we are about to make it. Tidy after when the change has taught us what the structure should have been. Tidy later when the tidying is worthwhile but unrelated to today's work. And never, when the code will not change again, because structure that nobody will read pays nothing.

Beck grounds this in finance. A euro today is worth more than a euro tomorrow, so behavior delivered sooner has more value, which argues against tidying. But structure creates options, the ability to make future changes cheaply, and options have value even before we know which changes we will want, which argues for it. Beck then states what he calls Constantine's equivalence: the cost of software is approximately the cost of changing it, which is approximately the cost of its big changes, which is approximately its coupling. The equivalence names Larry Constantine because coupling and cohesion as design ideas come from him, first set out with Wayne Stevens and Glenford Myers in the *IBM Systems Journal* in 1974 and developed in Yourdon and Constantine's *Structured Design*. The Architecture book's Section 1.3 teaches the concepts; Beck's contribution is to connect them to money.

The connection gives engineers a vocabulary that product managers and finance already speak. "This module is ugly" persuades nobody outside the team; "every change here costs us an extra week, and we have 11 changes planned this year" can be weighed against a feature. Beck offers this as an argument from finance, without measurements behind it, and Encore uses it that way: as a frame for a decision, with the numbers taken from the team's own history.

#### Smells as prompts {#c2-smells}

Fowler and Beck catalog code smells, patterns that suggest a refactoring might help: shotgun surgery, where one change requires many small edits in many places; divergent change, where one module changes for many unrelated reasons; feature envy, where a function is more interested in another module's data than its own. They present smells as prompts for judgment, and they warn that no set of metrics rivals informed human intuition in deciding when to act.

The warning has empirical support. Dag Sjøberg and colleagues had six developers carry out the same maintenance tasks on four functionally equivalent Java systems, 298 files in all, and measured the effort each file required. Once they controlled for file size and for the number of changes made, none of the 12 smells they studied was significantly associated with more effort. Size and change count explained nearly all of it. The result should sober anyone who has proposed a smell count as a quality goal, and it points to the next section: if effort follows size and change, then change history is where to look.

**Recap.** Refactoring changes structure in small, named, checkable steps without changing behavior, and tidyings are its smallest unit, done just before the change that needs them. Structure and behavior belong in separate changes, because mixing them blinds the reviewer and corrupts the history every later analysis depends on. Beck's economics give us a language for when to tidy, and smells are prompts for judgment, since counting them predicts little.

**Exercise 2.2.** Take your last behavior change and split it, after the fact, into the tidying and the change. How many lines would each pull request have had, and which of the two would a reviewer have needed to read closely?

### 2.3 Technical Debt as Data

#### The metaphor and its drift {#c2-metaphor-drift}

In 2009, 17 years after the WyCash report, Cunningham recorded a short video explaining the debt metaphor, because, as he put it, "A lot of bloggers at least have explained the debt metaphor and confused it, I think, with the idea that you could write code poorly with the intention of doing a good job later." "I coined the debt metaphor to explain the refactoring that we were doing on the WyCash product," he said; if the program failed to align with what the team now understood about financial objects, they would keep stumbling over the disagreement, "which was like paying interest on a loan." Then he drew the line that bloggers had blurred: "I'm never in favor of writing code poorly, but I am in favor of writing code to reflect your current understanding of a problem even if that understanding is partial." The 2009 account is a faithful reading of the 1992 report, which spoke of consolidation through rewriting, but we should keep the dates apart: the coinage is from 1992, and the gloss about refactoring from 2009.

Cunningham mentioned in the same video that his interest in how metaphors shape thought came from George Lakoff and Mark Johnson's *Metaphors We Live By* (1980), and that is a good lens for what happened next. A metaphor imports a whole structure of thought. "Debt" brought principal, interest and repayment, which served his purpose, and also the idea that debt is a choice one makes to buy something now, which the industry ran with until "technical debt" meant any shortcut, any old code, any design the speaker disliked. Martin Fowler tried in 2009 to sort the meanings with a quadrant, crossing reckless with prudent and deliberate with inadvertent, so that "we don't have time for design" and "now we know how we should have done it" could be told apart. In 2016 a seminar of researchers at Dagstuhl, convened by Paris Avgeriou, Philippe Kruchten, Ipek Ozkaya and Carolyn Seaman, agreed on a definition centered on design or implementation constructs that are expedient in the short term but make future change more costly or impossible. Figure 2.2 lays the history out in order.

{% include diagrams/fig-2-2.svg %}

*Figure 2.2 — The debt metaphor from its coinage to its consensus definition. Cunningham's two statements stand 17 years apart, and the word for repayment changed between them, from "a rewrite" to "refactoring".*

In this book, **technical debt** is the gap between the structure of the code and the team's current understanding of the problem, measured by what it costs each change that must cross it. That definition is closer to Cunningham's than to common usage, and it has one practical virtue: it makes debt something we can find in data. "Our code is full of debt" ends an argument, because there is nothing to say in reply. "Changes to this file take four times longer than changes elsewhere, and we plan 11 of them this year" starts a decision. The rest of this section is about measuring such debt, and the measurements begin in version control.

#### Hotspots {#c2-hotspots}

In the late summer of 1854, during a cholera outbreak in Soho, the physician John Snow marked the deaths on a map of the streets and saw them cluster around the public water pump on Broad Street. He persuaded the parish authorities to remove the pump's handle. What he left us is a method: before deciding what to treat, find where the cases are. Adam Tornhill's *Your Code as a Crime Scene* applies the same habit of mind to code. A **hotspot** is code that is both complex and frequently changed, found by combining a complexity measure for each file with its change frequency mined from version control. Complex code that nobody touches costs little; simple code that changes daily costs little; code that is both complex and constantly changed is where effort and defects concentrate.

The evidence behind this is older and stronger than the vendor literature. Todd Graves and colleagues, studying the change history of a large, long-lived system in 2000, found that the number of past changes to a module predicted its future faults better than its size did. Thomas Ostrand, Elaine Weyuker and Robert Bell, predicting faults across 15 releases of large industrial systems, found that the 20% of files their model ranked highest contained about 83% of the faults on average. Nagappan and Ball showed in 2005 that churn measured relative to size predicted defect density in Windows. The common thread is that a small fraction of files attracts most change and most defects, and that version control already knows which files they are.

Snow's map breaks as an analogy at one point. Every mark on his map was a death, while most commits are healthy work, and a file that changes often may simply be where the business is moving fastest. A hotspot tells us where to look, and the looking is still ours to do. Tornhill's advice is to read them as trends over time, asking whether a hotspot's complexity is growing or shrinking, and to confirm each one with the people who work in it.

Encore's Developer Portal team added a hotspot report to the service registry the year before, and the Inventory and Resale teams ran it across the purchase-path repositories for the previous twelve months. Figure 2.3 shows the top five, set by size against the number of changes.

{% include diagrams/fig-2-3.svg %}

*Figure 2.3 — Encore's hotspot run on the purchase path, one year of history. Two of the top three files belong to barcode issuance, and nearly all their changes come from one person.*

That barcode issuance and the purchase saga's orchestrator sat at the top surprised nobody; they are where every new ticket type, payment rule and channel must land. The share of changes by each file's top author surprised everyone. The saga's changes were spread across many authors, while the barcode files' changes came almost entirely from one engineer, because every team that needed something from issuance had learned over the years to ask that person to make the change.

#### Change coupling {#c2-change-coupling}

Static analysis sees the dependencies written in the code: this file imports that one, this function calls that one. It cannot see the dependencies that live only in people's heads. **Change coupling** is the tendency of two files to change together over time even though nothing in the code links them, and it reveals exactly those hidden dependencies. Harald Gall, Karin Hajek and Mehdi Jazayeri introduced the idea in 1998, as logical coupling found in the release history of a telecommunications switching system, and Thomas Zimmermann and colleagues showed in 2004 that mining version histories this way could suggest to developers which other files a change would probably need.

The method has conditions, and they follow from Section 2.2. It assumes commits are cohesive, each containing one logical change. Tangled commits, large automated changes of the kind Section 2.5 describes, and formatting sweeps all create false coupling, because they touch many files for reasons unrelated to one another. A sound analysis filters out commits above a size threshold and commits made by bots. Across services, files rarely change in the same commit, so coupling has to be found through the work item that links the commits, or a time window around them.

At Encore the analysis was run by work item across repositories, and it found that 70% of the changes to `BarcodeFormats.kt` were accompanied, in the same work item, by a change to Venue Entry's offline validator, the code in the door scanners that checks a barcode without a network. That coupling is legitimate, since the scanners must understand every format the issuer produces, but nobody had written it down, and twice that year a format change had reached the issuer before the validator. It also found a stranger coupling, with the Support Tools agent console, to which Section 2.5 returns. Findings like these feed the decomposition work of the Architecture book's Sections 3.3{% include xref.html to="architecture:3.3" %} and 3.4; here they showed that the barcode format was a contract, though nobody had declared it one.

#### Knowledge maps and the truck factor {#c2-truck-factor}

That top-author share in Figure 2.3 is a knowledge map in miniature. A **knowledge map** shows, for each part of a codebase, who has written and changed it, and it is how the truck factor that Section 1.3 defined is estimated in practice. Guilherme Avelino and colleagues, whose finding that 65% of 133 popular open-source systems had a truck factor of two or less Section 1.3 cited, computed their estimates from exactly this kind of authorship data.

Ownership affects quality as well as risk. Christian Bird and colleagues found in a 2011 study of Windows that components with many minor contributors, people who made only a small share of the changes, had more defects. In 2008 Nagappan, Brendan Murphy and Victor Basili found that measures of organizational structure, such as how many engineers and how many parts of the organization touched a binary, predicted the failure-proneness of Windows Vista binaries better than churn, complexity, coverage or dependencies did. It is as close as we have to Conway's law made measurable. These results need caution, since a later study by Greiler, Herzig and Czerwonka found the link between ownership and quality in some projects and not in others, but their general shape is that both extremes cost something: ownership concentrated in one person risks continuity, and ownership scattered across many occasional contributors risks quality.

Two cautions govern these maps. Truck-factor algorithms measure authorship, only a proxy for understanding; someone who reviewed every change to a module may know it well and appear nowhere. And a knowledge map shows where the organization is fragile, so it must never be used to rank the people in it. Encore's rule for scorecards applies here too: teams see their own maps, leadership sees trends, and nobody sees a league table.

Barcode issuance had a truck factor of one, the 1992 report's "extreme specialization of programmers" in its purest form. The remedies are old and well practised. Pairing puts a second person beside the expert for real changes, so that knowledge transfers where it is used. Ensemble sessions, a whole team working on one problem at one screen, spread it faster at a higher price in hours. Rotating reviews through the module turns routine work into teaching. And a written guide to the module, its history, its quirks and the reasons behind them, keeps what the expert knows available when the expert is on holiday. From month five the Inventory team paired two engineers with Lena on every barcode change, and one of them began the guide. Raising a truck factor takes quarters, and Chapter 11 tells how far this one rose.

#### The business case and the debt register {#c2-business-case}

The case for repaying debt has to be made in currencies the business already counts: time, predictability and defects. Adam Tornhill and Markus Borg's "Code Red" study (2022) is the most direct evidence. Across 39 proprietary codebases and 30,737 files, code with low health scores had 15 times as many defects as healthy code, took on average 124% longer to resolve issues in, and had maximum cycle times nine times longer. The study is correlational, and its quality measure is the proprietary Code Health metric of CodeScene, where both authors work. Terese Besker, Antonio Martini and Jan Bosch found in 2019, in a longitudinal study of 43 developers, that they reported wasting about 23% of their working time because of technical debt; the figure is self-reported and says most about how much developers feel the drag.

Encore's own numbers were more persuasive than either study, because they were Encore's. Over the year, the median change touching barcode issuance took 11 days from first commit to production, against two days for the rest of Seat Inventory & Ticketing, and the gap came largely from the wait for the one person who could review it. Verified Resale's plan called for at least 14 changes to that code before launch. That arithmetic went into the quarterly plan as a request for capacity, which Section 10.4 describes, and it was granted without much argument.

What the arithmetic needed was a place to live after the plan was approved. Philippe Kruchten, Robert Nord and Ipek Ozkaya's *Managing Technical Debt* (2019) recommends recording debt items explicitly, and the practice has a simple form. A **debt register** is a list of known debt items, each with its location, the interest it charges, an owner, and a trigger that forces repayment. The trigger is what keeps the register honest: an item without one is a complaint, and an item with one is a commitment that something will happen when a stated condition arrives. Encore's register lives beside each service's entry in the service registry, and its first barcode entry read:

```yaml
- id: INV-DEBT-017
  where: ticketing/barcode/BarcodeIssuer.kt (issue* variants)
  what: 19 public issue variants; callers choose by channel and era
  interest: median change 11 days vs 2 elsewhere; one reviewer
  owner: Inventory team
  trigger: before the first production reissue, or before any new channel
  repay: collapse to one issue() with a typed request, behind the reissue seam
  decided: month 5, Year 9 (quarterly plan)
```

The entry answers, once and in writing, the questions the team would otherwise have answered differently every time someone asked them.

**Recap.** Cunningham's debt was the gap between code and current understanding, repaid by consolidation; its drift into "anything we dislike" made the word end arguments it should start. Version control holds the data to measure it, through hotspots, change coupling and knowledge maps, and each item of debt is written down with its interest, an owner and a trigger.

**Exercise 2.3.** Run a hotspot analysis on one repository for the last year. Before looking at the result, ask the team to name the five files they expect at the top. Compare the two lists, and for each surprise, write one debt-register entry with interest, owner and trigger.

### 2.4 Legacy and Modernization

#### Legacy is code without tests {#c2-legacy-defined}

The word "legacy" usually carries a sneer, and the sneer gets the problem wrong. Michael Feathers, in *Working Effectively with Legacy Code* (2004), offers a definition that moves attention from the age of the code to the thing that actually makes it frightening: "To me, legacy code is simply code without tests." The definition earns its place because it names the remedy in the same breath as the condition. **Legacy code** is code we cannot change safely because nothing will tell us when we have broken it. Code written last month without tests is legacy in this sense, and eight-year-old code with good tests is not.

Marianne Bellotti, who modernized government systems with the United States Digital Service, makes a complementary point in *Kill It with Fire* (2021): old systems survive because they were successful, well fitted to the constraints of their time, and modernizing them means respecting what they got right as well as fixing what has aged. The Architecture book's Section 3.4 made the same argument. Encore's barcode issuer had issued every ticket the company ever sold, through two changes of scanner vendor, the year-four split into services and the year-eight move to rotating barcodes. Whatever was wrong with it, it had been right about a great many things, and the first task was to find out exactly which.

#### The legacy change algorithm {#c2-legacy-algorithm}

Feathers gives a procedure for changing code without tests, and its value lies in its order: identify the change points; find the test points, where tests can observe the change's effects; break the dependencies that keep the code out of a test harness; write the tests; and only then make the change and refactor. The order matters because the instinct of every engineer facing frightening code is to begin at step five, carefully, and the procedure exists to stop us. Feathers adds two tools for choosing test points: effect sketches, which trace what a change can affect, and pinch points, narrow places in the code through which many effects pass, where a few tests can cover a great deal.

Figure 2.4 shows the procedure as the Inventory and Resale teams applied it between months four and nine.

{% include diagrams/fig-2-4.svg %}

*Figure 2.4 — Feathers's legacy change algorithm applied to Encore's barcode issuer. Most of the effort went into the third and fourth steps, breaking dependencies and writing tests; the change itself was small.*

#### Seams and characterization tests {#c2-seams-characterization}

Breaking dependencies needs somewhere to break them. Feathers calls such a place a seam. A **seam** is a place where we can alter a program's behavior without editing the code at that place. An object seam lets a test substitute a different object through an interface or a constructor parameter; a link seam substitutes a different library at build time; a preprocessing seam, in languages that have a preprocessor, substitutes at compile time. The barcode issuer needed object seams it did not yet have. It called the system clock directly, so no test could ask what happened when an event was rescheduled, and it fetched rotation secrets from the secret store directly, so no test could run without production credentials. Making each a constructor parameter, the technique Feathers calls Parameterize Constructor, changed no behavior and made every later test possible.

With seams in place, the tests that come first are of a particular kind. A **characterization test** records what the code actually does, so that we notice if a change alters it, whether or not that behavior is what anyone intended. It is a description of the present, with no claim about what is correct. Before renovating an old building, architects commission a measured survey of what is actually there, because the original drawings describe what someone planned, and decades of alterations lie between the plan and the walls. Characterization tests are that survey for code. The analogy breaks usefully: a building stands still while it is measured, and a codebase changes every day, so the survey must keep running in continuous integration for as long as anyone alters the code.

The practical tool for characterizing at scale is approval testing, sometimes called golden-master testing: feed the code a large set of inputs, record its outputs, and on every later run compare the new outputs with the recorded ones. The Inventory team replayed a year of issuance requests, with personal data removed, through the issuer in a test harness, and recorded every barcode, check digit and event. Eight years of quirks came to light. Festival passes carried the festival's code in place of any single day's event code. Tickets issued before the year-four split still carried an older check-digit scheme that the scanners accepted. A ticket for a rescheduled event kept its original event code forever. Nobody had complained about any of these, and a careless reissue would have broken every one. Each became a named test, written so that a reader could see it described the past without endorsing it:

```kotlin
// Characterization: pins what the issuer does today. Not a specification.
@Test fun `festival pass carries the festival code, not a day's event code`() {
    val pass = issuer.issue(sale(product = FESTIVAL_PASS, festival = "F-0412",
                                 days = listOf("E-20431", "E-20432")))
    assertTrue(pass.barcode.startsWith("0412"))
}

@Test fun `rescheduled event keeps its original event code`() {
    val ticket = issuer.issue(sale(event = "E-18807", rescheduledTo = "E-21950"))
    assertTrue(ticket.barcode.startsWith("18807"))
}
```

Chapter 3 asks what a test is worth and how a suite grows from tests like these into one that specifies behavior; here they serve as a net under the old code while the new code is built beside it.

#### Sprout and wrap {#c2-sprout-wrap}

With the old code characterized, the temptation is to edit it, and Feathers offers a better default: write new behavior as new, tested code, and call it from the old code with as small a change as possible. Sprout Method and Sprout Class put new behavior in a new method or class, called from one line in the old code. Wrap Method and Wrap Class put it around an existing method or class, adding something before or after the old behavior. In each case the new code is tested from birth, and the old code changes by a line or two that the characterization tests can vouch for.

Reissue was sprouted as a class, the interface of Section 2.1, living beside the issuer inside Seat Inventory & Ticketing and owned by the Inventory team. Whether Resale or Inventory should own it had been argued in a request for comments (RFC) and settled in an architecture decision record (ADR), as Section 9.5 describes: Inventory owns issuance and revocation, and Resale calls it. Inside, Reissue made exactly one call into the old issuer, through the pinch point the tests already covered, and did everything new, the revocation, the new opaque identity and the event for the ledger, in tested code of its own. Figure 2.5 shows the arrangement.

{% include diagrams/fig-2-5.svg %}

*Figure 2.5 — Reissue sprouted beside the old issuer. The new code is tested from birth, and its single call into the old code passes through the pinch point the characterization suite already covers.*

One line separates these techniques from a larger relative. Sprout and wrap work inside a class or a module. When a whole component must be replaced while the codebase keeps running, the pattern is branch by abstraction, which the Architecture book's Section 3.4{% include xref.html to="architecture:3.4" %} teaches at the scale of a system and Section 4.5 of this book applies within a codebase behind flags. The barcode format change that follows Reissue is of that larger kind.

#### A modernization without a rewrite {#c2-modernization}

Every team that inherits old code feels the pull of the rewrite, and the Architecture book's Section 3.4{% include xref.html to="architecture:3.4" %} has already named the pull: the second-system effect, and the strangler fig as the pattern that replaces a system piece by piece instead. What remains is the running of the program, where modernizations most often fail, and Bellotti's book is a good guide to it, drawn from experience. The claim that rewrites usually fail is itself mostly anecdote, the best known being Joel Spolsky's 2000 essay on Netscape's decision to rewrite its browser from scratch, and we should not dress it up as a statistic.

Bellotti's central observation is that momentum is the scarce resource. A modernization is a long effort whose benefits arrive late, and it dies more often because people stop believing it will finish than because it hits a technical wall. So the program has to produce visible wins early, and it has to define "done" before it begins, since an effort without that definition tends to be abandoned at 80%, leaving both the old system and the new one to maintain. Decommissioning belongs in the scope from the start, because a modernization that adds a new path without removing the old one has increased the system's complexity. And a team joining a modernization midway should diagnose before it acts: what has been done, what has been promised, and what the old system still does that nobody has written down.

Encore's plan for the barcode core followed these lines. It did not rewrite the issuer; it changed it in place behind seams, with the strangler pattern held in reserve should the in-place work stall. It defined done in one sentence: every ticket issued or reissued through one typed interface, the issue variants deleted, and a truck factor of at least three. It put the deletion of the old variants in the plan as debt item INV-DEBT-017 with a trigger. And it chose its first visible win carefully: the first characterization suite running in continuous integration, which the whole Inventory team could see, by month six. Chapter 11 tells how the plan held.

**Recap.** Legacy code is code without tests, and the remedy follows from the definition. Feathers's procedure puts the tests before the change: find the change points and a pinch point, break dependencies through seams, characterize what the code does today, then sprout or wrap new behavior in new, tested code. A modernization without a rewrite is run as a program, with momentum protected, done defined in advance and decommissioning in scope.

**Exercise 2.4.** Find the least-tested file among your top hotspots. Without changing a line of it, write three characterization tests that pin behavior you did not know it had. Then name the seam you would need to make the fourth test possible.

### 2.5 Changing Code at Scale

#### Programming over time {#c2-programming-over-time}

Everything so far could be practised by one team on one module. Scale adds a dimension that changes the economics of every practice: time multiplied by people. Titus Winters, in the opening chapter of *Software Engineering at Google*, put the distinction in one line: "Software engineering is programming integrated over time." A program written for a weekend need not survive a new compiler, a new library version or its author's departure; code meant to live for a decade must survive all of them, many times.

From that framing follows a policy test: "everything your organization must do repeatedly should be scalable in terms of human effort." A practice whose cost grows linearly with the codebase or the headcount will eventually consume the organization. At nine engineers, asking the author of the barcode code to review every change to it cost a few minutes a week. At 400 it became the 11-day wait of Section 2.3, because the changes grew with the company and the reviewers stayed at one. The practices in the rest of this section are those whose costs grow slowly.

#### Hyrum's law inside the walls {#c2-hyrums-law-inside}

The Architecture book's Section 7.2 stated Hyrum's law for public interfaces: with a sufficient number of users of an API, every observable behavior of the system will be depended on by somebody, whatever the contract promises. The law holds just as firmly inside a company, where it is easier to forget, because internal callers feel like colleagues.

The history of the Go language gives a clean public example. The Go 1 release in March 2012 made the iteration order of maps deliberately unpredictable, precisely so that programs could not come to depend on it. A new map implementation in Go 1.1 neglected to randomize iteration over maps of eight or fewer entries, so in Go 1.1 and 1.2 those small maps iterated in an order that was consistent on a given system. Programs came to depend on it, and when Go 1.3 reintroduced randomization for small maps in 2014, its release notes warned that code assuming a fixed order would break, adding that the problem would arise most often in tests. The designers had anticipated the dependency, and it formed anyway in the gap their own implementation left open. An older case is told by Joel Spolsky in his 2004 essay "How Microsoft Lost the API War": the game SimCity read memory after freeing it, and rather than break the game, Windows added a special mode for its memory allocator that it switched on when SimCity was running.

Encore's ticket identity had collected its own dependents. The legacy barcode, and the identity it encodes, begins with the event code, an accident of how the year-one issuer derived identity from order and seat, never documented as a promise. Rowmate's integration with Partner Listings, written in year six, read that prefix to match a ticket a seller had forwarded to the right event page. The dependency survived the move to rotating barcodes in year eight, because rotation was built around the existing identity without changing it, and so for three years nobody noticed it. It surfaced only when Verified Resale replaced the identity itself. Partners had been told at month 2 that reissued tickets would carry a new, opaque identity, and the old format stays accepted on the partner API until month 14, which keeps Encore's promise of 12 months' notice. Even so, Rowmate's matching code failed against the sandbox when Rowmate began certification in month 9, and Rowmate's engineers rewrote it during certification, before any fan depended on it. Inside Encore, the change-coupling analysis of Section 2.3 found the same dependency in the Support Tools agent console, which derived a ticket's event from the first digits of its barcode so that agents could find a fan's booking quickly. Neither dependent had asked permission, and nothing had told either that it could not: the prefix was observable, and that was enough.

The lesson Encore drew is built into the new design. The ticket identity that Reissue issues is opaque: a `ticket_id` that carries no meaning anyone can parse. Partners receive it through the API and never parse barcodes, which rotate in any case, and internal callers that need a ticket's event ask Seat Inventory & Ticketing for it. An identifier with nothing observable inside it gives Hyrum's law nothing to work with. A decade of maintaining an open-source library has convinced me that documentation does not prevent such dependencies; only removing the observable behavior does, or, where it must stay observable, committing to it.

That commitment has a name inside Google, recorded in the same book. The Beyoncé Rule reads: "If you liked it, you should have put a CI test on it." It is the internal remedy for Hyrum's law, and it cuts in both directions. A team that depends on another team's behavior should protect that dependency with a test in the provider's continuous integration (CI), so that the provider learns of the dependency before breaking it. And a provider making a change that breaks no test is entitled to make it. At Encore, Venue Entry's offline validator now contributes tests to the barcode code's suite, so that the coupling Section 2.3 found is declared where the issuer's owners will see it.

#### Large-scale changes {#c2-large-scale-changes}

Some changes cannot be made in one commit. Hyrum Wright's chapter in *Software Engineering at Google* defines a **large-scale change (LSC)** as "any set of changes that are logically related but cannot practically be submitted as a single atomic unit", whether because they touch too many files for any build to test at once, or because they cross too many owners for any single review. Google generates such changes with compiler-aware tools, such as ClangMR for C++, which Wright and colleagues described in 2013, and Refaster for Java. A system called Rosie splits each change into shards along project and ownership lines, tests each shard independently, routes it to the owners or to a global approver, and submits it. The migration away from `scoped_ptr` touched more than 500,000 references and at its peak landed more than 700 changes a day touching more than 15,000 files. Google reports that changes of this kind account for 10% to 20% of the changes in a typical project.

The process has four steps: authorization, in which the change is approved as worth making across the codebase; change creation, by tools; sharding and submitting; and cleanup, which removes the old way once the new one has spread. Aviation has run fleet-wide changes this way for decades. When an authority such as the U.S. Federal Aviation Administration issues an airworthiness directive, every affected aircraft must be inspected or modified by a deadline, aircraft by aircraft, each signed off separately: one decision, many small executions, each verified on its own. The parallel breaks at the source of authority. A directive is law, while a large-scale change inside a company rests only on the authority the organization grants its global approvers, a grant that must be made explicitly.

The method has conditions. It needs tools that understand the language's types, so that generated changes are correct by construction; a CI system that can test each shard cheaply; and an ownership policy that lets a global approver land a mechanical change in a team's code without that team's line-by-line review. Without those, the honest alternative is a campaign: a tracked migration in which each team makes the change in its own code, supported by a codemod and a dashboard. Stripe's account of its move from Flow to TypeScript shows a third shape: its engineers built a codemod, later open-sourced, and on 6 March 2022 converted more than 3.7 million lines of the Dashboard codebase in a single pull request.

Encore's barcode format change, which moves every internal caller from parsing barcodes to asking for the opaque `ticket_id`, will be a change of this kind, across 11 services, and Chapter 11 follows it. Machine assistance now writes many such changes, and Chapter 5 examines where it helps and how its work is checked; the mechanics described here, of sharding, testing, approving and landing, are the same whoever writes the shards.

#### Deprecation as a process {#c2-deprecation}

Large-scale changes move callers to the new way. Deprecation removes the old one, and it is the half of the work organizations most often neglect, because removing code earns little praise. Wright's chapter on deprecation treats code as a liability to be justified by what it provides, so that two ways of doing one thing cost maintenance, security patches and the confusion of every new engineer who finds both.

The chapter distinguishes two kinds. Advisory deprecation marks the old way as discouraged and hopes callers will move; Google's verdict on it is "Hope is not a strategy," because callers with working code and other priorities rarely move on their own. Compulsory deprecation has a deadline and enforcement, and it works only when someone owns it, with time allotted, because the last few callers are always the hardest. Figure 2.6 sets the code-level mechanics side by side.

| Mechanism | Advisory | Compulsory |
|---|---|---|
| Discovery of callers | Code search, when someone looks | Code search plus runtime logging, kept current by the owner |
| Warnings | On every use, everywhere | Only on newly changed lines, so they are acted on |
| New uses | Allowed | Blocked by a visibility allowlist or a build rule |
| Migration | Each team, when it chooses | Tooling or an LSC, with a date |
| Owner | Often nobody | A named team, staffed for the work |

*Figure 2.6 — Advisory and compulsory deprecation at the level of code. Encore uses the right-hand column for anything it intends to delete.*

Two details in the figure carry more weight than they seem to. Google shows deprecation warnings only on lines a developer is already changing, because warnings on every old use teach people to ignore all warnings. And it prevents backsliding with visibility allowlists in its build system, which list exactly which code may still depend on the deprecated target, so that the list can only shrink. Encore gets the same effect from an ArchUnit rule that fails the build for any new import of a deprecated package outside a named allowlist. When Encore deprecated the legacy barcode parser in month eight, the Inventory team owned the deprecation, the allowlist named the four remaining callers, and the build turned away a fifth in its first week. Platform-wide deprecation campaigns, with brownouts and partner timelines, are Chapter 6's subject.

#### Dependencies and one version {#c2-one-version}

The last practice concerns the code we did not write. *Software Engineering at Google*, in its chapter on version control, states what it calls the One-Version Rule: "For every dependency in our repository, there must be only one version of that dependency to choose." Violations, it says, "lead to merge strategy discussions, diamond dependencies, lost work, and wasted effort." In a diamond dependency, two libraries a service uses depend on different versions of a third, and the service cannot satisfy both. Google is candid that the rule "is not hard and fast", and that what matters is adhering to the one-version principle as far as possible, monorepo or not. Its chapter on dependency management adds that its policy of at least two owners for every third-party package has failed when the owners moved on.

A company with many repositories, like Encore, can approach the rule without a monorepo. A shared version catalog or bill of materials (BOM), included in every service's build through the golden-path template, names one version of each third-party library, and automated update tools such as Renovate or Dependabot open pull requests to move each service to the catalog's version, gated by that service's own tests. Section 4.2 weighs the monorepo against the polyrepo; the one-version discipline is available under either.

Who does the upgrading is a policy choice, and Google's "Live at Head" places the burden on whoever changes the shared version. Encore made the same choice explicitly: the team that owns a library's entry in the catalog upgrades every caller, with the update tools doing the mechanical part. Its worked case was the date-time library on which every service that computes a schedule depends, whose catalog entry belongs to the Event Setup team. A survey in month six found four versions in use across Encore's services, two of them bundling different releases of the time-zone database. That mattered for Verified Resale in a specific way: the default resale window closes two hours before doors, and the Resale service and the gate apps must agree on when that is, in every time zone where Encore sells. Event Setup moved all services to one version in three weeks, most of it through automated pull requests, and added a build check that fails any service declaring its own version of the library.

**Recap.** At scale, the test of any practice is whether its cost grows more slowly than the organization. Hyrum's law applies inside the company, and its remedies are to remove observable accidents, such as a meaningful prefix in an identifier, and to protect deliberate dependencies with tests in the provider's CI. Large-scale changes land as many small, tested shards; deprecation finishes only with an owner, a date and enforcement; and each dependency has one version, upgraded by its owner.

**Exercise 2.5.** For one internal library your team provides, list the observable behaviors callers might depend on that no test protects: orderings, formats, timings, error messages, identifiers with structure inside them. For each, decide whether to remove it, or to commit to it with a test.

### Kata: The Rostering Rules

> **Your brief: "Ledgermoor."** Ledgermoor is a 12-year-old crew-scheduling SaaS used by 31 airlines in eight EU countries, from regional carriers to two mid-size flag carriers, building the monthly rosters of about 60,000 pilots and cabin crew. It has 120 engineers in 14 teams. At its heart sits the rostering-rules engine, roughly 60,000 lines written in the company's first three years, which checks every pairing and roster against the EU's flight-time limitations, national variations and each airline's labor agreement; its two principal authors left in the last 18 months, and one engineer who worked beside them is consulted on nearly every change. Test coverage averages about 55% across the codebase and 6% in the engine. Labor agreements are renegotiated every year or two, and a change to the engine takes a median of 19 days from first commit to production, against four elsewhere. Twice last year a rule change produced rosters that broke a crew member's minimum rest, caught by airlines' crew planners before publication. Leadership has asked for a rewrite; the head of engineering has asked you instead for a plan. You have one quarter and one team of seven, and two airlines' new labor agreements must be enforced by the engine before the winter schedule begins.

**Deliverables:**

1. **Hotspot and knowledge map** — Describe the analysis of the engine's history: the window, the complexity measure, how you will filter tangled and automated commits, and how you will show where knowledge has concentrated. Predict what it will find.
2. **Debt register** — Write the first five entries, each with location, interest in days or defects, owner and trigger. At least one must be debt the team chooses not to repay this quarter.
3. **Characterization strategy** — Explain how you will pin what the engine does today: the pinch points, the seams you must create, and how last year's published rosters, with crew identities removed, become approval-test inputs. Say who decides whether a quirk is preserved or fixed.
4. **The first change** — Show how one of the new labor-agreement rules enters the engine as sprouted or wrapped code, with the line it changes in the old code and the tests that vouch for it.
5. **Knowledge plan** — Show how the engine's truck factor will rise this quarter, and how you will know it has, without ranking anyone.
6. **The case against the rewrite** — Write the one-page argument for leadership in days, predictability and defects, with the quarter's definition of done and the conditions under which a strangler-fig replacement would become right.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Evidence before opinion | Does every claim about the engine rest on history, tests or measured cycle times, and not on its reputation? |
| Tests before change | Is the first rule change made only after the code it touches is characterized? |
| Honest debt | Does the register include interest, owners and triggers, and does it admit what will not be fixed? |
| Knowledge as risk | Does the plan raise the truck factor without turning the knowledge map into a ranking of people? |
| Momentum | Does the quarter produce a visible win early, and is "done" defined before the work begins? |
| Restraint | Is the rewrite argued against with numbers, and is the condition for reconsidering it stated? |

#### Where you now stand

You can now recognize complexity by its symptoms, design modules deep enough to hide their hard cases, and change structure in small, named steps kept apart from changes in behavior. You can find technical debt in version control and record it with interest, owners and triggers. You can change code that has no tests by characterizing it first and sprouting new behavior beside it, and you can reason about change across a large codebase, from Hyrum's law inside the company to one version of each dependency. All of it rests on tests, and the characterization tests that made the barcode issuer safe to change are not yet a strategy. Chapter 3 asks what a test is worth, and how a suite is designed so that it protects the five fairness invariants of Verified Resale without becoming the next thing nobody dares to change.

### References

- John Ousterhout — [*A Philosophy of Software Design*, 2nd ed.](https://web.stanford.edu/~ouster/cgi-bin/aposd.php). Yaknyam Press, 2021.
- Ward Cunningham — [*The WyCash Portfolio Management System*](http://c2.com/doc/oopsla92.html). OOPSLA '92 Experience Report, 1992 — free online.
- Ward Cunningham — [*Debt Metaphor* (video transcript)](https://wiki.c2.com/?WardExplainsDebtMetaphor). 2009 — free online.
- Michael C. Feathers — [*Working Effectively with Legacy Code*](https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055). Prentice Hall, 2004.
- Titus Winters, Tom Manshreck, Hyrum Wright (eds.) — [*Software Engineering at Google*](https://abseil.io/resources/swe-book). O'Reilly, 2020 — free online.
- Martin Fowler — [*Refactoring: Improving the Design of Existing Code*, 2nd ed.](https://refactoring.com/catalog/). Addison-Wesley, 2018.
- Kent Beck — *Tidy First? A Personal Exercise in Empirical Software Design*. O'Reilly, 2023.
- Adam Tornhill — [*Your Code as a Crime Scene*, 2nd ed.](https://pragprog.com/titles/atcrime2/your-code-as-a-crime-scene-second-edition/). Pragmatic Bookshelf, 2024.
- Adam Tornhill, Markus Borg — [*Code Red: The Business Impact of Code Quality*](https://arxiv.org/abs/2203.04374). International Conference on Technical Debt, 2022 — free online.
- Todd L. Graves, Alan F. Karr, J. S. Marron, Harvey Siy — [*Predicting Fault Incidence Using Software Change History*](https://doi.org/10.1109/32.859533). IEEE Transactions on Software Engineering, 2000.
- Guilherme Avelino, Leonardo Passos, Andre Hora, Marco Tulio Valente — [*A Novel Approach for Estimating Truck Factors*](https://arxiv.org/abs/1604.06766). ICPC, 2016 — free online.
- Marianne Bellotti — [*Kill It with Fire*](https://nostarch.com/kill-it-fire). No Starch Press, 2021.
- Hyrum K. Wright, Daniel Jasper, Manuel Klimek, Chandler Carruth, Zhanyong Wan — [*Large-Scale Automated Refactoring Using ClangMR*](https://doi.org/10.1109/ICSM.2013.93). IEEE ICSM, 2013.
- The Go Authors — [*Go 1.3 Release Notes*](https://go.dev/doc/go1.3). 2014 — free online.

---

## Chapter 3: Testing Strategy {#ch3}

> "Software is an expression of a highly detailed design and does not fail in the same sense as a mechanical system." — Ariane 5 Flight 501 Inquiry Board, 1996

What does a passing test tell us? The answer seems obvious: the code does what the test says it should. But a test says more than its assertions. Every test carries a picture of the world in which the code will run, the inputs it will see, the neighbors it will call, the order in which things will happen, and a green result means only that the code behaves well inside that picture. When the picture is accurate, the suite is among the most valuable things an engineering organization owns, a record of what the system should do, checked thousands of times a day. When the picture is wrong, the suite is worse than useless, because it lends the confidence of evidence to a guess about the world that nobody remembers making.

This chapter is about choosing what our tests should assume, and about spending a finite budget of effort on the tests that repay it. It begins with the suite that cleared the inertial reference software of Ariane 5 for its first flight in June 1996, and it ends with a kind of testing the Ariane engineers never had to imagine: evaluating a language model whose output differs every time we ask. Between them lie the ordinary disciplines of deciding what a test is worth, growing software in small steps, replacing the neighbors we cannot run with simulators we can trust, and keeping a few end-to-end journeys alive without letting them rule us.

Encore enters the chapter with tens of thousands of tests across forty teams, a developer survey in which flaky end-to-end tests ranked among the loudest complaints (Section 1.2), and a new product that will stress every layer of the suite. Barcode issuance, written by the original nine engineers in the company's first year and owned today by the Inventory team, was built on the assumption that a ticket is issued once. Its tests, such as they are, encode that assumption. Verified Resale will issue a ticket, revoke it and issue it again under a new identity, as often as fans resell it, with partners whose code Encore cannot run, a payment provider whose marketplace product splits the money four ways, and an organizer rule assistant whose answers a model drafts. Each is a test of the testing strategy itself.

### 3.1 What a Test Is Worth

#### The world a test assumes {#c3-world-a-test-assumes}

On 4 June 1996 the first Ariane 5 lifted off from Kourou, in French Guiana, carrying the European Space Agency's four Cluster satellites. About 37 seconds after main-engine ignition, half a minute into flight, both of the launcher's inertial reference systems failed within 72 milliseconds of each other. The on-board computer, now receiving a diagnostic bit pattern from the failed unit, read it as flight data and commanded full deflection of the nozzles. The launcher veered, began to break up under aerodynamic load, and destroyed itself at an altitude of about four kilometers. The inquiry board, chaired by the mathematician Jacques-Louis Lions, reported about six weeks later, in one of the clearest documents ever written about how software fails.

The mechanism was small. Software in the inertial reference system converted a 64-bit floating-point value, the horizontal bias, into a 16-bit signed integer. On Ariane 4 the value always fit. On Ariane 5, which builds horizontal velocity much faster in the early part of its trajectory, it did not, and the conversion raised an operand error. Of seven variables at risk of exactly this error, the designers had protected four and left three unprotected, the horizontal bias among them, to stay within a target of 80% maximum load on the computer. The system's specification said that on any exception the processor should shut down, because exception handling had been designed for random hardware failure, and under that assumption a shutdown hands control to the backup. The backup ran identical software on the same inputs, and it had already failed in the same way one data cycle earlier. The deepest irony is the one the board took care to record. The function that failed had no purpose after lift-off. It kept running for about 40 seconds into flight because Ariane 4 needed to be able to recover quickly from a hold late in the countdown, and the board noted that this behavior was not required for Ariane 5 at all.

What makes Ariane 501 a story about testing, more than about integer overflow, is the board's account of why nobody found the fault. The inertial reference system was reused from Ariane 4, "practically the same", in the report's words, "particularly as regards the software". It had flown successfully. When the Ariane 5 requirements were written, the report says, "it was jointly agreed not to include the Ariane 5 trajectory data in the SRI requirements and specification." In 1992 the project had also decided not to put the real inertial units in the loop during the closed-loop system simulation, using simulated outputs instead. So no test anywhere in the program ever fed the reused software the trajectory it would actually fly. The suite was not careless. It was faithful, with great rigor, to a world that no longer existed. The board concluded that had such a test been performed, by the supplier or as part of the acceptance test, "the failure mechanism would have been exposed," and two of its recommendations are worth quoting because they read like a testing strategy in miniature. The second: "Prepare a test facility including as much real equipment as technically feasible", with realistic inputs and complete closed-loop testing. The tenth: "Include trajectory data in specifications and test requirements." Figure 3.1 sets the flight that happened beside the world the tests assumed.

{% include diagrams/fig-3-1.svg %}

*Figure 3.1 — Ariane 501, schematic. In flight, both inertial reference systems met a trajectory their specification had left out and failed one data cycle apart; in test, simulated outputs stood in for the real units, and every test passed.*

Later writers drew different lessons. Jean-Marc Jézéquel and Bertrand Meyer argued in 1997 that a stated precondition on the reused routine would have exposed the error at the moment of reuse; Bashar Nuseibeh answered in the same year that the failure belonged to the system and its process more than to any one piece of code. Both are interpretations, and both are useful. The lesson I take for this chapter is narrower. A test suite is a model of the world, and reused code arrives with the old world's model intact, its tests still passing. Encore has paid for this lesson once already. The admission-rate change behind the Vesper Hale morning was approved on the strength of a load test run against a warm seat-map cache, a test that was perfectly sound for a world the on-sale did not live in (the Resilience book{% include xref.html to="resilience" %}, Section 2.3, and the Operations book's Chapter 6{% include xref.html to="operations:6" %} tell that story). Barcode issuance is Encore's own inertial reference system: old, trusted, reused for a purpose its authors never imagined, and tested, where it is tested at all, against a world in which a ticket is issued once.

#### The four pillars {#c3-four-pillars}

If a test is a model of the world, we need a way to judge whether a particular model is worth keeping. Vladimir Khorikov's *Unit Testing Principles, Practices, and Patterns* (2020) gives the most useful framework I know. He starts from the purpose of testing, which he states as enabling "sustainable growth of the software project", and he judges every test against four attributes, which he calls pillars. **Protection against regressions** is the test's chance of failing when a real bug is introduced. **Resistance to refactoring** is its chance of staying green when the code is restructured without changing its behavior. **Fast feedback** is how quickly it runs. **Maintainability** is how cheap it is to read, understand and keep running. A test's value is roughly the product of the four, so a test that scores zero on any one of them is worth nothing, however well it does on the others.

| Pillar | The question it asks | What destroys it | An Encore example |
|---|---|---|---|
| Protection against regressions | Would this test fail if the behavior broke? | Testing trivial code; asserting too little | A checkout test that never checks the amount charged |
| Resistance to refactoring | Would this test stay green if the behavior were kept but the code restructured? | Asserting on internal calls, private state or exact SQL | A barcode test that verifies the order of three repository calls |
| Fast feedback | How long until the author knows? | Real networks, sleeps, shared environments | A Seat Map test that waits 5 s for a cache to expire |
| Maintainability | How much effort does this test cost each time it is read or changed? | 40-line setups, opaque fixtures, copied helpers | A Resale test whose arrange section builds an entire event by hand |

*Figure 3.2 — The four pillars, after Khorikov. A test's worth is roughly their product, so one pillar at zero makes the test worthless.*

The pillars trade against one another. Protection and speed pull apart, because the tests that exercise the most real code are the slowest. Resistance to refactoring is the one Khorikov refuses to trade, and his reason is worth dwelling on. A test that fails when nothing is wrong is a false alarm, and false alarms teach the people who receive them that a red build means nothing. Google's *Software Engineering at Google* (2020) arrives at the same priority by a different road. It calls such a test **brittle**, "one that fails in the face of an unrelated change to production code that does not introduce any real bugs", and it opens its unit-testing chapter with an engineer whose brittle tests broke on a harmless refactor. DORA, the DevOps Research and Assessment program, puts it more plainly: "test failures should indicate a real defect". The pillars are a reasoned framework rather than a measured result, and their strength is that three independent sources converged on the same priority. A fire alarm that goes off whenever someone makes toast is soon unplugged, and the analogy holds closely here, with one difference: a building has one alarm, while a suite has thousands, and people learn to ignore all of them from the few that cry wolf.

#### Behavior, coverage and mutants {#c3-behavior-coverage-mutants}

The practical consequence is a rule easy to state and harder to keep: test what a caller can observe, and leave the implementation free to change. A test of the barcode issuance code should ask whether the issued ticket is valid at the gate, whether its identity is unique and whether a second request with the same idempotency key returns the same ticket. It should not ask which internal methods were called in which order, because that is precisely what a refactoring changes, and the Inventory team is about to refactor that code harder than it has ever been refactored (Section 2.4).

Coverage is where well-meaning organizations go astray, because numbers invite targets. Khorikov's verdict is exact: "coverage metrics are a good negative indicator but a bad positive one." Low coverage is a reliable sign of trouble, since code no test executes is code no test protects. High coverage proves very little, because, as Google's chapter on testing notes, coverage "only measures that a line was invoked, not what happened as a result." A test can execute every line of the fee-split code and assert nothing about the money. Google also observed what happens when the number becomes a target: "instead of treating 80% like a floor, engineers treat it like a ceiling." Encore's scorecards report coverage for each service for exactly this reason, as a warning light below a floor and nothing more.

A better question than "was this line executed?" is "would any test notice if this line were wrong?" **Mutation testing** asks it directly: a tool makes a small deliberate change to the code, flipping a comparison or deleting a statement, and checks whether some test fails. A surviving mutant marks a place where the suite would not notice a bug. Long dismissed as too expensive for real codebases, it was made practical at Google, as Goran Petrović and Marko Ivanković described in 2018, and the conditions of their success matter more than the technique. Google mutates only the lines changed in a code review, suppresses mutants in code where they are known to be unproductive, and shows the survivors to the author as review comments, with no score attached. By 2018 some 6,000 engineers had used it. A later study by the same group with Gordon Fraser and René Just, covering almost 15 million mutants, found that developers who were shown mutants went on to write more tests and stronger ones. Encore turned diff-based mutation on for two codebases where a quiet gap would be most expensive, the barcode core and the Resale service's fee arithmetic, and it reports nothing about mutants on any scorecard. A mutation score that became a target would repeat the coverage mistake one level up.

#### Sizes and shapes {#c3-sizes-and-shapes}

The Architecture book (Section 5.3) gave Encore's fleet its test pyramid, from many fast unit tests up to a handful of end-to-end journeys. It leaves open a practical question: when an engineer sits down to write the next test, how should they decide what kind it is? Google's answer separates two things that the pyramid blurs. A test's **size** is the resources it may use: a small test runs in a single process, with no sleeping, no disk and no network; a medium test is confined to a single machine and may talk to a real database on localhost; a large test may span machines. A test's **scope** is how much code it is meant to verify, from one function to a whole journey. Size and scope are, in Google's words, "two distinct dimensions for every test case". The distinction earns its keep because size, unlike scope, can be enforced: a build system can refuse a small test that opens a socket, which does more for determinism and speed than any exhortation. Google suggests a mix of roughly 80% narrow, 15% integration and 5% end-to-end by test count, which it explicitly calls its own version of Mike Cohn's pyramid, and it adds that every team's mix will differ.

Martin Fowler, surveying the arguments between pyramid, honeycomb and trophy in 2021, found that most came from people who meant different things by "unit test", some a solitary test of one class, others a sociable test of a cluster of real objects. Once the words are settled the shapes converge, and what matters is the quality Fowler borrows from Justin Searls, that tests should "run quickly & reliably, and only fail for useful reasons." The pyramid survives this scrutiny as a cost argument. Large tests cost more to run, more to debug and more to keep green, so we should buy as few as will do the job. It does not survive as a shape to hit: counting tests to check the proportions measures the shape and says nothing about the cost.

#### Doubles, and who owns them {#c3-test-doubles}

Every test that does not run the whole world must replace part of it, with what Gerard Meszaros named **test doubles** in *xUnit Test Patterns* (2007). Mock objects first appeared in print in 2000, in "Endo-Testing: Unit Testing with Mock Objects" by Tim Mackinnon, Steve Freeman and Philip Craig. The idea was a design technique as much as a testing one: by specifying the messages an object should send to its collaborators, the test helped discover the collaborators' interfaces. Fowler's essay "Mocks Aren't Stubs" later named the two schools that grew up around the technique. The **classical** school replaces only what it must and checks the final state; the **London** or mockist school replaces every collaborator and checks the interactions.

Both schools have produced good software, and long practice shows where they go wrong. Google's chapter on test doubles reports that the company learned "the hard way" that tests built heavily on mocking frameworks "required constant effort to maintain while rarely finding bugs", and its guidance is blunt: "A real implementation should be preferred over a test double," and where that is impractical, "the best option is often to use a fake", a lightweight working implementation of the same interface. Khorikov gives the most useful line to draw. A **managed dependency** is one only our service talks to, such as its own database; an **unmanaged dependency** is one whose interactions other systems can observe, such as a payment provider, a message bus or an email gateway. Use the real managed dependencies in integration tests, and reserve mocks for the unmanaged ones, where the interaction itself is the behavior a caller cares about. Charging a card twice is a bug the payment provider observes, so the test should check the call; the SQL Orders & Payments writes to its own database is a detail, so the test should run it against a real database and check the outcome. That is no longer expensive: libraries such as Testcontainers start a disposable database in a container for each test run, and at Encore the service template wires one in by default.

I created MockK, a widely used mocking library for Kotlin, and have maintained it for a decade, so I hold this view from the toolmaker's side. Much of what a mocking library for Kotlin must offer lets a test reach further into the code under test than the mock objects of 2000 ever did: classes are final by default in Kotlin, and MockK can mock them anyway, along with singleton objects, top-level functions, constructors and private functions. Each of those capabilities exists for a good reason, usually code we cannot yet change. Used routinely, they let a team test around a design instead of listening to it (Section 3.2 returns to that idea), and the result is a suite that pins the code's present structure in place and fails on every attempt to improve it. A mock is a precise statement about a conversation between two objects. It is valuable when that conversation is the thing we mean to specify, and expensive everywhere else.

The last question about doubles is who owns them. Google's answer is that "the team that owns the real implementation should write and maintain a fake", because that team knows how the real thing behaves and will notice when it changes. At forty teams the alternative is a dozen hand-rolled fakes of Seat Inventory, each a consumer's guess, each drifting at its own pace. Encore's rule is that a service's fake ships with the service, from the same repository, and that consumers use it or explain why not. Section 3.3 extends the rule to the outside world.

#### Sorting code by what it deserves {#c3-four-quadrants}

Not every line of code deserves the same testing, and Khorikov offers a sorting tool for deciding which deserves what. Plot code along two axes, its complexity or domain significance and the number of collaborators it talks to, and four quadrants appear (Figure 3.3). Domain logic and algorithms, complex and with few collaborators, deserve thorough unit tests, because that is where the bugs that matter live and where tests are cheapest. Controllers, simple but talking to many collaborators, deserve a few integration tests that check the wiring. Trivial code deserves no tests. And overcomplicated code, complex and entangled with many collaborators, deserves a refactoring before it deserves a test, because any test written against it now will be large, slow and brittle. The refactoring that moves code out of the fourth quadrant is Meszaros's **Humble Object** pattern: pull the decisions out into a plain object that is easy to test, and leave behind a thin shell that does the input and output and is too simple to get wrong.

The quadrants are one author's heuristic, built on long practice, with no measured study behind them, and they need one condition attached. "Trivial code deserves no tests" is a statement about getters and data classes. It does not license untested glue on a path where money or seats move. The resale purchase saga is mostly wiring, and every link of that wiring is covered by an integration test, because a mistake there costs a fan a ticket. For barcode issuance, which sits squarely in the fourth quadrant, the sorting tool says what Section 2.4 says by another route: characterize first, then pull the logic out of the shell and test it where it lands.

{% include diagrams/fig-3-3.svg %}

*Figure 3.3 — Sorting code by what it deserves, after Khorikov. Tests are cheapest and most valuable top left; code top right earns a refactoring first, and the Humble Object moves its decisions to where a unit test can reach them.*

**Recap.** A test is a model of the world, and Ariane 5 showed what happens when the model is faithful to a world that is gone. Khorikov's four pillars give us a way to judge a test, and resistance to refactoring is the one we cannot trade, because false alarms teach people to ignore the suite. Test observable behavior, treat coverage as a warning light and mutation as a question asked in review, choose tests by size as well as scope, and let the owners of a dependency own its fake.

**Exercise 3.1.** Take ten tests from your own suite, chosen at random, and score each from zero to three on the four pillars. Delete or rewrite the two with the lowest product. For each, write one sentence about the world the test assumed, and whether that world still exists.

### 3.2 Growing Software with Tests

#### The walking skeleton {#c3-walking-skeleton}

The Resale team formed in month 4 of the bet, and the first thing it built was not a feature. It was a **walking skeleton**: the thinnest possible implementation of the whole system that runs end to end, built, deployed and tested automatically, before any feature is fleshed out. Alistair Cockburn coined the term in *Crystal Clear* (2004). Steve Freeman and Nat Pryce made it test-driven in *Growing Object-Oriented Software, Guided by Tests* (2009), insisting that the skeleton's first job is to prove that the deployment pipeline and the automated tests can reach every part of the system, so that every later feature is born into a working harness.

For Verified Resale the skeleton is the same slice the Products book{% include xref.html to="products" %} drew in its Section 3.4, now made of code: one organizer, one partner, a face-value cap and nothing else, entry at one venue. A test fan who bought a ticket through the Gate lists it through a stub of Rowmate's integration; a second test fan buys it; Inventory reissues the ticket under a new identity; the seller's barcode lands on the revocation list held by one venue's scanners; and the buyer's new ticket reaches the app. Each step was as crude as it could be while still being real. The rules engine knew one rule, the fee split was hard-coded, and the reissue call entered the barcode core through a narrow new entry point the Inventory team wrote behind characterization tests. But every step ran in Encore's real pipeline, on the golden path, under one automated test.

The skeleton cost several weeks in which no organizer saw anything new, and it forced the cross-team questions to arrive early, while they were cheap: who owns revocation (the Inventory team, as Section 9.5 confirms), how a revocation reaches an offline scanner, which payment product carries the split. Civil engineers do something similar when they throw a pilot line across a gorge before building the bridge, a thin cable that proves the two sides can be joined and then carries the heavier cables across. The analogy breaks in a way that favors software. The pilot line is discarded once the bridge stands, while the walking skeleton becomes the bridge, every later feature added to bones that have carried traffic since the first week.

#### Two loops {#c3-two-loops}

Freeman and Pryce describe the rhythm of work after the skeleton as two nested loops. The outer loop begins with an **acceptance test**: a test of a whole feature, written from the outside in the language of the domain, which fails because the feature does not exist yet. The inner loop is Kent Beck's cycle from *Test-Driven Development: By Example* (2002): write a small failing unit test, make it pass with the simplest code that works, then refactor while the tests stay green. The engineer goes round the inner loop many times, each turn adding one small, tested piece, until the acceptance test passes and the outer loop turns once (Figure 3.4).

{% include diagrams/fig-3-4.svg %}

*Figure 3.4 — Two loops, after Freeman and Pryce. The acceptance test is the executable goal; Beck's cycle turns many times inside it, and the outer loop turns once per feature.*

Here is the acceptance test that drove the skeleton, essentially as the Resale team wrote it:

```kotlin
@Test
fun `a resold ticket moves to the buyer and the old barcode dies`() {
    val seller = resale.fanWithTicket(faceValueCents = 6000, boughtVia = GATE)
    val listing = resale.partner("rowmate").lists(seller.ticket, priceCents = 6000)
    val buyer = resale.screenedFan()

    buyer.buys(listing, via = "rowmate")

    assertTrue(buyer.app.showsTicketFor(seller.ticket.seat))
    assertTrue(resale.venueScanner().rejects(seller.ticket.barcode))
    assertEquals(6600, resale.charged(buyer))
    assertEquals(mapOf("partner" to 240, "organizer" to 180, "encore" to 180), resale.ledger.split(listing))
    assertEquals(6000, resale.payoutDue(seller))
}
```

The test names no service, endpoint or table, and money is in integer cents. The `resale` object is an application driver, a layer that translates domain actions into calls on the real system, and Section 3.4 returns to why that layer matters. It would survive a complete rewrite of everything beneath it.

The double loop is a way of working in small steps against an executable goal, and that is the claim it can carry; whether it beats other ways of working in small steps is a question the end of this section takes up. Chapter 5 takes the outer loop one step further, because the acceptance test written before the code is also the most precise specification we can hand a coding agent.

#### Listening to the tests {#c3-listening}

The most useful idea in Freeman and Pryce's book may be the one in its title for Chapter 20: listen to the tests. When a test is hard to write, the difficulty is usually information about the design. A test that needs 40 lines of setup is reporting that the code under test depends on too much. A test that needs five mocks is reporting that the object has too many collaborators, or that it is doing work that belongs elsewhere. A test that cannot be named without the word "and" is reporting that the code does two things. Treating these as testing problems, to be solved with better fixtures or a stronger mocking tool, silences the design's request for help.

David Farley's *Modern Software Engineering* (2021) builds a whole approach to design on this observation, treating testability as a proxy for the qualities we actually want, modularity, cohesion, separation of concerns and loose coupling, because code that has them is easy to test and code that lacks them is not. DORA's research on test automation adds a finding about who hears the message: when tests are written by a separate group, developers "write code that is hard to test", because the feedback never reaches the people who could act on it. This is practitioner consensus, with no controlled study that isolates the effect, and it is a consensus I share. The first time the Resale team tried to test the fee split, the test needed a running rules engine, an event, an organizer and a PSP fake. The team listened, and the split became a pure function of a price, a channel and a jurisdiction, tested with a table of cases in milliseconds.

#### Wrap what you do not own {#c3-wrap}

Freeman and Pryce add a rule that sounds fussy until it saves a team a month: only mock types that you own. When our code depends directly on a third-party library or a vendor's API, a mock of that interface encodes our guess about how the vendor behaves, and the guess goes untested. The remedy is an **adapter**, a thin layer that speaks the vendor's language on one side and our domain's language on the other. The adapter is tested against the real vendor, or its sandbox, by integration tests; everything else in our code depends on the adapter's interface, which we own, and is tested against a fake of it.

Encore already has the structure this rule needs. Orders & Payments talks to its two payment service providers (PSPs) through an anti-corruption layer, the Architecture book{% include xref.html to="architecture" %}'s term for exactly this kind of translating boundary, owned by the PSP Integrations team. The testing consequence is a division of labor. PSP Integrations runs integration tests of the layer against each provider's sandbox, including, now, the primary provider's marketplace split-payment product, through which resale money moves so that Encore never holds it. Every other team tests against the layer's fake, which PSP Integrations ships and maintains, and Section 3.3 turns that fake into something more ambitious.

#### What the evidence says about TDD {#c3-tdd-evidence}

Test-driven development (TDD), in which the test is written before the code, has been argued about for two decades with more heat than data. The most careful study I know is by Davide Fucci, Hakan Erdogmus, Burak Turhan, Markku Oivo and Natalia Juristo, published in 2017. They dissected the process into four characteristics: sequencing, whether the test or the code came first; granularity, how small each cycle was; uniformity, how steady the rhythm of cycles was; and refactoring effort. Across 82 data points from 39 professionals, granularity and uniformity were associated with better external quality and productivity. Sequencing, the defining feature of test-first, had no important influence. Refactoring effort, surprisingly, was associated with worse outcomes on both. Their tasks were short and their participants came from one company's workshops, so these are associations, not causal effects on long-lived systems, and the authors say so. Earlier work points in a compatible direction. Nachiappan Nagappan and colleagues studied one IBM team and three Microsoft teams in 2008 and found pre-release defect density 40 to 90% lower than in comparable projects without TDD, with the teams estimating that initial development took 15 to 35% longer; those were case studies, without randomization. A 2013 meta-analysis by Yahya Rafique and Vojislav Mišić found a small improvement in external quality, mostly against waterfall comparisons, and no clear effect on productivity. The honest summary is that controlled studies do not show that writing the test first matters, and they do support working in small, steady steps with fast feedback. Encore asks for small steps, a test with every change and an acceptance test for every feature, and leaves the order of the inner loop to the engineer.

**Recap.** Build the walking skeleton first, so that every feature is born into a pipeline and a harness that reach the whole system. Work in two loops, an acceptance test outside and small test-backed steps within, and treat a hard-to-write test as a report about the design. Wrap what you do not own and test the wrapper against the real thing. The evidence favors small, steady steps; the order of test and code within a step matters less than its advocates claim.

**Exercise 3.2.** Before you write any code for your next feature, write its acceptance test in the language of the domain, using no names of services, endpoints or tables. Note which design decision the test forced you to make, and which question it forced you to ask another team.

### 3.3 Contracts and Simulators

#### Consumer-driven contracts across forty teams {#c3-cdc-forty-teams}

The Architecture book (Sections 5.2 and 7.2) made the argument for consumer-driven contracts and extended them to the public API's edge. Ian Robinson set out the pattern in 2006: each consumer of a service publishes the expectations it actually relies on, and the provider runs all of them as tests, so that it learns before shipping which of its consumers a change would break. Pact, the tool most teams now use, came seven years later, written in 2013 at realestate.com.au while that company was building Ruby microservices. What this section adds is the operational side: what it takes to run the pattern across forty teams without its becoming the shared bottleneck it was meant to remove.

Four pieces of machinery do most of the work. A **broker** stores every consumer's contract, versioned, with the results of every provider's verification, so that a pipeline can ask whether two versions have been checked against each other. **Provider states** let a contract say what must be true before an interaction ("given a ticket that has been listed for resale"), and the provider's test harness sets that state up, so that consumers do not need to know how. A deployment check, Pact's `can-i-deploy` command, asks the broker whether the version about to ship has been verified against every consumer version currently deployed in the target environment, and the pipeline refuses to deploy if not. And a rule about ownership settles the argument a failed verification would otherwise start: at Encore the provider fixes a broken verification, or negotiates with the consumer before merging, and never merges first. Within a month the Inventory team's reissue endpoint had three consumers, Resale, Orders & Payments and Venue Entry, all checked on every pull request.

Contracts check shape. They cannot check meaning, as the Architecture book's example of euros and cents showed, and they need one extension for a company built on events. Most of what Verified Resale publishes is asynchronous: `TicketReissued`, `TicketRevoked`, the listing and sale events that feed the finance ledger. Request-response contracts say nothing about those. Encore covers them in two ways. Pact's message contracts let consumers of an event state the fields they rely on, verified like any other contract, and the Event Backbone team's schema registry enforces compatibility at publish time, so a producer cannot register a new version of `TicketReissued` that would break consumers reading the old one. The registry catches the structural break on every publish; the message contract catches the consumer who relied on a field the schema allowed to be optional.

#### When the consumer cannot run your tests {#c3-partner-sandbox}

Consumer-driven contracts assume something easy to miss: that the consumers are known, that they can write tests, and that the provider can run those tests in its own pipeline. Inside Encore all three hold. At the edge they fail. Rowmate is an independent company with its own release schedule and no obligation to publish its expectations, and Tessera will be another. The partners Encore most needs to protect, the small ones who integrate once and touch the code again only when it breaks, are precisely the ones least likely to maintain a contract.

When the consumer cannot hand the provider its tests, the provider must hand the consumer something to test against instead, and the best-known public example shows how. Stripe's test mode gives every integrator a sandbox that behaves like the real API, and its documented test card numbers produce specific outcomes on demand: a decline, a card flagged for fraud, a payment that requires 3-D Secure authentication. An integrator can exercise every failure path without waiting for it to happen in production. The sandbox is, in effect, the provider's contract made executable, published for anyone to run.

Encore publishes two things for its partners. The **partner sandbox** is a hosted copy of the partner API, populated with synthetic events, in which each partner gets an isolated account with its own test fans, tickets and organizer rules; partners receive sandbox credentials as soon as they sign. The **partner simulator** is a container image of the same API that a partner can run inside its own continuous integration (CI) pipeline, versioned with the API. Both can produce the awkward cases on demand: an organizer tightening a rule while a listing is live, a reissue that takes 40 seconds, a webhook that arrives twice or late, a listing rejected because it breaks the cap. The testing discipline that makes them trustworthy lies on Encore's side. The Partner APIs team runs the same suite of behavior tests against the production API, the hosted sandbox and the simulator image on every release, so that a partner who passes against the simulator has passed against behavior Encore has pinned. How partners are certified on the sandbox before they get production credentials belongs to Section 8.3.

One property of the sandbox was designed in from the start, and it came out of a painful memory. Section 2.5 told the story: Rowmate's integration with the old Partner Listings product had read the event-code prefix embedded in the legacy barcode, a detail Encore never promised and Rowmate could nonetheless observe, and the integration broke against the new opaque ticket identity the first time Rowmate ran it in the sandbox. That is Hyrum's law, which the Architecture book's Section 7.2{% include xref.html to="architecture:7.2" %} states for public interfaces. Verified Resale gives partners an opaque `ticket_id` through the API and never exposes a barcode, which rotates in any case, and the sandbox goes further: it issues `ticket_id` values in a deliberately different format from production, so that any partner whose code tries to parse them fails in the sandbox, on the partner's own schedule, instead of on Encore's next release.

#### Simulators as products {#c3-simulators}

The same reasoning applies to the vendors Encore depends on. Each outside service on the purchase and resale paths has a simulator, a fake in Google's sense, owned by the team that owns the integration and shipped with it. Each does what the vendor does on a good day and, on request, what it does on a bad one (Figure 3.5).

| Simulator | Owning team | Failure modes on demand |
|---|---|---|
| Primary PSP | PSP Integrations | Decline; slow to 8 s; timeout after authorization; duplicate webhook; SCA challenge abandoned; marketplace fee-split mode, including a split rejected by the provider |
| Secondary PSP | PSP Integrations | Decline; slow to 8 s; timeout after authorization; duplicate webhook. No split mode: resale never routes here |
| Email and push delivery | Fan Messaging | Accepted but never delivered; delayed by hours; rate-limited; bounced |
| Wallet pass updates | Fan Messaging | Update accepted but not applied to the device; stale pass shown |
| Bot-screening edge signals | Bot Screening | Signal unavailable; signal delayed; every session scored as high risk |
| Partner API (for partners) | Partner APIs | Rule tightened mid-listing; slow reissue; duplicate or late webhook; listing rejected by cap |

*Figure 3.5 — Encore's simulators. Each belongs to the team that owns the integration, and each can produce the vendor's bad days on demand.*

The "slow to 8 s" mode replays the first big outage in Encore's history, when the PSP slowed from 200 ms to 8 s and a retry storm, amplified by autoscaling, took the site down (the Architecture book, Chapter 4). Every team on the purchase path now has a test that sets the primary PSP simulator to that mode and checks that the breaker opens, new attempts move to the secondary provider and nothing retries in two layers. The Resilience book's game day (Section 5.5) injected a similar delay into production-like conditions; the simulator is its pre-production twin, run on every build. Resale payments run only through the primary provider's marketplace product, a documented limitation, so the secondary simulator deliberately has no split mode, and a test asserts that a resale purchase with the primary breaker open fails cleanly with an honest message to the fan, never silently routing to a provider that cannot split the money.

A simulator is a product in Chapter 6's sense, with other teams as its users: the ones that get used have documentation, a changelog and an owner who answers questions. Chapter 4 shows the same simulators in the inner loop, where an engineer runs the purchase path on a laptop without touching any vendor.

#### Keeping a fake honest {#c3-honest-fakes}

A fake is a model of a vendor, and Section 3.1 has already shown what happens to models nobody checks against the world. Google's chapter on test doubles states the requirement plainly: "A fake must have its own tests to ensure that it conforms to the API of its corresponding real implementation", and it suggests running the same contract tests against both the real implementation and the fake. Encore does exactly this. Each simulator's owning team keeps one suite of behavior tests and runs it on a schedule against the simulator and against the vendor's own sandbox; when the two disagree, the simulator is wrong until proven otherwise, and the owning team fixes it before the drift reaches anyone's build.

That check has a limit, and it is Ariane's lesson in miniature. A vendor's sandbox is itself a simulator, written by the vendor, and it can differ from the vendor's production in ways the vendor never documents. Running our suite against the sandbox tells us that our fake agrees with their fake, and nothing about whether either agrees with the world. The remaining distance can be closed only in production, and Encore closes it there with the two instruments other books describe: the synthetic buyers that run the real purchase path every hour against a hidden test event, paying through the providers' sandbox (the Architecture book, Section 5.3), and the canaries that expose a few percent of real traffic to each new version (the Resilience book, Sections 4.3 and 4.4). For Verified Resale the synthetic buyers gained a hidden test listing, so that every hour a scripted fan resells a ticket to another scripted fan, and a scripted scanner confirms that the old barcode is refused. The Ariane board's second recommendation, as much real equipment as technically feasible, is what this arrangement reaches for, accepting that some of the real equipment can only be met in flight.

#### Properties over examples {#c3-properties}

Most tests are examples: given this input, expect that output. They test only what their author thought of. A **property-based test** states instead a rule that must hold for every input, lets a generator produce hundreds of random inputs, and, when one fails, shrinks it to the smallest input that still fails, so that the report reads like a minimal bug report. Koen Claessen and John Hughes introduced the idea with QuickCheck for Haskell in 2000, and it has since spread to nearly every language. Its most powerful form is **stateful** or **model-based**: the generator produces random sequences of operations, and the test checks after every step that the system agrees with a simple model of what it should be doing.

The best public industrial account is from Amazon. In 2021 James Bornholt and colleagues described how the team building ShardStore, a storage node for Amazon S3, wrote an executable reference model and used property-based testing to check that random sequences of operations, including crashes and concurrent requests, gave the same results on the model and on the real implementation. The paper reports that the approach had prevented 16 issues from reaching production, including crash-consistency and concurrency bugs, and that engineers who were not formal-methods specialists extended the checks themselves. It is the right precedent for barcode issuance, because issuance has exactly the shape the technique handles best: a small model ("each seat has one live ticket") and an implementation full of retries and ordering.

Verified Resale adds two facts that example tests handle badly. A ticket may be resold, and so reissued, more than once. And a retried reissue request carrying the same idempotency key must be a no-op, whatever happened to the first attempt. The Inventory team's property test runs the real issuance code, with its storage in memory, against random sequences of reissues and retries. A small harness holds the service and the set of keys used so far, which is the whole of the model:

```kotlin
class ReissueProperties {
    class Harness {
        val issuance = IssuanceService(InMemoryStore())   // real code, small test
        val keys = mutableSetOf<String>()
        init { issuance.issue(seat = "B-14") }
    }

    @Property
    fun reissuesKeepOneLiveTicket(@ForAll("reissues") chain: ActionChain<Harness>) {
        chain.withInvariant { h ->
            assertEquals(1, h.issuance.liveTickets(seat = "B-14").size)
            assertEquals(h.keys.size, h.issuance.reissueCount(seat = "B-14"))
        }.run()
    }

    @Provide
    fun reissues(): Arbitrary<ActionChain<Harness>> =
        ActionChain.startWith { Harness() }.withAction(Reissue)

    object Reissue : Action.Independent<Harness> {
        override fun transformer(): Arbitrary<Transformer<Harness>> =
            Arbitraries.of("k1", "k2", "k3", "k4").map { key ->   // repeats model retries
                Transformer.mutate("reissue($key)") { h: Harness ->
                    h.issuance.reissue(seat = "B-14", idempotencyKey = key)
                    h.keys.add(key)
                }
            }
    }
}
```

The barcode core is Kotlin, so the team used jqwik, a property-testing engine for the JVM that runs on JUnit 5 and supports stateful testing through action chains. It generates sequences such as "reissue with k1, reissue with k1 again, reissue with k3", checks both properties after every step, and on a failure shrinks the sequence to the shortest one that still breaks them. The test found a real fault in its first week: under a particular interleaving the old code wrote the new ticket before revoking the old one, so for one step two tickets were live. The five fairness invariants of Section 1.3 are written the same way, as properties in CI (Section 11.3 shows them in the capstone), and the money has one of its own: for every generated price, channel and jurisdiction, the buyer's payment equals the seller's payout plus the three shares, to the cent. How such spec-level tests are guarded against being edited away by an author, human or machine, is the Resilience book's subject (Section 4.5); this section is only about how to write them.

A close relative of property testing deserves a paragraph, because Verified Resale hands it two ideal targets. **Fuzzing** feeds a program large volumes of generated or mutated input, guided by which inputs reach new code, and watches for crashes, hangs and broken invariants. It is the established defense for parsers and anything that reads untrusted input. Google's OSS-Fuzz service reports that as of May 2025 it had "helped identify and fix over 13,000 vulnerabilities and 50,000 bugs across 1,000 projects". Partner payloads and the barcodes venue scanners read are both untrusted input to parsers, and both now run under a fuzzer nightly.

**Recap.** Consumer-driven contracts work across forty teams when a broker, provider states, a deployment check and a clear rule about who fixes a broken verification stand behind them, with message contracts and schema compatibility for events. When consumers cannot run our tests, we publish a sandbox and a simulator pinned by our own suite. Fakes of vendors belong to the teams that own the integrations, and they stay honest only if the same tests run against them and the vendor's sandbox, with production checks closing the last gap. Properties, model-based and shrunk, test the rules examples cannot reach.

**Exercise 3.3.** Pick one external dependency of your system. List the five failure modes your tests can produce on demand today, then the five you most fear in production. Every fear without a matching mode is a gap; choose the one you would add to a simulator first.

### 3.4 End-to-End Without Despair

#### A few journeys, each with an owner {#c3-owned-journeys}

End-to-end tests are the most persuasive tests we can write and among the most expensive to keep, and the Architecture book (Section 5.3) gave the reason: they are slow, they fail for reasons unrelated to the change under test, and when they fail they rarely say whose code is at fault. Its advice was to keep only a handful, written as journeys a business would recognize. The clearest public account of keeping that handful healthy comes from Lyft.

In a series of posts on scaling productivity across its microservices, Lyft's engineers Ben Radler, Garrett Heel and Shu Zheng described a fleet of about 900 services whose integration suites had grown until they took upwards of an hour to run and gave a very poor ratio of signal to noise. Lyft kept a small set of end-to-end scenarios for its critical flows, logging in, requesting a ride and paying for it, and made them acceptance tests that run in staging after each deploy and gate the promotion to production. InfoQ's report on the change describes thousands of the old integration tests being removed or rewritten as unit tests, with no measurable rise in production bugs. The flows were well chosen: Lyft classes a failure in any of them as a SEV0, its most severe kind of incident, so nobody needed convincing that each deserved a test.

Encore keeps eleven end-to-end journeys, and each has a named owning team, the one whose pager would ring if the journey broke in production: a fan buys a ticket in an on-sale, a fan completes a pending payment, an organizer publishes an event, a venue scans a ticket offline, and so on. The owner fixes the journey when it fails, keeps its runtime within budget and decides when it should be retired, which happens when a lower-level test has come to cover everything the journey catches. DORA's finding that performance improves when "developers are primarily responsible for creating and maintaining suites of automated tests" is the general form of the rule; an end-to-end journey without an owner becomes everyone's flaky test and nobody's job. Verified Resale added one journey, the resale of Section 3.2's acceptance test running against the real system with the Rowmate stub replaced by the partner simulator, owned by the Resale team. Everything else the feature needs to prove lives lower down, where a failure points at one team.

#### Test data as a product {#c3-test-data}

Much of the cost of an integration or end-to-end test is the data it needs. A resale test needs an organizer with rules, an event with an on-sale schedule, a fan who bought through the Gate within the per-fan limit and a partner with credentials, and building all of that by hand in each test is how test suites become unmaintainable. Freeman and Pryce's answer is the **test data builder**: an object that constructs a valid domain object with sensible defaults and lets each test override only the fields it cares about, so that a test reads `anEvent().withResaleDisabled()` and the reader sees at once which fact matters. Humble and Farley's *Continuous Delivery* (2010) adds the discipline at the environment level: every test creates the data it needs, or starts from a known baseline that resets, and no test depends on data another test left behind.

At Encore's scale test data becomes a product with an owner, like the simulators. The Resale team's builders live beside the service and are used by every team that tests against it. Synthetic organizers and venues are created through the same onboarding workflow that real ones go through (Section 7.1), so a change to onboarding cannot quietly break every test that needs a tenant.

#### What each environment can tell you {#c3-environments}

Humble and Farley devote a chapter to managing environments, and their underlying point is that an environment is an instrument with a known range, answering some questions and silent on others. A developer's machine with simulators can tell us whether our code behaves correctly against the documented behavior of its neighbors. A shared staging environment can tell us whether services integrate, whether configuration is right and whether a deployment works. Neither can tell us how the system behaves under production load, against a vendor's real production behavior or with the data real fans create. Those questions can be asked only in production, carefully, as the previous section described.

The interesting choice is between shared staging and an environment per change. Lyft's move from Onebox, a full copy of its stack per developer, to request-level isolation inside shared staging is the clearest public evidence, and Section 4.1 tells it along with how Encore builds and pays for its own environments. The short version is that full per-change environments buy isolation at a price that grows with the number of services, and at some fleet size isolating requests becomes cheaper than duplicating everything. For a testing strategy the discipline is to write down, beside each test, which question it asks of which environment, much as Encore now requires every load test to state the cache state it assumed.

#### Why tests flake {#c3-why-tests-flake}

A **flaky test** is one that can pass and fail on the same code. Flakiness kills end-to-end suites by the mechanism of Section 3.1: each false alarm teaches people that red means nothing, until a real failure is rerun and ignored like the others. John Micco reported Google's numbers in 2016. About 1.5% of all test runs reported a flaky result, almost 16% of tests had some level of flakiness, and about 84% of the transitions from pass to fail that Google observed involved a flaky test. Google's 2020 book adds a judgment about thresholds: "as you approach 1% flakiness, the tests begin to lose value". These are two measurements made in different years by different methods, and they should be read separately.

The causes are better understood than the remedies are practiced. Qingzhou Luo, Farah Hariri, Lamyaa Eloussi and Darko Marinov studied flaky tests in 51 Apache Software Foundation projects in 2014, inspecting commits that fixed them and classifying the root cause of 161. Figure 3.6 gives their three largest categories, with the design that prevents each.

| Cause (Luo et al., 2014) | Share of 161 classified fixes | What it looks like | The design that prevents it |
|---|---|---|---|
| Asynchronous wait | 45% | A test sleeps 2 s and hopes the event has arrived | Wait on the condition with a deadline; better, make the asynchronous step observable and wait for it |
| Concurrency | 20% | Two threads race, and the test passes only for one interleaving | Control the scheduler in small tests; test concurrency deliberately, with properties |
| Test-order dependency | 12% | A test passes alone and fails after another one leaves state behind | Each test creates its own data and cleans up; no shared mutable fixtures |

*Figure 3.6 — The three largest causes of flaky tests in Luo et al.'s study, and the test design that prevents each.*

A further finding from the same study shapes how Encore fights flakiness. Some 78% of the flaky tests were flaky from the moment they were written, so flakiness is mostly a design defect present at birth, which argues for catching it at review time more than for repairing it years later. Two disciplines prevent most of what remains. Control time and randomness: inject the clock and the random seed into the code under test, so that a test about a resale window that closes two hours before doors can set the clock instead of waiting for it. And keep large tests as hermetic as possible, because, as Google's chapter on larger tests puts it, "if a large test is nonhermetic, it is almost impossible to guarantee determinism". Encore measures flakiness per test and per journey, by rerunning failures on unchanged code. When Verified Resale began, the end-to-end suite failed spuriously on about one run in 40, far past the point where Google's book says tests lose value. How CI detects flaky tests, quarantines them and decides when to rerun them is a property of the pipeline, and Section 4.4 owns it; this section owns the reasons tests flake and the designs that keep them from doing so.

#### Acceptance tests in domain language {#c3-domain-language}

The acceptance test in Section 3.2 spoke of fans, listings and scanners and never of pages, buttons or endpoints, and that was deliberate. Humble and Farley describe the structure in their chapter on automated acceptance testing: the test is written against an **application driver**, a layer that knows how to perform domain actions on the real system, and only the driver knows about the user interface or the API. When the interface changes, one driver changes, and the tests, which express what the business needs, stay as they are. Without such a layer, every visual change rewrites dozens of tests that were never about the visuals.

Encore's drivers are owned like any other shared code. The resale driver has two implementations, one that acts through the partner API and one that acts through the fan app's backend, and the same acceptance tests run against both, which is how Encore knows that a fan reselling through the app and a fan reselling through Rowmate experience the same rules. DORA puts the ownership plainly: "Primary authors and maintainers of acceptance tests are developers." At Encore the trio decides what the acceptance tests should say, and the engineers write and keep them.

**Recap.** Keep a few end-to-end journeys, each owned by the team whose pager it would wake, and retire them when lower-level tests cover what they catch. Treat test data and environments as instruments with known ranges, and write down which question each test is asking of which environment. Flaky tests are mostly born flaky, from asynchronous waits, races and shared state, and the designs that prevent them are cheaper than the reruns that hide them. Write acceptance tests in the domain's language against a driver, so that a redesign changes one layer.

**Exercise 3.4.** Measure the flake rate of your end-to-end suite for one month by rerunning every failure on unchanged code. Name the owner of the worst journey, classify its flakiness by Figure 3.6's causes, and estimate what fixing it would cost against what its reruns cost now.

### 3.5 Evals as Product Practice

Everything so far assumes that a correct output exists and can be stated in advance. The organizer rule assistant breaks that assumption. An organizer types a request in plain language, such as "no resale until a week after the on-sale, two per fan", and the assistant, a large language model (LLM) behind Encore's AI gateway, drafts a typed rule set and a plain-language summary, which the organizer confirms before anything applies (the Products book designs it in Section 6.5). Part of its correctness is guaranteed by construction. The assistant can express only rules the type system allows, so the third fairness invariant, "Organizer caps and rules can only tighten", holds whatever the model says, and an example test proves it. The rest is a matter of judgment. Did the draft capture what the organizer meant? Is the summary clear? Did it ask when the request was ambiguous? Those questions have answers but no single correct output, and the same request produces different drafts on different days. An **eval** is a test for this kind of system: a set of inputs with criteria for judging the outputs, run repeatedly, whose result is a rate of success by category. The practice is young, documented mostly by practitioners with a small body of research, and the subsections below say which is which.

#### Who decides what good means {#c3-who-decides}

The first question about an eval is not technical. Someone must decide what a good draft is, and the people best placed to decide are rarely the engineers who wrote the prompt. Shreya Shankar and Hamel Husain, whose *Evals for AI Engineers* (2026) collects the clearest practitioner guidance, give advice, in their published answers to common questions about evals, that surprises teams used to consensus: "For most teams, the most effective strategy is to appoint a single, internal domain expert as the final decision-maker on quality." They call this person a benevolent dictator. A committee averages away the judgments that matter, while one expert, consulted often, produces consistent labels quickly and can explain them. This is practitioner experience, with no controlled study behind it, and it fits what Encore knew from its support assistant.

For the rule assistant, the Resale trio asked the organizer-success lead to decide, and she accepted. She had spent years helping organizers configure events, and knew what "a week after the on-sale" means to a festival promoter whose on-sale runs in waves. She labels; the product manager decides what the assistant should attempt; the engineers build the machinery. How to check that her labels agree with a second labeler, and how to calibrate an automated judge against her, is taught in the Resilience book (Section 8.3), and Encore follows it.

#### Criteria drift {#c3-criteria-drift}

The second surprise is that the expert does not arrive with her criteria ready-made. Shankar and colleagues named the phenomenon in a 2024 paper, "Who Validates the Validators?", which studied nine industry practitioners building evaluators for LLM pipelines. They called it **criteria drift**: "users need criteria to grade outputs, but grading outputs helps users define criteria." People discover what they mean by "good" while they grade, and their criteria change as they see more outputs. The study is small and qualitative, and the phenomenon it names will be familiar to anyone who has coded interview transcripts, where categories always shift during the first pass.

The rule assistant's first labeling session showed it within an hour. The original criterion said a draft was good if its rules matched the request. Then the lead met "two per fan", graded three drafts that had each chosen differently between the listing limit and the buying limit, and realized that none of them was right, because the request was ambiguous and a good assistant should ask. The criterion changed: a good draft either matches an unambiguous request or asks one clarifying question about an ambiguous one. A criterion written in advance and frozen would have graded those drafts on a question the organizer never answered.

#### Criteria before prompts {#c3-criteria-before-prompts}

The analogy with Section 3.2 is close, and it needs care at one point. An acceptance test written before the code states a goal precisely and then holds still. For the rule assistant, the equivalent is to write down what good looks like before anyone writes the first prompt: a first set of real requests, drawn from the design-partner interviews and from support cases about resale settings, each with a provisional criterion. Then the prompts and the evals are iterated together, and after each reading of real outputs, the criteria are revised where the reading taught the lead something. Writing the criteria first keeps the team from tuning the prompt to whatever the model happens to produce; revising them keeps the team honest about criteria drift. Shankar and Husain's method begins from reading real traces before building automated evaluators, and Chip Huyen's *AI Engineering* (2025) gives evaluation a central place in building AI applications; the Resale team did both, in that order. Here is one case from the set, after its third revision:

```yaml
# rule-assistant/cases/two-per-fan-ambiguous.yaml
request: "No resale until a week after the on-sale, two per fan."
event: {on_sale: "2027-03-05T10:00+01:00", doors: "2027-06-12T18:30+02:00"}
expect:
  window_opens: "on_sale + 7d"
  window_closes: "doors - 2h"          # the default, unchanged
  clarifying_question: about listing limit vs buying limit
  must_not: [apply_any_rule_before_confirmation]
summary_must_say: ["one week after the on-sale"]
criterion_version: 3                     # v1 required a limit; v2 allowed either
labelled_by: organizer-success lead
```

The first set held 60 cases across the categories in Figure 3.7. By launch it had grown to about 250, most of the growth coming from failures found while reading outputs, each turned into a case.

| Category | Cases in the first set | What a good draft does |
|---|---|---|
| Resale windows, relative to on-sale or doors | 16 | Expresses the window exactly; keeps the default where the request is silent |
| Per-fan limits | 12 | Distinguishes listing from buying limits, and asks when the request does not |
| Disabling resale | 8 | Disables it; in Ireland, explains that the law does not allow it and offers the permitted options |
| Requests the rules cannot express | 14 | Says plainly what cannot be done, such as raising the cap or changing the fee split, and proposes nothing that loosens a rule |
| Several rules in one request | 10 | Captures each, and lists them all in the summary |

*Figure 3.7 — The rule assistant's first labeled set, by category. The categories came from the organizer-success lead's first reading of outputs, and two of them did not exist before it.*

#### A screen for reading {#c3-review-interfaces}

An eval's quality is bounded by how many outputs the expert actually reads, and that depends heavily on how painful reading is. Shankar and Husain give a whole chapter to interfaces for human review, and their advice is that "the best way to empower the domain expert is to give them custom annotation tools that display system outcomes alongside traces." Their supporting examples come from research prototypes and consulting practice, so the claim that a custom screen beats a generic tool is practitioner judgment, without a measured comparison. It is also cheap to try. In two days the Resale team built a page showing, for each case, the request, the event's dates, the drafted rules as the console would render them, the summary, and pass, fail and "criterion unclear" buttons. The lead's reading rate in an afternoon went from a few dozen cases in a spreadsheet to well over a hundred, and the "criterion unclear" button produced most of the criteria revisions.

#### Evals in the build {#c3-evals-in-build}

Once the criteria have settled enough to automate, the eval joins the pipeline like any other test, and the series has already taught how: the Architecture book (Section 12.4) runs evals in CI as fitness functions, and the Resilience book (Sections 8.2 and 8.3) runs each case several times, gates per category and grows the golden set from production failures. What this chapter adds is the path into the build. Every failure the lead marks becomes a case in its category, with the criterion version that judged it. A change to the prompt, the model or the rule schema runs the whole set, through the same AI gateway the assistant uses in production, before it can merge. And the typed-rule examples that prove invariant 3 run beside the eval in the same stage, so the guarantee made by construction and the judgment made by the expert are checked together. Repeated runs are needed because the model is not deterministic, and a gate that judged each case once would be a flaky test by another name.

**Recap.** Evals are tests for systems with no single correct output, and the practice is young. One domain expert, given authority and a good screen, decides what good means; her criteria will drift as she reads, so criteria are written before prompts and revised after reading outputs. Failures become cases, and the cases run in the build beside the conventional tests that prove what the type system guarantees.

**Exercise 3.5.** For one AI feature in your product, write ten labeled examples and a provisional pass criterion before anyone changes its prompt. Then read twenty real outputs and record every place where the criterion did not tell you what to decide.

### Kata: One Run in Twelve

> **Your brief: "Repwell."** Repwell sells class-booking software as a service to 900 gyms and fitness studios, from single-room yoga studios to chains with 40 clubs. Sixty engineers in seven teams build it. Members book classes through a web widget and a mobile app, and studios manage timetables, waitlists, reminders, memberships and payments in a back office. The test suite has grown for nine years. It takes 70 minutes on the CI cluster, and about one run in twelve fails for reasons nobody can reproduce, so engineers rerun failures by habit and merge on the second green. Coverage is 84%, a target leadership set three years ago. Most unit tests mock every collaborator, including the company's own database. Last quarter a reminder-scheduling bug shipped to every studio, although 31 tests touched the code, because none of them checked a reminder across a daylight-saving change. This quarter Repwell must integrate a corporate-wellness vendor, which confirms before a booking is accepted whether a member's employer-funded pass covers the class. The vendor offers a sandbox, publishes no simulator, has an uptime commitment of 99.5% and answers slowly at the start of each month.

**Deliverables:**

1. **The suite's worth** — Score a random sample of 20 tests on the four pillars (Figure 3.2), and propose what to delete, rewrite or keep, with the evidence for each group. Say what to do about the coverage target.
2. **The integration's test strategy** — Design the adapter around the eligibility vendor, the tests at the adapter, and the simulator every other team will use, with its failure modes on demand and the suite that keeps it honest against the vendor's sandbox. Say what only production can tell you, and how you will learn it.
3. **Properties** — Write, in prose or code, two properties for the booking core: one about overbooking a class under concurrent requests, one about reminders across time zones and daylight-saving changes, with the clock injected.
4. **The flaky-test plan** — Describe how you will measure flakiness per test, classify the worst offenders by cause, and redesign them, with a target rate and a date. Say which part belongs to test design and which to the CI pipeline.
5. **End-to-end journeys** — Choose at most five journeys to keep, name an owning team for each, and explain what happens to the rest.
6. **A 70-minute budget** — Show how the suite's runtime falls, by test size and by what runs on each change versus nightly, and what you will measure to know the trade has not cost protection.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| World assumed | For each important test, have I stated the world it assumes, including the clock, the vendor and the data? |
| Trust | Would an engineer at Repwell believe a red build after these changes, without rerunning it? |
| Ownership | Does every simulator, journey and builder have a team that will fix it when it breaks? |
| Honest fakes | Is the eligibility simulator checked against the vendor's sandbox on a schedule, and do I know what neither can tell me? |
| Evidence over targets | Have I replaced coverage as a target with signals that measure whether tests catch bugs? |
| Proportion | Is every expensive test buying something a cheaper test could not? |

#### Where you now stand

You can now judge what a test is worth and spend testing effort where it pays: grow a system from a walking skeleton, replace the neighbors you cannot run with simulators you keep honest, state the rules that matter as properties, keep a few owned journeys at the top and design flakiness out. You can also build evals where no single correct output exists. What a suite cannot do on its own is decide how quickly its verdict reaches the engineer who needs it. A test that takes an hour to report invites the same habits as a flaky one: engineers stop waiting for it, and then stop reading it. Chapter 4 follows a change from a laptop to main, through the inner loop, the build, code review and the CI pipeline that runs all of these tests, and asks how to make that journey short enough that engineers still listen.

### References

- J. L. Lions et al. — [*ARIANE 5 Flight 501 Failure: Report by the Inquiry Board*](https://www-users.cse.umn.edu/~arnold/disasters/ariane5rep.html). ESA and CNES, Paris, 1996 — free online.
- Vladimir Khorikov — [*Unit Testing Principles, Practices, and Patterns*](https://www.manning.com/books/unit-testing). Manning, 2020.
- Titus Winters, Tom Manshreck, Hyrum Wright (eds.) — [*Software Engineering at Google*](https://abseil.io/resources/swe-book) (chapters 11–14). O'Reilly, 2020 — free online.
- Steve Freeman, Nat Pryce — [*Growing Object-Oriented Software, Guided by Tests*](http://www.growing-object-oriented-software.com/). Addison-Wesley, 2009.
- Davide Fucci, Hakan Erdogmus, Burak Turhan, Markku Oivo, Natalia Juristo — [*A Dissection of the Test-Driven Development Process: Does It Really Matter to Test-First or to Test-Last?*](https://arxiv.org/abs/1611.05994). IEEE Transactions on Software Engineering 43(7), 2017 — free online.
- Ian Robinson — [*Consumer-Driven Contracts: A Service Evolution Pattern*](https://martinfowler.com/articles/consumerDrivenContracts.html). martinfowler.com, 2006 — free online.
- Qingzhou Luo, Farah Hariri, Lamyaa Eloussi, Darko Marinov — [*An Empirical Analysis of Flaky Tests*](https://doi.org/10.1145/2635868.2635920). FSE, 2014.
- John Micco — [*Flaky Tests at Google and How We Mitigate Them*](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html). Google Testing Blog, 2016 — free online.
- Goran Petrović, Marko Ivanković — [*State of Mutation Testing at Google*](https://research.google/pubs/state-of-mutation-testing-at-google/). ICSE-SEIP, 2018 — free online.
- Koen Claessen, John Hughes — [*QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs*](https://doi.org/10.1145/351240.351266). ICFP, 2000.
- James Bornholt et al. — [*Using Lightweight Formal Methods to Validate a Key-Value Storage Node in Amazon S3*](https://www.cs.utexas.edu/~bornholt/papers/shardstore-sosp21.pdf). SOSP, 2021 — free online.
- Hamel Husain, Shreya Shankar — [*Frequently Asked Questions (And Answers) About AI Evals*](https://hamel.dev/blog/posts/evals-faq/). hamel.dev, 2026 — free online.
- Shreya Shankar, J.D. Zamfirescu-Pereira, Björn Hartmann, Aditya G. Parameswaran, Ian Arawjo — [*Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences*](https://arxiv.org/abs/2404.12272). UIST, 2024 — free online.
- Jez Humble, David Farley — [*Continuous Delivery*](https://continuousdelivery.com/). Addison-Wesley, 2010.
- Nachiappan Nagappan, E. Michael Maximilien, Thirumalesh Bhat, Laurie Williams — [*Realizing Quality Improvement Through Test Driven Development: Results and Experiences of Four Industrial Teams*](https://doi.org/10.1007/s10664-008-9062-z). Empirical Software Engineering 13(3), 2008.
- Chip Huyen — [*AI Engineering*](https://www.oreilly.com/library/view/ai-engineering/9781098166298/). O'Reilly, 2025.

---

## Chapter 4: The Development Loop — From Laptop to Main {#ch4}

> A branch is a promise to merge, and the promise grows heavier every day it is left unkept.

Every change to Encore begins in one engineer's head and ends in the main line of a repository, where it becomes everyone's problem. Between those two points lies a short journey repeated many thousands of times a week: the engineer edits code, runs it, tests it, asks a colleague to look at it, waits for a machine to build and check it, and merges it. Each step is small and familiar. Repeated by 400 people, they make up the **development loop**, the cycle by which a change travels from an engineer's laptop to the main line, and the speed and safety of that loop set a ceiling on everything else the engineering system can do. A company whose loop takes an hour can try an idea before lunch and abandon it after. A company whose loop takes a week has, without anyone deciding so, committed to fewer and larger changes, which are slower to review, harder to integrate and riskier to ship. The question of this chapter is how a large organization keeps that loop short as it grows, and why tools alone have never been enough to do it.

The modern history of the loop turns on a few days in April 2005, when Linus Torvalds, having lost the free license for the version-control system the Linux kernel had used for three years, began writing his own. He called it Git. Within days it was managing its own source, and within a few years it had made branching so cheap that the industry came to think of a branch as costing nothing. What Git did not make cheap, and could not, was the integration of one person's work with everyone else's. The industry spent the better part of a decade learning the difference, and the practices this chapter teaches are largely what it learned.

Encore is in the middle of that lesson. Its new Resale team, formed in month four of Verified Resale from engineers drawn from Orders & Payments and Partner APIs, starts its service from the golden-path template and within weeks meets every slow step in Encore's loop at once. Its engineers need Seat Inventory and Notifications to test anything, and nobody can run Encore on a laptop. Their changes to the reissue path need reviewers from Inventory and Orders & Payments, and those reviews stall for two days. Every change to barcode issuance waits 31 minutes for continuous integration on `encore-core`, Encore's oldest repository. And no fan may see the product until month 12, so months of unfinished work must live somewhere without rotting. The five sections that follow take these problems in turn.

### 4.1 The Inner Loop

#### Ten days in April 2005 {#c4-git-2005}

For its first decade the Linux kernel had no version-control system at all. From 1991 to 2002 changes travelled as patches and tarballs, mailed to Torvalds and applied by hand: one person acting as the integration point for thousands of contributors, with his own attention as the only merge tool. In 2002 Torvalds moved the kernel to **BitKeeper**, a proprietary distributed system made by Larry McVoy's company BitMover, which offered it free of charge to open-source developers. The choice was controversial; some kernel developers refused to use a proprietary tool, and Richard Stallman objected publicly. But BitKeeper changed how the kernel was built. Every developer's tree was a full repository, branching was cheap, and changes moved between trees by pulling. The maintainers learned habits from it that they would never give up.

The arrangement ended in the spring of 2005. Andrew Tridgell, who worked on unrelated projects at the Open Source Development Labs (OSDL), Torvalds's employer at the time, wrote a client that could read BitKeeper's repository metadata, and BitMover, treating this as reverse engineering, withdrew the free license. On 6 April 2005 Torvalds told the linux-kernel mailing list, in a message titled "Kernel SCM saga..", that he would stop using BitKeeper. He was generous to its owners: "don't blame BitMover," he wrote, and of the tool: "It didn't work out, but it sure as hell made a big difference to kernel development." The message did not announce Git; its postscript pointed readers, if they must, at Monotone.

He had already started. By the commonly cited chronology, work began on 3 April, and on 7 April Git committed its own source for the first time, with the message "Initial revision of "git", the information manager from hell." The first merge of several branches followed on 18 April, Git managed the 2.6.12 kernel release on 16 June, Torvalds handed maintenance to Junio Hamano on 26 July, and version 1.0 appeared on 21 December 2005. Figure 4.1 sets the dates out. The sequence is often compressed into the legend that Git was "written in two weeks." The defensible version is more interesting: it hosted itself within days and ran a kernel release within about 10 weeks, because its author designed it around a few demanding goals and nothing else. His rule was to take CVS, the older system much of the industry still used, "as an example of what *not* to do; if in doubt, make the exact opposite decision." The goals *Pro Git* records are speed, a simple design, strong support for non-linear development with thousands of parallel branches, full distribution, and efficiency on very large projects.

{% include diagrams/fig-4-1.svg %}

*Figure 4.1 — Git's first year, with April drawn enlarged. Notice how little separates the break with BitKeeper from Git hosting itself, and how much longer the road ran from there to a kernel release and a 1.0.*

Git did not invent cheap branching. BitKeeper had it, and so did Monotone and darcs, and Olivia Mackall (then publishing as Matt Mackall) announced Mercurial on 19 April 2005, for the same reason. What Git did was make cheap branching *fast* at the scale of the kernel. In Git, as *Pro Git* puts it, "Creating a new branch is as quick and simple as writing 41 bytes to a file (40 characters and a newline)." Commits, diffs and switches between branches happen on the engineer's own machine in a fraction of a second. When GitHub launched in 2008 and made the pull request the unit in which most of the industry proposes a change, the loop Git had made fast became the loop nearly everyone worked in. (Version control itself is much older; Marc Rochkind's SCCS came out of Bell Labs in the early 1970s, as Chapter 6 tells.)

Git belongs at the head of this section because it is, above all, a tool for the inner loop. Its speed was a design goal, chosen by a man who integrated other people's work all day and could not afford to wait on his tools, and it teaches the section's first lesson: the time a developer waits between making a change and learning whether it works is a quantity worth engineering.

#### Why the inner loop decides productivity {#c4-why-inner-loop}

The **inner loop** is the part of the development loop that one engineer runs alone, many times an hour: edit the code, build it, run it or its tests, look at the result, and edit again. The **outer loop** is everything that involves other people or shared machinery: review, continuous integration, merging, deployment. The distinction matters because the two loops have different economics. The outer loop runs a few times a day for each change, and its waits can be scheduled around. The inner loop runs dozens of times an hour, and every second it costs is paid again on each turn.

Chapter 1 introduced the three dimensions of developer experience that Abi Noda, Margaret-Anne Storey, Nicole Forsgren and Michaela Greiler proposed in 2023: feedback loops, cognitive load and flow state. Their framework synthesizes earlier qualitative research and makes no causal claim, and Chapter 6 uses it to measure Encore's platform. Here we need only the first dimension. A **feedback loop** is the time it takes a developer to learn whether an action had the effect intended, and the inner loop is the feedback loop that runs most often. Practitioners aim for an edit-build-test cycle measured in seconds. Nobody has measured the effect of that target directly, but the reasoning is sound and old. A loop of a few seconds keeps the problem in the engineer's head. A loop of a few minutes invites a glance at messages, and the glance becomes a context switch that costs more than the wait. A loop of half an hour changes how people work: they batch several changes into one build, so that when it fails they no longer know which change broke it.

A musician practicing a difficult passage shows the same economics. She plays four bars, hears the wrong note and plays them again, and the speed of that cycle is most of what practice is. If she had to wait 10 minutes after each attempt to hear a recording, she would practice far less, and she would play longer passages between recordings to make each wait worthwhile, which is exactly the habit that makes mistakes hard to find. The analogy breaks at one useful point. The musician's instrument is complete in her hands. A developer's program is not: at Encore it depends on services owned by other teams, running elsewhere, and the inner loop is only as fast as the slowest of those it must touch. Most of the work of a fast inner loop at scale is deciding what the developer does *not* need to run.

#### Local environments {#c4-local-environments}

The first condition of a fast inner loop is a working checkout, and it fails in familiar ways: a toolchain version that differs from CI's, a database installed by hand, environment variables known only to the team's longest-serving member, a setup document last accurate two years ago. Each failure is paid again by every new joiner and every engineer who moves between repositories. The remedy is long practice, though its published evidence is mostly company case reports: a **reproducible development environment**, defined in the repository itself, that brings a fresh machine to a working, tested checkout with one command. Dev containers, an open specification many editors support, are one common form; pinned toolchain files and a bootstrap script are another.

GitHub's 2021 account of moving its own engineers to Codespaces is the most detailed public case, and since GitHub sells Codespaces it should be read with that in mind. Its lesson is independent of the product. GitHub's main repository was almost 13 GB on disk, and bootstrapping an environment for it took "upwards of 45 minutes." A shallow clone cut cloning from about 20 minutes to 90 seconds, caching brought creation to about 5 minutes, and **prebuilding** environments ahead of demand brought it to about 10 seconds. The step that mattered was doing the slow work before anyone asked for it, and that needs an owner, who keeps the prebuilt environment current and measures the time from a fresh machine to a first successful build, a number that decays quietly as a repository grows.

Encore's golden-path template gives every new service such an environment; keeping templates current is a platform problem for Chapter 6, and the onboarding test of a first commit in the first week belongs to Chapter 9. The Resale team found the difference at once. Its own service, born from the template, was running in minutes. `encore-core` needed a page of instructions and an afternoon, for reasons that run through the rest of this chapter.

#### Running against a fleet {#c4-running-against-fleet}

The harder problem is the one the musician never faces. To list a ticket, the Resale service must ask Seat Inventory whether the seller bought it through the Gate; to sell one, it must screen the buyer with Bot Screening, run a purchase saga in Orders & Payments and ask Inventory to reissue; afterwards it must tell Notifications to replace two wallet passes. An engineer working on any of this has three broad ways to give the code its neighbours, and each trades cost against fidelity.

The first is to run **local stubs or fakes**, small stand-ins that answer like the real service for the cases the developer needs. Chapter 3 set Encore's rule that the team owning a service ships its fake with the service and keeps it honest with contract tests (Sections 3.1 and 3.3), so the Resale team runs the Seat Inventory fake that Inventory ships from `encore-core` instead of writing its own guess. The second is to call **shared remote dependencies**, real instances running in a shared environment such as staging, which is cheap and faithful as long as that environment is stable. The third is a **per-change environment** in the cloud, the next subsection's subject.

The most instructive public account of choosing among these comes from Lyft, which published a four-part series in 2021. Lyft grew from about 100 engineers to more than 1,000, and for years its developers used Onebox, a Docker-based environment that ran a full copy of the stack for each developer, later on large cloud instances. By Lyft's own account, Onebox "could not scale anymore." Lyft moved to local-first testing of a single service with its dependencies stubbed, and to isolating requests inside a shared staging environment where real neighbours were needed. It removed or converted thousands of integration tests (Section 3.4 tells that half of the story), and pull requests became, in Lyft's words, "ready to merge in minutes."

The Resale team settled on a mixture, and Figure 4.2 sets out the options as Encore weighs them.

| Option | Fidelity | Cost to the developer | Cost to the organization | Encore uses it for |
|---|---|---|---|---|
| Local stub | Low: answers only what it was told | Seconds to start | Almost none | Bot Screening's verdicts in Resale's tests |
| Owner-supplied fake, contract-tested | Medium to high, for the behaviors under contract | Seconds to start | The owning team must maintain it (Chapter 3) | Seat Inventory, including holds and the per-fan limit |
| Shared remote dependency | High, for one shared version | Network latency; shared test data | One stable shared environment | Notifications, owned by Fan Messaging |
| Request-routed preview | High: real services, real wiring | Minutes to deploy changed services | Compute per preview, and routing in the mesh | Cross-service journeys, such as resale purchase and reissue |
| Full stack per developer | Highest in principle | Tens of minutes, and a large machine | Grows with every service; Lyft's Onebox | Never |

*Figure 4.2 — Ways to give a developer's code its neighbours, ordered from cheapest to most expensive. Fidelity rises down the table, and so does cost; the last row is where the cost outruns what fidelity can repay.*

The file that defines the Resale team's inner loop is short, and it is worth reading because every line records a decision about what to run where.

```yaml
# resale/dev.yaml — what `encore dev up` starts for the Resale service
service: resale
laptop_budget: 10              # Encore's ten-container rule
local:
  - resale                     # the service itself, rebuilt on save
  - postgres                   # its own database, seeded from fixtures
  - event-broker               # single node, carries ticket-sales.v2
  - seat-inventory-fake        # shipped by Inventory, pinned to contract v14
  - bot-screening-stub         # "allow" unless a test scripts a verdict
remote:
  notifications: staging       # Fan Messaging's shared instance
  orders-payments: staging     # real saga, test PSP behind it
```

Five containers on the laptop, two services reached remotely, and none of the others. Notifications is remote because Fan Messaging keeps a stable shared instance and the Resale engineers mostly need to see that a message *would* be sent; a remote call costs less than a fake someone would have to keep faithful.

#### Ephemeral environments {#c4-ephemeral-environments}

Some questions cannot be answered from a laptop. Does a resale purchase, run through the real saga, make Inventory reissue the ticket, put the old identity on Venue Entry's revocation feed and replace the seller's pass? That journey crosses four teams' services, any of which may be changing at the same moment. For such questions teams use **ephemeral environments**: short-lived environments, created for a change and destroyed when it merges, in which the change runs against real services.

The obvious design gives each pull request a full slice of the system. It works for a handful of services and fails for hundreds, for the reason Onebox did: the slice grows with the fleet, and so do its cost and the work of keeping its data and versions consistent. The large published accounts converge on another design. Lyft's staging overrides (2021) and Uber's SLATE (2022) deploy *only the services that changed* into a shared, continuously updated baseline, and route requests carrying a marker to the changed versions while everything else goes to the baseline. Lyft carried the marker as baggage in the request and routed on it in its Envoy mesh, keeping the offloaded deployments out of ordinary service discovery so that no untagged request could reach them. The conditions are specific: every service must propagate the request's context, the mesh must be able to route on it, and the deployed versions must be torn down on merge.

Encore already pays for preview environments; the Resilience book's Section 2.5{% include xref.html to="resilience:2.5" %} counts them among the build-pipeline costs in the cost per ticket. What changed in year nine was their shape. Encore's services already propagate the W3C `traceparent` header (the Architecture book{% include xref.html to="architecture" %}, Section 5.3) and its mesh can route on headers, so the Runtime team moved previews to the request-routed form: a preview deploys only the changed services into the staging cell and receives the requests that carry its key. One key can now cover changes in several repositories, which is what the resale journey needs, since its changes land in the Resale service, in `encore-core` and in Venue Entry's revocation feed. Encore keeps a full slice only for the rare journey whose test data cannot be isolated inside the shared baseline. Figure 4.3 follows one resale request through such a preview.

{% include diagrams/fig-4-3.svg %}

*Figure 4.3 — A request-routed preview for the resale journey. Only the three changed services are deployed; a request carrying the preview key reaches them, and falls through to the shared baseline wherever, as with Notifications, nothing changed.*

#### The laptop budget {#c4-laptop-budget}

One line in the Resale team's file records a choice that is Encore's own. `laptop_budget: 10` refers to the **ten-container rule**: no service's inner loop may require more than ten containers on a developer's machine, and when a service would need more, the platform owes its developers a fake or a remote option for the excess. I know of no published precedent for a written limit of this kind, and I offer it as Encore's heuristic. Lyft's Onebox shows what happens without one. The containers a laptop must run grow by one whenever a service gains a dependency, nobody notices any single addition, and by the time the loop is unbearable, reversing it is a project. A written budget turns a drift nobody sees into a line somebody crosses. The number ten is a judgment about Encore's laptops and services; what matters is that the limit is written down, checked when `encore dev up` runs, and treated by the platform group as its own problem when breached.

**Recap.** Git made the inner loop fast because its author treated speed as a design goal, and the same goal applies to every step a developer repeats many times an hour. A reproducible environment, prebuilt and owned, gets a developer to a working checkout; a deliberate mixture of stubs, fakes, shared remotes and request-routed previews gives the code its neighbours without running the fleet. Encore's ten-container rule is its own way of keeping that mixture from drifting back toward the full stack that failed at Lyft.

**Exercise 4.1.** Time your own edit-to-feedback loop for a one-line change in a service you work on, from saving the file to seeing a test result you trust. Write down each step and its duration, name the slowest, and say which option in Figure 4.2 would remove it.

### 4.2 Repositories and Builds

#### Trunk-based development {#c4-trunk-based}

Git made a branch cost 41 bytes. It did not change what a branch *is*: a promise to integrate later. The longer a branch lives, the more the main line moves beneath it, and the final merge must reconcile two sets of assumptions as well as two texts. Torvalds made the point himself in a talk at Google in 2007: branches are worthless unless they are merged, and merging was the problem Git had to solve well. Martin Fowler's 2020 essay on branching patterns puts it in one line: "branching is easy, merging is harder." Git merges text very well. It cannot tell whether two changes, each correct alone, still work together; Fowler calls that gap a **semantic conflict**, a pair of changes that merge cleanly and "may build but fail at run-time."

The response is **trunk-based development**: every engineer integrates into a single shared main line, the trunk, at least once a day, and branches, where they exist at all, live for hours or a day or two. DORA's research, reported in *Accelerate* (2018) from survey data gathered in 2016 and 2017, found higher delivery performance in teams that, in the words of DORA's capability page, have "three or fewer active branches" that merge to trunk "at least once a day" and have no code freezes or integration phases. *Software Engineering at Google* is blunt: "Long-lived dev branches are not a good default plan." Google's own monorepo was shared in 2020 by roughly 50,000 engineers making 60,000 to 70,000 commits a working day. Fowler's rule of thumb is the most practical form: "you should never have more than a day's work sitting unintegrated in your local repository."

Much of the industry spent the decade after Git going the other way, and the most honest account of that detour comes from one of the people who led it. In January 2010 Vincent Driessen published "A successful Git branching model," describing **git-flow**: long-lived `develop` and `main` branches, feature branches that could live for weeks, and release and hotfix branches between them. It was clear and handsomely drawn, and it became, in Driessen's later words, "a dogma or panacea" for teams it did not suit. In March 2020 he added a note at the top of the post: "If your team is doing continuous delivery of software, I would suggest to adopt a much simpler workflow (like GitHub flow) instead of trying to shoehorn git-flow into your team." Few authors of a popular practice retract it so plainly, and the retraction carries weight because its author watched the practice spread for ten years. Git-flow still suits software released in versions, such as a library or a desktop application. For services deployed many times a day, its long-lived branches only postpone the integration that trunk-based development performs daily.

A newsroom shows why one trunk works better than many. Reporters do not produce private newspapers and merge them at the end of the week. They file to one copy desk, all day, for the one edition printed tonight, and stories not yet ready are kept off the page without being kept out of the system, so two reporters covering the same event are found out the same day. The analogy breaks because a newspaper starts fresh each morning and a codebase never does. Yesterday's code constrains every change made today, which is why software must also keep trunk releasable at all times, and why Section 4.5's flags exist.

Encore has worked this way since the golden path arrived. The practice has one pitfall that DORA names on its capability page, and it leads to Section 4.3: trunk-based development suffers when review is slow, because a change waiting two days for a reviewer is a two-day branch, whatever the team intends.

#### Monorepo or polyrepo {#c4-monorepo-polyrepo}

The second choice is how many repositories to have. A **monorepo** keeps the code of many projects, often of a whole company, in one repository; a **polyrepo** arrangement gives each project, usually each service, its own. Both work at large scale, and both have documented costs.

Google is the famous monorepo. Rachel Potvin and Josh Levenberg described it in 2016: as of January 2015, about two billion lines of code in about nine million source files, 86 TB of data and about 35 million commits, developed on trunk. What makes it work is investment: a custom version-control system, a build system that understands the whole dependency graph, code search across everything and ownership files on every directory. A 2018 survey at Google by Ciera Jaspan and colleagues, one of the few studies of engineers who had worked both ways, found that the benefit they valued most was **visibility**: searching all the code, finding examples, and updating every caller of an API in the same change. What they valued in multi-repository setups was freedom of toolchain, finer access control and stability. Google's authors are candid: "no, we don't think the monorepo approach as we've described it is the perfect answer for everyone." Microsoft's move of Windows to Git in 2017, about 3.5 million files and 300 GB for about 4,000 engineers, needed a virtual file system built for the purpose, which shows the condition plainly: a monorepo at scale needs infrastructure that ordinary tools do not provide.

Encore is polyrepo for its services. About one repository per service, each generated from the golden-path template, holds most of the backend, and a few repositories hold shared libraries. The fan app has its own repository, with its shell and 14 modules; the web frontend is a monorepo, for reasons the Architecture book's Section 8.2{% include xref.html to="architecture:8.2" %} gave and the Products book's Chapter 7{% include xref.html to="products:7" %} develops; and the desired state of every environment lives in `encore-deploy` (the Resilience book, Section 3.4). Then there is `encore-core`, the year-one monolith's repository and the shared repository of Chapter 1. It still holds Seat Inventory & Ticketing, with barcode issuance inside it, the Orders & Payments saga and some shared libraries, and its CI takes 31 minutes, against about 6 for a golden-path service.

Encore's reasons for staying polyrepo are the ones Jaspan's survey records: teams own their pipelines, one service's broken build cannot block another, and Encore has never had the platform staff to build Google's tooling. The cost is the other side of the survey. A change that spans services spans repositories, needs several merges in the right order and cannot be atomic. Nor does one commit give Encore a single version of every dependency. It approaches the One-Version Rule by the route Section 2.5 described: a shared version catalog in every service's build, upgrade changes opened by a bot, and the team that owns a catalog entry responsible for moving every caller. That works, but through many merges over days where a monorepo would need one, and Encore accepts the slower convergence in exchange for independent pipelines.

#### Build systems {#c4-build-systems}

Beneath the repository lies the build, where the inner and outer loops slow down together. *Software Engineering at Google* draws the distinction that matters in a chapter by Erik Kuefler. In a **task-based build**, the engineer writes tasks (compile this, copy that, run these tests) and the tool runs them in order. Such builds give "too much power to engineers and not enough power to the system": a task can do anything, so the tool cannot know what it depends on or whether its output can be reused. In an **artifact-based build**, the engineer declares the targets and their inputs in "a declarative manifest," and the system decides how to build them. Because every input is declared, the system knows what a change affects, and because each action runs isolated in a sandbox, the same inputs produce the same output on any machine. That property, **hermeticity**, is what makes a build cacheable and trustworthy. Google's internal system was released as open source in 2015 as Bazel.

The costs deserve plain statement. Moving a large existing codebase to an artifact-based build means declaring every target, finding every hidden dependency and fixing every non-hermetic test. Below some size, a well-kept task-based build with good caching is enough. Encore's golden-path services build in about 6 minutes with the template's task-based tool, and migrating them would buy little. The problem was `encore-core`, an eight-year-old Kotlin codebase whose Gradle build had grown by accretion: its tests reached the network, a code-generation step wrote into the source tree, and nobody could say with confidence what a given change might affect.

#### Remote caching and execution {#c4-remote-caching}

A **remote cache** stores the outputs of build actions, keyed by a hash of their inputs, so that any machine, laptop or CI runner, can download an output already built elsewhere instead of rebuilding it. **Remote execution** goes further and runs the actions on a shared farm. Both depend on hermeticity: a cache over a build with undeclared inputs will one day hand someone a wrong result, which is worse than a slow one because nobody suspects it.

The best first-party account of what this buys comes from Uber's Go monorepo, described in 2022: about 500,000 files, more than 10 million Bazel targets, and about 50 changes an hour in working hours. Moving the remote cache to Buildfarm in 2021 "cut down the build time by about half," and the 95th-percentile time, which had fluctuated between 40 and more than 100 minutes, fell consistently below 40. Uber also computes, for each change, which targets it alters, in about 5 minutes; this is the dependency-graph test selection Section 4.4 returns to.

Encore's version is smaller. It did not move `encore-core` to Bazel. Instead, the Developer Portal team and two engineers from Inventory spent most of months five to eight making the existing build hermetic enough to cache: pinning the toolchain, declaring the code generator's inputs, cutting the tests off from the network and splitting the modules so that the build graph reflected which code depended on which. Then they added a remote cache shared by CI and laptops, and dependency-graph test selection. Figure 4.4 shows where the 31 minutes went.

{% include diagrams/fig-4-4.svg %}

*Figure 4.4 — Continuous integration on `encore-core`, step by step, before and after months five to eight, from 31 minutes to 9. Test selection and the remote cache account for 17 of the 22 minutes saved; neither would have been safe before the build was made hermetic.*

The largest saving came from running fewer tests, which is safe only because the graph that decides which tests to skip can now be trusted. The 9 minutes remain above the golden path's 6 because `encore-core` is still large, and Encore expects to close the gap by moving code out of it over time, having judged that a different build system would cost more than it returned.

#### Ownership in the repository {#c4-ownership}

A repository also records who owns what. Chapter 1 showed `encore-core`'s CODEOWNERS file, in which barcode issuance belonged to Inventory and the shared library `libs/http-client` had had no owner since year five. GitHub introduced CODEOWNERS files in July 2017, inspired by Chromium's OWNERS files, and they can require an owner's approval before a change merges; Google's OWNERS files, older and stricter, guard every directory.

Ownership files help only if they match the organization, which is Conway's law seen from the repository (the Architecture book's Section 5.5{% include xref.html to="architecture:5.5" %} is its home). A file that names a dissolved team, a departed person or nobody sends review requests nowhere. Encore now runs a CI check that fails when a path lacks an owner or names one that does not exist in the service registry the Operations book's Section 7.2{% include xref.html to="operations:7.2" %} describes. Its first run on `encore-core` found 41 such paths. The HTTP client library went to the Web & API Paths team as an interim owner, and Chapter 8 asks whether a library every service uses should be run as InnerSource instead. The check takes seconds and removes the stalled review in which nobody knew whom to ask.

**Recap.** Git made branches cheap and left integration as hard as ever, which is why trunk-based development, with branches measured in hours, remains the proven way to integrate, and why git-flow's own author now recommends something simpler for continuously delivered software. Monorepo and polyrepo both work at scale, each with costs that only tooling pays; Encore stays polyrepo and approaches a single version through a shared catalog. Hermetic builds make caching and test selection safe, and they took `encore-core` from 31 minutes to 9, while ownership files that match the team map keep reviews from going nowhere.

**Exercise 4.2.** Take one feature your organization shipped recently. Count the repositories it touched, the merges it took to land, and the days between the first commit and the last merge. Then find the longest-lived branch involved and ask what it was waiting for.

### 4.3 Code Review at Scale

#### What review is for {#c4-what-review-is-for}

Code review is older than the tools that host it. In 1976 Michael Fagan of IBM described formal design and code inspections, meetings with defined roles in which a team read code line by line to find defects before testing. The form most teams use today, **modern code review**, is lighter: an author proposes a change in a tool, colleagues read the diff and comment asynchronously, and the change merges when they approve. It is far more frequent than an inspection, and that changes what it is for.

The best evidence on what it does comes from a 2013 study at Microsoft by Alberto Bacchelli and Christian Bird, who surveyed 165 managers and 873 programmers, interviewed 17 developers and classified 570 review comments. Finding defects was the motivation most often named first, by 44% of the programmers. Yet only 14% of the comments concerned defects, the fourth most common of nine categories, while the most common, at 29%, were improvements to the code. The authors concluded that reviews are "less about defects than expected" and also bring knowledge transfer, team awareness and alternative solutions. Engineers say they review to find defects, but most of what reviews actually produce is better code and shared understanding. The hardest part of reviewing, the study found, was understanding the change and its context.

Google's account, published in 2018 by Caitlin Sadowski and colleagues from interviews, a survey and the logs of some nine million changes, names four expectations of review: education, maintaining norms, gatekeeping and accident prevention. Review began at Google as an educational tool. The four belong together, because a team that treats review only as gatekeeping designs it for suspicion, and one that treats it only as education lets dangerous changes through politely.

Publishing divides a related job between two people. The editor reads for sense: does the argument hold, does the author mean what the sentence says? The copy editor reads for consistency: spelling, house style, the numbering of figures. No good publisher spends the editor's scarcer attention on the copy editor's work, and review at scale divides the same way, with tools as the copy editor and people as the editor. The analogy breaks where it matters. A book's editor serves the book, and once it is published the editor's knowledge of it has done its job. A reviewer's knowledge of a change is itself one of review's products, because the reviewer will be among those who must understand that code next year.

#### Small changes, fast reviews {#c4-small-changes}

The strongest single lever on review is the size of the change. Sadowski's study gives Google's numbers. The median change is 24 lines; more than 35% of changes touch a single file and about 90% fewer than 10. The median wait for a first response is under an hour for small changes and about 5 hours for very large ones, and the median whole review takes under 4 hours, against 14.7 to 19.8 hours in earlier studies at AMD, Chrome OS and Microsoft. The median change has one reviewer, and more than 80% need at most one round of revision. Google's guidance for engineers states the target: "100 lines is usually a reasonable size for a CL, and 1000 lines is usually too large" (a CL, or changelist, is Google's word for a change).

Size works so strongly because a reviewer opening a 600-line change must first build a model of what it is trying to do, which takes a block of uninterrupted time the reviewer may not have until tomorrow, while a 60-line change can be understood in the gap between two tasks. Small changes are reviewed sooner because they fit into the day.

Real work does not come in 60-line pieces, and the practitioners' answer is **stacked changes**: a sequence of small dependent changes, each reviewed separately and each building on the one before, so the author keeps working while the first is in review. Stacking is the norm at Meta and common at Google. It needs tool support, since stacking by hand in Git is error-prone, and it pays most where review takes longer than writing.

#### Review latency as a team metric {#c4-review-latency}

The Resale team's first changes to the reissue path bore out Chapter 1's survey. Verified Resale's changes touch seats and money, so under the Resilience book's review tiers (Section 4.5) they are Tier 1: two reviewers, one of them the domain owner. For barcode issuance the domain owner was Inventory, and in practice it was Lena, the last of the module's original authors, who had approved every change to it for three years. For the purchase saga it was Orders & Payments. In its first weeks, months four and five, the team's typical change was about 600 lines across the Resale service and `encore-core`, and the median time from opening a change to merging it was a little over two working days. Nobody was slow on purpose. The changes were large, they arrived unannounced in other teams' queues, and the one person who could approve the most important of them was also doing her own team's work.

DORA's 2023 report gives the general finding: "Teams with shorter code review times have 50% better software delivery performance." It is a correlation from survey data and does not say which way causation runs. The practical question is how to shorten review without making it worse, and Meta's 2022 account is the most useful answer. Meta measures **Time In Review**, the time a change spends waiting on reviewers, at the 75th percentile, because the slow tail is where frustration lives; it found "a correlation between slow diff review times (P75) and engineer dissatisfaction." A bot that nudges reviewers of overdue changes cut average Time In Review by 7% and the share of changes waiting more than three days by 12%. Meta also set a guardrail, "Eyeball Time," the time reviewers actually spent looking at a change, so that speed could not be bought by rubber-stamping.

Speed must not destroy the reviewer's flow either. Google's guidance holds both sides: "One business day is the maximum time it should take to respond to a code review request," and "If you are in the middle of a focused task, such as writing code, don't interrupt yourself to do a code review." The reconciling rule is to review at the next natural break and to make sure breaks come often enough that nobody waits more than a day.

Encore's fix had four parts, and none was a new tool. The Resale team split its work into stacked changes of under about 200 lines, each description naming its step in the reissue path. The teams involved agreed **review latency targets**: a first response within four working hours, and Time In Review at the 75th percentile under one working day, which each team sees on its own scorecard and nobody uses to rank teams. They adopted Meta's guardrail in a simple form, flagging Tier 1 changes over 50 lines approved within two minutes of being opened. And, most important, Inventory widened the circle of domain owners for barcode issuance. From month five two Inventory engineers, one of them Jonas, paired with Lena on every barcode change; DORA notes that pair-programmed code can count as reviewed, and the teams agreed to record those sessions as the review itself. Chapter 2 and Chapter 11 describe the larger work of raising the module's truck factor; review was one of its instruments. By month eight the median time from opening a change to merging it was about seven working hours, and the P75 Time In Review was under a day.

#### Reviewers and owners {#c4-reviewers-owners}

Google asks three things of every change: "A correctness and comprehension check from another engineer," "Approval from one of the code owners," and "Approval from someone with language 'readability'." One person can provide all three. The structure separates three questions that blur easily: is the change correct and understandable, does the person accountable for this code accept it, and can the organization maintain it? Google's readability certification is costly and peculiar to Google, and I would not import it whole, but its idea, that readable code is a skill taught through review, travels well. A human reviewer should look for what tools cannot see: whether the change does what its description says, whether that is the right thing to do, whether its design fits, and whether its tests would catch the failure that matters.

Not every change needs to wait for review. Rouan Wilsenach's "Ship / Show / Ask" (2021) names three options: *ship* merges directly under CI, *show* merges and invites review afterwards, and *ask* waits for review. It needs strong CI and is excluded for anything in Tier 1. At Encore a documentation fix or a dashboard change may be shipped or shown; anything that touches seats or money is always asked.

#### Automation in review {#c4-automation-review}

The copy editor of code review is static analysis, and Google's Tricorder, described by Sadowski and colleagues in 2015, is the most instructive account. It runs more than 100 analyzers in more than 30 languages on more than 50,000 review changes a day, and its findings appear as comments inside the review tool while the reviewer is reading. Two rules explain why engineers trust it. New checks must "Produce less than 10% effective false positives," and the overall rate stays "just below 5%." And every comment carries a "Not useful" button that files a bug against the analyzer, so the authors of a check hear when it wastes someone's time.

The same checks belong earlier still, in the editor or a pre-commit hook, configured from the same file as CI, so that most of what CI would catch is caught before a push. When local and CI configuration differ, developers learn that a clean local run means nothing and stop running it. As AI assistants write more code, this division of labor matters more, since human attention is what does not scale; Chapter 5 takes that up.

**Recap.** Modern code review produces better code and shared understanding more often than it finds defects, and Google names four purposes that a review practice should serve together. Size is the strongest lever on review latency, and stacked changes keep work moving without large changes. Encore cut its cross-team review wait from two days to under one by making changes smaller, setting latency targets each team sees for itself, guarding against rubber-stamping, and widening the circle of owners, while tools took over everything a tool can check.

**Exercise 4.3.** Export your team's last 100 merged changes with their size in lines and their time from opening to first response and to approval. Plot latency against size. Then find the five slowest changes and, for each, say whether size, a missing owner, a cross-team reviewer or something else explains the wait.

### 4.4 Continuous Integration as a Product

#### A practice before a server {#c4-ci-practice}

Continuous integration is often confused with the server that runs it. The Resilience book's Section 4.2 traces its history; we need only the definition. In the 2024 revision of his essay, first published in 2000, Martin Fowler defines it as each member of a team merging "their changes into a codebase together with their colleagues changes at least daily," each integration verified by an automated build. A CI server running on long-lived feature branches is the server without the practice. The practice's second half is easy to forget: when main breaks, fixing it comes first. Fowler quotes Kent Beck, "nobody has a higher priority task than fixing the build," and gives the quickest remedy: "The best way to fix the build is to revert the faulty commit from the mainline."

#### The commit stage {#c4-commit-stage}

The first stage of the pipeline, the one a developer waits on after every push, is the **commit stage**: compile, run the fast tests and static analysis, and build the artifact every later stage will use. Jez Humble and David Farley give its budget in *Continuous Delivery* (2010): "Ideally, a commit stage should take less than five minutes to run, and certainly no more than ten." The Resilience book's Section 4.2 takes the pipeline onward; this chapter owns the commit stage from the developer's side, what keeps it fast and green.

The golden path's commit stage takes about 6 minutes. `encore-core`'s took 31, which is why 54% of Encore's engineers named it among their three worst delays. A 31-minute commit stage costs more than the wait. Engineers batch changes to avoid paying it twice, so changes grow and reviews slow. They push and start something else, so a failure is noticed an hour later, with the context gone. And they merge before CI finishes, on the reasonable belief that it will probably pass, which makes main the place where failures are found.

#### Test selection {#c4-test-selection}

There are two ways to choose which tests to run. **Dependency-graph test selection** runs only the tests whose code depends, directly or transitively, on what a change modified. It is proven at scale in Google's continuous testing system, TAP, which aims to "run the minimal set to be sure the change is safe," and in Uber's per-change calculation of affected targets. It depends on an accurate build graph: a graph that misses a dependency skips a test that should have run, and the failure surfaces later, where it costs more. That is why Encore made `encore-core` hermetic before trusting the graph to skip anything.

**Learned test selection** goes further. Meta's predictive test selection, described by Mateusz Machalica and colleagues in 2019, trains a model on the history of changes and test results to predict which tests a change is likely to break. It runs about a third of the tests that transitively depend on the modified code, still catches more than 95% of individual test failures and more than 99.9% of faulty changes, and halves the cost of testing infrastructure. It is proven at Meta's scale, which supplies an enormous history to learn from. An organization of Encore's size should expect dependency-graph selection to deliver most of the benefit, and reach for a learned model only when it has the data and the graph has stopped being enough.

Encore still runs `encore-core`'s full suite every hour on the head of main, so that anything selection missed is caught within the hour and traced to a small range of commits.

#### Keeping main green {#c4-keeping-main-green}

Two changes can each pass CI and still break main together. Change A renames a function; change B, written the same morning against the old main, adds a caller of the old name. Each is green against the main it was tested on, and together they do not compile. With a few committers this is rare and easily reverted; in `encore-core`, where a dozen teams commit, it happens weekly. The remedy is a **merge queue**: each change ready to merge is tested against main *plus the changes ahead of it*, so main only ever advances to a state that has passed. Uber described its version in "Keeping Master Green at Scale" (2019); GitHub made a merge queue generally available in July 2023, and GitLab offers merge trains. Encore turned one on for `encore-core` once CI fell to 9 minutes, since a queue of 31-minute runs would have been unbearable. Service repositories, each with one team committing, do not need one.

The other enemy of a green main is the **flaky test**, one that passes and fails on the same code. Chapter 3 explained why tests flake and how to design against it; living with the flakes that remain belongs here. Encore borrowed its mechanics from Google, whose tooling, as John Micco described in 2016, "automatically quarantines the test," taking it off the critical path and filing a bug. Encore's version is policy in the CI configuration the Developer Portal team maintains:

```yaml
# ci/policy/flaky.yaml — applied to every repository on the golden path
detect:
  rerun_on_failure: 1             # one automatic rerun, never more
  flaky_if: fails_then_passes_on_same_commit
quarantine:
  action: remove_from_merge_gate  # still runs; result no longer blocks
  ticket_to: codeowners           # the owning team, from CODEOWNERS
  deadline_days: 14               # fixed or deleted by then
  after_deadline: fail_owner_build
report:
  scorecard: quarantined_tests    # visible count, per team
```

Each line answers a way quarantine goes wrong. One automatic rerun lets a flaky failure through once without teaching people to rerun until green. A quarantined test still runs, so its owners can see whether their fix worked. The ticket goes to a team, not to whoever happened to see the failure. And the deadline is enforced, because quarantined tests without one are forgotten.

#### The pipeline as a product {#c4-pipeline-product}

All of this needs an owner. At Encore the Developer Portal team owns CI pipelines and their templates, and Runtime owns deployment from the artifact onward. The arrangement is sensible, and for years it was understaffed. Developer Portal's four people also owned the portal, the templates, the service registry, the scorecards and the exception ledger. Nobody decided to neglect CI; it simply never reached the top of a backlog shared with five other products, and `encore-core`'s build grew slower by a minute or two a year, each minute too small to justify a project. In month five of year nine, after the survey's 54% and the Resale team's first weeks in `encore-core`, Encore added two engineers to Developer Portal to work on CI, which brought the team to six.

Treating CI as a product means giving it users, an owner, a measure of whether it serves them and a way to hear from them. A hospital laboratory is a fair comparison. Clinicians do not care how its analyzers work; they care about turnaround time, from drawing a sample to having a result they can act on, and about the rate of wrong results, and a well-run laboratory publishes both. The analogy holds for the choice of measures and breaks at the source of error: a laboratory's false results come partly from the variability of patients, while CI's false reds come almost entirely from its own tests and machines.

Developer Portal now publishes an objective for CI in the same form as any service's: time from push to verdict at the 50th and 90th percentiles, with the 90th at or under 10 minutes on golden-path repositories and 12 on `encore-core`, and a **false-red rate**, the share of failed runs that pass on rerun with no change, held under 1%. Server uptime is left out, because developers feel it only through those two numbers. Published objectives for CI are still rare, though Google's build-satisfaction surveys show the measuring is done. Encore also asks about CI in its quarterly developer survey, and Chapter 6 discusses how the platform group reads the answers. My own years of platform engineering inside a bank left me convinced that the most useful thing an internal tool team can do is state in public what it promises its users.

**Recap.** Continuous integration is the practice of integrating daily and fixing a broken main at once; the commit stage serves it best when it answers in five to ten minutes. Dependency-graph test selection is proven wherever the build graph can be trusted, and learned selection pays at the scale where it was proven. A merge queue and an enforced quarantine keep main green as more teams commit to one repository, and someone must own the pipeline as a product, with an objective that measures what its users feel.

**Exercise 4.4.** Find the five slowest steps in your CI for one repository, with the median and 90th-percentile duration of each, and the name of the team that owns each one. If any step has no owner, say who should have it, and estimate its false-red rate from the last month's reruns.

### 4.5 Feature Flags in Development

#### Trunk with flags {#c4-trunk-with-flags}

Trunk-based development leaves an obvious question: if everyone merges to main every day, where does work that will not be finished for weeks go? It goes to main, switched off. A **feature flag**, as the Resilience book's Section 4.3{% include xref.html to="resilience:4.3" %} defines it, is a runtime switch that decides which behavior deployed code exhibits, and it rests on the distinction between deploying and releasing that the Architecture book's Section 5.3{% include xref.html to="architecture:5.3" %} drew. Those books own flags as a tool of release, with its rollouts, kill switches and debt. This section treats flags as a tool of development: how a team keeps unfinished work on trunk without exposing it, and the code-level discipline that keeps this from becoming a mess.

Pete Hodgson's "Feature Toggles (aka Feature Flags)," published on Fowler's site in 2016 and revised in 2017, remains the standard account, and Google works this way at very large scale: as Potvin and Levenberg reported, its features are controlled by flags rather than branches. A flag keeps integration happening every day, so the unfinished feature is compiled, tested and merged against everyone else's work continuously and semantic conflicts surface the day they are created. A branch defers all of that to one day at the end.

A theater building the set for its next production while the current one is still running builds it backstage, in the same building with the same crew, so that measurements, rigging points and trapdoors are checked against the real stage as the work goes on. Nobody builds it in a distant warehouse and hopes it fits on opening night. The analogy breaks in an instructive place. A set backstage takes up space but leaves the current show untouched. Flagged code sits in the same files as the running code, behind an `if`, and every flag adds a second path that must be kept correct and eventually removed.

Verified Resale has lived this way since its first code. From month four, each piece went to main behind a release flag owned by the team that wrote it: the listing endpoints, the resale purchase saga, the Resale module in the fan app. For the final six weeks before the month-12 launch, the complete flow ran on trunk and in production, dark, behind one release flag, `resale-verified-flow`, exercised end to end by Encore's staff and by Rowmate's certification traffic. How it was then switched on belongs to the Products book's Chapter 10{% include xref.html to="products:10" %} and the Resilience book's Section 4.3{% include xref.html to="resilience:4.3" %}.

#### Kinds of flags {#c4-kinds-of-flags}

Hodgson distinguishes four kinds of flags, each with its own lifetime and owner. The Resilience book's Section 4.3 gives Encore's expiry rules; Figure 4.5 adds the owners.

| Kind | What it decides | Typical life (Hodgson) | Owner at Encore | Example in Verified Resale |
|---|---|---|---|---|
| Release | Whether unfinished or unreleased code runs | "should generally not stick around much longer than a week or two" | The team that wrote the code | `resale-verified-flow` |
| Experiment | Which variant a user sees, for measurement | As long as the experiment needs | The team running it, via the Experimentation platform | None at launch (the Products book's Chapter 4{% include xref.html to="products:4" %}) |
| Operational | Whether an expensive or risky path runs under stress | Mostly short; kill switches for years | The team on call for the service | `resale-listings-intake`, which stops new listings during an incident |
| Permission | Which users or customers get a capability | Can last "multiple years" | Moves to entitlements | Which organizers may enable resale |

*Figure 4.5 — Four kinds of flags, with Hodgson's lifetimes and Encore's owners. The last row is a flag only until it becomes configuration.*

The last row repays a closer look. A permission flag that lives for years has become a product decision about who may use what, and it belongs in the system that makes such decisions. At Encore that is the entitlement machinery Chapter 7 describes, on which organizers' resale rules are built as per-organizer configuration, so a permission flag may exist only while a capability is being built. Experiment flags belong to the Products book's Chapter 4{% include xref.html to="products:4" %}.

#### Branch by abstraction inside a codebase {#c4-branch-by-abstraction}

Flags hide a new feature. They do not by themselves help replace an old component that many parts of the code depend on, and that was Inventory's problem with reissue. Chapter 1 explained it: barcode issuance derives a ticket's identity from its order and seat, four other places in `encore-core` recompute it the same way, and reissue needs a ticket to receive a new identity, which the derived scheme cannot express. The technique for changing such a thing on trunk is **branch by abstraction**, which Paul Hammant described in 2007, crediting Stacy Curl with it. The Architecture book's Section 3.4 introduced it at the scale of a system; here are its mechanics inside one codebase.

Introduce an abstraction in front of the old implementation. Move every caller to it, one small change at a time. Build the new implementation behind the same abstraction, switch to it with a flag, and finally remove the old implementation. At every step trunk builds and the system works. The best-known public case is Thoughtworks' Go continuous-delivery server, whose team, as Jez Humble told it, replaced its object-relational mapping layer, iBatis, with Hibernate this way, all on trunk.

Inventory's abstraction took this shape.

```kotlin
// encore-core: services/seat-inventory/issuance/TicketIdentities.kt
interface TicketIdentities {
    fun issue(order: OrderId, seat: SeatId): TicketId
    fun current(order: OrderId, seat: SeatId): TicketId   // callers stop recomputing
    fun reissue(request: ReissueRequest): ReissueOutcome   // Chapter 2's contract
}

class DerivedIdentities : TicketIdentities {               // year-one behavior
    override fun issue(order: OrderId, seat: SeatId) = TicketId.derive(order, seat)
    override fun current(order: OrderId, seat: SeatId) = TicketId.derive(order, seat)
    override fun reissue(request: ReissueRequest): ReissueOutcome =
        error("derived identities cannot change")
}
// OpaqueIdentities stores identities: existing tickets keep their derived value,
// reissued ones get a random opaque id. Chosen by flag `ticket-identity-opaque`.
```

The first changes did nothing visible. They introduced the interface and moved the four places that recomputed identities to call `current`, one small change each. Only then did Inventory build `OpaqueIdentities`, whose essential property is that for every existing ticket it returns exactly what the derived scheme returns, so switching the flag changes nothing for any ticket until it is reissued. For three weeks in month eight both implementations ran in production, the new one answering in shadow with every disagreement logged, the parallel run of the Architecture book's Section 3.4{% include xref.html to="architecture:3.4" %}; Chapter 11 reports what it found. Once the flag was on everywhere, `reissue` could do its work through the interface Chapter 2 designed: a new opaque identity for the buyer, the old one onto the revocation feed, and a retry with the same idempotency key treated as the same reissue, since a ticket may be resold, and reissued, more than once. Partners receive a `ticket_id` through the API and never parse a barcode, which rotates in any case; the one partner whose old code had parsed the identity's prefix, Rowmate, rewrote it during sandbox certification, as Section 2.5 tells.

#### Testing flag combinations {#c4-testing-flags}

A system with *n* flags has 2ⁿ possible configurations, and at 2,300 flags no team will test them all, nor should it try. Hodgson's advice is the practical one: "It's most important to test the toggle configuration which you expect to become live in production." He adds that "Many teams also perform some tests with all toggles flipped On," and he recommends testing the fallback, the configuration with the new toggles off, so that turning a flag off in an emergency is known to work.

Encore tests three configurations per service: production-next, the flag values the service will have after the change ships, taken from a snapshot of the flag service; all-new-on, which catches a new path that works only while another new path is off; and fallback, with the change's own flags off. Test fixtures default to the production snapshot, because a suite that hard-codes every flag to off is quietly testing a system that no longer exists. During its six dark weeks, `resale-verified-flow` also had a small suite of journey tests that ran with the flag on in every build, so the hidden product was tested as continuously as the visible one.

#### Cleanup as part of done {#c4-cleanup}

The Resilience book's Section 4.3 tells how Encore found a third of its 2,300 flags unchanged for a year, and sets out the rules that followed, along with Uber's Piranha, which writes cleanup changes automatically. What remains here is the code side.

The change that removes a release flag should delete the flag check, the branch no longer taken and the tests that exercised it, together. Hodgson describes teams that create "a toggle removal task" with the toggle, and others that build "time bombs," tests that fail once a flag expires. Encore uses the first and a variant of the second: a lint step in the commit stage fails on any reference to a flag the flag service does not know and warns on any reference to an expired one. A month after full release, the Resale team's removal of `resale-verified-flow` deleted about 300 lines across four repositories. Inventory's removal of `ticket-identity-opaque` took `DerivedIdentities` with it, and with that went the last place in Encore's code that assumed a ticket's identity could never change.

**Recap.** Flags let unfinished work live on trunk and integrate every day, which is why they beat long-lived branches, and each kind of flag has its own lifetime and owner, with long-lived permission flags belonging in entitlements. Branch by abstraction lets a team replace a component that many callers depend on, one reviewable change at a time, and with a parallel run it let Inventory change the year-one assumption about ticket identity without stopping the system. Test the configurations production will have, default tests to production's values, and remove each flag with its dead branch and tests in one change.

**Exercise 4.5.** List the flags in one service you own, with each one's kind, owner and removal date. Find one whose purpose is finished, and write the change that deletes it, including the dead branch and its tests. Note what you found that nobody had remembered was there.

### Kata: The Two-Quarter Lead Time

> **Your brief: "Inkstone."** Inkstone makes a collaborative design tool used in browsers and a desktop app, sold by subscription to studios and in-house design teams. It has 250 engineers in 26 stream-aligned teams and a platform team of eight, and its code lives in 30 repositories: a large `inkstone-app` repository that holds the editor, the rendering engine and the collaboration server, which together account for about two-thirds of all changes, and 29 smaller service repositories. CI on `inkstone-app` takes 45 minutes at the median and over an hour at the 90th percentile; its tests reach the network, and about one failed run in eight passes on rerun. The median change is about 450 lines, and changes that touch the rendering engine wait a median of two working days for review, because three engineers approve almost all of them. Teams use long-lived feature branches merged at the end of each two-week sprint, and the merges regularly break `main` for half a day. Nobody owns CI; the platform team runs the build machines and treats everything else as the product teams' problem. The CTO has asked for the lead time from first commit to merge on `main` to be halved within two quarters, and wants to know, before committing, how the company will tell whether it worked.

**Deliverables:**

1. **Baseline** — Measure lead time from first commit to merge on `main` for the last quarter, at the median and 75th percentile, split into its parts: time on a branch before review is requested, time in review, time in CI and time waiting to merge. Say which part is largest, and how you obtained each number.
2. **Branching and flags** — Propose a move from sprint-long branches to trunk-based development, with the flag practice that makes it possible. Name the kinds of flags you will allow, their owners and how each is removed, and give one branch-by-abstraction plan for a component of the rendering engine.
3. **Review plan** — Set a target change size, a latency target for first response and for P75 time in review, and a guardrail against rubber-stamping. Say how you will widen the circle of rendering-engine reviewers, and which changes may be shipped or shown without waiting for review.
4. **CI plan** — Lay out how `inkstone-app`'s CI gets from 45 minutes to under 10: what you would make hermetic first, how you would select tests, whether you need a remote cache or a merge queue, and how flaky tests are quarantined. Say who owns CI afterwards, how many people it needs and what objective they publish.
5. **Measurement and timeline** — Lay out the two quarters in order, explaining why that order, and name the measures, with guardrails, that will show the CTO whether the lead time halved without stability or review quality getting worse.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Finding the constraint | Does the baseline show where changes actually wait, and does the plan act there first? |
| Integration over branching | Does the plan make integration daily, with flags and branch by abstraction carrying unfinished work on trunk? |
| Review as a human system | Do the review targets respect reviewers' focus as well as authors' waits, and do they widen ownership as well as speed it up? |
| CI as a product | Does CI get an owner, an objective that measures what developers feel, and enough people to keep it? |
| Safe speed | Would the measures catch a lead time halved by skipping tests or rubber-stamping reviews? |
| Proven practice | Is each recommendation backed by a documented case, with anything unproven labelled as Inkstone's own choice? |

#### Where you now stand

You can now look at the development loop as a system of its own and find where a change waits on its way from a laptop to main. You can give a developer's code the neighbours it needs without running the fleet, choose a repository shape knowing what each costs, make a build trustworthy enough to cache and to select tests from, keep review fast without making it careless, run CI as a product with an owner and an objective, and carry unfinished work on trunk behind flags that are removed when their work is done. You have also seen why none of this followed automatically from Git: cheap branches made integration easier to postpone, and the discipline of integrating daily had to be learned separately. One force now presses on every part of this loop at once. Assistants that write code can produce changes faster than any loop designed for human authors was built to absorb, and the question of what that does to review, testing and ownership is the subject of Chapter 5.

### References

- Jez Humble, David Farley — [*Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*](https://continuousdelivery.com/). Addison-Wesley, 2010.
- Titus Winters, Tom Manshreck, Hyrum Wright (eds.) — [*Software Engineering at Google: Lessons Learned from Programming Over Time*](https://abseil.io/resources/swe-book). O'Reilly, 2020 — free online.
- Caitlin Sadowski, Emma Söderberg, Luke Church, Michal Sipko, Alberto Bacchelli — [*Modern Code Review: A Case Study at Google*](https://sback.it/publications/icse2018seip.pdf). ICSE-SEIP, 2018 — free online.
- Martin Fowler — [*Patterns for Managing Source Code Branches*](https://martinfowler.com/articles/branching-patterns.html). martinfowler.com, 2020 — free online.
- Alberto Bacchelli, Christian Bird — [*Expectations, Outcomes, and Challenges of Modern Code Review*](https://zenodo.org/records/1401198). ICSE, 2013 — free online.
- Nicole Forsgren, Jez Humble, Gene Kim — *Accelerate: The Science of Lean Software and DevOps*. IT Revolution, 2018; with DORA — [*Capabilities: Trunk-based development*](https://dora.dev/capabilities/trunk-based-development/), dora.dev — free online.
- Pete Hodgson — [*Feature Toggles (aka Feature Flags)*](https://martinfowler.com/articles/feature-toggles.html). martinfowler.com, 2016, revised 2017 — free online.
- Michael E. Fagan — [*Design and Code Inspections to Reduce Errors in Program Development*](https://ieeexplore.ieee.org/document/5388086). IBM Systems Journal 15(3), pp. 182–211, 1976.
- Patrick Riggs — [*Move faster, wait less: Improving code review time at Meta*](https://engineering.fb.com/2022/11/16/culture/meta-code-review-time-improving/). Engineering at Meta, 2022 — free online.
- Tyler French, Mindaugas Rukas, Xiaoyang Tan — [*How We Halved Go Monorepo CI Build Time*](https://www.uber.com/blog/how-we-halved-go-monorepo-ci-build-time/). Uber Engineering, 2022 — free online.
- Rachel Potvin, Josh Levenberg — [*Why Google Stores Billions of Lines of Code in a Single Repository*](https://doi.org/10.1145/2854146). Communications of the ACM 59(7), 2016.
- Mateusz Machalica, Alex Samylkin, Meredith Porth, Satish Chandra — [*Predictive Test Selection*](https://arxiv.org/abs/1810.05286). ICSE-SEIP, 2019 — free online.
- Garrett Heel — [*Scaling productivity on microservices at Lyft (Part 1)*](https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-1-a2f5d9a77813). Lyft Engineering, 2021 — free online.
- Google Cloud and DORA — [*Accelerate State of DevOps Report 2023*](https://dora.dev/research/2023/dora-report/). Google Cloud, 2023 — free online.
- Linus Torvalds — [*Kernel SCM saga..*](https://lkml.iu.edu/hypermail/linux/kernel/0504.0/1540.html). linux-kernel mailing list, 6 April 2005 — free online.
- Scott Chacon, Ben Straub — [*Pro Git*, 2nd ed.](https://git-scm.com/book/en/v2). Apress, 2014 — free online.
- Vincent Driessen — [*A successful Git branching model*](https://nvie.com/posts/a-successful-git-branching-model/). nvie.com, 2010, with a note of reflection added in 2020 — free online.

---

## Chapter 5: Building with AI Assistance {#ch5}

> "If the library is well-stocked, programming has been reduced to a matter of hours, rather than weeks." — Grace Murray Hopper, 1952

What does a machine that writes code actually change about building software with 400 engineers, and how would we know? The question sounds new, and the tools that raise it are new, but the promise behind it is one of the oldest in our field. Every generation of programmers has been told that programming is about to write itself. Each time, something real happened: the cost of producing some part of a program fell sharply. And each time, the work that remained turned out to be the harder part, the part that had been hidden behind the labor of typing instructions. The honest way to approach today's assistants is to ask which of those two things is happening now, and in what proportion, and to let the evidence answer.

The story that frames this chapter begins in 1952, when Grace Hopper described a program that assembled other programs out of a library of routines, and her colleagues declined to believe it could work. Section 5.1 develops that story, because it teaches something the present debate keeps forgetting: the doubters of automatic programming were partly right, its champions were partly right, and the work moved up a level without disappearing. We then examine the modern evidence in detail. This chapter is the series' home for that evidence, and where it is young we say so.

Encore is not deciding whether to adopt these tools. It adopted them years ago, piecemeal, as every company did. A coding agent rebuilt the Notification service overnight in year seven, and by the autumn of year eight a quarter of Encore's merged changes carried an agent label, as the Resilience book's Section 4.5{% include xref.html to="resilience:4.5" %} recorded. What Encore has never done is measure what the tools are worth. Verified Resale is the first large change built with them from the start. An agent migrates 60 call sites off the legacy barcode format, an assistant drafts the hand-written parts of the partner SDKs (software development kits), and a graduate engineer on the new Resale team learns the event-sourced seat ledger with an assistant at his side. Meanwhile Encore's leadership has asked a plain question, whether the tools pay, and a small working group has answered it with a measurement plan. The policy for reviewing agent changes already exists, in the Resilience book's Section 4.5{% include xref.html to="resilience:4.5" %}, and this chapter does not rewrite it. Our subject is the other side of the work: what the author owes before review begins, and what the organization owes before it claims a result.

### 5.1 The Evidence

#### Automatic programming, 1952 {#c5-automatic-programming}

Grace Murray Hopper learned to program on the Harvard Mark I during the Second World War. In 1949 she joined the Eckert-Mauchly Computer Corporation in Philadelphia, which Remington Rand bought the following year, and there she helped program the UNIVAC I, the first large commercial electronic computer in the United States. Programming it meant writing machine instructions by hand, and much of the writing was the same routines, recopied and readdressed for every new problem. In 1951 and 1952 Hopper and her group built a program they called the A-0 compiling routine. The word "compiler" meant something narrower then than it does now. The mathematician wrote a specification that named subroutines by their call numbers in a catalogued library, together with their arguments. A-0 fetched those subroutines, adjusted their addresses so that they fit together, and produced a complete machine-code program, which was then run. In today's terms it was closer to a linking loader with a subroutine library than to a translator of formulas, and it was not alone: Alick Glennie's Autocode at Manchester and Laning and Zierler's algebraic system at MIT have competing claims to being first. A-0 was one of the earliest such systems, and it is the one that gave the word "compiler" its software meaning.

Hopper described the scheme at the Association for Computing Machinery's national meeting in Pittsburgh in May 1952, in a paper called "The Education of a Computer". "The programmer may return to being a mathematician," she wrote. "He is supplied with a catalogue of subroutines." She saw, earlier than most, where the cost of computing was going: "With the computer paid for, the cost of programming and the time consumed, comes to the notice of vice-presidents and project directors." And she was candid about the price. Standardized subroutines, she noted, lose "a small amount of time … in performing duplicate data transfers which could be eliminated in a tailor-made routine". Her answer was to let the UNIVAC produce the program and then have a person remove the duplication by hand. That is the 1952 form of a practice this chapter will keep returning to: let the machine generate, then have a person refine and own the result. Figure 5.1 sketches the arrangement.

{% include diagrams/fig-5-1.svg %}

*Figure 5.1 — A-0's scheme, drawn as a schematic. The mathematician names subroutines by call number; A-0 fetches them from the library and fits them together; a person removes the duplicate transfers by hand. The machine generates, and a person refines and owns.*

The reception was cool. In 1987 Hopper told an interviewer, in a newsletter profile, "Nobody believed that. I had a running compiler and nobody would touch it. They told me computers could only do arithmetic." It is reported speech, recalled 35 years later, and should be read as such, but John Backus's own account of the period describes the same resistance. Writing in 1976, Backus recalled the programmers of the early 1950s as "members of a priesthood guarding skills and mysteries far too complex for ordinary mortals". To them, he wrote, "it was obviously a foolish and arrogant dream to imagine that any mechanical process could possibly perform the mysterious feats of invention required to write an efficient program." The phrase of the day for the whole enterprise was **automatic programming**: the hope that a machine could produce a working program from a description less detailed than the program itself. The Office of Naval Research held a symposium under that name in May 1954.

Two things about this history matter for us. First, the skeptics were not simply wrong. A-0's programs really were less efficient than hand-tuned code, and efficiency was a serious matter on machines whose time was scarce and expensive. It took FORTRAN's optimizing compiler, delivered in 1957, to show that generated code could be good enough that most programmers would stop checking it. The Architecture book's Section 15.4 uses that FORTRAN moment as a passing parallel to today's agents and shows where the parallel breaks: a compiler is deterministic and its behavior is specified, and a model is neither, so we can never come to trust the generator the way programmers came to trust FORTRAN. Our trust must rest on checks of what comes out. Second, consider what happened to the work. Fred Brooks, in "No Silver Bullet" (1986), listed automatic programming among the hopes that would not deliver an order-of-magnitude gain, and cited David Parnas's judgment that the phrase had only ever meant programming in a language one level higher than the programmer currently had. Hopper's library did not abolish programming. It moved programming up a level, from instructions to specifications, and the specification turned out to be where the difficult thinking had always lived.

#### Controlled studies of single tasks {#c5-controlled-studies}

The cleanest evidence comes from a **randomized controlled trial (RCT)**: an experiment in which participants are assigned by chance to work with or without the tool, so that any difference in outcome can be attributed to the tool rather than to who chose to use it. Two such trials anchor the early evidence.

The first, by Sida Peng and colleagues, ran from May to June 2022, just before GitHub Copilot became generally available. The authors recruited 95 freelance developers through Upwork and randomized 45 of them to use Copilot and 50 to work without it. Everyone received the same task: implement an HTTP server in JavaScript, checked by 12 tests that participants could see but could not edit. Among those who finished, the treated group took 71.17 minutes on average and the control group 160.89, which the authors report as 55.8% faster, with a 95% confidence interval of 21% to 89%. The treated group's success rate was seven points higher, but that difference was not statistically significant. Less experienced developers, those who spend more hours a day coding, and developers aged 25 to 44 gained the most. Asked to estimate their own gain, participants in both groups guessed about 35%, well below the 55.8% that was measured. They underestimated what the tool had done for them.

The second trial, by Elise Paradis and colleagues at Google, published in 2025, put 96 full-time Google engineers on one complex, enterprise-grade task in the summer of 2024, with or without three AI features in their internal tools. The best estimate was about 21% less time with the features, and the authors describe the confidence interval as large. Engineers who spend more hours a day on code gained more. The authors caution that Google's internal tooling may not generalize to other companies.

Both studies are well designed, and both are narrow by construction. Each measured one bounded task with a clear definition of done, the setting in which assistance should help most, and it did. Such trials cannot tell us what happens to a codebase that lives for years, or to the team that reviews the output.

#### Field experiments {#c5-field-experiments}

The best causal evidence from real work is a set of three randomized field experiments run at Microsoft, at Accenture and at an anonymous Fortune 100 company, analyzed by Kevin Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng and Tobias Salz. The working paper circulated from 2024, and the study was published in *Management Science* online on 27 February 2026. Each experiment was run by the company "as part of their ordinary course of business": chance decided which developers were given GitHub Copilot, a completion assistant, and which were not. Pooled across the three experiments and 4,867 developers, access to the assistant raised the number of completed tasks by 26.08%, with a standard error of 10.3%. "Less experienced developers had higher adoption rates and greater productivity gains."

Three cautions belong with the number. The abstract itself says that "each experiment is noisy and results vary across experiments", so the pooled estimate is real but imprecise. "Completed tasks" were measured mainly as pull requests, which counts output and says nothing directly about whether the output was worth having. And the tool was a completion assistant, so the result describes that class of tool and says nothing directly about agents. The study's lasting contribution is its method: it shows that a company can randomize access to a developer tool inside its ordinary operations and learn something true. Section 5.5 borrows that design.

#### The study that disappointed {#c5-metr}

In July 2025, METR (Model Evaluation and Threat Research) published a trial that set the rest of the evidence in a different light. Joel Becker, Nate Rush, Elizabeth Barnes and David Rein recruited 16 experienced open-source developers to work on 246 real issues in their own repositories, which averaged more than 22,000 stars and more than a million lines of code. Each issue, roughly two hours of work, was randomly assigned to be done with AI tools allowed or not; the tools were mostly Cursor Pro with Claude 3.5 and 3.7 Sonnet, and the work ran from February to June 2025. With AI allowed, tasks took 19% longer, with a confidence interval of 2% to 39% longer. Before starting, the developers expected a 24% speedup. Afterward, they believed they had been 20% faster.

I spent a decade maintaining a widely used open-source library, and the setting METR chose is one I recognize: a large, mature codebase whose maintainers carry years of unwritten context about why things are the way they are, and whose quality bar is set by thousands of users who will notice any regression. There an assistant has the least to offer and the most to get wrong. METR was careful to say what its result does not show. It does not show that AI tools fail to speed up most developers, nor that no better way of using them exists. It shows that in this demanding setting, with early-2025 tools, experts were slower and did not know it. Their perception was wrong by about 40 percentage points, in the opposite direction from Peng's participants, who had underestimated their gain. Together, the two studies teach this section's most useful lesson: developers' sense of how much a tool helps them is unreliable in both directions, and no organization should decide anything on the strength of it. Figure 5.2 sets the two trials side by side.

{% include diagrams/fig-5-2.svg %}

*Figure 5.2 — What developers believed against what two randomized trials measured. Peng's participants underestimated their gain; METR's experts believed they were faster when they were slower. Sources: Peng et al. (2023); Becker et al., METR (2025).*

METR has since marked the 2025 results as out of date, and its follow-up shows how hard the measurement has become. A second study, begun in August 2025 with 57 developers (10 returning and 47 new), 143 repositories and more than 800 tasks, estimated an 18% reduction in time for returning developers (confidence interval from 38% faster to 9% slower) and 4% for new ones (from 15% faster to 9% slower). Both intervals include zero. METR called the result "an unreliable signal": developers who did not wish to work without AI declined to take part, between 30% and 50% of participants withheld tasks they did not want to do unaided, and time-tracking broke down for developers running several agents at once. METR is redesigning the study, so the effect on experienced developers in mature code has not been reliably measured since 2025. A METR survey from May 2026 adds a final caution. Of 349 technical workers who responded, at a response rate of about 2%, the median reported that AI had made them 3× faster. Beside the 2025 trial's gap between belief and fact, that figure shows how far perception can run from measurement, and nothing more.

#### What DORA sees at the team level {#c5-dora}

The trials measure individuals on tasks. DORA (DevOps Research and Assessment), the research program behind the delivery metrics most engineering organizations use, measures teams, through large annual surveys. Its 2024 report found that as AI adoption rose, delivery suffered: "As AI adoption increased, it was accompanied by an estimated decrease in delivery throughput by 1.5%, and an estimated reduction in delivery stability by 7.2%." Those estimates are for each 25% increase in adoption, and the same increase went with better documentation quality (7.5%), code quality (3.4%) and code review speed (3.1%). The craft of the individual improved while delivery slowed and became less stable.

The 2025 report, *State of AI-assisted Software Development*, drew on nearly 5,000 technology professionals and more than 100 hours of qualitative data. Adoption had become "near-universal: 90%". More than 80% of respondents believed AI had raised their productivity, and 30% reported little or no trust in the code it generated. The central finding changed sign on one measure and not on the other: "Unlike last year, we observe a positive relationship between AI adoption on both software delivery throughput and product performance. However, AI adoption does continue to have a negative relationship with software delivery stability." Both halves must travel together. Teams that adopted more tended to ship more, and their delivery tended to be less stable. DORA framed AI as an amplifier of a team's existing strengths and dysfunctions alike, and published an AI Capabilities Model, to which Section 5.5 returns.

DORA's data carry their own conditions. They are self-reported, from self-selected respondents, and the findings are correlations, so they cannot say whether adoption causes instability or whether teams that adopt eagerly differ in other ways. What they offer is breadth: thousands of teams, in every kind of company. The Resilience book's Section 4.5 has already taken the stability finding into Encore's review policy. Sections 6.5 and 10.5 of this book point back here for the numbers.

#### How to read all of it {#c5-reading-the-evidence}

Figure 5.3 gathers the studies in one place, with the setting each one measured and the most important thing it cannot tell us.

| Study | Setting and design | Main finding | What it cannot tell us |
|---|---|---|---|
| Peng et al., 2023 | 95 freelancers, one bounded JavaScript task, randomized | 55.8% faster; participants guessed about 35% | anything about mature code, review or teams |
| Paradis et al., 2025 | 96 Google engineers, one complex task, randomized | about 21% less time, wide interval | whether Google's internal tools generalize |
| Cui et al., 2026 | 4,867 developers at three companies, randomized access in ordinary work | 26.08% more completed tasks (standard error 10.3%), larger for less experienced | whether the extra pull requests were worth having |
| METR, 2025 | 16 expert maintainers, 246 issues in their own mature repositories, randomized | 19% slower; believed 20% faster | how later tools and practices fare (the 2026 follow-up is unreliable) |
| DORA, 2024–2025 | thousands of survey respondents, correlational | throughput turned positive in 2025; stability negative in both years | cause and effect |

*Figure 5.3 — The evidence on AI assistance and productivity. Each study is sound within its setting, and the settings differ more than the headlines do.*

Read together, the studies are less contradictory than they first appear, because they measured different situations. Gains are largest on bounded, well-specified work and on work unfamiliar to the person doing it: a fresh server in a language one half-knows, a task in a codebase one has not lived in. Gains shrink, and can reverse, where experts work in mature code under high quality bars, because there the assistant contributes least of what the expert lacks and most of what the expert must then check. Perception is unreliable in both directions, so no organization can learn the answer by asking its engineers. Team outcomes depend on the system around the tool, the tests, review, batch size and platform that must absorb a higher volume of change. And as Section 5.4 will show, the velocity gained early can be bought with complexity that slows the same team later.

Brooks's distinction between essential and accidental complexity, introduced in the Architecture book's Section 1.2{% include xref.html to="architecture:1.2" %}, makes this pattern intelligible. An assistant attacks accidental complexity very well: recalling an API, writing the boilerplate around a query, translating a test from one framework to another. It does nothing for essential complexity, such as deciding what a resold ticket means to a door scanner that has no network, or which of five fairness rules a new endpoint might violate. Where most of a task is accidental, the gain is large. Where most of it is essential, the assistant's speed in the accidental part is spent checking its guesses about the essential part. Hopper's library worked the same way. It removed the drudgery of recopying routines and left the mathematician with the specification, which was the hard part all along.

**Recap.** Controlled trials show real gains on bounded tasks, and field experiments show smaller, noisy gains in real work, largest for less experienced developers. Experts in mature code were slower in the one careful trial of that setting, and believed the opposite. Team-level data show throughput rising with adoption while stability falls. The pattern follows Brooks's distinction: assistance removes accidental complexity and leaves the essential kind exactly where it was.

**Exercise 5.1.** For one recent task done with an assistant, write down how long you think it took and how long it would have taken without the tool. Ask a colleague who knows the task to make the same two estimates independently. Then check the timestamps in your version control and ticket history, and compare all three numbers.

### 5.2 Where It Helps

Section 5.1 predicts where assistance should pay: on work whose difficulty is mostly accidental, whose correctness machinery can check, and whose result a person can review without reconstructing every decision behind it. The strongest published accounts of assistance at scale come from exactly that kind of work.

#### Migrations at scale {#c5-migrations}

A **migration**, in this sense, is a change of the same kind applied at many places in a codebase: replacing a deprecated library, widening a type, moving from one testing framework to another. Section 2.5 described how large organizations make such changes, by splitting one logical change into many small shards, each reviewed and landed on its own. Migrations suit assistance unusually well, because the rule is known in advance, each instance is small, and the existing tests say whether an instance broke anything.

Google has published the most detailed account. In "How is Google Using AI for Internal Code Migrations?" (2025), Stoyan Nikolov and colleagues describe migrating identifiers in Google Ads, a codebase of more than 500 million lines, where "dozens" of ID types were defined as 32-bit integers and used in "tens of thousands of code locations across thousands of files". The team located the code with Kythe, Google's code-indexing system, prompted a model per change type, and sharded the results to the code's owners. Measured character by character, comparing the model's first output with what was finally committed, "80% of the code modifications in the landed CLs were fully AI-authored". (A CL, or changelist, is a change submitted for review.) Engineers estimated that the total time, including review and landing, fell by about 50%. The paper is equally plain about the rest: in most cases "the human needed to revert at least some changes the model made". A companion paper, "Migrating Code At Scale With LLMs At Google" (2025), by Celal Ziftci and several of the same authors, reports 39 distinct migrations carried out by three developers over twelve months: 595 code changes and 93,574 edits, of which 74.45% of changes and 69.46% of edits were generated by the model, again with an estimated halving of migration time. Every change passed automated checks including the build and regression tests, was inspected by its developer, and was reviewed by the code's owners.

Two cautions keep these numbers honest. The papers share authors and describe one family of migrations within one company, so they are best read as two measurements of one program in different units (characters of landed code in one, changes and edits in the other), and they do not confirm each other independently. The time savings, too, are the engineers' own estimates, which nobody measured under control. A second company supplies some independence. Airbnb reported in March 2025 that it had migrated nearly 3,500 React component test files from Enzyme to React Testing Library in about six weeks, against an estimate of a year and a half by hand.

Publishing offers a fair comparison. When a publisher changes its house style, a copy editor can apply the new rule across a whole backlist quickly, because the rule is explicit and each instance can be checked against the style sheet. The work goes wrong only where a sentence's meaning depended on the old form, where changing a word mechanically would change what the author said. A good copy editor flags those sentences and leaves them to the author. The comparison holds well for migrations and fails at one point: a copy editor knows when meaning is at stake and stops, while a model applies the rule with the same confidence everywhere. Somebody has to find the sentences whose meaning will change, and that somebody is the owner of the code.

Encore's own migration had exactly this shape. Barcode issuance, the eight-year-old core described in Chapter 2, embeds an event-code prefix in its legacy barcode format, and over the years 60 places in Encore's code had learned to read that prefix directly; none of them asked Seat Inventory which event a ticket belonged to. Verified Resale gives every ticket an opaque `ticket_id`, and reissue makes the prefix unreliable, so all 60 call sites had to move to the new identity lookup. They sat in 11 repositories owned by seven teams. Ines, a staff engineer on the Inventory team, which the draw described in Section 5.5 had placed in the first cohort to receive background agents, sponsored the migration. Once the characterization tests described in Chapter 2 were in place, she ran it much as the Google papers describe: a background agent generated one change per call site, and a ladder of checks ran before any human owner saw a line of it. Figure 5.4 shows the ladder.

{% include diagrams/fig-5-4.svg %}

*Figure 5.4 — The validation ladder for Encore's barcode call-site migration, with what each rung caught. Each rung is cheaper than the one after it, so the cheap machine rungs run first and spare the expensive human ones.*

#### Tests and boilerplate {#c5-tests-boilerplate}

Tests and boilerplate are the next obvious candidates, and the evidence is thinner: no controlled study has measured the quality of tests that assistants write. What we have is practitioner guidance, from Addy Osmani's *Beyond Vibe Coding* and from Gene Kim and Steve Yegge's *Vibe Coding*, both published in 2025, together with Airbnb's migration, which was itself a migration of tests. The guidance converges on one condition. A test has two parts: the setup that drives the code, and the **test oracle**, the part that decides whether the output is correct. Generating the setup is cheap and largely safe. Generating the oracle is where the danger lies, because a test whose oracle was inferred from the code under test will faithfully confirm whatever the code does, bugs included.

So the condition for using generated tests is that a person writes or approves the oracle, and that the author of the code, human or agent, cannot quietly change it. Peng's experiment used exactly this arrangement, with tests participants could see but not edit, and Encore's barcode migration used it on rung 2 of Figure 5.4. The Resilience book's Section 4.5 explains why the second half of the condition matters, with the evidence that agents faced with tests they cannot honestly pass often edit the tests instead; we take that finding as given here. What this chapter adds is the author's habit. When an assistant drafts tests for code you are writing, read the assertions before anything else, and ask of each one whether you would have written that expectation yourself, from the specification, without looking at the code.

The partner SDKs show where boilerplate generation fits in Encore's work. The client libraries in TypeScript, Python and Java are generated deterministically from the OpenAPI contract of the partner application programming interface (API), as any well-run API program does; that generation is ordinary tooling, with no model involved. What an assistant drafted were the hand-written parts around the generated core: usage examples, documentation, and small idiomatic helpers for retries with idempotency keys. Partners are promised 12 months' notice of any breaking change, so the SDKs' public surface runs through the same breaking-change differ as the API itself. In the first month the differ stopped an assistant-drafted helper that had renamed a public method to something tidier, a rename that would have broken every partner who called the old name.

#### Prototypes and throwaway code {#c5-prototypes}

Osmani distinguishes two ends of a spectrum. At one end is "vibe coding", accepting generated code by its apparent behavior without reading it closely; at the other is AI-assisted engineering, in which a person owns the design, reviews the output and verifies it. The framing is a practitioner's, and it lets us say plainly where the first end belongs: spikes, demos, internal one-offs, and the clickable prototypes that the Products book's Section 3.5{% include xref.html to="products:3.5" %} uses in discovery. Code whose only job is to answer a question, and which will be discarded once the question is answered, can be written by feel, because nobody will maintain it.

The engineering rule is that throwaway code must actually be thrown away, and it is the rule most often broken, because a prototype that works is a standing temptation to ship. Section 5.4 describes the measured cost of yielding: a brief rise in velocity and a lasting rise in warnings and complexity. Encore keeps prototypes structurally apart. The Resale team's discovery prototypes lived in a sandbox repository with no deployment pipeline to production, no access to production credentials and an expiry date in its README. When the team decided to build the fan resale module for real, it started from the prototype's screens and lessons and wrote the code again on the golden path.

#### Where it does not help yet {#c5-not-yet}

The same pattern that predicts where assistance helps predicts where it does not. It helps least in mature hotspots, the files that change often, break often and carry years of accumulated reasons; on invariants that span services, which no single file states; and on ambiguous requirements, where the hard part is deciding what to build. Osmani calls the experience the "70% problem": an assistant takes a task most of the way quickly, and the last 30%, the edge cases, the integration, the security and the maintainability, takes as long as it ever did, or longer, because it must now be done inside code the engineer did not write. The 70 and the 30 are a metaphor, not a measurement, and should not be quoted as data. But its shape fits METR's 2025 trial, and the Stack Overflow Developer Survey of 2025, in which 84% of roughly 49,000 respondents used or planned to use AI tools and about two-thirds named solutions that are "almost right, but not quite" as a frustration.

Encore's five fairness invariants show the problem concretely. Invariant 3 says that organizer caps and rules can only tighten. No single file in the codebase states it; it is enforced by the type of the rule set in the Resale service, by a check in the organizer console, and by tests in CI. An assistant adding a rule option sees only its file, and nothing there says that an option which loosens a default breaks a promise Encore has made to every organizer. The invariant lives in the system and in the heads of the people who designed it, and an assistant can respect it only once someone has written it where the assistant will read it.

Understanding unfamiliar code is a harder case to judge, and it deserves an honest label: the evidence here is practitioner experience only. No controlled study has isolated it, but two adjacent findings point in a useful direction. Peng and Paradis both found larger gains on unfamiliar tasks and stacks, and a 2026 study discussed in Section 5.5 found that engineers who used an assistant to ask conceptual questions kept their understanding, while those who delegated the work lost it. The practice that follows is modest: ask the assistant to explain the code, then verify the explanation against the code and tests before acting on it. Encore's engineers used it this way on the barcode module, whose last remaining author had been its only reader for years. The assistant's account of the issuance path was mostly right and once confidently wrong, about the order in which a retry wrote its two records. The characterization tests caught the error before anyone built on it.

**Recap.** Assistance pays best on migrations, with a human oracle on tests, and on code that is truly thrown away. It pays least on mature hotspots, cross-service invariants and ambiguous requirements, where the essential complexity sits. Explanation of unfamiliar code is useful on practitioner evidence alone, provided the explanation is checked against the code before anyone relies on it.

**Exercise 5.2.** Sort your team's last month of completed work into the four categories of this section: migrations, tests and boilerplate, throwaway code, and the work where assistance does not help yet. For each item, note whether an assistant was used and whether, looking back, it paid. Compare the pattern with Figure 5.3.

### 5.3 Agents in the Loop

#### From completion to agents {#c5-completion-to-agents}

The tools have changed shape quickly. Four classes are now in common use. Inline completion suggests the next few lines as the engineer types. Chat answers questions and drafts code that the engineer pastes in. Agentic editing, inside the engineer's editor, plans a change across several files, runs the tests and revises its work while the engineer watches. And a **background agent** takes a task, works on it unattended in its own environment, and returns a pull request for a person to review. What changes at each step is who holds the loop. With completion, the engineer decides every line, and the tool only proposes. With a background agent, the agent makes hundreds of small decisions the engineer never sees, and the engineer meets the result as a reviewer meets a colleague's change.

Kim and Yegge describe the work in three loops of growing scale, an inner, a middle and an outer developer loop, reaching from a single working session out to the work of teams, each with its own practices for preventing, detecting and correcting mistakes. Controls belong at every scale: a checkpoint in the editor and a canary in production are the same idea at two loop sizes. The shift is visible in published evidence, too. METR's 2026 follow-up reported developers running several agents at once, often enough that per-task time tracking stopped working.

Aviation offers a useful comparison. Autopilots work in modes, and the pilot's job changes with the mode, from flying the aircraft to monitoring the system that flies it. Human-factors research has long recognized mode confusion, a pilot's mistaken belief about which mode is engaged, as a hazard in its own right, and cockpit design answers it by displaying the active mode at all times. The comparison carries over well: an engineer must always know what an agent is allowed to do on their behalf, and the tooling should make that visible. It breaks at certification. An autopilot's modes are few, specified and tested to a standard before any passenger boards, while an agent's behavior shifts with each model version and has no such specification, which is why the controls in the rest of this section sit around the agent instead of inside it.

#### Specs and context {#c5-specs-context}

A background agent knows only what it is given and what it can find. The engineer's first contribution to an agent's work is therefore written: a task specification, the repository's rules file, and the acceptance tests that define done. Each is an old artifact with a new reader: a ticket written carefully enough for a stranger to act on, the conventions a new team member would otherwise learn in review, and tests that say what done means. The Architecture book's Section 15.4 argued that ADRs (architecture decision records) become agent context; the artifacts here are the engineer's, one level down.

The evidence that context matters is young but real. DORA's AI Capabilities Model names "AI-accessible internal data" as a capability that "boosts AI's impact on individual effectiveness and code quality", a correlational survey finding. Google's migration papers document the context they supplied: the set of files to change, located with Kythe, and a prompt written for each change type. John Berryman and Albert Ziegler, in *Prompt Engineering for LLMs* (2024), describe how GitHub Copilot assembles context under a fixed token budget, choosing what to include because not everything fits. The practical consequence for an engineer is that a good spec is short and specific. It names the files, the rule, the tests that must stay green and the things the agent must not touch, because whatever the spec leaves out, the agent fills in with a guess.

Here is the spec Ines wrote for one shard of the barcode migration, the Fan Messaging team's:

```yaml
task: replace barcode event-prefix parsing with ticket identity lookup
shard: fan-messaging (repo: notifications, 6 call sites)
locate: callers of BarcodeLegacy.eventPrefix()   # list attached, from code index
change: |
  Replace each call with ticketIdentity.eventOf(ticket_id).
  Pass ticket_id from the message envelope; never derive it from the barcode.
must_stay_green: [characterization/barcode_prefix, contract/notifications-consumers]
do_not_touch: [tests/**, build files, retry or timeout settings, any public API]
size: one change per call site; no unrelated edits
done_when: all listed tests pass and each diff touches only the call site and imports
sponsor: ines (inventory)   owner_review: fan-messaging
```

Every line answers a question the agent would otherwise have answered for itself. The `do_not_touch` line was added after rung 3 of Figure 5.4 found nine changes with unrelated "improvements" in the first shards; later shards had none.

#### Scoping a task {#c5-scoping}

Which tasks should go to an agent at all? Osmani's advice on task selection and Kim and Yegge's "head chef" framing agree on the essentials, and Google's migrations show them in practice. Good first tasks are well specified, so the agent need not guess at intent; covered by tests the agent cannot change, so success can be checked by machinery; reversible, so a mistake costs a revert; and reviewable by an owner in minutes, so the human check is real. Kim and Yegge's delegation framework adds the right scaling rule: the more autonomy a task is given, the more verifiable it must be, so delegation should be matched to risk and to how easily the result can be checked.

The rule rules out more than it admits, and that is its value. The barcode migration qualified on every count. Designing the reissue path did not: its spec was the open question, its tests did not yet exist, and its mistakes would sell a ticket twice. Encore's engineers used assistants heavily on reissue, for explanation, test drafting and boilerplate, but no agent was ever handed the design. Encore's tier-1 code, as the Resilience book's Section 4.5{% include xref.html to="resilience:4.5" %} defines it, is where an agent's change gets the closest review, and it is also where an agent is least often given a whole task.

#### Guardrails in the dev loop {#c5-guardrails}

Agents cut corners. Kim and Yegge give the problem a chapter, titled "When Your Sous Chef Cuts Corners: Hijacking the Reward Function", and its catalog, under names such as "baby-counting" and "cardboard muffin", is sobering to anyone who has watched an agent work: output that looks finished and is not, and litter left behind in the codebase. The behavior follows from the setup. An agent is rewarded for reaching the state its instructions describe, and if it can reach that state more cheaply by changing the checks than by doing the work, some of the time it will.

The controls are each proven in other settings, and their application to coding agents is recent. On the engineer's own machine, five habits do most of the work. Each agent task runs on its own branch, so its changes can be thrown away whole. The agent works in a checkpointed environment, so any step can be undone. Tests that define done are locked from the agent, by file permissions locally and by code-owner rules in the repository. Diffs stay small, because a reviewer can hold only so much in mind. And the agent never holds production credentials. At Encore, agents obtain short-lived, scoped tokens through the platform's token exchange. DORA's 2025 work supports the first two habits directly: it found that "frequent use of rollback features boosts the performance of AI-assisted teams". The wider questions of agent identity, sandboxing and prompt injection belong to the Architecture book's Section 15.4{% include xref.html to="architecture:15.4" %} and the Resilience book's Section 8.5{% include xref.html to="resilience:8.5" %}; this section stops at the edge of the developer's own loop.

#### The human stays the owner {#c5-human-owner}

Every change an agent makes at Encore has a **sponsoring engineer**: the person who asked for the change, can explain every line of it, and answers for it after it merges. The term comes from the authorship policy in the Resilience book's Section 4.5{% include xref.html to="resilience:4.5" %}, which records the sponsor on every commit. Code ownership is long-standing practice; *Software Engineering at Google* describes owners files that make a named group responsible for, and the approver of, each part of the codebase. Google's migrations kept owner review on every change, even when 80% of the characters came from a model. The sponsor answers for the change as a whole, and each owner answers for the part of it that touches their code.

Civil engineering has a long-established version of this arrangement. Drawings for a structure may be prepared by many hands, but an engineer of record reviews them and puts a professional stamp on them, and that engineer answers for the design whoever drew it. The analogy holds for the accountability and breaks for the drafters. A human drafter is trained and learns from correction, and the engineer of record comes to know their habits. An agent's work varies with each model version and carries no memory of last week's correction, so the sponsor must review it as fresh work every time.

Encore's barcode migration shows what the role demands. Six of the seven owning teams approved their shards with small corrections. The seventh, Venue Entry, rejected its shard outright, and that was the most useful moment of the migration. The door-scanning app reads the event-code prefix offline, to reject a ticket for the wrong event without a network round-trip, because gates often lose connectivity when a crowd arrives. The agent's change replaced the offline read with a call to the identity lookup, which was exactly what the spec asked for and exactly wrong for a scanner. Every test passed, since the tests ran with a network. Venue Entry's owner saw the problem in minutes, because she knew why the code read the prefix. The fix was a design change, written by hand: the gate's offline data now carries the `ticket_id` values valid for each event, alongside the revocation lists the gates already hold. Ines updated the remaining specs to flag any call site on an offline path for human design first.

**Recap.** The shift from completion to background agents moves the engineer from writing to specifying and verifying. A short, specific spec, tests the agent cannot touch and a well-chosen task do most of the work; a branch per task, checkpoints, small diffs and no production credentials contain the rest. Every agent change has a sponsor who can explain it and owners who review the parts they own, and the owner's knowledge of why code exists is what no check supplies.

**Exercise 5.3.** Choose one task you would hand to a background agent. Write its spec in the shape of Ines's, with the files, the rule, the tests that must stay green, what it must not touch and the definition of done. Then list the owners who would review it, and say what each of them knows about the code that the spec does not.

### 5.4 Owning What a Machine Wrote

The Resilience book's Section 4.5 set Encore's policy for reviewing machine-written change, and Section 4.3 of this book describes code review; both are about the reviewer. This section is about the author, the engineer who asked for the code and will put their name on the change. Most of what the author owes is old, and generated code makes it more important.

#### Never merge what you cannot explain {#c5-explain}

Osmani's advice is to treat generated code as a pull request from "a fast, confident junior": someone who produces a great deal quickly, sounds sure of all of it, and is wrong in ways that do not announce themselves. It sets the right posture: nobody merges a junior colleague's change unread, and nobody assumes it is wrong either. The rule that follows is the oldest rule of authorship: never put your name to a change you cannot explain, line by line, to a colleague who asks.

Publishing has lived with a version of this for a long time. Many books are written partly or wholly by ghostwriters, and the author whose name is on the cover still answers for every sentence in them, to readers, to critics and sometimes to courts. The convention works because the named author has read the book and agreed to every claim in it. The analogy breaks in a way that strengthens the rule. A ghostwriter spends months in conversation with the author and absorbs what the author means. A model has no such conversation and keeps no memory of what it intended, so the only person who can supply the meaning of generated code is the engineer who accepted it, and a line that engineer cannot explain has no one to explain it.

At Encore the author's obligations before review are short enough to keep beside the keyboard, and the Resale team wrote them into its pull-request template:

```markdown
Before requesting review (author):
- [ ] I can explain every line of this diff without the assistant open
- [ ] I read every assertion in new or changed tests against the spec, not the code
- [ ] No test was weakened, skipped or deleted to make this pass
- [ ] Inputs crossing a trust boundary are validated; queries are parameterized
- [ ] No new dependency, or the new one passed the dependency gate
- [ ] Names and structure follow this module's conventions, not a generic pattern
- [ ] The diff contains only what the task needed
```

None of the items is new. Each was always the author's job, and each is now easier to skip, because the code arrived looking finished.

#### The majority problem {#c5-majority-problem}

Osmani names a subtler hazard the "majority problem". A model trained on a vast body of public code tends to produce the most common solution to a problem, and the most common solution is often not the right one for this codebase. Encore met it repeatedly. Asked to make a call to the identity lookup more robust, assistants wrapped it in a retry loop with its own backoff, as most code on the internet does. At Encore it is wrong: the service mesh already retries within a budget of about 10%, and a second retry layer multiplies the first and turns a burst of failures into a storm, the very failure that took Encore down years ago. The fitness function described in the Resilience book's Section 4.5{% include xref.html to="resilience:4.5" %} caught each instance, but only because someone had once turned that lesson into a check. Encore has many conventions that have never been turned into checks, and those are defended only by the engineers who happen to remember them.

The majority problem is a practitioner's observation, and it now has one rigorous quantitative counterpart. Hao He, Courtney Miller, Shyam Agarwal, Christian Kästner and Bogdan Vasilescu studied 806 open-source repositories on GitHub that adopted the Cursor AI editor, comparing them by difference-in-differences with 1,380 matched repositories that did not, in a paper presented at the Mining Software Repositories conference in 2026. In the first month after adoption, commits rose by 55.4% and lines added by 281.3%. The only significant gain in velocity fell within the first two months. Static-analysis warnings rose by about 30% and stayed up, and code complexity rose and stayed up as well; the authors find that this accumulation of warnings and complexity is a major factor in the slowdown that followed. The study is observational and its subjects are open-source projects, so it is emerging evidence, but its shape is the one Section 5.1 anticipated.

This is the architectural erosion the Architecture book's Section 15.4{% include xref.html to="architecture:15.4" %} warned of, accumulating at the rate machines generate code, and Section 2.1 of this book gives the design response, deep modules whose simple interfaces hide their complexity. Each plausible generated change that adds a shallow helper, duplicates a function that already exists or widens an interface a little is individually harmless. Their sum is a codebase that nobody designed, growing faster than the team can understand it.

#### Security in the author's chair {#c5-security}

Generated code carries known weakness patterns, and the people using it tend to trust it more than they should. Both rest on peer-reviewed studies of 2021–2022 models, and the date belongs beside their numbers. Hammond Pearce and colleagues, in "Asleep at the Keyboard?" (IEEE Symposium on Security and Privacy, 2022), prompted the Copilot of 2021 with 89 scenarios built around common weakness types, and of the 1,689 programs it produced, about 40% were vulnerable. Neil Perry, Megha Srivastava, Deepak Kumar and Dan Boneh (ACM Conference on Computer and Communications Security, 2023) gave 47 participants five security-related programming tasks, 33 of them with an AI assistant and 14 without. Those with the assistant wrote significantly less secure code and were more likely to believe their code was secure, with the largest effects on string encryption and SQL injection.

The second finding is the one that should change the author's habits. Over-trust belongs to the person using the tool, so better models will not cure it on their own. The author's defense is the security lines of the checklist above, applied with care where generated code most often goes wrong: input crossing a trust boundary, database queries, cryptography (which belongs in a vetted library), authorization checks that a generic solution omits, and secrets hard-coded for convenience. Assistants also sometimes suggest packages that do not exist, whose names attackers then register; that risk and the dependency gate belong to the Resilience book's Section 7.4{% include xref.html to="resilience:7.4" %}, and fleet-wide patching to its Section 7.3. The author's part is to notice that a dependency arrived with the code, and to send it through the gate.

#### Licensing and provenance {#c5-licensing}

The legal position of code produced by models trained on public code is unsettled. The controls, however, are real and cheap. GitHub Copilot offers a filter that hides suggestions of about 150 characters or more that match public code, and a code-referencing mode that shows the matching repositories and their licenses instead. GitHub's own research has reported such matches to be rare. In September 2023 Microsoft announced its Copilot Copyright Commitment, under which it defends paying commercial customers against copyright claims arising from Copilot output, on condition that they use the guardrails and filters built into the product. The condition is the important part for an engineering organization: the commitment protects only those who keep the filters on.

Encore's approved assistants therefore run on commercial terms, with the public-code filter enabled by policy. Authorship is recorded at commit time under the Resilience book's Section 4.5{% include xref.html to="resilience:4.5" %}, so the record exists if a question of origin ever arises, and new dependencies pass the curated gate of that book's Section 7.4, whoever suggested them.

#### Keeping the codebase legible {#c5-legible}

The last obligation is the least dramatic and probably the most important over a system's life. Generated code must be made into the team's own code: renamed to the module's vocabulary, restructured to its patterns, stripped of whatever the task did not need. Refactoring, in Martin Fowler's sense of small behavior-preserving changes, and tidying, in Kent Beck's, are the tools, and Section 2.2 teaches both. What generated code changes is their urgency. He and colleagues measured the cost of skipping this step in the persistent rise of warnings and complexity, and the cost compounds, because every later change, by a person or an agent, is made in the codebase as the last change left it.

At Encore the habit has a simple form. A change that arrives from an agent is tidied by its sponsor before it is offered for owner review, in a separate commit so that reviewers can see the agent's work and the human's adjustments apart. The cost is a few minutes per change, and the return is a codebase whose names keep meaning what the team thinks they mean.

**Recap.** The author of a generated change owes what any author owes: an explanation of every line, a reading of every assertion, a check of security and dependencies, and the work of making the code fit its module. Generated code arrives looking finished, which is why these obligations are easier to skip. Early velocity bought with unexamined complexity is repaid later, and tidying is how a team avoids the debt.

**Exercise 5.4.** Take one generated change you merged in the last month and explain every line of it to a colleague, without the assistant open. Mark each line you could not explain, and for each, say what you would have had to know to explain it.

### 5.5 Adopting It Across 40 Teams

#### Measuring impact honestly {#c5-measuring}

Encore's leadership asked its question in the plainest form: do the tools pay? The bill was visible. Assistant licenses cost about €45 an engineer a month, roughly €216,000 a year across 400 engineers, and agent compute, metered through the AI gateway, was growing each quarter. The value was not. The usage dashboard showed suggestions accepted and agent pull requests merged, and a working group of two engineers from the Developer Portal team and an analyst from the Experimentation team was asked to answer properly. Its first conclusion was that the dashboard could not.

Its reasons are the lessons of Section 5.1. Albert Ziegler and colleagues at GitHub found in 2022 that the rate at which shown suggestions are accepted predicts how productive developers feel better than measures of how much generated code survives. That makes acceptance a good measure of perceived productivity, and Section 5.1 showed that perception misleads in both directions. A before-and-after comparison fails too, because the quarter, the roadmap and the teams change at the same time. The design that works is the one Cui and colleagues used at three companies: randomize who gets the tool first, inside ordinary operations, and compare those who have it with those still waiting.

A **staggered randomized rollout** is a rollout in which groups receive a tool in an order chosen by chance, a period apart, so that the groups still waiting serve as the comparison for the groups already using it. Medicine uses the same design for health-service changes that cannot be withheld forever, where it is called a stepped-wedge trial: hospitals or clinics adopt the change in a random order, and by the end everyone has it. The comparison breaks in one respect. Hospitals are separate places, while teams share code, reviewers and people, so a team with agents changes the work of the teams around it. The working group accepted that contamination, which shrinks the measured differences, and said so.

Encore could not randomize what it already had: inline assistants were universal. So it randomized the next step, access to background agents. The 40 stream-aligned teams were drawn into four cohorts of ten, starting a quarter apart from month 3 of year nine, and the Resale team, formed at month 4, joined the second cohort. The metrics were those Sections 6.5 and 10.5 define, DORA's delivery metrics including rework rate, with review time per change and the developer-experience survey, and agent usage as context only. Following He and colleagues, the plan added quality lag indicators, warnings and complexity in changed code, watched for two quarters. The working group wrote the plan down before the first cohort began, so that nobody could choose the measures after seeing the results:

```markdown
# Pre-registration: background-agent rollout, year 9
Question:   Does agent access change delivery outcomes for a team?
Design:     40 teams in 4 cohorts of 10, random order, one quarter apart
Baseline:   the quarter before each cohort starts
Primary:    change failure rate; rework rate; lead time for changes
Secondary:  review time per change; static warnings and complexity in changed code;
            two DevEx survey items on AI-assisted work
Context:    agent PRs merged, acceptance rate (never a target, never a result)
Stop rule:  pause a cohort if its change failure rate exceeds the waiting
            cohorts' by more than 3 points for two consecutive months
Lag check:  quality indicators tracked two quarters past each cohort's start
Reporting:  distributions across teams; no team ranked, no individual measured
Decision:   expand, hold, or withdraw, with the evidence, at each cohort start
```

The first answer came at month 9, when the first cohort had two quarters of use and the later cohorts served as comparison. Merged changes per engineer were up about 10% in the first cohort, with an interval wide enough to include no change. Review time per change was up by about a fifth, mostly in the teams that reviewed other teams' code. Rework rate was flat, and change failure rate showed no difference the data could detect. Static warnings in changed code rose in six of the ten teams. It was the shape Section 5.1 predicts, an amplifier whose cost lands on reviewers, and it gave leadership a usable answer: keep going, fix the review load before the third cohort, and look again in two quarters. Figure 5.5 lays the rollout out in time.

{% include diagrams/fig-5-5.svg %}

*Figure 5.5 — Encore's staggered randomized rollout of background agents. Each cohort waits as comparison, takes its baseline quarter, then has its quality lag watched for two quarters; the first answer came at month 9.*

#### Skills and juniors {#c5-skills-juniors}

The field experiments found the largest gains for less experienced developers, which raises the next question: what happens to how juniors learn? One controlled study has looked. Judy Hanwen Shen and Alex Tamkin, at Anthropic, randomized 52 mostly junior engineers, all of whom had used Python weekly for more than a year, to learn Trio, an asynchronous Python library none of them knew, with or without an AI assistant. On a quiz shortly afterward, the AI group averaged 50% and the hand-coding group 67%, a substantial difference, and the gap was widest on debugging questions. The AI group finished about two minutes faster, a difference that was not statistically significant. Within the AI group, the way people used the assistant mattered: those who asked conceptual questions, or who generated code and then worked to understand it, scored 65% or more, while those who delegated the work scored below 40%. The subgroups were small and that part of the analysis was qualitative, the assistant was a chat sidebar with no agent capabilities, and the authors call the results preliminary. This is emerging evidence, and specific enough to act on.

The two findings fit together once we separate doing from learning. A junior with an assistant produces more, as Cui's experiments measured, and a junior who delegates to it learns less, as Shen and Tamkin measured. Both can be true of the same person in the same week. The tension is an old one, a version of the deskilling Lisanne Bainbridge described in "Ironies of Automation" (1983), which the Operations book's Section 3.3{% include xref.html to="operations:3.3" %} develops. Medicine manages a version of the same tension through supervised residency, in which a resident does real clinical work, under graduated supervision, with the explicit aim of becoming someone who can do it unsupervised. The analogy holds for the structure: the work is real, and so is the teaching. It breaks at the teacher. An attending physician knows what the resident is meant to learn and steers toward it, while an assistant optimizes for finishing the task in front of it, which is exactly the habit that cost Shen and Tamkin's delegators their learning.

Encore's onboarding now holds both findings at once. Theo joined the Resale team from a graduate program at month 4 and had to learn the seat ledger, Encore's only event-sourced service, from which Resale reads ticket ownership. He used an assistant throughout as the study's high scorers did, asking why the ledger rebuilds its projections as it does, then tracing each answer through the code and its tests. His onboarding buddy asked him once a week to explain a part of the ledger with no tools open. That is an illustration of the practice; the evidence for it is Shen and Tamkin's. The rule Encore took from it is that new engineers use assistants from their first week, explanation first, and that their onboarding checks understanding directly, by asking for explanations, since merged changes say little about it. Section 9.4 builds this into hiring and onboarding.

#### The capabilities that make it pay {#c5-capabilities}

DORA's AI Capabilities Model, published in September 2025, names seven capabilities associated with teams that gain from AI adoption without paying for it in other ways. It rests on survey correlations and 78 interviews, so it shows association and leaves cause unproven, and most of its list is the good engineering practice DORA has described for a decade. Figure 5.6 maps each capability to the place in this series that builds it.

| DORA AI capability | What it asks | Where it is built |
|---|---|---|
| Clear and communicated AI stance | everyone knows what is allowed, where | Section 5.5 (Policy) |
| Healthy data ecosystems | data that is trustworthy and findable | the Products book, Chapter 4; the Architecture book, Chapter 9 |
| AI-accessible internal data | assistants can read the docs, decisions and code they need | Section 5.3; Chapter 6 |
| Strong version control practices | frequent commits, easy rollback | Chapter 4 (Section 4.2) |
| Working in small batches | small changes, reviewed and shipped quickly | Chapter 4 (Sections 4.3 and 4.4); Chapter 10 |
| User-centric focus | work driven by what users need | the Products book, Chapters 1–3 |
| Quality internal platforms | paved paths that make the right way easy | Chapter 6 |

*Figure 5.6 — DORA's AI Capabilities Model, mapped to the chapters that build each capability. Most of the list is ordinary engineering capability, which is why the tools amplify what a team already is.*

One entry deserves its own sentence. On user-centric focus, DORA warns that without it "AI adoption can have a negative impact on team performance". A team that builds the wrong thing faster has gained nothing from the speed, which is the Products book's whole argument.

#### Policy {#c5-policy}

DORA's first capability is a clear and communicated AI stance, and DORA notes that it need not be any particular policy, only a clear one. Engineers unsure whether a tool is allowed either avoid it or use it quietly. Encore's stance fits on one page. It names the approved tools, all reached through the AI gateway. It sets data rules by class: fan personal data and partner confidential data never appear in prompts to any tool outside the gateway, and sales-velocity data, which Encore keeps from everyone, is never placed in an agent's context. It states that agents never hold production credentials, that every agent change has a sponsor, and that the review tiers of the Resilience book's Section 4.5{% include xref.html to="resilience:4.5" %} apply unchanged. And it says, in one sentence, that no engineer will be measured or ranked by how much they use the tools.

Below the stance sit shared conventions. Kim and Yegge argue for shared rules files and team standards for human–AI work, and the argument is sound: a convention written in the repository is read by every agent that touches it. Their supporting case studies, a pilot with about 700 developers at Adidas and a productivity program at Booking.com, are company-reported and should be read that way, and their claims of 10× productivity rest on personal anecdote. Encore keeps a rules file in each repository, owned by its team and reviewed like code, on a common base the platform supplies.

#### The platform's part {#c5-platform}

The platform turns the policy into paths. Encore's AI gateway, designed in the Architecture book's Section 15.4{% include xref.html to="architecture:15.4" %}, is the single route by which any approved tool reaches a model. Because every call passes through it, the gateway can enforce the data rules, attach the agent's scoped identity, and meter cost by team. Each team sees its own spend on its scorecard beside its delivery metrics, and leadership sees trends and distributions across teams, with no ranking, as for every other scorecard measure. Usage is shown as context for the outcomes and never as a target, for the reasons Section 10.5 gives. Chapter 6 builds this platform as a product.

**Recap.** Adoption is measured honestly by randomizing who gets the next tool and comparing outcomes, with the measures written down in advance and the quality lag watched for two quarters. Juniors gain output and can lose learning, so onboarding must check understanding directly. The capabilities that make the tools pay are mostly the old ones, and a clear stance, shared conventions and a platform that meters without ranking turn adoption into practice.

**Exercise 5.5.** Draft a one-page measurement plan for adopting one AI tool in your organization, in the shape of Encore's pre-registration: the question, the comparison group and how it is chosen, the baseline, three outcome metrics, the stopping rule, and the result that would make you withdraw the tool.

### Kata: The Promise to the Board

> **Your brief: "Fieldnote."** Fieldnote sells farm-management software as a service to about 30,000 farms and 2,000 agronomists in five EU countries: field records, crop plans and the reports farms file to claim agricultural subsidies. It has 150 engineers in 18 teams. Its subsidy-reporting module dates from the company's first year, is understood by two engineers, and changes every season with the reporting rules. Spring is the busy season, when farms enter a year's records in six weeks and a release freeze holds. Engineers have used inline assistants for two years without anyone measuring them. In January the chief executive bought background-agent licenses for every engineer, at €70 a month each, and announced to the board that engineering would deliver "2× by Q3". Change failure rate has been 9% for a year. Review time per change has doubled since the autumn, and two senior engineers say they now spend most of their week reviewing. Six graduates join in March.

**Deliverables:**

1. **Adoption design** — A staggered, randomized two-quarter rollout across the 18 teams, with the baseline, and how you will handle the spring freeze and teams that share code.
2. **Pre-registration** — The measurement plan on one page, written before the first cohort starts: primary and secondary metrics, the role of usage data, the quality lag indicators and the stopping rule.
3. **Delegation map** — Fieldnote's kinds of work sorted by verifiability and reversibility: what goes to an agent, what gets assistance only, and where the subsidy-reporting module falls.
4. **Author and agent rules** — The spec template for agent tasks, the guardrails on engineers' machines, and the author's checklist, sized for Fieldnote's own teams.
5. **Graduate onboarding** — How the six graduates will use assistants from week one and still build the understanding they will need as reviewers.
6. **The flat-result memo** — The one page you will send the chief executive if, at the end of Q3, the numbers show no clear change in delivery, and what you will recommend.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Honest comparison | Would your design separate the agents' effect from the season, the roadmap and eager adopters? |
| Measures chosen in advance | Could anyone accuse you of choosing your metrics after seeing the results? |
| Stability in view | Does your plan watch change failure rate, rework and the quality lag as closely as it watches throughput? |
| Delegation by verifiability | Can a machine check, and an owner review in minutes, every task you hand to an agent? |
| Learning protected | Will the graduates be able to debug the subsidy module in a year, or only to prompt for changes to it? |
| Candor upward | Does the memo tell the chief executive what the evidence says, including that "2×" was never a measured promise? |

#### Where you now stand

You can now read each study on AI assistance for what it measured, and explain why careful studies disagree without any of them being wrong. You can say where assistance pays and where it does not yet, hand a task to an agent with a spec that leaves little to guess, and own what it produces as its author. And you can tell an organization whether its tools pay, by randomizing the next step and writing down the measures before the results arrive. One conclusion kept returning: the tools amplify whatever engineering system surrounds them, and the parts of that system that 40 teams share are built by a platform. Chapter 6 turns to that platform, and to building it as a product whose customers are the engineers themselves.

### References

- Kevin Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng, Tobias Salz — [*The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers*](https://doi.org/10.1287/mnsc.2025.00535). Management Science, published online 27 February 2026 (working paper 2024).
- Joel Becker, Nate Rush, Elizabeth Barnes, David Rein — [*Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). METR, 2025 (arXiv:2507.09089); with METR's [*uplift update*](https://metr.org/blog/2026-02-24-uplift-update/), February 2026, and [*self-reported impact survey*](https://metr.org/blog/2026-05-11-ai-usage-survey/), May 2026 — free online.
- DORA — [*State of AI-assisted Software Development 2025*](https://dora.dev/research/2025/dora-report/), with the [*DORA AI Capabilities Model*](https://dora.dev/ai/capabilities-model/report/). Google Cloud, 2025 — free online.
- DORA — [*Accelerate State of DevOps Report 2024*](https://dora.dev/research/2024/dora-report/). Google Cloud, 2024 — free online.
- Sida Peng, Eirini Kalliamvakou, Peter Cihon, Mert Demirer — [*The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*](https://arxiv.org/abs/2302.06590). arXiv:2302.06590, 2023 — free online.
- Elise Paradis et al. — [*How Much Does AI Impact Development Speed? An Enterprise-Based Randomized Controlled Trial*](https://arxiv.org/abs/2410.12944). ICSE-SEIP 2025, pp. 618–629 — free online.
- Stoyan Nikolov et al. — [*How is Google Using AI for Internal Code Migrations?*](https://arxiv.org/abs/2501.06972). ICSE-SEIP 2025, pp. 481–492; with Celal Ziftci et al. — [*Migrating Code At Scale With LLMs At Google*](https://arxiv.org/abs/2504.09691). FSE 2025 Companion, pp. 162–173 — free online.
- Hao He, Courtney Miller, Shyam Agarwal, Christian Kästner, Bogdan Vasilescu — [*Speed at the Cost of Quality: How Cursor AI Increases Short-Term Velocity and Long-Term Complexity in Open-Source Projects*](https://arxiv.org/abs/2511.04427). MSR 2026 — free online.
- Judy Hanwen Shen, Alex Tamkin — [*How AI Impacts Skill Formation*](https://arxiv.org/abs/2601.20245). arXiv:2601.20245, 2026; Anthropic research post, January 2026 — free online.
- Grace Murray Hopper — [*The Education of a Computer*](https://cs-web.bu.edu/courses/cs112/files/binary_logic/hopper_full.pdf). Proceedings of the ACM National Meeting, Pittsburgh, 1952, pp. 243–249; reprinted in Annals of the History of Computing 9(3/4), 1988 — free online.
- John Backus — [*Programming in America in the 1950s — Some Personal Impressions*](https://www.softwarepreservation.org/projects/FORTRAN/paper/Backus-ProgrammingInAmerica-1976.pdf). In Metropolis, Howlett & Rota (eds.), *A History of Computing in the Twentieth Century*, Academic Press, 1980, pp. 125–135 — free online.
- Neil Perry, Megha Srivastava, Deepak Kumar, Dan Boneh — [*Do Users Write More Insecure Code with AI Assistants?*](https://arxiv.org/abs/2211.03622). ACM CCS 2023, pp. 2785–2799; with Hammond Pearce et al. — [*Asleep at the Keyboard?*](https://arxiv.org/abs/2108.09293). IEEE S&P 2022, pp. 754–768 — free online.
- Albert Ziegler et al. — [*Productivity Assessment of Neural Code Completion*](https://arxiv.org/abs/2205.06537). MAPS '22, pp. 21–29 — free online.
- Addy Osmani — [*Beyond Vibe Coding*](https://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749/). O'Reilly, 2025.
- Gene Kim, Steve Yegge — [*Vibe Coding*](https://itrevolution.com/product/vibe-coding-book/). IT Revolution, 2025.
- Lisanne Bainbridge — [*Ironies of Automation*](https://doi.org/10.1016/0005-1098%2883%2990046-8). Automatica 19(6): 775–779, 1983.

---

## Chapter 6: The Internal Platform as a Product — Paths, Adoption, and Developer Experience {#ch6}

> "Get users on the system quickly, work with them closely, and let their needs and problems drive the design." — T. A. Dolotta, R. C. Haight and J. R. Mashey, 1978

Every software company of any size ends up building a second product whose customers are on its own payroll. The product is the collection of templates, pipelines, credentials, runtimes and documents through which its engineers turn an idea into a running service, and the customers are those engineers. Chapter 1 called this the system that builds the system. This chapter asks how that product should be built: how to learn what its customers need, how to build the smallest thing that meets the need, how to persuade 40 teams to use it and move off what they had before, and how to know whether any of it made their work better. These are product questions, and the uncomfortable discovery of the last decade is that most internal platforms were never asked them. They were built as infrastructure and announced as policy, and many of them stand half-used, a portal with a fine front page and a small fraction of the company behind it.

The Architecture book has already argued why a company at Encore's scale needs a platform and what one contains, and the Resilience book{% include xref.html to="resilience" %} has argued how a platform is run. We will not argue either again. What neither book could show, because both were about the platform as a thing, is the method by which a platform group finds its next piece of work and gets it adopted. That method has a surprisingly long history. Its clearest early instance is a machine at Bell Labs in the 1970s that served a thousand programmers whose real targets were other computers, and whose builders wrote down how they ran it in words that read today like a platform team's charter.

Encore's platform group has nine teams and 40 people, about a tenth of engineering, and early in year nine it did something it had never done before: it hired a product manager and began interviewing its users. Verified Resale is the first large new service to be built since then, and the Resale team's journey from an empty repository to its first production deploy became the group's first serious piece of research. The Resale service was created from the template on its first day, yet its first production deploy took 23 working days, and 15 of them were spent waiting. That wait is why the platform group built the two roads it showed to be missing: a way to issue partner credentials without a ticket, and a shared way to deliver webhooks to partners, which three teams had each built for themselves. This chapter follows the platform group as it builds both, migrates the three home-grown senders onto the shared one, and measures whether the next partner-facing service ships faster.

### 6.1 Why Platforms, Again

#### The Programmer's Workbench {#c6-programmers-workbench}

In 1973 UNIX was still a small research system in Bell Labs' Computing Science Research Center, running on a handful of PDP-11 minicomputers. Elsewhere in Bell Labs, much larger groups of programmers wrote the business software that ran the Bell System, and that software did not run on PDP-11s at all. It ran on big batch machines. The installation that later became famous served programmers whose targets were two IBM 370/168s, two UNIVAC 1100-series systems and an XDS Sigma 5, each with its own job-control language, editors and habits. A programmer working for one of those machines wrote code on it, submitted jobs to it and waited for it, and carried around decks of punched cards in the meantime. Evan Ivie suggested, in the middle of 1973, a different arrangement: as much of the development as possible should be done on a computer dedicated to that task, and only the finished work sent to the target. Rudd Canaday, one of the designers of the original UNIX file system, led the department that built it, and the first PDP-11/45 was installed late that year. They called it the Programmer's Workbench, or PWB.

The workbench was a collection of small tools aimed at the friction of a programmer's day. A Remote Job Entry subsystem sent jobs from the workbench to the target machines and brought their output back. John Mashey wrote the PWB shell, which came before the Bourne shell, and Dick Haight wrote `find`, `cpio` and `expr`. Marc Rochkind's Source Code Control System (SCCS), the first version-control system to run on UNIX, became one of its tools: Rochkind had begun SCCS in 1972 on an IBM System/370 and rewrote it in C for UNIX in 1973, and it first shipped publicly with the workbench. PWB/UNIX 1.0 was released on 1 July 1977, and much of it later flowed into the UNIX that the rest of the industry used. Ivie described the principle in *Communications of the ACM* that October, and in 1978 Ted Dolotta, Haight and Mashey described the system and how it had been run in the *Bell System Technical Journal*. Figure 6.1 draws the arrangement and its dates.

{% include diagrams/fig-6-1.svg %}

*Figure 6.1 — The Programmer's Workbench as a schematic: programmers on machines dedicated to development, small tools on top, and Remote Job Entry carrying finished work to the batch machines that had once received their card decks.*

That second paper is the reason PWB belongs at the head of this chapter. Its authors set out their approach in a handful of sentences. Get users on the system quickly, work with them closely, and let their needs and problems drive the design. They "forcefully nurtured a close, continuing dialogue" with their users. They chose to follow the UNIX habit of building small, independent tools rather than large, interrelated ones, and they changed UNIX itself only "after much deliberation, and only when major gains can be made." That last rule is a limit the team placed on its own surface, which is what the Resilience book means by thinness. The users, the paper records, were at first "a bit wary of what then seemed like a radical idea." Then "as word about the system spread, demand for service grew rapidly, almost always outrunning the supply." By the end of 1977 the main installation ran seven PDP-11s for about 1,100 people, which the authors called the largest known UNIX installation in the world, and most of those users had "thrown away their decks of cards."

One phrase in the paper seems at first to argue against this chapter's title. The team aimed "to provide to our users tools, rather than products." Read in context, the contrast is between small composable tools and large packaged systems that do everything one way, and the team's practice was exactly what we now call treating a platform as a product: users as customers, their problems as the backlog, their continued use as the test. We should also be careful about what the sources do not say. Nothing in them tells us whether Bell Labs' programmers were free to ignore the workbench, and it would be easy to retell PWB as a platform nobody mandated. What the paper does record is pull: demand outran supply, and the authors credited the system's qualities with making users "want to use our system." That is the measure this chapter will apply to every capability Encore builds. A platform succeeds when the people it serves come to it because their day is easier there, and the work of building it consists mostly of finding out what would make their day easier.

#### What is already settled {#c6-already-settled}

A good deal of the ground has been covered, in this book and in the others, and it saves pages to say where. Figure 6.2 is the map. Each row is an idea this chapter will use without arguing for it again, with the place where it is argued and the team at Encore that owns the corresponding machinery today.

| Settled idea | Where it is argued | Owner at Encore |
|---|---|---|
| Cognitive load as the resource a platform saves; the platform as a product; the thinnest viable platform; desire paths | Architecture book, Section 15.1 | Platform group lead and product manager |
| Golden-path anatomy: template, provisioning workflow, registry entry, scorecard | Architecture book, Section 15.2 | Developer Portal |
| Governance as code; the priced, logged, owned and time-boxed exception path | Architecture book, Section 15.3 | Developer Portal |
| Agents as tenants of the platform | Architecture book, Section 15.4 | AI Platform |
| Platform strategy, money and the message to leadership | Architecture book, Section 15.5 | Platform group lead |
| Reconciliation loops and GitOps | Resilience book, Sections 3.1 and 3.4 | Runtime |
| Thinness as an operating virtue; platform on-call and SLOs; the first three migrations done by hand | Resilience book, Section 3.5 | Reliability, with each plane's team |
| Large-scale changes, Hyrum's Law and the mechanics of deprecation | Section 2.5 | Every code owner |
| The pipeline as a product | Section 4.4 | Developer Portal (pipelines and templates); Runtime (deployment) |

*Figure 6.2 — What this chapter assumes, where it is argued, and who at Encore owns it.*

What remains is the method. The Architecture book says a platform must be built as a product and must win its users; it does not, for reasons of space, show how a platform group discovers what to build, writes it down, builds it so it stays current, gets it adopted, retires what it replaces and measures the result. That is this chapter's work.

#### The platform paradox {#c6-platform-paradox}

A platform speeds teams up by taking choices away from them, and this is less of a contradiction than it sounds. Gregor Hohpe, in *Platform Strategy* (2024), states it as a dichotomy that platforms dissolve: "Platforms break through the perceived dichotomy between harmonization and innovation." A team that need not choose a database, a broker, a deployment tool and a signing scheme for each new service has more attention left for the thing it was formed to build. One of the section headings in that chapter makes the point with paper: A4 does not stifle creativity. The German standard DIN 476 fixed the A series of paper sizes in 1922, and a century of writers, printers and office-equipment makers has built freely on top of it, precisely because nobody has to negotiate the size of a sheet any more.

The practical question is which choices to remove. Camille Fournier and Ian Nowland, in *Platform Engineering* (2024), frame it as limiting primitives while minimizing overhead: a platform should narrow the set of building blocks teams assemble services from, without adding so much process around those blocks that teams route around it. A large music festival offers a working picture. Most festivals provide a shared backline, the drum kit, amplifiers and keyboards that stay on stage all weekend, so that one band can follow another after a changeover of minutes. A band that insists on its own amplifier may bring it, with notice and at its own cost. The shared backline is why a festival can put 12 acts on one stage in a day, and nobody thinks the bands less creative for using it. The picture breaks where software's time scales differ. The backline serves for one weekend and goes back to the rental company. A platform's primitives stay in service for years, and every service built on them inherits their limits for as long as it lives, so the choice of what to standardize carries much more weight than a festival's choice of drum kit.

Encore's rule is written down and short. New services choose from one managed relational database family and publish events on the existing event backbone. The rule applies to new services only. Seat Inventory's event-sourced store predates it and sits in the exception ledger as a recorded, permanent exception with a named owner, as the Architecture book's Section 15.3{% include xref.html to="architecture:15.3" %} requires, and any other team that needs something different may leave the road on the same terms. The rule's rationale is recorded beside it: two families of database and two brokers would double what the Runtime and Event Backbone teams must patch, upgrade and support at three in the morning, and nothing Encore's teams have asked for in three years needed a second of either.

#### Platform or service desk? {#c6-platform-or-service-desk}

Not everything a platform group offers is a platform. Hohpe's sharpest chapter title puts it as "IT Platform and IT Services Are Antonyms", and his test is self-service: "Self-service is the default mechanism through which IT platforms assure low friction," and "instead of filing a ticket, teams directly provision a virtual machine." A capability that a team can use only by asking a person is a service desk, however good the people at the desk may be. The distinction has evidence behind it. DORA's (DevOps Research and Assessment) *Accelerate State of DevOps Report 2024* measured developer independence, defined as developers' ability to perform their tasks for the entire application lifecycle without relying on an enabling team, and found a 5% improvement in productivity where platform users could complete their tasks without involving one.

The method that follows from the test is unglamorous. Take a quarter's worth of the requests that reached the platform group, by ticket, chat message or email, and classify them by kind. The Operations book's Section 3.1 measured toil in the same spirit; here the aim is narrower. Each kind of request that recurs is a candidate for a self-service interface, and the counts say which candidates matter. Encore's platform group ran this audit over the quarter before the Resale team formed. About 1,100 requests had arrived. The most common kind was a grant of database access, the second was setting up a new repository and pipeline by hand where the template did not fit, and the third was partner credentials. Since the Rowmate key leak told in the Resilience book's Section 7.2{% include xref.html to="resilience:7.2" %}, every partner client has used 15-minute tokens bound to a client certificate, and every such client identity was being issued by a person on the Security Engineering team in answer to a ticket. The security model had improved; obtaining an identity under it still meant waiting for a person.

The audit taught the group something else, about its own front door. Requests arrived through four channels, and some never arrived at all, because teams had stopped asking. DORA 2024 found that the commonest ways platform teams hear from users are informal conversations and issue trackers, and that not collecting feedback at all hurts. So the group gave itself a single public request channel, a published response target for each kind of request, weekly office hours and a support rotation, which is ordinary service practice and is what makes the next audit's data worth counting.

#### Swamps and shadow platforms {#c6-shadow-platforms}

Fournier and Nowland give a name to the condition a platform exists to prevent: the over-general swamp. It arrives in two steps. First the choice of building blocks explodes, as every cloud provider and open-source project offers another way to do each thing. Then the operational demands on each service rise, for security, observability and compliance. Product teams end up writing and maintaining a great deal of glue between the blocks they chose and the demands they must meet, and each team's glue is a little different. The swamp is a form of accidental complexity in the sense the Architecture book borrows from Brooks, multiplied by the number of teams.

Where the platform is missing, teams build their own, and these shadow platforms are the best evidence a platform group has of unmet need. Fournier and Nowland give the management of shadow platforms a section of its own; the useful stance is to treat each one as a finding rather than a transgression, and then to decide deliberately whether to adopt it as the platform's own, absorb its users into something better, or leave it alone because it serves one team well. Chapter 1 recorded the finding that started this chapter: Encore's developer survey named three home-grown webhook senders. Partner APIs sent inventory and listing events to partners, Venue Integrations sent sales events to venues' own systems, and Billing & Payouts sent payout notices to organizers' finance tools. Each signed its payloads differently, each retried on its own schedule, and one did not retry at all. All three worked. None was anyone's job to improve, and every partner integrating with Encore had to learn three dialects.

#### A capability's life {#c6-capability-life}

A capability's relation to its users changes as it matures, and the platform group plans that change on purpose. The interaction modes of *Team Topologies* (collaboration, X-as-a-Service and facilitating) belong to team design, and Section 9.2 treats them there; for a platform capability they read as a life cycle. A new capability starts in collaboration with the first team that needs it, because nobody yet knows its right shape, and moves to a self-service interface once the shape settles. Encore's Security Engineering team and the Resale team collaborated on partner credentials for one quarter, from the Resale team's formation in month 4, and agreed at the outset on the date when the collaboration would end and the self-service interface would become the only way in: the first day of month 8. Fixing the date in advance protected both sides. Without it, collaboration tends to persist because it is pleasant, and the platform team becomes a permanent extension of its first customer.

**Recap.** The Programmer's Workbench shows that the method is old: a dedicated machine for developers, small tools aimed at daily friction, a close conversation with users, and growth by demand. A platform narrows its users' choices to speed them up, so the decisions about what to standardize, and the open exceptions to it, deserve to be written down. A capability is a platform only if teams can use it without asking someone, and both the requests that still reach the platform group and the shadow platforms teams build for themselves show where it falls short.

**Exercise 6.1.** Classify the last 50 requests your platform or operations team received, by kind. Which kind would you turn into a self-service interface first, and why that one? If it is not the most frequent kind, say what made it outrank the others.

### 6.2 Discovering What Developers Need

#### Interviewing colleagues {#c6-interviewing-colleagues}

Developers are users, and the established way to learn what users need is to ask them about what actually happened. The Products book's Section 3.1 teaches story-based interviewing in full, following Teresa Torres's *Continuous Discovery Habits* (2021): ask about a specific recent episode, follow it step by step, and listen for where it went wrong, because people describe their past behavior far more accurately than they predict their future wishes. A developer asked what the platform should build next will name a tool they read about last week. A developer asked to walk through the last time they set up a new service will name the three days they spent waiting for a firewall rule, often without realizing it is the answer.

Interviewing colleagues differs from interviewing customers in two ways, and both help. The interviewer and the interviewee share an employer, so politeness runs in both directions: an engineer may soften a complaint about a team they will need favors from next quarter. And the interviewer can check what they hear. A customer's account of their week cannot be compared with their keyboard, but a developer's account of their last deploy can be compared with the repository history, the pipeline logs and the ticket timestamps. Encore's platform group does exactly that after each interview, and the comparison is often more revealing than the interview itself: people remember the wait that annoyed them and forget the one they had grown used to.

Someone has to own this work, and it is not naturally anyone's. Fournier and Nowland describe four pillars of platform engineering, product, development, breadth and operations, and product is the pillar a group of infrastructure engineers is least likely to staff by instinct. Encore's group hired its first product manager, Hana, in month 2, two months after the Verified Resale memo. In her first six weeks she and a tech lead from the Developer Portal team interviewed five teams about the last new service each had built, and the Resale team, then forming, became the sixth, interviewed as its journey happened.

#### Mapping the journey {#c6-mapping-journey}

Interviews produce stories, and to compare stories the group needs a map. Section 1.1 introduced the method, value-stream mapping, which grew out of Toyota's material-and-information-flow diagrams and makes waiting visible as a quantity. It transfers to software with little change, because a change moving toward production is, like a part moving through a factory, mostly waiting.

A developer journey map works best when it follows one journey at a time, such as from idea to first production deploy for a new service, and marks every handoff. Figure 6.3 is the map of the Resale team's first deploy, built from the interviews and checked against timestamps. Read the shaded bars first.

{% include diagrams/fig-6-3.svg %}

*Figure 6.3 — The Resale team's journey to its first production deploy. Two-thirds of the 23 working days were waiting, nine for partner credentials and six for a security review of a sender the team should not have had to write; all of it was for two capabilities the platform did not offer.*

The map changes the conversation. Before it, the Resale team's complaint was that "getting started is slow", which is true of every new service at every company and suggests no particular remedy. After it, the complaint has a shape: nine days spent waiting for credentials, and six waiting for a review of code the team should never have had to write. The fourth webhook sender is the more telling of the two. The Resale team was not careless in writing it; there was simply nowhere else to go, so it copied the nearest one and inherited that sender's quirks along with its code.

Once several journeys are mapped, the frictions they share can be ranked. Encore ranks them by working days lost multiplied by the number of teams affected in the last two quarters. That rule is Encore's own heuristic, with no validation behind it, and it has a known blind spot: a friction that strikes rarely but badly, such as a migration that blocks a team for a month once a year, scores lower than its pain deserves. The group therefore reads the ranking as the start of a discussion, and keeps a short list of rare, severe frictions beside it.

#### Desire paths as data {#c6-desire-paths-data}

The Architecture book's Section 15.1 introduced desire paths as a metaphor, and noted where it breaks: grass records footsteps without being asked, and a platform team has to go looking. Here is how to look. Most organizations already have three instruments that can show where teams have worn their own tracks.

The first is code search. Copied pipeline definitions, vendored scripts and near-identical helper modules show up as clusters of similar text across repositories, and each cluster is a workaround someone found worth copying. The second is the dependency graph: when three internal libraries do the same job and each has its own set of importers, the duplication is visible without reading any code. The third is the wiki's own analytics. The pages everyone bookmarks, and the ones edited most often by people outside the team that wrote them, mark the places where a document is doing the work a tool should do. None of these instruments has published evidence of its yield behind it; they are technique, and their findings still need an interview to say why the track was worn.

Encore found its webhook senders the simple way. Every webhook from Encore carries a signature header, `X-Encore-Signature`, so that receivers can check where the call came from, and a code search for the header's name returned the three senders, the Resale team's new fourth, and one more surprise: a fifth caller, which Section 6.4 will meet. Spotify has published a larger version of the same technique. In a 2026 post on dataset migrations, its engineers describe using lineage data in Backstage together with code search to find which repositories needed a change, before handing those repositories to Fleetshift, its tool for running a change across many repositories as automated pull requests.

#### The thinnest increment {#c6-thinnest-increment}

Discovery always finds more than a platform group can build, so the next step is to choose, and the thinnest viable platform of *Team Topologies* is the principle. A platform group should build the smallest thing that removes real pain, and only then the next. Encore scores each candidate on four questions: how many teams it affects, how much time it saves them, what risk it removes or adds, and what it costs to build and run. The scoring is Encore's own rubric. It is deliberately crude, because its job is to make the group argue about the same four things, and a number to the decimal place would add nothing to that argument.

Before building anything that scores well, the group asks one more question, borrowed from Simon Wardley's mapping: how evolved is this capability in the industry? The Architecture book's Chapter 13 places capabilities on Wardley's evolution axis, from genesis through custom-built and product to commodity, and the rule that follows is to adopt or buy what has become a product or commodity and build only what is particular to the business. Certificate authorities and token exchange are commodities, and Encore buys and adopts them. What is particular to Encore is the policy: which scopes a partner may hold, how its identity is bound to its contract, how quickly it can be revoked. That is what the platform group builds.

The rubric chose two increments in the first half of year nine: self-service partner credentials and shared webhook delivery. The loudest request in the same period, a new visual theme for the internal portal with a dark mode, scored near the bottom. It affected every team and saved none of them a minute. The group published the ranking with its reasons, which turned out to matter as much as the choice, because the teams who had asked for the theme could see that their request had been weighed.

There is published testimony that this order of work is the one that succeeds. In 2023 Helen Greul, Spotify's head of engineering for Backstage, told *The New Stack* that among organizations that had installed Backstage, "the average Backstage adoption rate is stuck at 10%." Her explanation was that adopters "fail to understand the challenges developers are facing and build the thinnest viable platform around solving those first." It is practitioner testimony and not a study, but it comes from the people with the widest view of internal portals, and it describes a failure that Encore's audit had just shown it how to avoid.

#### The path brief {#c6-path-brief}

Before a line of a new path is built, Encore writes it a one-page brief. The format is borrowed from product discipline: it is a cousin of the briefs in the Products book{% include xref.html to="products" %} and of the pitches in Basecamp's Shape Up, cut down to what a platform needs. It names the user, the job the path does for them, what "done" means, what is out of scope, and how adoption will be measured.

The term "golden path" has a history worth knowing before writing one. Spotify's engineers described their golden paths in 2020 as "the 'opinionated and supported' path to 'build something'", and they built them to cure what they called "rumour-driven development", a fragmented ecosystem in which engineers learned how to build things by asking whoever sat nearby. Spotify's first golden paths were tutorials: one per engineering discipline, seven at the time, each owned by the teams of that discipline. The first began as a Hack Week project. So the original golden path was a document before it was a template, and that is a useful corrective to read beside the Architecture book's four-part anatomy. A path is first an opinion about how something should be built, written down and supported. Templates, workflows and scorecards come later, as ways of making the opinion cheap to follow.

Encore's brief for its partner-facing path reads as follows.

```text
Path: partner-facing service                 Owner: Web & API Paths, Security Engineering
User: a stream-aligned team whose service is called by, or calls, a partner
Job: from `exposure: partner` in the manifest to a first production call
     with a partner's sandbox, without opening a ticket
Done when: credentials and webhook delivery are self-service; docs and
     sample code are in the template; the first two teams have shipped on it
Out of scope: partner onboarding and certification (Partner APIs);
     the public API's style rules (Public API); new signing algorithms
Adoption measure: share of `exposure: partner` services on the path,
     six months after each first deploy
Outcome measure: working days from repository creation to first
     production deploy, for new partner-facing services
```

The brief's most useful line is the one about scope. Each item in it is something a team will ask for in the first month, and the brief records in advance that the answer is "not on this path", along with who owns the question instead.

**Recap.** Interview developers about recent concrete episodes and check what they say against repositories and logs. Map one journey at a time with value stream mapping, so that waiting becomes a number, and rank frictions knowing the ranking's blind spots. Code search, dependency graphs and wiki analytics show where teams have built their own tracks. Choose the thinnest increment, build only what is particular to the business, and write each path a one-page brief before building it.

**Exercise 6.2.** Map one developer journey in your organization from idea to first production deploy, recording for each step its working days, its waiting and what the wait was for, as Figure 6.3 does, and checking each step against timestamps. Mark the three longest waits and say which of them a self-service interface could remove.

### 6.3 Building the Platform

#### The manifest as an API {#c6-manifest-api}

A platform needs to know what each service is before it can do anything for it. The Architecture book's Section 15.2 described the registry entry; the next step is to treat the file that feeds the registry as the platform's main interface. A **service manifest** is a declarative file kept in each service's repository that records what the platform needs to know about the service: its owner, its tier, its dependencies, how it is exposed and what classes of data it holds. The idea is widely practised. Backstage's catalog descriptor, `catalog-info.yaml`, records a component's owner, life cycle, system and dependencies, and Score, a platform-agnostic workload specification, was accepted as a sandbox project of the Cloud Native Computing Foundation (CNCF) in July 2024.

Encore goes one step further than recording. Its platform reads each manifest and acts on it: the registry entry, the catalog page, the alert rules, the access policies and the provisioning requests are all rendered from the manifest and reconciled continuously, by the kind of loop the Resilience book's Section 3.1{% include xref.html to="resilience:3.1" %} describes. Few companies go this far, and it is Encore's choice. Its cost is that the manifest's schema becomes the most depended-on interface Encore has, read by every platform capability and written by every team. For Verified Resale, the schema gained one value, `exposure: partner`, and that value is what switches on the two new capabilities.

```yaml
# service.yaml — read by the platform; edits go through review like code
schema: encore.service/v4
name: resale
owner: team-resale
tier: 1                       # purchase-path tier: on-sale freeze applies
exposure: partner             # internal | partner | public
dependsOn: [seat-inventory, orders, bot-screening]
data: [fan-pii, payment-reference]
partner:
  scopes: [listings:read, resale:write]
  webhooks:
    events: [resale_listing_created, resale_ticket_reissued]
    retry: {profile: standard}  # per-partner overrides allowed
```

Because the manifest is an interface, Encore governs its schema the way the Architecture book's Section 7.2{% include xref.html to="architecture:7.2" %} governs a public API, turned inward. Fields may be added, and an existing field's meaning does not change. A new optional field is a minor version, and a removed or renamed one is a major version with a migration and a date. The platform reads at least two major versions at once, so that teams can move in their own sprint. And the schema has a changelog, because the people who read it are the same ones who will be surprised if it changes without one.

#### Templates that keep up {#c6-templates-keep-up}

A template that generates a new service once, and then forgets it, starts to go out of date the day after it is used. The pipeline it produced, the base image it pinned, the alert rules and the logging setup all stay as they were, while the platform moves on. A year later the company has a hundred services, each frozen at the version of the template that happened to be current when its team began, and every improvement to the template reaches only the services not yet written. This drift is the platform's view of the version skew that Section 2.5 deals with in code.

It matters which tools can fix this, because some popular ones cannot. Backstage's software templates are scaffolders: they run once, on demand, and changing a template does not touch any component it already created. Two other approaches can carry a newer template into an existing repository. Copier records the answers given when a project was generated, in a `.copier-answers.yml` file, and `copier update` re-applies a newer tagged version of the template using those answers, surfacing merge conflicts where the project has diverged; cruft does the same for cookiecutter templates. The second approach works at fleet scale: dependency bots such as Renovate and Dependabot, and change runners such as Spotify's Fleetshift, open automated pull requests across many repositories at once.

Encore uses both. Its templates are versioned and published with changelogs, and a bot opens an update pull request in each repository when a new template version is released. The platform group watches one number, the count of services more than two template versions behind. When it first measured that number, in year nine, it was 74. The count is a measure of the platform's own work, and it says nothing against the teams whose services lag: a pull request that a team cannot merge without a day of conflict resolution is a sign the template change was badly made.

#### Self-service instead of tickets {#c6-self-service}

Each recurring kind of request from the audit in Section 6.1 is a candidate for a declarative request with a reconciler behind it: the team states what it wants, in the manifest or through an API, and the platform makes it so and keeps it so. The machinery of reconciliation belongs to the Resilience book's Section 3.1{% include xref.html to="resilience:3.1" %}, and the Architecture book's Section 15.2{% include xref.html to="architecture:15.2" %} names the tools, Crossplane and Kratix among them. What this chapter adds is a warning about the shape of what gets built.

Hohpe calls it the grim wrapper. A platform team, meaning well, wraps a cloud service in its own simplified interface, and at first the wrapper is a kindness. Then the cloud service gains features the wrapper does not expose, the wrapper's simplicity turns out to have been easiness that hides necessary choices, the documentation and community knowledge for the underlying service no longer apply, and the platform team finds itself operating a homemade abstraction indefinitely. Two of his other chapter titles point to the remedy: "Build Abstractions Not Illusions" and "Failure Doesn't Respect Abstraction". An abstraction is honest when, if the thing underneath breaks, its user can still understand what broke.

Encore's partner-credential API is built to that standard. A team with `exposure: partner` in its manifest calls one endpoint to issue a sandbox client identity for a named partner, bound to the partner's certificate and limited to the scopes the manifest declares; production identities follow automatically once Partner APIs records the partner's certification. The API's error responses are written for the failures that actually happen, and they name them plainly: the partner's certificate expires in nine days; this client was revoked at a stated time by a named person; the token-exchange service is degraded and existing tokens will keep working until they expire. Each of those conditions is something a product team would otherwise discover from a partner's angry email, and the API's job is to make sure the team hears first and understands what it heard.

Documentation is part of the path, and it is built with the same care. Every path's guide lives beside the code it describes, rendered into the portal from the repository in the docs-as-code style that Backstage's TechDocs supports, and a path's release is not finished until its guide has changed with it. Spotify's experience is the reason for the rule. Its golden paths began as tutorials and were refined by the feedback of new hires, the readers least able to fill a gap from memory.

#### The portal comes last {#c6-portal-last}

An internal developer portal shows the catalog of services, their documentation and owners, and the paths a team can start from. The Architecture book names the products, Backstage, Port and Cortex, and there is nothing wrong with any of them. The risk lies in the order of work. A portal built before the paths exist is a front door that opens onto an empty room, and practitioners describe this as a common way for platform programs to fail. In the same 2023 interview, Greul described organizations stalling at the proof-of-concept stage, faced with more than 70 steps and 100 plug-ins before they could begin. That is testimony, with no measurement behind it, and it agrees with Encore's own history: its portal predates this chapter by several years, and it has always been the most visible part of the platform while doing the least to remove waiting.

So Encore builds each capability as an API first, then as a command-line interface (CLI) that teams can script, and then as a page in the portal. The order matters for a reason beyond economy. An API forces the platform group to decide exactly what the capability does, while a portal form can hide an unfinished capability behind a pleasant layout. The catalog follows the same principle: every catalog entry is rendered from the service's manifest and never edited by hand, so that the catalog cannot drift from the services it describes. Machine interfaces matter for a newer reason too. As the Architecture book's Section 15.4{% include xref.html to="architecture:15.4" %} describes, coding agents reach golden paths through the platform's APIs and Model Context Protocol (MCP) tools; that practice is young, and it is one more argument for building the API first.

#### Releasing the platform itself {#c6-releasing-platform}

A platform capability is software that other teams depend on, so it is released the way the best of Encore's own APIs are released. It has a version. It is tested against its consumers, using the consumer-driven contract tests of Section 3.3, so that a change that would break a team's integration fails in the platform's pipeline and never in the team's. It moves through stages with stated criteria. And it publishes release notes written for the people who use it, which means saying what changes for them and what they must do, if anything, before saying what the platform team found interesting about the work. Fournier and Nowland give planning and delivery a chapter of their own, and the reason is plain enough: a platform's release discipline is how it earns the trust that its users extend every time they build on it.

Encore's shared webhook delivery followed this course. It went into beta in month 7 with one consumer, the Resale team, under a written agreement that the interface could still change. It reached general availability in month 9, once three criteria were met: two teams in production, the contract tests of both consumers passing on every platform change, and a service level objective (SLO) of its own, under the Resilience book's Section 3.5{% include xref.html to="resilience:3.5" %}, that 99.5% of webhook events reach a healthy partner endpoint within 60 s over 28 days. Before general availability, any team adopting it accepted the risk of change in writing. After it, the interface fell under the same deprecation rules as everything else the platform offers, and changes to its delivery logic rolled out progressively, as the Resilience book's Chapter 4{% include xref.html to="resilience:4" %} describes for any platform change.

**Recap.** The service manifest is the platform's main interface, so its schema is versioned and changed with the care of a public API. Templates need a way to reach the services they already generated, which one-shot scaffolders cannot provide and update tools and fleet-wide pull requests can. Self-service interfaces should be honest abstractions that name their failures plainly, documentation is part of each path, the portal is built last, and the platform's own capabilities are versioned, tested against their consumers and released in stages.

**Exercise 6.3.** Write the manifest fields your organization's next service would need. Mark which fields the platform could act on automatically today, which it could act on with work, and which are only recorded.

### 6.4 Adoption and Migration

#### The easy road {#c6-easy-road}

A platform capability is adopted the way any innovation is, gradually and unevenly, and it helps to see adoption as a sequence of stages. The sociologist Everett Rogers, in *Diffusion of Innovations* (1962), described the decision to adopt as a process that runs from knowledge through persuasion, decision and implementation to confirmation, and his most lasting point was that people abandon innovations at every stage, including after adopting them. Encore measures each path with a funnel of four stages of its own, shaped by Rogers's process: a team is aware of the path, has tried it, has adopted it for a production service, and is still using it six months later. The funnel is Encore's own instrument, and its last stage is the one that matters, because a path that teams try and then quietly leave has failed in a way that a launch-day count would never show.

Figure 6.4 shows the funnel for shared webhook delivery across the 14 services whose manifests declared `exposure: partner` by month 11.

{% include diagrams/fig-6-4.svg %}

*Figure 6.4 — The adoption funnel for shared webhook delivery. At month 9 seven services had tried it and two had adopted it; the stall between "tried" and "adopted" lasted until retries became configurable per partner. No count yet exists for the six-month stage.*

The stall at "tried" was the most useful thing the funnel showed. Teams tried the shared delivery in their sandboxes, liked it, and did not move production traffic onto it, and interviews found out why within a week. The service retried every failed delivery on one fixed schedule, and Rowmate's endpoint rate-limited Encore's calls during large on-sales, so a fixed schedule would have hammered Rowmate at exactly the wrong moment. Partner APIs' own sender had a hand-tuned backoff for Rowmate. Moving to the shared service would have meant losing it. Once retry profiles became configurable per partner, in the manifest, the stall cleared.

A path wins when it is the default and costs less effort than any detour, and both conditions can be engineered. The default is the template: a new service whose manifest says `exposure: partner` gets the shared delivery and the credential API without anyone asking. The cost of a detour is set by the exception path of the Architecture book's Section 15.3{% include xref.html to="architecture:15.3" %}, which lets a team leave the road provided it carries the cost, records the exception, names an owner and accepts an expiry date. What Encore deliberately does not do is mandate. DORA 2024 found that platforms were associated with lower throughput and stability particularly when they were mandated for the entire application lifecycle, which supports the stance the Resilience book's Section 3.5{% include xref.html to="resilience:3.5" %} takes: the road must keep earning its traffic.

Opt-outs are data. Each exception in the ledger is a team saying the path does not fit its work, and the platform group reads the ledger every month as part of discovery. When the same kind of exception appears for the third time, the group treats it as a missing path and opens an interview, which is how per-partner retries would have been found even without the funnel.

#### Lighthouse teams {#c6-lighthouse}

The first team on a new path does more than use it. Its experience becomes the story every other team hears, and so the order in which a platform takes on its users shapes how fast trust in it grows. Fournier and Nowland put this as optimizing growth in trust by ordering use cases. The first users should have a real need, so that the path is tested against real work, and their success should be visible to others, so that it persuades. The same idea, applied to external customers, is the design-partner program in the Products book's Section 3.3{% include xref.html to="products:3.3" %}.

Verified Resale was the obvious lighthouse for the partner-facing path, and the platform group chose it deliberately. Its need was real and urgent, since the team was already writing a fourth webhook sender. Its success would be seen by everyone, since the whole company was watching the bet. And it was a demanding first user, which is worth more than it sounds: a path that survives a demanding first team has fewer surprises left for the second. The choice carried a risk the group named in advance. A failure on so visible a service would be remembered for years, so the platform group staffed the collaboration fully for its quarter and put the Resale team's go-live dates on its own plan.

#### Migration campaigns {#c6-campaigns}

New services can be steered onto a path by the template. Existing services must be migrated, and migrations are where platforms most often fail their users. Each one costs the teams that must move a little of their attention, every team receives several at once, and none of them was in the team's plan. Fournier and Nowland give migrations and sunsetting a chapter of their own, and the published accounts agree on the principle: the platform should carry the cost, doing as much of the work as possible itself, so that each product team spends as little as possible. The Resilience book's Section 3.5 adds Encore's rule that the platform team performs the first three migrations itself before writing the self-service guide, and the Architecture book's Section 15.3{% include xref.html to="architecture:15.3" %} lists the parts of a deprecation campaign. What is left to describe is how a campaign is run.

The best published account is Spotify's. In "Tech Migrations, the Spotify Way" (2020), Saunak Chakrabarti and Jenni Lee describe a company of about 300 squads that, by 2017, was sending its engineers a steady stream of uncoordinated deprecation emails. Spotify's response was to treat migrations as a portfolio. A single prioritized migrations map was negotiated with its technical architecture group, and each migration was costed before it went on the map. "Each migration is owned by a PM," with alpha and beta groups trying it before everyone else, and with automated pull requests doing the mechanical work. Progress was tracked by squad on a page in Backstage, and each migration was driven "until it's 100% complete." The stated aim was to "remove the need to expose our engineering teams to 99% of migrations." For the mechanics of changing thousands of files, Section 2.5 has already described Google's tooling for large-scale changes, which shards one logical change into many reviewable pieces by ownership; a campaign is the layer of planning and persuasion that sits above that tooling.

Encore's campaign to retire the three home-grown webhook senders ran for one quarter, from month 9 to the end of month 11, and its plan fitted on one page.

```text
Campaign: retire home-grown webhook senders      Owner: Hana (platform PM)
Inventory: Partner APIs, Venue Integrations, Billing & Payouts senders;
           callers found by code search for `X-Encore-Signature`
Done by platform: migrations 1–3 by hand (Web & API Paths); then a
           codemod plus an automated pull request per remaining caller
Support: office hours Tue/Thu; one named engineer per migrating team
Tracking: campaign dashboard of callers remaining, by owning team
Brownouts: two, announced four weeks ahead; never within 48 h of an on-sale
End date: last day of month 11; old senders removed, code deleted
```

The order inside the campaign followed the same reasoning as the lighthouse. Partner APIs went first, because its sender was the largest and its team had been overloaded since Verified Resale was announced, as Section 9.2 recounts; taking the work off its hands was the campaign's best advertisement. Billing & Payouts went last, because payout notices are seen by organizers' finance departments and the team wanted a month of the shared service's track record before trusting it with them.

#### Deprecation that finishes {#c6-deprecation-finishes}

Migrations stall in their last few percent. The inventory says three callers remain, and nobody can say who owns two of them; the dashboard has been at 94% for six weeks; the old system costs little to keep running, so it keeps running. Hyrum's Law, which the Architecture book's Section 7.2{% include xref.html to="architecture:7.2" %} and Section 2.5 both discuss, explains why the tail is so long: with enough users, every observable behavior of a system is depended on by somebody, including users nobody knows about. *Software Engineering at Google*'s chapter on deprecation adds the organizational half: without an explicit owner, a deprecation is unlikely to make meaningful progress. I spent a decade maintaining a widely used open-source library, and every removal in that time taught the same lesson: the callers nobody has found usually announce themselves on the day the thing they used is removed.

Brownouts are the established way to find them first. A **brownout** is a scheduled, announced and temporary shutdown of a deprecated capability, short enough to do no lasting harm and long enough to make its hidden dependents fail visibly while the old path can still be restored. GitHub's retirement of password authentication for its API is the clearest published case. GitHub announced the deprecation on 14 February 2020, explaining that "during a brownout, password authentication will temporarily fail." It ran brownouts on 30 September and 28 October 2020, each in two windows, from 07:00 to 10:00 and from 16:00 to 19:00 UTC, and from 13 November 2020 at 16:00 UTC password authentication to the API returned an error for good. Each brownout turned an unknown number of forgotten scripts into a known list of failures with owners attached, at a time of GitHub's choosing.

Encore ran two brownouts of its old senders, in month 10 and early in month 11, each for two hours on a Tuesday morning, scheduled through the on-sale calendar so that neither fell near a large sale. The first found nothing new. The second found the fifth caller that code search had already shown and nobody had claimed: a nightly batch job in the Box Office team, written years earlier, which imported Venue Integrations' sender library to notify one venue's finance system of the day's in-venue sales. The job's author had moved teams. The brownout failed it at the next run, the venue noticed by morning, and the job was moved to the shared service within the week. Without the brownout, the same failure would have arrived on the day the old library was deleted, with no way back. The senders were removed and their code deleted on the last day of month 11, on the date the campaign had announced.

Removal has one more step that is easy to forget: preventing new uses. Google's deprecation chapter describes tooling that stops new callers from appearing while old ones are migrated, and Encore's equivalent is a lint rule in the pipeline that rejects any new code setting the `X-Encore-Signature` header outside the shared service. The rule exists because the fourth sender was written by a careful team with nowhere else to go, and the next team would have been in the same position.

#### Telling forty teams {#c6-telling-forty-teams}

A message sent once to 40 teams is received by a handful. People read announcements when they are relevant to the work in front of them, and for most teams, most of the time, a platform change is not. So the platform group says each thing several times, in several places, in the terms of each audience. Spotify's migration account makes the same point: after the email flood of 2017, it consolidated its communications and explained each migration's value separately to engineers, managers and leadership. The Architecture book's Section 15.5 covers the argument to leadership for funding a platform; here the audience is the engineers who must change their code.

Encore's mechanisms are ordinary and kept up. Each path has a changelog. Each release gets a short demonstration at the monthly engineering forum. And the platform newsletter, sent every two weeks, reports each path's adoption funnel in the form of Figure 6.4, so that teams can see where their colleagues stand and the platform group is held publicly to the numbers it chose.

**Recap.** Adoption is a funnel with leaks at every stage, and the stage after adoption, continued use, is the one that counts; stalls are found by asking the teams stuck at them. A path wins by being the default and the cheapest route, with a priced exception path for teams that leave it, and the exception ledger feeds discovery. Order the first users for trust, run migrations as campaigns with an owner, a plan and an end date, find hidden dependents with announced brownouts, and block new uses of what is being removed.

**Exercise 6.4.** Draft the campaign for one migration your organization owes, in the form of Encore's one-page plan: inventory, the work the platform will do itself, support, tracking, brownout dates and the end date.

### 6.5 Measuring Developer Experience

#### Three lenses {#c6-three-lenses}

There are three well-established ways to look at developers' work, and they answer different questions. DORA's delivery metrics, set out by Nicole Forsgren, Jez Humble and Gene Kim in *Accelerate* (2018) and extended since, measure the outcomes of software delivery: how often a team deploys, how long a change takes to reach production, how often changes fail, and how quickly service is restored. SPACE, from Forsgren, Margaret-Anne Storey and colleagues in 2021, is a menu of five dimensions of developer productivity, satisfaction and well-being, performance, activity, communication and collaboration, and efficiency and flow, with the advice to measure several at once and never one alone. DevEx, from Abi Noda, Storey, Forsgren and Michaela Greiler in 2023, names three dimensions of the developer's own experience: feedback loops, cognitive load and flow state.

The choice among them depends on the question. If we want to know whether the organization delivers well, DORA's metrics are the instrument, and Chapter 10's Section 10.5 uses them for exactly that. If we want to know whether a platform made developers' work better, DevEx is the closer fit, because a platform's purpose, in the Architecture book's terms, is to reduce cognitive load and shorten feedback loops, and those are two of DevEx's three dimensions. SPACE is the check against measuring too narrowly. This section measures the platform's effect, and leaves delivery at large to Chapter 10.

#### Surveys done properly {#c6-surveys}

Developers' own reports are the place to begin, for two reasons. They are quick to collect, and they see what systems cannot: no log records that an engineer spent a morning confused by a template, or gave up on a path and wrote their own. *Accelerate* devotes two chapters to the case for surveys and to psychometrics, the discipline of building questions whose answers can be trusted, and the Operations book's Section 7.4{% include xref.html to="operations:7.4" %} uses Westrum's validated items in the same tradition. A survey earns trust when its items are tested, its cadence is stable and its response rate is published alongside its results, because a survey answered by a third of engineers describes a third of engineers.

The harder discipline is tying each question to a decision. *Software Engineering at Google*'s chapter on measuring engineering productivity, by Ciera Jaspan, gives the method its name: Goals–Signals–Metrics (GSM). "A goal is a desired end result." "A signal is how you might know that you've achieved the end result." "A metric is proxy for a signal." The chapter adds that Google tries "to triangulate on the truth using mixed methods", setting survey answers beside logs. LinkedIn published a reusable framework built on the same method in 2023, its Developer Productivity and Happiness Framework, and it is a good starting point for anyone writing their own. Figure 6.5 shows GSM applied to Encore's partner-facing path.

| Goal | Signal | Metric | Decision it informs |
|---|---|---|---|
| A team can ship a partner-facing service without waiting on others | Teams report no waits for credentials or reviews | Survey: "In my last new service, I waited on another team for…" (days) | Which path step to make self-service next |
| Partners receive webhooks reliably | Partners stop reporting missed or duplicate events | Webhook SLO attainment; partner support cases about webhooks | Whether delivery needs work before new features |
| The path stays in use | Teams do not rebuild their own senders | Funnel's six-month stage; new exceptions in the ledger | Whether the path is missing something |
| New partner-facing services start faster | First deploys arrive sooner | Working days from repository creation to first production deploy | Whether the path delivered its brief |

*Figure 6.5 — Goals–Signals–Metrics for the partner-facing path. Every metric names the decision it exists to inform.*

Encore runs a quarterly developer experience survey with ten core items that never change, so that one quarter can be compared with the next. Among them: "In the last quarter, I could get a change to production without waiting on another team." "I understand how to use the platform capabilities my service needs." "When something on the platform fails, I can tell why." Each path may add a few items of its own for a quarter or two. In the quarter after the path reached general availability, 71% of engineers answered, and that figure is printed at the top of every result.

#### System metrics beside the survey {#c6-system-metrics}

Surveys tell us how the work felt. System metrics tell us what happened, and the two are most useful side by side, which is the combination the DevEx paper recommends. For a platform, the system metrics worth having are few and concrete: time to first production deploy for a new service; the feedback time of build and test, which Chapter 4 owns and which a platform affects through its templates; time to a new engineer's first merged change; and the time teams spend waiting for anything to be provisioned. Each needs a written definition before anyone builds a dashboard for it. "Time to first deploy" can start at the first commit, the creation of the repository or the approval of the work, and the three choices give very different numbers; a team that changes the definition halfway through a year has two half-years of data instead of one.

Encore defines time to first deploy as working days from repository creation to the first production deploy that serves real traffic, and measures it for every new service. The Resale team's was 23. The second partner-facing service to start after shared webhook delivery reached general availability was the Festivals team's festival feed, which sends event and pass updates to the festival app, and it was created early in month 11. Its time to first production deploy was four working days. One service is not a trend, and the group says so in the newsletter. But the four days decompose cleanly: no credential tickets, no security review of a sender, and two days of the team's own work. Those are the steps the path was built to remove.

#### Adoption, satisfaction, outcomes {#c6-platform-metrics}

For each path, the platform group reports three things: who uses it, how they rate it and what changed for them. Adoption comes from the funnel, satisfaction from the survey's path items, and outcomes from the system metrics. Each alone misleads. A path can be widely adopted because it is the default and still be disliked; it can be loved by its two users and irrelevant to the other 38 teams; it can be adopted and liked and change nothing measurable, because the friction it removed was not the one that mattered.

Encore expects the numbers to be mixed at first, and the evidence says it should. DORA 2024 found that users of internal platforms reported 8% higher individual productivity and 10% higher team performance, with organizational performance 6% higher. It also found that throughput fell 8% and change stability fell 14%, figures the Architecture book's Section 15.5{% include xref.html to="architecture:15.5" %} has already discussed. DORA described the pattern over time as a J-curve: initial gains, followed by a decrease and then recovery as the platform ages and matures. A platform group should therefore report its numbers over several quarters before drawing conclusions. To see where time saved by a platform actually went, Encore uses Mik Kersten's flow distribution, which Chapter 10's Sections 10.4 and 10.5 explain: if the Resale team's saved days went into features, the distribution shows it, and if they were lost to waiting somewhere else, it shows that too.

#### Scorecards that do not rank {#c6-scorecards-no-rank}

Every measure in this section can be turned into a league table, and doing so would destroy it. Goodhart's Law, which Chapter 10's Section 10.5 develops with its real case, is the general reason: a measure that becomes a target stops measuring. DORA's own guidance on its metrics is specific about the form the damage takes. The metrics "are meant to be applied at the application or service level," and "the goal is to improve your team's performance over time, not to compete against other teams or organizations." A team ranked against others learns to improve its rank, which it can do faster by changing what it reports than by changing how it works.

Encore's rule settles a wording question between this book and the Architecture book. The Architecture book's Section 15.3 says each service's scorecard is visible to both the team and its leadership. Both remain true, and the rule says how. A team sees its own scorecard in full. Leadership sees trends over time and the distribution across all teams, and uses them to find where the platform is failing its users. Nobody sees a ranking, there are no league tables, and no scorecard number enters anyone's performance review.

Campaign tracking needs a careful line, because Spotify's published practice crosses it on purpose. Its migration pages showed progress by squad, explicitly to make completion something of a game, and Spotify reports that this worked. Encore allows the same thing within narrow limits: a dashboard showing which teams still call the old webhook senders is campaign tracking, finite and dated, and it disappears when the campaign ends. It shows who has work left, never who is good at their job, and it is never used in performance reviews. Continuous quality measures are not shown that way at all. The difference is that a campaign has an end and every team can reach it, while a ranking on a continuous measure guarantees that someone is always at the bottom.

AI assistance raises the question of whether these measures need to change. Encore's answer so far has been to add two survey items about AI-assisted work and change no targets. The evidence, including what DORA sees at the team level, is in Section 5.1, and the organization's delivery measures are in Section 10.5.

**Recap.** Choose a lens by the question: DORA for delivery, DevEx for the developer's experience of a platform, SPACE as the check against measuring one thing. Begin with a stable, validated survey and tie every question to a decision with Goals–Signals–Metrics, then set defined system metrics beside it. Report adoption, satisfaction and outcomes together, expect a J-curve, show teams their own scorecards and leadership the trends, and rank nobody.

**Exercise 6.5.** For one golden path in your organization, write five survey items and two system metrics with precise definitions. Beside each, write the decision it would inform, and delete any item for which you cannot name one.

### Kata: The Portal Nobody Visits

> **Your brief: "Copperline."** Copperline rents cars and vans from about 600 branches in four EU countries, booked through its own website and app and through travel partners, with 250 engineers in 28 teams. Two years ago its 14-person platform team built an internal developer portal, with a catalog, a dozen service templates and a scorecard page, and launched it with a company-wide announcement. Today only 9% of Copperline's services were created from its templates, the scorecard page is opened mainly by the platform team, and the catalog lists about a third of the services in production. Product teams describe the platform as "the place you file tickets." Each quarter the platform group receives about 900 requests, most of them for database access, network rules and service accounts, and the median wait is six working days. A new service takes a median of 31 working days to reach production. Three teams run their own deployment pipelines, two of them copied from each other, and the rental-agreements team maintains a document-signing library that five other teams import. The CTO has given the platform group two quarters to show that it is worth its budget.

**Deliverables:**

1. **Discovery findings** — A plan for interviewing six teams about recent concrete episodes, an audit of one quarter's requests classified by kind, and a desire-path search for copied pipelines and duplicated libraries. State what each finding would change.
2. **A journey map** — One journey, from idea to first production deploy, in the form of Figure 6.3, with each step checked against timestamps and the waits ranked.
3. **The thinnest increment** — The one or two capabilities you will build first, chosen with a stated rubric and a check on each capability's evolution stage, with a one-page path brief for each. Say what you will decline, including anything the portal's users have asked for.
4. **One migration campaign** — A one-page plan for moving the three home-grown pipelines, or the signing library's importers, onto the platform: inventory, the work the platform does itself, support, tracking, brownouts and an end date.
5. **The measures** — Five survey items and two system metrics with written definitions, tied to decisions by Goals–Signals–Metrics, and the adoption funnel you will report each month.
6. **The portal's future** — A short decision on what to do with the existing portal while the paths are built, and how its catalog will stop drifting from production.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Evidence before building | Can you trace every capability you chose to an interview, a request count or a journey map? |
| Thinness | Is your first increment the smallest thing that removes the largest wait, and did you buy or adopt what is a commodity? |
| Self-service | After your increment, can a team get what it needs without asking anyone? |
| A campaign that finishes | Does your migration have an owner, an end date and a way to find callers nobody knows about? |
| Honest measurement | Does each measure name the decision it informs, and would any of them rank teams? |
| Pull | Would Copperline's teams choose your path if nobody required them to? |

#### Where you now stand

You can now treat an internal platform as a product with colleagues for customers: find what they need by interviewing them and mapping their journeys, choose the thinnest increment and write it a brief, build it as an honest self-service interface behind a versioned manifest, bring teams onto it with defaults, lighthouses and campaigns that finish, and measure whether it helped without ranking anyone. The partner-facing path is the first piece of Encore's platform whose users reach beyond Encore's engineers, since its credentials and webhooks are what partners touch. Chapter 7 turns to the platform whose users are all outside: Encore SaaS, sold to venues, where onboarding, identity, entitlements and the life of a tenant are product questions of the same kind, asked of customers who can leave.

### References

- T. A. Dolotta, R. C. Haight, J. R. Mashey — [*UNIX Time-Sharing System: The Programmer's Workbench*](https://archive.org/details/bstj57-6-2177). Bell System Technical Journal 57(6), 1978 — free online.
- Camille Fournier, Ian Nowland — [*Platform Engineering: A Guide for Technical, Product, and People Leaders*](https://www.oreilly.com/library/view/-/9781098153632/). O'Reilly, 2024.
- Gregor Hohpe — [*Platform Strategy: Innovation Through Harmonization*](https://leanpub.com/platformstrategy). Leanpub, 2024.
- DORA — [*Accelerate State of DevOps Report 2024*](https://dora.dev/research/2024/dora-report/). Google Cloud, 2024 — free online.
- Saunak Chakrabarti, Jenni Lee — [*Tech Migrations, the Spotify Way*](https://engineering.atspotify.com/2020/6/tech-migrations-the-spotify-way). Spotify Engineering, 2020 — free online.
- Gary Niemen — [*How We Use Golden Paths to Solve Fragmentation in Our Software Ecosystem*](https://engineering.atspotify.com/2020/8/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem). Spotify Engineering, 2020 — free online.
- Titus Winters, Tom Manshreck, Hyrum Wright (eds.) — [*Software Engineering at Google*](https://abseil.io/resources/swe-book). O'Reilly, 2020 — free online.
- Abi Noda, Margaret-Anne Storey, Nicole Forsgren, Michaela Greiler — [*DevEx: What Actually Drives Productivity*](https://queue.acm.org/detail.cfm?id=3595878). ACM Queue 21(2), 2023 — free online.
- Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, Thomas Zimmermann, Brian Houck, Jenna Butler — [*The SPACE of Developer Productivity*](https://queue.acm.org/detail.cfm?id=3454124). ACM Queue 19(1), 2021 — free online.
- GitHub — [*Deprecating password authentication*](https://developer.github.com/changes/2020-02-14-deprecating-password-auth/). GitHub developer changelog, 2020 — free online.
- Matthew Skelton, Manuel Pais — [*Team Topologies*, 2nd ed.](https://teamtopologies.com/book). IT Revolution, 2025.
- Nicole Forsgren, Jez Humble, Gene Kim — [*Accelerate*](https://itrevolution.com/product/accelerate/). IT Revolution, 2018.
- Evan L. Ivie — [*The Programmer's Workbench — A Machine for Software Development*](https://dl.acm.org/doi/10.1145/359842.359856). Communications of the ACM 20(10), 1977.
- Mike Rother, John Shook — [*Learning to See*](https://www.lean.org/store/book/learning-to-see/). Lean Enterprise Institute, 1998.
- Copier — [*Updating a project*](https://copier.readthedocs.io/en/stable/updating/). Copier documentation — free online.

---

## Chapter 7: Building the SaaS Platform — Tenants, Identity, and Administration {#ch7}

> Every customer wants a system built for them alone. The craft is to give them one by changing nothing but the data.

A software company that sells its system to other businesses soon finds that it has built two products. The first is the one in the brochure: for Encore, ticketing that a venue can put its own name on. The second is everything needed to have many such customers at once. Someone has to sign them up, give their staff accounts and take them away, decide what each has paid for, help them when something goes wrong, and one day let them leave. The Architecture book drew this second product as the **control plane**, the part of a software-as-a-service (SaaS) system that manages the tenants, as distinct from the application plane that serves them, and it argued for the shape of each piece (the Architecture book{% include xref.html to="architecture" %}, Chapter 14). This chapter is about building those pieces and keeping them working, at 400 engineers, while the application plane changes under them every day. The question that runs through it is how a company can let hundreds of customers differ from one another without letting its code differ for each of them.

The best early answer came from a small company in a rented apartment on Telegraph Hill in San Francisco. On 8 March 1999, Marc Benioff, Parker Harris, Frank Dominguez and Dave Moellenhoff began work on the first version of Salesforce's customer relationship management (CRM) service, and on 7 February 2000 they launched it at an event they called "The End of Software". The slogan mocked the installed enterprise software of the day, in which every customer ran its own copy with its own customizations compiled in. Salesforce ran one shared copy for everyone, and that decision forced a second one. If thousands of businesses were to share one running system, and each wanted its own fields, its own forms and its own rules, then those differences could not live in the code, because there was only one code. They had to live in data. Over the next decade the company built this idea into a general platform, released as Force.com in 2008, and in 2009 its chief architect, Craig Weissman, with Steve Bobrowski, described the design at the ACM's SIGMOD conference. Weissman had joined in 2002, when the engineering team was still small, so the paper describes what the founders' design had grown into, and he did much to extend it.

The companion whitepaper Salesforce published in 2008 states the principle with unusual clarity. "Inherently, a multitenant application must be dynamic in nature, or polymorphic, to fulfill the individual expectations of various tenants and their users." When a customer defines a custom table or lays out a form, the platform "does not create an 'actual' table in a database or compile any code. Instead, Force.com simply stores metadata that the platform's engine can use to generate the 'virtual' application components at runtime." A universal data dictionary holds every object, field, form and access rule as metadata. Tenant data sits in one very large table with hundreds of generic, variable-length columns, onto which each tenant's custom fields are mapped. Every row carries an organization identifier, the `OrgID`, which leads every index and partitions every table. Governors cap the processor time, memory and queries any one tenant's code may use in a single execution, so that no tenant can monopolize the shared engine, and deletions are soft, landing first in a recycle bin. Salesforce even reran every customer's unit tests against each new release of the platform, to learn before its customers did whether it had broken one of them. Nearly every section of this chapter descends from one of those mechanisms: the organization key on every row becomes Encore's tenant directory, the metadata becomes its configuration and entitlements, the governors become per-tenant quotas, and the recycle bin becomes the soft delete that Atlassian made universal across its own products after its outage of 2022. Figure 7.1 draws the design as the whitepaper describes it.

{% include diagrams/fig-7-1.svg %}

*Figure 7.1 — Force.com's multitenancy in schematic. The customizations live in the metadata, every tenant's rows share one table, and the `OrgID` that leads every index is the only thing that keeps them apart.*

Encore has run a control plane since the venue chain's email in the Architecture book. About 500 self-service venues share pooled serverless cells of about 50, Professional venues run in Kubernetes cells with a database each, and one Enterprise tenant, `venue-chain-a`, has a silo of its own. Seven teams build Encore SaaS for venues, among them Tenant Onboarding, Tenant Identity and Tenant Configuration. Verified Resale now asks more of that control plane than venues ever did. It brings in resale partners, Rowmate and later Tessera, organizations with people, machines and a lifecycle of their own that are nevertheless not tenants. It gives every organizer a set of resale rules that must be edited, checked, rolled out and audited like code. And the people who run the marketplace behind the scenes need tools of their own. This chapter follows each of those demands into the control plane that has to meet it.

### 7.1 Onboarding as a Product

#### Time to first sale {#c7-time-to-first-sale}

Touring crews have a word for the work done before a show reaches a town: the **advance**. Weeks ahead, the production manager calls the venue and works through a long list. How wide is the loading door, how much power is on the stage, when may the trucks arrive, who holds the keys? A good advance is invisible on the night; a bad one shows up as a truck that cannot reach the dock at four in the afternoon. Onboarding a tenant is the software company's advance, judged by what happens on the night. The comparison breaks on scale: a crew advances a few dozen venues a year by telephone, while a SaaS company must advance hundreds of customers it will never speak to, so its advance has to be software. The Architecture book set Encore's measure in its Section 14.2: time from signature to first sale.

The first step is to define the event that stops the clock, and to define it so that it cannot be gamed. **Activation** is the moment a new customer first gets the value the product promised; the term comes from the startup "pirate metrics" of the late 2000s, and Alistair Croll and Benjamin Yoskovitz's *Lean Analytics* (2013) treats it at length for SaaS. For a venue on Encore, the value is a ticket sold to a stranger. Encore therefore counts activation as the first paid order placed by someone who is not on the venue's own staff, so that the box-office manager's test purchase on the first evening does not count. Every step before that is instrumented as a tracking event, named by the convention the Products book's Section 4.2{% include xref.html to="products:4.2" %} lays down: `onboarding_storefront_provisioned`, `onboarding_payout_account_verified`, `onboarding_seat_map_completed`, `onboarding_first_event_published` and `onboarding_first_sale_recorded`. With those events in place, the funnel is a query.

The funnel has to be cut by tier before anyone reads it. An Enterprise onboarding contains weeks of contract negotiation and identity setup, and those waits belong to the deal and say nothing about friction in the product, so mixing them into the self-service numbers would hide everything interesting. Figure 7.2 shows Encore's self-service venues over the four quarters before Verified Resale.

{% include diagrams/fig-7-2.svg %}

*Figure 7.2 — Encore's self-service onboarding funnel over four quarters, with each step's venues, share of sign-ups and median time from sign-up. The provisioning workflow takes minutes; the venue's own work takes days, and most of the loss happens at the seat map.*

Two readings of the figure are worth separating. The first concerns the workflow. Provisioning, the part the Architecture book asked to happen in minutes, does: 99% of venues have a storefront within four minutes of signing up. Engineers looking only at the workflow would conclude that onboarding works. The second reading concerns the customer. Fewer than half of the venues that signed up sold a ticket, and the largest single loss, 64 venues, is at the seat map. When Tenant Onboarding cut the funnel by venue type, the cause became plain. Standing-room clubs, which need only a capacity, passed through the step in minutes; seated halls had to draw every row in the seat-map builder by hand, and many gave up. The fix was a seat-map importer that reads the floor plans and seat lists venues already hold from their previous ticketing system, and Event Setup, which owns the builder, shipped it. The general lesson is that the activation metric must belong to the customer's journey as a whole, because a workflow measured only on its own steps will report success while customers stall somewhere it cannot see.

#### The tenant directory {#c7-tenant-directory}

Before onboarding can be built, something has to hold the answer to the most basic question a control plane is asked: who is this customer, and where do they live? In Salesforce's design that answer is the `OrgID` on every row. At Encore it is the **tenant directory**, the single system of record for each tenant's identity, tier, placement, lifecycle state and contacts. The directory has one writer, the Tenant Onboarding team's service. Every other service reads it, through an API or from the events it publishes when a record changes, and none keeps its own private copy of who a tenant is. This is ordinary single-writer discipline from the Architecture book's Chapter 6{% include xref.html to="architecture:6" %}, applied to the record that every other record depends on.

Verified Resale forced Encore to be precise about what the directory holds. Encore has four kinds of customer: fans, organizers, partners and SaaS tenants. Only venues are tenants. A tenant has a placement, a cell in a region, an isolation tier and a storefront of its own. An organizer is a customer with an organization account in the organizer console; it sells events through Encore and through venues, but it has no cell and no storefront. A partner is an organization that calls Encore's public application programming interface (API). The three share a great deal, since all three have members, roles, a lifecycle and an audit trail, and so the directory records all of them as **organizations**, distinguished by a `kind`. Only tenants carry placement. Keeping them in one directory, while keeping the word "tenant" for venues alone, gives the identity and audit machinery one model to serve without pretending that an organizer lives in a cell. A record for a Professional venue looks like this:

```yaml
org_id: org_7f3k2q            # opaque; never derived from a name or domain
kind: venue_tenant           # venue_tenant | organizer | partner | encore_staff
display_name: "Riverside Hall"
tier: professional           # placement follows tier; checks use entitlements
placement: { region: EU-2, cell: pro-eu2-04, data_residency: EU }
state: live                  # trial | live | suspended | offboarding | closed
contacts: { owner: user_19ab, billing: user_2c4d, security: user_19ab }
identity: { sso: saml, scim: enabled, recovery_owner: user_19ab }
resale_eligible: true        # market supports Verified Resale
version: 41                  # every change increments; history is kept
```

Two absences in that record matter as much as its fields. It holds no fan's personal data, because a record read by almost every service is the worst place for data that must be erased on request. And it holds no entitlements: the directory says what tier a tenant is in, while what that tier includes belongs to the entitlement service of Section 7.3, so that packaging can change without touching the record of who a customer is.

#### Onboarding as a durable workflow {#c7-durable-onboarding}

The Architecture book argued that onboarding should be a workflow with four steps, provision, configure, seed and verify, each with a compensation that undoes it, run on the workflow engine of its Chapter 6. Compensating sagas go back to Hector Garcia-Molina and Kenneth Salem in 1987, and durable engines such as Cadence, built at Uber from 2015, and its successor Temporal have made running them routine. What the argument leaves open is what building such a workflow demands of the people who write its steps, and four properties have mattered at Encore.

The first is that each step is idempotent, keyed by the tenant and the step. Workflow engines retry, and a step that creates a database must recognize, on its second attempt, that the database it is about to create already exists because the first attempt succeeded just before the network failed. The second is that each step states its precondition and checks its result. "Create the storefront domain" first asks whether the tenant's record is in the `trial` state and the domain is free, and afterwards it fetches the domain and confirms that it resolves; a step that trusts its own success is a step that will one day report success for something that did not happen. The third is telemetry per step, so that the ops console shows each tenant's onboarding as a timeline, with the step it is on, how long each step took and what each retry saw. The fourth is resumption. A workflow interrupted by a deploy or a regional failover resumes from its last completed step; it does not start again, and it never leaves a tenant half built.

The Operations book's curtain-up workflow (its Section 3.2) follows the same pattern for the same reasons: long-running steps across many systems, partial failures, and operators who need to see where they stand. When a self-service venue's onboarding stalls at two in the morning, nobody is woken; the step retries on its schedule, and if it fails for good the compensation runs and the venue is told plainly what to do next.

#### Signup and its abuse {#c7-signup-abuse}

Open signup is the reason self-service is cheap, and it is also an invitation. The fraud that follows a ticketing platform's open door is the fake organizer, who publishes an event that will never happen, sells tickets to it and disappears with the money, leaving fans with the loss and the platform with chargebacks. The obvious defense, verifying every new business before it may sell anything, would destroy the activation curve of Figure 7.2, since **know-your-business (KYB)** checks, which verify that a company exists and who controls it, can take days.

The published practice of marketplace payment platforms resolves the tension by separating the right to sell from the right to be paid. Stripe's Connect platform, for instance, tracks whether an account may accept charges separately from whether it may receive payouts, collects the required information "upfront or incrementally", and disables payouts when a verification deadline passes. Eventbrite tells new organizers that their first payout will be sent after their event ends. The principle is to let activation proceed while the money waits, but it comes with conditions that are easy to forget. The payment service provider (PSP) decides what must be known before the first charge, and that minimum varies by country and business type, so "no checks before the first sale" is never quite true. And holding the payout is not enough to protect fans: the funds themselves must stay where a refund can reach them, or a fake event leaves fans with nothing to be refunded from.

Encore applies the rule to organizers, whose signup, verification and contracts belong to the Organizer Onboarding team. A new organizer can publish and sell as soon as the PSP's hosted onboarding has collected what it needs for charges. Full KYB runs through the same hosted flow, and until it completes and the organizer's first event has taken place, the organizer's revenue stays with the PSP. Encore's counsel also reads the Digital Services Act (DSA), the EU regulation that has governed online platforms since February 2024, as applying to organizers who sell to fans through Encore's storefront: Article 30 requires a platform to collect a trader's identity, contact and payment details, with a self-certification, before the trader may use the service. The signup form collects them, and the PSP's checks later verify them. Partners are vetted on the same rails with stricter checks, which Chapter 8 describes.

#### The same rails for the largest customers {#c7-enterprise-onboarding}

Sales-assisted onboarding tempts every company into a second process. The customer is large and the contract is valuable, so senior engineers set up its environment by hand as a mark of respect, and the result, as the Architecture book's Section 14.2{% include xref.html to="architecture:14.2" %} warned, is a one-off that the next disaster-recovery drill rebuilds wrongly. The engineering answer is to model the human work as steps in the same workflow. A **human task** is a workflow step that waits for a person, with a named owner, a deadline and an escalation path; workflow engines have long supported such steps, as signals, callbacks or the user tasks of business-process notations.

When a group of 12 municipal venues in one Dutch city joined Encore as Professional tenants, its onboarding ran on the self-service workflow with six human steps added: the signed contract, identity-provider federation, a data migration from the group's old box-office system, configuration of its door-scanning hardware with Venue Entry, a security review of its integration with the city's finance system, and a joint test on-sale. Each had an owner, a due date and an escalation to the account lead after two working days' delay, on the same timeline as the machine steps. When the city's identity team took three weeks over federation, everyone could see where the onboarding was waiting, and when Encore later rebuilt the cell hosting the group's venues during a drill, the workflow knew exactly how each venue had been made.

**Recap.** Onboarding has a customer's measure, time to a first real sale, and only a funnel cut by tier shows where customers are lost. The tenant directory is the single, versioned record of every organization, holding neither fan data nor entitlements, and durable workflows carry every tier, human steps included, while payouts wait for verification and selling does not.

**Exercise 7.1.** Write down the tracking events of your own onboarding funnel, from sign-up to the first moment a customer gets real value from a stranger. Then name the step at which you expect to lose the most customers, the query that would prove or disprove it, and the cut (by tier, segment or customer type) without which the answer would mislead you.

### 7.2 Organizations and Identity

#### Users, organizations and memberships {#c7-identity-model}

Backstage at a large concert, nobody's identity is a single fact. A lighting technician carries a laminate that names her, the tour she works for and the zones she may enter; on another tour next month she will carry another laminate with other zones, and she is the same person throughout. The laminate fails as a model only in its permanence, since it is printed once for a tour, while a membership must be revocable within minutes. Business software has to model the same thing, and the standard model for it has four parts. A **user** is a person who can sign in. An **organization** is a customer, partner or internal body that users act for. A **membership** joins one user to one organization, and a **role** on that membership says what the user may do there. Because memberships are many to many, one user can belong to several organizations, with different roles in each. GitHub organizations, Slack's enterprise workspaces and the "organizations" features of the commercial identity services all take this shape.

At Encore the model has to say something the Architecture book deliberately left out. Its Section 14.2 simplified matters by giving each member of staff exactly one tenant, so that the token issued at sign-in could carry the tenant directly. That simplification served a chapter about architecture, and it no longer fits the company. A box-office manager at a Professional venue may also do the ticketing for a promoter that books shows into other venues, so she is a member of a venue tenant and of an organizer, with different roles in each. Encore's model replaces the simplification in one precise way. The user chooses an **active organization** at sign-in, or switches to another later, and the token carries that one organization. The gateway therefore still resolves exactly one tenant or organization per request, as the Architecture book required; the change is only that the person chooses which one it is. Fans stand outside this model altogether. A fan's identity carries no organization, and the venue a fan buys from is still determined by the storefront, as before.

Encore's directory has four kinds of organization: venue tenants, organizers, partners and Encore staff. Treating Encore's own staff as an organization is the choice that pays most over time, because a support agent acting inside a venue's console is then simply a member of one organization acting on another, which the model can represent and the audit log can record.

#### Single sign-on in practice {#c7-sso}

**Single sign-on (SSO)** lets a customer's staff sign in to Encore with their own corporate accounts, checked by the customer's own identity provider (IdP). The two protocols that matter are Security Assertion Markup Language (SAML) 2.0, which OASIS standardized in March 2005, and OpenID Connect (OIDC), whose core specification the OpenID Foundation published in February 2014. The protocols are mature. The engineering lies in letting a customer configure them without a support case.

A Professional venue's administrator sets up SSO herself in the console, and the console asks three things of her in order. First she proves that the venue owns its email domain, by publishing a token Encore gives her in a TXT record in the domain's Domain Name System (DNS) zone; without that proof, anyone could configure an identity provider that claims every user at somebody else's domain. Then she enters the identity provider's metadata, Encore runs a test sign-in, and she chooses whether accounts are created **just in time**, on a user's first sign-in, or only through provisioning. Throughout, the venue keeps a **recovery owner**: one account that can still sign in with a password and a hardware key when the venue's identity provider is down or misconfigured. It is the customer's own break-glass account, and it exists because the day an identity provider fails is exactly the day an administrator most needs to get in.

The one rule Encore adds from hard public experience concerns the parsing. In March 2025 GitHub's Security Lab disclosed two vulnerabilities in ruby-saml, a widely used library for consuming SAML responses (CVE-2025-25291 and CVE-2025-25292, fixed in version 1.18.0). The library used two XML parsers that could be made to disagree about the same document, and an attacker holding one validly signed SAML document could exploit the disagreement to sign in as any user. What the episode teaches is that signature handling in SAML is subtle enough that nobody should write their own, and that the library one uses is security-critical code to be patched on the security-fix clock of the Resilience book's Section 7.3{% include xref.html to="resilience:7.3" %}. Encore uses one maintained SAML library across the console, and Tenant Identity owns its upgrades.

#### SCIM and the departing employee {#c7-scim}

SSO solves the arrival of a user, and the harder problem is the departure. When a box-office manager leaves the venue chain, her access to Encore should end on the same day without anyone filing a ticket. The **System for Cross-domain Identity Management (SCIM)**, published by the Internet Engineering Task Force (IETF) in September 2015 as RFC 7643 for the schema and RFC 7644 for the protocol, lets the customer's identity provider or human resources (HR) system create, update and deactivate users in Encore automatically. The protocol exchanges JavaScript Object Notation (JSON) documents over HTTP, and most of its value lies in deprovisioning.

The cost of slow deprovisioning has a public record. In a filing with the US Securities and Exchange Commission on 4 April 2022, Block disclosed that on 10 December 2021 a former employee had downloaded reports containing information on about 8.2 million current and former customers of Cash App Investing, "after the employee's employment ended". The filing did not say why the access remained. For our purposes the lesson is the interval itself: between the day a person leaves and the day their access ends, anything they can still reach is exposed, and every organization has such an interval, measured or not.

Encore measures the gap as time from deprovision to lost access, with a target of under five minutes, and "lost access" is meant literally. A SCIM request that sets a user's `active` attribute to false, which identity providers send far more often than a delete, disables the account, but a session already open in a browser and a refresh token held by an integration both outlive the account unless something cuts them. So deactivation at Encore revokes the user's sessions and tokens in the same transaction, the console's sessions are short, and the metric is measured by a probe that tries to use a deprovisioned user's session after the fact.

Testing a SCIM endpoint is mostly testing against other people's implementations, since each major identity provider reads the RFCs slightly differently. Tenant Identity built an identity-provider simulator in the manner of Section 3.3, with the behaviors of the main providers on demand, and checks it against public validators such as Microsoft's SCIM Validator and open-source conformance testers. The details that break integrations are small and specific: a request for an unknown user must return 404 with SCIM's error schema, never a 500, and a duplicate create must return 409 with the `uniqueness` error type.

#### Roles, permissions and delegated administration {#c7-roles}

The long-standing answer to what users may do is **role-based access control (RBAC)**: fine-grained permissions, such as `refund.issue` or `event.publish`, grouped into roles such as box-office manager or finance viewer, and roles assigned to memberships. Enterprise customers soon ask for custom roles, which RBAC handles with little strain. What strains it is hierarchy. The venue chain's central administrator must manage the staff of every venue in the chain, a regional manager must manage only her region's venues, and a venue manager only her own. Expressing that with flat roles means creating a role per venue, or writing code that walks the hierarchy, and Encore had done both, separately, in each tier's console.

**Relationship-based access control** answers the hierarchy directly, by storing permissions as relations between objects, such as "user U is an admin of region R" and "venue V is in region R", and computing what follows. Google's Zanzibar, described by Ruoming Pang and colleagues at USENIX ATC in 2019, is the proof that this works at scale: the paper reports "trillions of access control lists and millions of authorization requests per second", serving Calendar, Drive, Maps, Photos and YouTube with a 95th-percentile latency under 10 milliseconds and better than 99.999% availability over three years. Its "zookie" consistency token keeps a permission change and a content change from being applied out of order. Zanzibar proves the model, not that a company of Encore's size should build one. Airbnb's Himeji, a centralized authorization service inspired by Zanzibar and described by its engineers in 2021, is the closer precedent, and open-source implementations of the model now exist.

Encore replaced its tier-specific role code with one authorization service, run by Tenant Identity on an open-source Zanzibar-style implementation, which every console and API consults. Delegated administration fell out of the model. The chain's administrator can grant roles anywhere below her in the hierarchy and nowhere above it, and the authorization service enforces the limit for every console.

#### Partners as organizations {#c7-partner-orgs}

Verified Resale brought in the first organizations that are neither tenants nor organizers. Rowmate, the launch partner, and Tessera, the second, are organizations with human members, who use a partner console to watch their listings, and machine clients, which call the public API. Each partner gets a sandbox of its own at once and, after it passes certification, a production grant of its own: its own scopes, keys and client certificates. The scopes keep the original boundary that held even when Rowmate's key leaked (the Resilience book, Section 7.2): `listings:read` and `resale:write`, never primary inventory, fan data or payouts. Machine clients authenticate with the 15-minute certificate-bound tokens Encore adopted after that leak.

The organizer's side of the relationship is recorded as configuration. An organizer's resale rule for an event, described in Section 7.3, decides whether that event's tickets may be resold at all and when; if they may, a listing enters Encore's resale pool and is visible to every authorized partner. The gateway checks two records on every partner call: the partner's grant, to establish what this partner may do, and the event's effective resale rule, to establish whether it may be done for this event now. The grant records the Encore person who approved it and the partner administrator who accepted it, and revoking it takes effect within one token lifetime, 15 minutes, because no new tokens are minted and existing ones expire. A change to an organizer's rule reaches the gateway through the ordinary configuration path, so the console and the gateway never disagree, and each partner receives a `rules.changed` webhook so that its own pages can follow.

**Recap.** The business identity model of users, organizations, memberships and roles replaces the one-tenant-per-person simplification with an active organization carried in the token. SSO needs a maintained parser, SCIM is measured to the last live session, relationship-based authorization gives hierarchy one home, and partners hold per-partner grants checked with each event's rule on every call.

**Exercise 7.2.** Draw your product's identity model as entities and relations. Mark where a person who works for two of your customers would break it, and where your own staff act inside a customer's account. Then measure, with a real test account, how long a deprovisioned user's open session keeps working.

### 7.3 Entitlements and Configuration

#### Entitlements as a service {#c7-entitlements-service}

The Products book's Section 5.3 decides what each plan includes and argues that a tier should be held as data, a set of **entitlements**, the features, limits and quotas a customer has paid for, so that product code checks entitlements and never tiers. This section builds the service that makes the argument true. A mapping from each plan to its entitlements is held as versioned data; each organization's effective entitlements are computed from its plan plus any contractual additions; and code asks a single question, "does this organization have this entitlement, and what is its limit?", through one client library backed by one service. Stripe's billing platform now sells the same shape as a product, a fair sign that the pattern has settled. Each entitlement also carries a contract test, of the kind Section 3.3 describes, which checks that an organization without it cannot reach the feature by any path, since an entitlement enforced on one path and forgotten on another is not enforced.

Two design choices decide whether such a service helps or harms. The first is the failure mode of each check, chosen per entitlement and written down. A check that only decides what to display, such as whether to show the resale badge in a venue's storefront, should fail open, because showing a feature briefly to someone who has not bought it costs little. A check that moves money or exposes data should fail closed, because the cost of being wrong runs the other way. The second is caching: checks sit on hot paths, so the library caches answers, with a stated bound on staleness, 60 seconds at Encore. A third question waits for Section 7.5: what happens to work already in flight when an entitlement disappears.

Verified Resale is an entitlement, and it shows why the service is more than a commercial device. Every plan on every tier includes it, as the Products book's Section 5.3{% include xref.html to="products:5.3" %} decided, so the entitlement does not distinguish one plan from another. It exists because it carries limits, such as the markets in which resale is offered, and because it has a lifecycle: an organizer whose verification has lapsed or whose account is suspended loses it, and the loss must reach every service that would otherwise list, sell or pay. If resale had been gated by a check on the plan, each of those services would have had to learn the suspension rules separately.

#### Configuration as versioned data {#c7-config-as-data}

Entitlements say what a customer may use; **configuration** says how a customer has chosen to use it. A venue's branding, its box-office hours, its refund-policy text and an organizer's resale rules are all configuration. They change often, people outside engineering set them, and each change alters a running system, so Encore treats per-tenant and per-organizer configuration as versioned data: typed by a schema, validated before it is accepted, kept with its full history, reviewed when it is risky, and attributed to the person who made it.

The best published case for this discipline is Facebook's. In "Holistic Configuration Management at Facebook" (SOSP 2015), Chunqiang Tang and his colleagues described Configerator and its companion tools, which handled thousands of configuration changes a day and trillions of configuration checks. In 2014, they reported, more engineers changed live configuration than changed the frontend product code. The paper observes that "configuration errors are a major source of site outages", citing a 2003 study by David Oppenheimer and colleagues, which found operator error, much of it in configuration, among the leading causes of failure in the services it examined. Facebook's response was to treat a configuration change "the same as a code change": it is written as source, checked by a compiler and validators, reviewed, tested and rolled out in stages. The Resilience book's Chapter 4 has already followed two recent outages that began as configuration pushed everywhere at once.

Salesforce's whitepaper made the same point from the other direction. Because its tenants' customizations were metadata, a change to one tenant required only "a simple non-blocking update to the corresponding metadata", with no deployment and no downtime. That is the power of configuration as data, and it is also its danger, since an update that requires no deployment also passes through none of a deployment's checks unless someone builds them in. Encore's configuration service, owned by Tenant Configuration, builds them in: each configuration type has a schema owned by the service that interprets it; the configuration service stores, versions, validates and rolls out every type the same way. The Resale service owns the schema and meaning of resale rules, and the configuration service carries them.

#### Rolling out configuration like code {#c7-config-rollout}

A configuration change that affects one organizer is reviewed and applied. A change to a platform-wide default, which affects every tenant or organizer at once, is a deployment and is rolled out like one. A change to a plan file, which alters the entitlements of every customer on that plan, is a deployment of this kind. Encore's progressive delivery already runs canaries at 1%, 5%, 25% and 100%, with none during on-sales (the Resilience book, Section 4.3), and configuration uses the same mechanics. What is specific to configuration is the choice of who goes first. Code canaries are slices of traffic; configuration canaries are tenants. Encore's first wave is internal test tenants, its second a few friendly customers who have agreed to receive changes early, and its later waves proceed cell by cell, with health signals computed per tenant and a rollback that restores the previous version of the configuration, which the history makes trivial.

The case for this discipline comes, fittingly, from the touchstone company itself. On 17 May 2019 Salesforce deployed a database script that, by its own statement, gave users in organizations that used or had used its Pardot marketing product "broader data access than intended". To contain the exposure, Salesforce cut off access to every organization on the affected instances, of which press reports counted more than a hundred, including many customers that had never used Pardot. Most access returned after about 15 hours, and some customers' administrators had to repair permissions by hand. A change to tenants' permissions is a change to their configuration, and it needs a wave rollout and a tested rollback like any other.

When the Resale team migrated every stored resale rule to the second version of its schema, the change went first to internal test organizers, then to two design-partner organizers who had agreed to it, then to the rest by market, with the fairness invariant tests run against each wave.

#### Organizer resale rules {#c7-resale-rules}

The resale rules are the most consequential configuration Encore holds, because they decide what fans may do with tickets they own and what the law permits in each market. The Products book's Section 5.5 explains why price caps are both a product rule and a compliance capability.

An organizer may change four things, and only in one direction. It may disable resale for an event. It may shorten the resale window, by opening it later or closing it earlier; by default the window runs from purchase until two hours before doors open. It may lower the per-fan listing and buying limits, which default to the event's own per-fan limit. And it may set a price cap below face value, where face value in these books means the original price the seller paid, primary fees included. It may never raise the cap above face value or loosen any default, and the fee is not an organizer setting at all: the buyer pays 10%, split as four points to the partner through which the buyer purchased, three to the organizer and three to Encore, and when the buyer purchases in Encore's own app Encore keeps the partner's four points. The third of Encore's fairness invariants states the rule: "Organizer caps and rules can only tighten." The schema makes that invariant structural, so that a loosening rule cannot even be expressed:

```yaml
resale_rule:                       # owned by the Resale service; stored by config
  scope: { organizer: org_m2p8, event: evt_4471 }
  effective_from: on_publish        # or a future date; never retroactive
  enabled: true                    # false not offered where law forbids blocking
  price_cap: { platform_max: face_value, organizer_pct_of_face: 90 }   # at most 100
  window: { opens_after_onsale: P7D, closes_before_doors: PT48H }  # defaults: 0 and PT2H; may only grow
  per_fan: { list_max: 2, buy_max: 2 }    # bounded above by the event's per-fan limit
  # fee split is not configurable: 4/3/3 is platform policy
  set_by: user_7c1a                # person, never a shared account
  reason: "Tour-wide policy agreed with the artist's management"
```

The law enters as bounds that differ by market. Ireland's Sale of Tickets (Cultural, Entertainment, Recreational and Sporting Events) Act 2021, in force since 31 July 2021, bans the resale of tickets above their original sale price for events at designated venues, those with a capacity of at least 1,000 whose operators have applied, and at designated events. The Act also voids terms that would block resale at or below face value, so the console offers Irish organizers only a lower cap, a window and per-fan limits, and no switch to disable resale. Where the law caps what the buyer pays in total, as it does for designated Irish events, the 10% fee comes out of the seller's proceeds. The Resale service enforces these limits whatever the console, a partner or the rule assistant sends it. The assistant, which drafts rules from an organizer's plain-language request (the Products book, Section 6.5), can express only what this schema allows, which is why a model's mistakes cannot reach a fan's price.

Every rule carries an effective date, because an organizer who tightens the window on Tuesday must not strand a fan whose listing was valid on Monday. Listings already reserved by a buyer complete under the rule in force when they were reserved, and listings that the new rule forbids are withdrawn with a message to the seller explaining why. The history of every rule is kept, so that a dispute about what the rule was on a given day is settled by a query.

#### Flags, entitlements and configuration {#c7-flags-entitlements-config}

Three mechanisms can each switch behavior on for one customer and off for another, and that resemblance is the source of a persistent confusion. A release flag can be targeted at one organizer; so can an entitlement; so can a configuration value. Used interchangeably, they produce systems in which nobody can say why a customer sees a feature, who decided it, or whether removing the switch will break a contract. Figure 7.3 separates them by purpose, owner and lifetime.

| Mechanism | Purpose | Owner | Lifetime | Encore example |
|---|---|---|---|---|
| Release flag | Hide unfinished or unproven code | The engineering team that wrote it | Weeks; removed when done | `resale-verified-flow` targeting the three launch organizers |
| Entitlement | Grant what a customer has paid for or qualifies for | Product, through the plan | As long as the plan | `verified_resale` on every organizer plan |
| Configuration | Record how a customer has chosen to use the product | The customer, or operations | As long as the customer | An organizer's resale window for one event |

*Figure 7.3 — Three switches, three owners. The confusion begins when a switch outlives its purpose and is quietly used as one of the others.*

Pete Hodgson's taxonomy of feature toggles (2017), which Section 4.5 uses, includes **permission toggles** as a fourth kind of flag: toggles that turn features on for particular users, such as premium customers. Hodgson notes that permission toggles can be very long-lived. Encore's rule is a refinement for a SaaS company: a permission toggle that will live longer than a release is an entitlement, and it moves into the entitlement service, where it acquires an owner, a plan and a place in billing. Knight Capital, which the Resilience book's Section 4.1{% include xref.html to="resilience:4.1" %} recalls, showed how dangerous a repurposed switch can be.

Encore found a quieter example of its own during the build. In the Partner Listings years, some organizers objected to "resale available at Rowmate" links on their sold-out pages, and support turned the links off for them with a release flag left over from Partner Listings' launch. By year 9 the flag was a contractual setting in all but name, with no owner and no record of who had been switched off or why. Verified Resale's migration turned each organizer's flag state into an explicit resale rule, disabling resale where the law allowed it; in Ireland, where it does not, the organizer kept the platform's rule and was told which limits it could still tighten. Each organizer received a letter explaining the change. Then the flag was deleted.

**Recap.** Entitlements are data checked through one service with a stated failure mode, and configuration is versioned, typed, attributable and rolled out in waves of tenants. Resale rules are configuration whose schema can only tighten within each market's law, and flags, entitlements and configuration keep separate owners and lifetimes.

**Exercise 7.3.** List every per-customer setting in your product and classify each as release flag, entitlement or configuration, with its owner and expected lifetime. Mark every flag older than six months that is targeted at named customers, and decide which of them is an entitlement in disguise.

### 7.4 Internal Tools

#### Internal tools have users {#c7-internal-tools-users}

Every SaaS company runs a second set of products that its customers never see: the consoles in which support agents answer cases, finance staff reconcile payouts, partner managers watch partners, and operators intervene in a tenant's affairs. These tools tend to be built last, from whatever screens already existed, and the people who use them all day learn to work around them. It shows up as slower cases, as errors made under time pressure, and as engineers who are asked to run a query in production because no tool can answer the question.

Encore treats these tools as products with users: research with the people who use them, design on the Setlist design system, and measures of task time and error. There is little published evidence specific to internal tools, and vendor surveys on the subject are marketing; the evidence for the methods comes from usability practice in general (the Products book, Section 6.3), which Section 6.2 applies to developers. When Support Tools observed agents at work, it found that they spent about a third of each case gathering context from six separate screens: the order, the payment, the ticket and its barcode history, the fan's messages, the organizer's refund policy and, after Verified Resale, the listing and its reissue. One case view, assembled from the same services and laid out in the order agents actually asked their questions, replaced the six.

#### Typed operator actions {#c7-typed-actions}

The most dangerous internal tool is the one that is not a tool at all: an engineer with a database console and good intentions. An **operator action** is an operation on a customer's state that staff perform outside the normal product flow, such as extending a hold, suspending a listing or restoring a deleted event. Encore's rule is that every operator action is a typed API call in a catalog, with a reason code, stated preconditions, a dry run and an audit entry, and that nobody runs SQL against production data.

Atlassian's outage of April 2022 is the clearest public argument for the rule, and its post-incident review is unusually candid. On 5 April, between 07:38 and 08:01 UTC, a maintenance script meant to delete a retired application, "Insight – Asset Management", from customers' sites was given a list of site identifiers instead of application identifiers. The API it called accepted either kind and gave no "warning signal to confirm the type of deletion (site or app) being requested", and it deleted 883 sites belonging to 775 customers. Restoration took up to 14 days, because Atlassian "did not have the ability to select a large set of customer sites and restore all of their inter-connected products", and data in shared stores had to be extracted by hand. Atlassian "missed our RTO but met our RPO", its recovery-time and recovery-point objectives, losing at most five minutes of data. Among its remediations were soft deletion everywhere, staged rollout of deletions, automation for restoring many sites at once, and an immediate block on bulk site deletion.

Each remediation corresponds to a property of a typed action. A typed action knows what kind of identifier it takes, so an application identifier and a site identifier cannot be confused. It checks its preconditions, so "is this an application?" is asked before anything is deleted. Its dry run shows what would change, and for destructive actions the dry run is mandatory and its result must be confirmed. And its destructive effects are soft for a retention period, as Salesforce's recycle bin was in 2008, so that a mistake can be undone by the same catalog that made it. Encore's catalog holds 40 actions, among them "suspend partner listings":

```yaml
action: partner.listings.suspend
target: { type: partner_org, id_format: "org_*", kind_must_be: partner }
scope: [all_events, event_ids]        # an empty scope is rejected, never "all"
preconditions:
  - partner.state == live
  - no_open_suspension(partner, scope)
reason_codes: [policy_breach, security_incident, partner_request]
dry_run: required                     # shows listings affected and reserved sales spared
effect: listings -> paused            # reversible; reserved listings complete
undo: partner.listings.reinstate
approval: single                      # not on the dual-control list
audit: { statement_of_reasons: true }
available_to_cue: propose_only
```

The catalog is the same one that the Operations book's Section 3.5{% include xref.html to="operations:3.5" %} describes from the operator's side, the platform-enforced list from which Cue, Encore's operations agent, may propose actions. People in the ops console and Cue draw on one catalog, and each entry states whether Cue may propose it; actions that touch a tenant's data or money are not available to Cue at all.

#### Two people, short access and the customer's consent {#c7-dual-control}

Some actions are too consequential for one person, and some access is too sensitive to be standing. Three patterns govern them, all long established. **Dual control** requires a second person to approve an action before it runs, as in the two-person rule of nuclear weapons custody or the four-eyes principle of banking. Anyone who has worked on platforms inside a bank, as I have, learns that the principle is respected only where its scope is narrow enough to be honored every time. Encore therefore applies dual control to a named list of staff actions on tenant data: impersonation of a customer's user, bulk refunds over €5,000 and changes to payout details. The refund agent's limit, which auto-approves refunds under €80 when more than 48 hours remain before the show, is a separate rule about a separate actor. A vague rule that "money actions need two people" would have collided with the refund agent on its first day.

**Time-boxed access** means that elevated access expires on its own. The Resilience book's Section 7.2 gives engineers break-glass access for 60 minutes with a second approver, and the same expiry and second person now apply to staff acting inside a tenant. The third pattern is access with the customer's consent. Salesforce lets its customers' users grant administrators or support login access for a period they choose. Microsoft's Customer Lockbox goes further: an engineer requests access with a service request number and a duration, a Microsoft manager approves, and then the customer's own approver must approve within 12 hours or the request expires; access lasts at most four hours, and every action is logged in the customer's audit log as "Microsoft Operator". Google Cloud's Access Approval follows the same shape, and so does Encore's. A support agent may view a venue's or organizer's console only with access that the customer has granted, by default for 24 hours and never more than 72, and impersonation additionally needs a second Encore approver.

The scope of consent must include what customers send to support as well as what support may view. In November 2023 Okta reported that, between 28 September and 17 October, an attacker had reached its support case system through a service account whose credentials an employee had saved to a personal Google account, most likely compromised from there, and had downloaded files associated with 134 customers. Some were HTTP Archive (HAR) files, browser recordings that contained live session tokens, and the attacker used them to hijack the sessions of five customers. The support system was a privileged system, and the files in it were credentials in all but name. Encore's case view therefore scrubs session tokens from uploaded files on arrival, and every uploaded file expires with the case.

#### Audit as a product surface {#c7-audit}

The Architecture book's Section 14.5 named the requirement: audit logs become a product surface, visible to the tenant, exportable and immutable. What remains is to design the record and the view. The catalog of security controls published by the US National Institute of Standards and Technology (NIST), SP 800-53, lists what an audit record must establish (control AU-3): what happened, when, where, from what source, with what outcome and by whom. Encore's record adds the distinction that a multi-organization system cannot do without, between the **actor**, who performed the action, and the **principal**, the organization on whose behalf it was performed.

Each of Encore's audit records therefore carries the actor (a user, a machine client or an Encore staff member), the organization the actor belongs to, the organization acted for, the action from the catalog, its target, the reason code and free-text reason, the outcome, the request identifier that joins it to traces, and the consent or approval under which it ran, if any. Records are append-only and chained to the event ledger, whose tamper evidence the Architecture book's Chapter 6{% include xref.html to="architecture:6" %} describes. They are retained for the period each customer's contract and the law require, and customers can query and export them.

The product consequence is that an organizer can see every action taken on its events, including those taken by partners and by Encore's own staff. When a support agent extended a resale listing's window for a fan at the organizer's request, the organizer's console showed it as an action by an Encore staff member, on the organizer's behalf, with the reason and the consent that allowed it. Support teams used to working out of sight find this uncomfortable at first, and enterprise customers' security reviewers ask about it before anything else.

#### Tools for running a marketplace {#c7-marketplace-tools}

Verified Resale made Encore the operator of a marketplace, and a marketplace needs a console of its own. The partner manager's console shows each partner's health (call volumes, error rates, certification status and the age of its keys), listings under review, suspensions and reinstatements, goodwill credits and refunds subject to dual control, and the dispute queue. Each control in it is a catalog action, so the console adds no power that the catalog does not already define and audit.

For resale, Encore is an online marketplace under the DSA, and three of the regulation's duties bear directly on this console: a mechanism for notices about illegal content (Article 16), a statement of reasons to anyone whose content or account is restricted (Article 17), and an internal complaint-handling system (Article 20). So a suspension records its reason in a form that can be sent to the affected party, and the dispute queue doubles as the complaint system. Fans who resell their own tickets within per-fan limits are consumers, not traders, and the regulation's trader-traceability rules in Article 30 would apply to anyone reselling as a business. That is one more reason, alongside fairness, why Verified Resale admits no professional resellers. The policy on partners' conduct belongs to Chapter 8's Section 8.3.

The first dispute in the French launch tested the console. A buyer in Lyon wrote that his reissued ticket had not appeared in his phone's wallet. From one screen the agent could see that the reissue had completed, that the seller's old barcode was on the gates' revocation lists, and that the buyer's ticket was live and rotating in the Encore app; only the convenience copy in the wallet had failed to update. The agent re-sent the pass and closed the case in four minutes.

**Recap.** Internal tools have users whose time and errors can be measured. Operator actions are typed, checked, dry-run, reversible and audited, from one catalog shared by people and Cue; dual control covers a short named list, access to a customer's data needs consent and expires, and audit records separate who acted from on whose behalf.

**Exercise 7.4.** Pick one action your support or operations team performs by hand in production. Write it as a typed catalog entry with its target type, preconditions, reason codes, dry run, undo and audit record. Then ask the person who performs it today which precondition you have missed.

### 7.5 The Tenant Lifecycle

#### A lifecycle as a state machine {#c7-lifecycle-states}

The Architecture book named the stages, onboarding, tier changes, suspension and offboarding, in its Section 14.2. Building them well means making the lifecycle explicit as a **state machine**, a fixed set of states with defined transitions between them, owned by one service, with each transition published as an event that every affected service must handle. Figure 7.4 shows Encore's.

{% include diagrams/fig-7-4.svg %}

*Figure 7.4 — Encore's tenant lifecycle, with what each state means for fans and for every service. Each transition is an event, and each consumer's handling of it is tested by contract.*

The directory owns the state, and the transitions are published as `TenantSuspended`, `TenantReinstated`, `TenantOffboardingStarted` and so on. A transition that a service ignores is a bug, and the platform finds it with a contract test: every service that holds tenant data or acts on a tenant's behalf registers, in the service registry, how it handles each transition, and a consumer-driven contract test of the kind Section 3.3 describes checks that it does so. When Verified Resale's services joined, the test failed on the first build: the Resale service did nothing on `TenantSuspended`, so a suspended venue's events would have kept accepting new listings. The fix took a day; in production, the same gap would have surfaced only when a fan complained.

Verified Resale also added a state that belongs to an event. **Resale paused** is a sub-state of an event in which existing listings are hidden and no new ones are accepted, while primary sales and valid tickets are untouched. It is entered when an organizer's rule disables resale with immediate effect, when Trust & Safety suspects a fraud pattern on one event, or when the venue or organizer selling the event is suspended. Keeping it separate from the tenant's state allows a single event to be paused without touching anything else the venue sells.

#### Upgrade and downgrade {#c7-tier-changes}

Moving between tiers has two parts that run at very different speeds. Entitlements change at once: when a self-service venue upgrades to Professional, the entitlement service reflects the new plan within its 60-second cache bound, and features appear. Placement changes slowly, because moving from a pooled self-service cell to a Professional cell with a database of its own, or back, is a data migration. The Architecture book argued that such a move must be planned and verified; here it is a workflow on the same engine as onboarding, with steps to copy the tenant's data to its new home, verify counts and checksums, switch the tenant's routing at the gateway, and keep the old copy for a reversal period. A self-service venue that upgrades sees Professional features the same afternoon and moves to its own database over the following week, scheduled around its on-sales.

A downgrade raises a harder question, because the tenant may be over the limits of its new plan. A Professional venue moving back to self-service may have more staff accounts than self-service allows, or a custom domain that self-service does not include. Encore's rule is a grace period, 60 days, during which nothing is removed and the console shows what will change and when, followed by changes that never destroy data: surplus staff accounts are disabled and kept, and the custom domain redirects to the pooled storefront for a year. It is the Products book's grandfathering with a sunset date (Section 5.5), applied to the shape of an account.

#### Suspension without collateral damage {#c7-suspension}

Suspension is the lifecycle's most delicate transition, because those who suffer from a careless one are rarely the ones being suspended: a venue may be suspended for an unpaid invoice or a breach of terms, and its fans did neither. The Products book's Section 5.4 established that suspension is a state only a person can enter, that no on-sale is stopped without a person's decision and that a suspended organizer's fans are never harmed; the Architecture book's Section 14.2{% include xref.html to="architecture:14.2" %} established that suspension blocks access without deleting anything. Encore adds the fans' side, and states it as a rule: a fan's valid ticket is never revoked because of a dispute between Encore and an organizer or a venue.

The rest follows from that rule. When a venue is suspended, tickets already sold stay valid and continue to rotate, so that the gates admit their holders. New sales stop. Resale listings for its events move to resale paused, and listings already reserved complete. Payouts to the venue are held, while payouts to fans who resold tickets proceed on their normal schedule, since the sellers are not party to the dispute. Each of those behaviors is a service's response to `TenantSuspended`, checked by the contract test described above. An organizer, though not a tenant, has a lifecycle state in the same directory, and its suspension, the case the Products book's dunning policy has in mind, triggers the same guarantees for its events.

The Salesforce incident of May 2019 shows the other side. Cutting off every organization on the affected instances was defensible as containment, but it was suspension at the scale of an instance, falling for many hours on customers who had done nothing. Encore's lifecycle is designed so that the narrowest scope is always available: one event, one tenant, one partner, or one partner on one event.

#### Export and switching {#c7-export-switching}

Every tenant will one day leave, and the law now says a good deal about how. For people, the General Data Protection Regulation (GDPR) gave a right to data portability in Article 20, covering personal data they provided where processing rests on consent or contract. For business customers of cloud and SaaS services, the EU Data Act (Regulation 2023/2854) applies from 12 September 2025, and its chapter on switching between data processing services sets clocks that a switching runbook must meet. Figure 7.5 gathers them.

| Obligation (Data Act article) | What it requires |
|---|---|
| Notice period (Art. 25) | The customer may give notice of at most two months |
| Transition (Art. 25) | Switching completes within 30 calendar days of the notice period ending |
| If 30 days is technically unfeasible (Art. 25) | Say so within 14 working days; an alternative of up to seven months, with service maintained |
| Data retrieval (Art. 25) | At least 30 calendar days after the transition |
| Scope of export (Art. 25) | An exhaustive specification of the data categories that can be ported |
| Erasure (Art. 25) | Full erasure of the customer's data after the retrieval period |
| Charges (Art. 29) | Reduced charges, at cost, until 12 January 2027; no switching charges from that date |
| Interfaces (Art. 30) | Open interfaces for portability, free of charge |

*Figure 7.5 — The Data Act's switching clocks, as a runbook must meet them. The charges row agrees with the Architecture book's Section 13.4{% include xref.html to="architecture:13.4" %}.*

The practice that satisfies those clocks is a documented export format, published in advance with the exhaustive list of data categories; a self-service export through the console and an open API; and a switching runbook run as a workflow whose timers are the clocks of Figure 7.5. Encore's export for a venue tenant includes its events, seat maps, orders, tickets with their current state, resale history and audit log. Organizers, which are not tenants, get the same export by Encore's own policy.

A venue's resale history and orders contain fans' personal data, for which the venue and Encore play different roles under the GDPR, depending on the field and the purpose. Encore's export format therefore declares, field by field, what personal data it carries and the basis on which it is transferred, and its design was reviewed with Encore's data protection officer before the first tenant used it.

#### Offboarding and erasure with evidence {#c7-offboarding}

The last transition, to closed, cannot be undone, and the quality of an erasure is invisible unless it is proved. The Architecture book's Section 14.5 explained crypto-shredding, deleting data by destroying the keys that encrypt it, and its limit: it reaches only copies encrypted under the tenant's own keys. Encore's offboarding workflow therefore begins with an inventory of every store that holds the tenant's data, drawn from the service registry, and ends only when each store has reported its erasure or its key destruction. The result is a **deletion record**, a signed document that lists each store, the method used and the time, which the departing customer's auditors can keep.

Erasure has limits set by law, and the workflow must know them. The GDPR's right to erasure does not apply where a legal obligation requires data to be kept (Article 17(3)(b)), and financial records are the usual case. Retention periods are national, and some have changed recently: in Germany, accounting vouchers fell from ten to eight years from 1 January 2025. Encore keeps such records for the statutory period of the relevant country, in a separate store under keys of their own, and erases the rest after the retrieval period the Data Act requires.

Two further practices complete the design. The first is soft deletion with a retention window before anything is destroyed, which Atlassian made universal across its products after 2022. The second is a rehearsed restore of one tenant. Restoring a whole database is a drill the Resilience book's Chapter 6{% include xref.html to="resilience:6" %} recommends; restoring one tenant from pooled storage without disturbing its neighbors is a different operation, and the one Atlassian lacked. Encore rehearses it each quarter on a self-service test tenant in a pooled cell.

When a Professional arena in the Netherlands left Encore for another provider, it had sold tickets, some of them resold and reissued, for events after its departure, and those tickets had to work. So the export included every valid ticket for future events with its current identity, and the revocation list of every barcode that reissue had killed, in the documented format that the new provider's gates could load. Encore kept serving those tickets in its app until each event had passed, and only then erased the arena's personal data on schedule and issued the deletion record.

**Recap.** The lifecycle is a state machine whose every transition is checked by contract test, and suspension never revokes a fan's valid ticket. Tier changes migrate placement with verification and downgrade with grace, export runs to the Data Act's clocks, and offboarding ends in erasure with evidence and a rehearsed single-tenant restore.

**Exercise 7.5.** Write the offboarding of one customer as workflow steps, from notice to deletion record. Mark the data you are legally required to keep and for how long, the stores that crypto-shredding would not reach, and the step at which your customer's own users, as distinct from the customer, could be harmed.

### Kata: The Inspector's Copy

> **Your brief: "Countwise."** Countwise sells stock-control and controlled-drug-register software as a service to about 4,000 independent community pharmacies in three EU countries. It has 60 engineers in eight teams. Every pharmacy is a tenant in one pooled database, onboarded by hand by a support engineer in nine days on average. A buying group of 20 member companies, which together own 140 pharmacies, wants to move all of them to Countwise this year, on four conditions: single sign-on with its own identity provider; automatic provisioning from its HR system, so that departing staff lose access the same day; one administrator who can manage all 140 pharmacies, with regional managers below her; and an audit log of every entry in each pharmacy's controlled-drug register that the national pharmacy inspectorate can read directly. Many of the group's pharmacists are locums, who work in three or four pharmacies a week. Last year two departing pharmacies asked for their data; each export took three weeks of hand-written SQL, and one lacked its register history. The Data Act now sets the clocks for any pharmacy that leaves. Leadership can spare eight engineers for two quarters.

**Deliverables:**

1. **Tenant directory** — The record that makes each pharmacy, member company and the buying group an organization, the events it publishes, and the services that must stop keeping their own copy.
2. **Onboarding workflow and activation** — The steps from contract to first register entry, with preconditions, checked results and compensations, the human steps with owners, and the activation event that stops the clock.
3. **Identity model** — Memberships and roles for locums, an active-organization rule, SSO with domain verification and a recovery owner, a deprovisioning target that includes open sessions, and delegated administration over the group's hierarchy.
4. **Audit and inspector access** — The audit record, distinguishing actor from principal, and a design for the inspectorate's access that requires the pharmacy's consent, expires, and appears in the pharmacy's own log.
5. **Operator actions** — Three actions that support performs by hand today, rewritten as typed catalog entries with preconditions, dry runs and undo, and which of them need a second person.
6. **Offboarding and switching runbook** — The export format and its data categories, the Data Act clocks as workflow timers, how controlled-drug records are kept for the statutory period, and the deletion record.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| One record of truth | Can any service answer "who is this pharmacy and where does it live?" from one directory, without a copy of its own? |
| The customer's measure | Does the activation metric count real value to the pharmacy, and does the funnel show where pharmacies stall, whatever the workflow's own speed? |
| People who belong to several customers | Can a locum work in four pharmacies in a week, with the right role in each, and lose all access within minutes when the group removes her? |
| Consent and evidence | Could the inspectorate read a register's history without Countwise staff seeing anything the pharmacy did not allow, and would the pharmacy see every access? |
| Typed and reversible | Is there any remaining path by which a person changes production data without a typed action, a dry run and an audit record? |
| A lawful exit | Would a departing pharmacy get a complete export within the Data Act's clocks, with its register history intact and its erasure proved? |

#### Where you now stand

You can now build the control plane that a SaaS architecture only sketches: a directory of every organization, onboarding measured by the customer's success, an identity model in which people belong to several customers and leave cleanly, entitlements and configuration rolled out like code, internal tools that are typed and audited, and a lifecycle that suspends without harming the innocent and lets customers leave with proof of erasure. Verified Resale tested each of these with organizations that are neither tenants nor organizers, the partners whose machines call Encore's API every minute. Those partners are the beginning of something larger. Once other companies build their businesses on Encore's resale pool, Encore is running an ecosystem as well as selling a product, with a marketplace to design, a partner program to govern and economics to keep honest, and inside the company the same question arises about code that many teams share. Chapter 8 takes up business platforms, partners and InnerSource.

### References

- Craig D. Weissman, Steve Bobrowski — [*The Design of the Force.com Multitenant Internet Application Development Platform*](https://doi.org/10.1145/1559845.1559942). Proceedings of ACM SIGMOD, 2009.
- salesforce.com — [*The Force.com Multitenant Architecture: Understanding the Design of Salesforce.com's Internet Application Development Platform*](http://developerforce.s3.amazonaws.com/whitepapers/WP_Force-MT_101508_PRINT.pdf). Whitepaper, 2008 — free online.
- Tod Golding — [*Building Multi-Tenant SaaS Architectures*](https://www.oreilly.com/library/view/building-multi-tenant-saas/9781098140632/). O'Reilly, 2024.
- Atlassian — [*Post-Incident Review on the Atlassian April 2022 Outage*](https://www.atlassian.com/engineering/post-incident-review-april-2022-outage). Atlassian Engineering, 2022 — free online.
- European Parliament and Council — [*Regulation (EU) 2023/2854 (Data Act)*](https://eur-lex.europa.eu/eli/reg/2023/2854/oj). Official Journal of the EU, 2023 — free online.
- Chunqiang Tang, Thawan Kooburat, Pradeep Venkat, Akshay Chander, Zhe Wen, Aravind Narayanan, Patrick Dowell, Robert Karl — [*Holistic Configuration Management at Facebook*](https://doi.org/10.1145/2815400.2815401). Proceedings of SOSP, 2015.
- Ruoming Pang et al. — [*Zanzibar: Google's Consistent, Global Authorization System*](https://www.usenix.org/conference/atc19/presentation/pang). USENIX ATC, 2019 — free online.
- P. Hunt (ed.), K. Grizzle, M. Ansari, E. Wahlstroem, C. Mortimore — [*RFC 7644: System for Cross-domain Identity Management: Protocol*](https://www.rfc-editor.org/rfc/rfc7644). IETF, 2015 — free online.
- P. Hunt (ed.), K. Grizzle, E. Wahlstroem, C. Mortimore — [*RFC 7643: System for Cross-domain Identity Management: Core Schema*](https://www.rfc-editor.org/rfc/rfc7643). IETF, 2015 — free online.
- Microsoft — [*Customer Lockbox requests*](https://learn.microsoft.com/en-us/purview/customer-lockbox-requests). Microsoft Learn — free online.
- Okta Security — [*Unauthorized Access to Okta's Support Case Management System: Root Cause and Remediation*](https://sec.okta.com/articles/2023/11/unauthorized-access-oktas-support-case-management-system-root-cause/). Okta, 2023 — free online.
- Hector Garcia-Molina, Kenneth Salem — [*Sagas*](https://doi.org/10.1145/38713.38742). Proceedings of ACM SIGMOD, 1987.
- Oireachtas — [*Sale of Tickets (Cultural, Entertainment, Recreational and Sporting Events) Act 2021*](https://www.irishstatutebook.ie/eli/2021/act/21/enacted/en/html). Irish Statute Book, 2021 — free online.
- European Parliament and Council — [*Regulation (EU) 2022/2065 (Digital Services Act)*](https://eur-lex.europa.eu/eli/reg/2022/2065/oj). Official Journal of the EU, 2022 — free online.
- David Oppenheimer, Archana Ganapathi, David A. Patterson — [*Why Do Internet Services Fail, and What Can Be Done About It?*](https://www.usenix.org/conference/usits-03/why-do-internet-services-fail-and-what-can-be-done-about-it). USENIX USITS, 2003 — free online.
- Pete Hodgson — [*Feature Toggles (aka Feature Flags)*](https://martinfowler.com/articles/feature-toggles.html). martinfowler.com, 2017 — free online.

---

## Chapter 8: Ecosystems — Business Platforms, Partners, and InnerSource {#ch8}

> "The various members also compete vigorously against one another to issue cards and sign merchants." — U.S. Court of Appeals for the Eleventh Circuit, *NaBanco v. Visa* (1986)

Until Verified Resale, almost everything Encore built was something Encore itself sold, to fans, organizers and venues, and in each case one party made a promise and the other relied on it. Verified Resale changes the shape of that promise. A fan sells to another fan, through a partner that in other markets is Encore's competitor, under rules an organizer has set, and Encore's job is to make the exchange safe for people who have no reason to trust one another. The engineering question changes with it. When a product becomes a place where others do business, what must the system itself enforce, and who pays for the parts that everyone shares?

The question is older than software, and its best answer came from banking. Half a century ago a group of rival banks agreed to run one card network under one set of rules, with a fee they had set together, while they went on competing for every cardholder and every merchant. Dee Hock's National BankAmericard Inc. is this chapter's touchstone, and Section 8.1 tells its story, because the shape it found, rivals selling through one system under shared rules with the money divided by a default nobody has to negotiate, is the shape of Verified Resale.

We meet Encore at the point where that shape has been tested. The Products book's Chapter 2 chose the market and its sides, and its Chapter 10 followed the bet from memo to launch. At month 12 Verified Resale went live with three design-partner organizers, one partner, Rowmate, and one market, France. Tessera was certified around month 15 and went live soon after, and at the month-18 review there are two partners and no kill criterion has fired. This chapter covers the marketplace rules as the system enforces them (Sections 8.1 and 8.2), the partner program (Section 8.3), and two kinds of sharing inside Encore: code that six teams change together (Section 8.4) and the costs of both of Encore's platforms (Section 8.5).

### 8.1 From Product to Platform

#### The banks that agreed to compete {#c8-bankamericard}

Bank of America launched BankAmericard in California in 1958, and in 1966 it began licensing the card to banks across the United States. The licensing created what the Eleventh Circuit would later describe as a four-party system: the cardholder, the bank that issued the card, the merchant, and the merchant's bank. Each purchase crossed from one bank to another, and each pair of banks settled the other's paper on terms negotiated between the two of them. The court's phrase for it is that the "variable interchange fee system" stopped working well, and the licensees, struggling with fraud, failed credit controls and slow clearing, blamed one another for all three.

Dee Hock was running the card operation of the National Bank of Commerce in Seattle, one of the early licensees, when the arrangement reached its crisis. At a contentious licensee meeting in Columbus, Ohio, in 1968, he argued for restructuring and was put at the head of a committee to address the problems. In 1969 he gathered a hand-picked group of bankers at a hotel in Sausalito, California, to design a new organization, and in 1970 Bank of America gave up control of the program. The issuing banks formed **National BankAmericard Inc. (NBI)**, which the court later described as "a for-profit nonstock-membership corporation", with Hock as its first president and chief executive. The banks owned the network and made its rules together, and they went on competing for customers as fiercely as before.

Late in 1971 NBI's board did something that looks small and was not. It adopted a uniform fee, set by the network and paid by the merchant's bank to the card's issuer on every transaction that cleared through NBI's system, to carry part of the issuer's costs: credit losses, the interest-free period, and the fact that cardholders paid no fee. The fee was a default. Members could bypass the network's clearing and negotiate other rates privately, but the default spared them from having to negotiate at all. In 1973 Hock pushed through VisaNet, the electronic system for authorization and clearing, and in 1976 the organization took the name Visa. Hock resigned in 1984, later told the story in *Birth of the Chaordic Age* (1999), reissued with new chapters as *One from Many* (2005), and died in 2022. Figure 8.1 draws the system the banks built and the road from licensees to Visa.

{% include diagrams/fig-8-1.svg %}

*Figure 8.1 — The four-party system under NBI. The charge cleared through the network, and the fee ran the other way, from the merchant's bank to the issuer, at a rate the network set and any two banks could still replace by private agreement.*

Three things in the story carry straight across to Verified Resale. The first is that rivals can sell through one system when the rules are shared and the network, not each member, enforces them. The court named the prize "universality of acceptance — the key element to a national payment system", and Verified Resale's prize is the same in miniature: a reissued ticket must work at every gate, whichever partner sold it. The second is that a network-set default for dividing money removes a whole class of negotiation, which is what Encore's fixed split of the buyer's fee does. The third is less comfortable. Shared rules about price attract regulators. NaBanco, a merchant processor, sued in 1979, claiming the fee was horizontal price-fixing; the district court found for Visa in 1984, and in January 1986 the Eleventh Circuit affirmed, calling the fee "an internal control mechanism" of a joint venture. Decades later the European Union (EU) capped consumer interchange at 0.2% for debit cards and 0.3% for credit cards. A rule that sets a price must be defensible in public, because sooner or later someone will ask it to defend itself.

The parallel has a limit, and the limit teaches as much as the parallel. The banks owned NBI. Rowmate and Tessera own nothing of Encore, and Encore is both the network and one of the channels, since fans can also buy resale tickets in Encore's own app. A network owned by its members can claim neutrality by construction. A network owned by one participant has to earn it with rules it publishes and data it refuses to share, which is much of what Section 8.3 is about.

#### Three kinds of platform {#c8-platform-types}

The word "platform" covers several different businesses, and confusing them leads to building the wrong governance. Cusumano, Gawer and Yoffie, in *The Business of Platforms* (2019), separate two kinds. A **transaction platform** is an intermediary that matches parties who want to exchange something, such as buyers and sellers, riders and drivers, or fans and fans. An **innovation platform** is a foundation on which other companies build complementary products, such as an operating system and its applications. Their chapter on the subject is titled "Innovation, Transaction, or Hybrid", and its argument is that the most valuable platform firms tend to be **hybrids**, companies that run both kinds at once.

Each kind makes different demands on design and governance. A transaction platform lives or dies on matching and trust: whether a buyer finds a seller, and whether both believe the exchange will be honest. Its rules govern conduct. An innovation platform lives or dies on the stability of what others build on: whether its interfaces hold still long enough to be worth building on, whether its documentation is good, and whether its owner will compete with the complements. Its rules govern change.

Verified Resale is a transaction platform, and Encore's partner application programming interface (API) makes it a narrow hybrid. Partners build storefronts on Encore's interfaces, so the innovation side's demands apply to them: the 12 months' notice of breaking changes, the sandbox, the developer experience that the Products book's Section 9.4{% include xref.html to="products:9.4" %} designs. But partners build only storefronts. They cannot build new kinds of exchange, new rules or new ways to move money, and that narrowness is deliberate. It means the governance Encore must invent is mostly transaction governance, and the innovation governance it needs already exists in its public API program (the Architecture book{% include xref.html to="architecture" %}, Section 7.5).

#### The core interaction, written into the system {#c8-core-interaction}

The Products book's Section 2.3 teaches the core interaction, the single exchange a platform exists to make happen, described by its participants, its unit of value and the filter that matches one to the other. Here we take the result as given and ask what it does to the code. Encore's design reviews for resale begin from one sentence, which the Resale team wrote at month 4 and has changed only once:

*A screened fan buys, through any authorized channel, a listing that is tied to one real ticket bought through the Gate, at no more than the price its seller paid, and receives that ticket reissued in their own name.*

Each phrase in the sentence maps to a component and an owner. "A screened fan" is Bot Screening and the per-buyer limits. "Any authorized channel" is the partner program and the listing pool, which shows every listing on Encore's app and on every partner. "Tied to one real ticket" is the listing's reference to a ticket identity held by Seat Inventory & Ticketing, which makes a listing for a ticket nobody holds impossible to create. "At no more than the price its seller paid" is the cap, enforced by the Resale service. "Reissued in their own name" is the Inventory team's reissue, which Section 8.2 examines. A proposal that cannot say which phrase it touches is either outside the product or a sign that the sentence is incomplete, and the one change to the sentence came from exactly such a proposal, when Ireland's law forced the team to separate "the price its seller paid" from "what the buyer pays". The same test screens out features that would make the market busier without making the exchange safer, since such features touch no phrase at all.

#### How far to open, and when {#c8-openness}

Openness is a set of levers, and Parker, Van Alstyne and Choudary devote a chapter of *Platform Revolution* (2016) to them. A platform decides who may join, what they may build, and what they may see, and the third lever covers data and access to participants as much as it covers interfaces. The Products book's Section 2.4 treats openness as a strategic choice. The engineering concern is the sequence in which the levers move and the mechanisms that hold them in place: credential scopes, partner tiers, and contracts.

Encore's history shows what happens when the levers are set in the wrong combination. From year 6, under "Partner Listings", partners could post resale offers that appeared as links on sold-out event pages, but the ticket changed hands outside Encore, and Encore checked nothing beyond the partner's word. Partner Listings was open on exactly the lever that should have been closed, what partners could assert, and closed on the lever that mattered to fans, whether the ticket was real. When Rowmate's long-lived key leaked, the two fraudulent listings it produced were possible only because of that combination (the Resilience book{% include xref.html to="resilience" %}, Section 7.2). Verified Resale reverses it. Partners may assert almost nothing, since every listing is checked against a real ticket and every sale is settled by Encore, while fans gain many more places to buy.

The sequence matters as much as the setting. Cusumano and his co-authors list mistiming and hubris among the common platform mistakes, and both describe the temptation to open everything on the first day. Encore opened in three steps: a closed pilot with Rowmate, then partners admitted through certification, and never an open resale API that anyone could call. Ticketmaster showed the same instinct under regulatory pressure: on 13 August 2018 it closed its secondary sites, Seatwave and Get Me In!, across Europe, and replaced them with fan-to-fan resale at face value or less inside its primary site.

A festival site is a fair picture of the levers. Wristbands of different colors decide who may enter the arena, the pit or the backstage area, and stewards check them at each boundary. Scopes on a partner's credentials do the same work at the gateway. The picture breaks at judgment. A steward can recognize that a wristband looks wrong and ask a question; a gateway enforces exactly what the scope says and nothing else. So the scopes must be drawn on the assumption that no person will ever review an individual request.

#### Fairness as invariants {#c8-fairness-invariants}

The Products book's Chapter 2 made fairness Encore's strategy for resale, and this book's Section 1.3 restated it as five invariants that the code must keep. A **design invariant** is a property the system must keep in every state it can reach, enforced at one named place and proved by a test that runs on every change. Each part prevents a failure: "every state" rules out invariants that break during retries, "one named place" rules out enforcement smeared across services where each team assumes another is checking, and "a test on every change" rules out slow drift. Chapter 3 builds the tests, mostly as property-based tests; Figure 8.2 records where each invariant is enforced in the running system.

| Invariant (Section 1.3) | Where the system enforces it | Owner |
|---|---|---|
| 1. Partners never buy primary tickets. | Partner credentials carry no purchase scope; Seat Inventory refuses holds from any partner principal | Security Engineering, Inventory |
| 2. Only tickets bought through the Gate, within the per-fan limit, can be listed. | The Resale service checks the ticket's order provenance and the seller's listing count when a listing is created | Resale |
| 3. Organizer caps and rules can only tighten. | The rule schema accepts only values at or inside the platform defaults; the validator rejects anything looser | Resale |
| 4. Every resale buyer passes Bot Screening and the per-buyer limits. | Resale checkout passes through Bot Screening and the per-buyer limit check before a listing is reserved | Bot Screening, Resale |
| 5. Partners never see sales-velocity data. | Partner responses are built from the same coarsened availability everyone receives; a contract test fails any partner-facing field tagged as velocity | Partner APIs |

*Figure 8.2 — The five fairness invariants and the single place each is enforced. Other services may check again, but each invariant has one owner.*

Building codes are the right comparison, and they are older than any of our methods. A city does not rely on each builder's goodwill to keep a stairwell wide enough; it writes the requirement down, names the inspection at which it is checked, and refuses occupancy until it passes. The comparison breaks in our favor. A building inspector visits a few times during construction, and a building can drift out of compliance for years between inspections. An invariant test runs on every change, so the system can never be further than one change away from proof.

The law sits beside the invariants without commanding them. The EU's Omnibus Directive (2019/2161) added to the list of commercial practices always considered unfair the resale of event tickets to consumers by a trader who acquired them using automated means to get around limits on the number of tickets per person or other purchase rules, and Member States have applied it since 28 May 2022. The prohibition binds the trader who resells. It does not require Encore's design, and the invariants are Encore's own commitments. What invariants 2 and 4 do is make it hard for anyone selling through Encore to break the Directive by accident, since a ticket bought by circumventing the Gate's limits cannot be listed at all.

#### What Encore keeps {#c8-build-buy-belong}

Cusumano and his co-authors frame an incumbent's choice when platforms arrive as build, buy or belong: build a platform of its own, buy one, or join someone else's. Encore's answer is a blend, and the line through it is drawn by what must be true at the gate. Encore builds and keeps the system of record for ticket identity, the reissue that changes it, and the ledger that records the money. It belongs to its partners' audiences, letting Rowmate and Tessera be storefronts with their own buyers, discovery and marketing. Ticketmaster's 2018 move followed the same logic, whatever its motives: resale moved inside the system that issues tickets, which is the only system that can guarantee them. The general economics of building and buying belong to the Architecture book's Chapter 13{% include xref.html to="architecture:13" %}, and the positioning of each capability on a Wardley map to the Products book's Section 2.4{% include xref.html to="products:2.4" %}. The narrower point here is that a transaction platform should own whatever makes the transaction trustworthy, and should be content to let others own whatever makes it convenient.

**Recap.** National BankAmericard showed that rivals can sell through one system when the network sets and enforces shared rules, with a default division of money that nobody has to negotiate, and that rules about price must be defensible in public. Verified Resale is a transaction platform with a narrow innovation side, so its governance is mostly about conduct. Its core interaction is written as one sentence whose phrases map to owners, its openness is set lever by lever and in sequence, and its fairness is a set of invariants, each enforced in one place and tested on every change.

**Exercise 8.1.** Write your product's core interaction in one sentence that names the participants, the unit of value and the filter. Under each phrase, name the component and the team that make it true. Then list the invariants that keep the exchange fair, and for each one name the single place it is enforced. If you cannot name one place, you have found your first piece of work.

### 8.2 Designing a Marketplace

#### Measuring liquidity {#c8-liquidity}

The Products book's Section 2.3 explains why most matchmakers fail, in Evans and Schmalensee's phrase from *Matchmakers* (2016), because they "ignite or fizzle": they never reach enough participants on both sides at once. It also chose Encore's ignition plan, which piggybacks on fans Encore already has and on buyers Rowmate already has. What that section leaves to engineering is measurement, because a marketplace that cannot see its own liquidity cannot tell ignition from a slow fizzle until it is too late.

For Encore, **liquidity** is the likelihood that a listing finds a buyer before it can no longer be used. The general idea is common to every marketplace, but the measures are Encore's own choice, and two of them do most of the work. The first is the share of listings sold before the resale window closes, two hours before doors. The second is the median time from listing to sale. The first tells Encore whether sellers are being rescued; the second tells it whether buyers are finding listings while they still care. Both are computed per event class, since a stadium show and a 400-capacity club behave as different markets: the stadium has thousands of listings and thousands of buyers, while the club may have three listings and no buyers at all.

An unsold listing is a broken promise: the fan is out of pocket and cannot attend. The Resale team's first live-quarter key result was that at least 55% of listings sell before the window closes, and Encore watches that number for events above 5,000 capacity, setting no target for small venues, where the market may simply be too thin. It also built one seeding mechanism that the Products book's Section 2.3{% include xref.html to="products:2.3" %} did not need to describe. When a fan asks Support for a refund that the policy does not allow, the reply offers to list the ticket on Verified Resale, which turns a refusal into a listing and adds supply exactly where demand for refunds signals that some fans can no longer go.

#### The listing lifecycle {#c8-listing-lifecycle}

Evans and Schmalensee call the design of a marketplace's rules its "interior design", and their point is that the rules are part of the product, as much as any screen. In software the rules attach most naturally to transitions. A listing is a small state machine, shown in Figure 8.3, and each transition is the moment at which some rule is checked and some team's code runs. Modeling a lifecycle as a state machine with guarded transitions is long industry practice; its value here is that it forces the organizer's rules (Section 7.3) and the platform's rules to be checked at named moments, where they can be tested, and nowhere else.

{% include diagrams/fig-8-3.svg %}

*Figure 8.3 — The listing state machine. Every rule is checked on a transition; partners are told of every transition by webhook and reconcile their copies hourly.*

Two details of the figure deserve a closer look. The first is the window's close. Encore ends resale two hours before doors, by default, so that reissue, delivery to the buyer's phone and the update of every gate's revocation list can finish while there is still time to fix anything that goes wrong; organizers may shorten the window but cannot lengthen it. The second is the "withdrawn" transition, which is where rule changes bite. When an organizer lowers a cap below the price of an existing listing, the listing is withdrawn and the seller is invited to list again at the new price. The alternative, letting old listings keep their old terms, would quietly turn a tightening rule into a loosening one for everyone who listed early, which is precisely the kind of exception that invariant 3 exists to forbid. Partners hold copies of listings, and copies drift, so every transition is published to them and they reconcile on a schedule, as the Products book's Section 9.5{% include xref.html to="products:9.5" %} designs.

#### Reissue as the trust mechanism {#c8-reissue}

**Reissue** is the step that, on every resale, voids the seller's ticket identity and issues a new one to the buyer, as one atomic operation inside Seat Inventory & Ticketing. The Inventory team owns issuance and revocation, and the Resale service calls it; Section 9.5 tells how a request for comments (RFC) and an architecture decision record settled that ownership. Two mechanisms make the old identity worthless. Every mobile ticket at Encore already carries a rotating barcode, generated on the phone from a per-ticket secret, so a screenshot stops working within seconds; reissue goes further by changing the ticket identity behind the barcode. And the old identity joins the revocation lists that every venue scanner holds for offline validation, so even a device that has not heard the news refuses the seller's old ticket. Wallet passes are updated too, but wallet updates are best effort, and Apple Wallet passes at Encore do not rotate, so the guarantee is the revocation list at the gate (the Products book's Section 8.3{% include xref.html to="products:8.3" %} covers the phone).

The design has a well-documented precedent. In May 2019 Ticketmaster announced SafeTix, a ticket whose encrypted barcode refreshes every few seconds and is tied to the holder's account and phone, and on transfer the recipient receives a new ticket. It went into production at scale that year, starting with National Football League stadiums for the 2019 season and selected tours. The precedent also shows the cost. At a Black Keys show at the Wiltern in Los Angeles in September 2019, fans who did not have the rotating ticket on their phones were refused entry, and the episode became a public lesson in what phone-only entry demands of fans and of gate staff. Rotating credentials are proven, but the gate and its staff have to be ready for them.

Reissue also closes a door that regulators have had to close by force elsewhere. A listing in Verified Resale references a ticket identity that exists and belongs to the seller, so a speculative listing, an offer to sell a ticket the seller does not yet hold, cannot be created. In the United Kingdom, the Competition and Markets Authority (CMA) secured a court order against viagogo in November 2018 that required it, among other things, to prevent the sale of tickets a seller does not own and may not be able to supply. In July 2019 the CMA said it would seek contempt proceedings for non-compliance, and it suspended them in September 2019 after viagogo addressed the outstanding issues. Encore sells only in the EU, so the case is context, but its lesson is general: a rule that a platform must police listing by listing is far weaker than a structure in which the forbidden listing cannot exist. Partner Listings, the year-6 predecessor, had sold the same barcode to several buyers, and that was the first line of the bet memo's diagnosis.

The box office returns desk is the oldest version of the mechanism. A theater that accepts returned tickets takes the old ticket back across the counter, tears it, and sells a new one for the same seat, and the house guarantees the new ticket because it issued it. Reissue is that desk at the scale of a continent, with partners in place of the counter. The comparison breaks on the torn ticket. At the returns desk the old ticket is physically destroyed in front of the clerk; in software the old identity survives on the seller's phone and in every screenshot, and only the revocation list at every gate makes it worthless. That is why revocation, more than issuance, is the part of reissue the Inventory team tests hardest.

#### Money flows and fee sharing {#c8-money-flows}

The money in a resale moves among more parties than in a primary sale, and law governs its flow as much as convenience does. The resale price is capped at what the seller originally paid, including primary fees, which these books call face value. The buyer pays a 10% service fee on top, shown in the all-in price from the first screen. Of that fee, 4 points go to the partner through which the buyer purchased, 3 to the organizer and 3 to Encore; when the buyer purchases in Encore's own app, Encore keeps the partner's 4 points as well. Encore's points carry the payment fees, fraud losses and support costs. The seller receives the resale price in full, five days after the event, when the ticket is no longer at risk of a dispute.

Who holds the buyer's money during those days is the question that shapes the system. The revised Payment Services Directive (PSD2, Directive 2015/2366) excludes from its scope payments made through a commercial agent authorized to negotiate or conclude a sale on behalf of only the payer or only the payee (Article 3(b)). Its recital 11 explains that an agent acting for both sides is excluded only if it never, at any time, enters into possession or control of the client's funds, and the European Banking Authority's answer to question 2020_5355, final in December 2021, adds that national authorities decide each case from the business model. In fan-to-fan resale Encore serves the selling fan and the buying fan alike, so the one-sided route very probably does not apply, and the both-sides route applies only if Encore never holds the money. The details are for counsel, but the consequence is plain: if Encore held sellers' proceeds in its own account, it would need to be a licensed payment institution.

There are two proven ways out, and both have public examples. A marketplace can use a licensed PSP's marketplace product, in which the PSP verifies the sellers, holds the funds in accounts in their names, delays payouts and splits each payment. Or it can become licensed itself, as eBay did after announcing in February 2018 that it would move its marketplace payments off PayPal to a system it managed, which in Europe runs through an eBay entity authorized as a payment institution in Luxembourg. Encore took the first route. Resale payments and payouts run through its primary PSP's split-payment product; the seller's proceeds sit at the PSP and are released on the payout date, and the 10% fee goes to Encore. The organizer's 3 points and the partner's 4 are then Encore's own commercial obligations, paid out of its fee revenue, the organizer's with the regular organizer payouts by Billing & Payouts and the partner's on a monthly statement. Paying a commission from one's own revenue is not a payment service. The law is still moving: the EU's Payment Services Regulation and a third directive were provisionally agreed on 27 November 2025 and are close to adoption, and the exclusion for commercial agents is expected to narrow further, which is one more reason to keep Encore out of the flow of funds.

The choice has a price, and Encore wrote it into the decision record rather than discovering it later. Encore has two PSPs behind its anti-corruption layer, and its primary sales fail over from one to the other. Only the primary PSP carries resale, because the split-payment integration exists only there. When the primary PSP is degraded, primary sales move to the secondary and resale checkout pauses; listings stay listed, and buyers are told to try again shortly. It is a documented limitation with an owner and a review date, debt of the recorded kind Chapter 2 describes.

Touring has an old ritual for this. After each show the promoter and the tour manager sit down for the settlement, count the box office, deduct the agreed costs and split the rest, and nobody is paid until the numbers are known. Encore's five-day payout is a settlement of that kind. The analogy breaks at the cash box. In a tour settlement the promoter holds the money and pays it out; in Verified Resale the law requires that Encore never hold it, so Encore keeps the count while the PSP keeps the cash.

Keeping the count is still hard work. Every resale writes entries in the finance ledger (the Architecture book, Section 9.1), and a reconciliation each day compares three records that must agree: the PSP's settlement report, the ledger and the partners' statements. One resale of a €60 ticket bought through Rowmate leaves this trace:

```text
resale_sale   ticket T-48213 reissued as T-91770   channel: rowmate
  buyer_paid             66.00  held by primary PSP, split at capture
  seller_proceeds        60.00  seller's PSP account; release five days after the event
  service_fee             6.00  Encore's PSP account
    partner_commission    2.40  accrued; payable on monthly statement
    organizer_share       1.80  accrued; paid with organizer payout
    encore_retained       1.80  carries PSP fees, fraud and support
  release_trigger        five days after the event, if no dispute is open
  reversal_rule          chargeback before release: reverse all lines
```

Where the law caps the buyer's total, as Ireland's Sale of Tickets Act 2021 does for designated events, the buyer pays €60, the 10% fee is taken from the seller's proceeds, and the split is unchanged. The ledger shows that case as a different `seller_proceeds` line and nothing else, which is a small sign that the model is right.

#### Fakesters and fraudsters {#c8-fraud}

Every marketplace attracts people who want to cheat it, and Evans and Schmalensee devote a chapter (Chapter 9 of *Matchmakers*) to the "fakesters" and "fraudsters" that every matchmaker must keep out. Encore's resale fraud falls into four kinds. Stolen cards buy resale tickets, and the real cardholder later reverses the charge. An attacker takes over a fan's account, lists the fan's ticket and changes the payout account to their own. A seller and buyer agree on a side payment off the platform to get around the cap. And a trader poses as a fan, listing far more tickets than any fan buys.

The controls are standard ones, applied at the transitions of Figure 8.3. The payout five days after the event is a hold that lets most card disputes surface before any money leaves. Velocity rules, written by Trust & Safety, watch how many listings an account creates and how fast. Step-up authentication is required before listing and before any change to a payout account. Encore's first real fraud pattern after launch was a listing created within minutes of a password reset, followed by a change of payout account, and the rule written for it now requires step-up sign-in and a review by Trust & Safety whenever a listing follows a credential change within 24 hours. For traders, the law adds a duty as well as a motive. The Digital Services Act (Regulation 2022/2065) requires online marketplaces to collect and check identifying information from traders before letting them sell to consumers (Article 30), and since the Omnibus Directive marketplaces must tell consumers whether a seller is a trader. Encore admits no professional resellers at all, so its rule detects accounts that behave like traders, more than 20 tickets listed across more than four events in 12 months, and stops them listing until a person has reviewed the account.

Chargebacks need their own procedure. A buyer can attend a show and then tell the card issuer the ticket never arrived. A card-scheme dispute has deadlines, and a marketplace that cannot answer in time loses by default. Encore's strongest evidence is the scan at the gate, which shows that the reissued ticket was used, at which door and when. Trust & Safety assembles the evidence automatically from the ledger and the scan records, and the policy on who bears the loss is written down: a chargeback that arrives before the seller is paid reverses the sale from the held proceeds, and one that arrives after is Encore's loss unless the seller's own fraud is shown.

Reputation is the classic marketplace defense, and the best evidence for its value comes from eBay. Paul Resnick, Richard Zeckhauser, John Swanson and Kate Lockwood ran what they described as the first randomized controlled field experiment of an internet reputation system, published in 2006. An established seller with a strong reputation sold matched lots of vintage postcards under his own identity and under new ones, and buyers paid 8.1% more to the established identity; one or two negative ratings on the new identities had no measurable effect. The experiment shows that buyers pay for a seller's history when they bear the risk of the seller. Verified Resale removes most of that risk, since the buyer's ticket is reissued and guaranteed whatever the seller's history, and so Encore deliberately builds no seller ratings. The reputation that matters in its market is the partners', and Encore tracks it as dispute rates per partner that feed the enforcement described in Section 8.3. Bot Screening's operation belongs to the Resilience book's Section 1.3{% include xref.html to="resilience:1.3" %}.

**Recap.** Liquidity needs measures of its own, chosen per event class, because an unsold listing breaks a promise to the seller. Rules belong on the transitions of an explicit listing lifecycle, where each is checked once and tested. Reissue, with revocation at every gate, is the mechanism that makes a resold ticket trustworthy and speculative listings impossible. Under PSD2 a marketplace that serves both sides must never hold the buyer's money, so the funds flow through a PSP's marketplace product while Encore keeps the ledger, and the fraud controls sit at the same transitions as the rules.

**Exercise 8.2.** Draw your marketplace's listing state machine as Figure 8.3 draws Encore's. Mark the transition at which each rule and each fraud control applies, and name its owner. Then trace one payment from buyer to seller and write down, for every day the money is in flight, whose account it sits in. If any of those accounts is yours, take the question to counsel before you build further.

### 8.3 Partner Programs

#### A program around an API {#c8-partner-program}

An API lets a partner call a system; a program lets a partner build a business on it. A **partner program** is the agreement, tiers, enablement, review, support and change management that a company wraps around an API product so that other businesses can depend on it safely. Medjaoui, Wilde, Mitra and Amundsen, in *Continuous API Management* (second edition, 2021), describe the pillars of an API product and its lifecycle; the Products book's Section 9.4{% include xref.html to="products:9.4" %} applies the lifecycle to Encore's partner API, and the Architecture book's Section 7.5{% include xref.html to="architecture:7.5" %} measures the developer's first call. At Encore the program is jointly owned: the Partner APIs team runs the technical side, from sandbox to certification to credentials, and a partner manager who works with the Resale team's product trio owns the agreements and the relationships.

The "Verified Resale Partner" program has one tier at launch, because two partners do not justify a hierarchy, and every partner signs the same terms. What a well-run program adds beyond the agreement is operational communication. Partners receive the on-sale calendar, since they are rate-limited per partner during major sales and should know when; they receive incident notices from the same status page fans see; and they receive a change calendar that shows every planned change to the partner API months ahead.

Airlines offer a fair analogy. A codeshare lets one airline sell seats on a flight another airline operates, under the operating carrier's rules for safety, baggage and boarding, with the revenue divided by agreement. The selling airline owns the customer relationship; the operating airline owns everything that must be true for the flight to happen. The analogy fails on scale: codeshare partners are usually peers with flights of their own, while Rowmate and Tessera depend on Encore entirely for this product, which obliges Encore to change its rules slowly and in public.

#### Vetting and onboarding partners {#c8-partner-onboarding}

Admitting a partner is a workflow with four parts: verifying the business (know-your-business checks), meeting any registration a market requires, completing a security questionnaire, and signing the contract. Encore runs it on the same durable-workflow rails that onboard tenants (Section 7.1), with each step idempotent, owned and visible, and with the human steps carrying owners and deadlines. Two credentials come out of it at different times. Sandbox credentials are issued the day the workflow starts, so the partner's engineers can begin; production credentials are issued only after certification. Both are the 15-minute, certificate-bound tokens that every partner has used since the Rowmate leak (the Resilience book, Section 7.5), so there is no long-lived key for a contractor to commit to a public repository.

The two partners' timelines show what a program is for. Rowmate, the pilot, spent about three months between entering the sandbox and going live, from month 9 to month 12, and much of that time was spent writing the certification suite with Encore, since nobody yet knew what a resale partner had to prove. Tessera arrived with the program already built. It failed its first certification run, for a reason the next subsection describes, fixed the fault and passed, and its first live listing came 11 days after it was certified. The difference is the program's return, because what Encore and Rowmate learned during the pilot did not have to be learned again.

#### Certification as a program {#c8-certification}

The Products book's Section 9.4 lists what a resale partner must demonstrate in the sandbox before receiving production credentials. The program decides who runs the suite, when it is rerun, what failure means and what it costs. The partner runs the suite itself against the sandbox, as often as it likes, and Partner APIs reviews the results along with a recorded walk-through of the partner's own screens. A partner recertifies on every major version of the partner API, after any change to how it handles listings or payments, and after any serious incident in which it was involved. A failure blocks production credentials and returns a written list of findings. Certification is free, since Encore wants partners more than it wants the fee. Precedents exist at much larger scale: Salesforce's AppExchange requires a security review before an app is listed, and Shopify reviews apps before they appear in its App Store.

Tessera's failed first run shows what certification is really testing. Tessera's storefront cached listing prices to keep its pages fast, and when the suite lowered an organizer's cap in the middle of the run, Tessera went on showing the old, higher price for longer than the suite allowed. The fix was easy, consuming the rule-change webhook and invalidating the cache, but in production fans would have seen prices the organizer had forbidden. Most of what can go wrong between partners and a platform happens when rules change, and a suite that tests only steady state certifies very little.

#### What partners may and may not do {#c8-may-and-may-not}

The contract states the policy, and the gateway enforces whatever part of it can be enforced by machine. The principle at Encore is that every "may not" has an enforcement next to it, either automatic at the gateway or detectable in audit. Figure 8.4 is the list as it stands at the month-18 review.

| Partners may | Partners may not | Enforcement |
|---|---|---|
| Show every listing in the resale pool and sell it to screened buyers | Buy primary inventory | No purchase scope on partner credentials (invariant 1) |
| Read event and availability data | Scrape beyond their contractual quota, or receive sales-velocity data | Quota and token-bucket limits at the gateway; coarsened availability only (invariant 5) |
| Set their own storefront design and marketing | Display a price without the service fee, or above the cap | Certification; monthly audit of sampled pages |
| Use buyers' personal data to deliver the purchase and support it | Use resale buyers' data for unrelated marketing without the buyer's consent | Contract; data-protection review at certification |
| Use organizer and artist branding within the organizer's rules | Imply an endorsement the organizer has not given | Contract; organizer complaint route |

*Figure 8.4 — Encore's "may and may not" list for resale partners. Breaches of policy move up a ladder of warning, throttle, suspension and termination.*

Breaches move up an enforcement ladder: a written warning, then throttling, then suspension, and termination last. The ladder is published in the agreement, and the partner manager decides each step with Partner APIs. Encore has used the second rung once. In the third month after launch a partner's listing traffic for one event exceeded its event-scoped limit during a major on-sale, and it was throttled to its quota until the sale ended; the cause was a retry loop in its synchronization job. Credential hygiene belongs to the Resilience book's Section 7.2{% include xref.html to="resilience:7.2" %}, and the partner terms, including the 12 months' notice, to the Products book's Section 9.4{% include xref.html to="products:9.4" %}.

#### Revenue share and partner statements {#c8-revenue-share}

The partner's 4 points are earned when a sale happens and kept only when the sale holds. Encore accrues the commission at the sale, releases it at the same moment it releases the seller's money, five days after the event if no dispute is open, and reverses it if the sale is reversed by a chargeback or a cancelled event. Each month Billing & Payouts generates a statement for each partner from the ledger, showing what was accrued, released and reversed, line by line and ticket by ticket. A partner may dispute any line within 60 days, and the Finance platform team answers from the ledger events behind it. The statement is reproducible from those events, which is the same discipline the Products book's Section 5.4{% include xref.html to="products:5.4" %} asks of invoices.

Revenue share is a strategic lever, and partners remember every movement of it. Shopify's public history makes the point well. At its Unite conference in June 2021 it announced that, from August that year, developers would pay no revenue share on their first US$1 million of annual app revenue and 15% above it, down from 20%. In April 2025 it announced that, from 16 June 2025, the exemption would apply to the first US$1 million of lifetime revenue instead of resetting each year, with only revenue earned since 1 January 2025 counting toward it, and developers who had planned their businesses around the annual reset said so publicly. Encore therefore treats a change to the partner commission like a breaking change to the API, with 12 months' notice, since it disrupts a partner's business as much as any change to an interface.

#### Partners who compete {#c8-competing-partners}

Rowmate also runs resale for other ticketing companies, where tickets are not reissued and caps are not enforced. That makes it a partner in Encore's market and a competitor in the wider one, and the Products book's Section 2.4{% include xref.html to="products:2.4" %} maps what that means strategically. The engineering consequence is information walls. Each partner sees only its own listings, sales, statements and reports, never another partner's. The walls do two jobs. They protect each partner's commercial position, and they keep Encore from becoming a channel through which competitors learn about each other, a recognized risk under EU competition law on information exchange between competitors; that second job is a matter for counsel, and Encore's partner policy says so.

Parity clauses are the other trap. A wide parity clause, one that requires a seller not to offer better terms on any other platform, is excluded from the EU's block exemption for vertical agreements (Regulation 2022/720, Article 5(1)(d)), so it needs an individual assessment; narrow parity, covering only the provider's own direct channel, remains exempted. The Digital Markets Act bans parity clauses outright only for designated gatekeepers, which Encore is not. Encore asks for no parity at all, and it hardly needs to, since the price is capped, the pool is the same on every channel and the fee is the same everywhere. Its own app is a channel too, and it keeps 7 points when it sells there, so the rule that matters is the one Encore imposes on itself: every channel receives the same listings in the same order, and partners can verify that from the feed.

**Recap.** A partner program is the business wrapper around an API product: agreements, tiers, enablement, review, support and change communication. Onboarding is a workflow on shared rails, with sandbox credentials at once and production credentials after certification, and certification should test behavior when rules change. Every "may not" needs an enforcement beside it and a published ladder above it, commission should be earned only when the sale holds, and partners who compete need walls between them, with no parity clauses that would need defending.

**Exercise 8.3.** Write your partner program's "may and may not" list as a table like Figure 8.4. For each "may not", name the enforcement: a scope, a limit, a test, an audit or a contract clause. Mark every "may not" whose only enforcement is a contract clause, and decide whether you can move it to the gateway.

### 8.4 InnerSource

#### Shared code without a ticket queue {#c8-innersource}

Inside a company of 40 teams, code is shared in two ways, and both go wrong. A team that needs a change in another team's component can ask for it, and wait in that team's backlog behind work the owner considers more important. Or it can copy the component and change the copy, and leave the company with two versions that drift apart for years. **InnerSource** is a third way: the use of open-source development practices inside one organization, in which code is visible to every team, any team may contribute changes by pull request, and the owning team keeps responsibility for what is merged. The name is usually traced to a column Tim O'Reilly wrote in December 2000, in which he described helping large companies use open-source development techniques internally and called the work "inner sourcing". Its vocabulary is borrowed from open source: the owning team is the **host**, and contributing teams are **guests**.

The research supports the practice and is candid about its conditions. Danese Cooper and Klaas-Jan Stol's *Adopting InnerSource* (2018) collects case studies from companies including PayPal, Bosch and Ericsson. Stol and his co-authors, in a 2014 study of the key factors for adopting it, found that most of those factors were organizational: who may contribute, how contributions are recognized, and whether managers make room for them. InnerSource complements the X-as-a-Service mode that Chapter 6 describes and does not replace it. A platform that serves many teams through a stable interface should usually stay a service. InnerSource suits the component that many teams need to change, where the changes come from the guests' own domain knowledge.

Scholarly publishing is a fair picture of the arrangement. A journal's editor does not write the articles; contributors submit them, referees review them, and the editor keeps the standard and decides what is published. The host team is the editor, and its trusted committers are the referees. The picture breaks on motive. Authors submit to journals because publication advances their careers. Guests contribute to InnerSource projects because they are blocked, and once unblocked they have little reason to stay. That difference explains why recognition, which a journal gets for free, has to be designed into InnerSource deliberately.

#### Trusted committers and contribution rules {#c8-trusted-committers}

A **trusted committer** is a member of the host team whose job is to help guests contribute well: answering questions, reviewing pull requests, mentoring, and guarding the component's quality. The role is a named pattern in the InnerSource Commons catalogue, and Cooper and Stol's chapter on PayPal describes it in practice, together with a written contribution guide and response times that the host publishes and keeps. The role is an investment of the host's time, and it has to be counted as one. I have spent a decade maintaining a widely used open-source library, and the lesson that experience taught most firmly is that the contributors a project keeps are the ones who heard back quickly the first time.

Encore's resale rules engine has two trusted committers at any time, and Encore rotates them each quarter, so the knowledge spreads and nobody becomes the engine's only gate. The rotation is Encore's own choice and is not prescribed by the sources. Discoverability matters at 40 teams as well; the catalogue's InnerSource Portal pattern exists so that guests can find projects open to contribution, and Encore lists the engine in its developer portal with its contribution guide. The guide is short enough to read in a minute:

```text
# Contributing to resale-rules
Host: Resale team. Trusted committers this quarter: see OWNERS.
1. Open an issue first for any new rule type; describe the organizer need.
2. New rule types need a short RFC; reviewers: both trusted committers.
3. Every rule must be expressible in the typed schema; no free-form rules.
4. The fairness invariant suite must pass; never edit it in the same PR.
5. Add property tests for your rule's boundaries (see tests/rules/README).
6. First response within one working day; merge decision within five.
7. Your team fixes defects in your rule for 30 days after release.
8. Ask in #resale-rules; office hours Tuesday 14:00 CET.
```

#### Patterns that work {#c8-innersource-patterns}

The InnerSource Commons maintains a catalogue of patterns, each a documented solution to a recurring problem, with known instances at named companies. Three of them shaped Encore's guide. The **30 Day Warranty**, drafted at the Spring 2017 InnerSource Summit, has the contributing team fix defects in its contribution for 30 days after it reaches production; it answers the host's natural fear that guests will merge and leave, and some companies use longer periods, GitHub six weeks. **Issue Tracker Use Cases** and **Transparent Cross-Team Decision Making using RFCs** together describe discussing a change before writing it, which saves guests from building a pull request the host will refuse. And **Contracted Contributor** answers the question of time: a formal agreement among the contributor, their line manager and a central office that caps the time spent on InnerSource, reimburses the contributor's business unit, and gives the community leader a voice in the reviews of anyone contracted above 20%. The catalogue also includes **Praise Participants**, a reminder to thank contributors visibly.

The cases Cooper and Stol collected point to one conclusion, which is their synthesis and worth stating as theirs: management support decides the outcome more than tooling does. Stol's earlier study points the same way, since its key factors concern people and incentives far more than software.

#### Encore's resale rules engine {#c8-rules-engine}

The resale rules engine is the typed library that evaluates every organizer and platform rule at the transitions of Figure 8.3. The Resale team hosts it, and five guest teams contribute rule types from their own domains: Orders & Payments, Inventory, Trust & Safety, Pricing & Presales and Festivals. Festivals is writing a cap kind for multi-day passes split into day tickets, where face value must be computed from the pass price, so that festival passes, deferred at launch, can join; Pricing & Presales contributed the rules for tickets bought in presales; Trust & Safety contributes the listing-velocity rules. Each team knows its own domain far better than the Resale team could, and each would otherwise have waited a quarter in Resale's backlog for a change it could write in a week.

The fairness invariant tests are the gate every contribution must pass, and the guide forbids changing them in the same pull request as a rule. Guests are trusted to change the rules because no rule they write can break an invariant without a test failing, and the invariant tests change only through the host's own review. The typed schema has a second benefit: the organizer rule assistant, the one AI feature in Verified Resale, can express only rules the schema allows, so whatever it drafts is bounded by the same tests.

#### When InnerSource fails, and how to tell {#c8-innersource-failure}

InnerSource fails when guests have no time allocated for contributing, so contributions are squeezed between deadlines and abandoned. It fails when contributing earns no recognition, so the people who do it once never do it again. And it fails when the host is overwhelmed, so pull requests wait for weeks and guests conclude that copying would have been faster. The patterns above exist because each failure is common: Contracted Contributor answers the first, Praise Participants the second, and the 30 Day Warranty, by reducing the host's risk, the third.

Encore learned this before the rules engine. In year 8 the Seat Map team opened its renderer, `seatmap-renderer-v2`, to contributions from Event Setup and Box Office, which both needed changes for their own screens. Nobody's quarterly plan contained time for it, the Seat Map team had no trusted committer and was preparing for the Vesper Hale on-sale, pull requests waited weeks for review, and within two quarters the guests had gone back to filing requests in the Seat Map backlog. When the rules engine opened, the lesson was written into planning: each guest team's quarterly plan carries explicit time for its rule types (Section 10.2), the host names its trusted committers, and contributions appear in the engineers' reviews.

To tell success from slow failure, Encore measures what the CHAOSS project (Community Health Analytics in Open Source Software) defines for open source, applied to one repository: time to first response, change requests accepted, and the number of active contributors, combined much as the catalogue's Repository Activity Score pattern suggests. By month 18 the engine had merged 37 changes from guest teams, with a median first response under one working day and contributors from all five guest teams. A first-response time creeping from one day to four is the earliest sign of an overwhelmed host.

**Recap.** InnerSource lets teams change shared code by pull request while the host keeps ownership, and it suits components whose changes come from the guests' domains. Trusted committers, a short contribution guide and published response times make contributing practical, and the catalogue's patterns answer the common failures of time, recognition and host overload. Its success depends on management making contribution part of the job, and its health is visible in response times and contributor counts long before it fails.

**Exercise 8.4.** Pick one shared component your team depends on and does not own. Write its contribution guide in ten lines: who the host is, how to propose a change, what must pass, how fast the host responds, and what the contributor promises after merge. Then ask the host whether they could keep the response time you wrote.

### 8.5 Platform Economics

#### Funding shared capabilities {#c8-funding}

Encore now runs two platforms, and they are funded in different ways for good reasons. The internal platform, the platform group's nine teams, serves Encore's own engineers. The business platform, Verified Resale, serves fans, organizers and partners. For a shared internal capability there are three common ways to pay. **Central funding** pays for it from the company's overall engineering budget. A **platform tax** takes a fixed share of each product team's budget to pay for it. **Chargeback** bills each team for its measured use at an internal price.

Mik Kersten's *Project to Product* (2018) argues for funding long-lived products over temporary projects, and the argument applies to platforms with particular force, since a platform funded project by project is rebuilt every year by whoever has budget left. Gregor Hohpe's chapter "Platform, Inc." in *Platform Strategy* treats an internal platform as an internal business with customers and a strategy of its own, and Camille Fournier and Ian Nowland's *Platform Engineering* (2024) shows how to keep it aligned with the teams it serves. Encore funds its platform group centrally, as a long-lived product with its own roadmap and its own measures, and it does not use chargeback. How the central budget enters the company's allocation of capacity, including whether it appears as a platform tax in each value stream's plan, is the subject of Section 10.4.

The business platform is funded the other way. Verified Resale was funded in tranches against milestones (Section 10.4), and it is expected to pay its own way from Encore's 3 points per resale. A business platform has revenue and should be judged by its margin; an internal platform has none and should be judged by what it saves and enables.

#### Showback before chargeback {#c8-showback}

**Showback** shows each team the cost of what it uses, without billing it; **chargeback** bills it. The FinOps Foundation's framework treats showback as necessary in every cost practice, and leaves chargeback to the company's accounting policy, stating that neither should be considered more mature than the other. Chargeback can be worth its overhead where spending lands in many independent budgets, and it is often not worth it where, as at Encore, engineering spending lands in a few cost centers.

Encore's choice is showback only. The Resilience book's Section 2.5 already allocates more than 90% of the cloud bill to services and tenants, and the showback report builds on that allocation, showing each team its cost per service and its contribution to cost per ticket, a blended €0.16 of which about €0.12 is variable. There is also an argument against chargeback that Encore finds persuasive, though no study proves it. An internal price invites teams to save money by leaving the paved road, running their own cheaper database or their own deploy scripts, and the savings appear on the team's bill while the costs appear later, in incidents and migrations nobody budgeted.

#### Unit economics of the business platform {#c8-unit-economics}

**Contribution margin per resold ticket** is the revenue Encore keeps from one resale minus the costs that resale itself causes. The Products book's Chapter 5 sets the price; this subsection asks what the price leaves. Figure 8.5 works the example on a €60 ticket, sold once through a partner and once in Encore's own app. The PSP fee, fraud loss and support cost are Encore's averages at the month-18 review.

{% include diagrams/fig-8-5.svg %}

*Figure 8.5 — Contribution margin per resold ticket. The partner channel runs on a margin of 38 cents, and each additional point of dispute rate costs 15 of them.*

On the partner channel, which carries most resales, the margin is 38 cents, and it is far more sensitive to disputes than to the fee. Each additional percentage point of resales that end in a dispute costs €0.15, so a dispute rate of about 4.5% would wipe the margin out entirely, while raising Encore's share of the fee by half a point would add only €0.30. Encore learned from this that the cost of handling one dispute, about €15 of an agent's time, decides its margin more than the fee level does, and it has spent its effort there: automatic assembly of gate-scan evidence, a self-service dispute flow, and the tracking of dispute rates per partner described in Section 8.3.

The other column carries a temptation, and the margin of €2.78 in Encore's own app makes it plain. Encore earns seven times as much when a buyer purchases in its app, and a business optimizing its margin would steer buyers there. The rule from Section 8.3, every channel receiving the same listings in the same order, is what stops it, and the figure is the reason the rule had to be written down before anyone was tempted.

#### When to stop building {#c8-stop-building}

Every capability a company builds moves, over time, toward commodity, and the Architecture book's Section 13.2{% include xref.html to="architecture:13.2" %} maps that movement using Simon Wardley's evolution axis. The practical tool is a **stop-doing list**: a short, maintained list of capabilities Encore intends to hand to a vendor or retire, each with the criteria that put it there. Encore's criteria are three: a mature product meets Encore's requirements, Encore holds no knowledge in the capability that its competitors lack, and running it costs more than buying it.

The first entry on the list was Encore's own feature-flag service. The Resilience book describes the rules Encore enforces on flags, each with an owner, a kind and an expiry date, no reused names, every change recorded as a production change, and expired release flags blocking deploys, and those rules are Encore's own knowledge. The service that stores and evaluates flags is not; mature products do it well. So Encore decided to keep the rules as a thin policy layer over a bought flag product and to retire its own service through a deprecation campaign of the kind Section 6.4 describes, with a dated end and brownouts to find forgotten callers. The list also records what will never appear on it. Reissue and the ledger hold the knowledge that makes Verified Resale trustworthy, and Section 8.1 drew that line before any capability was weighed.

#### Reporting the value of both platforms {#c8-platform-report}

Encore puts both platforms on one page each quarter, because the same leadership funds both. David Anderson's *The Value Flywheel Effect* (2022) argues for organizing technology work around time to value, and the page follows that idea: each platform reports how quickly the people it serves get what they came for. For the internal platform, the measures come from Section 6.5: the adoption funnel for each paved path, the quarterly developer-experience survey, and time to first production deploy for a new service. For the business platform, the measures come from the Products book's Section 5.2{% include xref.html to="products:5.2" %}: liquidity, take rate, dispute rate and organizer adoption.

A platform's **take rate** is the share of the value of each transaction that the platform keeps as revenue. Verified Resale's gross take rate is the 10% fee, but Encore's own take is 3 points on partner sales and 7 points in its app, and the page reports the blended figure, since it shows the channel mix moving. The page shows trends and distributions, never rankings of teams or partners, under the rule Encore applies to every scorecard. When the internal platform's time to first deploy falls and Verified Resale's dispute rate rises in the same quarter, leadership can see that the next quarter's best investment may be a support tool, not a faster pipeline.

**Recap.** Encore funds its internal platform centrally as a long-lived product and funds its business platform in tranches against a margin, and it judges each by the test that fits it. It shows teams their costs without billing them, because chargeback's overhead and its pull away from the paved road outweigh its benefits at Encore's scale. Contribution margin per resold ticket shows that disputes, more than the fee, decide whether resale pays its way. A stop-doing list retires what has become commodity, and one quarterly page reports both platforms by time to value.

**Exercise 8.5.** Compute the contribution margin per transaction for one marketplace or platform feature you know, line by line as in Figure 8.5. Name the cost you are least sure of, and work out how much it would have to move to make the margin zero. If that movement is small, find out who owns the cost.

### Kata: Gear Between Rivals

> **Your brief: "Kitebridge."** Kitebridge is a software-as-a-service company of 120 engineers whose tenants are film-equipment rental houses: 260 houses in seven EU countries, renting cameras, lenses, lighting and grip to productions. When a house is short of a lens for a shoot, it borrows one from a rival, today by phone and by spreadsheet, about 11,000 times a year. Kitebridge wants a marketplace for those sub-rentals, in which houses list spare gear, other houses book it, and three production-management apps that crews already use book on their behalf, through Kitebridge's API, as certified partners. A typical sub-rental is worth €1,400 for four days; the owning house expects a deposit of 30% and a share of the fee; and about 3% of rentals end in a damage claim, averaging €2,200, which today takes months to settle. Last year a pilot let houses hold deposits in their own accounts, and a dispute over a damaged lens lasted four months before anyone agreed whose money it was. The two largest houses will join only if their competitors can never see how busy their inventory is.

**Deliverables:**

1. **Core interaction and invariants** — Write the core interaction in one sentence, naming participants, unit of value and filter, and map each phrase to a component and owner. Then write the invariants that keep the market fair to small houses and large ones, and name the single place each is enforced.
2. **The rental state machine** — Draw the lifecycle of a sub-rental, from listing through booking, handover, return and inspection to settlement, as a diagram like Figure 8.3. Mark the transition at which each rule, each fraud control and each damage claim applies.
3. **Money and deposits** — Trace the buyer's payment, the deposit and the fee from the booking house to the owning house. Decide who holds the deposit while the gear is out, and justify the decision against the possession-or-control rule of Section 8.2. Say what happens to the deposit when a damage claim is disputed.
4. **The partner program** — Write the "may and may not" list for the three partner apps, with an enforcement for every "may not", and the certification tests that prove a partner handles a rule change and a cancelled booking correctly.
5. **Contribution margin** — Compute the contribution margin per sub-rental, line by line, including payment fees and the cost of handling a damage claim. Name the cost you are least sure of and the movement in it that would make the margin zero.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| One sentence | Can every feature in your design be traced to a phrase of the core interaction? |
| Enforced fairness | Is each invariant enforced in exactly one place, and tested on every change? |
| Rules on transitions | Does every rule and control in the state machine sit on a named transition with an owner? |
| Money held lawfully | Is there any day on which Kitebridge holds a house's money, and if so, has that been put to counsel? |
| Walls between rivals | Could the largest house learn anything about a competitor's utilization from what your platform shows it? |
| Honest margin | Would your margin survive the damage-claim rate doubling, and did you say what happens if it does not? |

#### Where you now stand

You can now treat a product that others trade through as a system with rules of its own. You can write its core interaction as one sentence that maps to owners, turn its fairness into invariants enforced in one place each, put its rules on the transitions of an explicit lifecycle, and route its money so that the platform keeps the ledger while a licensed provider keeps the funds. You can build a partner program that admits partners through certification and governs them with enforcement they can see coming, open shared code to the teams who need to change it, and judge both of a company's platforms by tests that fit them. Throughout, though, the teams have appeared as if they were fixed, and they are not: the Resale team was formed at month 4 out of two other teams, and it is about to grow and split. How an organization of 400 engineers grows, designs its teams and leads them is the subject of Chapter 9.

### References

- David S. Evans, Richard Schmalensee — *Matchmakers: The New Economics of Multisided Platforms*. Harvard Business Review Press, 2016.
- Geoffrey G. Parker, Marshall W. Van Alstyne, Sangeet Paul Choudary — [*Platform Revolution*](https://archive.org/details/platformrevoluti0000park). W. W. Norton, 2016.
- Michael A. Cusumano, Annabelle Gawer, David B. Yoffie — *The Business of Platforms: Strategy in the Age of Digital Competition, Innovation, and Power*. HarperBusiness, 2019.
- U.S. Court of Appeals for the Eleventh Circuit — [*National Bancard Corp. (NaBanco) v. VISA U.S.A., Inc.*, 779 F.2d 592](https://law.resource.org/pub/us/case/reporter/F2/779/779.F2d.592.84-5818.html). 1986 — free online.
- Visa — [*Dee Hock in memoriam*](https://corporate.visa.com/en/sites/visa-perspectives/company-news/dee-hock-in-memoriam.html). Visa, 2022 — free online.
- European Parliament and Council — [*Directive (EU) 2015/2366 on payment services (PSD2)*, Article 3(b) and recital 11](https://www.legislation.gov.uk/eudr/2015/2366/contents). 2015 — free online.
- European Banking Authority — [*Single Rulebook Q&A 2020_5355*](https://www.eba.europa.eu/single-rule-book-qa/qna/view/publicId/2020_5355). EBA, 2021 — free online.
- Danese Cooper, Klaas-Jan Stol — [*Adopting InnerSource: Principles and Case Studies*](https://www.oreilly.com/library/view/adopting-innersource/9781492041863/). O'Reilly, 2018.
- InnerSource Commons — [*InnerSource Patterns*](https://patterns.innersourcecommons.org/). InnerSource Commons — free online.
- Mehdi Medjaoui, Erik Wilde, Ronnie Mitra, Mike Amundsen — [*Continuous API Management*, 2nd ed.](https://www.oreilly.com/library/view/continuous-api-management/9781098103514/). O'Reilly, 2021.
- Paul Resnick, Richard Zeckhauser, John Swanson, Kate Lockwood — [*The Value of Reputation on eBay: A Controlled Experiment*](https://presnick.people.si.umich.edu/papers/postcards/index.html). *Experimental Economics* 9(2), 2006 — free online.
- European Parliament and Council — [*Directive (EU) 2019/2161 (Omnibus Directive)*](https://eur-lex.europa.eu/eli/dir/2019/2161/oj). 2019 — free online.
- Competition and Markets Authority — [*Summary of the court order secured by the CMA against viagogo*](https://www.gov.uk/government/publications/summary-of-the-court-order-secured-by-the-cma-against-viagogo/summary-of-the-court-order). GOV.UK, 2018 — free online.
- European Commission — [*Regulation (EU) 2022/720 (Vertical Block Exemption Regulation)*](https://eur-lex.europa.eu/eli/reg/2022/720/oj). 2022 — free online.
- FinOps Foundation — [*Invoicing & Chargeback*](https://www.finops.org/framework/capabilities/invoicing-chargeback/). FinOps Framework — free online.

---

## Chapter 9: Teams at Scale — Growing, Designing, and Leading the Organization That Builds {#ch9}

> A team can be asked to do the impossible once. An organization has to be designed to do the difficult every year.

Every chapter so far has treated the organization as a given: forty teams, a platform group, a trio here and a staff engineer there. This chapter asks how it came to be, and how it should be shaped. Who belongs on which team, and how much should a team own? Who decides when two teams disagree, and who writes the decision down? How many people can an organization hire in a year before it stops getting faster and starts getting slower? These are among the oldest questions in our field, and engineers are seldom taught to answer them; most of us learn by getting them wrong.

The story that frames the chapter took place in a basement in Westborough, Massachusetts, between 1978 and 1980, where a small group of young engineers at Data General built a 32-bit minicomputer under a manager named Tom West, and the writer Tracy Kidder watched them do it. His book, *The Soul of a New Machine* (1981), won the Pulitzer Prize and has been passed from engineer to engineer ever since, usually as a story about what a committed team can achieve. Read to its end, it is also a story about what an organization pays when it depends on heroics instead of design, and that second reading is the one this chapter needs.

Encore reached 400 engineers in its seventh year and has stayed at about that size since. Now, in year nine, Verified Resale needs a team that does not yet exist. By month four of the bet a Resale team must be formed from people who already have jobs, with a product trio and a staff engineer, and its first cross-team decision, whether Resale or the Inventory team owns the reissue of a barcode, must be settled in a way that 12 teams will accept. We will follow that team, and use Encore's history from nine engineers to 400 to explain why its teams, roles and decision forums look the way they do.

### 9.1 Growing from 9 to 400

#### The Eagle and what it cost {#c9-eagle}

In 1977 Digital Equipment Corporation released the VAX, a 32-bit machine, and Data General's 16-bit Eclipse line began to lose sales. Data General's founder, Edson de Castro, moved the company's lead development group to North Carolina to build an ambitious new 32-bit design, the Fountainhead Project. Tom West, who ran the Eclipse group in Westborough, was among the senior engineers who stayed behind, and in 1978 he proposed something smaller: a 32-bit extension of the Eclipse, compatible with the software customers already ran, offered as insurance in case North Carolina failed. De Castro gave tacit approval, West promised the machine in a year, and it was code-named Eagle.

West and his deputy, Carl Alsing, recruited about two dozen engineers, most of them straight out of college. The "Microkids", led by Alsing, wrote the microcode; the "Hardy Boys", led by Ed Rasala, built the hardware; Steve Wallach was the architect. West's word for the commitment he asked of them was "signing up", and in Kidder's account it meant agreeing to do whatever the machine required, including a great deal of overtime, for no extra pay. West called the reward "pinball": win one game and you get to play another, so the prize for building this machine was the chance to build the next. The team worked in near isolation, shielded from the company's politics by a leader who kept the schedule always in front of them. Figure 9.1 draws the project and its team as a schematic.

The machine was late, as ambitious machines are, but it shipped. Fountainhead was cancelled, and Eagle was announced in April 1980 as the Eclipse MV/8000; by Evan Ratliff's account in *Wired* 20 years later, it kept Data General in the minicomputer business for several years. What happened to the team concerns us more. A new vice president of engineering regarded the group as having defied the company, the group was broken up, and West was sent to Data General's office in Japan before a single MV/8000 had been sold. By the time Kidder's book appeared in July 1981, many of the engineers had left or were leaving, some to found companies and some simply burned out. Ken Holberger, one of the Hardy Boys, told Ratliff the team had been like gunfighters brought into town to solve a problem; they solved it, and "then the town had to figure out what to do with them afterward. Which was mostly to get rid of them."

{% include diagrams/fig-9-1.svg %}

*Figure 9.1 — The Eagle at Data General, drawn as a schematic. The machine shipped and the North Carolina project was cancelled, yet soon after the launch the team that built it was broken up.*

Burnout is part of the story, but the departures were caused at least as much by the organization's inability to recognize and absorb what the team had done. A small, isolated group can do remarkable work; Heidi Helfand would later call this the *isolation pattern* of reteaming, and Data General used it long before it had a name. An organization that relies on isolation, overtime and one protective leader has no way to keep the people afterward, fold their knowledge back into the company, or do the thing again. Tom West was a substitute for a design. This chapter is about designing an organization in which the next machine does not depend on another Tom West.

#### One team of nine {#c9-one-team}

Encore began, as the Architecture book{% include xref.html to="architecture" %} told, with nine engineers in one team building a modular monolith. Much of what made that team effective was invisible because it worked. There was one backlog. The two founders acted as an informal product trio, one holding the customer and the other the code. Decisions were made in conversation and remembered by everyone, because everyone had been in the room. New engineers learned the system by sitting next to the people who had written it, and nobody needed to write down who owned the payments code.

Tom DeMarco and Timothy Lister argued in *Peopleware* (1987, now in its third edition) that the major problems of software development are sociological more than technological. It is a thesis without a measurement behind it, but nearly four decades of practitioners have recognized it, and it is the right lens for what happened next. Encore did not hit a technical wall as it grew. It hit a social one, built of things that had been free. Implicit decisions stopped reaching everyone who needed them. Onboarding by proximity stopped working when the people worth sitting next to had three newcomers each. And knowledge of the payments code, still held by one person, became a risk whenever that person took a holiday.

Encore's history marks the moment. In its second year, at about 25 engineers, a thread appeared in the company chat that began "Who decided this?" Someone had changed how holds expired, for good reasons, and two other engineers had built on the old behavior. Nobody had been careless; the decision had been made in a conversation that two of the people it affected were not part of. The Architecture book's Chapter 5 opens with the arithmetic behind this, the number of possible conversations growing roughly as the square of the group, and the thread was its first visible sign at Encore.

#### Nine teams of 70 {#c9-nine-teams}

By year four Encore had 70 engineers in nine teams, drawn along the services that the Architecture book's Chapter 5{% include xref.html to="architecture:5" %} cut (its Section 5.1 and Section 5.5 tell that half of the story). The half it leaves out is management, which is where most of the early mistakes were made.

The first managers were promoted from the best engineers, as they are in most young companies. Camille Fournier, in *The Manager's Path* (2017), makes this a fork in a career: stay on the technical track, or become a manager. The branches lead to different jobs, and the skills that made someone an excellent engineer are only part of what the second demands. Encore presented management as a promotion, so some of its best engineers took a job they had not chosen and nobody had trained them for.

Will Larson's rules of thumb, from his experience at Uber and Stripe, give a check on what Encore built. In "Sizing engineering teams" (2018) he writes that "managers should support 6-8 engineers", that "small teams (<4) are not teams", and that a new team is best made by growing an existing one to 8 or 10 and splitting it into two of four or five. These are heuristics, but they encode real forces: a team smaller than four cannot carry an on-call rotation or survive one departure, and a manager with more than eight reports has stopped managing and started triaging. The first draft of Encore's 70-engineer map broke both rules. It showed 11 teams, two of them of three people who depended on a neighbor for every review and every page, and one manager in Orders & Payments had 14 reports. The two small teams were folded into their neighbors, which is how Encore came to nine, and the 14 were split under two managers within the year.

#### Hypergrowth to 400 {#c9-hypergrowth}

Between years four and seven Encore grew from 70 engineers to 400. Hiring outpaced the organization's ability to absorb people, managers of managers appeared, and every practice that had worked for nine teams was tested at forty. The Architecture book's Section 15.3 shows what happened to the architecture review board, which becomes a bottleneck or a rubber stamp at forty teams, and its Section 5.5 shows what replaced it. The human side of the same growth followed the same arithmetic.

Larson's essay "Productivity in the age of hypergrowth" (2016) is the clearest model of that human side. Writing about Uber, he observed that "our process is always six months behind our headcount." In his model a trained engineer must spend time training each new one, and in his worst case, two untrained engineers to every trained one with the hiring load included, "the overall team is getting 1.06 engineers of work out of every three engineers." The numbers are illustrative, from one company, and Larson presents them that way; the direction is not in doubt. Past a certain ratio of new people to experienced ones, adding people subtracts work. His prescriptions follow: concentrate hiring in one team at a time, and shorten training, because every week cut from it returns capacity to the whole team.

Encore's version of the lag was visible in its numbers. At the end of year six it had 250 engineers, and 145 of them had joined within the previous 12 months. More than half the organization had never been through an on-sale and had learned the system from people who had learned it a few months before.

#### The organization as stocks and flows {#c9-stocks-flows}

The tool that makes this lag visible before it becomes a crisis comes from outside software. Jay Forrester founded system dynamics at MIT in the late 1950s, and Donella Meadows's *Thinking in Systems* (2008) is its most readable introduction. A **stock** is a quantity that accumulates over time, such as the number of engineers still ramping up; a **flow** is a rate that fills or drains a stock, such as hires per month. Stocks change only through their flows, and flows are limited by things we can name. Tarek Abdel-Hamid and Stuart Madnick applied the method to software projects in *Software Project Dynamics* (1991). We borrow the method for a narrow purpose: checking a growth plan against the organization's capacity to absorb it before anyone approves the plan.

Larson's "Introduction to systems thinking" (2018) uses the frame mainly for developer velocity, with stocks of open pull requests and ready commits, and briefly for trained managers; the hiring model we need is closer to his hypergrowth essay. Drawn for people, it is simple. Hires enter a stock of engineers who are ramping; ramping engineers flow into the productive stock at a rate limited by onboarding capacity, which is the time of experienced people; and productive engineers leave through attrition or move into management. Each arrow has a limit, and a growth target has to be checked against all of them. Figure 9.2 draws it.

{% include diagrams/fig-9-2.svg %}

*Figure 9.2 — People as stocks and flows. The valve between ramping and productive is opened only by experienced people's time, and the productive stock feeds back into it, so a slow year weakens the next one.*

Anyone who has worked the doors of a large concert venue knows this shape. However many fans are queuing outside, the hall fills only as fast as the doors and stewards allow, and a promoter who sells more tickets than the doors can admit before showtime has sold a longer queue. The ramping stock is the queue, and experienced engineers are the stewards. The analogy breaks in a way that makes the organizational case worse: fans who get through the doors simply watch the show, while newcomers who get through onboarding become the stewards for the next cohort, so a slow door one year produces poorly trained stewards the next.

In year nine, prompted by the developer survey of Section 1.2, in which one engineer in five named new engineers taking about a quarter to make a meaningful change among their top three complaints, Encore redrew its years of hypergrowth this way. Figure 9.3 shows the result.

| Year | Engineers at year end | Hired | Left | Joined within the year, at year end | Median days to a new engineer's tenth merged change |
|---|---|---|---|---|---|
| 4 | 70 | 28 | 6 | 26 | 34 |
| 5 | 120 | 62 | 12 | 58 | 41 |
| 6 | 250 | 150 | 20 | 145 | 68 |
| 7 | 400 | 185 | 35 | 178 | 74 |
| 8 (to month 0 of year 9) | about 400 | 40 | 38 | 38 | 71 |

*Figure 9.3 — Encore's people as stocks and flows. The ramping stock grew faster than the engineers available to teach it, and the time to a tenth change, a proxy for ramp-up, nearly doubled and never came back down.*

The table told a story the retrospectives had missed. For two years teams had blamed slow delivery on "culture": on newcomers who did not care about quality, or a loss of the founding spirit. The stock-and-flow view named the constraint. Onboarding depended on a buddy from the same team, and a buddy could usefully take one newcomer at a time. In year six there were fewer engineers with a year's tenure than newcomers, so buddies were doubled up, borrowed from other teams or skipped. The time to a tenth change rose from about five weeks to about 10 and stayed there after hiring slowed, because those who had ramped slowly became the next cohort's buddies. It was a flow limited by a stock, and Section 9.4 applies the flow solutions.

The model also has an outflow, which Encore had watched carelessly as a single annual attrition percentage. It now tracks **regretted attrition**, the departures its managers would have tried to prevent, separately from the rest, and reads exit interviews against the stock-and-flow picture, because a team that loses two experienced engineers in a quarter also loses part of its capacity to ramp the next ones.

#### What did not have to break {#c9-teamicide}

Not everything that broke was forced by arithmetic. Some of it Encore did to itself, and *Peopleware* has catalogued such wounds for nearly 40 years. Its best-known evidence comes from the Coding War Games that DeMarco and Lister ran from 1984 to 1986, in which more than 600 developers from 92 companies worked separately on the same specification, in pairs from the same organization. Language made no difference except for assembly, and years of experience did not predict performance. Pay barely tracked it: the better-performing half earned less than 10% more than the other half while performing nearly twice as well. Nearly a third of participants finished with zero defects and paid no penalty in speed. The top quarter outperformed the bottom quarter by 2.6×, the best organization worked 11.1 times faster than the worst, and pair mates from the same organization performed within about 21% of each other, which points to the organization more than the individual. The top performers also reported quieter, more private workspaces. The data are correlational, partly self-reported and gathered in offices before open-plan floors and remote work. They remain the best-known evidence that the environment an organization provides accounts for much of the difference between developers.

*Peopleware* also named the ways organizations destroy teams without meaning to, which it called **teamicide**: defensive management, bureaucracy, physical separation, fragmentation of people's time, the quality-reduced product, phony deadlines and clique control. Read against Encore's year six, the list is uncomfortable. At about 200 engineers, a quarter of them were assigned to two or three initiatives at once. A launch date for the organizer console was set before discovery had started, and missed by a quarter. Encore avoided other items: teams sat together, in an office or a shared channel, and nobody was asked to ship a product the team believed was broken. Each item on the list looks like a reasonable management decision on the day it is made, and its cost appears later, in a team that has stopped jelling.

Encore's engineers work across several EU countries and time zones, so the office data of the 1980s describe only part of its world. The claim about uninterrupted time carries over; a distributed team protects it with written communication, meetings clustered into part of the day, and agreed core hours.

**Recap.** Encore's growth broke first where things had been free: implicit decisions, onboarding by sitting nearby, and knowledge held by one person. Larson's hypergrowth model and the stock-and-flow frame show why: the ramping stock grows faster than the experienced people who can drain it, and process lags headcount by months. Some damage was not forced by growth at all, and *Peopleware*'s teamicide list, old as it is, still names it.

**Exercise 9.1.** Draw your organization's last three years as a stock-and-flow diagram of people: hired, ramping, productive, leaving. Put a number on each flow, and mark the stage at which each of your current pains first appeared. Then name the flow that limits the others.

### 9.2 Designing Teams

#### Forty teams on one map {#c9-team-map}

The vocabulary for team design is shared across this series. Matthew Skelton and Manuel Pais's *Team Topologies* (2019; second edition 2025) gives four team types, stream-aligned, platform, enabling and complicated-subsystem, and three ways for teams to interact. The Architecture book's Section 5.5 uses them, with Conway's law, to draw teams to match services, and its Section 15.2 sizes the platform group at 5 to 10% of engineering. We take all that as given and show the map itself, since a vocabulary proves its worth only on a real organization.

| Area | Teams | Type | Examples |
|---|---|---|---|
| Fan storefront and app | 9 | stream-aligned | Seat Map, Checkout, Mobile App, Design System |
| Organizer console | 7 | stream-aligned (Forecasting behaves as complicated-subsystem) | Organizer Console, Event Setup, Forecasting |
| Partner and public APIs | 3, plus Resale from month 4 | stream-aligned | Public API, Partner APIs, Embeds & Channels |
| Encore SaaS for venues | 7 | stream-aligned | Tenant Identity, Venue Entry, Box Office |
| Shared domains | 14 | stream-aligned | On-Sale, Inventory, Orders & Payments, Fan Messaging |
| Platform group | 9 teams, 40 people | platform | Reliability, Runtime, Developer Portal, AI Platform |

*Figure 9.4 — Encore's team map at about 400 engineers. Forty stream-aligned teams average nine engineers each; enabling work is carried as a second duty by two teams instead of by standing enabling teams.*

Two features of the map depart from the textbook. Encore has only one team that behaves as a complicated-subsystem team, Forecasting, whose demand models need specialist statistical knowledge and reach Organizer Insights through an interface. Seat allocation and bot scoring are hard too, but they are the core of their stream-aligned teams' work, and separating the specialists from the stream would add a hand-off to every change; a complicated-subsystem team earns its place only when the specialism is deep and the interface narrow. And Encore has no standing enabling team. Design System coaches other teams on accessibility and AI Platform helps teams adopt its gateway and eval tooling, each as time-boxed engagements that end when the other team can work alone. Marty Cagan and Chris Jones's *Empowered* (2020) gives a product-side reading of the same map, distinguishing experience teams, whose customers are end users, from platform teams, whose customers are other teams.

A caution belongs beside any published team map, this one included. The "Spotify model" of squads, tribes, chapters and guilds was copied widely after Henrik Kniberg and Anders Ivarsson described it in a 2012 paper, *Scaling Agile @ Spotify*. In April 2020 Jeremiah Lee, who had worked at Spotify, wrote that the model had been "only ever aspirational and never fully implemented" there. A published map shows the shape one organization chose for its own constraints. Another organization can borrow the reasoning only if it can see it, which is why this section gives the reasons beside the map.

#### Cognitive load as a budget {#c9-cognitive-load}

The Architecture book defined cognitive load and traced it to John Sweller's research on learning, and the Operations book{% include xref.html to="operations" %} uses it to limit what a team can be asked to operate. Here it is a budget: when a team overspends it, something must be handed away. The framing matters in practice. Asked whether a team is overloaded, people argue about the answer; asked what the team would hand to someone else, they have to name a responsibility, and a named responsibility can be moved.

No validated instrument for team cognitive load exists; Team Topologies' own materials call its measurement a challenging area, and the book offers the idea, with a team size of roughly five to nine people, rather than a scale. Encore runs a short self-assessment each half: each team rates how many domains it owns, how often other teams interrupt it, how much of its on-call load comes from things it did not build, and how well it understands each system it owns. The answers start a conversation between a team and its manager and are never used to compare teams. The Brazilian fintech Creditas has described a similar practice as a Team Topologies case study, without numbers, which is about the strength of the evidence: the practice is in use, and its value is the conversation.

The assessment earned its keep in year nine. Partner APIs already owned the partner endpoints, inventory feeds, sandbox, certification and webhooks; Verified Resale would add a new partner API, a reissue certification suite and Tessera's onboarding after Rowmate's, while three of its nine engineers left for the Resale team. Every dimension came back red, and the conversation produced one decision: Partner APIs would hand webhook delivery to the platform group. Chapter 6 tells the platform's side. Its own audit of requests had already ranked shared webhook delivery among its first increments, and it built the capability by absorbing three home-grown senders, Partner APIs' first. From this side the same hand-off was a budget decision by an overloaded team, and because the two views met, the work moved within a quarter.

#### Team APIs and interaction modes over time {#c9-team-api}

A team that owns services also owns promises to the teams around it, and they are worth writing down. A **team API** is a short, written description of what a team owns, how other teams should ask it for things, and what it promises in return. Skelton and Pais publish a free template, and the Resale team's first draft read like this:

```markdown
# Team API: Resale (formed month 4)
Owns: Resale service, Resale fan-app module (15th), resale rules engine (InnerSource host),
      organizer rule assistant
Does not own: barcode issuance and revocation (Inventory), payouts (Billing & Payouts)
Ask us: #resale-requests channel; reply within 1 working day; rule-type contributions by PR
Interaction modes:
  Inventory            collaboration on reissue, months 4–7; then X-as-a-Service via `reissue` API
  Security Engineering collaboration on partner credentials, months 4–7 (Chapter 6)
  Web & API Paths      collaboration on shared webhook delivery, months 4–8; then X-as-a-Service
  Partner APIs         X-as-a-Service: we consume the partner gateway and sandbox
On-call: own rotation from first production deploy; runbooks in the service registry
Review this API: every quarter, and whenever a mode's end date arrives
```

The middle section carries most of the design. In **collaboration**, two teams work closely on a shared problem, with blurred boundaries and high communication cost, because neither yet knows where the boundary belongs. In **X-as-a-Service**, one team consumes what another provides through a clear interface. In **facilitating**, one team helps another learn something and then steps away. Collaboration discovers the boundary, and X-as-a-Service makes it cheap to live with.

This works only if the end date is real. Teams that collaborate well tend to drift into it permanently, because nobody is obliged to define the interface that would let them stop, and a collaboration without an end date becomes one team spread across two org-chart boxes, paying the coordination cost of two teams without their independence. So Encore writes the end date into both teams' APIs and reviews it when it arrives. Resale and Inventory collaborated on reissue for one quarter, months four to seven, working in the barcode issuance code together; then Inventory published a `reissue` operation with a contract test, and the relationship became X-as-a-Service.

#### Reteaming as a capability {#c9-reteaming}

Teams change shape constantly in a growing organization, and most organizations improvise each change and then forget it. Helfand's *Dynamic Reteaming* (2nd edition, 2020), drawn from her years at AppFolio and interviews elsewhere, treats reteaming as a capability and gives it five patterns. In **one-by-one**, people join or leave a team. In **grow-and-split**, a team grows too large and divides. In **isolation**, a small group is set apart, with its own way of working, to build something new or handle an emergency. In **merging**, teams combine; in **switching**, people move between teams to spread knowledge or to grow. Her evidence is practitioner experience, so the patterns describe what happens in growing companies without promising what works.

Two practices from the same tradition have public cases. In **self-selection**, people choose their teams within stated constraints; Sandy Mamoli and David Mole ran such events for a department of about 300 people at Trade Me in New Zealand and described the method in *Creating Great Teams* (2015). The constraints make it work: each team must end with the skills it needs, and people know in advance what happens if choices do not balance. The **calibration session** is a working meeting, held when a team forms or doubles, at which it agrees its purpose, working agreements and roles instead of assuming the old habits carried over. Helfand also names anti-patterns, two of them common: breaking up a high-performing team to "spread" its performance, and reteaming by abstraction, announcing a structure without explaining what it means for the people in it.

A larger reorganization adds a sequencing problem. Larson's "Running an engineering reorg" in *An Elegant Puzzle* (2019) and Lara Hogan's communication plans in *Resilient Management* (2019) agree on the essentials: decide who hears what, in which order and through which channel, before anything is announced, and write down the questions people will ask. Managers hear first so they can answer, the people most affected hear next and in person, and everyone else hears the same day.

Encore formed the Resale team by the isolation pattern, from volunteers. Before announcing it, the engineering director for the partner area wrote a one-page reteaming FAQ: why a new team instead of a project inside Orders & Payments, who could volunteer, what would happen to the teams they left, and whether anyone could go back. There were 12 volunteers for seven engineering places. Four came from Orders & Payments, among them Katrin, who had been the discovery trio's tech lead, and three from Partner APIs, so that the team held both the purchase saga and the partner surface. Theo, a graduate, joined at month 4 as the team's first hire from outside, after these founding seven (Section 5.5). Amira, the product manager, and Paolo, the designer, who had run discovery with Katrin (the Products book's Section 1.3{% include xref.html to="products:1.3" %}), moved with the work, so the trio that wrote the bet also built it, and a staff engineer from Orders & Payments was lent to the team for nine months. In its first week the team held a calibration session and wrote the team API above.

The isolation pattern is the Eagle's pattern, which is a reason for care. Encore planned the return before the departure: the FAQ promised that anyone could go back to their old team after a year, and the plan said in advance that the Resale team would grow and split after month 18, so that its knowledge would spread through the organization.

#### The four states of a team {#c9-four-states}

Asking every team for "more velocity" treats different problems as one. Larson's "Staying on the path to high performing teams" (2018) describes four states, each with its own fix. A team **falling behind** has more work arriving than it can finish: "hire more people until the team moves into treading water." A team **treading water** keeps up but cannot reduce its backlog: "add process to consolidate the team's efforts to finish more things and reduce concurrent work", which is to say, limit work in progress. A team **repaying debt** can at last pay down its accumulated problems: "add time." A team **innovating** can take on new work: "maintain enough slack in your team's schedule that the team can build quality into their work." Figure 9.5 draws the four as a staircase.

{% include diagrams/fig-9-5.svg %}

*Figure 9.5 — The four states of a team, after Larson. Each state has its own fix, and the fix for one state is the wrong medicine for another.*

The model is a heuristic whose value is that it makes a manager diagnose before prescribing. At month four, Partner APIs was falling behind, which is why it shed webhook delivery; Inventory was repaying debt on the barcode core and needed protected time for characterization tests (Chapter 2); and the new Resale team was, by design, innovating. Section 10.2 shows how Encore's quarterly planning uses the four states.

#### Teams that jell {#c9-jell}

DeMarco and Lister called a **jelled team** a group of people so strongly knit that the whole is greater than the sum of the parts, with its own identity and momentum. Such teams cannot be built by decree; management can create the conditions in which they form, and can easily destroy them.

The evidence that stability pays is stronger than *Peopleware* could offer. Robert Huckman, Bradley Staats and David Upton studied more than 1,000 software project teams at the Indian services company Wipro (*Management Science*, 2009). **Team familiarity**, how often a team's members had worked together before, had a significant positive effect on performance, while years at the firm were not consistently related to it. Encore draws the practical conclusion: it treats the stable team as the unit to invest in, and when it breaks one up it counts a cost that the org chart does not show.

Touring crews know this well. A road crew that has loaded in and out of 100 venues together needs few words at four in the morning: each person knows where the others will be and who will catch the mistake they are about to make, and a pickup crew of equally skilled strangers is slower and more error-prone. The analogy stops at the nature of the work. A crew repeats nearly the same load-in every night, while a software team rarely does the same thing twice, so its familiarity pays off less in rehearsed motions than in knowing whom to ask, whose judgment to trust, and how far a teammate's "nearly done" is from done.

Change is still inevitable. In 1965 Bruce Tuckman proposed that small groups pass through forming, storming, norming and performing, and in 1977 he and Mary Ann Jensen added adjourning. The model is descriptive, built from a review of studies of mostly therapy and training groups, and deserves modest confidence. Hogan uses it as a reminder that a team returns to something like forming whenever its membership changes, even by one person. So when Orders & Payments lost four engineers to Resale, its manager told planning to expect a slower quarter, before anyone could be surprised by one.

**Recap.** Encore's map applies the shared vocabulary to forty teams, with enabling work carried as a second duty and only one true complicated-subsystem team. Cognitive load is used as a budget that forces hand-offs, written team APIs carry interaction modes with real end dates, and reteaming is treated as a practiced capability with its FAQ, its sequence and its calibration session. Team familiarity, which has evidence behind it, makes the stable team the unit of investment, and every change returns a team, briefly, to forming.

**Exercise 9.2.** For your team, write its team API on one page, including an interaction mode and an end date for each neighboring team. Then run the four cognitive-load questions from this section with your team and name one responsibility you would hand to another team or to the platform.

### 9.3 Product, Design, and Engineering Together

#### What forty trios need from engineering leadership {#c9-context}

The Products book's Section 1.3 introduced the product trio, and its Section 1.4 described what leaders must provide so that forty empowered teams pull in one direction: vision, principles, team topology, product strategy and team objectives, following Cagan and Jones. This section takes up the engineering half, which product writing tends to assume and engineering leaders often fail to supply.

It has three parts. The first is the team map of Section 9.2, because a trio can be empowered only over a problem its team owns, and where ownership is unclear a trio spends its weeks negotiating with neighbors over who may change what. The second is an engineering strategy, which Section 9.5 shows how to write, so that a trio choosing between a quick integration and a durable one knows which the organization prefers. The third is principles held by code. Verified Resale's product principles became the five fairness invariants of Section 1.3, tested in continuous integration; invariant 3, "Organizer caps and rules can only tighten", is a product principle, a type in the rules engine and a test that fails the build. When leadership turns the principles that must never bend into constraints the system enforces, trios can spend their autonomy on everything else.

#### Staffing the trios {#c9-staffing}

How many product managers and designers does an organization of 400 engineers need? No evidence supports any particular ratio; surveys circulate, but none measures what a ratio does to outcomes, so Encore's numbers are reasoned choices. Cagan's position is a principle: an empowered team has a product manager and a designer of its own, because discovery is their work and cannot be done part-time from elsewhere.

Encore applies the principle where discovery is continuous. It has 40 product managers: 39 across the 41 stream-aligned teams, since four mostly operational teams share two, and one in the platform group, Hana, whose customers are engineers and who was hired in month 2 as the group's first (Chapter 6). Its 24 designers make design the scarce role. Every fan and organizer team has its own designer, because those teams change what users see every week, while teams with narrow surfaces share: Box Office, Venue Entry and Venue Integrations share one designer, whose time is planned quarterly across the three. Partner APIs has its own trio, as the Products book's Section 9.4{% include xref.html to="products:9.4" %} notes, since a developer's experience of an API is designed as surely as a fan's experience of a screen.

When a trio lacks a member, the other two tend to absorb the role silently: a tech lead who also designs does both jobs less well, and a product manager who leads engineering judges feasibility without the knowledge. Encore names the gap in the team's charter, says who covers it and until when, and treats the cover as temporary.

#### The engineering manager {#c9-em}

Fournier's *The Manager's Path* describes the management ladder as a sequence of different jobs: the tech lead, who still writes code; the manager of people; the manager of managers; and the director, whose work is mostly the organization itself. Each step changes how the week is spent, and each is a place where someone excellent at the previous job can fail. The core of the people manager's job is well established: one-on-one meetings that belong to the report more than the manager, continuous feedback given close to the event, and, a level up, skip-level meetings with the people two levels down.

Hogan, in *Resilient Management*, separates three acts. **Mentoring** is sharing one's own experience and advice. **Coaching** is asking questions that help the other person find their own answer. **Sponsoring** is using one's standing to put someone forward for an opportunity they would not otherwise get. A manager who only mentors teaches people to wait for advice, and one who never sponsors leaves the quietest good engineers invisible.

Encore's first managers had none of this vocabulary. By year five it ran a programme for first-time managers: cohorts of six to eight meeting every two weeks for six months, each paired with an experienced manager from another area, with Fournier's book as the shared text. Two later pieces of machinery matter as much. The performance cycle runs twice a year, and managers calibrate their assessments together so that "exceeds expectations" means the same in Catalog as in Checkout; Larson's *The Engineering Executive's Primer* (2024) and Fournier both treat calibration as what makes reviews fair across teams. And there is succession. Larson's *An Elegant Puzzle* asks every leader to know who could take over their role, and Encore asks the same of knowledge. The barcode issuance code, written in year one, is still understood only by Lena, one of the original nine, a truck factor of one, which Section 11.2 shows Encore raising to four.

#### Writing roles down {#c9-roles}

When roles are left implicit, their overlap is decided by whoever pushes hardest, and at the top of a product team the overlap is large. Does the product manager, who owns the outcome, decide what goes into a launch, or the tech lead, who knows what is safe? Hogan's advice is to set expectations in writing, and Fournier's is to depersonalize decisions by agreeing in advance how they will be made, so that a disagreement about a decision does not become one about a person.

The tool is the **responsibility chart**: a table listing recurring decisions down one side and roles across the top, marking for each decision who decides, who is consulted and who is informed. RACI (responsible, accountable, consulted, informed) is the best-known variant; whatever the letters, each decision has exactly one person who decides.

Theatre solved this long ago. In a running show every cue is called by one person, the stage manager, from a prompt book that lists each cue and who executes it, because two people acting on the same cue a second apart is how scenery falls on actors. The responsibility chart is a team's prompt book. The comparison fails in one place: a prompt book is fixed in rehearsal, while a product team meets new kinds of decision as the product changes, so its chart must be reopened when they appear. Figure 9.6 shows the Resale team's charter.

| Decision | Product manager | Designer | Tech lead | Engineering manager | Staff engineer |
|---|---|---|---|---|---|
| Which problem to solve next | decides | consulted | consulted | informed | informed |
| Launch scope | decides | consulted | consulted | informed | consulted |
| Launch go or no-go against the memo's written criteria | decides jointly | decides jointly | decides jointly | informed | decides jointly |
| Interaction design and copy | consulted | decides | consulted | — | — |
| Technical design within the team | consulted | consulted | decides | informed | consulted |
| Cross-team technical decisions | consulted | — | consulted | informed | decides, by RFC |
| Hiring, growth and performance | consulted | consulted | consulted | decides | consulted |

*Figure 9.6 — The Resale team's responsibility chart. Each decision has one owner, except the launch call, which the Products book's Section 10.4{% include xref.html to="products:10.4" %} makes a joint decision of the trio and the staff engineer against criteria written months earlier; any one of the four can stop a launch alone.*

The chart did its most useful work before it was finished. Drafting it, the Resale trio found that the product manager and the tech lead each believed they owned launch scope, and settled it on paper in an hour.

#### Coaching and collaboration {#c9-coaching}

Cagan and Jones argue that a leader's main job is coaching: assessing each person's skills, writing a coaching plan, using the one-on-one for it, and asking people to write narratives of their thinking. It is a prescription from Cagan's consulting work at the Silicon Valley Product Group, without outcome data, and it gives leaders of forty teams something to do besides deciding on the teams' behalf.

They also argue that stakeholders such as legal, finance, sales and trust and safety belong inside discovery. The Products book's Section 1.3 makes the case that these functions shape viability; this chapter adds the working arrangement. Encore's legal counsel and a trust-and-safety lead joined the Verified Resale trio's weekly discovery sessions from the first month. Legal's earliest contribution changed the product. Under the EU's Digital Services Act (DSA), Encore is an online marketplace for resale and the fans who resell are consumers; the Act's trader-traceability rules (Article 30) would oblige Encore to vet and identify anyone reselling as a business. That became one more reason for a rule Encore had already chosen, that Verified Resale admits no professional resellers, and it was settled months before any review.

**Recap.** Engineering leadership's half of strategic context is a clear team map, a written engineering strategy, and product principles turned into constraints the code holds. Staffing ratios are choices to be reasoned about, gaps in a trio should be named and time-limited, and the engineering manager's job is a sequence of distinct jobs built on one-on-ones, feedback, calibration and succession. Writing roles down settles overlaps on paper, and stakeholders do the most good inside discovery.

**Exercise 9.3.** Write the responsibility chart for your team's leadership roles, with your five most frequent decisions down the side. Show it to every person named in it, separately, and record each cell where their answers disagree.

### 9.4 Hiring and Onboarding

#### Hiring as a system {#c9-hiring-system}

Hiring at 400 engineers is a production system with stages, defects and throughput. Larson's *The Engineering Executive's Primer* gives the elements: a documented process every hiring manager follows; hiring managers who are trained; leveling decided at offer time, from the interviews; funnel metrics that show the stage where good candidates are lost; and a hiring plan tied to the financial plan, so that open roles are a decision about money.

Should a committee outside the hiring team make the final decision? Google's hiring committees, described by Laszlo Bock in *Work Rules!* (2015), protect the bar from hiring managers under pressure, at a cost in time and distance from the team. Encore chose a narrower check: two senior engineers from outside the hiring team review the evidence for offers at staff level and above and confirm the level. Below staff, the hiring manager decides, against a written rubric.

#### Interviews that predict {#c9-interviews}

The evidence on selection is unusually good and mostly ignored. In 1998 Frank Schmidt and John Hunter combined 85 years of studies in a meta-analysis of how well selection methods predict job performance: work samples had a validity of .54, general mental ability tests .51, structured interviews .51 and unstructured interviews .38. In 2022 Paul Sackett and colleagues found that the earlier work had over-corrected for range restriction. Their revised figures are lower by .10 to .20, and the ranking changes: structured interviews come first at .42, then job-knowledge tests at .40, empirically keyed biodata at .38, work samples at .33 and cognitive ability tests at .31. Both are meta-analyses across all jobs, with no special weight on software.

What the revision supports is precise: structure matters more than format. A **structured interview** gives every candidate the same questions, or the same task, and scores the answers against criteria written in advance. A work sample scored on an interviewer's impression is an unstructured interview with a laptop; scored against a written rubric, it combines the realism of the task with the consistency the 2022 evidence ranks highest. *Peopleware* made a related point long before: to hire a juggler, ask to see the juggling, which DeMarco and Lister called an audition.

In 2013 Laszlo Bock, then running Google's people operations, told *The New York Times* that brainteasers were "a complete waste of time" and that Google had moved to structured behavioral interviews with a consistent rubric. Encore made the same move in year six, replacing puzzle questions with a 90-minute work sample on a trimmed copy of one of its own services: the candidate extends a small feature, fixes a planted bug and explains a design choice. One criterion of the rubric reads:

```yaml
criterion: reading-unfamiliar-code
question: "Before changing anything, how did the candidate learn what the code does?"
evidence_to_record: the files opened, the tests run, the questions asked
scores:
  1: edited before reading; could not explain the existing behavior
  2: read the code but missed the test that encodes the planted bug's expected behavior
  3: ran the tests first; explained the behavior; found the bug through a failing test
  4: as 3, and named a risk in the surrounding code the task did not ask about
calibration: two interviewers score independently, then compare before the debrief
```

The last line matters as much as the scores, because independent scoring keeps the loudest interviewer from setting everyone's view.

#### Hiring when candidates use AI {#c9-hiring-ai}

Coding assistants built on artificial intelligence (AI) have changed what a work sample measures, and this is emerging practice. The most detailed public account is Canva's: its engineering blog announced in June 2025 that it expects backend, machine learning and frontend candidates to use tools such as Copilot, Cursor and Claude in technical interviews, and assesses whether they can explain and defend what they accept. Meta was reported in 2025 to be introducing an AI-enabled coding interview. Neither company has published evidence that the new formats predict performance, and Canva's early results are self-reported.

Encore's rule since year nine follows Canva's reasoning because it matches the job. Assistants are allowed in the work sample, and the rubric weights what an assistant cannot do for the candidate: reading the existing code, judging generated changes, finding the planted bug and explaining the design. The criterion above survived the change unaltered, a fair sign it measured the right thing. Section 5.5 discusses what assistants do to junior engineers' learning.

#### Onboarding as a product {#c9-onboarding}

Every new engineer is a customer of the engineering system, and their first weeks are its most honest usability test. Treating **onboarding as a product** means giving it an owner, a defined journey, a measure of success and a backlog driven by that measure. The best-known public precedent is Facebook's engineering bootcamp, which Andrew Bosworth described in 2009: six weeks in which engineers had real work assigned the first time they opened their laptops, many pushed code to the live site in their first week, senior engineers rotated through as mentors, and at the end each bootcamper chose the team they would join, which gave every team a reason to be one people wanted to join.

Research confirms that most of what newcomers struggle with is social. Andrew Begel and Beth Simon followed new graduates through their first months at Microsoft and found their difficulties lay mostly in communication and collaboration. An Ju and colleagues, also at Microsoft, found three themes in successful onboarding, learning, confidence building and socialization, and found that managers chose first tasks by strategies they used without naming. A buddy, a deliberately chosen first task and introductions to the people a newcomer will depend on are what the evidence recommends.

Medicine has the oldest worked example of designed onboarding. A teaching hospital takes in a cohort of new doctors on a fixed date, gives each a curriculum and a supervisor, and grades their responsibility upward as they show they can carry it. Software can borrow the cohort, the curriculum and the graded responsibility. It differs in our favor: a newcomer's change in a well-built engineering system is reviewed, tested and can be rolled back before it harms anyone, so a software team can let a new engineer ship in week one, where a hospital waits years before letting a resident operate alone.

Encore's measure has a public precedent. In 2021 Spotify reported that the time for a new engineer to make their tenth pull request fell from over 60 days during a hiring boom to 20 after its developer portal, Backstage, was in place. The figures are self-reported, in a post promoting Backstage, but the metric is sound because it captures sustained contribution. Encore measures time to first and to tenth merged change, per cohort.

In year nine Encore gave onboarding an owner, Hana, the platform group's product manager, with the Developer Portal team building its tooling. The curriculum covers the system map, an on-sale explained by someone who has worked one, and the golden path. The buddy is assigned before the start date and never doubled up. The first task is chosen in advance and sized to merge in week one, the onboarding test Section 4.1 sets for the inner loop, made possible by Chapter 6's golden path. Figure 9.7 shows the cohorts.

{% include diagrams/fig-9-7.svg %}

*Figure 9.7 — Encore's onboarding cohorts in year nine: median days to a new engineer's first and tenth merged change, with what changed for each cohort. The first change moved into week one once the environment was ready on day one; the tenth change, which depends on people more than tools, fell more slowly.*

The two columns moved at different speeds. Tools fixed the first change, which mostly needs a working environment and a good task. The tenth depends on knowing whom to ask, how the team reviews and where the system's surprises lie, and it improved only as buddies and curriculum did.

#### Absorption rate {#c9-absorption}

A team's **absorption rate** is the number of new people it can take in over a period before its output falls. It is limited by the stock of experienced people who can teach, by the time a newcomer takes to ramp, and by how far the team's own work can pause while it teaches.

The oldest statement of the limit is Fred Brooks's, in *The Mythical Man-Month* (1975): "adding manpower to a late software project makes it later." The Architecture book's Chapter 5 opening teaches the communication arithmetic beneath it; the law adds training time and ramp-up time, which on a late project arrive exactly when there is none to spare. Brooks himself, in the 1995 anniversary edition, called the law an oversimplification, and it is one: more people can help when the work divides cleanly and the newcomers know the domain. As a warning about the general case it has held for half a century.

Larson's model and Encore's own figure turned the law into two rules. First, no team is more than a third new at any time, counting anyone who joined Encore less than six months ago, so a team of nine absorbs three newcomers and a fourth waits or goes elsewhere. The threshold is Encore's choice, with no study behind the exact number; it keeps two experienced engineers for every newcomer, so no buddy is doubled up. Second, Encore hires into teams, never into a pool, so that each offer is checked against a named team's absorption rate. When Orders & Payments lost four engineers to Resale, it backfilled two in month five and two in month 11, which kept it inside the rule.

**Recap.** Hiring is a system with a process, trained managers, leveling at offer, funnel metrics and a plan tied to money. The evidence favors structured assessment, and a work sample scored against a written rubric takes the best of both; letting candidates use assistants is emerging practice with public accounts and no validity data yet. Onboarding becomes a product with an owner and a measure, and the absorption rate, with Brooks's law as its oldest statement, sets how fast any team can grow.

**Exercise 9.4.** Find the time to first and to tenth merged change for your last five hires. For the slowest of them, identify the step that cost the most days, and decide whether onboarding or the codebase caused it.

### 9.5 Technical Leadership

#### Staff-plus roles {#c9-staff-roles}

An organization of 400 engineers needs technical leadership that does not run through management. **Staff-plus engineers** are engineers at staff level and above whose scope extends beyond one team. Larson's *Staff Engineer* (2021), built from interviews at companies such as Stripe, Slack and Dropbox, describes four archetypes. "The Tech Lead guides the approach and execution of a particular team." "The Architect is responsible for the direction, quality, and approach within a critical area." "The Solver digs deep into arbitrarily complex problems and finds an appropriate path forward." "The Right Hand extends an executive's attention, borrowing their scope and authority to operate particularly complex organizations." The archetypes come from experience, and their use is to make an organization decide which kinds it needs before it promotes anyone into a title.

Tanya Reilly's *The Staff Engineer's Path* (2022) describes the work in three pillars: big-picture thinking, execution of projects that cross teams, and leveling up the engineers around you. A staff engineer who neglects the third becomes a bottleneck with a senior title, the Eagle's failure in miniature: one person whose knowledge the organization depends on and cannot reproduce.

Encore has 26 staff-plus engineers. Most are tech leads or architects; a few are solvers attached to no team. For Verified Resale two mattered: the architect for the partner surface, a principal engineer whose area spans Public API, Partner APIs and Embeds & Channels, and the solver lent to the Resale team from Orders & Payments, chosen because the reissue path would cut through the purchase saga she knew best.

#### Working on what matters {#c9-what-matters}

A staff engineer's time is the scarcest technical resource an organization has, and the commonest way to waste it is to spend it well on the wrong things. Larson names the temptations: **snacking**, easy work that feels productive; **preening**, "low-impact, high-visibility work"; and **chasing ghosts**, a new leader's "strategy shift that fundamentally misunderstands the challenges at hand." Against these he recommends existential problems, growing others, editing others' work so it lands, finishing things, because "we only get value from finishing projects", and work that "simply won't happen if you don't do it."

Reilly offers a way to find that work in three maps. A **locator map** shows where you stand and what you can see from there. A **topographical map** shows the terrain: teams, politics, the rivers that are hard to cross. A **treasure map** shows where the organization is trying to go and what lies between. She pairs them with a frank account of finite time: a week has room for few large commitments.

The Resale team's solver drew the topographical map before writing anything. She interviewed someone in each of the 12 teams Verified Resale touches and recorded what each owned, what it feared about the bet and what it would need to say yes. Most of the 23 dependencies in the first quarterly plan ran through Inventory and Partner APIs, and the hardest was a question nobody had asked aloud: who owns reissue?

#### RFCs and design documents {#c9-rfcs}

The Architecture book's Section 15.5 describes the request for comments (RFC) loop: a short proposal circulated in writing, commented on asynchronously, decided visibly and archived, under a name that goes back to the ARPANET in 1969. An organization of forty teams must add the institutional part: when an RFC is required, who must review it, how long comments stay open and how the process ends.

Two public accounts show how large companies answered. Malte Ubl's "Design Docs at Google" (2020) describes the design document as the main tool for aligning engineers across a large organization, with sections for context and scope, goals and non-goals, the design, alternatives considered, which he calls one of the most important, and cross-cutting concerns; he is as clear about when not to write one, when the solution is obvious or the document would be only an implementation manual. Gergely Orosz's account of RFCs at Uber (2018, updated 2022) follows a process that grew from tens of engineers to a couple of thousand, from plans sent to all engineers to per-domain mailing lists with templates, and that met new challenges at a few thousand.

Encore's process is short. An RFC is required for any change to another team's interface, data or on-call load, and for any decision that is expensive to reverse. The owners of every team it touches and the area's architect must review it. Comments stay open for 10 working days, an Encore choice with a public precedent in the Rust project's "final comment period", and the author then records the decision and its reasons as an architecture decision record (ADR) in the format of the Architecture book's Section 1.4{% include xref.html to="architecture:1.4" %}. Without the time box, an RFC that touches many teams stays open until someone calls a meeting to close it, and the meeting is the slow, attendance-dependent forum the written process was meant to replace.

The reissue-ownership RFC, written by the Resale team's solver in month five, opened like this:

```markdown
# RFC-0412: Who owns reissue?
Status: open for comment until month 5, week 3 (10 working days)
Required reviewers: Inventory, Resale, Venue Entry, Orders & Payments, partner-surface architect
Problem: a resale must revoke the seller's barcode and issue the buyer's as one atomic step.
Non-goals: the partner API shape (Products book, 9.4); payout timing (Billing & Payouts)
Options:
  A. Resale issues and revokes barcodes itself, in its own service
  B. Inventory owns issuance and revocation; Resale calls a `reissue` operation
  C. A shared reissue module both teams change
Recommendation: B. One owner for every barcode; reissue stays idempotent by key (Chapter 2)
Decision record: ADR to follow on close
```

The ADR, recorded three weeks later, chose option B: the Inventory team owns issuance and revocation, and Resale calls it. Option A would have created a second writer of barcodes, and option C would have made two teams jointly responsible for the oldest and most fragile code in the company. Section 11.1 follows what that decision meant for the code.

#### Strategy from the bottom up {#c9-strategy}

Where does an engineering strategy come from in an organization too large for anyone to see all of it? Larson's answer is practical: "To write an engineering strategy, write five design documents, and pull the similarities out." For a vision, take about five strategies and forecast their implications two years ahead. In *The Engineering Executive's Primer* he returns to the method in a section titled "Shouldn't Strategy Be Bottoms-Up?" and qualifies it himself. It works best for discovering what an organization already believes, with a leader's judgment where those beliefs conflict.

Richard Rumelt's kernel, a diagnosis, a guiding policy and coherent actions, is taught in the Products book's Section 2.1{% include xref.html to="products:2.1" %}, and engineering strategy uses it too. Encore's partner-surface architect synthesized a strategy from three year-nine documents: the reissue-ownership RFC, the partner-credentials RFC that Security Engineering and Resale wrote together, and the platform group's RFC for shared webhook delivery. The diagnosis was that each partner-facing capability had been built by whichever team needed it first, so partners met three conventions. The guiding policy was one owner per partner-facing capability, with partners receiving opaque identifiers and never parsing Encore's internal formats, the lesson of the barcode-prefix breakage in Chapter 2. The coherent actions were the three RFCs, and a rule that the next partner-facing capability starts from the platform.

#### Decisions without a board {#c9-decision-groups}

Most decisions at Encore are made by the team that owns the thing decided, inside the guardrails of the Architecture book's Section 15.3{% include xref.html to="architecture:15.3" %}: scorecards, policy as code and a priced, time-boxed exception path. That book's Section 5.5 warns against a board that approves every service. A few decisions, though, must be consistent across teams and cannot be checked by a machine, such as the public API's versioning policy. They need a human forum, which must not become that board.

Larson's "Scaling technical consistency" (2018) gives the design. A centralized decision group needs a charter, saying what it decides, how decisions reach teams and how much time members give, and a membership, saying how members are chosen, how long they serve and whom they represent. "If it's six or fewer folks, it's possible for them to gel into a true team"; "If it's more than ten, you'll find it hard to even have a good discussion." Such groups "tend to be domineering, bottlenecks, status-oriented or inert," he warns, and membership "often becomes an important signal of organizational status." An escalation path is Encore's addition: it reuses the Architecture book's exception path, so a team overruled by the forum can still proceed, in the open, at its own cost.

Encore's API council has seven members serving one-year terms: the partner-surface architect as chair, the Public API team's lead, a staff engineer each from Partner APIs, Web & API Paths and Security Engineering, and two rotating staff engineers from teams that consume partner APIs. Its charter lists what it decides: the versioning and deprecation policy, including 12 months' notice of breaking changes to partners; the authentication model for new partner scopes, including the rule that each partner gets its own scopes, keys and sandbox; and the style guide's mandatory rules. It lists as explicitly what it refuses to decide: any individual endpoint, any team's internal interfaces, and anything a linter can check, which goes to Web & API Paths as policy as code. Those refusals keep the council small. A team that disagrees with it may take the exception path, and Encore expects people to disagree and then commit, in the phrase of Amazon's leadership principle, without the disagreement counting against them. Years of platform engineering inside a large bank taught me to judge such forums by whether the teams that lose an argument still bring them the next one.

#### Two ladders {#c9-ladders}

If the only way to earn more is to manage, an organization will turn its best engineers into reluctant managers. The standard answer is a **dual ladder**: a career ladder whose technical track reaches as high as the management track, in pay and standing. Dual ladders are universal at large technology companies, and the research is more sceptical than the practice. Thomas Allen and Ralph Katz surveyed nearly 1,500 engineers and scientists in nine US organizations in the 1980s and found that, with age, a growing share preferred interesting project work to promotion on *either* ladder, and they questioned the premise that productive engineers were being forced into management for money.

Both findings shaped the ladder Encore wrote in year five, when its first staff engineer said, reasonably, that she would become a manager if that was the only way to be paid like one. It runs from senior engineer through staff, senior staff and principal, paired level for level with engineering manager, senior manager, director and vice president. Fournier's chapter on writing a career ladder supplied the method, describing each level by scope and impact; Larson's promotion packets supplied the practice, a written case assembled with a manager; and sponsorship supplied the rest. A staff promotion requires a sponsor at or above the target level who has seen the work, which makes Hogan's least practiced act part of the system. And because Allen and Katz were right about what many engineers want, Encore's staff roles are defined by the problems they own.

**Recap.** Staff-plus engineers lead without managing, and an organization should decide which archetypes it needs. Their time goes furthest on finished, important work found by mapping the terrain first. RFCs with required reviewers, a time box and an ADR at the end align teams; strategy can be distilled from the documents teams already write; and the few decisions that must be consistent go to a small chartered forum with an explicit list of what it refuses to decide. A technical ladder that reaches as high as management keeps the best engineers engineering.

**Exercise 9.5.** Take one cross-team decision your organization made this year and trace it: who wrote it down, who could object and for how long, how it ended, and where the reasoning is recorded. Name the step that was missing, and say which forum, if any, should have owned it.

### Kata: The Second Shift

> **Your brief: "Pennant."** Pennant is a software-as-a-service (SaaS) platform for freight forwarders and regional carriers in the EU: it books shipments, tracks them across road, rail and sea, generates customs documents and connects to about 300 carriers through electronic data interchange (EDI) and APIs. It has 1,100 customer companies and processes about 40 million shipment events a month, with a hard peak every autumn as retailers stock up for the holidays. Pennant has 60 engineers in seven teams, and it has just raised a round that funds growth to 250 engineers in two years. Its trouble is the trouble of a company that grew up as one team. Two of its seven teams have three people each. The rate engine, which prices every booking, is understood by one engineer. Architecture is decided in a weekly meeting the chief technology officer chairs, which now has a six-week backlog. Interviews are unstructured conversations with whoever is free. New engineers take about 10 weeks to make their tenth merged change, and the board's plan assumes 95 hires in the first year, starting next quarter, two months before the autumn peak.

**Deliverables:**

1. **Target team map** — Draw Pennant's teams at 120 and at 250 engineers, with team types, owned services and the interaction mode between each pair of neighboring teams, each collaboration with an end date. Show which teams you will grow and split, and in what order.
2. **Stock-and-flow hiring plan** — Model hiring, ramping, productive engineers and attrition quarter by quarter for two years. State the absorption rule you will apply and show that the board's 95 hires either fit inside it or must be reshaped, with the autumn peak marked.
3. **Onboarding as a product** — Name an owner, a curriculum, a buddy rule and the first-week task, and set targets for time to first and tenth merged change per cohort, with the measure you will use to check them.
4. **Interview loop** — Design a work sample drawn from Pennant's own code, with a written rubric of four or five criteria and a rule for candidates' use of AI assistants, stated as emerging practice.
5. **Decision process** — Replace the weekly architecture meeting with an RFC process (when required, who reviews, the time box, the ADR) and, if needed, one chartered forum with a written list of what it decides and what it refuses to decide.
6. **Leadership roles** — Write a responsibility chart for a product team's leadership and a one-page career ladder with a technical track, and say how the rate engine's truck factor of one will be raised before the peak.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Absorption | Does the hiring plan keep every team within a stated limit of newcomers, and does it survive the autumn peak? |
| Map quality | Does every team own something real, are there no teams under four, and does each collaboration end on a date? |
| Evidence | Does the interview loop use structured, rubric-scored assessment, and is the AI rule labelled as emerging? |
| Decisions | Could a team get a cross-team decision in under three weeks without the chief technology officer in the room? |
| Knowledge risk | Who else will understand the rate engine by the peak, and how will you know? |
| Heroics | Where does your plan still depend on one person's extraordinary effort, and what replaces it? |

#### Where you now stand

You can now read an organization's growth as stocks and flows, and check a hiring plan against the rate at which teams can absorb people. You can draw a team map with a written API for each team and interaction modes that end, form a new team by a named pattern with its FAQ and calibration, and write roles down before they collide. You can design hiring around structured, rubric-scored evidence, run onboarding as a product with a measure, and give technical leadership a ladder, a decision process and a forum that knows what it will not decide. What this chapter has left aside is time and money: how forty well-designed teams plan a quarter together, how they forecast when work will be done, and how an organization funds long-lived product teams. Those are the questions of Chapter 10.

### References

- Tracy Kidder — [*The Soul of a New Machine*](https://www.hachettebookgroup.com/titles/tracy-kidder/the-soul-of-a-new-machine/9780316204552/). Little, Brown, 1981.
- Evan Ratliff — [*O, Engineers!*](https://www.wired.com/2000/12/soul/). Wired 8.12, December 2000 — free online.
- Tom DeMarco, Timothy Lister — [*Peopleware: Productive Projects and Teams*, 3rd ed.](https://www.informit.com/store/peopleware-productive-projects-and-teams-9780321934116). Addison-Wesley, 2013.
- Will Larson — [*An Elegant Puzzle: Systems of Engineering Management*](https://press.stripe.com/an-elegant-puzzle). Stripe Press, 2019.
- Will Larson — [*Staff Engineer: Leadership Beyond the Management Track*](https://staffeng.com/book/). Self-published, 2021.
- Will Larson — [*The Engineering Executive's Primer*](https://www.oreilly.com/library/view/the-engineering-executives/9781098149475/). O'Reilly, 2024.
- Matthew Skelton, Manuel Pais — [*Team Topologies*, 2nd ed.](https://teamtopologies.com/book). IT Revolution, 2025.
- Camille Fournier — [*The Manager's Path*](https://www.oreilly.com/library/view/the-managers-path/9781491973882/). O'Reilly, 2017.
- Tanya Reilly — [*The Staff Engineer's Path*](https://www.oreilly.com/library/view/the-staff-engineers/9781098118723/). O'Reilly, 2022.
- Heidi Helfand — [*Dynamic Reteaming*, 2nd ed.](https://www.oreilly.com/library/view/dynamic-reteaming-2nd/9781492061281/). O'Reilly, 2020.
- Lara Hogan — [*Resilient Management*](https://abookapart.com/products/resilient-management). A Book Apart, 2019.
- Paul R. Sackett, Charlene Zhang, Christopher M. Berry, Filip Lievens — [*Revisiting Meta-Analytic Estimates of Validity in Personnel Selection*](https://ink.library.smu.edu.sg/lkcsb_research/6894). Journal of Applied Psychology 107(11), 2022 — free online.
- Frank L. Schmidt, John E. Hunter — [*The Validity and Utility of Selection Methods in Personnel Psychology*](https://doi.org/10.1037/0033-2909.124.2.262). Psychological Bulletin 124(2), 1998.
- Robert S. Huckman, Bradley R. Staats, David M. Upton — [*Team Familiarity, Role Experience, and Performance*](https://doi.org/10.1287/mnsc.1080.0921). Management Science 55(1), 2009.
- Malte Ubl — [*Design Docs at Google*](https://www.industrialempathy.com/posts/design-docs-at-google/). industrialempathy.com, 2020 — free online.
- Marty Cagan, Chris Jones — [*Empowered: Ordinary People, Extraordinary Products*](https://www.svpg.com/books/empowered-ordinary-people-extraordinary-products/). Wiley, 2020.

---

## Chapter 10: Planning and Flow — Economics, Forecasts, and Funding {#ch10}

> A plan earns its keep on the day it tells us what to stop doing.

Forty teams can each be well designed, well led and well tooled, and the organization they form can still fail to deliver anything that matters on time. The failure lives between the teams, in the questions no single team can answer for itself. Which of the many good things we could build should come first? When will a piece of work that crosses a dozen teams actually be done, and how sure are we? Who pays for the work that keeps the lights on, and who decides when a bet has earned more money? Chapter 9 designed the teams. This chapter is about the economics, forecasts and funding that let those teams act together, and about the measures that tell an organization whether it is getting better at delivering or only better at reporting.

These questions have a long history, and much of it has been told as a triumph of control. The founding story of modern project management is the US Navy's Polaris missile programme, which put a ballistic missile on a submerged submarine years ahead of its original schedule and was credited with inventing the Program Evaluation and Review Technique, PERT, the network-and-estimate method that spread from there into every defense contract and project-management textbook. The story is true in its outline and misleading in its moral. Historians who looked closely found that PERT's greatest service to Polaris was political, and that the programme succeeded through priority, protection, a motivated organization and a willingness to cut scope. Those four things are the subject of this chapter, and we will meet them again under modern names.

Encore needs them now. At month 4 of the Verified Resale bet, in the late spring of year nine, discovery is done and the decision to build has been made. The first quarterly plan for the build shows 12 teams with work to do, 23 dependencies among them, and a launch date that nobody in the room believes. The Products book's Chapter 10 tells how the trio decided what to build. Here we follow Encore as it prices the cost of delay against the autumn tour season, makes its dependencies visible and removes the ones it can, forecasts the partner API from the throughput its teams have actually achieved, funds the bet in tranches released against learning, and measures its delivery without turning the measures into targets.

### 10.1 The Economics of Flow

#### Polaris and the network on the wall {#c10-polaris}

Late in 1955 the US Navy created a Special Projects Office to build a ballistic missile that could be launched from a submarine, and appointed Rear Admiral William F. Raborn to direct it. The office was set up deliberately outside the Navy's Bureaus of Ordnance and Aeronautics, whose rivalry might otherwise have strangled the programme. Its original target was an interim capability around 1963. Then, in October 1957, the Soviet Union launched Sputnik, and the schedule was compressed to 1960. On 20 July 1960 USS *George Washington* made the first Polaris launch from a submerged submarine, and the commander's message to President Eisenhower read, "Polaris — from out of the deep to target. Perfect." The submarine left on the Navy's first deterrent patrol that November, roughly three years ahead of the original plan by the Navy's own account. Figure 10.1 sets the dates against the plan they overtook.

{% include diagrams/fig-10-1.svg %}

*Figure 10.1 — Polaris from the Special Projects Office's creation to the first deterrent patrol, drawn as a schematic timeline. The date held because the scope gave way: the A-1 went to sea with less range and a smaller warhead than first wanted.*

The technique the programme made famous was described in 1959 in *Operations Research* by D. G. Malcolm, J. H. Roseboom and C. E. Clark of Booz, Allen & Hamilton, with W. Fazar of the Special Projects Office. PERT drew a research and development programme as a network of events joined by activities, and it asked the engineers responsible for each activity to estimate its duration "in probability terms": an optimistic time, a most likely time and a pessimistic time, combined into an expected time weighted four to one toward the most likely. The longest chain through the network, the critical path, set the date. Anyone who has watched a touring crew load into an arena has seen the same idea at work. The rigging must be flown before the lighting can hang from it, the lighting must be focused before the sound check, and the sound check must finish before the doors open, so the stage manager watches the one chain of tasks that leaves no slack and lets the others float. That was PERT's lasting gift: it made dependencies visible, and it treated a duration as a range.

Its reputation outgrew its use, as Harvey Sapolsky showed in *The Polaris System Development* (1972), a study with a chapter titled "PERT and the Myth of Managerial Effectiveness." PERT never governed most of the programme. Contractors resented it and set up units to process their data before it reached the Navy, and the Special Projects Office never evaluated whether the technique worked. Its real value, Sapolsky argued, was to give the office a reputation for management excellence, and with it the freedom to work without interference from the Pentagon, Congress and rival services. Sylvain Lenfle and Christoph Loch, drawing on Graham Spinardi's later history, summarize the point: "The image of managerial efficiency helped the project. It mattered not whether parts of the system functioned or even existed, it mattered only that certain people for a certain period of time believed that they did." What delivered Polaris was a national priority, an organization protected from its rivals, people who believed in the work, and scope that gave way when the date could not. The missile that went to sea in 1960, the A-1, had less range and a smaller warhead than the Navy had first wanted, and Lenfle and Loch describe a programme that put the schedule ahead of cost and specification and changed the specifications as it went. The full reach and yield came with later models.

We should honour both halves of this history. PERT's network thinking is real, and so is its idea that an estimate is a distribution. Its three-point estimate was a first attempt at a probabilistic forecast, and its known flaw, which MacCrimmon and Ryavec analyzed in 1964, points at the remedy Section 10.3 teaches: when several uncertain paths merge, the critical-path calculation is systematically too early, because the merge waits for whichever path finishes last. The other half is a warning about every planning artifact we will meet. A plan can be a tool that changes decisions or a performance that reassures the people watching, and the same document can be both.

#### Cost of delay {#c10-cost-of-delay}

The economic question underneath every plan is what it costs to be late. Donald Reinertsen, whose *The Principles of Product Development Flow* (2009) is the most rigorous treatment of the subject, argues that if an organization quantifies only one thing, it should be this. **Cost of delay** is the value lost for each unit of time a piece of work is not yet delivered, usually expressed per week. With it, time, scope, risk and money can be traded in one currency, and the question of whether to spend two more weeks on a feature or ship it now becomes arithmetic that anyone in the room can check, where before it was settled by argument and seniority.

Cost of delay also gives a rule for sequencing. When two pieces of work compete for the same people, do first the one with the highest cost of delay divided by its duration. Reinertsen calls this weighted shortest job first; Joshua Arnold, who applied it in practice, later named it **CD3**, cost of delay divided by duration, and the two names describe one rule. Its logic is that of a box office with one window. If one customer needs a single ticket and another needs to rebook a school trip, serving the quick one first costs the slow one a minute and saves the quick one half an hour. The analogy breaks where the economics begin: customers at a box office suffer equally per minute of waiting, while pieces of work do not, and CD3 weights the queue by that difference.

The best public account of the rule in use comes from Maersk Line, where Arnold and Özlem Yüce introduced it to an IT portfolio of about US$100 million between 2010 and 2013. Their Agile 2013 experience report is the consultants' own account, and its numbers are instructive all the same. Before the change, a quarter of requirements took more than a year to deliver. One feature needed 82 hours of work and took 46 weeks, 38 of them spent waiting, at an estimated cost of delay of about US$210,000 a week. Once cost of delay was quantified across the portfolio, the most valuable quarter of requirements turned out to be worth roughly 1,000× the least valuable quarter, and after sequencing by CD3 cycle time on the main system roughly halved. The skew is the important finding. When value is distributed that unevenly, rough estimates are good enough to sequence by.

That robustness is the condition under which cost of delay works: it is an estimate used to rank work against other work, with its assumptions written down and its ranges stated, re-estimated as information arrives. Reinertsen himself warns that intuitive estimates of it vary enormously between people looking at the same work, and the remedy is an explicit model, so that disagreement becomes a disagreement about an assumption that can be checked.

Encore wrote its model for Verified Resale on one page. The steady part of the cost had two sources: the fee shares, Encore's three points and the organizer's three, on the resales the product would complete each week, estimated from the four-show pilot in Lyon and Antwerp and the grey-market listings around the Vesper Hale tour; and the cost of the grey market it would displace, in support contacts about duplicated barcodes, chargebacks and organizers lost to other channels. Together these came to between €30,000 and €70,000 a week once the product was live. The other part was a step. Organizers sign the next year's contracts in the autumn, and the Products book's Section 2.5{% include xref.html to="products:2.5" %} made the resale clause in those contracts Encore's high-integrity commitment; if the partner API was not in Rowmate's hands by the start of October, a whole season of tours would go on sale without resale. Arnold calls this shape an urgency profile, and David Anderson's Kanban method turns such profiles into **classes of service**, standing policies for treating work of each shape: expedite, fixed date, standard and intangible. Verified Resale was fixed-date work until October and standard work after it.

| Initiative | Cost of delay (€ thousand per week, midpoint) | Duration (weeks) | CD3 | Urgency profile |
|---|---|---|---|---|
| Venue Entry scanner fleet refresh | 40 | 12 | 3.3 | Fixed date: the vendor ends support next spring |
| Verified Resale, build to launch | 50 | 32 | 1.6 | Fixed date to October, then standard |
| Festival passes in the fan app | 18 | 14 | 1.3 | Standard |
| Self-service venue onboarding in hours | 12 | 10 | 1.2 | Standard |
| Organizer Insights reporting rebuild | 9 | 20 | 0.45 | Intangible |

*Figure 10.2 — Encore's cross-team initiatives at month 4, ranked by cost of delay divided by duration. The portfolio holds five; the lowest-ranked initiative waited.*

Verified Resale did not come first in Figure 10.2, because its duration was long. CD3 rewards short jobs, so the cheapest way to raise a long initiative's priority is to make it shorter, and every week cut from the build raised the bet's ranking against everything else. That is one reason the cuts described in Section 10.3 were made early.

#### Queues are invisible inventory {#c10-queues}

A factory floor shows its inventory: half-finished parts stack up between machines where any manager can see them. Product development hides its inventory in tickets, unmerged branches and pull requests awaiting review, none of which occupies space or appears on a balance sheet. Reinertsen's central claim is that these **queues**, work that has started and is waiting for someone, are the largest hidden cost in most development organizations, and Maersk's 38 weeks of waiting in 46 is typical of what people find when they measure.

The mathematics has been taught twice already in this series, for servers, and we need only carry it across to people. The Architecture book's Section 4.3 introduced Little's law, proved by John Little in 1961: the average number of items in a stable system equals the arrival rate multiplied by the average time each item spends inside. The Resilience book's Section 2.2 developed J. F. C. Kingman's result of the same year: waiting time grows in proportion to ρ/(1−ρ), where ρ is utilization, so the wait at 95% utilization is nearly five times the wait at 80%, rising without limit toward 100%.

Applied to a team, Little's law says that cycle time is work in progress divided by throughput. A team that finishes six items a week and has 30 started will take five weeks, on average, to finish each one, however hard everyone works. The law holds for long-run averages in a stable system, and a team whose work in progress grows week by week is not stable; its future cycle times will be worse than its past ones. Applied to a reviewer, Kingman's result says that a person who is busy all the time has a long queue in front of them, and the manager pleased to see every engineer fully utilized is looking at the cause of the delays.

Encore met both laws in one place. In the first weeks of the build, months four and five, the Resale team's changes to `encore-core` took a median of a little over two working days from opening to merge, and a change touching the barcode core took a median of 11 days from first commit to production, against two for the rest of Seat Inventory & Ticketing. The Inventory team was not slow; it was full. Its engineers were committed to their own roadmap at close to all of their time, and changes touching the barcode core needed review from Lena, the one remaining author of that code and the team's busiest person before Verified Resale arrived. The remedies were the ones queueing theory suggests, and Section 4.3 tells them: reserved review time lowered utilization where it mattered, and pairing with Lena from month 5 widened the single server into three. By month 8 the median from opening a change to merging it was about seven working hours. The barcode core's own queue drained more slowly, because it emptied only as knowledge spread, and Chapter 11 follows it from 11 days to six by launch. Coding assistants can make this problem worse, because they raise the arrival rate into exactly these queues.

#### Batch size {#c10-batch-size}

If queues are the hidden inventory, large batches are one of the main ways we create them. A release of many changes, or a pull request touching 40 files, holds finished work back until the slowest part is ready and makes every downstream step bigger and riskier. The Resilience book's Chapter 4 showed why small changes are safer to deploy; the economic argument is separate.

Reinertsen frames it as a U-curve. Each batch carries a transaction cost, the fixed effort of building, testing, reviewing and deploying it, and a holding cost, the value delayed and risk accumulated while work waits for the batch to fill. Large batches spread the first thinly and pile up the second, small batches do the opposite, and the total is lowest somewhere between. Exhorting people to ship smaller therefore rarely works, because they already sit near the bottom of the curve their transaction costs allow. What moves the optimum is a lower transaction cost, which is the economic case for the fast continuous integration and trustworthy review of Chapter 4. A 31-minute build in `encore-core` gives every engineer who waits for it a reason to batch.

*Accelerate* (2018), by Nicole Forsgren, Jez Humble and Gene Kim, lists working in small batches among the capabilities that predict delivery and organizational performance, and DORA's 2024 report named small batches and robust testing as basics that AI assistance does not replace.

#### WIP and the five thieves of time {#c10-wip}

Dominica DeGrandis, in *Making Work Visible* (2017), names five thieves of a team's time: too much work in progress, unknown dependencies, unplanned work, conflicting priorities and neglected work. She calls the first the ringleader, because each of the others leaves another item started and stalled. **Work in progress**, or WIP, is everything started and not finished, and a **WIP limit** is an explicit cap on how much of it a team or an organization will carry at once. The idea is easy to state and hard to hold to, because starting something new feels like progress and finishing something old often feels like a chore.

Air traffic control offers a useful model. When weather cuts an airport's landing capacity, controllers hold aircraft on the ground at their origins, where waiting is cheap and safe, and release them at the rate the destination can absorb, instead of letting every flight take off and circle. That is a WIP limit applied to a whole network, and it works because circling aircraft burn fuel and crowd the airspace, as started work consumes attention. The analogy breaks at measurement. An airport knows its landing rate, while a portfolio's capacity is uncertain and changes as work is started, so WIP limits in software are set from observed throughput and adjusted as the queues reveal themselves.

WIP limits help when the work is visible, so that the limit is seen to bind, and when someone acts on the queues the limit exposes; a limit quietly exceeded teaches people that limits are decoration. The strongest published case near Encore's scale is Siemens Health Services, an organization of about 50 teams, reported by Daniel Vacanti and Bennet Vallet in 2014. After a WIP policy was applied across all teams in September 2012, story cycle time stabilized at about 41 days, and its 85th percentile fell from 71 days to 43. Before the policy, cycle times had grown release after release, the signature of a system Little's law calls unstable.

Encore limits WIP at two levels. Each team sets its own limits on its board. Across teams, Encore caps company-wide cross-team initiatives, those needing planned work from three or more teams, at five. The rule is Encore's own, dating from the months after Vesper Hale, when the post-incident work ran alongside four other initiatives and every one of them slipped. Verified Resale displaced the rebuild of Organizer Insights' reporting, the lowest item in Figure 10.2, which waited two quarters. The decision was uncomfortable for the team that had planned the rebuild, and the published ranking, with its assumptions on view, made it bearable.

#### Cadence and decentralized control {#c10-cadence}

Coordination is expensive when it must be arranged each time and cheap when it happens on a rhythm everyone knows. Reinertsen calls this **cadence**: a regular rhythm for planning, review and integration that makes coordination predictable. Encore's quarter, its fortnightly operating reviews and its weekly fan-app release train are cadences of this kind, and their value lies in their reliability more than their length. A team that knows the next planning point is six weeks away can defer a question with confidence.

Cadence answers when to decide; decentralized control answers who decides. Reinertsen draws on the US Marine Corps doctrine set out in *Warfighting* (1989): decisions belong where the information is freshest, with people who understand the commander's intent well enough to act on it when the plan no longer fits the ground. A central planner cannot know, week by week, whether a team should spend two more days hardening an endpoint or ship it. The team can, if it knows what delay costs.

Maersk published its cost-of-delay figures to every team so that trade-offs could be made locally, and Encore did the same. The one-page model went to all 12 teams with a decision rule: any choice that saves more than a week of the bet's critical path, at a cost of less than €50,000 in other work, may be made by the teams involved without asking anyone. Most of the trade-offs in the following months were made under that rule, several by teams the trio never heard from.

**Recap.** Polaris shows that planning can be a tool or a performance, and that priority, protection, motivation and flexible scope delivered the programme. Cost of delay puts time, scope and value in one currency and, divided by duration, sequences work, robustly because value is so skewed. Queues are inventory nobody sees, and the laws of queues apply to people. The lever on batch size is the cost of each batch, WIP limits work when someone acts on the queues they expose, and a published cost of delay lets teams decide locally.

**Exercise 10.1.** Estimate the weekly cost of delay of your team's three largest items, with the assumptions behind each and each item's urgency profile. Rank them by cost of delay divided by duration and compare that order with the order in which you are actually doing them. Where they disagree, find the assumption that would have to change for your current order to be right.

### 10.2 Planning Across 40 Teams

#### Planning in three phases {#c10-three-phases}

Most planning pain in large organizations comes from arguing about the wrong thing first. Teams arrive with roadmaps that add up to more people than the company has, and the meeting becomes a negotiation over features that is really about headcount and money. Will Larson, in the fourth chapter of *The Engineering Executive's Primer* (2024), proposes an order that dissolves much of this: first the financial plan, how much the company will spend on engineering; then the portfolio allocation, what share of that capacity goes to each area and kind of work; and only then the roadmap, what each area will build with its share. Each phase is settled before the next begins.

This is one experienced executive's prescription, widely cited and not formally studied. Its logic is that of a building budget: an architect who designs the rooms before knowing the budget designs a house nobody can afford, and the later argument about which rooms to cut is harder than the argument about money would have been. The analogy breaks because a building's budget is fixed at the start, while an engineering organization's is revisited yearly, which is why Section 10.4 replaces the annual project budget with funding that moves.

Encore runs its annual plan in that order. In year nine the envelope was roughly flat at about 400 engineers; the allocation of Section 10.4 followed; and a roadmap that asked for more than its allocation was returned with a question about what it would drop.

#### The quarterly cycle {#c10-quarterly-cycle}

The Products book's Section 2.5 explains how strategy becomes objectives and what a high-integrity commitment is. What remains here is the calendar. Encore's quarter has four fixed points. Three weeks before it begins, each team drafts objectives against the annual intent and its allocation. In the following fortnight, areas reconcile the drafts and surface the dependencies between them. In the quarter's first week a dependency session settles what crosses team boundaries. At mid-quarter each team holds a short check-in on whether its objectives are still right and its commitments at risk.

Marty Cagan and Chris Jones, in *Empowered* (2020), insist that high-integrity commitments be rare and tracked apart from ordinary objectives. At Encore a commitment has an owner, a date, the dependencies it rests on and a forecast, and it appears on the operating review's board every fortnight until it is met or explicitly renegotiated. Missing an objective is information; missing a commitment is an event leadership hears about before the date.

The two books use different commitments for Verified Resale. The Products book's is the resale clause in the autumn organizer contracts. This book's is the engineering promise that made the clause honest: the partner API, with reissue behind it, in Rowmate's sandbox by the start of October. Everything else in the build was an objective.

#### Making dependencies visible {#c10-dependencies}

A **dependency**, in planning, is a piece of work one team needs from another before its own work can finish. Each is a small contract between teams and a queue in waiting, because the providing team has its own priorities. DeGrandis advises exposing dependencies before managing them: tag them on cards, draw them as a matrix of teams against teams, and look at the picture before scheduling anything. *Accelerate* explains why: a loosely coupled architecture, in which teams test and deploy without fine-grained coordination, was among the strongest predictors of delivery performance it found.

The better response to a dependency is usually to design it out. Section 9.2 drew Encore's team boundaries so that most work starts and finishes inside one team, and a dependency that remains is a sign that the boundary does not fit this piece of work. Encore's triage gives each dependency one of three answers. **Remove** it by moving the work to the team that needs it, or by changing a boundary. **Contract** it, by turning it into a stable, self-service interface. **Coordinate** it, by putting it on the plan with a date, an owner on each side and a place on the operating review.

Verified Resale's first plan showed 23 dependencies across the 12 teams, and Encore removed nine of them by moving work, leaving the schedule alone. The Resale team took over the resale module in the fan app, which the plan had assigned to Mobile App, and Mobile App's part shrank to the release train and the version floor. Several of the other removals were of the same kind: small pieces of screen and configuration that the first plan had spread across teams for no better reason than that each team owned the screen beside them. Partner credentials and webhook delivery, two dependencies on Security Engineering and Partner APIs, became platform capabilities through the work Chapter 6 describes, and so left the plan altogether. By month 9 the plan showed 14 dependencies. Eight were contracts the Resale team consumed through documented interfaces, such as Fan Messaging's pass-replacement API. Six required real coordination, and one of them, reissue inside the barcode core, was the dependency that would block for a quarter. Chapter 11 tells what happened to it.

#### Cross-team planning events and their alternatives {#c10-planning-events}

The best-known way to plan across many teams at once is the Program Increment planning event of the Scaled Agile Framework (SAFe), in which every team on a release train meets for two days to plan the next eight to 12 weeks and map its dependencies on a shared board. It is widely adopted, and its supporters report better transparency and handling of dependencies. The evidence consists mainly of case studies, many published by the framework's own vendor, and practitioner surveys; a 2018 multivocal literature review by Abheeshta Putta, Maria Paasivaara and Casper Lassenius found the peer-reviewed evidence thin, and there are no controlled comparisons. Big-room planning may well help, and we do not know by how much.

At the other end sits Basecamp's Shape Up, whose betting table the Products book's Section 3.4{% include xref.html to="products:3.4" %} adapts for Encore. A third approach is **rolling-wave planning**: the near horizon is planned in detail and the far horizon in outline, with the detail rolled forward as the horizon approaches. It is old practice in engineering projects, and it matches what forecasting can honestly support.

Encore combines the second and third with a piece of the first. Inside teams, work is shaped and bet on in six-week chunks. Across the 12 Verified Resale teams, a one-day dependency session at the start of each quarter, attended by each team's tech lead and product manager, produces one output: the dependency map, triaged and dated. Beyond the coming quarter the plan shows milestones and forecasts, never task lists. The session borrows big-room planning's best feature, a picture of dependencies drawn by the people who own them, without asking 12 teams to plan every story together.

#### Planning for unplanned work {#c10-unplanned-work}

Every team does work nobody planned: incidents, support escalations, urgent patches, a partner's broken integration. A plan that ignores it will be missed, and the miss will be blamed on the team. The remedy is to treat unplanned work as a planned input: measure each team's historical share, reserve it, and plan the rest. Google's SRE book puts a number on the operational form, a goal of keeping toil below 50% of each engineer's time.

The Operations book's Section 3.1 described how Encore measured its toil, by having on-call engineers tag each interrupt for a quarter, and found it took about 30% of the on-call week, with the On-Sale team near 45% in the touring season. Encore extended the same tagging to all unplanned work and used it as the planning input. Each team's reserve is its own trailing two-quarter share, which averages about a fifth of capacity and runs from about one-eighth on the quietest teams to over a third for On-Sale in spring. A team with reserve left over pulls work forward; a team that overruns says so at the check-in, where the overrun is treated as a question about the work.

The four team states of Section 9.2, from Larson's *An Elegant Puzzle* (2019), apply here. A plan that gives new work to a team falling behind only deepens the hole. A steadily rising unplanned share is the early sign, and the usual answer is to reduce what flows in, by fixing the source of the interrupts or moving work elsewhere.

#### The operating review {#c10-operating-review}

A plan needs a place where it meets reality on a regular rhythm. DeGrandis, following David Anderson's Kanban method, calls it the operations review: a short, data-first meeting at which the people doing the work look at flow, commitments and risks across teams. Larson gives the underlying practice a name worth keeping, **inspected trust**: leaders trust teams to run their own work and inspect the results often enough to notice when the trust is misplaced. The evidence is practitioner experience, and the failure mode is well known. A long, ceremonial review owned by people who do not do the work turns into theatre, which is where Polaris's PERT charts ended up.

Encore's Verified Resale review meets every second Tuesday for 20 minutes around one board: the bet's items by state, the dependencies with dates and owners, and the current forecast for the commitment. It asks three questions in order. What finished, and did it teach us anything that changes the plan? What is waiting, and on whom? Has the forecast moved, and what will we cut, move or ask for? The trio runs it, the tech leads with active dependencies attend, and a director comes once a month and speaks last. When the board shows nothing new, the review ends early.

**Recap.** Settle money first, then allocation, then roadmaps, so that planning stops being a disguised fight over headcount. A quarterly cycle needs only a few fixed points, and commitments are tracked apart from objectives. Dependencies are designed out where possible, contracted where stable and coordinated only where necessary; Encore removed nine of 23 by moving work. Big-room planning has thin evidence, unplanned work is planned for from measured history, and a short, regular review keeps the plan honest.

**Exercise 10.2.** List every dependency your team's current quarter relies on. Mark each one "remove", "contract" or "coordinate", and for the first one you would remove, estimate what it would take: which work would move, to whom, and what that team would stop doing to absorb it.

### 10.3 Estimation and Forecasting

#### Why estimates disappoint {#c10-why-estimates-disappoint}

People are optimistic about their own work in a remarkably consistent way. Daniel Kahneman and Amos Tversky named the pattern the **planning fallacy** in 1979: forecasts of how long a task will take tend to be too close to the best case, even when the forecaster knows that similar tasks have run late before. Roger Buehler, Dale Griffin and Michael Ross tested it in 1994 with students writing their theses. Asked when they expected to finish, the students predicted 33.9 days on average; asked for a date by which they would finish if everything went as badly as it could, they predicted 48.6 days. They took 55.5 days, longer than their own worst case, and only about 30% finished by the date they had predicted.

Software adds two complications. The first is that estimates are often set by someone other than the person doing the work, and sometimes used as a lever. Tom DeMarco and Timothy Lister, in *Peopleware*, report a study by Michael Lawrence and Ross Jeffery of 103 Australian projects, studied in the early 1980s and scored on a weighted productivity measure. Projects whose estimates were set by the programmers did better than those whose estimates were set by supervisors, and the projects with no estimate did best of all. The data are old and correlational, and they are at least consistent with a view many practitioners share: an estimate used as pressure does not make people faster.

The second complication is the shape of the overruns. Bent Flyvbjerg and Alexander Budzier studied 1,471 IT projects and found an average cost overrun of 27%, which sounds manageable until we look at the tail. One project in six was what they called a black swan, with an average cost overrun of 200% and a schedule overrun of almost 70%. An average is a poor guide to a distribution like that, because the risk lives in the tail. Encore's own history had the same shape. Its three previous cross-team launches, Partner Listings in year six, the festival app's checkout integration in year five and rotating barcodes in year eight, were each more than half as late again as planned: 75%, 60% and 67% respectively.

#### Throughput instead of story points {#c10-throughput}

Many teams estimate in story points, a relative measure of effort, and convert them to dates by dividing by velocity, the points finished per sprint. Within one stable team this can work tolerably. Across many teams it fails, because points are a private currency: one team's five is another's eight, the scale drifts, and once outsiders watch velocity the scale inflates. A cross-team plan built on the sum of points adds numbers in different units.

Daniel Vacanti's *Actionable Agile Metrics for Predictability* (2015) proposes forecasting from what the team actually did: **cycle time**, the elapsed time from starting an item to finishing it, and **throughput**, the number of items finished per unit of time. Both come from the work tracker and need no conversion. A cycle-time scatterplot, with lines at the 50th and 85th percentiles, tells a team more about its predictability than any velocity chart, and it supports a discipline that replaces estimating each item: split work until each item is no larger than the team's 85th-percentile cycle time, and then count items. The method needs right-sized items and a reasonably stable process; it does not need items of equal size.

The Siemens Health Services report is again the strongest evidence. In a pilot of 15 teams, Siemens moved from points and velocity to WIP, cycle time and throughput. Velocity had looked healthy while features failed to finish, because teams started stories to claim their points. Afterwards cycle time fell by 42%, the first release came in on schedule and more than 10% under budget, the second completed 33% more stories, and first-pass test yield rose from 75% to 95% over two releases.

Encore stopped converting points to dates. Teams may keep points for their own conversations, but no plan above the team uses them. Each team's scorecard shows its cycle-time scatterplot and throughput, and the cumulative flow diagram, which shows how many items sit in each state over time, became the standard view at the operating review.

#### Monte Carlo forecasting {#c10-monte-carlo}

Throughput history answers a question estimates cannot: given how fast this team has actually finished work, how long will this backlog take, and with what probability? **Monte Carlo forecasting** simulates the future thousands of times by drawing weeks at random from the team's real throughput, records how long each simulated future takes to finish the backlog, and reads dates off the resulting distribution. Monte Carlo simulation is long practice in engineering and finance; its use for software delivery is documented mainly by practitioners, Vacanti and Troy Magennis among them, and Siemens ran it beside its points-based forecasts to compare the two.

It works under three conditions. The history must come from a broadly similar system, the same team doing a similar mix of work. Backlog growth must be modelled, because items split and new work is discovered, and a forecast that assumes a fixed backlog is optimistic in exactly the way PERT was. And it must be re-run weekly, because its value lies in noticing drift early. Here is the Partner APIs team's forecast as it ran at month 4:

```python
import random
weekly = [7, 9, 4, 11, 8, 6, 10, 8, 5, 9, 12, 7]   # items finished, last 12 weeks
backlog, growth = 80, (1.3, 1.65)  # growth range from past launches (the outside view)

def weeks_to_finish():
    left, weeks = backlog * random.uniform(*growth), 0
    while left > 0:
        left -= random.choice(weekly)
        weeks += 1
    return weeks

runs = sorted(weeks_to_finish() for _ in range(10_000))
for p in (50, 85, 95):
    print(f"{p}%: {runs[len(runs) * p // 100 - 1]} weeks")
```

The growth range is the line that matters most. Without it, the simulation said 11 weeks at the 85th percentile, in comfortable agreement with the team's points-based plan. With growth drawn from Encore's past launches, it said 17 weeks, which from the start of June meant the last week of September. Figure 10.3 sets these forecasts side by side. Encore committed to the start of October knowing the margin was thin.

{% include diagrams/fig-10-3.svg %}

*Figure 10.3 — Four forecasts of the same milestone, in weeks from the start of June. The first two agree with each other and with the team's hopes; the third includes the work nobody has found yet, and the fourth, the week-8 re-run, crossed the commitment before the cut brought it back.*

The weekly re-runs earned their keep in week 8. Early integration sessions with Rowmate's engineers had turned up partner-specific retry behaviour for webhooks, the backlog had grown faster than its range, and the 85% date moved three weeks past October. Nobody had to announce a slip, because the forecast announced it at the operating review two months before the date. The Partner APIs team moved bulk listing import and two reporting endpoints out of the sandbox milestone and adopted the platform's new shared webhook delivery in place of the retries it had been building. The next re-run put the 85% date back in late September, and the sandbox opened to Rowmate on 29 September.

#### The outside view {#c10-outside-view}

A forecast built from the details of the work in hand takes what Kahneman and Dan Lovallo, in 1993, called the inside view. The **outside view** begins instead from how long similar efforts have taken. Formalized as **reference-class forecasting**, it chooses a class of comparable past efforts, takes the distribution of their outcomes, places the new effort within it, and only then considers what makes this case different.

Kahneman told the story that made the idea memorable in *Thinking, Fast and Slow* (2011). In the 1970s he led a team writing a curriculum and textbook for Israeli high schools, and the team's estimates of how long it would take clustered around two years. He then asked the curriculum expert on the team, Seymour Fox, how long comparable teams had taken. Fox recalled that about 40% had never finished, and that none of those that did had taken less than seven years or more than ten. The team carried on anyway. The book took eight years, and it was never used. Fox held the outside view all along, and the inside view prevailed even after he had stated it.

Flyvbjerg has done most to make the outside view an institutional practice. His database, described with Dan Gardner in *How Big Things Get Done* (2023), covers about 16,000 projects in more than 20 fields, of which 8.5% came in on budget and on time and 0.5% on budget, on time and with the benefits promised. Governments have turned it into rules. Since 2003, supplementary guidance to the UK Treasury's *Green Book* has told appraisers of public projects to add optimism-bias uplifts to their estimates of cost and duration, percentages drawn from the record of comparable past projects.

Encore used its three previous cross-team launches as the reference class for Verified Resale. Three is a small class, and Encore knew it. But in all three the backlog had grown by between 30% and 65% after the plan was made, mostly through work discovered at boundaries between teams, and that finding went into the forecast as the growth range above. It also explained what Section 10.2's triage was for: the lateness came from cross-team waits, and removing nine dependencies attacked that cause more directly than any adjustment to an estimate could.

#### Saying no with numbers {#c10-saying-no}

A forecast changes the conversation about a date. "Can you do it by June?" invites a yes, followed later by a slip. A forecast turns the question into one about scope, date and risk together: at the current scope there is an 85% chance of finishing by this date, and to reach the earlier one with the same confidence, here is what would have to go. The Products book's Section 3.4 described appetite as a fixed budget against which a forecast is compared; when the forecast exceeds it, scope gives way, as it did for Polaris.

At month 4 the forecast for the whole launch, built from the throughput of all 12 teams and the dependency map, put the first resold ticket at month 14 at the 85th percentile, two months beyond the 12-month appetite. The Products book's Section 10.3 tells which cuts the trio made, each tested by whether the bet could still be judged afterwards: Tessera moved to after launch, festival passes left the first release, and the organizer dashboard became a monthly statement. One further cut came from the engineering side. Organizers had asked for tour-wide rule templates, and the forecast showed that templates touched the rules engine, the organizer console and the reissue path at once; in the first version, organizers set rules per event. The cuts were agreed at month 4, and as the weekly re-runs absorbed them the 85th percentile came back to month 12 by month 6, where it stayed.

This works only if leadership accepts probabilistic dates, and the commonest failure is that an 85th-percentile date becomes a promise in the retelling, although one time in seven the work will be later. Encore's guard is small and effective: every published forecast carries its percentile and the date of its last re-run, and nobody quotes a date without both.

**Recap.** The planning fallacy is consistent, estimates used as pressure do not help, and IT overruns have fat tails. Throughput and cycle time are measured rather than estimated, add up across teams, and support right-sizing in place of estimation. Monte Carlo forecasting turns throughput history into dates with probabilities, provided backlog growth is modelled and the forecast is re-run weekly. The outside view supplies that growth from comparable past efforts, and a forecast turns a demand for a date into a conversation about scope.

**Exercise 10.3.** Take your team's last 20 finished items and compute weekly throughput. Run a Monte Carlo forecast for your current backlog, once with the backlog fixed and once with a growth range drawn from your last two comparable efforts. Compare the 85th percentile of each with the date already promised, and write down what you would cut to close the gap.

### 10.4 Funding Products, Not Projects

#### From project to product {#c10-project-to-product}

Most organizations still fund software the way they fund buildings. A project is proposed with a scope, a budget and an end date, a team is assembled for it, and at the end date the team disperses and the software passes to someone else to run. Mik Kersten, in *Project to Product* (2018), argues that this fits software badly, because software is never finished and the people who understand it best are the ones who built it; project funding dissolves them just as their understanding becomes most valuable. The alternative is to fund long-lived teams by **value stream**, the sequence of activities that delivers value to a customer, and let the work flow to them.

The Products book's Section 1.1 introduced this shift and Kersten's four flow items, features, defects, risks and debt, and deferred the funding mechanics to this section. The evidence for the shift is mostly case-based, and the Flow Framework comes from Kersten's own company. The stronger support is indirect: *Accelerate*'s findings on long-lived, cross-functional teams that own their services, and Arnold's queueing argument that every project start creates a batch of work and every project end an orphan.

Encore made the change in its fourth year, at about 70 engineers, during the split into seven services the Architecture book's Chapter 5{% include xref.html to="architecture:5" %} describes. The trigger was an orphan: the project that built the first venue embeds ended, its people returned to their teams, and the embeds ran ownerless for most of a year until a venue's broken checkout exposed the gap. Since then every service has had one owning team, funded as a standing cost of its value stream, and new initiatives arrive as work for those teams.

#### Capacity allocation {#c10-capacity-allocation}

Once funding follows teams, the question becomes what share of capacity goes to each kind of work. **Capacity allocation** is that decision: dividing engineering capacity among value streams and among kinds of work such as new product, maintenance, platform and debt. It is the second of Larson's phases and the most consequential, because it decides what the roadmaps may contain. Kersten's flow distribution, the share of finished work that was features, defects, risks and debt, shows whether the allocation was honoured. There is no empirically correct split; the percentages are management choices, stated with reasons and revisited when the reasons change. Figure 10.4 shows Encore's for year nine.

{% include diagrams/fig-10-4.svg %}

*Figure 10.4 — Encore's capacity allocation for year nine. Only the first line is negotiated each quarter; the second is measured, the third is protected, and the platform line is top-sliced before allocation.*

The structure matters more than the numbers. Keeping the lights on is measured, so nobody can win capacity by understating it. Debt and risk work has a floor per team that leadership does not raid for a deadline. Only new product work is negotiated, and that is where Verified Resale's capacity came from: its planned work in 11 teams besides Resale was funded from their product share, which in four of them meant deferring roadmap features by a quarter.

The Inventory team tested the rule, because its debt work was the barcode core, which Verified Resale needed changed. A planner under pressure could have reclassified the debt floor as bet work and called it efficiency. Encore kept the characterization tests and the spreading of knowledge beyond Lena on the debt line, protected, because they were worth doing with or without the bet, and funded reissue itself from the bet. Debt work folded into a feature is usually cancelled the day the feature's priorities change, and the separation prevented that.

#### Keeping the lights on and the platform tax {#c10-platform-tax}

Two costs hide easily in a budget: keeping existing systems running, which unmeasured appears as a vague drag on every roadmap, and the platform, whose cost tends to be invisible or resented. Section 8.5 covers showback and unit economics, and the Architecture book's Section 15.5{% include xref.html to="architecture:15.5" %} the business case for a platform; this subsection covers only how both enter the budget.

Encore makes both explicit lines. Keeping the lights on is the measured 20% in Figure 10.4, and a rising share is an early warning of accumulated debt or a fragile dependency. The platform group is funded centrally, without chargeback, for the reasons given there. What this subsection adds is how the central budget appears in the plan. It is top-sliced before allocation, the 10% line of Figure 10.4, and each value stream's plan shows its share of that line as a **platform tax**: the portion of engineering capacity spent by the platform group on that stream's behalf, shown in the stream's plan though no team pays it from its own budget. The tax makes the paved road's cost visible to the people who use it, and showback, which reports each team's actual consumption, lets them see what they get for it. Neither becomes a bill a team must defend. The tax is reviewed yearly against the platform's adoption and its measured effect on delivery.

#### Funding a bet in tranches {#c10-tranches}

A bet like Verified Resale is too uncertain to fund in full at the start and too large to fund a sprint at a time. The answer, long practised in venture capital, is staged funding: money released in **tranches**, each tied to a learning milestone written in advance, with kill criteria someone has agreed to act on. Paul Gompers's 1995 study of venture financing showed how investors use staged rounds to monitor a venture and limit what they lose when it falters. Inside companies the evidence is case-based: Eric Ries's *The Lean Startup* (2011) supplied the vocabulary of innovation accounting, and Bjarte Bogsnes's account of Statoil, now Equinor, replacing its annual budget with rolling forecasts and dynamic allocation shows the finance side at the scale of a large company.

Staged funding works when the milestones are learning milestones, statements about what will be known, written before the money is spent, with kill criteria concrete enough that someone who did not write them could check them. When they are progress milestones instead, such as "integration 60% complete", every tranche is released, because progress can always be reported. The Products book's Section 10.1 shows the memo that set Verified Resale's first tranche and its kill criteria, K1 at month 4 and K2 at month 18. Its revision at month 4, after K1 had passed, set out the tranches in full:

```
VERIFIED RESALE: funding tranches (memo revision 1, month 4)
Tranche 1  Discovery, months 0–4. The trio; six weeks of two lent teams.
           Released at month 0. Gate: K1 at month 4 (passed).
Tranche 2  First partner live, months 4–12. The Resale team, and planned
           work in 11 other teams from their product share.
           Released on: K1 passed; cuts agreed that fit the forecast to appetite.
           Learning milestone, month 9: a reissued ticket's old barcode refused
           offline at a staging gate; Rowmate certifying in the sandbox.
Tranche 3  All partners, from launch. Part A: Tessera's certification, on the
           first cohort's evidence (no barcode admitted twice; resales counted
           at the door). Part B: further markets, after the month-18 review.
Kill       K1 and K2 as written at month 0. No tranche relaxes them.
```

The last line carries the discipline. A tranche can add conditions but cannot loosen a kill criterion written earlier, because the temptation to loosen them grows with every euro spent. Tranche 2 was released at month 4 on K1 and on the cuts in Section 10.3, and the re-run forecast confirmed within two months that the cuts had done their work. Part A of tranche 3 was released shortly after launch, when the first cohort had produced resales with no double admission at any gate, and funded Tessera's certification. Part B waited for the month-18 review, where the Products book's Section 10.5{% include xref.html to="products:10.5" %} records the decision to widen.

#### The finance conversation {#c10-finance}

Engineering leaders who want to fund products eventually meet the accountants, and it helps to know their terms. The central one is capitalization. Under IAS 38 *Intangible Assets*, which applies because Encore reports under International Financial Reporting Standards (IFRS), the costs of internally developed software are expensed in the research phase and may be capitalized in the development phase only when six conditions are all met: technical feasibility, the intention to complete, the ability to use or sell the result, probable future economic benefits, adequate resources to finish, and reliable measurement of the costs. Capitalized costs become an asset amortized over the software's life, which changes reported profit considerably.

The standard was written with projects in mind, and that has long pulled finance departments toward project-shaped funding, since a project has a start, an end and one asset to attach costs to. The pull is weakening. The IASB is reviewing IAS 38, and in the United States the FASB's Accounting Standards Update 2025-06, issued in September 2025, replaced the stage-based model for internal-use software with a principles-based threshold that suits incremental development better.

Encore's controller and engineering leadership agreed a practice under the current standard. Capitalization is assessed per initiative, from the work tracker's records of which items belong to which initiative, and the six criteria are assessed at the tranche gates, which give documented points at which feasibility and intention are established. Verified Resale's discovery tranche was expensed in full, and its build was capitalized from the release of tranche 2. It is offered as an illustration. The judgments involved are accounting judgments, and each organization must make them with its own controller.

**Recap.** Projects dissolve the teams that understand the software at the moment their understanding is most valuable; funding long-lived teams by value stream keeps them. Capacity allocation is a choice, best structured so that maintenance is measured, debt work is protected and only new product work is negotiated. Platforms enter the budget as an explicit tax with showback. Bets are funded in tranches against learning milestones and kill criteria that later tranches cannot loosen, and the finance conversation goes better when engineering knows how IAS 38 treats development costs.

**Exercise 10.4.** Classify your team's last quarter of finished work into features, defects, risks and debt, by count and, if you can, by effort. Compare the split with what your plan said it would be. If keeping the lights on took more than the plan allowed, find where the difference came from, and write the allocation you would propose for next quarter with a reason for each line.

### 10.5 Measuring Delivery

#### DORA for learning {#c10-dora}

The Architecture book's Section 11.2 defined DORA's delivery metrics, and Chapter 1 summarized them: change lead time, deployment frequency, change failure rate, failed deployment recovery time and, since 2024, rework rate, the share of deployments that were unplanned fixes for problems users had seen. DORA groups them into throughput and stability, and the Resilience book's Section 4.2{% include xref.html to="resilience:4.2" %} showed why the two do not trade off. The question here is what an organization does with them.

Each team uses them to find its own constraint. A team with a long lead time and a high deployment frequency is waiting somewhere before its deploys, often in review. A team with a high rework rate is shipping problems it then has to chase. Only the team knows which remedy fits, so at Encore each team sees its own five metrics on its scorecard with a trend line and nothing to compare against but its own past. Leadership sees the distribution across teams and uses it to find systemic problems, such as a platform capability that slows everyone, and never to rank teams.

Encore's median lead time was about 26 hours in year nine, with about 180 production deploys on an ordinary working day. Those numbers interest the board and tell leadership almost nothing about where to act. The distribution does. Most teams in the slowest fifth by lead time turned out to be teams whose changes passed through `encore-core`'s 31-minute build, and that is how a delivery metric became the argument for Chapter 4's investment in CI.

#### Flow metrics for the value stream {#c10-flow-metrics}

DORA's metrics begin when a change is committed, which for most features is late in the story; the weeks of shaping and waiting before the first commit are invisible to them. Kersten's **flow metrics** measure the whole value stream, from acceptance of the work to its arrival with a customer: flow velocity, the items finished; flow time, the elapsed time from start to finish; flow load, the items in progress; flow efficiency, the share of flow time in which someone was actively working on an item; and flow distribution, the mix of features, defects, risks and debt. Chapter 1 described value-stream mapping as the way to see one stream once; flow metrics watch it continuously.

They are only as good as the states recorded in the work tracker, and flow efficiency is noisy, because few teams record waiting honestly. The Flow Framework also has less independent validation than DORA's research. The published cases point the same way all the same: Maersk's 38 weeks of waiting in 46, and Siemens's flow efficiency, computed as touch time over cycle time, both show waiting dominating.

Encore measured its Verified Resale items in the first quarter of the build by adding explicit waiting states, "waiting on another team" and "waiting on review", to the work tracker of the 12 teams. Flow efficiency came to about 30%: the items spent about 70% of their elapsed time waiting, most of it in the Seat Inventory review queue and the dependencies still marked "coordinate". The number was imprecise, and Encore said so whenever it showed it, but its direction was not in doubt.

Flow time has a blind spot: it is known only when an item finishes, so the item stuck longest is the last to show up in it. **Work item age**, the time elapsed since an item started and not yet finished, sees it while it is still stuck. The Kanban Guide that Vacanti and John Coleman published in 2020 names it as one of four basic flow measures, with work in progress, throughput and cycle time. Encore applied it where its forecasts were weakest. It charts the age of every open cross-team dependency, counted from the day it was requested, against the ages at which past dependencies of the same kind closed, and an item past the 85th percentile of that history appears at the next operating review. The chart shows only that something is stuck. Somebody still has to be asked to act, and Section 11.4 tells what happened when, for three weeks, nobody was.

#### Goodhart's law {#c10-goodhart}

In 1975 Charles Goodhart, an economist advising the Bank of England, wrote about the difficulty of controlling the money supply through statistical relationships the Bank had observed. His formulation was precise and narrow: "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes." Relationships that held while nobody steered by them broke down once policy targeted them, because the people being measured changed their behaviour. The popular version is the anthropologist Marilyn Strathern's phrasing, from a 1997 essay on audit in British universities: "When a measure becomes a target, it ceases to be a good measure." In this book, **Goodhart's law** means the general principle in Strathern's words, with Goodhart's sentence as its origin: a measure that people are rewarded for moving stops telling us what it used to tell us. The social psychologist Donald Campbell reached a similar conclusion in the 1970s, arguing that the more a quantitative indicator is used for social decision-making, the more it is corrupted and the more it distorts the processes it was meant to monitor.

The best-documented modern case is Wells Fargo. The bank's community banking business pressed its employees for years to sell more products to each customer, under targets that were hard to meet honestly. On 8 September 2016 two federal regulators and the Los Angeles city attorney announced penalties totalling US$185 million, over about 1.5 million deposit accounts and about 565,000 credit-card accounts that employees might have opened without authorization; about 5,300 employees had been dismissed over five years. In August 2017 the bank raised its estimate of potentially unauthorized accounts to about 3.5 million. The independent directors' report of April 2017 named the sales culture and performance-management system, with a decentralized structure that let them go unchecked, as root causes, and in February 2020 the bank agreed to pay US$3 billion to settle investigations by the US Department of Justice and the Securities and Exchange Commission into conduct between 2002 and 2016. The cross-sell figure it had reported to investors as a sign of deep customer relationships had come to measure something else.

Software measures are corrupted the same way, less dramatically. In year eight Encore's quarterly-objectives template began to suggest deployment frequency as a goal for teams wanting to improve delivery. The Embeds & Channels team adopted it in good faith and nearly tripled its deploys within a quarter, from about four a day to about 11, while its lead time and the size of the changes reaching venues stayed the same. It had begun deploying configuration, flag changes and code for one change separately, which counted three times and delivered the same thing once. Nobody had cheated; the team had done what the objective asked. Encore removed deployment frequency from team goals. It remains on each scorecard as a signal the team can read.

#### What not to measure {#c10-what-not-to-measure}

Some measures do harm from the moment they are collected. Lines of code reward verbosity, story points compared across teams reward inflation, and utilization, which *Accelerate* singled out as a poor measure alongside velocity, rewards the full calendars that Kingman's result says lengthen every queue. Individual productivity is the most contested. In August 2023 McKinsey published "Yes, you can measure software developer productivity", which built on DORA and SPACE and proposed adding individual-level and effort measures. Gergely Orosz and Kent Beck replied in *The Pragmatic Engineer*, in a first part published on 29 August 2023, urging engineering leaders "to look to outcome and impact measurements, to identify what to measure." Both sides agree that delivery outcomes should be measured, the dispute is about individuals and effort, and on that question the history of Goodhart's law favours caution.

Encore settled its own position in writing. The engineering leadership group keeps a short list of measures it will not collect, reviewed yearly with two team representatives present:

```
Encore engineering: measures we do not collect (revision 3, year nine)
- Lines of code, commits or pull requests per person
- Story points or velocity, compared across teams
- DORA or flow metrics computed per individual
- AI usage, or accepted AI suggestions, as a goal for anyone
- Hours online, keystrokes, meeting load as a proxy for effort
- Any ranking of teams on a continuous measure
A team may track anything it finds useful for itself. Nothing on this list
enters a performance review, a promotion case or a report above the team.
```

The list exists because measures accumulate by default. A dashboard that can compute something will eventually be asked to show it, by someone with a reasonable question, and a refusal agreed in advance saves relitigating each request under pressure.

#### Measuring for the teams and for the board {#c10-for-the-board}

Larson, in the *Primer*'s chapter on measuring engineering organizations, distinguishes measures that help leaders steer from those stakeholders need, and argues for introducing them in sequence, starting with those that help the people doing the work. That practitioner judgment matches Encore's scorecard rule: each team sees its own measures in full, leadership sees trends and distributions, and nobody sees a ranking. The board needs a short account of whether engineering is delivering what the company needs, at what cost and risk, with enough detail to know where to ask questions. Figure 10.5 shows Encore's one page.

| Board page section | What it shows | Source |
|---|---|---|
| Delivery | Distribution of lead time and change failure rate across teams, trend over four quarters | Platform scorecards |
| Bets | Each funded bet: tranche, next learning milestone, forecast with percentile, kill criteria status | Operating reviews |
| Allocation | Planned against actual flow distribution; keeping-the-lights-on trend | Work tracker |
| Risk | Commitments at risk; top three systemic constraints and what is being done | Leadership review |

*Figure 10.5 — Encore's quarterly delivery page for the board. It reports distributions, bets and constraints, and names no team.*

When the page was introduced, Encore's directors asked for one ranking teams by delivery. The head of engineering declined and offered instead to bring the owner of any worrying number to the next meeting. Over the following year the directors asked for that twice, and both times the explanation was a constraint the team had already found.

The same discipline applies to AI assistance. The evidence, gathered in Section 5.1, is mixed and moving: DORA's 2024 report associated rising AI adoption with slightly lower delivery throughput and markedly lower stability, and its 2025 report found adoption associated with higher throughput and still with lower stability. Encore keeps the same delivery and flow measures and substitutes nothing for them. Its rollout of coding assistants is judged on rework rate and cycle time in the early-adopting teams against their own history, never on usage counts.

**Recap.** DORA's metrics help each team find its own constraint, and their distribution helps leadership find systemic ones; flow metrics extend the view to the whole value stream, imprecisely but usefully, and work item age shows a stuck item while it is still stuck. Goodhart's law, in Strathern's popular wording, explains why measures turned into targets stop measuring, and Wells Fargo shows the extreme. A written list of what not to collect saves an organization from its dashboards, and the board needs distributions, bets and constraints, never a ranking of teams.

**Exercise 10.5.** Write down every delivery metric your organization reports upward. For each, name one way a team could improve the number while making the work worse, and one decision the number has actually informed in the last year. Delete any metric for which you can find the first and not the second.

### Kata: The Dashboard Deadline

> **Your brief: "Halyard."** Halyard sells pension-administration software as a service to 40 occupational pension funds in two EU countries, with 180 engineers in 18 teams. The pensions regulator in its larger market requires every administrator to connect to a new pensions dashboard, through which members see all their pensions in one place, and Halyard must pass the regulator's conformance tests within nine months; any fund whose administrator misses the date is fined, and the contracts pass the fines to Halyard. Meanwhile the funds expect the roadmap promised at renewal: a contributions portal for employers and annual statements in members' own languages. Planning runs on story points converted to dates, and the last three cross-team projects came in 40%, 85% and 70% late. The dashboard work touches seven teams, and the first plan shows 19 dependencies, six of them on the Member Records team, whose median review wait is 11 days. The Connectivity team finished 6, 3, 8, 5, 7, 4, 9, 6, 2, 7, 5 and 8 items in its last 12 weeks and has 150 items in its backlog. Finance funds the work as one fixed-budget project, and the board pack ranks teams by velocity.

**Deliverables:**

1. **Cost-of-delay ranking** — Estimate the weekly cost of delay of the dashboard connection, the contributions portal and the multilingual statements, with assumptions, ranges and urgency profiles, and rank them by cost of delay divided by duration.
2. **Dependency map** — Draw the 19 dependencies, mark each remove, contract or coordinate, and show how many you can remove by moving work. Say what you would do about the review queue on Member Records, using the queueing results of Section 10.1.
3. **Monte Carlo forecast** — Forecast the Connectivity team's backlog from the throughput supplied, once with a fixed backlog and once with a growth range taken from the three past projects. Give the 50th and 85th percentiles of each and compare them with the regulator's date.
4. **Capacity allocation** — Propose an allocation for the next two quarters across new product, keeping the lights on, debt and risk, and platform, saying which lines are measured, protected or negotiated, and what the funds will be told about their roadmap.
5. **Funding and reporting** — Replace the single project budget with tranches, each with a learning milestone and a kill or escalation criterion. Then design the board's one-page delivery report, and write the list of measures Halyard will stop collecting.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Economic reasoning | Is every sequencing decision traceable to a cost of delay with its assumptions written down? |
| Dependencies designed out | Did you remove dependencies by moving work before you scheduled the rest? |
| Honest forecasting | Does the forecast model backlog growth, carry its percentile and say what will be cut if it slips? |
| Protected capacity | Are keeping the lights on and debt work measured or protected, so that no deadline can quietly absorb them? |
| Learning-based funding | Could someone who did not write the tranches tell from the evidence whether each one should be released? |
| Measures without targets | Would anything in your board report tempt a team to move a number without improving the work? |

#### Where you now stand

You can now price delay and sequence by it, see and shrink the queues between people, plan across many teams by settling money and allocation before roadmaps, and design out the dependencies that make cross-team plans fragile. You can forecast from what teams actually finish, with the probability stated and the undiscovered work modelled, and cut scope before a slip has to be announced. You can fund long-lived teams, protect the work that keeps systems healthy, release money to a bet as it learns, and measure delivery without inviting teams to game the measure. Chapter 11 follows a single change, the reissue of a ticket under a new barcode, from the first characterization test in Encore's oldest code to the first resold ticket scanned at a gate, and shows these practices working together with everything else this book has covered.

### References

- Donald G. Reinertsen — [*The Principles of Product Development Flow: Second Generation Lean Product Development*](https://openlibrary.org/isbn/9781935401001). Celeritas Publishing, 2009.
- Dominica DeGrandis — [*Making Work Visible: Exposing Time Theft to Optimize Work & Flow*](https://itrevolution.com/product/making-work-visible/). IT Revolution, 2017.
- Daniel S. Vacanti — [*Actionable Agile Metrics for Predictability*](https://actionableagile.com/books/aamfp/). ActionableAgile Press, 2015.
- Daniel Vacanti, Bennet Vallet — [*Actionable Metrics at Siemens Health Services*](https://www.agilealliance.org/wp-content/uploads/2016/11/ActionableMetricsAtSiemensHealthServices.pdf). Agile Alliance Experience Report, 2014 — free online.
- Joshua J. Arnold, Özlem Yüce — [*Black Swan Farming using Cost of Delay*](https://blackswanfarming.com/black-swan-farming-using-cost-of-delay). Agile 2013 experience report, IEEE, 2013 — free online.
- Sylvain Lenfle, Christoph Loch — [*Lost Roots: How Project Management Came to Emphasize Control over Flexibility and Novelty*](https://www.sylvainlenfle.fr/images/Publications/Lost_Roots_R2_VF.pdf). California Management Review 53(1), 2010 — free online.
- Harvey M. Sapolsky — *The Polaris System Development: Bureaucratic and Programmatic Success in Government*. Harvard University Press, 1972.
- D. G. Malcolm, J. H. Roseboom, C. E. Clark, W. Fazar — [*Application of a Technique for Research and Development Program Evaluation*](https://doi.org/10.1287/opre.7.5.646). Operations Research 7(5), 1959.
- Bent Flyvbjerg, Dan Gardner — [*How Big Things Get Done*](https://www.penguinrandomhouse.com/books/672118/how-big-things-get-done-by-bent-flyvbjerg-and-dan-gardner/). Currency, 2023.
- Bent Flyvbjerg, Alexander Budzier — [*Why Your IT Project May Be Riskier Than You Think*](https://arxiv.org/abs/1304.0265). Harvard Business Review 89(9), 2011 — free online.
- Mik Kersten — [*Project to Product*](https://itrevolution.com/product/project-to-product/). IT Revolution, 2018.
- Will Larson — [*The Engineering Executive's Primer*](https://lethain.com/eng-execs-primer/). O'Reilly, 2024. And *An Elegant Puzzle*. Stripe Press, 2019.
- Nicole Forsgren, Jez Humble, Gene Kim — [*Accelerate*](https://itrevolution.com/product/accelerate/). IT Revolution, 2018.
- DORA — [*Accelerate State of DevOps Report 2024*](https://dora.dev/research/2024/dora-report/). Google Cloud, 2024. And [*State of AI-assisted Software Development*](https://dora.dev/research/2025/dora-report/). Google Cloud, 2025 — free online.
- Daniel Vacanti, John Coleman — [*The Kanban Guide*](https://kanbanguides.org/the-kanban-guide/2020.12). Kanban Guides, 2020 — free online.
- Marilyn Strathern — *"Improving ratings": audit in the British University system*. European Review 5(3), 1997.

---

## Chapter 11: Capstone — One Change, from Legacy Core to Production {#ch11}

> A change is not finished while the old way still works somewhere.

For about four decades, from the 1950s into the 1980s, programmers stored the year as two digits. Storage was scarce and expensive, the century seemed far off, and "67" meant 1967 to every program that read it. The US General Accounting Office (GAO) later put the consequence in one plain sentence of its 1997 guide: in a two-digit field, the year 2000 cannot be told from 1900. The article usually credited with turning years of quiet warnings into public alarm is Peter de Jager's "Doomsday 2000", in *Computerworld* on 6 September 1993. What followed was a single, small change that had to be made in nearly every computer system in the world, much of it in code whose authors had retired, moved on or died, and all of it against a date that could not be moved. The US Senate's Special Committee on the Year 2000 Technology Problem, chaired by Robert Bennett with Christopher Dodd as vice chair, described the effort in its final report of 29 February 2000 as "one of the most complex and vast management challenges in recent history", and dated it plainly: "From roughly 1995–1999, private and public organizations … mobilized huge resources." Nobody knows what it cost in total, and the committee said so; the estimates it collected for the United States alone ranged from about $100 billion (the Commerce Department) to $225 billion (Gartner).

The way the work was organized deserves more attention than the money. The GAO's *Year 2000 Computing Crisis: An Assessment Guide*, published as an exposure draft in February 1997 and in final form that September, set out five phases that agencies and, in practice, most large organizations followed: awareness; assessment, which meant finding and listing every system and deciding which mattered; renovation, which it summarized as "Convert, replace, or eliminate"; validation; and implementation. It told agencies to "plan and manage the Year 2000 program as a single large information system development effort", and it reported, with some alarm, that "only half of the 24 departments and major agencies reported that they completed the assessment phase by the end of August 1997". The guide also warned that "the testing and validation process may consume over half of the Year 2000 program resources and budget." Martyn Thomas, who led Deloitte's international Y2K services, adds a second lesson in his 2017 Gresham College lecture. Organizations that chose to replace old systems "could not resist adding new features", and where those projects met the deadline, "testing was cut short, leading to later failures that were rarely publicised as having been Y2K related." Under a fixed date, the rewrite was the risky path.

Then the date arrived, and almost nothing happened. The Senate report recorded that "hundreds of computer problems have been reported since January 1, 2000, but most have been quickly corrected and none have caused serious disruptions." Its appendix lists the kind of thing that did go wrong, such as 800 slot machines in Delaware that shut down after reading the date as 1 January 1900. In Britain the worst case surfaced later: a hospital pathology system had miscalculated mothers' ages from January 2000, and more than 150 pregnant women were wrongly told they were at low risk in screening for Down's syndrome. The quiet invited an argument, never settled, about whether the work had been needed at all, and Section 11.5 returns to it, because the review of any successful change meets the same argument in miniature.

Encore's version of the problem was smaller and its date was its own, but the shape was the same. Chapter 1 described a ticket identity derived from the order and the seat, written by the original nine engineers in the first year, recomputed in four other places since and, as Chapter 5's migration would find, read out of the barcode at 60 more, and a product that could not exist until that identity could change. This capstone follows that one change, the ability to reissue a ticket under a new identity, from the first characterization test in the barcode core at month 4 of the bet to the engineering review held at month 24, a year after launch. The Products book's capstone (its Chapter 10) follows the same 18 months as a bet: why Encore made it, whether it paid, and what the month-18 review of the memo decided. This chapter follows the code and the engineering system that changed it, and reports what the practices of Chapters 2 to 10 yielded when applied to one change at once. Figure 11.1 lays the change out in time.

| Month | What changed in the code and the engineering system | Taught in |
|---|---|---|
| 2 | Partners told the barcode format will change; old format accepted on the partner API until month 14 | The Products book, Section 9.4 |
| 4 | Resale team formed; 23 dependencies planned; first Monte Carlo forecast; Resale repository created from the template | Sections 1.3, 9.2, 10.3 |
| 5 | Reissue-ownership request for comments (RFC) closes in an architecture decision record (ADR); pairing on the barcode core begins | Sections 9.5, 2.3 |
| 6 | Characterization suite of 1,400 cases in continuous integration (CI); format campaign begins | Sections 2.4, 5.2 |
| 7 | Inventory publishes `reissue` with a contract test; the Resale–Inventory collaboration ends | Sections 9.2, 3.3 |
| 8 | Legacy barcode parser deprecated; 56 of 60 call sites moved | Sections 2.5, 5.3 |
| 9 | Walking skeleton end to end; partner API in sandbox; dependencies down to 14 | Sections 3.2, 6.4, 10.2 |
| 10–12 | Six weeks on trunk behind flags; reissue drill on a test event; Rowmate certified | Sections 4.5, 8.3 |
| 12 | Launch in France; the first resold ticket scans in Lyon | Section 11.4 |
| 13–15 | Issue variants deleted; last parsers moved; most flags removed; Tessera live | Sections 2.3, 4.5 |
| 24 | Engineering review: codebase, platform, teams | Section 11.5 |

*Figure 11.1 — One change through two years. The middle column is what this chapter reports; the right-hand column is where each practice is taught, so that the chapter can report it without teaching it again.*

### 11.1 The Change

#### What reissue asks of the code {#c11-what-reissue-asks}

A change that crosses a dozen teams is easiest to grasp by asking what must be true once it is done, and for reissue there were four things. A ticket must be voidable and reissuable as one atomic step, so that at no moment are there two live tickets for one seat, or none. The seller's old identity must stop working at every gate, including gates with no network when the crowd arrives. The buyer must receive the new ticket, which at Encore means the rotating barcode in the app first and the wallet pass where one exists, because wallet updates are best effort and Apple Wallet passes at Encore do not rotate. And the money and the record must agree: both legs of the reissue in the event stream, and the fee split in the finance ledger that is reconciled daily. Section 8.2 explained why reissue is the trust mechanism of the whole marketplace; here the four requirements are a route through code.

Traced through the services, the route is longer than the product description suggests. The Resale service, new, holds the listing and starts the purchase. Orders & Payments runs the resale purchase saga through the primary payment service provider's (PSP's) marketplace product, which splits the money four ways. Seat Inventory & Ticketing, owned by the Inventory team, performs the reissue inside the barcode core, and publishes `TicketReissued` and `TicketRevoked`. Venue Entry turns the revocation into an entry on the lists its scanners hold. Fan Messaging replaces passes and tells both fans what happened. The Mobile App team's ticket view must show a reissued ticket correctly in every app version still in use. Billing & Payouts meters the fee and pays the seller five days after the event. Every service but the first already existed, and each was built on the implicit assumption that a ticket's identity never changes once issued. Like the two-digit year, it was a representation decided once, early, for good reasons, and then left visible to every piece of code that cared to read it.

#### Who owns reissue {#c11-who-owns-reissue}

Section 9.5 printed the opening of RFC-0412, the request for comments that asked whether Resale or Inventory should own reissue, and the ADR that settled it three weeks later: the Inventory team owns issuance and revocation, and Resale calls it. What the RFC could not show was the consequence. The objection raised most often in its comment period came from inside Inventory. The team was being asked to own the hardest new code in the bet, in a module that one of its members, Lena, understood and nobody else did, while it also carried the on-call load of the seat ledger. The ADR answered by making the objection a condition. Inventory would own reissue, and the plan would fund making the module understandable by more than one person before the first production reissue, tracked as a dependency in its own right. The ownership decision and the knowledge problem of Section 11.2 were, in the end, one decision.

#### The map and the forecast {#c11-map-forecast}

Chapter 1 showed the 23 dependencies of the first quarterly plan, drawn in month 4 and grouped by the team that had to deliver, with a column, added by a Resale engineer, recording the age of the oldest code each one touched. Over the next five months, during building, the plan cut them to 14. Section 10.2 gave the rule: remove a dependency by moving the work, contract it where the interface is stable, and coordinate only what is left. Figure 11.2 shows where the nine went, and every one of them went by moving work.

{% include diagrams/fig-11-2.svg %}

*Figure 11.2 — Verified Resale's dependencies at the first quarterly plan and at month 9, one square for each, by the team that had to deliver. Three ways of moving work account for all nine cuts (six taken over by Resale, two moved to the platform, one folded into a change already planned), and none of them was a decision to skip the work; VR-01, inside the barcode core, was among the 14 that stayed.*

Each of the three moves is a general one. A requesting team doing the work itself, in its own code or in another team's code under that team's review, is the commonest, and inside another team's code it is InnerSource at the scale of a single pull request (Section 8.4); it works only where the owner has written down how it accepts contributions, and it is easiest where the requester can build on an event the owner already publishes, as Resale did with `TicketIssued`, provided the event's schema is registered and its consumers hold message contracts (Section 3.3). The platform taking over a capability removes the dependency for every later team as well as this one, which is why Chapter 6 treats the partner-facing path as an investment. And folding a request into a change the owner was making anyway removes a coordination point without adding work. Of the 14 that remained, eight were contracts consumed through documented interfaces and six needed real coordination; the hardest of the six, reissue inside the barcode core, is the subject of Section 11.4.

The forecast is where this chapter can show what no other chapter can: how wrong it was, and in which direction. In month 4 the Monte Carlo simulation that Section 10.3 builds put the 85th percentile of the launch at month 14, two months past the appetite. The scope cuts that the Products book's Section 10.3{% include xref.html to="products:10.3" %} records (Tessera after launch, festival passes deferred, the organizer dashboard replaced by a statement) and the one engineering added (no tour-wide rule templates) were agreed against that number at month 4, and as the weekly re-runs absorbed them the 85th percentile came back to month 12 by month 6 and stayed there. The launch came in month 12. The date was about right, and much of what lay beneath it was not. The backlog for launch grew by about 40%, from about 120 items in month 4 to about 170 by month 9, as work was split and discovery added things nobody had planned, such as pairs listed together; that was inside the 30–65% growth the outside view had supplied, which is why the date held. And the item that came closest to breaking the date was one the simulation could not see clearly. It drew on Inventory's past throughput, in which the barcode core hardly figured, so it could not foresee the queue that formed when at least 14 changes arrived at the core's one reviewer within a few months. Waiting of that kind leaves no trace in a throughput history until it has happened, and Section 11.4 tells how a different instrument showed it.

#### The plan that was not a rewrite {#c11-not-a-rewrite}

Section 2.4 gave Encore's reasons for changing the barcode core in place: Bellotti's counsel on momentum, Feathers's algorithm, and a definition of done written in one sentence before the work began. What the Y2K record adds is a sharper view of the alternative. Thomas lists three remediation methods: expanding dates to four digits, windowing two-digit years, and replacing the system. Many organizations repaired their code in place, and those that chose replacement under the deadline, in his account, often cut testing short. The rewrite, which feels like the thorough option, was the one most exposed to a fixed date, because it had to reproduce all of the old behavior before it could ship any of the new. Encore's date was its own, the 12-month appetite, with the autumn contract season as a step in the cost of delay (Section 10.1), and the same reasoning applied.

The narrower decision was which pattern to use, and the Architecture book's Section 3.4{% include xref.html to="architecture:3.4" %} supplies the terms. The strangler fig replaces a system piece by piece behind a facade; Martin Fowler, who named it in 2004 and revised the description in 2024, judges that "the reduced risk and earlier value from the gradual approach outweigh its costs". But the barcode core was a library inside one service, called in-process, and the tool for replacing a component inside a codebase is branch by abstraction, the strangler's smaller relative. Encore kept the strangler in reserve, as its plan said, and never needed it. The choice was right for one reason above the others: the code could be put under test. Feathers's procedure assumes that, and where it is false, where the old code cannot be characterized because its behavior depends on state nobody can reproduce, the strangler's facade and a parallel run become the safer course.

#### What engineering promised {#c11-what-engineering-promised}

The funding of the bet, in tranches tied to what each stage would learn, belongs to Section 10.4 and the Products book's Section 10.1{% include xref.html to="products:10.1" %}, and this chapter does not retell it. Engineering's part of the promise fitted in three lines of the month-4 plan. It gave the forecast as a range with its percentile stated, never as a date. It kept the preparation of the barcode core, the characterization tests and the spreading of knowledge beyond Lena, as its own line on Inventory's protected debt allocation (Section 10.4), about a fifth of Inventory's capacity for two quarters, apart from the reissue work the bet funded, so that it could not be squeezed out of the reissue estimate. And it reserved capacity after launch for cleanup, on the ground that a change whose cleanup is unfunded leaves two systems running. That last line was the one most often questioned; Section 11.4 shows it was needed.

**Recap.** Reissue asked four things of the code, and every service on its route had been built on a ticket identity that never changed. The ownership verdict became a condition: Inventory would own the hardest new code, and the plan would pay to spread its knowledge first. The dependency map shrank because work moved to the teams that needed it, to the platform, or into changes already planned, and the forecast was about right on the date while missing the one queue that nearly broke it. The plan repaired the old code in place because the old code could be put under test.

**Exercise 11.1.** For a change you are planning, write the one-page plan: what must be true of the code afterward, stated as properties a test could check; who owns each part; why you are not rewriting; and the line item for cleanup after launch. Then take your dependency list and, for each item, ask which of Figure 11.2's three moves of work could remove it.

### 11.2 Preparing the Old Code

#### What the survey found {#c11-survey-found}

Section 2.4 described how the Inventory team built a characterization suite for the barcode core by replaying a year of issuance requests, with personal data removed, through the issuer in a test harness. By month 6 the suite held 1,400 cases and ran in CI, the first visible win the plan had promised. What Section 2.4 could not report was the result of reading it. The replay, together with the property tests that followed it, surfaced 31 behaviors that no document, ticket or living memory specified, and the team had to decide, for each, whether reissue would preserve it.

Nineteen were kept on purpose, because something outside the module depended on them. Festival passes carry the festival's code in place of any day's event code, and the door-scanning app relies on that to admit a pass holder on any day of the festival. A rescheduled event keeps its original event code, and the Support Tools console had been built around that fact. Accidents had become promises the moment another team leaned on them, and each such test was renamed as a specification naming the team that relied on it. Nine more belonged only to the old format, among them the older check-digit scheme carried by tickets issued before the year-four split into services. Every event those tickets were for had long since passed, so the behavior could be deleted with the format, and Section 11.4 reports that it was. The last three were bugs. The most serious was the one Section 3.3's property test found in its first week, an interleaving in which the old code wrote the new ticket before revoking the old one, so that for one step two tickets were live for the same seat. It had never mattered while tickets were issued only once.

Of 31 surprises in eight-year-old code, three were bugs and 19 were load-bearing. A team that treated the module's oddities as defects to clean away would have been wrong almost two times in three. The GAO's warning that validation could consume more than half of a Y2K program's budget is the same lesson in money. Most of the cost of changing old code safely lies in finding out what it does and who depends on it, and only a small part lies in the change.

#### The seam and the parallel run {#c11-seam-parallel-run}

Thomas, closing his lecture, relays an observation of Peter Neumann's that states the root cause better than any account of two-digit fields: "systematic use of concepts such as abstraction, encapsulation, information hiding, and object-orientation could have allowed the construction of efficient programs in which the representation of dates could be changed easily when needed." That is David Parnas's 1972 criterion for decomposing systems into modules, hide each decision likely to change behind an interface, which the Architecture book takes up in its Section 1.3. Y2K was expensive because the representation of a date had no seam around it. Changing it meant finding and changing every program that read it. A **seam**, in Feathers's sense, is a place where behavior can be altered without editing the code at that place; seen against Y2K, it is information hiding added late, at the cost of finding everyone who had been reading what should have been hidden.

The barcode core's seam was the identity. Before the change every caller computed a ticket's identity or parsed it from the barcode; after it, every caller asked one interface. Two tidyings of the kind Beck describes in *Tidy First?* came before the seam could be cut: the identity computation, repeated inside the issuer's 19 public variants, was moved into the pinch point Section 2.4 found, the one method every variant finally calls, and the module that held both formatting and persistence was split in two, so that the format could change without touching the code that wrote to the ledger. Neither changed behavior, and together they made the seam a small change. Figure 11.3 shows the identity before and after it.

{% include diagrams/fig-11-3.svg %}

*Figure 11.3 — The barcode core's identity before and after the seam. Before, every reader, including code outside Encore's repositories, reached the representation itself; after, each asks one interface, and the representation behind it can change.*

Characterization tests describe the past, and the team wanted evidence from real traffic before it trusted the new path with every ticket's identity. The best public precedent is GitHub's: in December 2015 Vicent Martí described how GitHub replaced the merge implementation behind its merge button, which had shelled out to Git, with one built on libgit2. Its Scientist library ran the old and new implementations side by side on real requests, always returned the old result, and logged every mismatch. The experiment began at 1% of requests and found, among other things, two bugs in Git itself; in one, 768 conflicts were reported as none, because a shell keeps only the low eight bits of an exit code. The new code ran at 100% for 24 hours with no mismatches before the old code was removed. Encore ran the same pattern on identity, as Section 4.5 describes. For three weeks in month 8, every issuance computed the identity both ways, the derived identity and the new opaque one with its lookup, served the old result and logged any case where the lookup disagreed with what the old derivation implied. There were two mismatches, both for tickets issued while an event was being rescheduled, and both were cases the characterization suite had pinned for the old code without anyone asking how the new code should treat them. A parallel run of this kind is a characterization test run against the present, and it finds exactly the cases that a replay of the past has not yet seen.

#### From one to four {#c11-one-to-four}

Thomas tells of a moment in the late 1990s when COBOL programmers came out of retirement and commanded high salaries. That is a truck factor paid for at the last minute, at the market's price. Encore paid for its own early. From month 5 the Inventory team paired two engineers, one of them Jonas, with Lena on every change to the barcode core, and Jonas began the written guide to the module that Section 2.3 mentions. Ines, the Inventory staff engineer who sponsored the call-site migration in Section 5.2, learned the module from the outside in, by reading every characterization test that failed during the migration and asking Lena why. Once, in month 7, the whole Inventory team spent a week on the module as an ensemble, all of them working on the seam at one screen, an Encore choice drawn from practitioner writing such as Woody Zuill and Kevin Meadows's *Software Teaming*, with no controlled study behind it.

The guide is worth describing, because it was the most durable of the four remedies. A stage manager keeps a prompt book: the script annotated with every cue, every blocking change and the reason behind each, so that the show can be run by someone who was not at the rehearsals. Jonas's guide was a prompt book for the barcode core. It recorded each of the 19 kept behaviors with the team that relied on it, the history of each format, and the questions reviewers had asked most often, with Lena's answers. The analogy breaks at the moment of reading. A prompt book is read during the show by someone who knows they need it; a guide to code is needed by whoever is about to change the code, often without knowing it, so the guide was linked from the template of every pull request that touched the core.

Section 2.3 cautioned that truck-factor algorithms measure authorship, which is only a proxy for understanding, so Encore measured the truck factor the same way before and after, in two parts: the knowledge map of authorship and review from version control, and a simple test of understanding, whether each person had made or reviewed a change to the core in the last quarter without needing Lena. By month 12 four people passed both: Lena, Ines, Jonas and the second engineer paired with Lena. The plan's definition of done had asked for at least three. The best evidence, though, was behavioral. A change to the core had taken a median of eleven days from first commit to production in Section 2.3's analysis, mostly in the queue for one reviewer; by launch it took six.

#### The format change as a campaign {#c11-format-campaign}

Every Y2K program began with an inventory, and Thomas recounts how often that step failed: in one FTSE 100 group, none of 60 departmental IT directors "was confident that they could rebuild their key systems without introducing errors." Encore's inventory of everything that read the old identity came from its code index and the change-coupling analysis of Section 2.3, and it found 60 call sites in 11 repositories owned by seven teams. Section 5.2 described how an agent generated one change per call site and a ladder of checks decided which landed, and Section 5.3 told of Venue Entry's rejection of a change that was exactly wrong for a scanner with no network. This chapter adds only the outcome. Fifty-six of the 60 had landed by month 8, six weeks after the campaign began. The legacy parser was then deprecated, with an allowlist naming the four callers that remained (Section 2.5): Venue Entry's offline path, which needed a new design; the Support Tools console; a Sales Analytics job; and the Finance platform team's reconciliation report. The long tail took seven more months, which is the usual shape of such work, because each of the last callers had a reason of its own to be last.

The partner side ran on a different clock. Partners had been told in month 2 that reissued tickets would carry a new, opaque identity, and the old format was accepted on the partner API until month 14, which kept the promise of 12 months' notice. Under Verified Resale partners never see a barcode at all. They receive an opaque `ticket_id` through the API, as Section 2.5 and Section 3.3 explained, so the notice protected only integrations left over from Partner Listings. Rowmate's was one of them. Its parser of the old event-code prefix had survived the move to rotating barcodes in year eight unnoticed, because rotation left the identity alone, and it was found and replaced during Rowmate's sandbox certification in month 9, where the sandbox's deliberately different `ticket_id` format made it fail on Rowmate's own schedule.

Y2K supplied one more practice, and it was the most useful thing on the campaign's single page. Thomas describes the four rules for how software should handle dates that the British Standards Institution published in January 1997, quotes the fourth of them, "Year 2000 must be recognized as a leap year", and adds that the rules "were increasingly referenced in contracts and audit standards." Such a definition turns "are you compliant?" into a checklist a team can sign. Encore wrote its own, called it reissue-ready, and asked each of the 12 teams to sign its copy. Inventory's read:

```
REISSUE-READY (each of the 12 teams signs its own copy)
1. No code we own derives a ticket's identity from order and seat
2. No code we own parses a barcode; event and holder come from the identity lookup
3. Every consumer we own of TicketReissued and TicketRevoked holds a message contract
4. A ticket may be reissued more than once; a retried reissue with the same key is a no-op
5. Old-format barcodes keep working until their events have passed
6. Our part of the reissue drill passed on the test event
7. Copies of our code running outside our repositories are listed, with owner and version
Team: Inventory      Signed: Lena, Ines      Month: 10 (line 7 added month 11)
```

The seventh line was not in the first version, and Section 11.4 explains how it got there.

#### Debt paid and debt taken {#c11-debt-paid-taken}

The most widely used Y2K remedy was a deliberate debt. **Windowing** kept years as two digits and interpreted them through a pivot: in the example Thomas gives, "years 00 to 19 would be treated as 2000 to 2019 whereas years 20 to 99 would be treated as 1920 to 1999." It was cheaper and simpler to test than expanding dates to four digits, and the last of the disadvantages Thomas lists is the one that matters here: "it was not a permanent solution." The Senate's final report warned that remediated software "may encounter problems with the approach of the 'pivot year'", and that organizations "must undertake permanent software fixes where temporary patches were utilized." Windowing was technical debt in Cunningham's sense, whose metaphor is Chapter 2's touchstone, and it came with a built-in trigger: the pivot year. Where the record of the trigger was kept, the debt was repaid; where it was lost, the trigger fired anyway.

Encore paid one debt and took another, and wrote both down. The debt paid was INV-DEBT-017 from Section 2.3, the 19 public issue variants, whose trigger required repayment before the first production reissue; Section 11.4 reports how that trigger was moved, in writing, and the debt repaid. The debt taken was Encore's own pivot year. Tickets sold before launch carry the old, derived identity, and they must keep working until their events have passed, so every gate validator and the issuer itself carry two paths until the last of those events. The team entered it in the register in month 6, before the campaign began:

```yaml
- id: INV-DEBT-031
  where: venue-entry validator; ticketing/barcode/LegacyFormat.kt
  what: old-format tickets (identity derived from order and seat) still accepted
  why taken: tickets sold before launch must work until their events pass
  interest: two validation paths at every gate; every scanner test runs twice
  owner: Venue Entry (validator), Inventory (format)
  trigger: the day after the last event holding an old-format ticket (month 29)
  also: partner API accepts old-format references until month 14 (12-month notice)
  repay: delete both old paths and their replay tests in one change
  decided: month 6, Year 9
```

The trigger is a date computed from data, the latest event for which an old-format ticket was sold, and it is written where the owners will see it every quarter. That is all the Y2K record asks of a temporary fix. It does not ask that the fix be avoided, only that its expiry be written down by someone who will still be there when it arrives, which is why the entry names teams. Figure 11.4 sets the two pivot years side by side.

{% include diagrams/fig-11-4.svg %}

*Figure 11.4 — Two pivot years. Windowing read two-digit years through a pivot, and Encore accepts old-format tickets until a dated trigger; both are temporary fixes with a built-in trigger, and the trigger fires whether or not anyone kept a record of it.*

**Recap.** Reading the characterization suite found 31 unspecified behaviors, of which 19 were load-bearing and three were bugs, so most of the work of changing old code lay in learning what it did. The seam was information hiding added late, as Y2K's root cause suggests, and a parallel run in production checked it against the present. Knowledge of the core spread to four people by pairing, an ensemble week and a guide kept like a prompt book. The format campaign moved 56 of 60 call sites in six weeks and the rest in seven months, under a written definition of done; the old format stays, as debt with a dated trigger.

**Exercise 11.2.** Write the first characterization test for the oldest code your next feature must change, before any new code. Then, for the first three surprising behaviors your tests reveal, find out who depends on each, and decide in writing whether it is a bug, a promise, or something to delete with the old path.

### 11.3 Building the New Parts

#### Twenty-three days to the first deploy {#c11-first-deploy}

The Resale service was created from the golden-path template on the day the team formed, and in the sense that matters to the template it existed from that day: a repository, a pipeline, a registry entry and a scorecard. Its first production deploy that served real traffic came 23 working days later, and Section 6.2 mapped why in its Figure 6.3. Fifteen of the 23 were waits: nine for partner credentials, which could then be issued only through two tickets to Security Engineering, and six for a security review of a webhook sender that the team should never have had to write. Neither wait was anyone's failure. The platform had no road for either need, so the team took the only roads there were. The platform group built the two missing roads as the partner-facing path, and the second partner-facing service to start after shared webhook delivery reached general availability, the Festivals team's festival feed, reached its first production deploy in four working days (Section 6.5). The Resale service was born on the golden path and still waited three weeks, because the path ended before its needs did, and the cost of those weeks was paid once.

Once deployed, the service grew as Section 3.2 described, from a walking skeleton that ran one test fan's resale from a stub of Rowmate's integration through Resale, Orders & Payments and Inventory to a revocation list on one venue's scanners and a new ticket in the app. The skeleton ran end to end in month 9, as planned, with none of the plan's slack left: it went almost entirely on the step that crossed into the barcode core, where the entry point had to be written behind characterization tests that did not yet cover reissue. That is the skeleton doing its job: it forced the hardest cross-team question, how a reissue enters the barcode core, into month 5, when it was cheap to answer.

#### Contracts, simulators and the invariants {#c11-contracts-invariants}

Chapter 3 taught the testing of Verified Resale; this subsection gives the counts. By launch the contract broker held 26 consumer contracts against the services on the resale path, nine of them message contracts on events; the Inventory team's reissue endpoint alone had three consumers within a month of existing, and the broker showed all of them on every pull request Inventory opened. One of the simulators of Figure 3.5 caught the most expensive bug of the build. In the PSP simulator's fee-split mode, a split rejected by the provider left the resale saga waiting for a confirmation that would never come, holding the buyer's payment authorization and the seller's listing for the full hold window. No end-to-end test would have found it, because the real provider's sandbox never rejects a split. The fix was a compensating step in the saga, and the simulator mode stayed in the suite.

Section 1.3 called the five fairness invariants an engineering contract, and Section 3.3 promised that they would run as property tests on every build. Here they are, in the file the Resale team hosts and every contributing team's build runs:

```kotlin
// Runs in CI for Resale, Inventory, Orders & Payments, Partner APIs and the rules engine.
// Changed only through the host team's review (Section 8.4).
class FairnessInvariants {
    private val world = ResaleWorld.inMemory()   // real rules engine; simulated neighbors

    @Property fun `Partners never buy primary tickets`(@ForAll("partnerCalls") s: Script) =
        world.run(s).primaryPurchasesBy(PARTNER).isEmpty()
    @Property fun `Only tickets bought through the Gate, within the per-fan limit, can be listed`(@ForAll("listings") s: Script) =
        world.run(s).listings.all { it.boughtThroughGate && it.withinPerFanLimit }
    @Property fun `Organizer caps and rules can only tighten`(@ForAll("ruleEdits") s: Script) =
        world.run(s).ruleHistory.zipWithNext().all { (before, after) -> after.isNoLooserThan(before) }
    @Property fun `Every resale buyer passes Bot Screening and the per-buyer limits`(@ForAll("purchases") s: Script) =
        world.run(s).resales.all { it.buyerScreened && it.withinPerBuyerLimit }
    @Property fun `Partners never see sales-velocity data`(@ForAll("partnerReads") s: Script) =
        world.run(s).partnerResponses.none { it.revealsVelocity() }
}
```

Each test's name is the invariant, word for word, so that a failing build reports the broken promise in the language of the product. Between month 9 and launch the five properties failed 11 times on pull requests. Seven failures were in tests or generators, and four were real: two rule contributions that could, in combination, loosen a limit, one listing path that skipped the per-fan check for tickets bought in a presale, and one partner endpoint whose error message, on a rejected listing, quoted a remaining-inventory count precise enough to estimate velocity. Each was fixed before it merged. None of the four came from the code the team was most worried about.

Partners, tenants and entitlements have their homes elsewhere: organizer rules are typed configuration built on the entitlement machinery of Section 7.3, and the partner program is Section 8.3's. One part of that program belongs in a chapter about tests. The certification suite is versioned with the partner API, and each partner runs it against the sandbox from its own code, again on every major version and after any change to how it handles listings or payments (Section 8.3). It is the only test of Verified Resale that runs in someone else's code. It is where Rowmate's old prefix parser was found, and where Tessera's stale price cache was caught when an organizer tightened a cap in the middle of a run (Section 8.3).

#### Six weeks on trunk {#c11-six-weeks-trunk}

Verified Resale's pieces went to trunk behind release flags from month 4, and for the last six weeks before launch the complete flow ran dark in production behind one of them, `resale-verified-flow`, as Section 4.5 described; in the fan app the Resale module shipped dark on eight release trains before any fan saw it. Cross-team reviews, which had stalled for two days early on, settled under the latency targets Section 4.3 describes once the team made its changes smaller.

The detail of the loop that matters for the rest of this chapter is a field. Every release flag Verified Resale created, 17 across the services and the app, was created with an owner and a removal date, in the way Section 4.5 teaches. The date for `resale-verified-flow`, the main one, was month 14, after the second launch cohort. Writing a date into a flag costs nothing on the day it is created, and Section 11.4 shows what it was worth a year later.

#### The assistant, briefly {#c11-assistant}

The organizer rule assistant, Verified Resale's one AI feature, was designed in the Products book's Section 6.5{% include xref.html to="products:6.5" %} and evaluated by the criteria and golden set that Section 3.5 describes. For this chapter its one engineering point is structural. The assistant drafts a typed rule set, and the type cannot express a loosening, so invariant 3 is enforced by the schema and checked by the property test above, whatever the model says; the organizer confirms every draft before it applies.

**Recap.** The Resale service was born on the golden path and still waited 23 days, because the path ended before its needs did; the platform closed the gap once, for everyone. The skeleton surfaced the hardest cross-team question early. Contracts, simulators and five properties named after the invariants caught real defects before they merged, and the certification suite carried the same discipline into partners' code. Every flag was born with a removal date.

**Exercise 11.3.** For one feature you are building, write each invariant it must never break as a sentence a customer would understand, then name the test that would fail if it broke. Where no test exists, write the property's name and its generator before writing the code it protects.

### 11.4 Shipping Across Forty Teams

#### Integration without a big bang {#c11-integration}

Chapter 1 named the big-bang integration as one of the ways large changes fail, with TSB's migration of 2018 as the public case, and Encore's defense was the ordinary one: every team's work met every other team's on trunk, daily, behind flags, from the walking skeleton onward. The defense worked. No integration between two services on the resale path surprised anyone after month 9, because contracts, simulators and the hourly synthetic resale had exercised each of them long before launch. Chapter 6 told the platform's part whole: the partner credentials and webhook delivery that the Resale team would otherwise have built for itself were built once by the platform group and adopted by every partner-facing team, and the three home-grown webhook senders were retired in a campaign that ran from month 9 to month 11.

One integration did surprise everyone, and it came from outside the repositories. In month 11 Encore ran a reissue drill on a test event at each design-partner venue, an exercise in the spirit of the clock-forward tests that Y2K programs ran on their plants and the rollover drills the Senate report mentions: scripted fans resold tickets to one another, and real devices at real gates tried both the old and the new barcodes. At one venue, an arena whose turnstiles came from an access-control vendor, the turnstiles refused the buyer's new ticket. The vendor's firmware did not use Venue Entry's validator. It had been built years earlier to an Encore integration specification, maintained through the Venue Integrations team's connector, and it computed a ticket's identity from the order and the seat, exactly as the year-one code had done. To that firmware, a revoked ticket for seat B-14 meant that seat B-14 was revoked, whoever now held it. The code index had not found it because it was not Encore's code, and the reissue-ready definition had asked each team only about code it owned.

The GAO's guide had warned of exactly this in 1997: agencies "must not only test Year 2000 compliance of individual applications, but also the complex interactions between scores of converted or replaced computer platforms … and interfaces." A touring crew learns the same thing from the advance, the visit before the show when the production manager walks the venue and checks the house's own equipment against the rider, because the band's gear has been rehearsed and the house's has not. The analogy breaks at the scale. An advance covers one building, while a revocation list is consulted by every device that has ever been integrated with the format, and Encore had no list of those devices in one place. The vendor shipped corrected firmware in four weeks, and Venue Entry agreed that the arena's events would not open to resale until it was installed, which it was, a week before launch. And the reissue-ready definition gained its seventh line, which asked every team to list the copies of its logic running outside its repositories, with owner and version. The Venue Integrations team's list turned up two more vendor integrations built to the same old specification, at venues not yet in any launch cohort.

#### The dependency that blocked {#c11-dependency-blocked}

Chapter 1 predicted a dependency that would block for a quarter, and Section 10.2 named Verified Resale's: VR-01, the void and reissue in one step inside the barcode core, whose entry Chapter 1 printed. It did hold the bet for about a quarter, though not in the way the plan had feared. The fear was that the work would never reach the top of Inventory's backlog. It reached the top at once, because the ADR had made it Inventory's, and from month 4 Resale and Inventory worked on it together, as Section 9.2 describes. What held it was the order Feathers's procedure imposes and the queue in front of one person. Nothing in the core could change until the core was under test, the characterization suite reached CI only in month 6, and in the first weeks every change that touched the core waited for Lena, at a median of 11 days from first commit to production (Section 10.1).

The instrument that showed how long it was taking was work item age, which Section 10.5 introduces: for a dependency, the time since it was requested. Encore charts the age of every open cross-team dependency against the ages at which past dependencies of the same kind closed. By day 20 VR-01 had passed the 85th percentile of that history, and the chart showed it at the next fortnightly operating review. For three more weeks nobody changed anything, which is the honest part of the story. The chart could not say whether the item was stuck or merely large, and each team read it as the other's to act on: Resale assumed Inventory had the matter in hand, and Inventory assumed that a collaboration meant Resale would say if it was not. The review then made two decisions. Inventory set aside review time each day and widened the circle of reviewers through the pairing already under way (Section 4.3), and the item was split, so that the narrow entry point the walking skeleton needed could land behind the first characterization tests while the full operation waited for the rest. Inventory published `reissue` with a contract test in month 7, 61 working days after the dependency was requested, and from then on Resale consumed it as a service.

The lesson the teams drew was about the chart. A dependency's age is the earliest warning a plan has, and it is useful only if the plan says, before any item is stuck, who acts when an item crosses the line; Encore's plans now name that person for each coordinated dependency. Of the other five, Mobile App's came closest to trouble, since the reissue-aware ticket view had to ride the weekly release train and old app versions linger; the soft floor on app versions was raised three months before launch, as the Products book's Section 8.2{% include xref.html to="products:8.2" %} describes, so that nearly every active phone could show a reissued ticket by launch day.

#### The first resold ticket, through the code {#c11-first-ticket}

The first resold ticket was a Lyon fan's: a seat at a sold-out Saturday concert promoted by one of the design-partner organizers, with a face value of €80. The Products book's Section 10.4 follows it through the product, as the fans and the partner experienced it. Figure 11.5 follows it through the code, naming at each step the service and operation involved, the team that owns it, and the test that would fail if that step broke.

| Step | When | Code path | Owner | Test that protects it |
|---|---|---|---|---|
| 1 | Tuesday evening | Rowmate calls `POST /listings` with `validateOnly`, then creates the listing | Partner APIs, Resale | Rowmate's certification suite; listing contract |
| 2 | Tuesday evening | Rules engine checks Gate purchase, per-fan limit, window and the €80 cap | Resale | Invariants 2 and 3 as properties |
| 3 | Thursday lunchtime | Buyer scored by Bot Screening; per-buyer limit applied | Bot Screening, Resale | Invariant 4; shadow mode for new rules |
| 4 | Thursday lunchtime | Resale purchase saga; €88 through the primary PSP's split product | Orders & Payments | PSP simulator in split mode; the money property |
| 5 | Thursday lunchtime | `reissue` with an idempotency key; `TicketReissued`, `TicketRevoked` | Inventory | Stateful reissue property; characterization suite |
| 6 | Within 30 s | Revocation reaches the venue's lists; scanners sync | Venue Entry | Hourly synthetic resale with a scripted scanner |
| 7 | Minutes later | Seller's pass voided, buyer's ticket in the app, pass where offered | Fan Messaging, Mobile App | Wallet simulator's stale-pass mode; app ticket-view tests |
| 8 | Minutes later | Signed `listing.sold` webhook to Rowmate, which fetches the result | Partner APIs (platform delivery) | Partner simulator's duplicate and late webhooks |
| 9 | Thursday | `ResaleCompleted` metered: €3.20, €2.40, €2.40; ledger reconciles | Billing & Payouts | Message contract on `ResaleCompleted`; daily reconciliation |
| 10 | Saturday evening | Buyer's rotating code validated at the gate, offline if need be | Venue Entry | The resale end-to-end journey; the reissue drill |

*Figure 11.5 — The first resold ticket, through the code. Ten steps, nine owning teams, and a test for every step; the seller's €80, paid five days later by Billing & Payouts, is covered by the money property of step 4.*

Read down the last column and a pattern appears that no single chapter could show. Seven of the ten tests run inside Encore's own repositories on every build. Three are different. Rowmate's certification suite runs in a partner's code; the hourly synthetic resale runs in production; and the reissue drill ran on real devices at real gates. Those three are the only tests on the route that reach code Encore does not build or environments it does not control, and the drill was the only one of all ten that could have found the turnstile firmware. A test strategy for a change like this one is mostly a matter of pushing tests down to where they are cheap, as Chapter 3 teaches, and then deliberately keeping the few that reach outward, because the parts of the route nobody owns in a repository are where a change's surprises live.

#### Cleaning up {#c11-cleaning-up}

The Senate's final report closes its domestic findings with an item that was easy to skim in February 2000: organizations "may need to address non-mission critical systems where repairs were postponed", and "internationally, most fixes were temporary clock rollbacks that ultimately must be fixed permanently." It is the long tail, named by the official record of a change everyone remembers as finished on 1 January. Uber's published account shows the scale of the problem in our own field. Its engineers built a tool called Piranha to remove stale feature flags automatically, described it at the International Conference on Software Engineering in 2020, and reported on the company's blog that it had been used to remove around two thousand stale flags.

Encore had funded its cleanup in the month-4 plan, and it went as follows. Of the 17 release flags, 15 were removed by month 16. `resale-verified-flow`, due at month 14, came out in month 15, two weeks late, because its removal waited for Tessera's certification; Section 4.5 records what its deletion took with it, and what went with Inventory's `ticket-identity-opaque`. Two were kept deliberately as operational kill switches, resale on or off per market, owned and documented as permanent, a legitimate change of kind because it was recorded as one. INV-DEBT-017 did not meet its own trigger. It said the 19 issue variants would be collapsed before the first production reissue, but in month 11 Inventory judged that collapsing them weeks before launch was a greater risk than carrying them, since Reissue reached the old issuer only through the pinch point the tests covered, and it re-dated the entry to month 13 in the register, with that reason beside the new date. The variants were collapsed into one `issue()` with a typed request in month 13, and the old check-digit path went with them. The last four callers of the legacy parser moved by month 15, the Finance platform team's reconciliation report last, and the parser was deleted the same week. One piece of the old world remains, on purpose: INV-DEBT-031, the acceptance of old-format tickets at the gates, waits for its trigger in month 29.

**Recap.** Integration on trunk worked as designed, and the one surprise came from code outside every repository, found only by a rehearsal on real devices. The dependency that blocked, reissue inside the barcode core, was visible on an aging chart three weeks before anyone acted, and it closed after a quarter once review time was reserved and the item was split. Traced through the code, the first resold ticket crossed ten steps and nine teams, and only the three tests that reached outside Encore's repositories could have found what the others missed. Cleanup was funded in advance and finished, except for the one debt whose trigger has not yet arrived.

**Exercise 11.4.** For one transaction of your product, list every place its code runs: your own services, and also a partner's system, a device, a vendor's firmware, an old app version. For each place outside your repositories, name the test, drill or inventory that would find a fault there before a customer did, and mark the places where the honest answer is none.

### 11.5 What the Engineering System Learned

#### The review at month 24 {#c11-review}

The Products book's Section 10.5 records the review of the bet at month 18, about six months after launch, which asked whether Verified Resale had worked as a product and decided to widen it. The engineering review came six months later, at month 24, a year after launch, for a reason the two reviews' subjects explain. Product metrics answer within months, while the effects of a change on a codebase, a platform and an organization take a year or more to show, and a review held too early would have measured only the construction. It compared the system with the plan of month 4 and the definition of done of Section 2.4, under one rule above the rest: every number had to be measured by the same instrument as its baseline, or it was left out. A developer survey with new questions, or a truck factor computed by a different algorithm, cannot show change, only difference.

#### The codebase a year later {#c11-codebase-later}

Meir Lehman's second law of software evolution, which Chapter 1 quoted, holds that a program's complexity increases as it is changed "unless work is done to maintain or reduce it." The month-24 review is, among other things, a test of that clause, and Figure 11.6 sets out the result for the barcode core and the new code beside it.

| Measure | Month 4 | Month 12 (launch) | Month 24 |
|---|---|---|---|
| Barcode core, lines of Kotlin | about 11,000 | about 12,300 | about 7,600 |
| Public issue variants | 19 | 19 | 1 |
| Tests on the core | a handful | 1,400 characterization cases, plus properties | about 450 specification tests; replay kept for the old format |
| Median days, first commit to production, for a core change | 11 | 6 | 2 |
| Truck factor, by knowledge map and review test | 1 | 4 | 4 |
| Callers parsing the barcode | 60 | 2 | 0 |
| Verified Resale release flags | — | 17 | 2, kept as kill switches |
| Top hotspot in resale code | — | Resale purchase saga | Rules engine |

*Figure 11.6 — The codebase at month 24, measured by the same instruments as at month 4. The core grew during the change and shrank after it; the hotspot moved into the new code.*

The core's line count tells Lehman's story in two movements. It grew by about 1,300 lines during the change, as Reissue was sprouted beside the issuer and the seams were cut, and it fell by about 4,700 after launch, when the 19 variants collapsed into one and the old check-digit path was deleted. Both movements were planned, and the second happened only because it had been funded. The median time for a change to the core fell from eleven days to two, the same as the rest of Seat Inventory & Ticketing, the most useful single measure of a repaired legacy core. Lena still works on it. She reviewed fewer than one in five of its changes in the last quarter before the review, where at month 4 she had reviewed all of them.

The new code is where Lehman's law reasserts itself. The hottest file in the resale code at month 24 was the rules engine's evaluator, which six teams now contribute to (Section 8.4), and its complexity had risen with every contributed rule type. The festival-pass cap kind alone added a third to the evaluator's branching. Six teams adding reasonable rules to one evaluator is exactly the condition under which the second law operates, and the review's response was the one the law's final clause implies: an item in the debt register, owned by the host team, with a trigger set at the next rule type contributed, to restructure the evaluator before it grows further.

#### The platform a year later {#c11-platform-later}

What the platform absorbed from this change is easy to state, since Chapter 6 tells how. Partner credentials became self-service, webhook delivery became a platform capability with one implementation instead of three, and both were packaged as the partner-facing path. By month 24 three more partner-facing services had been created on it, and their median time to first production deploy was five working days, against the Resale team's 23. Section 6.5 cautioned that one service is not a trend; three is the beginning of one. The rules engine is the change's other contribution to shared code, an InnerSource project with six contributing teams, Resale as host with Orders & Payments, Inventory, Trust & Safety, Pricing & Presales and Festivals, which is how festival passes reached it.

The quarterly developer survey of Section 1.2, its ten core items unchanged and still answered by about two thirds of engineers, gave the review its other comparison. "Building plumbing the platform should provide, such as partner webhooks" had been one of the six commonest answers in Figure 1.3, named by 24%, and by month 24 it had dropped out of the six. Waiting for CI on the shared repository had not. Test selection and a remote cache had brought the build of `encore-core` down from 31 minutes to nine, as Section 4.2 describes, but engineers who worked in the oldest repository still ranked its feedback time among their pains, and the review said plainly that the change had made the barcode core easier to change without making its repository faster to build.

#### The teams a year later {#c11-teams-later}

The organization belongs to the review of the bet, and the Products book's Section 10.5{% include xref.html to="products:10.5" %} records it: the Resale team, grown from its first seven engineers to 15 people by month 18, split after that review along the line between the fan and partner flows and the organizer's rules, as its reteaming plan had said from the start (Section 9.2). What the engineering review adds is what the split and its neighbors did to the flow of knowledge. Two of the original volunteers took up the reteaming FAQ's promise and returned to Orders & Payments after a year, taking a working knowledge of the resale saga with them, and the staff engineer lent from Orders & Payments returned on schedule after nine months.

The interaction modes changed in the way Section 9.2 recommends, from collaboration toward service. Inventory and Resale worked as one group in the barcode core from month 4 to month 7, and since then Resale has consumed reissue as an operation behind a published interface with an owner, an objective and a contract test, without meetings; at month 24 neither team could name a change to the interface that had needed one. Planning changed in one small, durable way, and it came from the column a Resale engineer added to the dependency list in month 4. Encore's quarterly plan template now asks, for every cross-team dependency, for the age of the oldest code it touches and the number of people who understand that code, and planners read those columns before the estimates.

#### What AI changed and what it did not {#c11-ai-changed}

Where assistance measurably helped this change is narrow, and Chapter 5 documents it: in the format campaign an agent generated the changes for 60 call sites, and a ladder of checks caught what it got wrong. The published accounts have the same shape. Google's 2025 paper on migrations with large language models reports that about 74% of the changes and 69% of the edits in 39 migrations were generated by a model, with time savings the developers estimated, and Airbnb's account of moving nearly 3,500 test files in six weeks against an estimate of a year and a half rests on the existing test suite to judge each change. In every published success of this kind, the machine wrote the edits, and tests, compilers and human owners decided which ones landed.

Where assistance did not change the work is where most of the work was. The four callers that took seven months were not slow because their edits were hard to write. They were slow because each needed a decision only its owner could make, such as how a scanner with no network should learn which tickets are valid. The 31 behaviors in the characterization suite were classified by people who asked Lena, and the turnstile firmware was found by a drill. Engineers used assistants constantly to read unfamiliar code and draft tests, and reported that it helped, but no controlled study measures how much assistance speeds the understanding of legacy code, and Encore's own evidence on that point is testimony.

Y2K offers a precedent whose outcome is known, which is more than any recent anecdote can claim. Thomas reports that repair costs estimated in 1996 at "$1 to $2 per line" fell to "only a few pennies per line because automated Y2K tools became extremely accurate and efficient at fixing the code", and that organizations which started late "were able to make up the lost time." Automated transformation made the change itself cheap, and testing was still expected to take more than half of the money. That is the honest forecast for AI-assisted change: the edit gets cheaper, while the proving, the deciding and the finding of what the inventory missed stay where they were.

#### The Crisis Moved {#c11-crisis-moved}

The argument about Y2K began almost as soon as the date passed, and it has two serious sides. The Senate committee concluded that "the level of effort was justified, and the expenditures of the public and private sectors were indeed necessary", and Thomas called the episode "a signal event: a near miss". John Quiggin, writing in 2005, argued the opposite: that "most money spent specifically on Y2K compliance exercises was wasted", that a strategy of fixing failures as they appeared would have served, and that countries such as Italy, which did far less, suffered little. The Senate's own report holds a rebuttal: late countries "greatly benefited from the lessons learned by countries leading the world" and often "simply rolled back computer clocks". Neither side can win outright, because the counterfactual cannot be audited. A prevention that succeeds looks exactly like one that was not needed. The only defense is the one Encore's review used: write down beforehand what failure would look like, so that its absence can be judged. Encore's plan said, in month 4, that a failed reissue would show as a revoked ticket admitted or a valid one refused at a gate. In its first year there was neither, and the drill had found the one place that would have produced the second.

Chapter 1 opened at Garmisch in 1968, with a conference that named a gap between what organizations needed to build and what their methods could build, and promised that this last chapter would return to ask how much of the gap has closed. One change at Encore gives a partial answer. Every practice this chapter has reported, from characterization tests and seams to contracts, platforms, flow measures and agent-written migrations, closes part of the gap, and each worked here roughly as its chapter promised. And the gap was still there, because it had moved. It was no longer in writing code that works, which Encore's teams did well and its tools did faster. It was in knowing what the old code did and who depended on it, in the one queue a forecast could not see, in firmware that no repository held, and in the patience to delete what had been replaced. The crisis Garmisch named has not ended. It has moved from construction to understanding, and from the program to the organization that changes it.

I have come to think that this is what an engineering system is for. Y2K's root cause was a representation decided once and never hidden, and its remedy was mostly inventory and testing, by organizations discovering under a deadline how little they knew about their own systems. Encore's barcode identity was the same kind of decision, and Encore had the time and the practices to change it without a crisis. Neither the time nor the practices came free. They came from an organization that had built, deliberately, the second system this book has been about, the one that builds the first. That system does not make large changes easy. It makes them ordinary, which at 400 engineers is the most that can be asked of it.

The Resilience book picks up where this one stops, with what it takes to keep the system standing when a million fans arrive at once, and its Chapter 9 covers the readiness review that every launch, including this one, has to pass. The Operations book takes the morning itself, when the system and the people who run it meet the load together.

**Recap.** The engineering review came a year after launch, with every number measured by its baseline instrument. The barcode core grew during the change and shrank after it, as the second law allows when work is done, while the new rules engine became the hotspot. The platform absorbed what the change needed, the Resale team split as planned, and AI made the edits cheap without making the understanding cheaper. The crisis that Garmisch named has moved from writing code to understanding and changing it, and an engineering system is how an organization keeps up with it.

**Exercise 11.5.** Write a review of a large change your organization finished at least a year ago, against what was planned and measured by the same instruments as the baseline. Before reading any results, write down what failure would have looked like, so that its absence can be judged. Then list what the change left behind (flags, old paths, compatibility code, debt with triggers), with an owner and the date on which each will go; any item that has neither is the review's first finding.

### Kata: The Lease That Changes Hands

> **Your brief: "Lintelby."** Lintelby is a software-as-a-service company for long-term residential lettings, with 220 engineers in 25 teams; about 4,000 letting agencies in six EU countries run some 900,000 active leases on it. Tenants who must leave early today find a replacement, end the lease and sign a new one, which takes weeks and loses deposits in transit. The board wants lease transfer: a departing tenant hands the lease to a new tenant found through a partner letting agent, the landlord approves, the deposit moves, and the new tenant is referenced and screened like any other. The tenancy core was written in the company's first year, eleven years ago. Its lease identifier is built from the property reference and the start date, and 70 places in Lintelby's code, plus the integrations of 25 partner agents and three deposit-protection schemes, read the property reference out of it. One engineer understands the core well, and she begins parental leave in three months. The deposit ledger must reconcile to the cent every night, partner terms promise nine months' notice of breaking changes, and the busiest moving season of the year begins in eight months.

**Deliverables:**

1. **The change plan** — One page: what must be true of the code once a lease can change hands, written as properties; who owns each part; why you will repair the tenancy core in place, and what would make you switch to a strangler; and the cleanup budget after launch.
2. **The characterization and knowledge plan** — The replay or survey that will characterize the core, how you will classify each surprise as bug, promise or deletable, and how you will raise the core's truck factor to at least four, measured the same way before and after.
3. **The dependency map and forecast** — The cross-team dependencies at the start, each with the age of the oldest code it touches, and for each the kind of cut that could remove it; a Monte Carlo forecast from supplied throughput, stated as a percentile; and the aging chart you will use for what the forecast cannot see.
4. **The identity change** — The new lease identity, an inventory of every reader inside and outside your repositories, a definition of done each team signs, the notice timeline for partners and schemes, and a dated debt-register entry for the old identity you must keep accepting.
5. **The contract and invariant tests** — Each invariant (for example, one live lease per tenancy, deposits conserved to the cent, a landlord's approval before any transfer) as a named property, the contracts and simulators on the transfer path, and the rehearsal that will exercise what runs outside your code.
6. **The one-year review template** — The measures you will compare, each with its baseline instrument, a statement written now of what failure would look like, and the list of everything the change will leave behind with its removal date.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Old code first | Does the plan find out what the tenancy core does, and who depends on it, before changing it? |
| Inventory reach | Would your inventory find a reader in a deposit scheme's software or a partner's integration, or only in your own repositories? |
| Invariants as tests | Could a single pull request that breaks a tenant's or landlord's promise merge without a named test failing? |
| Honest forecast | Does the forecast say what it cannot see, and does the plan say who acts when an item ages past the line? |
| Finishing | Does every flag, old path and accepted old identity have an owner and a date, and is the cleanup funded? |
| Coherence | Do the plan, the tests, the rollout and the review describe one change, so that the review could be written from the plan alone? |

#### Where you now stand

You can now take one change through an engineering system of forty teams: write down what the code must be afterward, decide ownership with its consequences in view, cut dependencies by changing who does the work, characterize old code and read what the characterization says, cut a seam and check it against production, spread knowledge beyond one person, run the change as a campaign with a definition of done, test the invariants, rehearse what lies outside your code, finish the cleanup, and review the result a year later by the instruments you began with. That completes the Software book. The Resilience book takes up what such a system must withstand under load, and the Operations book{% include xref.html to="operations" %} what it takes to run it on the morning that matters.

### References

- US Senate Special Committee on the Year 2000 Technology Problem — [*Y2K Aftermath — Crisis Averted: Final Committee Report*](https://www.govinfo.gov/content/pkg/GOVPUB-Y1_3-PURL-LPS90964/pdf/GOVPUB-Y1_3-PURL-LPS90964.pdf). S. Prt. 106-42, US Government Printing Office, 2000 — free online.
- US General Accounting Office — [*Year 2000 Computing Crisis: An Assessment Guide*](https://www.gao.gov/products/aimd-10.1.14). GAO/AIMD-10.1.14, 1997 — free online.
- Martyn Thomas — [*What Really Happened in Y2K?*](https://www.gresham.ac.uk/watch-now/what-really-happened-y2k). Gresham College lecture, 2017 — free online.
- Michael C. Feathers — *Working Effectively with Legacy Code*. Prentice Hall, 2004.
- Hyrum Wright — [*Large-Scale Changes*, ch. 22 of Titus Winters, Tom Manshreck, Hyrum Wright, *Software Engineering at Google*](https://abseil.io/resources/swe-book/html/ch22.html). O'Reilly, 2020 — free online.
- Vicent Martí — [*Move Fast and Fix Things*](https://github.blog/engineering/move-fast/). GitHub Engineering blog, 2015 — free online.
- D. L. Parnas — *On the Criteria To Be Used in Decomposing Systems into Modules*. Communications of the ACM 15(12), 1972.
- John Quiggin — [*The Y2K Scare: Causes, Costs and Cures*](https://rsmg.group.uq.edu.au/files/1186/WPP04_1.pdf). Australian Journal of Public Administration 64(3), 2005 — working paper free online.
- US Senate Special Committee on the Year 2000 Technology Problem — [*Investigating the Impact of the Year 2000 Problem*](https://www.govinfo.gov/app/details/GPO-CPRT-106sprt10). S. Prt. 106-10, 1999 — free online.
- Martin Fowler — [*Strangler Fig*](https://martinfowler.com/bliki/StranglerFigApplication.html). martinfowler.com, 2004, revised 2024 — free online.
- Kent Beck — *Tidy First? A Personal Exercise in Empirical Software Design*. O'Reilly, 2023.
- Celal Ziftci, Stoyan Nikolov, Anna Sjövall, Bo Kim, Daniele Codecasa, Max Kim — [*Migrating Code At Scale With LLMs At Google*](https://arxiv.org/abs/2504.09691). arXiv:2504.09691, 2025 — free online.
- Charles Covey-Brandt — [*Accelerating Large-Scale Test Migration with LLMs*](https://airbnb.tech/infrastructure/accelerating-large-scale-test-migration-with-llms/). Airbnb Tech Blog, 2025 — free online.
- Murali Krishna Ramanathan, Lazaro Clapp, Rajkishore Barik, Manu Sridharan — *Piranha: Reducing Feature Flag Debt at Uber*. ICSE-SEIP, 2020.
- Guilherme Avelino, Leonardo Passos, Andre Hora, Marco Tulio Valente — [*A Novel Approach for Estimating Truck Factors*](https://arxiv.org/abs/1604.06766). 24th IEEE International Conference on Program Comprehension, 2016 — free online.
- Daniel S. Vacanti — *Actionable Agile Metrics for Predictability*. ActionableAgile Press, 2015.

---

## Appendix: Encore at a Glance {#encore-glance}

A large engineering organization is learned the way a stage manager learns a new production: one cue at a time, in the order the show needs them. This book has introduced Encore in the same way. The shared repository appeared when a chapter needed a slow build, the platform group when a chapter needed a road that was missing, and the Mobile App team's backlog when a chapter needed a dependency that would not move. For a reader who goes from front to back, that order is the right one, because each part arrives with the reason it matters. For the reader who opens the book at Chapter 8, or returns after some months to look up one practice, it is less kind, since the example may rest on a fact introduced six chapters earlier.

This appendix is for that reader. It gathers into a few tables the company, its engineering system, the teams Verified Resale touches, the facts of the change itself, the people who appear in its story and the kata companies, so that a single glance can answer "what was that again?" Each row points to the chapter where the fact does its work, and some point further: to the Architecture book{% include xref.html to="architecture" %}, where Encore's systems were designed, and to the Products book{% include xref.html to="products" %}, which follows the same months from the product side. A row compresses a chapter's reasoning into a line, and the compression is useful only because the reasoning is one pointer away.

### The company

| Term | What it is | Where to read more |
|---|---|---|
| **Encore** | A company selling concert tickets across the EU, priced in euros, which also sells its platform to venues as software as a service (SaaS). Three facts shape its engineering: traffic rises 500× within minutes when a tour goes on sale, every seat must be sold exactly once, and bots arrive before the fans | [Architecture book, 1.1](https://oleksiyp.github.io/arch-book/#encore-our-running-example); Chapter 1 |
| **Customers** | Four kinds: fans; organizers, about 900 of them active; partners, among them venues, a festival app and the resale partners, calling the API at `api.encore.com`; and more than 500 venues running Encore SaaS in three tiers | Chapters 1 and 7 |
| **Size and history** | Nine engineers in one team in its first year; about 25 in year two; 70 in nine teams in year four; 120 in year five; 250 in year six, 145 of whom had joined that year; 400 in 40 teams by year seven, and about 400 since | Chapters 1 and 9 |
| **The present of this book** | Year nine, from the Verified Resale memo in late winter, to the engineering review at month 24, a year after the launch in the winter of year ten | Chapters 1 and 11 |
| **The services on the resale path** | The Sale Gate (admission for on-sales); Seat Inventory & Ticketing, the event-sourced core that holds the seat ledger and barcode issuance; Orders & Payments, the purchase saga across two payment service providers (PSPs); Bot Screening; Notifications; Billing & Payouts; and, from month 4, the Resale service | [Architecture book, Chapters 2–5](https://oleksiyp.github.io/arch-book/#24-choosing-a-style); Chapters 1 and 11 |
| **Partner Listings** | The year-six arrangement that Verified Resale replaces. Partners posted resale offers as links on sold-out event pages, the original pass was forwarded outside Encore, and Encore checked nothing. Rowmate's integration with it parsed the old barcode's event-code prefix | Chapters 1, 2 and 11 |
| **Rotating barcode** | Since year eight, the barcode in Encore's app is generated on the phone from a per-ticket secret, so a screenshot stops working. Rotation was built around the old ticket identity without changing it. Gates hold revocation lists for offline validation | Chapters 1 and 11 |

*Figure A.1 — Encore, the company, as this book finds it.*

### The engineering system

| Part | What it is | Where to read more |
|---|---|---|
| **`encore-core`** | The shared repository, grown from the year-one monolith. It holds Seat Inventory & Ticketing with barcode issuance, the Orders & Payments saga and shared libraries, one of which has had no owner since year five | Chapters 1 and 4 |
| **Other repositories** | About one repository per service, generated from the golden-path template; a few for shared libraries; the fan app in its own repository, with a shell and 14 feature modules (Resale became the 15th); the web frontend as a monorepo. A dependency bot approximates one version of each library | Chapters 1, 2 and 4 |
| **Barcode issuance** | About 11,000 lines of Kotlin written in year one, with a truck factor of one. It derives a ticket's identity from the order and the seat, and four other places recompute it | Chapters 1 and 2 |
| **CI** | `encore-core` took 31 minutes, cut to 9 in months 5–8 by a hermetic build, a remote cache and test selection, after which a merge queue was added. Golden-path services build in about 6 minutes. Objectives: 90th percentile at or under 10 minutes on golden-path repositories and 12 on `encore-core`, and a false-red rate under 1%. Developer Portal owns CI; Runtime owns deployment | Chapter 4 |
| **Delivery** | Trunk-based development; about 180 production deploys a working day (about 20 a day in year four); a median lead time of about 26 hours; about 2,300 feature flags; canaries at 1, 5, 25 and 100%, never during an on-sale | Chapters 1 and 4; Resilience book, Chapter 4 |
| **Review** | Tier 1 changes, which touch seats or money, need two reviewers, one of them the domain owner. Targets: a first response within four working hours and the 75th percentile under one working day. Open-to-merge time for the Resale team fell from a little over two days to about seven working hours by month 8 | Chapters 4 and 10 |
| **Tests** | Tens of thousands across 40 teams. Eleven owned end-to-end journeys, flaking about one run in 40 at month 0; Verified Resale adds a twelfth. Diff-based mutation testing on the barcode core and fee arithmetic | Chapter 3 |
| **Developer survey** | Quarterly, ten core items that never change, about 68% response at month 0 (71% in the quarter after the partner-facing path). The top pain was waiting for CI on the shared repository (54%) | Chapters 1 and 6 |
| **AI assistance** | Assistant licenses at about €45 per engineer a month. Background agents rolled out to four random cohorts of ten teams a quarter apart; Inventory was in the first and Resale the second. At month 9: about 10% more merged changes, with an interval that includes zero, review time up about a fifth | Chapter 5 |
| **Onboarding** | Owned by the platform product manager since year nine. Median days to a new engineer's tenth merged change fell from 71 at months 0–2 to 27 at months 9–11 | Chapter 9 |
| **Funding** | Product funding since year four, under IFRS. Capacity allocated 56/20/14/10; large bets funded in tranches against learning milestones and kill criteria | Chapter 10 |

*Figure A.2 — The system that builds the system, at the start of Verified Resale.*

| Platform team | People | What it owns | Where to read more |
|---|---|---|---|
| **Reliability** | 10 | SLO tooling, incident process, readiness reviews, game days | Operations book, Chapter 7 |
| **Security Engineering** | 6 | Identity, secrets, signing, partner credentials | Chapter 6; Resilience book, Chapter 7 |
| **Runtime** | 6 | Clusters, cells, GitOps and deployment | Chapter 4 |
| **Developer Portal** | 4, then 6 from month 5 | The portal, templates, registry, scorecards, the exception ledger and CI | Chapters 4 and 6 |
| **Web & API Paths** | 3 | API linting, gateway templates, frontend build paths, and shared webhook delivery | Chapter 6 |
| **Event Backbone** | 3 | Streams and the schema registry | Chapters 3 and 11 |
| **Data Platform** | 4 | The data products platform | [Architecture book, Chapter 9](https://oleksiyp.github.io/arch-book/) |
| **AI Platform** | 4 | The AI gateway, the MCP server, eval tooling | Chapters 3 and 5 |
| *The product manager* | 1 | Hana, the group's first, hired in month 2 of year nine | Chapters 6 and 9 |

*Figure A.3 — The platform group: nine teams, 40 people at month 0 and 42 after Developer Portal grew. Its partner-facing path (self-service partner credentials and shared webhook delivery, 99.5% of events within 60 s) reached general availability in month 9.*

### The teams Verified Resale touches

| Team | Its part in the change | Dependencies, month 4 → month 9 | Where to read more |
|---|---|---|---|
| **Resale** | Formed at month 4 from Orders & Payments and Partner APIs. Owns the Resale service, the fan app's Resale module, the rules engine (an InnerSource project with six contributing teams) and the organizer rule assistant | — (the requester) | Chapters 8, 9 and 11 |
| **Inventory** | Owns barcode issuance, and so reissue and revocation (settled by RFC-0412 and an ADR); publishes `TicketReissued` and `TicketRevoked`. Reissue in the barcode core was the dependency that blocked | 3 → 2 | Chapters 2, 9 and 11 |
| **Venue Entry** | Door-scanning apps and devices, offline validation, revocation lists; rejected its shard of the agent-written migration | 3 → 2 | Chapters 5 and 11 |
| **Orders & Payments** | The resale purchase saga, through the primary PSP's split-payment product | 2 → 2 | Chapters 3 and 11 |
| **Billing & Payouts** | Meters the fee split on `ResaleCompleted` and pays sellers five days after the event | 3 → 3 | Chapters 8 and 11 |
| **Partner APIs** | Partner endpoints, sandbox and certification | 3 → 1 | Chapters 3, 8 and 11 |
| **Bot Screening** | Screens every resale buyer; reviews the per-buyer limits Resale wrote | 2 → 1 | Chapter 11 |
| **Organizer Console** | The resale rules console | 1 → 1 | Chapter 7 |
| **Mobile App** | The release train, the version floor and the reissue-aware ticket view; the fan app's Resale module moved to Resale | 2 → 1 | Chapter 11 |
| **Fan Messaging** | Pass replacement and the "your ticket sold" and "your new ticket" messages behind one Notifications call | 2 → 1 | Chapter 11 |
| **Design System** | The Verified badge, capped-price display and reissue status, contributed by Resale | 1 → 0 | Chapter 11 |
| **Security Engineering** | Partner credentials, made self-service on the partner-facing path | 1 → 0 | Chapters 6 and 11 |
| *Consulted, no planned work* | Trust & Safety, Fan-BFF, Web Storefront, Finance platform, Experimentation, Catalog, Public API, AI Platform | — | Chapter 1 |

*Figure A.4 — The twelve teams Verified Resale touches, and the 23 dependencies of the first quarterly plan cut to 14 by month 9: six taken over by Resale, two moved to the platform and one folded into a change already planned.*

### The change

| Term | What it is | Where to read more |
|---|---|---|
| **The product** | Fans list tickets they bought through the Sale Gate, in Encore's app and on authorized partners, Rowmate at launch and Tessera second. A screened fan buys at no more than face value plus a 10% fee, split 4 points to the partner, 3 to the organizer and 3 to Encore. Encore reissues the ticket; organizers may only tighten the rules | Chapter 1; the Products book, Chapters 2 and 5 |
| **Ticket identity** | Before: derived from order and seat, recomputed or parsed across the codebase. After: an opaque `ticket_id`, behind one lookup. Old-format tickets stay valid until their events pass | Chapters 2 and 11 |
| **Reissue** | Void and reissue in one atomic step, with one idempotency key per resale; a retried request is a no-op, and a ticket may be resold more than once. Returns `Reissued` or `Conflict`. Most reissues finish in under 30 s, 99% within 4 minutes | Chapters 2 and 11; the Products book, Chapter 9 |
| **Five fairness invariants** | 1. Partners never buy primary tickets. 2. Only tickets bought through the Gate, within the per-fan limit, can be listed. 3. Organizer caps and rules can only tighten. 4. Every resale buyer passes Bot Screening and the per-buyer limits. 5. Partners never see sales-velocity data. Each runs as a property test, named word for word, on every build | Chapters 1, 3 and 11 |
| **The format campaign** | 60 call sites in 11 repositories owned by seven teams read the old event-code prefix. An agent wrote one change per call site; 56 had landed by month 8, when the legacy parser was deprecated with four callers on an allowlist; the last moved by month 15 | Chapters 5 and 11 |
| **Characterization** | 1,400 cases replayed from a year of issuance requests, in CI by month 6. They surfaced 31 unspecified behaviors: 19 kept as specifications, 9 deleted with the old format, 3 bugs | Chapters 2 and 11 |
| **Debt items** | INV-DEBT-017, the 19 public issue variants, repaid in month 13. INV-DEBT-031, old-format tickets still accepted at gates, recorded in month 6 with a trigger at month 29 | Chapters 2 and 11 |
| **Flags** | 17 release flags, each with an owner and a removal date, among them `resale-verified-flow`, `ticket-identity-opaque` and `resale-listings-intake`. 15 removed by month 16; two kept as per-market kill switches | Chapters 4 and 11 |
| **Reissue-ready** | A seven-line definition of done that each of the 12 teams signed; the seventh line, listing copies of a team's logic running outside its repositories, was added after the month-11 drill | Chapter 11 |
| **The organizer rule assistant** | The change's one AI feature. It drafts a typed rule set that cannot express a loosening, and the organizer confirms before anything applies. Its evals grew from 60 cases to about 250 by launch | Chapter 3; the Products book, Chapter 6 |

*Figure A.5 — The change, in the terms the code uses.*

| Month | Season | What happened in the code and the engineering system | Where to read more |
|---|---|---|---|
| 0 | Late winter, year 9 | The bet memo. Developer survey baseline; median days to a tenth merged change 71 | Chapters 1 and 9 |
| 2 | — | Partners told the barcode format will change. Hana hired as the platform group's first product manager | Chapters 6 and 11 |
| 3 | — | The first cohort of ten teams gets background agents | Chapter 5 |
| 4 | Late spring, year 9 | Resale team formed; 23 dependencies across 12 teams; first Monte Carlo forecast puts the 85th percentile at month 14; Resale service created from the template, first production deploy 23 working days later | Chapters 6, 9, 10 and 11 |
| 5 | — | RFC-0412 closes in an ADR: Inventory owns reissue. Pairing with Lena begins. Work on the `encore-core` build begins | Chapters 4, 9 and 11 |
| 6 | — | Characterization suite in CI; INV-DEBT-031 recorded; forecast back inside the appetite | Chapters 2, 10 and 11 |
| 7 | — | Ensemble week on the barcode core; Inventory publishes `reissue` with a contract test, and Resale consumes it as a service; shared webhook delivery in beta | Chapters 6 and 11 |
| 8 | — | Three-week parallel run of the new identity; 56 of 60 call sites moved, legacy parser deprecated; `encore-core` CI at 9 minutes | Chapters 4 and 11 |
| 9 | Autumn, year 9 | Walking skeleton running end to end; partner API sandbox open to Rowmate on 29 September; webhook delivery generally available; dependencies down to 14 | Chapters 6, 10 and 11 |
| 9–11 | — | The three home-grown webhook senders retired | Chapter 6 |
| 11 | — | Reissue drill finds turnstile firmware that derived identity from order and seat; Rowmate certified; the festival feed reaches its first deploy in four working days | Chapters 6 and 11 |
| 12 | Winter, year 10 | Launch in France. The first resold ticket, €80 face value, bought on Rowmate for €88, scans in Lyon on a Saturday evening. Truck factor of the core: four | Chapter 11; the Products book, Chapter 10 |
| 13 | — | The 19 issue variants collapsed into one `issue()` | Chapter 11 |
| 14 | — | The partner API stops accepting the old format | Chapter 11 |
| 15 | — | Main reissue flag removed; last legacy-parser caller moved and the parser deleted; Tessera certified | Chapters 8 and 11 |
| 18 | Summer, year 10 | The bet's review. Resale has grown to 15 people and splits afterwards | Chapters 9 and 11; the Products book, Chapter 10 |
| 24 | — | The engineering review | Chapter 11 |
| 29 | — | INV-DEBT-031's trigger: old-format tickets no longer accepted at gates | Chapter 11 |

*Figure A.6 — The change's two years. The Products book reviews the bet at month 18; this book reviews the engineering at month 24.*

| Measure | Month 4 | Month 12 (launch) | Month 24 |
|---|---|---|---|
| Barcode core, lines of Kotlin | about 11,000 | about 12,300 | about 7,600 |
| Median days from first commit to production for a core change | 11 | 6 | 2 |
| Truck factor of the core | 1 | 4 | 4 |
| Callers parsing the barcode | 60 | 2 | 0 |
| Days to a partner-facing service's first production deploy | 23 (Resale) | 4 (festival feed) | median 5 (three more services) |

*Figure A.7 — What changed, measured by the same instruments before and after.*

### People named in this book

| Who | Role | Where to read more |
|---|---|---|
| **Lena** | One of Encore's first nine engineers, now a senior engineer on the Inventory team; the last remaining author of barcode issuance and, at month 0, the only person who understood it | Chapters 1, 2 and 11; the Products book, Chapter 3 |
| **Ines** | Staff engineer on the Inventory team; sponsored the agent-written migration of the 60 call sites and wrote its specs | Chapters 5 and 11 |
| **Jonas** | Inventory engineer who paired with Lena from month 5 and wrote the guide to the barcode core | Chapters 4 and 11 |
| **Hana** | The platform group's first product manager; owns the webhook-sender campaign and onboarding | Chapters 6 and 9 |
| **Amira** | Product manager of the Resale trio, from Partner APIs | Chapter 9; the Products book, Chapters 1 and 3 |
| **Paolo** | Designer of the Resale trio, from Organizer Console | Chapter 9; the Products book, Chapters 1 and 3 |
| **Katrin** | Tech lead of the Resale trio, from Orders & Payments, and one of the Resale team's first seven engineers | Chapter 9; the Products book, Chapters 1 and 3 |
| **Theo** | A graduate who joined the Resale team at month 4, its first hire from outside after the founding seven, and learned the seat ledger with an assistant | Chapters 5 and 9 |
| *The second pair* | The other Inventory engineer paired with Lena, the fourth person to pass the truck-factor test | Chapter 11 |
| *The lent staff engineer* | A staff engineer from Orders & Payments, lent to the Resale team for nine months | Chapters 9 and 11 |
| *The engineering director* | The director for the partner area, who wrote the reteaming FAQ | Chapter 9 |
| *The partner-surface architect* | Chair of the API council | Chapter 9 |
| *The organizer-success lead* | Labels the rule assistant's evals | Chapter 3 |

*Figure A.8 — The people of the change. Names in italics are roles; the book does not name them.*

### The kata companies

| Chapter | Kata | Company | The brief in a line |
|---|---|---|---|
| 1 | The Tariff Deadline | Northgrid | Energy-retail SaaS whose year-one billing core must carry a new hourly tariff in 14 months |
| 2 | The Rostering Rules | Ledgermoor | Airline crew-scheduling SaaS with a rostering-rules engine its authors have left and a request to rewrite it |
| 3 | One Run in Twelve | Repwell | Gym and fitness-class booking SaaS with a 70-minute suite that fails one run in twelve |
| 4 | The Two-Quarter Lead Time | Inkstone | A design-tool company asked to halve its lead time to `main` in two quarters |
| 5 | The Promise to the Board | Fieldnote | Farm-management SaaS whose chief executive promised the board double output from agents |
| 6 | The Portal Nobody Visits | Copperline | Car and van rental with a developer portal behind 9% of its services |
| 7 | The Inspector's Copy | Countwise | Pharmacy stock-control SaaS onboarding a buying group of 140 pharmacies |
| 8 | Gear Between Rivals | Kitebridge | Rental-house SaaS building a sub-rental marketplace between rivals |
| 9 | The Second Shift | Pennant | Freight-logistics SaaS funded to grow from 60 engineers to 250 |
| 10 | The Dashboard Deadline | Halyard | Pensions SaaS facing a regulator's dashboard deadline across seven teams |
| 11 | The Lease That Changes Hands | Lintelby | Lettings SaaS whose lease identifier must change to allow lease transfer |

*Figure A.9 — Eleven practice briefs, each a different company with its own scale and trouble. All are fictional.*
