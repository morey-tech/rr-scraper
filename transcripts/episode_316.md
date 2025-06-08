## Episode 316

Ben Felix: This is the Rational Reminder Podcast, a weekly reality check on sensible investing and financial decision-making from two Canadians. We're hosted by me, Benjamin Felix, and Cameron Passmore, Portfolio Managers at PWL Capital. 

Mark McGrath: Welcome to episode 316. Cameron is obviously not here today, so, Ben, good job on the modified intro there. Two Canadians, not three. 

Ben Felix: This is a big thing. Can we just, real quick, for a second, pause here? This is your first episode with a guest and the first time you and I are together doing an episode. 

Mark McGrath: And without Cameron as well. I mentioned that to my wife who's away right now. But I texted her this morning like, "You're not going to believe this. I'm replacing Cameron today." I still pinch myself over it. It's wild to me after being such a fan and a listener for all these years that now you and I got to interview Andrew Chen today. 

Ben Felix: What an episode for you to start on.

Mark McGrath: Oh, boy. What a conversation that was. He's obviously brilliant, tons of incredible insight. He's done some amazing research, and I think my mind was blown multiple times through this conversation. 

Ben Felix: Andrew's research, he looks at meta-research. Looking at meta-studies, large-scale replications, large-scale statistical inference, meta-science being the broad term of all of that. He's doing this on cross-sectional asset pricing literature. Factor investing is based on that, and so he's looked at this from a whole bunch of different angles. He's looked at replication. He's looked at out-of-sample performance. He's looked at whether factor premiums survive transaction costs. I'm not going to give away the answer on whether they do or not. You'll have to listen, but all just absolutely fascinating. 

Honestly, a lot of stuff that I thought to be true or just held as a belief kind of turns it on its head. I think he kind of says that for a very long time, cross-sectional asset pricing research was kind of not going in a great direction. It's improved more recently. We talked about that, I think, near the end of the conversation. Some pretty serious stuff. Any other thoughts before I talk a little bit more about who Andrew is? 

Mark McGrath: Like you said, incredible conversation and really very insightful and, to your point, has me thinking about the topic more and more. What I do with the information I learned in this episode remains to be seen. But as you said, I won't spoil it for the listeners. They'll have to listen to the rest of it.

Ben Felix: Andrew has been an economist at the Federal Reserve Board since 2014. He's got a PhD in finance from Ohio State University and an MBA from Georgetown. He was previously a research fellow at the National Institutes of Health, which is interesting. His primary research interest, as I mentioned in financial economics specifically, is in understanding whether finance research is going in the right direction using tools from meta-science. Most of his papers are around that. 

His research has been published in Management Science, the Journal of Financial Economics, Critical Finance Review, the Journal of Finance, the Journal of Financial and Quantitative Analysis, The Review of Asset Pricing Studies, and The Review of Financial Studies. For anyone unfamiliar, those are the top journals in financial economics. 

His focus on cross-sectional asset pricing, which, again, is what the concept of factor investing is based on, makes him really, really-well suited for our podcast. I thought this was an incredible conversation that will affect the beliefs of everyone listening. 

Mark McGrath: Okay. It's a great introduction. Let's go to the episode. Let's do it.

***

Mark McGrath: Andrew Chen, welcome to the Rational Reminder Podcast.

Andrew Chen: It's great to be here. I just need to put the disclaimer upfront that my views are not necessarily those of the Federal Reserve Board or the Federal Reserve System. 

Mark McGrath: Understood. Andrew, what is an asset pricing factor, and how is it different from a predictor? 

Andrew Chen: Predictor is how it sounds. It's something that predicts asset returns. A very popular one is when you take book equity of a firm and divide by the market value. You get this variable that predicts returns. Now, there's different ways to measure that predictability. One of them is to construct a factor, which is basically a trading strategy on book to market. But there's also lots of other things people mean when they say factor. I prefer the word predictor and try to use it as much as possible. But the language has just gotten all squished. People say predictor, factor, and anomaly, and just squish it all together. Try to say predictor. But it's okay if we deviate a bit.

Ben Felix: Okay, makes sense. What are the plausible explanations for why cross-sectional predictors exist? 

Andrew Chen: There's basically three explanations. The first is that it's due to risk. The stock or the strategies giving you high returns because it's exposing you to something that you should fear, and it's rewarding you for that exposure. Another one is, of course, mispricing. Just that the price isn't right. It's going to move up in the future, or it's going to move down in the future. The third one is that the statistics got wrong somehow. There's always some uncertainty in the stock market. You can't know for sure what the return is going to be, and there could be something wrong with the statistics. 

Mark McGrath: We've heard about the predictor zoo or the factor zoo with over 400 predictors. How many predictors are there really?

