## Episode 251

Ben Felix: This is the Rational Reminder Podcast, a weekly reality check on sensible investing and financial decision making from two Canadians. We're hosted by me, Benjamin Felix and Cameron Passmore, portfolio managers at PWL Capital.

Cameron Passmore: Welcome to episode 251. After a great episode last week with Professor Campbell, but this week is another great one. I think by popular demand, Ben, you're going to dig into covered calls.

Ben Felix: This is one that just never died. People have been asking me to cover covered calls for like, I don't even know how long, since I started doing my YouTube videos. It was like, here and there, I'd get requests for it. It wasn't everybody asking all at once, but it's been one of the most persistently requested, even if not the most frequently requested, concepts to cover. I finally caved and spent a bunch of time reading about it, and I hopefully have some interesting commentary.

Cameron Passmore: Then much like we did a few weeks ago with Jonathan Clements, we're going to do a review of past guest, Robin Powell. He was guessing on 27, but he, along with his co-author, Jonathan Hollow, just released a great book called How to Fund the Life You Want: What Everyone Needs to Know About Savings, Pensions and Investments. We'll look back on our interview with Robin a few years ago, then those guys will join us after we do a quick book review. Phenomenal book, by the way. Then of course, we'll do the after show for the three people that stick around.

Ben Felix: There should be a shirt for that in the store.

Cameron Passmore: The three people?

Ben Felix: I don't know what it says, but it's a running joke, the last three people.

Cameron Passmore: That is true. earlier this year, Ben, you and I started promoting, I guess, our practice. Since we've done that, we've had a bunch of people reach out to the team, which is fantastic and it's great to meet Canadians who might want some help with their financial decision-making. We have a phenomenal team of a dozen, or so highly skilled people. If you're looking for some help and you’re Canadian, with your financial decision-making, please do reach out. Anything to add, Ben?

Ben Felix: I was just going to say, that's been interesting. I think we've always been a little shy, or hesitant about promoting our business. Since we've been doing it, the number of people getting in touch to talk to us about becoming clients has increased pretty significantly. I don't know what's contained there, what information is in there. I guess, that we just weren't talking about it enough and that there are people out there who could use a service like the one that we provide, but maybe just needed a prompt, or maybe didn't know what we did. I don't know.

Cameron Passmore: Reach out. We're easy to find. Okay, with that, let's get to the episode.

***

Cameron Passmore: All right. Welcome to episode 251 with the main topic being covered calls. I'll do my best to make sure we go through this slowly and understandably as I try to do. This one is particularly, in other words, complicated, but I guess it is complicated. I'll let you get going and I'll do my best to help.

Ben Felix: It is complicated. This is not part of my main coverage of this topic, but just as some commentary to start. One of the things we talked about in a recent episode was the complexity of financial products. There's some really interesting empirical research on how more complex products tend to perform worse and have higher costs for investors. We also talked about the concept of shrouding, how complexity can shroud high costs, where consumers end up paying costs they don't realize. Even fee conscious consumers might end up paying high costs, because the costs are hidden. Just an interesting preface to think about as we dive into this.

It is a complex topic when we start getting into options and payoffs and how all that stuff works. I did get input on these notes from a few people who know a lot about this stuff, including some of the co-authors of one of the papers that we referenced in the notes. I also talked to Patrick Boyle, who people may recognize from his YouTube channel. He's got a very large YouTube channel. He wrote a textbook on options and I know him casually. I sent him a note just saying, “Hey, can you look at this?” He thought it all looked pretty good.

I did try to get a whole bunch of input from people who know what they're talking about. We have Vinviz in the Rational Reminder Community. people know him by his username. I also chatted with him about it. Lots of input. Okay, I'm rambling on. We'll dive into it.

Okay. Covered call strategies, which are sometimes referred to as buy right strategies are often sold as producing high-income yields and generating equity-like returns with less risk. These claims, as you may have guessed, they fall apart under scrutiny, which is exactly what we're going to apply here. The target yields on these products are often above 10%, sometimes away above 10%. Those yields are often advertised in promotional documents and on fund websites and stuff like that. You also see statements like, enhances current income and lowers volatility and downside risk.

Cameron Passmore: Sounds good.

Ben Felix: Those are the claims we're going to dive right into. It's going to be a lot of fun. Now, it's important to remember, and this is something that Vinviz from our community reminded me about. I hadn't thought about this statement in a very long time. We got to remember that risk cannot be destroyed. It can only be transformed, or transferred.

Cameron Passmore: What a line.

Ben Felix: That comes from physics. It's a play on the law of conservation of energy, which says, the energy can neither be created nor destroyed. It can only be transformed, or transferred from one form to another. Risk is similar. You can't make it go away. You can just transform it, or transfer it to somebody else with a financial contract. Nice way to start thinking about this, because you cannot make risk go away. You can give it to somebody else. In this case, when you're selling calls to somebody else, you're the one taking the risk.

Covered call strategies don't generate income in the way that investors imagine. That's a big one. Talk about 10% yields. That's not really income. I'll explain what I mean in a second. their risk adjusted returns. That's one of the other big things. You expect to get – or the pitches. You might get a little bit lower total return than equities, but with much less risk, or with less risk in such a way that your risk adjusted returns typically measured by something like the Sharpe, or the Sortino ratio are going to be much more attractive. Now one of the things that I'm going to argue is that that is only true when risk is improperly measured.

When you use an incorrect measure of risk, it is true that the risk adjusted returns of covered call strategies can be very attractive, but that's due to an error in measurement, not due to a reduction in risk.

Cameron Passmore: Wow. Okay.

Ben Felix: These strategies are also generally going to be tax inefficient and more expensive to own in terms of fees and costs than simply investing in the underlying assets.

Cameron Passmore: That's a pretty good setup.

Ben Felix: That's the setup. Now, go a little bit into what the assets involved here are. A call option is a financial contract that gives the buyer the right to purchase a security at a set price.

Cameron Passmore: Check.

Ben Felix: When a call option is in the money, it can be sold before maturity, or exercise to purchase the underlying security below its market price from the option seller. Covered call strategies own securities. You own the underlying stocks, or assets in the index or whatever, and then you sell options on the same security. You own it, you own the security and then you sell an option, a call option on the security.

