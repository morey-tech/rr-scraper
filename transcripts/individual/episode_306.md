## Episode 306

Ben Felix: This is the Rational Reminder podcast, a weekly reality check on sensible investing and financial decision-making from two Canadians. We're hosted by me, Benjamin Felix, and Cameron Passmore, Portfolio Managers at PWL Capital.

Cameron Passmore: Welcome to episode 306. And this week, Ben, it is a complete ringer. What a conversation. I'm going to steal a line from our guest, "We're going to get our hands dirty with data and fight for every basis point." What a phenomenal conversation with Wei Dai. 

Wei is the Head of Investment Research and Vice President at Dimensional Fund Advisors. She holds a doctor of philosophy degree in statistics, operations research and financial engineering from Princeton. And prior to that, Wei earned a bachelor's degree in mathematics and applied mathematics from Zhejiang University. She's based in Singapore. Joined us from Austin. Unbelievable. The notes I took down, the highlights, it just covered so much ground so clearly. Technical stuff. Beautifully presented. What say you? 

Ben Felix: What say me? Incredible conversation. It's got to be one of my favourites. Although, that's like naming a favourite child, I guess. 

Cameron Passmore: As she said.

Ben Felix: She talked about that too with picking factors is like picking a favourite child. Wei has done a ton of research. Obviously, in her role at Dimensional. But she's published a ton of papers. Both white papers for Dimensional, but also published academic research on topics relevant to, obviously, investing and portfolio implementation, factor investing. How to select the individual securities that are going to make up a factor portfolio. We really got into the details of different ways to do that and how to evaluate the different approaches. And how Dimensional does it? And why they do it that way? I thought all that was great. 

We talked about premium timing, which was also great. Can you use valuation ratios to predict when you should be in stocks or when you should be in value versus growth stocks and all that kind of stuff? I thought her insights based on her research on that were incredible. Diversification was another big one. And this is one that, as I mentioned during the episode, has been discussed at length in the Rational Reminder community. 

Dimensional has a couple of papers looking at the relationship between diversification and the reliability of capturing premiums. I'll spare you the details for now. But that paper, anyone who's in the Rational Reminder community will know what I'm talking about, has been discussed at length. And getting her thoughts on why they set the analysis up the way they did and what the implications are for portfolios I thought was super interesting. We also talked about how to select a systematic investment manager. What to look for? And how you should hope they are charging their fees.

Cameron Passmore: Oh, that discussion on how to valuate performance fees. 

Ben Felix: Yeah, I like that too.

Cameron Passmore: I've never heard it put that way before. I thought it was brilliant.

Ben Felix: I mean, it's a new paper that they have. I think it's a new thinking on that topic. Co-authored with. 

Cameron Passmore: The whole short-run reversal part, so interesting. And how it's different from momentum.

Ben Felix: And how to measure it. And how – 

Cameron Passmore: Implement it? 

Ben Felix: How they had to think about – yeah. That's another paper. That's with Professor Novy-Marx. And then she's got the one on systematic performance fees with Bob Merton.

Cameron Passmore: Uncle Bob.

Ben Felix: She's doing research at Dimensional, which is incredible on its own. Because, obviously, your research at Dimensional is being reviewed by people like Fama and French. But Wei's also been co-authoring with Professor Novy-Marx and Professor Merton, which, as she says, when I asked her about this in the episode, is pretty cool.

Cameron Passmore: Okay. Good to go? 

Ben Felix: Yeah, I think so. This is a good return to, as you like to call it, a bit of a red meat episode. I'm excited. Hope the audience enjoys it.

Cameron Passmore: With that, let's go to our conversation with Wei Dai. 

***

Ben Felix: Wei Dai, welcome to the Rational Reminder podcast.

Wei Dai: Well, thanks for having me. I have been a regular listener of your show.

Ben Felix: That is very cool to hear. Wei, what are the main risk premiums that Dimensional targets in portfolios?

Wei Dai: In our equity strategies, we will target the size value and profitability premiums. I think your listeners are already quite familiar with some of these concepts. Essentially, the size premium being the differences in expected returns between smaller cap versus larger cap securities. And value being the difference between those with lower relative price. Value stocks versus those with higher relative price or gross stocks. And then, finally, profitability being the difference between companies with higher profitability versus those with lower profitability. 

These are what we call long-term return drivers. That means we can structure our portfolios around to get broadly diversified and low-turnover portfolios. We do consider a lot of shorter-term, fast-decaying signals when we decide daily what to buy and sell. Definitely happy to get into some of that later related to momentum or [inaudible 00:04:43] fees. And then short-term reversals being the latest addition in that category. 

Ben Felix: Can you talk about short-term reversals briefly? Just what is that and how is it used? 

Wei Dai: The short-term reversal, that's basically the tendency for stocks for recent winners to underperform the recent losers. And then we're talking about very short horizon. Essentially, if you're ranking stocks over the last, say, months or couple weeks and then you see that ranking reverse in the more recent, in the next month or so. 

There has been a really long literature on that. Even the first time was documented in Fama's research back in 1965. And then there has been some recent papers kind of linking to liquidity provision. And we did a work with Professor Robert Novy-Marx on that related to more the cross-sectional variation. Happy to maybe talk about that later in the [inaudible 00:05:31] show. 

Ben Felix: I do want to come back to that. On the long-term drivers of returns, can you talk about how the magnitudes of the expected size value and profitability premiums vary across regions? Like, Canada and the US, for example? 

Wei Dai: That's actually a question we do get a lot from clients. I understand where the questions come from, because the realized premiums we observe are different across regions. And you ask about Canada versus US. And, also, for example, we know that it has been challenging period, for example, for size and value premiums in the US. But then you actually see, over the same period, the premiums have been much stronger outside the US. In particular, in emerging markets. 

But then the realized premium we observe are the combination of the expected premium and also the unexpected. To your question, what can we say about the expected magnitude of the premiums? Because that's what our investment decision should be based on rather than extrapolating the unexpected noise. 

For that, we did a bunch of statistical tests to try answer that question. Essentially, for each premium, size, value, profitability premium, we ask whether the magnitude is reliable different in one region versus another. Essentially, we did a two-sample t-test for each pair of regions. For example, US versus DevelopX US. US versus emerging markets. DevelopX US versus emerging markets. In the end, we cannot really reject the hypothesis that the expected premium is the same between any two regions. 

We not only did that for each premium, we also tested the premiums jointly. All three of them together in one region versus another. That's essentially a multivariate extension of the two-sample t-set. Again, cannot say the premiums are reliably different across regions. 

Ben Felix: What about relative to each other? Is the value premium different from the profitability premium? 

Wei Dai: Exactly. We were just talking about the test across regions. And you can do similar tests across premiums as well. Instead of looking at different pair of regions, we basically look at each pair of premiums. Right? Size versus value. Value versus profitability. Size versus profitability within each region, but also all regions combined. Also, a set of statistics tests that we did. Again, they are very similar conclusion. We cannot really see reliable difference between any pair of these premiums. And that is also further confirmed by kind of running an F-test on the equality across all three premiums jointly in any region. Sometimes I joke with our clients that this is like asking parents who their favourite kid is. Well, we love them equally. 

Ben Felix: That's super interesting. Across regions, premiums are not statistically different. And then the premiums relative to each other are not statistically different. It's hard to say value is better than profitability or emerging markets like your earlier example is better than US. 