Andrew Chen: If you're talking about predictors that are clearly documented in the academic literature, I would say there's roughly 200. I say roughly because it's not always very clear if one predictor is different than another predictor. Also, it's impossible to say if you really have the whole literature captured. People have this idea of 450 anomalies out there from a paper, which I think has some issues. They're pretty creative with their language as you can see. I try to be strict about my language. I also can make mistakes, too. But in this very famous paper, they take 150 predictors, and they create 450 anomalies from them by tweaking them in certain ways.

Ben Felix: Why was it important for you to create an open-source data set of cross-sectional asset pricing predictors? 

Andrew Chen: Academic finance and, I guess, science more generally always has this trade-off between open collaboration, like standing on the shoulders of giants, and closed competition. If you don't have any competition, you might not really get those cutting-edge insights. 

When we started on this project, academic finance was very much closed competition. It's kind of like the business school culture to compete. But then we got to the state where we're publishing these papers with these machine learning algorithms that are really complicated, fitted to dozens and dozens of predictors. It seemed like it was impossible to openly collaborate at that point. I thought it was very important. You can see in the AI space how that's become so critical to progress. 

Another aspect of this was that, at the time, there were some papers that were, I think, not very high-quality that were misleading people into thinking that there's some kind of replication crisis. We wanted to put out a paper to really counter this narrative.

Ben Felix: Can you maybe just talk a little bit more about the Open Source Asset Pricing project? 

Andrew Chen: What we did there is we took 150 papers on cross-sectional asset pricing, and we found any kind of result about predictability in the paper. Just to be clear, it's about predictability. What is the factor? I don't know. Everyone disagrees. But you can see it's predictors. There's a regression. It shows predictability. We try to replicate every single one of those predictors. 

Then not only that, we posted all the code online and the data online, and we update this every year. We try to make it high-quality code, too. Once you have a project this big, you realize, "Oh, man. You need to write things nicely." We're still primarily economists and finance researchers, so we don't have the best code. But I think it was a good step up from what people often provide. Especially, if you go to some Stanford professor's website, you might not like what you see. I hope ours is a bit better. 

Mark McGrath: How did you choose which predictors to study? 

Andrew Chen: As I alluded to before, there are some papers out there pushing this replication crisis narrative. One is by Hou, Xue, and Zhang. It's published in the Review of Financial Studies. It has a ton of citations. That's the paper where they have 450 anomalies. There's really only 150 predictors underlying there. Their main result was that they failed to replicate the anomalies, and so we want to clarify that. That's not really what you see if you look closely. We replicate everything that's in that paper. 

Then there are other papers simultaneously on this topic. A very important one is by McLean and Pontiff. I don't know how much you guys are into these names, but this is a very important paper that documents how predictability decays out of sample. If you read some numbers in the paper, it tells you that, "Well, you got to divide by two in the future if you're looking forward." We want to replicate everything in there, too, and we got that pretty much done. 

Then there is another meta-study that they didn't actually replicate anything. This was more challenging. They had a lot of stuff that was very, very difficult to deal with. We still tried to replicate everything that's in there. Ultimately, we got this list of 300 variables that may or may not predict returns, but they were discussed in these previous meta-studies. We wanted to be comprehensive. Cover all that.

Ben Felix: How many of those were you actually able to reproduce? 

Andrew Chen: Let me back up a bit and say that of those 300 variables, only 200 actually were shown to predict returns in the original papers. That was a major comment that we wanted to make that some of these influential papers, they never really look to see whether there's anything to replicate in the first place. That's something to document. That's something, I think, we document clearly as part of the open-source project. We have these spreadsheets where we actually write down the page that you should look at for predictability. If there's no predictability, we just say there's nothing in there. 

Of those 300, about 200 variables actually were shown to predict returns. Replication is a bit subjective. It's not clear if you get the number seven and the original number was eight. Is that good or not? But our judgment was that we replicated everything but three. There were three failures that were pretty unsatisfactory.

Ben Felix: Three out of 200.

Andrew Chen: Yes.

Ben Felix: Wow. Okay.

Andrew Chen: Roughly one to two percent failure rate. 

Ben Felix: That's wild. You mentioned the other paper that showed maybe replication was not so great. Why were your results different from that? 

Andrew Chen: If I'm frank about it, it's because they're very loose with their language. It is pretty surprising because this is a really influential paper. It's still highly cited all the time in this top journal. But, really, they never defined what an anomaly is. They defined what a failed replication is. But it's not a good definition because they don't define an anomaly. It's helpful to describe an example. 

One of the papers in our dataset, both of us shared this paper. It's by Dichev in the late 1990s, and he talks about bankruptcy risk. To try to be more precise, the probability of bankruptcy. You have these variables from the accounting literature that predict bankruptcy, and he wants to know do you get a reward for bearing this bankruptcy risk. Stocks that have high bankruptcy probability, do they have high returns in the future? He finds that the answer is no. They actually tend to have low returns. 