Say, it owns the S&P 500, then you sell call options on the S&P 500. It's called covered, because the underlying security is owned when the option is sold. A naked call would just mean selling the option without owning the security. Then in that case, you have unlimited downside with a naked call, because of security, price can go up infinitely, theoretically. Unlike a covered call, which can have negative returns only to this point that the underlying security goes to zero, because if it goes up, you're hedged by owning the security.

Due to put called parity, a covered call and a short put have the same payoff. I got that from Patrick Boyle. It's hard to think about. Options are confusing. But if you look at the payoff diagrams for the two strategies, it's very clear that they're the same. That's more just a point of interest. Selling call options does generate income through option premiums. That's one of the things a lot of investors find attractive, but it also puts a cap on the upside of the underlying securities, while only slightly improving downside risk.

When you sell a covered call, you're selling the right to purchase the underlying asset that you already own at a specified price. If the call expires without being exercised, you earn the return on the underlying assets, plus the call premium.

Cameron Passmore: Exactly.

Ben Felix: If the buyer of the call option exercises, the underlying securities have to be sold below their market value. Now, covered call strategies are typically going to demonstrate those high distribution yields that I talked about earlier, which seem attractive to income-oriented investors, but the yields are misleading, and this is one of the really important points. When an option is sold, the seller receives income from the option premium and they have a potential liability in the event that they need to sell the underlying shares below market value to the option buyer in the event of an exercise.

The fact that the option premium is distributed as an income yield, like that 10% yield that I mentioned earlier, that's super confusing to investors and we know about mental accounting being problematic and the whole concept of income investing and dividend versus capital, all that stuff. What selling covered calls is doing is generating current income from the option premiums at the risk of foregoing future capital returns due to appreciation for gone appreciation in the underlying security.

Cameron Passmore: Precisely.

Ben Felix: When you think about total return on a net basis, we would not expect covered call strategies to have higher risk adjusted returns than their underlying assets. That's important on its own. Unless, options are overpriced. I have three references for that statement. One is for an old paper by Fisher Black, once from Robert Merton, and one from a paper by a guy named Rentalman. That's not a controversial thing to say. You would not expect higher risk adjusted returns, unless options are overpriced.

That makes the income yield figure somewhere between irrelevant and overstated. Not completely irrelevant. That's not fair. You know what? It could be relevant to a behavioral investor. One of the things I'll talk about later is that to the extent that income and capital separation can be used as a tool to modify investor behavior, maybe it's not totally irrelevant, but at least from a rational non-behavioral perspective, it is completely irrelevant.

Cameron Passmore: How important is a line, unless options are overpriced?

Ben Felix: The total return of a covered call strategy can be decomposed into a reduced equity beta relative to the underlying and a volatility risk premium, which exists if options are overpriced. Writing options slightly decreases exposure to the underlying equity, while eliminating exposure to large positive moves, and we'll talk about the effects of that shift in the distribution as we move on to the next section. This is important though, because if you want a lower beta to an asset, you could reduce your exposure to the asset, but systematically selling options primarily makes sense as a strategy to pursue that volatility of risk premium, that option mispricing, but not as an income strategy, so that pricing piece matters because of that, because this strategy is interesting if options are mispriced, but much less so if they are properly priced.

Let's jump into the lower risk idea here. Covered calls are often sold as having equity-like return with less risk. That's one of the big selling points. We have to dive in the measure of risk, which matters a lot in making that judgment. The challenge is that options affect higher moments of the distribution, including skewness and kurtosis, being the big ones. A common measure of risk-adjusted returns, like the Sharpe ratio, which most people are familiar with, that's the ratio of an asset's excess return over the standard deviation of the excess return, that's going to be inadequate for assessing the performance of strategies that have options, generally, due to the effect of options on the normality of the distribution.

The Sharpe ratio follows the logic in Harry Markowitz's mean-variance framework, which assumes that the mean and the standard deviation of single-period returns are sufficient for evaluating the relative attractiveness of investment portfolios. Now, if you imagine a normal distribution, which is well-described by its mean and standard deviation, the distribution of outcomes is going to be symmetrical about the mean.

Now, when you write call options, you're going to slightly improve the left tail, the bad outcomes, by the amount of the option premium. I mean, that's another interesting point, is that these are often sold as having downside protection. You're getting an option premium, which slightly improves your downside, but you're not getting any hedge, because if the underlying drops, you're still fully eating the decline, minus your option premium. Writing call options slightly improves the left tail by the amount of the option premium, but it completely cuts off the right tail above the strike price. You do get a lower standard deviation, but you also get much more skewness.

Now, if you think about that, you're completely cutting off one tail of the distribution, lowering your standard deviation, measuring the risk adjustment returns of that strategy with something that only takes the first two moments, the mean and the standard deviation into account. Of course, it's going to make it look better.

Cameron Passmore: Fascinating.

Ben Felix: There are other performance measures like the Sortino Ratio, which replaces the standard deviation in the Sharpe ratio with downside risk relative to a benchmark. That's also going to be inadequate, again, due to the shape of the distribution, because we're really affecting that right tail, and the Sortino ratio is not worried about that.

There's another metric devised also by Frank Sortino, who came up with the Sortino ratio. He devised one called the Upside Potential Ratio, and that replaces the excess return over the risk- free rate, like you have in the Sharpe ratio, with the excess return over a benchmark. That ratio is more successful in assessing strategies with skewed distributions. We're measuring, in this case, the expected return above a benchmark over the level of downside risk, rather than the mean above the risk-free rate over the level of volatility, as with the Sharpe ratio.

When you use that lens, the Upside Potential Ratio lens to look at covered call strategies, they're typically going to underperform the underlying index, even before fees and costs and taxes are considered.

Cameron Passmore: Wow.

Ben Felix: It's not a perfect measure, or anything like that, but it is a measure that has been shown to work with more skewed distributions. When you flip the lens to that ratio, these strategies don't look so good, which I mean, it just makes sense because of how important the right tail of the distribution is for stock returns. We know that, empirically. The best months or whatever are really important to your total return. If you cap them, it makes sense, it wouldn't have a very good effect. When you measure using the ratio that takes that into account, it just makes sense that it wouldn't look so good anymore.