Wei Dai: I think the takeaway is that, probably, the investors shouldn't really favour one premium over another or one region over another just based on your perceived magnitude difference of the premiums. To your point, I think it makes a lot of sense to be globally diversified, integrate multiple premiums if you can, and also have balanced tilts. 

This is not to say that investors should never have more emphasis on one premium over another or overweight a region. We all know that there are good reasons for them to, say, have home bias or maybe have different types of factory exposures to complement other parts of their portfolios. You just need reasons that are justifiable.

Cameron Passmore: Can you expand on that? What are some typical approaches to pursuing multi-premium strategy in a portfolio? 

Wei Dai: I'm glad you're asking that. Because I feel, in the industry, there's a lot of discussion around which premiums to pursue, which variable to use. But not enough intention really paid to how you go about pursuing those premiums? In the end, even with our agreement on the same set of premiums, you can get very different outcomes depending on your implementation. Depending on your approach. 

To your question, I've definitely seen a few different approaches. One is basically just say let's combine single-factor portfolios. You can imagine having a small cap portfolio, a value portfolio, and then a high profitability portfolio. And maybe you put one-third in each. That's one approach. 

And another one I see is more like a market satellite approach. The majority of portfolio may be in just the plain market. And then you get the factor exposure just through the satellite. And, typically, that satellite will be a lot more concentrated, say, deep value, highly profitable corner within small caps. 

And these two are what I will call as combination approaches. Basically, you're combining these different components. And in our mind, a better approach is the integrated approach. Essentially, you start with the market and then you consider these premiums together. Essentially, you do a three-way sort on size, value, profitability. And then you can gradually shift weight away from the segments with lower expected returns to the segments with higher expected returns. 

Sometimes we use the analogy of tilting the ice cube tray, right? You think about the water going from one corner to the other. But now I think about it's probably too ancient of analogy. I don't think my kids have ever seen an ice cube tray. But I think with that approach, we do think it's more effective in terms of giving you that exposure to higher expected returns and give you better risk control, and also is more cost-efficient. 

Ben Felix: Can you keep going on the tradeoffs just between those – like you mentioned, integration being the one that you guys like. Can you just talk more about the trade-offs of those three approaches? 

Wei Dai: Ultimately, when you think about those portfolio designs, you care about expected return, risk, and cost. These are really fundamental aspects to portfolio design. Now if we start with that single-factor portfolio, essentially, you're looking at each factor in isolation and then you combine them. But then there are interactions between these premiums. Small cap deep value stocks, they're probably not the most profitable companies out there. 

As you sort on size or relative price, you're already getting the dispersion in profitability. When you then combine those single-factor portfolio together, you may actually get offsetting tools towards different premiums. You don't really have good control over the premiums. 

For the market satellite approach, we are saying you are basically getting the exposure through that satellite. That means in order to get the same level of our performance, you need to push a lot harder on that satellite. And, essentially, you're using the information about expected returns only in that one corner of the market, so you end up overweighting a small corner of the market by a lot more. I don't think that that's a kind of efficient way of using your tracking error or using your deviation from the market. 

And in contrast, if you think about an integrated approach, it's a lot easier to account for the interactions between these premiums. And then you can get more balanced tilts. And because the over and underweight will be more evenly spread out across the entire market, so that's a more measured deviation from the market. 

In our analysis, we show that for strategies that have, say, similar historical outperformance, compared to the combination approaches, you do get lower tracking error coming from the integrated approach. And that actually leads to higher reliability of output performance. 

I will also maybe mention the cost consideration. Because in the practical world, that's important. Typically, with the combination approaches, you also see higher turnover. Not only within each component. But, also, you also need to do the rebalancing between components. And, also, it's not just the level of turnover. The cost per unit turnover can also be higher. Because if you think about that market satellite approach, a lot of turnover will come from that small-value, high-profit corner. That's probably not the cheapest segment to trade. 

Whereas for the core approach, basically, everything is all-in. You're breaking down that artificial boundaries. You're not buying and selling the same securities. And because the over, underweights are more spread out, more gradual. As stock prices change, expected return changes, you need to rebalance. The amount of rebalancing that's needed is also more moderate. From those perspective, we do think the integrated core approach will give you better tradeoffs between expected return risk and cost. 

Ben Felix: I heard like a tracking error and turnover is being a couple of the lenses that you use to evaluate the quality of an approach. Are there any other analysis lenses that you use to look at these differences? 

Wei Dai: I think when it comes to evaluating these portfolios, it's very helpful to evaluate holistically. It's usually not just one number. That's the smoking gun evidence. We tend to use a lot of holding space and also returns-based analysis. 

Starting from returns-based, basically, you look at the time series of returns. Of course, you can look at new absolute returns, access returns, volatility, tracking error. Also, helpful I think to kind of bootstrap the return series, so that allows you to calculate the probability of output performance over different holding periods. And that's how we see the core approach will give you that higher probability of output performance. 

And in terms of the holdings-based, I would say, usually, the starting point is just to at some of the aggregate characteristics. For a lot of portfolios, you can say let's look at weighted average total capitalization or maybe aggregate price to book, weighted average profitability. And you can compare the portfolio relative to the benchmark. And that gives you some sense about the tilt. 

But, usually, that doesn't give you the full picture, again, because of the interactions. You can imagine small-cap value firms, they have lower profitability to begin with. As you tilt towards size value, even if you also tilt on profitability, the aggregate profitability number might still be kind of market-like. You're not really seeing that tilt directly, which is why we think it's quite important to look deeper and say, "Well, we typically look at that is to say, well, let's look at the weight distribution across different market segments." You can segment into size, value, profitability segments and you say how much the market is in different segment and how much the portfolio is in those segment. Then, that way, you can look at some of the over and underweight to evaluate factor exposures. You can do that for a single strategies. Also, for the overall asset location. 

I know a lot of people also use maybe commercial risk models to look at factor exposures. I would say that the type of holdings analysis I was referring to really has the benefit of being very straightforward and intuitive and then requires no modeling. It's not very sensitive to say model misspecification or parameter choices. Then you can look at each snapshot and monitor overtime. That's why we tend to provide those type of data lenses to our clients.

Cameron Passmore: Great description of an integrated approach. But I'm wondering, are there cases where an approach like that would not make sense?

Wei Dai: That's an interesting question. I think we've been talking about more like market-wide poor integrated portfolio where you integrate multiple premiums in a balanced manner. But I can imagine, there are definitely many cases where investors might want to use more of a components portfolio. Think about a small value portfolio or maybe a large profitability portfolio. 

Some of the reasons may be related to what they hold in other parts of their location. Some maybe – they may already getting certain exposure through their, say, traditional active, or private, or even if they are thinking about their human capital relative to their financial capital. There can be reasons to say I want to customize my factory exposures more. 

And, also, when we talk to, for example, some institutional clients, they sometimes just divvy up the different market segments. And they have different teams overseeing different parts. I do think the component strategies can play a pretty important role there. But even there, I would say you should still consider multiple factors within that universe. 

For example, if you think about the value strategy. Yes, your first cut is on value. But then within the value universe, you can still consider the market capitalization, profitability in addition to the value metric. To some extent, you can still do multi-factor within that kind of a single-factor structure.

Ben Felix: Once you've decided on a level of factor exposure, what are some of the ways to approach assigning individual security weights to achieve that exposure?