The relationship is the opposite of what you would expect in an efficient market. You're not going to be compensated for that. But he doesn't find that this relationship is statistically significant. It depends on the tests. Some of the tests show significance. Some of them don't. But the relationship goes the wrong way. That's a very interesting result. You definitely want to know about this. When you replicate it, you need to be careful. If you find an insignificant result, that's actually a successful replication. He finds that there's no relationship. There should be a relationship between – higher bankruptcy probability should be higher return. He finds actually a negative relationship. It's not statistically significant. But if you get that direction right, that's a successful replication. 

In the Hou, Xue, and Zhang paper, they don't care about that. They call it a failed replication. To make it more interesting, they made, I think, three or four versions of this bankruptcy variable. Then they get four failed replications, although they should all be called four successful replications if you did this carefully. 

Ben Felix: Very interesting.

Mark McGrath: How do anomaly returns change post-publication in your data? 

Andrew Chen: I want to be a bit more precise about that. Instead of post-publication returns, let's talk about out-of-sample returns. It takes a long time to publish a paper. Usually, if you find a paper published in '93, the sample ends in like ‘89. If the sample ends in '89 in the paper, from 1990 to present, the returns decline by about 50%. 50% as in if you had 10% per year in sample before 1989, from 1990 to present, you'll have a return of about 5%. But there's a big nuance there, which is that, in the first few years out of sample, from like 1990 to 1993, the decay will only be about 25%. 

Ben Felix: You replicate a lot of these things. You find the premiums decline but don't go away. What would you say are the implications of this research for the so-called replication crisis that people have talked about in cross-sectional asset pricing? 

Andrew Chen: The replication crisis is interpreted in a big way. You could mean a replication crisis in that you just can't write the code to reproduce the numbers in the original papers. That's clearly out. That's just false. I think it's become well-accepted about that for at least the equities literature. 

But then you could also think about a replication crisis more broadly. I'm not a fan of how this is being used. But people also interpret this as external validity is wrapped up in a replication crisis. It makes sense. But when you're talking about stock markets, you have to be a bit more careful. If a predictor is based off mispricing and the markets are reasonably efficient, which we hope that they are, you would expect that predictability to decay out of sample. 

What you're really afraid of, I think, is something called like a false discovery or like a statistical figment, where the numbers in the papers, they look good, but because of these statistical problems like P-hacking, multiple testing problems, perhaps these are just statistical figments. If that was the case, then you would expect the returns to vanish immediately out of sample. It shouldn't take five years. Right after 1990, you should see the returns go to zero. But that's not what we see. We see them gradually, in a sense, decay to 50%. That tells you that that's also a relatively minor problem. 

I should say I need to credit McLean and Pontiff for that result. Academics care a lot about that, and they're the ones who really discovered that. We replicate it, which I think is pretty cool. They're a meta-study that replicates many papers, and we're a replication of their replications. You could still see this result. It's perhaps one of the most solid results in empirical asset pricing.

Mark McGrath: Can you just elaborate a little bit on that term, false discovery? 

Andrew Chen: It's a term from the statistics literature. In statistics of discovery, it's something that's statistically significant using some tests. But then even though something statistically significant, it could still represent no effect at all. They call that null in statistics. But traditionally, in asset pricing, that would mean the true alpha or the true expected return is just zero. A false discovery is when you have a statistically significant result. The statistics look good, but the actual underlying effect is zero. There's actually no alpha there, just the false positives. 

Ben Felix: How large is the false discovery rate in cross-sectional asset pricing research? 

Andrew Chen: You could reliably say this is just a statistical concept, so there's caveats. But what the numbers say is that the false discovery rate is less than 10%. It's actually quite small.

Mark McGrath: Why does the false discovery rate that you find differ from other studies? 

Andrew Chen: This is another case where it might get a bit controversial because we're finding stuff at odds with other people's results. Also, the way that things are at odds is also a bit striking. The previous paper on this, which is still probably the most well-known paper by Harvey, Liu, and Zhu, also in the Review of Financial Studies, extremely influential paper. Basically, they conflate insignificant with false. There's a difference between insignificant and false. Just because you have a negative COVID test, you could still actually have COVID. You could have a false negative. 

There's a distinction between what the statistics show you and the underlying truth. The fundamental part of statistics is that there's uncertainty. If there's no uncertainty, there's no need to do statistics. That just be like, I'm not sure, history or something. If you equate false and insignificant, then you're ignoring this uncertainty. 

Ben Felix: That's something that they just didn't think about, and then you did and put it into your research? 

Andrew Chen: I can't get into the heads of what Harvey, Liu, and Zhu were thinking. I think the rhetoric actually just got too strong. Another thing in the paper, which is probably more striking than equating false and insignificant, is they equate many with most. You actually have to dig very deep into the paper to understand any of this. 