Now, Markowitz theory suggests that rational investors are going to weigh single period mean against variance and making asset allocation decisions. It implicitly assumes that mean and variance describe the distribution of returns. In that case, the Sharpe ratio is useful, but if investors care about weighing returns above a benchmark, above returns below a benchmark, and returns are not normally distributed, then the upside potential ratio is going to be more useful. I think that better describes what most people are trying to do with covered call strategies. Well, maybe they don't realize what they're trying to do, but mean and variance aren't the only things that matter in assessing risk, I think, is the main takeaway there.

When you account for that, the attractiveness of these strategies changes pretty materially. There's no perfect model for assessing risk-adjusted returns. It's ultimately going to come down to defining the user, the person investing in the strategy's utility function, which does mean that for some investors, covered call strategies could make sense. It's one of the hard things with investing. What are you trying to maximize? One of the things I've heard Fama say, I can't tell you what the optimal portfolio is, unless you tell me what your utility function looks like.

Cameron Passmore: Exactly.

Ben Felix: Even if we decide what the rational model is for assessing these strategies, and that model suggests that they're suboptimal, it can still be useful for prospect theory investors who are very risk-averse for small losses, but will take on investments with a small chance of very large losses, and investors who rely on mental accounting to determine their spending and who want to spend aggressively from their portfolio. An investor described by those behavioral characteristics, maybe this is a great strategy for them. There's a paper from Hersh Shefrin, who we've had in the podcast, actually co-authored with Meir Statman, who we hope to have in the podcast, or will have in the podcast. They've got a paper on this, on looking at covered call strategies through this behavioral lens. Then say, it's not so crazy when you consider these behavioral characteristics of investors, even if it is otherwise a suboptimal strategy.

Cameron Passmore: That's also the thing we talked about with upcoming guest, David Blanchett.

Ben Felix: Totally. There are all kinds of investor preferences and characteristics that you can try and model, that can make any strategy look good, given those investor characteristics and preferences. There's no correct model to say, everyone should invest this way. Now, all that said, if the objective is outperforming a benchmark, or some benchmark level of return, covered calls probably are suboptimal.

Now another approach of assessing the optimality of covered call strategies and the existence of a volatility risk premium is just controlling for the skewness and their return distributions using a couple of different control techniques that a paper that I found did. When you do that, when you control for that, any perceived superiority in risk adjusted performance disappears. Another way of saying that and what this paper I'm talking about concludes is that the abnormal performance of covered call writing is largely driven by the disregard of skewness and the measurement of its performance.

Cameron Passmore: Wow.

Ben Felix: The information on the shape of the distribution limiting the usefulness of standard performance metrics when options are in play, this has been known in academia for a long time. I remember Cam Harvey told a story about this when he was on our podcast. It's been known in academia for a long time, but in practice, you look at any fund web page and you see the Sharpe ratio still for any strategy. Maybe the Sortino ratio. It's a thing where whether they realize they're doing it or not, investment managers can effectively game the system. They can game the performance metrics by using things like options and other complex strategies that will make the Sharpe ratio artificially, but mechanically inflate.

If you know investors are going to look at that as a metric, then you can mark it, the fact that you have attractive risk adjusted returns, if you know people are using the Sharpe ratio to assess risk adjusted returns. That gaming, and there's a paper from Will Goetzmann actually on this, that gaming works even in the face of high costs, extremely high costs, which can be relevant for this covered call strategy that we're talking about specifically.

Now, Goetzmann in that paper, they did actually devise a manipulation proof performance measure, specifically to get around these issues. It's a little more complicated than the upside potential ratio we talked about earlier, but one of the papers that I'll mention in a bit, they actually use that manipulation proof performance measure, and again, show that these types of strategies that use option writing to generate income are suboptimal. I've alluded the fees and costs and taxes a couple of times. These are major considerations for this type of strategy.

When you look at XYLD, for example, which is a US S&P 500 covered call ETF, using Morning Star’s tax cost ratio methodology for estimating of the tax efficiency, you can think about this like an MER that you pay in taxes. XYLD has a tax cost ratio for the trailing five years of 3.49% compared to 0.65% for SPY, which is just a S&P 500 index fund. Big difference.

In Canada, it's a little different, because those option premium income is going to be taxed as capital gains. In the US, I think it's going to be taxed as short-term capital gains, which is less tax efficient. Maybe not quite as bad in Canada, but you're still getting pretty significant capital gain distribution yields in Canada. Of course, that is an additional liability for taxable investors to overcome. It's important to remember that you're paying tax on that income, but it's not income in the sense that an interest payment, or a dividend is income. It's income that comes with an embedded liability that empirically, we know actually reduces your total term.

You've got this big tax hit combined with a lower total expected return. Not the best. It's due to foregone gains in the event that the underlying appreciates. They also are going to tend to have higher fees, products implementing these strategies. If you look at again, XYLD, it's got a MER of 60 basis points. If you look at Canadian products doing covered calls, they're often similar fee range, or maybe a little bit more expensive. Of course, we're benchmarking that against 25 basis points for a VGRO, or three basis points for a VOO. We pay a lot more in costs. Now, those costs also don't include implicit costs, like bid ask spreads, just from more transactions. You're going to probably have higher implicit implementation costs as well.

Now, if you take a step back, so I mentioned a couple, just random examples of ETFs, but if you take a step back and look at the broad sample of mutual funds, live mutual funds using covered calls and covered puts in this sample to generate income tend to underperform, but measured both by their excess return and by that manipulation proof measure that we mentioned earlier from Will Goetzmann’s paper.

On that point, for completeness, I do want to mention that DIY investors implementing the strategy aren't going to pay those higher fund costs, but there's also research showing that individual retail investors trading options pay, like 12% spreads and they lose money on average. While it may be true to say that yes, theoretically, you could do this at a lower cost by implementing yourself, you might give up any gains in higher transaction costs than an institution might get.