Wei Dai: Okay. Weighting schemes. We're really getting into the weeds today. I think that's definitely another important aspect to consider when it comes to portfolio design. We decide on the premiums. Let's say size value profitability. But then there can still be many different weighting schemes. Again, leading to very different portfolios. 

And, in, fact we did a paper on eight different weighting schemes that are commonly used in systematic equity portfolios and index design. I'll just mention a couple here. One is rank weighting. Essentially, you rank stocks on the factors you want. In this case you have, say, a size rank, a value rank, a profitability rank. And you take the average of these ranks. And then you can say, "Well, let's assign the weight to be proportional to that average rank." 

Sometimes you also see, say, a Z-score weighting. Meaning that instead of using ranks, like from one to n, then you use the characteristics related to those factors, but transformed or standardized into Z-scores. And you also see some others with similar flavours. People sometimes call signal strength weighting. 

And, of course, for a lot of the weighting schemes, there are usually many other moving parts and other constraints that will be placed on top of that. But I think what I described kind of capture the main spirit of some of these weighting schemes. 

Although the details are different, one thing that they have in common is actually that they break that link between market cap weights of the security and the portfolio weights. That's why in our paper, we call them non-price-based weighting schemes. Because the security weights will be just proportional to the rank or to the Z-score regardless of how big or small the stock is to begin with. 

And the problem with that approach is that that can lead to oftentimes very uncontrolled overweights in the smallest names. And then that weight will be taken from the biggest names. That can also lead to very significant underweight in the biggest names. 

More concretely, we see in our analysis sometimes you end up with, say, overweighting some of the small-cap names by 50 times or even 100 times their market cap weights. And then for the largest stocks, the Mag 7 of the world, you may be holding them at basis points. Those deviations are definitely very much on the extreme ends. Some of the extreme deviation can actually produce shiny performance on paper. But those portfolios are just not practical. And that paper performance is very unlikely to actually survive the turnover and trading cost in the real world. 

Cameron Passmore: Can you expand on how Dimensional approach is assigning individual security weights? 

Wei Dai: That's definitely what I would like to go next, because we feel like the non-price weighting schemes have those issues. What we think is a better way is to actually have a weighting scheme that's a little bit more tied or more tightly tied to the current prices and market cap weights. That's why we call it a price base. Basically, that's the weighting scheme that we use in our integrated approach. And, internally, we referred to it as a multiplier approach. It's a very nerdy term. 

Just let me explain. What we do is, for the stocks in our eligible universe, we're going to independently sort those stocks by their market capitalization, relative price and profitability. Three-way sorts. And the intersection of this three-way sort will then form groups of securities or firms with similar characteristics. For example, your mega-cap growth high-prof firms will form one group. And mega-cap value low-prof firms will form another group. 

And each of those groups will then be weighted in proportion to their total market capitalization times a multiplier. And that multiplier effectively is what we use to control that group's over and underweight relative to their market. If the multiplier is 2x, that means you're doubling the market cap weights in your portfolio. If it's, say, .5x, that's underweighting. You're half-weighting the market segments. 

We design those multipliers to kind of more gradually increase as we move from groups with lower expected returns to those with higher expected returns. And then within each group, we then hold those firms in proportion to their market capitalization. It's not the easiest waiting scheme to explain, I have to say. But I do think it has great properties in terms of your targeting of your higher expected return and controlling risk and cost. 

Maybe just to elaborate a bit more there. In terms of expected return, we all know that prices change all the time. Expected return potential also changes all the time. By tying your security weights to the market cap weights, the market prices, you're effectively considering that up-to-date information about expected returns in your portfolio. That's great in terms of targeting higher expected return. 

Now, second, on risk. Earlier we talked about some of the uncontrolled over or underweights. This type of weighting scheme that we use can be very robust in terms of risk control. Essentially, how much you allowed to over and underweight is explicitly controlled through the multipliers. 

For example, let's say a small value high-prof segment of the market. Yes, it may have higher expected return, but it may only take up 1% of market. We're not going to put half of our portfolio there. You can have a more explicit control on your over and underweight. And, lastly, on cost. In terms of turnover, the multipliers are more gradual. That means, as stocks migrate from one group to the other, the turnover tends to be more moderate and limited.

And, also, remember, within those groups, we're actually mega-cap weighting them relative to each other. That means you can actually take advantage of the natural rebalancing that comes with market cap weighting. And, lastly – because, earlier, we talked about customizing factor exposure and accounting for the interactions, we do think that this weighting scheme of working with size, value and profitability directly, those three dimensions, considering them together will give you better control over the exposure you want versus, say, "Okay, we only use the average rank." 

We actually have an example in the paper showing that you might have actually two securities very different. Maybe one is small growth low-prof and another being large cap value high-prof, but they may have the same average rank. But we actually want to deal with them differently. Maybe the small growth low-prof, you want to exclude. The large value high-prof, you want to overweight within large caps. 

To some extent, I feel it's a bit like working with a pancake premix that's already all mixed. You don't have too much control over. Versus directly dealing with the flour, the eggs and butter. Then you can still make pancake, but you can also make a sourdough, croissant. There's a lot more control over the exposure that you actually want.

Ben Felix: A three-way sort on size, value and profitability. And then there's a multiplier, kind of a fixed multiplier assigned to each one of those categories. And then stocks are sorted daily by those three dimensions? 

Wei Dai: Yeah.

Ben Felix: And then weights are assigned to the individual stocks. Super interesting. What about investment? You talked about the three dimensions that firms are stored by. How does investment, the fourth dimension, factor into weights? 

Wei Dai: Some work we did a few years ago related to basically firm with high investment tends to have low expected returns. We see that you use the asset growth as a variable to measure investment. That's more of a catchall variable. That gives you a good information about future investment. 

What we see though is the effect is mostly in small caps. And, also, it's not a continuous effect. It's more like a cliff-like pattern that we see. For example, if you sort small-cap stocks from those with lowest investment to the highest investment, let's say deciles. First 8, 9 deciles, they are pretty similar. But it's more the last decile with the highest asset growth, that's where you see the big cliff-like pattern. Basically, a big decrease in the average returns. 

Because of that, we feel that it lends itself pretty well to more of an exclusion approach. Rather than using it as part of a multiplier, going to basically exclude those stocks with high asset growth within our small caps or any portfolios that host small caps. That's kind of an additional exclusion that we did in addition to the small growth low profitability I used in the example earlier. That's another exclusion we use. 

I feel that's also kind of where the research meets the implementation. You have the research findings, but then you also need to think about how you actually implement in the actual world depending on the finding and depending on the behaviour of the premiums.

Ben Felix: There's a three-way sort. There are multipliers. And then there's an exclusion for asset growth. Are there any other exclusions? 

Wei Dai: For small growth low profitability, that's another exclusion we do within small caps. And then there is also – these are more exclusions from our eligible universe. We're not going to buy them in the first place. But then there are also other short-term signals we use that's more related to buying stock safely. Maybe there are certain stocks we want to delay buying. If the stock is on a downward momentum, let's say, or maybe has very high lending fee on special, or latest addition being reversals. If it's also have done well recently in terms of our reversal signals. Those are the ones we might want to refrain from buying more. And then we can actually emphasize buying others. Definitely a lot of details when you think about combining all of these different signals. 

Cameron Passmore: Here's a question that's very popular in Canada and I'm sure many other countries, how should investors decide whether to currency hedge their foreign asset exposures? 