It took a long time for even me to understand as someone who specializes in this. All these papers we've been talking about, they're dozens of pages long. It's not until you get to page 26 or something like that of the Harvey, Liu, and Zhu paper that you really see how do they get this claim. In the abstract, they loudly proclaim most claim research findings in financial economics are likely false. 

But you have to get to page 26 of the paper. Get through all these statistics to really understand what's going on there. If you get there, you'll see that they mix up both false and insignificant, and also mix up many with most. It's pretty incredible. I think it's because of the incentives, and I'm vulnerable to this. Perhaps I've also overstated things before. But there's a big incentive to make big claims in academia.

Ben Felix: Can you talk about how the false discovery rate relates to publication bias and out-of-sample returns? 

Andrew Chen: Let's start with publication bias. We haven't talked about that yet. Publication bias is no one wants to read something that's not interesting. Though, people who write for a living want to write things that are uninteresting. We all get together. Look for only the interesting stuff. Sometimes, we push it too far. Or another way to think about it is it's an inevitable fact that if we're only looking for interesting stuff, some of that stuff will be not interesting. If we're kind of biasing our reading or our writing towards stuff that's interesting, some of it will actually not be there. That's publication bias. 

Then how that relates to false discovery rates is you can think of publication as people searching through thousands of ideas and just reporting what is really noteworthy in the journals. That could be thought of as a multiple-hypothesis testing problem. Traditionally, if you go to your – I'm not sure where people learn statistics nowadays but, hopefully, high school. You'll say, "Oh, yeah. You have a hypothesis. You construct this test. If the test statistic exceeds some value, it's significant.” 

That procedure assumes that you have a single test. But what happens if you have many, many tests? If you only talk about the very extreme test, the extreme test in the tail, then that's when you need to use these false discovery rate methods. It's interesting that they're relatively recent in statistics. They didn't really get developed until the late nineties.

Mark McGrath: Interesting. Switching gears a little bit, how much of an effect do transaction costs have on factor expected returns? 

Andrew Chen: That's a very important thing to bring up because I'm kind of emphasizing false discovery rates, and this publication bias I've been talking about are really statistical concepts, at least the way I've been using them. The statistics are only as good as the ingredients you put in. Or they only reflect the economics that you put into it. 

The economics that we've been talking about, perhaps surprisingly, they don't account for transaction costs at all. I don't want to go too much of a tangent about this. But perhaps there's a good reason for that. No one agrees on how to measure transaction costs. If someone puts in some number, someone's going to want to take it out and put in their own number. In a way, it makes sense for the academics to just focus on gross returns.

Well, if you try to measure transaction costs in a very basic way, I have a paper with Mihail Velikov where we find that they eat up about 25%, 30% of the trading strategies returns in the original samples. 

Ben Felix: That's a lot, right? When you think also about the out-of-sample performance declining, is that eating all the out-of-sample performance? 

Andrew Chen: If you know the literature, you know that people, they have these equal-weighted trading strategies that you weigh every stock equally no matter how illiquid it is. My intuition was 25%, 30%. That's about right of what would have in-sample. But I think then you're alluding to this fact that we find in this paper that out-of-sample, the returns are basically completely gone after trading cost. 

I mentioned that people find that out-of-sample, the returns decline by 50%. But that ignores transaction costs. Then if you account for transaction costs in the recent period from 2005 to the present, even the best of these anomalies or predictors earns nothing in this very baseline transaction cost case.

Ben Felix: On the transaction costs, though, are those worst-case transaction costs or using cost mitigation techniques that a real asset manager might use? 

Andrew Chen: They're not worst-case. We are using some transaction cost mitigation techniques. We look to see if we can modify the strategy to eliminate these tiny stocks. Or we can try to tilt towards the large stocks. We also try to rebalance less frequently. We also try to rebalance only when the signal really tells us to rebalance. After you do all of that and you get that 25% decline in sample and then out of sample, the returns are gone. 

There are definitely caveats on this. Like I mentioned, people argue about how to measure transaction costs. Our cost is the effective bid-ask spread, which you can think of as assuming aggressive market orders for a small trader who doesn't have price impact and ignoring short sale costs. There's recent paper that says that just a short sale cost will eliminate these anomalies altogether. 

At the same time, it could get messier than this. The real way to think about these predictors is in combination. In fact, there's an economics of this that transaction costs are actually, in a sense, lower if you use more predictors at the same time. If one predictor is telling you you need to make a trade, if you only have one predictor, then you kind of have to eat the cost. But if you have two predictors, the other predictor may tell you that you can offset it, and you don't have to make the trade. I've been talking about these predictors in isolation. There are some recent studies that find that even net of transaction costs, if you can combine predictors, you can still get some returns. 

Mark McGrath: Wow. That's really interesting. I hadn't thought about that, that the combination of predictors can actually reduce trading costs. What are the problems with estimating factor expected returns using historical data? 