Now, it is true that in a flat market, covered call strategies will outperform, because in that case, you're collecting the option premium and it's not being offset by foregone appreciation in the underlying securities. If you believe that the market, or a segment of the market is going to be flat, or slightly negative, in that case, covered calls could be interesting. Of course, timing the market is hard at best when you can't predict a flat market and cutting off that right tail of returns is not great, because we know how important the right tail is to total stock returns, especially in the long run. We've seen those stats on if you missed the best of months of returns, how much lower your total returns. It’s the same idea.

Covered calls are sold as high-income strategies with attractive risk adjusted returns under the hood. When you use the appropriate lenses to assess them and their risk adjusted returns, they're neither high income, nor do they have attractive risk adjusted returns, and especially net of fees and taxes. Empirically, when you look at funds that have been around for a while implementing these strategies, they've typically trailed a plain vanilla fund of the same asset class by a very wide margin, while having a higher Sharpe ratio. That's the thing, right, is that some people will look at, okay, it's trailed by 3% a year, but look at that Sharpe ratio. As we've hopefully articulated, that's more driven by measurement error than actual reduced risk, or increased risk adjusted returns.

Cameron Passmore: That's it?

Ben Felix: That's it.

Cameron Passmore: Okay. Good listener. Good viewer. How good was that? That was clean, understandable, concise, gold in my opinion.

Ben Felix: Glad you think so.

Cameron Passmore: I'm sure that will be used by many of our fellow advisors, or good friends in the community to share with people when they ask that question.

Ben Felix: I hope so. I'll make this into a shorter CSI videos, too.

Cameron Passmore: Excellent work. Okay. You good to move on?

Ben Felix: Yep.

Cameron Passmore: Let's do one episode in 60 seconds. But I want to give a backstory on this. The point of these is for regular listeners who may not have been around back in the earlier days to help choose an episode to go back and listen to. We welcome Robin Powell four years ago, Ben, if you can believe it. He was one of the higher profile guests that we had early on. I think he was that interview is convinced us to go to this every other week with a guest episode. I thought it'd be a good idea to highlight this.

Robin is an award-winning journalist and a self-described campaigner for positive change and investing. He previously worked in broadcast news in the UK. Was also in current affairs. He was a news reporter and documentary maker for ITV for 14 years, before joining organizations like Sky News and BBC. He's also the founder and editor of The Evidence-Based Investor, which is a news and content syndication service. He's also the editor of Advisor 2.0, which you can find at advicereinvented.com, which is a blog exploring changes in our sector, Ben. The financial advice sector. He’s also the founder of Ember Regis Group and Subsidiaries, Regis Media, which provides content to financial advisory firms and also, Ember Television, which produces and distributes video content about our industry.

He's a well-regarded individual, who's got a great background and incredible passion for the difference we're all trying to make. With that, here is a quick 60-second review. We'll see how well I do on time this week.

Episode 27 in January 2019, we welcome Robin Powell. What makes Robin really interesting is that he's a journalist who discovered our shared investment philosophy and now spends an unreal amount of energy spreading that word of this philosophy. Then he combined his background in television journalism to create a simply remarkable documentary called Passive Investing in the Evidence. In that, he interviewed people like Bogle, Ellis, Melchiel, Booth, French, Ferry, Bernstein and Sharpe, and these conversations he had with them greatly impacted Robin.

This documentary, along with a great deal of other content you can find at sensibleinvesting.tv. In addition to that, we discussed his views on the state of financial advice around the world, including the role of robo-advisors and how so many people think that financial advice is solely about recommending mutual funds, or moving money around. He, of course, says it's so much more than that. He says, we have a large responsibility towards client education. Also, being a journalist, Robin was able to speak about the short-term nature of daily journalism, which can cause people to lose long-term perspective. That was Robin Powell, our guest in episode 27.

He also wrote a book, which is our book review this week, which will be quick, because Robin Powell and his co-author Jonathan Hollow will join us in a couple of minutes here. The book they released is called How to Fund the Life You Want: What Everyone Needs to Know About Savings, Pensions and Investments. It’s part of our back to basics this year. We're featuring books and authors, if we can get them on, to talk about their book to help improve financial literacy.

This book, even though they targeted for people in the UK, the material is absolutely applicable to anyone. We introduced Robin already. Jonathan Hollow recently worked for the UK government's Money and Pension Service. He worked with leaders and regulators in government in the financial services industry to create the UK strategy for financial well-being. He previously worked as editor-in-chief for the Cabinet Office's online publications before becoming the Innovation Director at Cerco, which is a UK-based global public service outsourcing company. Incredible background.

This book, Ben, is fantastic. It's 277 pages long and it is an incredible resource. I would suggest that you buy the hard copy. I read it on Kindle, but there's workbooks in it that don't really work that well in Kindle. Hard copy, I would say, is a must. I really like how they started the book, which is what the chapter called Your Money or Your Life. They encourage you to think about the life you want, what's important to you, the goals that are important to you, and to realize that a happy life is made up of experiences, relationships and time, which of course is stuff we've talked about.

Aiming for money as an end goal is the wrong target. Obviously, we're in sync with them in terms of investment and planning philosophies, including things like capture market returns, manage your asset allocation, find a good advisor, and use conservative, safe withdrawal rates. One part I really did like is they highlight six rules that one must follow to be successful. In our conversation, Robin talked about a couple, but quickly, the six are have a purpose, a plan and a method. Take a slice out of everyone's business, own the market. Number three, to dilute your risk, add lots of time, focus on the long-term.

Number four, they call it phone a friend, especially when times are taxing. They suggest that someone, be it your advisor, your partner, or some other trusted guide to have a round to keep you anchored to your plan. Number five, focus on what you can control. These are things like savings rate, your behaviour, your spending and your asset mix. Number six, keep your investments simple, cheap, and automated. If you're looking for what I would call an active resource, resource you keep on yourself, I highly recommend this book. Check it out. The workbooks are excellent. With that, let's go to our conversation with the authors Jonathan Hollow and Robin Powell.

***

Cameron Passmore: Jonathan and Robin, welcome to the Rational Reminder Podcast.

Jonathan Hollow: Thank you.

 Robin Powell: Well, thank you very much for having us.