Wei Dai: I'm happy if actually investors are asking that question. At least that means that they are going beyond their home market. They are enjoying a bigger opportunity side and they are getting that global diversification. I think then the currency hedging decision will depend a lot on their asset allocation and also their investment goals. 

We did do a few papers on the impact of currency hedging on your overall portfolio. In terms of the impact on volatility, that very much depends on basically how volatile your assets is relative to currencies. Typically, with equities, equities already move around quite a bit. At least on par or even more volatile than currencies, then hedging currency exposures will have very little impact on your equity investments or for any portfolios that's already very heavy in equities. 

And in contrast, if you think about fixed income, fixed income tend to be less volatile. Everyone knows that. And much less so than currency movements. Then currency hedging can be a very effective tool to reduce the portfolio volatility for fixed-income heavy portfolio. That's on the volatility side. 

Now on the return side, it gets a little bit more interesting. I think you can actually decompose the return difference between the hedge portfolio versus the on-hedge portfolio. The difference has two terms. One is basically your forward currency premium. The second is the currency return. 

The currency return part, based on our analysis, it's not really predictable over the short term. Basically, you can treat it as a very noisy zero. And then the forward currency premium, basically that's what you can calculate from forward rate and spot exchange rate today. That actually can tell you then something about the expected return difference between hedged versus unhedged version of your assets.

That means you can actually use a dynamic hedging approach in attempt to increase expected return. Essentially, you can say, "Well, let's just hedge the currency exposure in markets where the forward currency premium is positive. Expected return of the hedge portfolio is higher. And then you leave the currency exposure unhedged otherwise. And that's approach that can increase your expected return. And, also, it does not require forecasting exchange rate movements. But then in terms of volatility, it will give you more volatility at least for fixed income investor. It will make sense for fixed-income investors if you are willing to take on that additional return volatility. For equities, the volatility impact will be minimal. 

Ben Felix: Interesting. If someone's currency hedging their foreign equities, does it make more sense do you think to have like a constant currency hedge? Or should it be dynamic using forward rates like you said? 

Wei Dai: It's kind of depends. I feel there are a few different things at play here. Let me take a step back to say, typically what we do, we would actually leave the equities unhedged. And then we hedge on the fixed income side more as a default. This is mostly coming from that volatility impact perspective. And that's also frankly where we see a lot of client demands. 

And in some regions, we will offer – you guys know very well, we offer hedge and unhedged versions of equities, and then 50/50. Those are most also driven by client preferences, at least in aggregate. Those are more constant hedging. But we do have selectively hedge equity strategies. Also, selective hedge fixed-income strategies in some regions. 

I think those haven't been the most popular strategies or maybe not the default for people partially because it does require more education. More understanding, right? How dynamic hedging actually works? What really drives realized returns? And, also, you probably need to consider if there's any impact on tracking error relative to benchmark, which are typically unhedged. We're definitely happy to provide those strategies. But then I think in the end, it also depends on what clients are asking us for.

Ben Felix: I want to move on to premium timing, which you've done a bunch of really good work on. Can you talk about why timing exposure to premiums is so tempting?

Wei Dai: Well, there is a lot of economic incentive for doing so. It's also not our first time to look at premium timing. Basically, if you can figure out precisely when to go in and when to get out, that's phenomenal returns. Just before this, I took a quick look at just S&P 500 return, say, from 1926 to end of last year. Your $1 will grow to $15,000. That's pretty good. That's 10% annualized. 

But then let's assume you have perfect timing strategy. Say, not monthly, but let's say just calendar year. I know when the S&P 500 will be up and that's when I'm in the market. And then, otherwise, if the market is down, I go into T-bills. That $1, instead of growing to $15,000, will grow to 2 million. That's 16% annualized. That's a huge difference. There's a lot of incentive in between that difference, which is why I think that attempt to time the market or to time the premiums that we pursue will be never ending. That's a forecast I'm making here. But you'll always see some of that attempts. 

Cameron Passmore: What are some of the ways that investors do try to time the premiums? 

Wei Dai: There are lots of different things I see. One of the most popular ones is using valuation ratios. Because you probably often hear people talking about, "Oh, the US market is being so expensive based on aggregate valuation. Is it now time to get out?" Those type of statements you hear quite a lot. And, also, the same concept you can apply to any two sides of the premium. If you think about value versus growth, you can calculate, say, the price book ratio of growth stocks relative to that of value stocks. Basically, then the difference is called the valuation spread. You can, say, "Well, the spread is high, maybe that's the time we want to switch to value. When the spread is slow, it's time to switch back to growth." That's definitely one popular signal I see. 

The other ones, I think people inevitably also look at past performance a lot. There are definitely people who are betting on mean reversion. Essentially, if a premium has done really well, maybe then the premium will tank in the future. But then, equally, there's also people betting on momentum. If the premium has done really well, maybe then the momentum will continue. It's the time to continue to be in that premium or get into the premium. Definitely seek both sides of that that the spectrum. 

I would also say that we do get a lot of questions from our clients in different kind of shape and forms. But a lot of them are actually timing questions in disguise. People ask you about interest rate fed actions, inflation, business cycles. Ultimately, I feel everyone wants to know if there's anything we can say about the future direction of the premiums or the magnitude of the premiums. And then what that means for their asset allocation. Definitely, lots of different methodologies that we see. 

Ben Felix: What kind of parameters need to be defined to implement one of those timing strategies? 

Wei Dai: A lot of the concept I was just referring to can be quite straightforward. But, actually, translating them into an actual strategy will involve a lot of parameter choices to your point, Ben. Essentially, what you want to know is when to go in and when to get out. 

Let's use, say, valuation ratio as an example. People say, "Well, we should go in when it's cheap. Get out when it's expensive." But what is cheap? What is expensive? People say, "Well, then maybe you can look at the current valuation relative to the historical distribution." That's reasonable. But then how do you then construct a historical distribution? Do you look at the most recent 10 years or 20 years? Or do you look at all the data available to construct the historical distribution? Basically, an expanding window approach versus a rolling window approach. 

And once you have that historical distribution, you still need to ask what is the threshold for being cheap versus expensive? Do you look at the 10th percentile, or 20th percentile, or maybe the median? And, also, how often do you want to look at that signal and then to decide whether or not to rebalance? Is it monthly? Is it quarterly? Is it annual? 

You can probably already get the sense that, for every strategy, there's lots of parameters involved. And, also, the same strategy can be applied to different premiums, different regions. Which is why in our recent study on timing, we looked at 720. That's a combination of three signals. Valuation spread, mean reversion, momentum. And five different kind of thresholds for switching in and out. And two rebalancing frequency; annual versus monthly. And then also two historical distribution construction using rolling versus expanding. Four premiums; equity, size, value and profitability. And three regions; US, DevelopX US, emerging markets. Hopefully, that's all. If you multiply all of them, you should get 720. That's what we did in our analysis. 

Cameron Passmore: Pardon me. On behalf of all the listeners, which timing strategies worked in your research?

Wei Dai: Yes. That's actually typically what people are most interested in. Which ones work? And I'm happy to report that 30 out of those 720 works. By kind of work, I meant that delivered reliable output performance relative to just staying invested, staying consistent focus on the premiums. 