Andrew Chen: Of course, everyone knows that past performance doesn't necessarily reflect future performance, but one thing that is coming out of the anomalies literature is that the markets get more efficient over time. If you're looking at stuff that's performance in the past, it's likely to be not just that. It's not necessarily reflective of the future but probably overstates performance because of these market efficiency changes, technological changes. 

As an example, a lot of this data, I’ll keep on using this 1990 sample [inaudible 00:22:37], Fama-French 1993 or 1992, they were these very influential papers at that time. They're using data from 1963 to 1990 or 1989. You think how would you trade on book-to-market in that time? For a lot of people, you have to get these accounting statements in the mail and write everything down and make a ton of phone calls. It's a completely different world now. Now, it can take a microsecond to do that once you get the data. That's the big problem. Think about the era that your data reflects. How do you need to take a haircut off of that because of the new era of technology? 

Ben Felix: How did factor performance change after 2005? 

Andrew Chen: Let me just state the empirical fact first before I speculate or try to give my view on what it is. The fact is that from a lot of studies, you see these anomaly returns or predictor returns or factor returns, they all decay. There's like a kink around the mid-2000s. It's pretty cool that you see this across many studies. The hypothesis that I prefer is that that was when the internet took off, when IT took off. Thinking back when I was an MBA student, even then, it was still kind of growing. It could be somewhat difficult to get an annual report and digest it. You'd have to go through a little bit of hurdles. Now, AI will read these things. 

There's a competing hypothesis, though, which is that this was also the time when a lot of these anomaly papers were published. If you look at the publication dates in the open-source dataset that we have, that's one of the things we provide is all this documentation, every predictor, what table the – look for predictability sample dates. Then you can plot the distribution of publication years. There's a big peak in the mid-2000s. That's this competing hypothesis.

Ben Felix: The empirical fact is that after 2005, there's kind of a kink where factor performance decreases. It could be because markets got more efficient. Is that the argument? With easier access to information? Or, I guess, the publication thing could also be related to market efficiency. But in either case, yeah, interesting. 

Andrew Chen: Yes. I think, ultimately, it's market efficiency. Maybe this is just academic. But was it technology improvements in IT that made markets more efficient? Or was it the professors writing their papers that made things more efficient? Maybe because I'm not really a professor, I think the IT is more powerful. But I think people disagree.

Ben Felix: We talked about transaction costs. We talked about the stale data idea. If you take those two things together, how much of a combined effect does that have on factor expected returns? 

Andrew Chen: The two effects you're talking about are transaction costs and post-2005 decay. After that, it's pretty much gone. The returns are pretty much gone for individual anomalies using our baseline effective bid-ask spread costs. 

Ben Felix: All of them? 

Andrew Chen: Even the best ones. There's an important thing to do here, which is if you look 2005 to now, of course, there's going to be some things that got lucky. There's noise in markets. You have to adjust for that luck. You just take the best stuff that worked in the past. Some part of that's due to luck. Then we have these multiple testing methods, these statistical methods that adjust for this luck. Once you adjust to the luck, then you shrink the returns. You could call it shrinkage. Basically, the returns are very close to zero. They're not exactly zero. I say effectively zero because we're ignoring short sale costs. We ignore price impact. I want to be qualitative with this because, like I keep saying, everyone disagrees on how to measure transaction costs. 

Of course, you get some things that are lucky, but then it's cool. If you plot the distribution of returns there and you compare that to a simulation where there's actually no real predictability, they looked exactly the same or not exactly. They looked very similar. The simulation of nothing there, luck will get you what we see in this paper with Mihail Velikov. 

Mark McGrath: In your research, which factor or factor combinations had the strongest investable expected returns? 

Andrew Chen: Once you account for trading costs and you account for just the modern era of technology, nothing really does much. There's some stuff in the details. But you want to shrink that towards zero. It's actually funny. The paper was published a few years ago, and one of the things that sticks out in detail is it doesn't work anymore just a few years after that. There's luck. 

If you talk about factor combinations, our paper doesn't really study this in detail. We have a bit about that in the paper. There are other papers on this. If you take a look at them, they actually disagree what is the most important stuff. There's a [inaudible 00:26:46] paper that I think finds that quality predictors are the most important. But then if you look at the new paper, I'm thinking about – this is the older paper. If you look at this paper by Victor DeMiguel and others, they find that investment is the most important. I think it really depends. 

In my view, it's not really the best way to think about this. The big picture from this literature is that none of these predictors are actually super special. They all kind of decay out-of-sample. They're all just kind of these mispricings that get corrected. What you really want to think about is the method. The meta method for collecting these predictors, and for combining them, and for eliminating them once they get stale. 

Ben Felix: You just kind of told us that factor premiums are zero after costs. What are the implications of this research for investors pursuing higher expected returns through factor tilts? 