Cameron Passmore: Great to have you back, Robin. It's super great to welcome you back. Jonathan, great to meet you. I must say, I was asking before we started recording, I asked Jonathan how you guys met, assuming it was a part of your career. You guys have been friends for over 40 years.

Jonathan Hollow: We have. Then we decided to write a book together.

Robin Powell: It's strange, because we've had very different career paths. I've been a journalist, and Jonathan has worked in various communications roles. We've both developed a strong interest in financial education and helping people to do sensible things with their money.

Cameron Passmore: Where did you get the energy and what prompted you to write this book, which is an incredible feat?

Robin Powell: Well, that's a good question, because anyone who's written a book will tell you that it's not a decision you should take lightly. It's a huge undertaking. We really wanted to do this properly. We wanted to research it thoroughly. We wanted something that was absolutely evidence-based. It was a huge time commitment. There are lots and lots of books out there, far too many books, let's face it, Cameron, about investing. We just felt there was still a gap in the market for a book that was, as I say, evidence-based. But that was also accessible and written with real people in mind, with real lives and hopes and aspirations and so on, and not investing nerds.

So many of these books tend to be about which stocks and funds you should buy to become rich and so on. But we really, really didn't want that. We just wanted to help people, as the title of the book implies, to fund the lives they really want to lead.

Ben Felix: The other thing that's clear from looking at the book is that you wanted it to be practical. I mean, there are workbooks in the book, which is not super common. How do you recommend readers get the most out of the book?

Jonathan Hollow: Yes, we were very excited by the idea of attaching a workbook to the book. You can download it from Robin's evidence-based investor website, print it out and work through it alongside the book itself. We felt this was valuable and necessary, because there are just so many great tools and calculators out there on the Internet that will help you with so many different aspects of your financial life and looking at your own behavioural strengths and weaknesses and so on. But we didn't want just to have a index of them in the back that was a complete jumble.

We put them together in the logical framework. That means, if you work through the workbook, you're working through the sense of each chapter of the book and trying to apply it to your own circumstances. By the end of it, you'll have a good sense of your financial plan and where you stand, and have something really strong that you could take to a regulated financial advisor if you want to use one and have a great conversation with them.

In terms of getting the best out of the workbook, I mean, I think one thing I would say is it probably is helpful to have a physical copy of the book, because then you can scribble on each chapter as you go through it. If you're a procrastinator, it's probably a good idea to work out how long it takes to read the book, add a couple of weekends on after that and write down a date, recommit and say, “By date X, I plan to have completed the workbook,” having read the whole book.

Then the other thing we emphasize throughout the book is the importance of talking through what you find and what you think with your partner and/or with a friend. We absolutely say, don't go to your friends for investment tips, but there are plenty of really useful things you can go to your friends for, like how often do you discuss with your friends, how much money you think you're going to need to live on when you start working. That's something that everybody can discuss. There's a very little harm that can come from that and a lot of benefit. We recommend that people talk through the ideas and conclusions from the workbook with somebody they trust.

Cameron Passmore: Robin, I really like the six rules you guys highlighted and actually cover them in the intro to this conversation. Are there a couple of those rules that you'd really like to highlight?

Robin Powell: We really wanted to simplify this whole area of investing and personal finance and particularly, saving for retirement. We simplify it and we condensed it into these six rules. They're all important. But two particularly resonate with me. First, take a slice of everyone's business. It is just a no-brainer that if we want to provide for our long-term financial prosperity, that we need to invest in companies, equities, historically for well over a hundred years have reduced returns that are considerably in excess of bonds of cash, and so you really need to invest in equities.

All the talk is about, well, what sort of equities? Canadian equities, UK equities? Buy them all. You should really diversify across the whole world. I see it as taking a slice of global capitalism, if you like. If you're investing in shares, you're sharing in the profits of human enterprise. If you invest in bonds, you are effectively lending human entrepreneurs money to do what they want to do to make the world a better place to solve the world's problems.

Either way, capitalism has proved remarkably resilient. Just look at the last century and the extraordinary setbacks that investors went through. Yet, if you stayed the course, as Jack Vogel liked to say, you kept your discipline. It rewarded you in the end. The other rule that I would highlight really is to focus on what you can control.

Most of the things that we think are important are actually not particularly important in the long run. Almost everything about investing, we cannot control. We can't control the economy. We can't control the outcome of elections and referenda and so on. But we can control how much we pay to invest each month, or each quarter, each year, whatever it is. Also, we can control our expenses. As you guys both know, expenses are a really important part of this story.

Ben Felix: Jonathan, can you describe the eight keywords that you set up for managing money day to day?

Jonathan Hollow: Yeah, I certainly can. I mean, we devote a whole chapter in the book to managing money day-to-day, because of this profound truth that when you're earning, every pound or dollar you earn has to pay not just for your current life, but some of it has got to pay for your future life. You've got to squeeze as much as possible out of every part of your income. We talk about the eight words are accept, divide, track, stabilize, prioritize, trim, maximize and teach.

I'm not going to go through them all one by one, but just to pick out the themes in them. The first and the last, accept and teach, are really about you and your emotions and your relationship to money. You've got to accept any past mishaps, or fears, or mistakes you've made about money. When you have got a system for managing your money day-to-day, you really should be teaching it to young people. We may come back to that later in the conversation.

Then in the middle of that, we propose a very simple system. For some readers, the book, it's still a revelation, which is set up separate bank accounts, divide your money up into separate bank accounts, so that when your paycheck comes in, you've got some money going into an account for bills, some for an account for everyday spending. We recommend a separate account for holidays, because a lot of people will find it difficult to manage holiday spending. Then you can track the money that's going into those. That becomes a natural budgeting system.

Once you've got that natural budgeting system up and running and your money is stabilized, you've got to think about your priorities. Can you put more into your long-term savings? Can you trim your expenditure? Can you maximize what you're getting out of your savings accounts? All these things add up to a simple system, which doesn't require endless spreadsheets. It's really about setting money up into different bank accounts, drip feeding it in, and taking care that you know whether the amount you're drip feeding in matches what's going out of each of them each month.