One of the best strategies we saw was a timing strategy that was used to time the – it's the market premium in DevelopX US market and based on the valuation ratio that we were just talking about. And that strategy was able to actually avoid major market downturns in 2001, 2008. 2012 as well. That led to an excess return on top of that average market return. Let's call it 10%. You get the excess return of 5.5 percentage points. That's quite impressive. 

But there are definitely a lot of caveats. What we also saw is that, yes, it's very easy to focus on the winner without asking how much of that is actually due to luck versus skill? I often like to use that coin-flipping analogy. If I ask you, Ben or Cameron, if I have, say, 10,000 people flipping coins, how many of them will flip 10 heads in a row? Any guesses? 

Ben Felix: I don't know. 

Cameron Passmore: Far more than I'd guess, I'm sure.

Wei Dai: Yeah. On expectation, there will be 10. Then, we'd then be calling them, say, coin-flipping masters and expect them to continue their performance? Probably not. In terms of the best strategy I was referring to, it does rely a lot on that exact combination parameters, annual frequency, rolling 10-year window, a 10th percental to switch out, 50% out to switch back in. 

And then we did some sensitivity analysis. We saw that if you just change one single parameter of that strategy, for example, change one of the percentiles you use or maybe change the rebalancing frequency to annual to monthly, that alone would already reduce that access return by more than half and also make that access return no longer reliable. 

And, also, the same strategy doesn't really work in other regions or doesn't really work if you apply to other premiums. I think just a good example showing that, yes, shining results can happen. At the same time, they can be quite tenuous, especially if they are due to random chance. 

Ben Felix: You can find a strategy that works, but it's super sensitive to like the region you tested it in, the parameters used to define it, and even the time period.

Wei Dai: Yeah. Absolutely.

Ben Felix: Very interesting.

Wei Dai: In our paper, we definitely have another example showing how the results can be very sensitive to time periods. I think it was related to timing the US size premium using momentum. Essentially, betting the performance to continue. And a lot of that access return is due to just two years. It was 1972 when size premium was down by a lot. '73, again, down by a lot, like negative 20%. Of course, the momentum strategy worked by avoiding that second negative year. But that alone contributed half of that excess return. And if you look at maybe the second half the sample periods without those years I was describing, then none of the strategies would work.

Ben Felix: I guess the idea then being that it wouldn't be reasonable to expect that type of event to happen again in the future with that exact strategy.

Wei Dai: Yeah. If your results are driven by, say, some outliers, very small part of the sample, then I think you do need to ask yourself how confident you are to kind of put your money into a strategy that has worked well in historical data, but actually very sensitive to just a few outliers. 

Ben Felix: And I guess there are other tradeoffs too, right? You'd introduce more turnover, probably more tracking error, all that kind of stuff.

Wei Dai: Actually, in our analysis, we didn't even consider tax considerations or trading cost. On top of that, it will be even less appealing to go with any of these timing strategies. 

Ben Felix: On valuation ratios, can you talk about why theoretically it makes sense they would be related to differences in expected returns? Why are they not useful in timing premiums? 

Wei Dai: That's a great question. I've been thinking about that myself as well. Generally speaking, I do think there is a distinction between identifying changes in expected stock returns over time and differences in expect returns across stocks at any point in time. 

Essentially, that time series aspect has always been a lot harder than the cross-sectional aspect possibly because there are a lot of changes from time to time. Whereas more things can be controlled for when you're looking at the same cross-section at each point in time. 

But when it comes to valuation ratio, there is a theoretical link. Price being the discounted future cash flows. But that also means that if you see a lower route valuation ratio, that can result from higher discount rate. Meaning higher expected return. But it can also be due to lower expected future cash flows. Or, usually, a combination of both. 

Empirically, I think at least in the time series, we see it's not really possible to cleanly isolate that cash flow versus discount rate effects from the data. That's on the equity side. But, actually, good to point out that, in contrast, on the fixed income side, the future cash flows are a lot more certain. If you're thinking about the promised coupons and PAR payment. You can actually say something about the variation of expected returns over time. The variation of the term premiums and credit premiums over time. And that's what we do in our strategies. But then it's more like on the equity side, I think because of the noise, you are better off behaving as if the expected premiums are constant. 

There is another broader point I want to maybe just quickly mention, is that there's also a distinction between a statistical relation that you see from the data versus a profitable strategy you're able to run. Because, oftentimes, you see regressions, scatter plots showing you some in-sample relation using all the data. But then when you run a strategy, you need real-time out-of-sample prediction that's based on only data available to you at that point. I think that's a much harder hurdle. 

Sometimes you see valuation ratios, people say things like CAPE ratio. Cyclically adjusted price-to-earnings ratio. They have been shown to be related to future returns, usually over the long-term, right? Over the next 5 years, 10 years, or 20 years. 

An interesting thing is that even if you assume there is some long-term return predictability, but then you use it for short-term asset allocation decisions. Oftentimes we see people deciding on allocation on annual basis. That misalignment in the horizons means that, oftentimes, you're still not better off. Basically, the precision that's required for you to have a successful timing strategy is nowhere near what we can observe from some of the popular valuation ratios. I found that pretty interesting from our analysis as well. 

Cameron Passmore: What are the main implications of this research for pursuing premiums? 

Wei Dai: In short, it's time to stop timing, if that makes sense. In the end, I think premiums, they are positive on average. Good to keep in mind that whenever you switch out of the market or switch out of these premiums, the odds are already stacked against you. 

In recent years or just over the longer history, we see that the premiums can also turn very quickly. You really need to be there to capture them whenever they show up. But then I also understand, we said that very earlier, it's very tempting to do so. Definitely, staying invested will require a lot of discipline. That's why we see a lot of value from financial advisors to help people stay disciplined. 

One thing I found useful to point out to people is that just keep in mind that as you are going through those ups and downs in terms of the volatility of the premiums, the volatility itself should actually give us some comfort for why the expected premiums are positive in the first place. If things just go up every day, you should be worried. And why are you even being compensated? 

To some extent, that willingness to bear that uncertainty and that potential underperformance is rewarded with higher expected returns. Stop timing. But think about other ways to put the odds in your favour. Think about integrating multiple premiums. Think about being broadly diversified. These are much more effective ways to put the odds in your favour.

Ben Felix: Just on the idea of timing, I tweeted, I don't know, a week ago about how the death of the value premium had been declared in 2021. And then I looked the value premium from then until April 2024 and it's like, especially in Canada, very, very positive. Staying in your seat is definitely important.

Wei Dai: Even equity premium back in the last decade, probably 2009, people say, "Oh, is the equity dead?" Things went different ways. I think there's definitely something to be said about not being carried away by some of the headlines and then stay disciplined through those ups and downs.

Ben Felix: Can you talk about how important diversification is to capturing the return premiums? 

Wei Dai: We're talking about what are the ways to actually increase your odds? At least improve your odd of capturing the premiums. I would say diversification is a very important consideration. People already know that diversification is very useful when it comes to reducing [inaudible 00:44:24] risks associate with single stock, or a country, and sector, and so on. But our analysis also shows that it can play very important role in increasing your reliability of capturing those premiums. 

The reason is that if you just imagine, let's say, a year you said value premium with strong in Canada, let's say we have a year with a positive value premiums. Let's say 4%. But if you look at all the different value stocks, it's not the case that all value stocks have out-performed growth benchmark by exactly 4%. A subset has done really well. They are the ones driving the positive premiums. Some probably have done average and some poorly. 