Andrew Chen: It's not going to be very fruitful. You're going to have to work harder. You can't just read this old paper and implement it. I mean, you could try to avoid the transaction cost we measured. You have to be really good at placing your orders. Really optimize. There could be a reason why these predictors like we talked about at the very beginning. If it's not mispricing and it's due to some kind of fundamental thing that's not going to be corrected, you don't mind bearing that risk. Then that would work out. But it doesn't seem like that's the case. It seems like there's nothing really special in this zoo. 

I couldn't say this is the consensus from the literature. But this is what I find in my research and when I read papers. People want to make things special. But in the end, these are all mispricings that are transient. If you're a practitioner, you’ve got to get to something new.

Ben Felix: Your finding is kind of what you'd expect, I think, in an efficient market if they're mispricing. Is that the premiums would decrease up to the point of the transaction costs? 

Andrew Chen: The complication is that this is kind of like the Adaptive Markets Hypothesis if you've heard of this concept from Andrew Lo. It's an influential concept. But I think it doesn't get enough credit. The classical idea of efficiency is the market is efficient all the time. In my view, that's how these predictors became factors. 

In 1980, Dennis Stattman finds that book-to-market predicts returns. The efficient market view is like, "That shouldn't exist." 13 years later, Fama and French repackaged that. They're like, "Oh, if we have this book-to-market factor, we could explain the book-to-market predictor," which sounds circular at least. But in the end, yeah, the book-to-market factor doesn't seem to be super special. I've been talking about the anomalies as a whole and how they decay. Book-to-market, it's in the middle of the pack. 

Ben Felix: What about peer-reviewed factors with strong theoretical underpinnings? How do those perform relative to a naively data-mined factor or predictor? 

Andrew Chen: This touches on this recent paper by myself and Alejandro Lopez-Lira and Tom Zimmermann. The short answer is that even the stuff with the strongest theoretical underpinning, stuff with these fancy equilibrium models, they don't do any different or any better. They might do something different. They perhaps do worse than the stuff without a strong justification. That's kind of a disturbing result. We find no difference. We look through all the papers, and we categorize their theoretical underpinnings. Are they a mispricing idea or risk idea? We also look at their modelling. Do they just wave their hands and say, "Oh, this should predict returns?" Or do they write down like a toy model? Or do they have these quantitative equilibrium models that are calibrated to capture key moments of the US economy? 

These are like this holy grail that people in my world want to create. My dissertation was actually one of these really fancy models of the value premium. It doesn't matter. If anything, this is risk-based. The more stronger the theoretical underpinning, they seem like the worst out-of-sample performance. 

Ben Felix: That's wild, strong theoretical underpinning. What about the risk-based specifically explanation? How do those do?

Andrew Chen: You would think that the risk-based explanations are the strongest underpinning. At least in one sense, they actually tend to underperform mispricing-based predictors. We're talking about risk-based off of the words in the paper. That's kind of an innovation there. Usually, people use factor models to measure risk, but we we're just like, “Let's see what the peer review process says.” All these sentences, they're not just a view of the author. These sentences in the papers, they have to get through referees and editors. It's such a thing to get through that process. If I could describe to you the sweat and toil and the brain power that goes into these things, I thought that there would be something there. 

One thing we do in this paper is we also compare these peer-reviewed trading strategies to what would happen if you just mine accounting ratios instead. I keep going back to this example of 1963 to 1989 data. You find book-to-market predicts returns using that sample. What happens if instead you use that same sample? You're kind of living in 1989. You just take one accounting variable and divide by another one, then keep repeating that until you search through thousands of accounting variables, and you construct this trading strategy that has a [inaudible 00:31:34] bigger than two. Is that statistically significant? 

You would get almost the same returns as from trading off stuff that's published in the literature. One of the responses we get to that is this hypothesis that the publication process really matters. So when people publish these ideas, then the currents get traded away. That's not really fair to compare data mining, which not necessarily people know about to publish stuff that people do know about. As I mentioned before, the publication dates are all around 2000, so it's all mixed up with this technology story. 

Mark McGrath: I think you wrote a tweet about that, the data mining, the accounting ratios last year, a while back. I follow you on Twitter, and I remember reading that being quite concerned, of course. It's very fascinating. 

Andrew Chen: It's weird. It's something that makes me slightly emotional. So much work goes into these things. I think partly what's happening here, it’s not an idea I could publish. It's not scientifically proven. But people love these theories so much, and that biases them towards wanting to make these theories. Some of these equilibrium models, these fancy models, they're beautiful to me. They're like works of art, and so you want them to be true. That's why I think the literature gets kind of biased towards publishing these things. You'd think that they have some incremental impact after how hard it is to run these things. 