Robin Powell: Good advice. In the book, Robin, you guys recommended that people continually keep up their knowledge up to date about what's happening in the world of money. What's the best way for people to do that?

Perhaps, maybe I should start this answer by reiterating something I said earlier, and that's that most of the things that we think are important, particularly as far as investing is concerned, are actually not important at all. They might seem really important in the present moment, but in the great scheme of things. They're not very important. I think you need to think very carefully about what information is really valuable.

I like to make a distinction between business news and money, personal finance news. I mean, we have this catch-all-turn, financial news, which I think is too broad. Business news is really interesting in its own right, how businesses are fairing in the cost of living crisis that we've got in various countries, including ours around the world, which sectors are doing well, what are the latest trends and so on. That's what I call business news, and it's got really nothing to do with investing. There are lots of investment writers and marketing people that fund management companies and brokers and soon, who will try to turn those stories into investment stories.

For example, I was just reading this morning a very ridiculous article about the spending trends of millennials and how you could actually position your portfolio to capitalize on those spending trends, which is complete baloney. I would differentiate between those two things. For personal finance and money news, how much is new? There isn't a huge amount of new stuff to say, particularly about how to invest, as you know. The most reliable newspaper and we find, this is not a plug. I'm not paid by them to say this. Johnathan, I mentioned the FT in our book. There's another very good website, Money Saving Expert, run by a guy called Martin Lewis here in the UK.

In Canada, I'm a fan of Rob Carrick in The Globe and Mail. I can't say I read that publication regularly, but most of what he writes about tends to chime with me. Look for reliable media sources. The other thing I would say is a critical thing that we go to in the book is this whole idea of tax changes. Tax changes are really important, wherever you are in the world, and you need to keep abreast of what's going on. What is the most tax efficient way to invest? The rules change all the time. It's actually really quite hard for ordinary people to stay abreast of all those changes. I would say, that's actually one of the strongest arguments for using a financial advisor.

Ben Felix: Johnathan, we talked earlier about day-to-day money management. How important do you think it is to have a regular savings habit?

Jonathan Hollow: Well, it's very important. In my last job, I worked for a government body called the Money and Pension Service. We did surveys of thousands of UK adults, and we asked them questions about what they believed, what they did. We set them tests about what they understood, and we looked at details of their bank accounts with their permissions. What came out of that was that regular saving was the golden lead indicator for lots of other good money behaviors. People who saved regularly were more likely to understand money better, more likely to have a healthy bank account, and so on and so forth.

What was really interesting about it was it wasn't about the amount. Even people who were saving really tiny amounts of money on a regular basis, for them, it was still a golden indicator. I don't think you can say that it's just because people with a surplus of money who are able to save are generally financially well. It seemed to be more deep-rooted than that. Whether its cause and effect was impossible to untangle with that type of survey. I mean, are people better with money, because they save, or is it the other way round? You can't be sure.

My hunch, and it's only a hunch, is it's a bit of a two-way street, and there's a golden circle of behavior and reinforcement and confidence. I would say, getting into that of putting even a pound, or a dollar away a month, as long as you stick to it, is going to increase your financial confidence. Obviously, many people can save more and they should save much more, but they shouldn't feel that they need to opt out if the amounts that they can afford are really tiny.

Ben Felix: Your comment about confidence is really interesting. I agree. We can't find causation with that type of data, but there's a lot of other literature that you may be familiar with about financial self-efficacy and financial self-confidence, and those are related to lots of positive financial behaviour. That's a really interesting comment.

Cameron Passmore: How do you guys think parents should teach kids about money?

Robin Powell: Well, I'm afraid the first thing is that they shouldn't rely on schools. We did, again, with the job I worked in, we did a lot of research into what was going on in the schools in the UK, but I was also part of an international network that was looking at best practice across the world. A lot of schools don't teach financial education, and with the ones that do, what you've got to remember is teachers are human. A lot of adults aren't financially literate and aren't financially confident.

That is probably going to seep out of the teachers who are actively teaching financial education, but who are not so confident, or self-aware themselves. It really is much more valuable done at home. I think, one thing I would say is think of the age of which you should start talking to your child about money, then halve it. Because most people start far too late. A lot of really important money attitudes and behaviours are formed at an incredibly early age.

Beginning to talk to your child about money at the age of five or six is not too early. Even before that, impulse control and self-control is such an important part of the way we manage money in later life. There are things that happen even before that that influence things. In terms of what the evidence showed about what parents should actually do, basically, there are three golden experiences at home that if the children were exposed to them, they were generally going to do better with money in later life. The first one was seeing and handling money from an early age, and don't forget how difficult that is in an age of digital cash, talking about money in the home, what it's worth, what it's used for, how to manage it. Then the third one was that the children who did well received money regularly and took responsibility for it.

Now with that last one, it could be pocket money, or it could just be delegating an area of the household budget to a child and saying, “Well, we need to get bread every week. We need to get milk every week. How about if I give you this amount of money, you could take responsibility for that.” Pocket money is part of that picture. There are other ways of approaching that as well.

Jonathan Hollow: If I could just add to that, what an amazing opportunity the current economic and global situation presents us with as far as educating children about money is concerned, I know the situation is similar in Canada. Here in the UK, we've had soaring inflation, higher inflation than pretty much anywhere in Europe really, and prices are particularly going up. Still question about whether we're going to see a recession and redundancies and so on, but people are already starting to lose their jobs. These are all really difficult issues that Brits particularly don't particularly like talking about, but they are really important to talk about.

Now is a really good time, I would say, to engage children about the value of money, the importance of work, the fact that we can't always rely on work, and we have to keep building our skills and employability throughout our lives. Because that's at the end of the day, our human capital is our most valuable asset of all. Just encouraging children as well to think about spending. Money doesn't grow on trees and we need to spend wisely.

Yes, we need to treat ourselves, but we also need to have savings and investments. We also need to set aside money as well for helping others less fortunate than ourselves. It's a really, really good learning opportunity, I think.

Ben Felix: Jonathan, something that we've talked about in a few recent episodes is that financial advice theoretically has benefits, but the financial services industry has a lot of really big problems that make it a bit of a minefield for investors. How would you suggest someone go about finding what you call a first-rate advisor?