The issue is that you cannot really predict which stocks will end up driving that premium. And that subset will also change over time. That means if you have a more concentrated portfolio, meaning that you kind of just simply sample from the value universe, then you might miss out on the subset that actually drive the premiums. And in contrast, if you have more broadly diversified exposure, and then that will help you to capture the premium whenever they occur. 

In our analysis, more concretely – not sure if you have seen that. Basically, we say let's look at a fully diversified portfolio that's tilted to our size, value and profitability. And then we also look at a few sampled portfolios. Meaning that they maintain the same level of tilt to the premiums. Basically, you can think about their expected returns being similar. But then they have fewer stocks. Maybe 500 or even 50 on average. And then what we show is that the more diversified portfolio will actually give you lower deviation from the market. Lower tracking error for the same level of out-performance. And that leads to a higher probability of out-performance. Which is why you see that in our portfolios, we want to be as diversified as possible given the investment universe and then given our investment goals.

Ben Felix: I really like that paper. I thought the way that you set it up is really intuitive. But I will say that it's a paper that's been discussed at length in the Rational Reminder community. One of the nerdiest places – 

Wei Dai: Oh, really? Yeah. 

Ben Felix: At length. There's pages and pages and pages of discussion on it. And the main point of discussion is the fact that you did what you said, which is held expected returns for the different levels of concentration constant. Do you have thoughts on what that analysis would look like if you were increasing expected returns with concentration? Like a more diversified portfolio with a lower expected return versus more concentrated one, but with a higher expected return. Does that make concentration look better? 

Wei Dai: I see what you're saying. Yeah. I need to check out the debate. And I'm very curious. But it is a very interesting question. Because, ultimately, the results in terms of the probability of out-performance will be driven by two things. One is your expected outperformance and the other is the uncertainty around that outperformance. You can think about basically the distribution of your excess return, you have the mean of that distribution, you have the width of that distribution. 

To your point, yes. In our analysis, we control for the mean of the distribution. That's basically usually what we do when it comes to research to say let's isolate the effect of diversification so that you can show the impact more cleanly. 

I understand, oftentimes there are also portfolios with different level of tilts. Or maybe even for us, we have four portfolios with different level tilts. Or maybe even exclude certain parts, say exclude mega caps or poor versus a vector type of portfolio. So then they will come with different expected returns. 

Then there are two effects. You are moving the mean to the right. More positive. But you're probably also increasing the width of that excess return distribution because your tracking error will be bigger. I would say that if the strategies are well-designed, you can actually balance the tradeoff between those two effects to actually achieve very comparable results. That's typically what you see in terms of just the average asset return numbers we see for these portfolios versus the tracking error we see. 

But I would say there's still a limit to it. How much you want to concentrate? You can still say, "Oh, I can find 20 stocks." The smallest, deeper value, highly profitable. Yes, maybe on paper they will have the highest expected return, but it's still not a robust portfolio. And then trading cost will be super high if you have such a tiny opportunity set. I would say you can achieve comparable results, but you need to design thoughtfully.

Ben Felix: I think that's probably where that discussion in the Rational Reminder community ended up. There's a tradeoff between concentration and expected returns. And it's really hard to define where that optimal point is.

Wei Dai: Yeah.

Cameron Passmore: There's lots of fund managers pursuing factor premiums today. What do you think investors should look for when choosing systematic investment manager? 

Wei Dai: I definitely see there are more managers trying to do systematic active approach, and also more investors embracing this type of approach. I think it's good to see the world is moving in our direction. But as we have been talking a lot today, not all systematic strategies are created equal. And when it comes to assessing different systematic managers or strategies, oftentimes, people start with performance, which is understandable. But I think good to keep in mind that returns are noisy. So every manager will have maybe some strategies that have done well in certain period. You need to be able to differentiate luck versus skill, which is not an easy task. 

A few things I think can be helpful. One is when you look at track record, try to look at longer term track record over different market environments. And, also, look at not just one strategy. Even if you only are interested in one strategy, because it's a systematic approach, you need to look at the full set of strategies that's a reflection of the process and how you are able to capture the premiums. And also, importantly, not just look at the strategies that you can buy today that are still around today. You should also include those that are closed, or merged, or liquidated, because that gives you a much better sense of the performance that's not biased by survivorship. And also shows to some extent the commitment of the manager to a particular investment approach. 

And you can also look at conditional performance. By that, I mean, that maybe lookout periods when the premiums the managers are pursuing are positive. Even in the challenging period, like last decade with value on average on performing, we've seen periods of outperformance. So then you want to see what the managers are able to maintain their exposure and actually capture your fair share of the premiums when the premiums show up. 

And, ultimately, it will be great if people can actually look beyond just performance and really think about what drives a good systematic strategy. In my mind, it's really a combination of two things. One is do you have rigorous research that's underpinning your strategies? And then second is do you have that implementation expertise to translate those research insights into actual strategies? 

Now on the research side, I would say, especially these days with the rise of big data, a lot of computing power, it's getting even easier to find patterns in the historical data. We talked about it in timing. I feel there's actually not only you need the technical skills to be able to differentiate noise versus signal. You also need to have the right incentives for researchers and to have that discipline to not to make constant tweaks to your portfolios. 

On that side, I would say, especially with Dimensional, we have a culture that's very heavily influenced by our academic heritage. For me, it's quite scary. You have your work judged by such a crowd, including Noble laureates. But at the same time, I would say it's very tremendously helpful.

Lastly on implementation, I would say we already talk a lot about that in terms of portfolio design. Even if you know the same premiums, how you design the portfolio matters. And, also, how you do the daily implementation matters. The process, the infrastructure, and also how you think about technology versus human oversight. That matters a lot in today's environment as well. 

And for us, there has always been a very relentless focus on implementation, probably because our very first strategy is a micro-cap strategy, right? It has been part of our DNA. If we are not careful, if we're not practical, then we would have been killed in the market. We wouldn't have a business. That focus on research and implementation has really served us well until today. 

Ben Felix: Continuing on manager selection for systematic strategies, can you talk about the downsides of performance fees, specifically for systematic managers? 

Wei Dai: That's actually a research paper we did with Professor Bob Merton, who is a resident scientist at Dimensional. That's a few years ago. Maybe just give you a little bit background why we're even looking at that. Because, traditionally, if you think about long-only investments, the typical fee structure is just a fee expense ratio or fee as a percentage of your assets under management. 

Performance fee is more for alternative investments. Like hedge fund, you do here 2 and 20, so that 20% being charged on out-performance against some threshold. That said, we started to see performance fee structure kind of trickle into the traditional long-only space within separate manager accounts, which is why we decided to do a deeper dive and just to understand the incentives induced by performance fees. And whether it's suitable, especially for systematic strategies like the ones we are running. 

And the reason I mentioned Bob was involved, the reason that Uncle Bob was involved, because actually the performance fee from the manager's perspective, the payoff off very much looks very much like a co-option. If you have out-performance above certain threshold, the manager gets paid a portion of per profit. But then the managers don't usually share the downside. There's the floor. It's like constant and going up. It's a call option. That's why you can also price the value of performance fees using standard option pricing models. 

And if you remember the option pricing models, the pricing of the option doesn't really rely on the expected return of the underlying. But it relies on the volatility and other inputs. By analogy, the valuation of the management fee from the manager's perspective, it doesn't rely on the strategies expected return or alpha. It actually relies on the volatility or tracking error. 