I used to wake up in the middle of the night to make sure that my software for calculating the equilibrium is converging to solve these heterogeneous [inaudible 00:32:56] models with the time-bearing risk premiums to model the value premium. It could take days for the computer to solve it if you don't have a fancy computer. In the end, I think it has not been the right track. 

Ben Felix: You talked about some of these biases in the publication process. What do you think this tells us about the academic peer review process in general?

Andrew Chen: I want to be very cautious. I don't want to extrapolate. Now that we have LLMs, everyone gets a sense of what happens if you extrapolate. If you ask a LLM something that's really in its data set, it'll get it right. If you need a gin and tonic recipe, it's going to be in there. But if you get to make up some kind of weird cocktail, you have no idea what it'll hallucinate because that's outside of its trading data. 

We could say about the cross-sectional asset pricing literature as it was done in the 1980s to 2015 or so is then you could trust the numbers. That's what the replication open-source paper shows. If you read a number, you could trust that that's probably the right number. Whether the text actually adds any information, the text and the supporting evidence, it's unclear. In my view, I don't think it really adds anything. As I mentioned, there's this competing hypothesis. But if you're just digesting this as just purely predictive information, that text doesn't add much. 

I want to add the big caveat that just about the numbers being right, the Open Source Asset Pricing project was really about equities. It really should be a cross-sectional stock return predictability data set. I'm not sure if you've heard about this, but there's been recent scandals. I mean, I think it's legit to say it's a crisis in corporate bonds. Now, it's kind of emerging in option pricing where these option return predictabilities. I think the option one is less widespread. I am not an expert in this but both of these literatures, which they have messier data, something very different than in stocks. 

We're blessed with the Center for Research in Security Prices at the University Chicago. But those guys really created an amazing data set. Because it's so standardized and so clean, it’s probably hard to pass off a crap number. But that corporate bond data, I'm not sure if you know, is kind of a mess. The very nature of corporate bond trading is so much messier. You don't necessarily want to extrapolate what I'm saying to other fields. Also to the future, I need to credit Tom Zimmermann for the replication and the false discovery rate stuff. Hopefully, people will read our stuff and learn from it. 

Ben Felix: You mentioned that the text in the peer-reviewed literature maybe doesn't add much, maybe the flip side of that. What do you think your findings tell us about the usefulness of things like machine learning for asset pricing research? 

Andrew Chen: There's two ways to think about this question. One way is to think about machine learning just as purely statistical methods for approaching research or for approaching investing. A derogatory way to describe this is data mining. What is machine learning? You just plow through a ton of data looking for patterns. That was previously really frowned upon. It was even taboo, I think, to talk about data mining. I think our research shows that data mining at least was undervalued in the eighties and nineties, 2000s. 

One of the striking results from the paper with Alejandro and Tom is that I'm not sure how feasible this is. But if you could data mine like we did searching through 29,000 accounting ratios, if you could do this in 1980, you could have uncovered all of these anomalies long before they were published, even decades before. If you just look for the stuff with the strongest predictability in 1980, you'll find the investment anomaly wasn't published until at least 2004, so like 24 years in advance of that. You also find external financing anomalies. You'll find a [inaudible 00:36:24] anomaly, inventory investment anomaly. You'll find also the earnings surprise anomaly. It also was clearly undervalued then. 

If you're talking about machine learning research going forward, the logic of what we see with markets getting more efficient over time means that machine learning that works now will probably not work later. Then you'll always have to try to stay one step ahead. 

Ben Felix: That's the same for the peer-reviewed research, though. Machine learning is no better or worse than peer-reviewed academic research for that purpose. 

Andrew Chen: To be clear, I think you'll get an edge. I think it'll be fleeting. It depends on how well you can do it. Similarly with the academic literature, if you follow up on it very quickly, you'll get some results. It seems like the market is adaptive. Maybe the market gets more and more adaptive. I'm painting things with a very broad brush. The bottom line is you have to act quickly, which is in retrospect it seems kind of obvious. People do talk about these behavioral biases sometimes as being some kind of fundamental part of our personalities. Sometimes, people come up with these stories about, as a whole, we'll interact in this way, and they'll create this predictability that’s just a mispricing. But empirical evidence doesn't support any of that being very permanent so far. 

Mark McGrath: Given everything we've just discussed, what do you think the implications are for people like us, like Ben and I, who use this type of research as peer-reviewed research for investing in asset allocation decisions? 

Andrew Chen: Big caveat that you're kind of asking me to extrapolate. If I'm going extrapolate, the major lessons are it's probably better to trust the numbers than the text. For the text, if you see some people claim some big thing, you probably want to verify that the numbers actually support that. That's kind of been a theme in my research. 

The other aspect of that, the other wrinkle in that is the numbers – This relates to the corporate bond issues. The numbers for more exotic and more dirty data, especially data that's examined by fewer people. I should mention that most of these anomalies that I've been talking about are documented using extremely standardized data sets that everyone has access to. But if you have these 30 or more exotic data sets, then you have to check it and be skeptical of it. But my research doesn't touch directly on that. I'm just saying that's kind of a boundary. 