Jonathan Hollow: We made that the last chapter of our book, because we wanted people to be as educated and self-aware as possible before they started to look for a financial advisor. Because really, the first thing you need to do is think about, well, what are my needs? I mean, Robin mentioned the importance of being up to date with tax advice. In the UK, being qualified as a tax advisor is a different skill from being a financial advisor and they may overlap in the same person, or they may not. You've got to think about the needs you have.

Obviously, in different countries, there are different regulations and there are different directories. At the end of the day, you're going to come up with a short list of people that you think might be the right person for you. One thing I would say is in this age, here we are talking on Zoom, you can have a perfectly good financial advice consultation over Zoom. The world is your oyster, or your country is your oyster. Don't just look about for people that you might be able to meet locally.

Then the other thing we suggest people do in our last chapter of our book is that they prepare what we call a death box. I got this expression from a very good financial advisor I used in the UK. It's an index of your bank accounts, a state of the nation about all your money, your savings, your pensions. This is what our workbook helps people to put together. The reason why that's so great to have before you go to see a financial advisor is firstly, they're going to know that they're not going to have to put that together themselves and spend hours and hours of scraping people's money information together.

Then the second thing is in that first meeting with them, because most of them will offer you, say, an hour's first contact for free, you can see whether they come up with some really brilliant ideas about your money circumstances. They can't do that, unless they've got your state of affairs in front of them in a really neat, indexed way.

Now, the reason why we call it a death box is because when you do eventually die, the people left behind will find it incredibly useful as well. Most people don't do it. Or if they do, they do it a long time after they should have done. We're very keen on encouraging people to think about that in terms of getting their affairs in order.

Robin Powell: I can't exercise enough the importance of going to your prospective financial advisor who you're interviewing with a list, a comprehensive list of questions. You really are listening hard. You can record the interview on your phone if they're happy with that, or certainly take notes. If you're not happy with any of the answers, then you should be very skeptical about using them. What professional qualifications have you got, Mr. Advisor? What qualifications do you have over and above the minimum requirement? Financial regulators around the world actually set a very low bar for becoming a financial advisor. What have you done over and above the bare minimum?

Here in the UK, we talk about restricted advice and independent advice. Restricted advice is absolutely worth avoiding. It is essentially sales. What you're looking for is an independent advisor who has the whole cross-section of investing products and so on to choose from. What is your charging model? Do you charge so-called ad valorem fees, percentage fees? Or do you charge an hourly fee, or do you charge a fixed fee? There's no right or wrong way to charge, but there are certainly advisors out there who are charging far too much money.

Generally speaking, paying by the hour, not many advisors will let you do that, but generally that's the most cost-efficient way to go about it. There's also fixed fees, which again, particularly those with larger portfolios, can work out considerably cheaper. How much would I pay for your advice on an ongoing basis? That's another critical question.

Also, just find out something about their investment philosophy. If the advisor is talking about the markets and his opinions on what's going to happen to UK shares, or Canadian stocks, or whatever, avoid, because nobody knows what's going to happen to those things. You really want to find out that this person knows about what Jonathan and I call evidence-based investing, that they know the shortcomings of active fund management, they know the importance of broad diversification and focusing on the long term. Those are really the key questions I suggest that everyone asks an advisor.

Jonathan Hollow: I think it's safe to say that advisors will not like the last chapter of our book, because we set out these kinds of questions. They are harsh, but fair questions, but they will ruthlessly whittle down your shortlist quite quickly to the really good ones. That's why we say, if you're going to pay for it, make sure they're first rate.

Robin Powell: The part that I liked about that chapter is you also asked, or proposed some more provocative questions. What is the latest evidence on the merits of active and passive? Fine. Then what other new evidence should I be aware of? Are there recent innovations that can help me manage my money better? What mistakes have you made recently? These are provocative questions. I think to tease out more of the character, perhaps, of the advisor. How was the financial advice profession changing? This is something that has been alluded to. We've talked about a lot on this podcast. But these are more, I think, thought-provoking provocative questions that someone can ask.

Jonathan Hollow: Exactly. We use this metaphor in the book of saying, your financial advisor is a financial bodyguard. They're there to compliment you. If you have particular weaknesses in your ways of managing money, you need an advisor who doesn't have those same weaknesses. You really do have to get to know their personality and try to predict their behaviour.

Robin Powell: At the end of the day, of course, it's all about trust. There are two components to that. One is getting satisfactory answers to the questions that I just suggested people ask, but the second thing is just a gut reaction to that other person. Can I really trust this person? Does he really get me? Cameron, that's such an important point that you make about the changing nature of financial advice. It is not about investment advice anymore. Investing, of course, it's important, but it's a small part. It's a relatively small part of a much bigger picture.

The most important thing is that you feel that this person is listening to you, is understanding what you're saying, will want to learn more about you and have an ongoing relationship with you and helping you on your investment journey. At the end of the day, that's such a subjective thing. Only you can say, having spoken to someone for an hour if you really entrust that person with your wealth and your financial future.

Cameron Passmore: Such a great point to wrap this up. Jonathan Robin, again, congratulations on the wonderful book. Thanks so much for joining us.

Robin Powell: It's been a pleasure.

Jonathan Hollow: Thank you very much.

***

Cameron Passmore: Thanks again to Robin and Jonathan for joining us. I thought that was pretty fun. It's also fun that they've been friends for 41 years, which is crazy. It goes back to teenagers.

Ben Felix: You can tell.

Cameron Passmore: Yeah, I thought there were colleagues that met in the biz, so to speak, but no, they've been long-time friends and thought it was time to write a book.

Ben Felix: No, it's nice. You can tell they’re buddies just from the way that they – I don't know. You can just tell.

Cameron Passmore: I know I keep mentioning in the show, but Succession as a show is phenomenal. Every week, we can't wait for the new episode to come out. You've been watching any shows recently?

Ben Felix: No. Sorry.