If you're thinking about absolute return, it's volatility. If it's excess return, it's tracking error. Then you can see there is some incentive to increase your deviation from the benchmark in order to make the payoff more valuable. But as we have talked about earlier, in many examples, not all deviation from the market is justified by higher expected return. If you sample the universe, I can give you higher tracking error. But you might actually get worse outcomes. 

And then in the end, we kind of discussed that incentive structure in different type of strategies. I would say that I can see in some cases the performance fee structure could make sense or even preferred by manager. If you are a traditional active stock picker, your strategy is already high volatility or high tracking error, then maybe you like it. 

And, also, if you have some capacity constraint. You cannot increase revenue through growing your AOM. Then maybe getting that through the performance fee will be better route to do it. But then for systematic managers, we've talked a lot about striking that right balance between expected return, risk control, and cost, and diversification. I don't think that the incentive to increase tracking error probably, if anything, will be detrimental. It will probably lead to less robust portfolios. 

And then we also talked about earlier how the premiums can be very volatile. That means that if the manager is not getting paid when the premiums are negative, you're to some extent penalized for staying focused on the premiums. But we all know, it's important to stay focused in order to be there when the premiums turn around. I feel, in that sense, having that fixed fee is probably more appropriate just to recognize the effort that's required to stay consistently focused on the premiums.

Ben Felix: What was it like writing a paper with Bob Merton? Is that pretty cool? 

Wei Dai: Yeah, it is pretty cool. I actually feel quite fortunate that not only with that paper. I get to do a lot of research update calls with him. Of course, you benefit a lot from his insights and his guidance. But at the same time, I'm just very impressed by how excited he is about another paper. Because he probably doesn't need yet another paper to show how good he is. But he's still very excited. And when it gets published at the journal, he's very happy. He sent us those emails. And, also, he was very careful even sending us some edits on wording in the footnote. I feel all of that is very inspiring for me. I feel if I can continue to have that passion, I'll be pretty happy. 

Ben Felix: We had Bob on in episode 234. He was very enthusiastic about the nerdiest topics. 

Wei Dai: I'm sure.

Cameron Passmore: And such gracious. He was a great guest.

Wei Dai: Did it last like five hours? 

Ben Felix: It was like two and a half hours. It's one of our longest episodes.

Cameron Passmore: And he kept apologizing.

Wei Dai: I'm not surprised. 

Cameron Passmore: Apologizing for taking so much time. We said, "You're Bob Merton."

Ben Felix: Yeah. Talk as long as you want, Bob.

Wei Dai: Yeah. His generosity is quite impressive too.

Ben Felix: Yeah, really is. Really is incredible. I want to come back to something we talked about briefly earlier, which is short-run reversals. Can you talk about how short-run reversals are different from momentum? 

Wei Dai: I kind of said very earlier what is short-run reversal. As a recap, it's basically the tendency for recent winners to underperform recent losers over very short horizon. We're talking about ranking performance over the last couple weeks up to a month. And then you see the reversal kind of over the next few weeks as well. 

Now momentum is to some extent the opposite the tendency for continuation. The winners over the last 6 to 12 months. Typically, that's the horizon. Longer Horizon. To continue to outperform losers. They're related in a way that, typically, when people construct momentum signals, you would skip the most recent month for individual stocks. Reversals is the reason for skipping the most recent month. Because the most recent periods, that's more reversals.

Ben Felix: How are reversals related to liquidity? 

Wei Dai: That's a paper that has done kind of looking at the reversals and the liquidity in the time series. And we looked at in the cross-section. But more broadly speaking, if you think about the returns to a reversal strategy, that's basically approximates the compensation to liquidity providers. It could be designated market makers or any market participants that provide liquidity basically for the service they offer. 

You can imagine, let's say if an investor wants to quickly sell a large amount of a particular stock, that demand for immediate liquidity will have some downward pressure on the stock. They will generally be forced to sell at a discount. Because then the price will later revert back to a higher level once the liquidity demand is alleviated. 

And then that reversal then is basically compensation for market makers for providing that liquidity. Because when they provide the liquidity, they are exposed to the risk of the price falling even further before they can actually offload their inventory. And you can also imagine the opposite happening when investors want to quickly buy a large amount of stock. 

And we say that the understanding of this link to liquidity provision is actually quite important. Because one of the contributions of our study is to actually construct a cleaner signal to isolate the liquidity-driven reversals. Because you know, price change for many reasons, right? Could it be due to liquidity? Could be due to information? And if it's due to information, it shouldn't be causing reversal. 

That's why if you look at the literature, if you just rank on stocks raw returns over the last month, it's polluted by some of the news-driven effects. That's why in earlier papers, some of the effects, reversal effect is not very strong. What we did was actually to adjust the past performance for two news-related effects. Post-earnings announcement drift and also short-round industry momentum. 

What that means is that, basically, we don't just look at the raw returns of the stocks. We basically look at their returns relative to their industry returns. And we also take out the returns during the earnings announcement window. And by using that signal, you get much stronger reversal effects globally. Not just in the US, but also outside the US, including emerging markets.

Ben Felix: Yeah, it's a really cool idea. This one's published in the Financial Analysts Journal, right? 

Wei Dai: Yeah, earlier this year, it got published. We're very happy about that. Hopefully, more people get to see that and give us some feedback and comments.

Ben Felix: Yeah. Very cool. How do reversals vary across different types of stocks? 

Wei Dai: Oh, yeah. That's definitely the focus for our analysis. Essentially, you think about how it's related to liquidity. Then you can imagine the less liquid the stock, then the higher the compensation for providing liquidity for it. As a result, reversal should be stronger among stocks that are less liquid. 

But the problem is liquidity is a very nebulous concept. It's very complex. Very multi-dimensional. There's a huge literature on that. Basically, there's not necessarily a single variable that is a comprehensive measure of liquidity, which is why we kind of looked at a few different aspects. We looked at the market capitalization of stocks. We looked at volatility and turnover. 

The reason that they are related is that, intuitively, the smaller cap stocks and more volatile stocks, they're probably riskier to hold in the market maker’s inventory. Reversals should then be stronger among those stocks. And then similarly, if you think about turnover, if a stock trade less often, then that means it probably will stay in the inventory for longer. We see some evidence of that from other papers. 

That means the reversals should also persist longer, because it takes longer for alleviating that demand. Then what we confirm is that that's indeed the case empirically. We find that, in particular, the effects on volatility and turnover quite drama. Basically, you see that for stocks are very volatile. The reversals happen very fast and initially very strong. And then for stocks that have lower turnover, the reversal effects tend to be a lot more persistent. Ultimately, the cumulative effect can be pretty strong as well. 

Which also means – and you related to my comment earlier about how you measure reversal signal, if you just use the standard one-month horizon, that's typically in earlier literature, that's simply too long for some of those stocks. For high turnover, high volatility stocks, the reversal effect has already dissipated before you kind of see it. That's why it's more sensible to use a shorter look-back period, which is why, in our implementation, we will use the cleaner signal I was just describing. But, also, kind of over a shorter look-back period. 

Ben Felix: Can you talk more about how Dimensional will use this in implementing portfolios? 

Wei Dai: We actually just started implementing this year in all of our global equity strategies. Very exciting for. The general idea though is just to say, "Well, if it's related to liquidity demand, the compensation for providing liquidity, what you want to do as an investor is to reduce the cost of demanding liquidity and then to increase the compensation for providing liquidity. But then how you implement matters. 