Then the last thing is as we keep talking about, you have to act quickly. Don't expect it to persist. Even if someone says, “Oh, this is a new risk factor,” they write down a fancy equilibrium model to say, “Oh, there's a reason why this should exist, and it should continue to exist.” I think I would be skeptical of that still. Hopefully, the profession will get to writing ideas that are more grounded, more real, more reflecting the real world. We'll have to see. 

Ben Felix: What about the extreme case? How plausible is it that all asset pricing factors are just data-mined? 

Andrew Chen: Data mining has this negative connotation. Then the data mining is something that you could do as an individual or you could do as a profession. I think for the most part, people are not sitting around searching through copy stat for statistical significance and writing a paper about that. I think for the most part that's not happening. It's so taboo, like I mentioned. But as a collective, all these professors trying to publish papers, it could just turn out to look that way. This guy looks in this corner of the data. This guy looks in that corner. As a whole, as a community, we're doing that. There's nothing negative about that, in my opinion. 

8

What's, I guess, negative is that you think that all the economics that we learn, all these ideas we learn to get a PhD. You need to have some pretty deep understanding of economics to get through there. You would think that that human understanding would add something beyond just data mining. Unfortunately, for cross-sectional stock return predictability, as it was practiced from 1980 to 2015, that doesn't seem to be the case. It's a long-winded answer. Yes, basically, kind of plausible. 

Mark McGrath: Based on all your research on this, how would you describe the current state of cross-sectional asset pricing? Is it still useful? Is it productive?

Andrew Chen: Cross-sectional asset pricing has evolved a lot. I've been critical of this Harvey, Liu, and Zhu paper for confusing false and insignificant and completing many and most. But I think one reason why the paper is popular is it picked up a feeling that something was wrong with the literature. I want to be humble and say the paper's not published yet. We could make errors, too. But I think the paper with – my paper with Alejandro and Tom. We more clearly show that there's something really wrong here that we should add value beyond data mining. The data mining can work, too. Just to be clear, we should add value beyond it. 

After Harvey, Liu, and Zhu, which was published in 2016, I think the literature has tried to move beyond this. Here's one predictor. Let's make up a story around it and publish it. It's changed a lot. I don't know where it's going. I think it's promising to see there's so much machine learning being done in the literature. But like I was saying, before I would be skeptical of the claims. A lot of times, I feel like the numbers are right. I could replicate the numbers. But sometimes, the statements are too strong. A lot of times, a simple OLS does just as well as random force. Sometimes, random force is even worse than OLS. But it won't be portrayed this way because then there be less to talk about. 

I guess it's cautiously optimistic I would say. I think the literature is moving. It's changing. But, yes, I'm still wary of texts. I hope it's rational. We all have behavioral biases, but I become more skeptical of the text. 

Ben Felix: No kidding. Geez, crazy to think about. It shatters so much of what – the idea of factor investing kind of rests on a lot of beliefs about some story. People use different stories to justify whatever their investment strategy is, but they all rest on some story. You're kind of saying that the stories are not super relevant. 

Andrew Chen: I don't know what kind of stories people have in the industry. If you really have a brilliant, brilliant idea, you're not going to run around sharing it. I mean, although getting a publication in journal finance does guarantee you a pretty nice life, there's also incentives to do that, too. I still feel uncomfortable agreeing with you on this. It's kind of shocking all these stories, all this economics. It’s not just stories. Stories makes it sound pejorative. 

I like this term that John Cochrane has. He calls it economic parables. These should be real descriptions of the economy that are clean, that have a message to them. We make too many of them. In the big picture, we've been talking this whole time about the adaptive markets hypothesis parable. There's this tendency for markets to be efficient. If there's predictability, people buy the underpriced stocks, sell the overpriced ones, and trade it away. This is a parable, and that is an overwhelmingly powerful parable that's still underappreciated. We make a lot of parables. Maybe a lot of these underlying factors are not so helpful. 

Ben Felix: Incredible. All right, our final question for you. How do you define success in your own life?

Andrew Chen: What I try to do every once in a while is try to think about what it'll feel like to be at the end of my life and to be looking back on my life and to want to be happy about what I've done. 

Ben Felix: It's a great answer. 

Mark McGrath: It’s a great answer. I do the same thing. 

Ben Felix: All right, Andrew. This has been a fantastic conversation. We really appreciate you coming on the podcast. 

Andrew Chen: Thanks. It's a pleasure to be here. I think you guys have a great program, and I love how you get research out to the public. So happy to contribute.

Is there an error in the transcript? Let us know! Email us at info@rationalreminder.ca. Be sure to add the episode number for reference.