Cameron Passmore: Yeah, I think now that summer's coming, there's going to be less television, which is not a bad thing. I wanted to share with everyone that our friend and fellow financial advisor, Jeff Bernier, invited me on his podcast a couple of weeks ago, and it was super fun. His podcast is called The Money and Meaning Show. Jeff's an advisor in Atlanta. Really nice and really thoughtful guy and this pod is definitely worth checking out if you're interested. You and I, Ben, are going on for the first time together on someone else's pod in a couple of weeks, fellow Canadian Shaun Maslyk, who is a financial wellness advocate has invited us on his popular podcast, The Most Hated F-Word. That should be fun.

Ben Felix: Agree. I think it should be fun.

Cameron Passmore: Having the tables turned on us. You wanted to talk about CE credits?

Ben Felix: Oh, yeah. We talked a while ago about how we were working on a project where we would turn Rational Reminder episodes into continuing education courses that financial advisors can take. We have completed 10 episodes as fully accredited CE credits, both for IROC and FP Canada, or it's not IROC anymore. The New Self-Regulatory Organization? CIRO

Cameron Passmore: CIRO. C-I-R-O.

Ben Felix: We've been accredited by them and by FP Canada. They're priced for people who need CE credits. If you're a casual user, it's probably too expensive. We ideally will make a product for casual users, too. Right now, it's just CE credits, which are more expensive because we have to pay a bunch of fees to get them accredited. We want to at least recover our costs on that. We're pricing it right now at a $150 for the full package of 10 episodes. One of those episodes is worth two credits. I mean, when you look at the price of CE credits out there, it's not a bad price at all.

Cameron Passmore: I think, I have to do the course. We don't get credits for doing the production of this.

Ben Felix: Yeah. We don't get CE credits for creating –

Cameron Passmore: We have to go create our own exams.

Ben Felix: Correct. We have to go take the CE credits ourselves. For IROC, as any IROC advisor knows, we're coming to the end of a two-year cycle this year. There are 11 credits available in there. One of them is an FP Canada Professional Responsibility Credit and an IROC compliance credit, which on both sides of those are the harder ones to get, so our episode with Harold Geller met the accreditation bar for those types of credits there.

Anyway, the courses are great. The questions are really good. Ray on our team here created the questions and I think he did a great job. The interface is nice. We'll put the link in the show notes, but it just learn.rationalreminder.ca. You can see the product there. I didn't mention that for the $150, it's the existing episodes that are in there now, plus any additional episodes that we create between now and it's a year subscription for a $150. We're going to release this. We're going to say this on this episode and see what happens. If nobody signs up, then we're probably not going to do any more accreditations. Because we have to pay for them, like I mentioned earlier, for the accreditation process. If enough people sign up and I don't exactly know what enough is, then we'll continue. We'll get back on creating additional courses. I mean, it's a test. It's an experiment. We'll see what happens. But it's out there now. We hope people subscribe. I think it is a nice, useful product, but we'll see. We'll see what happens.

Cameron Passmore: I had some good people reach out to me. Benjamin reached out to me from Kitchener on LinkedIn. He has a book coming out this summer on cognitive and behavioural biases and how they affect long-term investing. he's going to send us an advanced copy and hopefully, it's great and love to have him on as a fellow Canadian and an author, which is nice.

On Twitter, we heard from Michael, who's got a PhD in stoicism. After listening to our conversation and book review with Lucas two weeks ago on the book, The Obstacle is the Way, he reached out offering to be a guest. Hope to have him on sometime as well this summer. It's really cool to hear from listeners that are engaged and has something interesting to join us about.

Ben Felix: Definitely.

Cameron Passmore: Meetups coming up. LA September 9th, future proof conference in the fall. If you're going, let us know and we're hosting a breakfast. Toronto meetup September 20th, Edmonton for the IAFP conference. Our friend Marcus offered help set something up. If you're going to that, drop us a note for any one of those events at info@rationalreminder.ca. Unreal guests coming up, Ben. We have Burt Malkiel next week. David Blanchett in three weeks. Meir Statman in five weeks. We have authors Nick Maggiulli and Jill Schlesinger coming up. Incredible lineup of guests. We've already recorded Burt Malkiel and David Blanchett. Incredible conversations.

Ben Felix: Those were incredible. We have the fun task now of probably, later today after we record this, we're going to map out guests for the rest of the year. That should be fun. I know we've already got some very interesting names in mind.

Cameron Passmore: Exactly. As always, reach out to us. We're on Twitter, LinkedIn, we're on Instagram, companies on Instagram as well. Anything else, Ben?

Ben Felix: No, I think that's good.

Cameron Passmore: Oh, something we should highlight is the webinars that the team has been doing. We've been doing a lot of live events lately and they're going to be posted on the PWL Capital YouTube site. I see the first one has already been posted there that they did. It's Canadian centric on some tax updates, but that was a couple of weeks ago. It's there, but more of these events will be showing up. Go and hit subscribe on our YouTube channel.

Ben Felix: We'll announce any future webinars. The timing hasn't lined up where we were able to mention them on an episode before they happen. For future webinars that we're planning on doing, we'll mention them here on the podcast and people can check them out. The ones we've done, that like you said, we'll post recordings out. They've been great.

Cameron Passmore: Yeah. If you follow us on Twitter or LinkedIn, we'll repost everything that comes up. The team's really got a format down where it's an active dynamic, Q&A type format for a lot of these. They love doing it in the engagement. There was one last night that the engagement I heard was fantastic. Again, we're grooving just prompt questions using a tool they have in this presentation software.

Ben Felix: Very cool.

Cameron Passmore: Anything else this week?

Ben Felix: I don't think so. I think we're good. Hopefully, the covered calls topic was interesting. If people thought it was or wasn't, let us know in the YouTube comments, or in the Rational Reminder community. It's always great to hear from people about what they thought about the episode, because that's something that we don't always get. Then we don't know. Was it good? Do people not comment because it was bad, or because it was good, or because it was mediocre? We just never know. We always appreciate comments about the content, whether it was good, or what resonated, or what didn't.

Cameron Passmore: Beautiful. Thanks, everybody, for listening, and we'll see you next week.

Is there an error in the transcript? Let us know! Email us at info@rationalreminder.ca. 

Be sure to add the episode number for reference.