If you think about a standalone reversals. Let's say you just chase the most recent losers and then sell the most recent winners, that's not practical. The turnover will be extremely high. And then the cost will be probably eating into any premium you can get. Even if you just look at monthly rebalancing frequency with monthly signal, you're already looking at a thousand percent one-way turnover. That's not practical. 

Which is why in our approach, we will use reversals basically as a reason not to trade instead of as a reason to trade. We can delay buying the recent winners. And then we can delay selling the recent losers until the reversal effect dissipates. That's what we call reversal screen. It's very similar to how we incorporate momentum. We call it momentum screen. 

Basically, you can then use the screen on your buy and sells. And that way, you can increase the expect return of your strategy but really without impacting the strategy's long-term focus on size, value and profitability. And, also, that out-performance will come without additional turnover and cost. 

We actually, in addition to the FHA , did a shorter blog just to estimate the value adds. We looked at new data from 2000 on. Basically, the period post-decimalization. A little bit more representative of today's market microstructure. We see that across different strategies, across different regions, or core versus component, the value adds is somewhere between one to 10 basis points. We think that's quite meaningful if you can get that without additional turnover. Because in the end, if you think about these type of systematic strategies, you're fighting for every basis point. We'll keep fighting. Whenever there's something that really clears that hurdle frost that we're able to implement, that's always very exciting for us.

Ben Felix: Can you talk about how just the process at Dimensional there's an idea for something like this, how does it go from that, to research, to publication, to implementation? 

Wei Dai: Every single project, I think the process will be a little bit different. But by and large, you start by getting your hands dirty with data. With the reversals analysis, we looked into the US data first and then we decided to look into DevelopX US and emerging markets. And then we started with monthly data. And then we really wanted to look at shorter signal. Looking into daily data, which is definitely non-trivial. 

And because Robert Novy-Marx, that that's a joint work with him, he has been very interested in this topic. And he has done some work on his side as well. It was natural for us to collaborate with him. It was very close collaboration. We were kind talking every single week and then to compare results and think about next steps. That's more the research part. 

Then once we get comfortable with the result, think, "Oh, there is something actually interesting and maybe potential useful for implementation." Then there's the process of bringing that to the investment research committee. That's basically the committee setting, the big picture. Basically, you also need to approve what the changes we need to add to our investment process or enhancements we put into our strategies. 

And that investment research committee, I was talking about how scary it is to get judged by such a crowd. There are top financial economist academics on that committee. People like Ken French & Farm, Robert Merton. But, also, our seasoned investment folks. Not just research, but also profile managers and training. Because then they have much holistic view of what that may mean for our investment process. And then there will be some back and forth. 

And then when it comes to the implementation, it will be truly cross-department work to kind of move that into something that's operationalized. And then once it's in the system, the portfolio managers will actually not turn it on immediately but actually monitor and see what kind of orders we'll get. What kind of changes will happen? And just to make sure everything in good shape before it gets live in our portfolios. I hope that makes sense. 

Ben Felix: Oh, it makes a ton of sense. And it sounds like just an incredible in process to work on something like that with Professor Novy-Marx and have the people at Dimensional and on the committee reviewing it. That's crazy.

Wei Dai: I will remind everyone that not everything will go into like an enhancement in our portfolio or even into a paper. But that's part of our understanding to begin with. When you look at data, look at research, a lot of things will be – even if it's some negative results, will be additive to our understanding of investment. Basically, giving us good reasons for why we don't do this. Why we don't change. And so on. I feel all of that research is useful. And that's how our researchers are incentivized just to kind of get a better sense of asset pricing and then how things work.

Ben Felix: Yeah. It's just incredible. To think about – I do have one more question on this. This is published in the Financial Analysts Journal. People can read the paper. How important is Dimensional's ability to – because this is public. Anybody can read the paper and try and implement it. How important is Dimensional's ability to execute on something like that? What makes Dimensional different from someone else who could read the paper and try and implement it in their own portfolio? 

Wei Dai: I've actually got similar questions at one of the panels recently, asking with AI and ChatGPT, does it mean that people can easily replicate your factors or factor models? You would not need Dimensional to do this. Kind of similar to the spirit of your question. I think in the end, what I said actually at the panel is that you can already use those factor models for free. French's website, you can find those models. But at the end of the day, just the factors themselves are not investment solutions. Just knowing the signals by themselves are not investment solutions. 

There's still a lot of expertise to interpret the data and then also think about how you want to implement into your strategies. It also depends on what your investment process and what your investment approach is in the first place. The reason we can incorporate some of these shorter-term signals very effectively is, one, because we run a systematic strategy, right? We're not in love with a particular stock. That means we can actually be more indifferent across stocks with similar characteristics. That helps us to use that short-term signal more effectively without impacting the long-term focus. 

The other thing is we have already built up that daily investment process. It uses a lot of technology infrastructure. But then there's also the human oversight on top. That means you know, every day, we can do the evaluation. If these stocks are not great today, we can look at them tomorrow. If feel kind of setting up the whole process, it's not something you can do overnight. 

In the end, there's a lot of devil in the details. We feel very comfortable to share these results partially because we feel there's a lot of value adds in how we implement these results. And then we share these papers for people to have a better understanding of what we do in our investment process. Because I feel the more you understand what we do, the more likely that you can actually buy into the idea and become a long-term investor. Because that's what's also required to actually reap that higher expected return over the long term.

Ben Felix: I will say that you guys have gotten much better. I don't know if better is the right word. But you've been publishing much more research like this and research is getting published. I, for one, love it. 

Wei Dai: I'm glad. Yeah. Sometimes I send a lot of papers to our clients and say, "Okay, here are the weekend reading. Enjoy." For a lot of these papers, we also write shorter-term blogs. If you just want to get an executive summary of things, there's something in that format as well. Hopefully, that way we can explain better what we're doing in our portfolios. Because those investment processes are getting more complex over time as we refine and we constantly enhance. Hopefully, those papers are useful for increasing that understanding. 

Cameron Passmore: Our final question for you, Wei, for what has been an incredible conversation. I'm grateful. But here's our final question. How do you define success in your life? 

Wei Dai: I have to say, I'm even humbled to be even asked that question, because sometimes – especially with two young kids and then busy work, sometimes I feel just surviving the day is already a huge success. Believe me. But I do think that the definition of success has evolved overtime. It used to be a lot more binary, right? Do I get a good school? Do I get my job offer? And so on. But now it's much more about the process than the outcome. 

What I hope I can do is similar to what I was talking about Bob Merton being so passionate about research. I hope I can maintain that curiosity about the world. Whether it's a new data set I get to work on, a new paper, a new client request, or maybe a new challenge my kids are facing. Just still having that passion and really to put in my best efforts to embrace all of them without even thinking about the outcome. If I can do that, I will be very happy.

Ben Felix: That's an incredible answer to the question. 

Wei Dai: Thank you. It's been a pleasure. It's a fun conversation. I don't know how long it took. 

Cameron Passmore: Wei, that was great. Thank you so much for joining us. We learned – I learned a ton. Great, great conversation. Thank you.

Wei Dai: Yeah. Thank you.

Is there an error in the transcript? Let us know! Email us at info@rationalreminder.ca. Be sure to add the episode number for reference.