## Episode 362

Ben Felix: This is the Rational Reminder Podcast, a weekly reality check on sensible investing and financial decision making from two Canadians. We're hosted by me, Benjamin Felix, Chief Investment Officer at PWL Capital and Dan Bortolotti, Portfolio Manager at PWL Capital. Welcome to episode 362, our seventh AMA episode.

We got some good questions today. Keen listeners will have noticed that the episode order was a little different from usual. We had back to back guests followed by an AMA.

Typically, we would have had a guest, an AMA and then another guest. You may be able to hear it in my voice, but I had a wicked cold last week when we were supposed to record this episode, so we brought forward the Alex Edmonds episode and we're doing this one this week.

Dan Bortolotti: All right, we got some good questions in the AMA today. I think we do. I do have an oncology update. I'll give that at the end though.

We got some good reviews as well on the after show. Yeah, let's jump into the AMA questions. For the first one from King Richard III, okay.

Dan Bortolotti: Not the original King Richard III, I'm assuming.

Ben Felix: Yeah. The question is, withdrawal rate and its corresponding estimated years of retirement, i.e. early and late retirees with a 100% equity position in VEQT. That's an interesting question.

The original safe withdrawal rate analysis from Bill Bengen, who we have had on this podcast talking about that research, looked at a 30-year horizon and it focused on US stocks and bonds only. That's what led to the famous 4% spending rule that people like to talk about. Looking at global stocks and increasing the time horizon does affect that 4% number.

Fortunate for King Richard III, I have a model set up to basically answer this question. It looks at global stock data, so not quite VEQT, which has a Canadian home bias. This just looks at global market cap data from 1900 through 2023 and I can easily manipulate the time horizon in that model to see how it affects the safe withdrawal rate.

At the 30-year horizon, I get a safe withdrawal rate of 3.5% with a 5% failure rate, which is typically how that type of analysis is done.

Dan Bortolotti: We should probably clarify here that Bill Bengen 4% spending rule was based on a balanced portfolio. I think it was 50-50 stocks and bonds. The questioner here is asking about what it would be if you had 100% equities.

Would you not expect the safe spending rate to be higher than 4%, not lower? With equities? Yeah.

Obviously, you have much more volatility, but you also have much higher expected returns. You would presumably, if you took additional risk, be able to withdraw larger amounts over time, but that doesn't sound like what you're initially seeing here.

Ben Felix: One important point there is that I'm using global stock data and Bill Bengen was using US stock data. It makes that much of a difference. It makes a big difference.

If I included US bonds in this specific projection, like the 30-year horizon, I could probably get a little bit more out of this, but that's US bonds specifically. If you look at the Scott Cederberg research, adding bonds from a broader sample would make things look worse universally. It really does depend on the data inputs that you're using.

It is a good point. I do think that the volatility can matter a bit with the safe withdrawal rate because you're withdrawing a fixed amount each period. If you have big, big drawdowns and you keep withdrawing the same amount, that can be really bad.

We've talked about this when we covered the concept of variable withdrawals. I think one of the terms that we used was we shouldn't be calling this sequence of returns risk. We should be calling it sequence of withdrawals risk because if you withdraw the same amount when markets are really bad, that's really what hurts you more so than the bad return.

It's withdrawing the same amount when returns are bad. I do have some comments on variable withdrawals in a sec. As that baseline, I get 3.5%. I don't think that's a new finding or an exciting or controversial number. Other researchers have found the same thing. If you go global, it drops to around 3.5%. If I hold that safe withdrawal rate constant, I get an 8% failure rate at a 35-year horizon, a 14% failure rate at a 40-year horizon, and a 16% failure rate at a 45-year horizon, 21% at a 50-year horizon. You can see holding the spending rate constant, the failure rate as you'd expect is increasing at longer horizons.

I did look past that past 50 years. The failure rate does continue to increase, but it increases at a slower rate. Be interesting to put that on a chart.

I did not do that, but I think it'd probably be an interesting looking chart. If I flip the perspective to safe withdrawal rates holding the failure rate constant, so I hold the failure rate at approximately 5%. The safe withdrawal rates I get 3.2% for a 35-year horizon, 3% at a 40-year horizon, 2.9% at a 45-year horizon, and a little over 2.8% at a 50-year horizon. You can see why when people are talking about the 4% rule for an early retirement, 4% is probably too high if you extend the sample past just US data, but it's probably way too high if you're looking at a much longer time horizon, which an early retiree would be.

Dan Bortolotti: Most people would be surprised by how low that number is. I'm a bit surprised, to be honest. These are inflation adjusted withdrawals, we should say.

It doesn't mean you'd withdraw the exact same dollar amount. Of course, you withdraw the same amount in real dollars over decades, but still, that is not a big number, somewhere in the neighborhood of 3%.

Ben Felix: It's based on the starting portfolio. If you have a million dollars and you're withdrawing 2.8%, that's $28,000. The way that this concept works, the way the safe withdrawal rate works is that you're withdrawing that initial amount, $28,000, adjusted for inflation or deflation every year thereafter.

It's a constant inflation adjusted withdrawal where the dollar amount is based on the starting portfolio value.

Dan Bortolotti: When you consider that, if you were able to save a million dollars, you could reliably withdraw, let's call it somewhere between $28,000 and $35,000 in real dollars indefinitely.

Ben Felix: One of the challenges I think with the safe withdrawal rate is that it is based on the worst historical outcome. It's challenging for a couple of reasons. One, because the worst historical outcome is not necessarily the worst future outcome, so this could be risky.

Then on the other side of it, and historically this has been more of the problem, is that the worst outcome doesn't happen very often by definition. We'll see when we talk about variable withdrawals in a second, the average amount you can spend is a lot higher. You just don't know if you're going to get the worst outcome or not.

Under this safe withdrawal rate idea, you're withdrawing a very conservative amount because you're planning for that worst case scenario. I think there are other ways to approach that. I did try going the other direction.

I looked at a 20-year horizon. If you're retiring very late or have a short life expectancy for some reason, I did get a little over a 4.4% withdrawal rate with a 5% failure level. Scott Zederberg's paper does mention the failure rate under 4% withdrawals for their optimal 100% equity portfolio, which is the one-third domestic, two-thirds international.

The failure rate there was 7%. Now their time horizon is different. I'm using these fixed time horizons to look at how it affects the withdrawal rates, but their data setup is based on a couple retiring at age 65 and then being subject to the distribution of mortality for US residents.

They're modeling a whole bunch of different life expectancies, but looking at their numbers, on average, they'd be living less than 30 years, but it's a similar range of numbers, I think. That safe withdrawal rate model that I have is also set up to look at amortization-based withdrawals. I think that's quite interesting to see how they change relative to safe withdrawal rates with an increasing time horizon.

If people want to learn more about amortization-based withdrawals, they should listen to episode 340 with Ben Matthew, where we went very deep into this actually, into safe withdrawal rates versus amortization-based withdrawals. In short, it's a variable spending policy that's designed to deplete the asset at the end of the target horizon, but not before. It does that by adjusting each year to changes in the starting portfolio value of that year and expected returns.

My version of this model holds expected returns constant. At the 30-year horizon, amortization-based spending is, on average, 7.6% of the starting portfolio value. That's on average for all of the 30-year periods that I looked at from 1900 to 2023.

The worst 30-year period has average spending of 3.6% of the starting portfolio value. The worst single year is 1.5% of the starting portfolio value. Again, back to the million dollar example, there was a year in there where you had to spend $15,000 to follow this rule.

That's rough. On average, you spent a lot more. The fifth percentile single year spend is 3%.

Dan Bortolotti: More than double the average at 7.6%. That's a lot more than the 2.8 to 3.5 we were talking about before. If you want certainty and consistency, you have to be very conservative. If you're willing to be a little bit more inconsistent with those annual withdrawals and recalibrate every year, chances are you're going to be able to spend a lot more.

Ben Felix: Yeah, exactly. I did look at a 40-year horizon too and that drops average spending to 7.4%. 7.6% at 30 years, 7.4% at 40 years on average. The worst 30-year period was just under 3.1% at 40 years compared to 3.6% at 30 years. Then the worst single year was 1.4%. The fifth percentile year was 2.6% of the starting portfolio value as a spend. It is important to emphasize that under amortization based withdrawals, the spending amount is changing from year to year, whereas with safe withdrawal rates like you just mentioned, Dan, is constant.

Dan Bortolotti: Yeah. The challenge, of course, as a retiree who's actually spending that money, nobody wants to be on a extremely variable annual budget where they have to dramatically adjust their withdrawals based on last year's investment returns.

Ben Felix: Totally. Yeah, even in that fifth percentile, say you have a bad year, the worst 30-year period has average spending at 3.6%. In the worst year, you're spending on average a bit more than the safe withdrawal rate spending, but there is a year within that 30 years where you have to drop spending down to $15,000. That's a big cut.

Dan Bortolotti: If it was only one year out of 30, you'd probably be able to adjust, but you just never know when that year is going to come.

Ben Felix: Exactly.

Dan Bortolotti: If that's the year where you booked your big trip and you have to cancel it because it doesn't meet your scheduled withdrawals. I mean, that's a specific case. I think we've talked about it before.

Most people naturally resist the idea of these variable spending plans.

Ben Felix: Yeah, I think any spending rule is tough. Pretty sure I talked about this on the Morningstar podcast because they asked about spending rules and withdrawal rates. I don't think that a rule works for an actual person.

It's really fun to analyze. This is cool data to talk about and it's neat to see how flexibility affects spending and what the trade-offs are for you or I to sit down with the client and say, no, you can't do that this year because the rule says so. It's just not going to happen. It doesn't make sense.

Dan Bortolotti: You might be able to do it next year, but you can't do it this year. Nobody wants to have a retirement plan like that.

Ben Felix: I think it's got to be a lot more human than a rule, but I do think that the rules help you think through what the trade-offs are. All right, next one.

Dan Bortolotti: All right, this one is Ricardo from Italy who asks, don't you think that the most difficult part about investing is to forget that you're invested? Once you set your goals, asset allocation and monthly savings, then starts the hard part, the so-called boring middle. How can you forget you're in the market if we receive daily news from everywhere about everything?

I think this is actually a pretty insightful question. Take it away and I'll chime in with some first person experience here as well.

Ben Felix: I did have an interesting conversation recently that is relevant to this question. One of our portfolio managers came to me with this observation that he had these client cases where the client had either wanted to get out of the market or make a portfolio more conservative due to some external event. This is all recent politics and stuff like that.

The general things that have been happening in the world, he'd had several interactions with clients that had come and said, hey, I want to get out of the market or I want to make my portfolio more conservative. In all of the cases, he talked through what they were feeling and related it back to their financial plan. In all cases, the client left feeling much better and they stuck with their initial asset allocation, didn't make any changes.

Then this portfolio manager was thinking about those interactions as he was doing other financial planning work for those clients. He went and modeled what their financial plans would have looked like if they had moved to a more conservative portfolio. Then he compared the expected impact of that to the impact of other financial planning strategies that he was looking at implementing for them.

His observation, and this is why he sent me a message about this because he thought it was so interesting, is that it was really hard to find a financial planning strategy. Think of things like optimal withdrawal sequence from retirement accounts, for example, that had anywhere near the expected impact of a 10 percentage point increase in the portfolio stock allocation or in this case, in not decreasing the stock allocation in the portfolio. One exception to that would be the savings rate, which is a necessary precondition for asset allocation to matter.

They made another interesting point as they were just thinking through this, which is that he suspects that the risk tolerance – this is Jordan, tear us off for what it's worth. He's been on this podcast in the past. He suspects that the risk tolerance of an investor in isolation is likely quite a bit different from the risk tolerance of an investor with an advisor.

All that to say, I agree with the premise of the question that setting up a plan and doing smart financial planning and picking an asset allocation, those are all great, important, smart things to do. I think it can be argued that their effects on the long-term outcome of a given plan or a given financial situation sit in the shadow of taking the right amount of risk and maintaining that level of risk through good times and bad. There is a highly cited paper in the Journal of Finance that's on this topic.

It's called Money Doctors. The paper acknowledges that the net of fee underperformance of professional money managers is a problem. That's there.

We know that professional money managers underperform, but they look to answer the question of why people still pay for financial advice. If you look at us, we're an interesting example where we're a little different because we use dimensional. You're an even better example, Dan.

You're using index funds. Your clients are going to get the return of the index less the fees that they paid you. They must be deriving value from that fee because it's not to beat the market because they think that's explicitly not going to happen.

You're right about that. In this paper, they say, we propose an alternative view of money management that is based on the idea that investors do not know much about finance, are too nervous or anxious to make risky investments on their own and hence hire money managers and advisors to help them invest. That's basically it.

To the listener's question, I think financial advice can be one way to solve the problem of taking the right amount of risk and staying in your seat despite all the crazy stuff that's happening around you. Another solution could be automating as much as possible when Morningstar analyzes the effects of cash flow timing on investor returns. Asset allocation funds like VEQT and other single products that contain a diversified rebalanced portfolio, they have the lowest return gaps between product returns and investor returns.

That seems to me to imply that investors in those types of products, as opposed to managing their own portfolio, rebalancing across individual asset classes may have an easier time behaviorally.

Dan Bortolotti: People who are naturally sensitive to volatility will probably tolerate a more risky portfolio if they're working with an advisor than if they work with them on their own. If you feel like you're going to be watching the markets on a daily basis and be very bothered by the volatility, sometimes working with an advisor allows you to take a little more of a hands-off approach. You're delegating that to somebody else.

I certainly have many clients who I've spoken to who went from being DIY to working with us and now have told me, I just don't look at it nearly as much as I used to. I think we all know the less you look and the less you touch, the bigger your portfolio is going to grow. That's part of it.

You had said to stay in your seat. This idea that you would probably be more likely to change your asset allocation, I think, if you weren't working with someone who enforced the consistency. One of the things I hear all the time, and it isn't just from nervous investors, it's just people who want to get tactical.

Sometimes it's like we should increase our equity allocation after the markets go down. If you're going to do that, you might as well do it in that direction versus panic selling. Anytime you get into the business of trying to tactically change your asset allocation, I think you're asking for long-term erosion of returns.

This idea that if an advisor can help you build a portfolio that is still appropriate for you, but kind of as risky as you can comfortably tolerate and keep you there, those two things are going to make a big difference. Getting back to his question though, I think the listener was sort of asking, well, okay, but that's very boring. Once you found an asset allocation that you're comfortable with and you're sticking to it, I don't know what to say about that, but I do think you're right that the financial planning strategies, even if they don't have as dramatic of an effect as a change in asset allocation, still do have some value in that they keep you focused on the right things.

They keep you focused on the saving, the tax efficiency, the discipline, and all these sorts of things that an advisor can help you enforce. None of those have anything to do with investment returns, but they do have long-term value.

Ben Felix: That's a really interesting point.

Dan Bortolotti: The boring middle is good. Boring is the place to be in investing. If your investment portfolio is exciting, you're probably doing something wrong.

Embrace the boredom and if you're restless and you need to do something, do it on the margins. Don't do it inside the portfolio. Try to focus on other areas of your financial life that you can do less damage.

Ben Felix: I really like that point of letting financial planning be the interesting part. Let the investing be boring.

Dan Bortolotti: For so many of the clients that I've been working with for many years, in our review meetings, we don't spend very much time talking about the markets or the portfolio. I mean, we do the usual. We review the portfolio.

We review the returns. Nobody's surprised because that's one of the benefits of using an indexing strategy. Everybody knows what the performance is going to be if they've been following the markets.

Then we get on to what really matters in their life. That's the things that's much more interesting.

Ben Felix: That's true. Solving little problems about how to best accomplish whatever this thing that they want to do that year. I cut my quote short from that paper and it actually echoes one of the things that you said.

The paper says, net of fees, investors consistently underperform the market, but experience less anxiety and earn higher expected returns than they would have by investing on their own.

Dan Bortolotti: Nails it. That's exactly it.

Ben Felix: It is a good question though. I agree. That is an insightful one.

You can feel like there comes a point where everything's set up and everything's done and then what's next? All right. We've got another question here from Italy.

I didn't realize we were so important of a listen in Italy. This is a great one. I'll read this one.

What if 2025 will start with the worst crash of all time? How do you think people will react? I don't know when this was sent in.

I didn't check the date, but it was clearly before 2025. It's fun having these questions that were sent in a long time ago. It's like this time capsule into what people were worried about back then.

Then we get to discuss now with the benefit of hindsight, knowing exactly what happened. 2025 did start with quite a crash for US stocks. Nothing historically unprecedented, but lots of volatility.

I looked at the numbers from January 30th through April 8th, 2025, XUU, which is the iShares core S&P US total market index ETF, dropped by 19.7%. That is measured in Canadian dollars to be clear. It's a Canadian listed ETF. Now some people were very concerned.

You and I then co-authored an email that we sent out to all of PWL's clients because everyone was very concerned at the time and worried about what was going to happen and what all the volatility meant. Some people were not worried, but in any case, here we are now with US stocks down 2.54% as of June 6th when I last checked, again in Canadian dollars. VEQT, the Vanguard All-Equity Portfolio is up 3.6% over the same period. I'll throw in a shout out to DFA607, which is up 4.31% year to date. That's the DFA global equity portfolio. Not catastrophic by any means.

I think we tried to kind of nudge toward this in the email that we wrote to clients then. It would be incredible if we could approach all future crashes this way, only observing them in hindsight, knowing that things will work out. I think the fact that we can't do that is exactly why they're hard for people to deal with.

It's super easy to look at the numbers now, 19.7%. That's not so bad. Not feel like what it felt to live through that period when you're battered with tariff related headlines and predictions about their effects and how everything's going to collapse. I remember how it felt then.

It's really hard to put myself back into that mindset that I had when things were really uncertain. It's easy to look back now and say, well, that wasn't so bad when you look at the numbers, but that really doesn't go through actually going through it justice.

Dan Bortolotti: We touched on it in the client letter too. It's not just what has happened in the last few days or weeks. It's the narrative that we're hearing and that we're telling ourselves about how much worse this could get.

Nobody who experiences a 10% decline is all that upset over the 10% decline. They're upset because they think that 10% might become 40%. It's very easy to come up with scary, worst case scenarios when you're in the middle of an event, whether it's COVID or the trade war.

Both of those were very scary when you were in the middle of it. Then looking back, it turned out not to be that big of a deal. COVID is even a more dramatic example than this recent one because at the depths of it, we were down, what, 30% in a couple of weeks.

It was very, very deep and very fast. Then it recovered just as quickly, but you didn't know that. Not only was the market down, everybody was worried about their own health.

To just look back at that now and dismiss it as saying, oh, it wasn't a big deal or sure we knew the markets were recovered. I think that's being a bit disingenuous.

Ben Felix: I remember going through COVID. 30% doesn't do that justice when it felt like going through it. It felt worse than that, didn't it?

Yeah, that was a rough one. I think this crash in 2025 was fundamentally like any other crash. Market crashes happen because of uncertainty and fear.

Exactly what you're just saying now because people don't know how much worse things will get, which makes it really scary to go through it. They don't know when it's going to turn around. Now people are going to respond to those events in different ways and I think they should plan accordingly and that planning can be done through some combination of appropriate asset allocation, automation, maybe just not looking at it.

If needed, professional financial advice. There are a couple unpublished papers, one from Steve Utkus from Vanguard, where they looked at the effects of good quality advisors and they had a way to measure that when markets were rough and they found clients of the good advisors were much less likely to leave the robo-advisor service after bad markets, which is an interesting data point. Then there's another one, I'm forgetting the paper, it was a Canadian sample.

They looked at a similar thing. They looked at clients who had been with an advisor for a while. I don't remember what the time period was, but a lot longer relationship, which were much less likely to get out of the market or make their portfolio more conservative after the great financial crisis.

There does seem to be some evidence that that can help.

Dan Bortolotti: To answer the listener's question directly, how do you think people will react to the worst crash of all time? They will overreact, panic, act like it's the first time the market has ever gone down. Then when it's over, we'll look back and say, it was no big deal because we all knew it was going to recover.

I don't think things change very much in that respect.

Ben Felix: It's been going on for a while. There's hundreds of years at this point of documented financial crashes and recoveries. That doesn't mean that that's always going to happen, but it's been happening for a while and it's a pretty consistent pattern.

All right. Should we move on to the next one?

Dan Bortolotti: Yeah, let's do it. This one is from Shiva, the God of Death.

Ben Felix Okay.

Dan Bortolotti: Ben, I think this is a question we all need to take seriously given its source. Can you do an episode or a video about commissions and incentives in the financial industry? Specifically, calling out all of the investment advisors at banks who roll A-class structured notes for 3% a pop and do not manage portfolios. No love for the banks from the God of Death.

Ben Felix: Doesn't appear so. This is a very common thing. Structured notes are such a seemingly attractive thing to sell to an investor with little knowledge about expected returns and risk and how markets work and they do pay high commissions.

It doesn't help the situation. This is a pretty well-known problem. Banks sell financial products and they've got a strong profit motivation.

They don't really sell financial advice. They give advice about products maybe, but more in the way that someone, like when I go to the Subaru dealership to get a new car, they do give me advice about buying cars, but they're telling me which Subaru to buy. It's a different kind of advice than I think what we would tend to give to a client.

Just a different set of incentives. There was a March 2024 investigation that CBC did and they found that bank employees give questionable advice like telling people to invest in mutual funds or GICs instead of paying off credit card debt, which that's about as objectively wrong advice as you can get. Misrepresenting the importance of high mutual fund fees to long-term investment outcomes and upselling customers on higher fee credit cards and lines of credit.

Now bank employees don't seem to be malicious based on the CBC report. Many of them are stressed out by the pressure to sell at all costs. There are some pretty sad quotes and interviews from anonymous employees who are having a really hard time with the sales pressure, but also with having to push products on people that they maybe didn't need.

Based on some of the answers given by bank advisors on mutual fund fees and expected returns, I suspect that beyond conflict of interest, there's a lack of education that's contributing to the quality of advice. I think those two things can go hand in hand. If you don't know what's right, it's hard to give people the right advice.

It's probably also hard to deal with a conflict of interest. If you're being incentivized to do one thing and you don't realize that thing is wrong, it's probably a lot harder to overcome the incentive.

Dan Bortolotti: I find it interesting going through the whole education procedure, the certification process for the financial advisory designations, whether it's less so certified financial planner, but certainly the investment related ones. A lot of the courses in education you take are surprisingly sales oriented. They start from a premise that your job as an advisor is to produce market beating returns for one thing.

They constantly talk about products in a way that it's just about disclosure. As long as you tell them about the risks, you can pretty much sell them whatever they want. Cost isn't important because after fee returns are what really is important.

I think you're right about that. These are not bad people. These are people that are brought up in a bad system and given the wrong incentives.

As a consumer, you just have to be aware of that and go in with your skepticism up.

Ben Felix: There are some changes coming to proficiency in Canada. CRO has guidance on their website right now that's public, have been on this committee that's set these changes up. They're implementing new rules to establish an assessment centric proficiency model with some mandatory education and training requirements.

On January 1st, 2026, the CRO, the Canadian Investment Regulatory Organization will implement new rules to establish an assessment centric proficiency model with some mandatory education and training requirements. Purpose of this guidance is to assist dealer members, existing approved persons and individuals seeking approval prepare for the new rules in advance of the implementation date. They're giving guidance on what the new rules are going to look like.

They give commentary on, I don't know if they give commentary on what the exams are going to be like, but it's going to be good. They're very positive changes coming to proficiency in Canada, which I think is good news. It's definitely getting better.

Dan Bortolotti: There's no question about that. I've noticed that just in my own education here that we're all required to do just over the last decade or so, it's for sure getting better. There's much more of a focus on planning versus investing as well, which we've seen in the industry and therefore in the educational components of the industry as well.

So that's all good news. It's definitely not as bad as it was. There are much better, low cost products.

And there's, I think a little bit more transparency than there was in the past and higher levels of investor education. I've definitely seen that. I'd say 15 years ago, the level of awareness of fees and things was much, much lower than it is today.

So we're definitely making progress.

Ben Felix: You're right. If you go through the current reading requirements to become a licensed financial advisor in Canada, you wouldn't necessarily come away from that. If you studied that as your investment knowledge and came away and said, all right, I'm ready to invest.

You'd come away doing a bit of technical analysis maybe, probably picking some stocks, probably timing the market.

Dan Bortolotti: I'm going to look at that as a benchmark for progress. To be honest, I haven't looked at it while. But they need to get rid of that technical analysis component to basic financial advisor training, which just jumps out as something that's so transparently without value.

And that is considered not a fringe special skill that an advisor might pursue later, but what you need at the very basic level to advise your clients. It's just nonsense.

Ben Felix: Even the harmonization or the merger of the MFDA and CERO, I think that was also a positive development. Getting a mutual funds only license, the education requirements, the bar was lower to get a mutual funds license, which is you could still sell investment products to people. All that to say, I think part of the problem with the listener's question here stems from a lack of education for people who are able to get a license to sell financial products.

There is evidence supporting that. There's a paper in the Journal of Finance. That's a pretty well-known paper.

Juhani Linnainmaa was a guest in this podcast. He's a co-author of the paper. Actually, Stephen Forrester as well.

Two co-authors there. They have been guests, which is kind of neat. They look at a Canadian sample of financial advisors and the advisor's clients.

They find that advisors typically make the same mistakes personally as they do in their client accounts. They're trying to ask, is bad financial advice coming from conflicts of interest, or is it coming from education? They find that advisors trade too much, chase returns, prefer expensive actively managed funds, and under-diversify both in their clients' accounts and their personal accounts.

Their personal accounts underperform just as poorly as their clients' accounts do. One interesting thing they do is they show that advisors don't make these mistakes on purpose to convince their clients to do the same. Like, hey, look, I'm doing this too.

But the advisors continue to make the same mistakes after they leave the financial services industry. When they no longer have that incentive to say, look, I'm doing the same thing as I'm telling you to do, they continue making the same mistakes. That paper suggests that conflicts of interest are only part of the problem.

It does highlight the importance of education for financial professionals and for consumers to seek out financial advice from people with appropriate credentials and training. There is also a 2018 paper in the review of financial studies that's very relevant to this listener's question. They use data from a large retail bank to analyze how banks and their financial advisors generate profits from customers.

They find that advised transactions earn the bank higher profits than independently executed trades placed by the client. Unsurprising, the bank's own mutual funds and structured products are the most profitable products for the bank. That is not surprising.

Bank profits increase with trade size. Further, unsurprisingly, bank advisors recommend those transactions, large transactions into the bank's own products. Now, if those transactions were making clients better off, we might say, well, hey, these advisors are just giving good advice.

But the research finds that advised clients have worse performance than unadvised clients. This research really suggests strongly that advisors are putting their employer's interest first, likely due to incentives. But that is the system that the bank creates because the bank exists to generate profits and sell products in order to generate profits.

Dan Bortolotti: I think it's worth mentioning too a reference to the listener's specific question about structured notes. These are products that are extremely common in the bank advice channel. I don't even think anybody offers them other than banks.

At least, you don't see them nearly as often in other advice channels. But for listeners who might not be familiar with them, typically they are products that are sold to you with a return that is tied to some underlying index or some underlying investments. And just to give you an example, I had a client just very recently ask me, a friend of his had said that there was a product that he purchased from a bank that was tied to the big six Canadian bank stocks and it yielded 9%.

If you hold this biggest six bank stocks, your yield is, I don't know, a little under 4% probably today. Where is this 9% coming from? Well, I don't know.

The investor doesn't know. The bank knows. There's something built into the structure of that note.

I don't know whether it's returning some of your original investment to you. There are hidden risks and hidden structures that are extremely difficult to understand. And when those are packaged into an investment that sounds extremely enticing, like a 9% yield, this is a recipe for people buying products that sound superficially inviting, but they have no idea how they work.

If these are sold to you by advisors, and I've said this to people before because they've told me they've been offered them. I said, you ask your advisor to, in plain English, describe to you where that return is coming from. And if he starts hemming and hawing or she starts feeding you a whole bunch of BS, you know right off the bat that there's risks that you're not seeing.

These products, I just think are extremely dangerous because they're that toxic mix of extremely attractive at a surface level and extremely complex once you start digging into it. They're huge money makers for the banks. It's one thing to talk about high price mutual funds.

I think these are actually a lot worse.

Ben Felix: They're profitable for the banks because what the bank will do is they'll structure this payoff stream. In the 9% yield case, I'd have to look at that specific product, but typically what that number will be based on is the total return. That'll be the headline yield, the headline return, which is basically the best case return you're going to get from that product.

If the bank stocks increase in value up to some point, then you get to keep this high yield. They might cap your downside. They structure these payoffs using options.

What the bank will do is they'll structure the payoff that costs them some amount to hedge. They know exactly how much it's going to cost them to buy the underlying financial products that's going to allow them to deliver the payoff to the customer. Then they're going to sell those payoffs to the customer for a significant markup.

They're very, very profitable for the bank. We did an episode, episode 261. We had two researchers, Felix Fattinger and Petra Vokata, who have each great research on structure products specifically and just how they're sold, how they're packaged, how expensive they are, how big the markups are.

That's one of our longest episodes ever because we did two pretty in-depth discussions with two individual conversations we put in one episode. We went very deep on structure products. Actually, Dan, I think there are people in our portfolio manager channel who are using structure products too.

They're going to be different. They'll be F-class products, not paying commissions like the one somebody at the bank is selling. I've had some Twitter spats when I was more active on Twitter with people who are PMs who are promoting this type of thing, appealing to the same types of biases that make these things attractive to retail investors.

Dan Bortolotti: There's always a better product to deliver something similar. It may not be as enticing in the marketing materials, but if you want to get most of the upside, but less of the downside, there are always better ways to do it than structured nodes.

Ben Felix: That's exactly what the research on this suggests, that whatever it is that you're trying to accomplish, there's a better way to do it than a structured node. Unless you want that exact, very specific payoff, they will give you that, but you're going to pay a markup for it, which I don't know. I've talked to one advisor who thinks like we do, like they mostly use index funds.

They think markets work, but they will use structured nodes in certain cases. In that case, I'm thinking of if the market drops by some amount, say it's like a 20% threshold, they will go to a bank with their pricing of a structured node. This is how much this should cost.

We're not going to pay more. They'll negotiate a large allocation of that, and then the bank will structure it. It'll be something like when the market drops 20%, we're going to buy the structured node that gives us leveraged upside with limited downside.

They just systematically do that. My reaction is the same as yours, Dan.

Dan Bortolotti: My eyes are rolling for those who are listening here.

Ben Felix: But that is a less crazy use of those products. They're very specifically pricing them out themselves and going to the bank and saying, this is what this is worth. We'll allow you to do this much markup.

That's the least crazy use of those products that I've ever seen, but it's still, to me, crazy.

Dan Bortolotti: It's the least crazy, but there's still some crazy elements.

Ben Felix: It's a spectrum of crazy. It doesn't come off that spectrum with those products. All right, next one.

Dan Bortolotti: Based on available evidence, is trend following anything other than glorified technical analysis used to justify market timing? Has it been proven to have ex-ante returns beyond a buy and hold strategy that survives transaction costs and expenses? He's added here, and will you have Meb Faber on the podcast, who of course is a proponent of that trend following strategy?

Ben Felix: Yeah, Meb's a proponent of a few interesting strategies, but yes, this is one of them. Meb's welcome on this podcast anytime. I like Meb.

He's got a good podcast as well. Super smart guy and has written a lot of really good work. Totally.

Lots of respect for Meb. He can come on whenever he wants. Just let me know.

Now this is a topic that I'm not super comfortable being the arbiter of truth on. I think I've said before, I don't have a really strong opinion on it. There are two papers in the Journal of Financial Economics.

There's a 2012 paper titled Time Series Momentum and a 2020 paper titled Time Series Momentum. Is it there? Those two papers in the top journal or one of the top journals in financial economics that are taking opposing positions on the statistical reliability of the evidence supporting simple time series momentum.

I'm not going to be the guy that says who's right there. I think the law of financial economics research applies where for every PhD, there's an equal and opposite PhD, which is one of the reasons I think the term evidence-based investing is silly because whatever evidence you have, I can find some opposing evidence. We do not use Time Series Momentum products at PWL.

Looking at the live performance of many of them, this seems to have been perfectly fine so far. I'm not saying there's anything wrong with these products necessarily and it's possible that they can play a role in diversified portfolios. I have seen some research showing using simulation data, how they can fit into retirement portfolios for example.

Maybe we just haven't seen the type of environment where these products can shine yet with live performance. I looked at a few that are out there, a couple that are just really simple so it makes it easy to illustrate the point, but there's the Pacer Trendpilot US Large Cap ETF, which is getting in and out of stocks based on trend following rules. It's trailed the S&P 500 since inception in 2015 by 5 percentage points annualized.

The Pacer Trendpilot International ETF has trailed its underlying index by around 4 percentage points annualized since its inception in 2019. These are designed to participate in the market when it's trending up and then pair back exposure during short term market downtrends and prevent extended declines by moving to T-bills during long term market downtrends. Now they have been successful at reducing downside.

If you look at their returns chart, they're really interesting charts actually because you'll see this decline of the underlying equity index and the trend following one will kind of stop. Then it's flat for a bit and then the equity index recovers and the trend following one eventually starts participating in stocks again. The overall result has not been great unless you really value those specific payoffs.

I guess it's kind of like structured products. If you really care about doing exactly this thing, and maybe I guess if you believe the evidence is strong enough that it'll add value to your situation, but it seems like a pretty rough trade off, at least in isolation. I think somebody who's a proponent of these would say, you shouldn't just compare it to stocks, you should compare it maybe to a stock bond portfolio that has similar volatility or similar downside risk.

Fine. Or they might say that it belongs in a portfolio alongside equities, tailor it to your overall preferences. Fine.

I think like any product, you have to have a lot of conviction in what you're doing. You have to understand the range of potential outcomes and you've got to have an overarching philosophy to fall back on when things are not working as expected. To me, this just conceptually in terms of an investment of philosophy, I don't find these products compelling.

I know some people do and some very, very smart people have created products that implement these ideas. That's great and if people want to use them, that's fine, but it's not something that I think we'll be touching at PWL anytime soon.

Dan Bortolotti: It's funny because these last two questions, I think kind of dovetail. They're both based on the idea that you can achieve the returns of the market without accepting the risks of the market. There's always some kind of you get the upside, but you don't get the downside.

Look, we would all love for that to be a thing, but part of becoming a mature investor is let going of the idea that you can get that. If you want higher returns, we'd always joke diversification is the only true free lunch, but even that is just on the margins. It's like a misunderstood quote, but the idea is for the most part, if you want outsized returns, you got to take outside risk.

If you want to limit your losses, then you have to take less risk. There's no magic formula, whether it's some kind of structured product or what's essentially a market timing strategy that will allow you to avoid that. Just accept it and move on.

Ben Felix: Pretty much it. There's no magic formula or a silver bullet. There are different ways that you can transform risk and if you find a way that makes more sense for you, then that's fine.

As long as your expectations are in order, that's all I mean. I think we generally at PWL, we have a philosophy that is rooted in simplicity and I think that's an important part of our DNA. The hurdle for us to add something that's more complex, even something like dimensional, which is more complex than index funds, the hurdle is quite high.

Trend following is just not there for us. All right, next one. We often talk about how to best manage our income or investor savings.

If we thought about our years as 52 units and life as units, decade blocks, how do you plan on spending yours? How would you diversify your life for the maximum returns on sacrifices? I don't think in blocks, that's an interesting idea.

I guess it relates to, we talked to Cassie Holmes a while ago who researches happiness and one of the things she talked about is counting the times left. How many times left do you have to walk your kids to school in your life? How many times left do you have to go to dinner with your parents?

That's, I guess, kind of a form of blocking. How many blocks do you have left to do those things? I don't really think like that, but I do try to think along the lines of the PERMA model to filter how I spend my time from day to day.

That's positive emotion, that's like feeling good while you're doing stuff. I do try to check in with myself and make sure that I'm literally, am I enjoying what I'm doing right now? If I'm not enjoying it, I'll ask myself if it contributes to one of the upcoming points, one of the upcoming factors in the model.

If it doesn't, I'll consider whether I should really be spending my time doing that thing. I've also got little things that I enjoy and look forward to, like having a cup of tea in the morning, which is such a small thing, but I enjoy it. Sometimes if I take my daughter to her preschool, there's a really good coffee shop.

It's like a destination. People will come from Ottawa to go there. Sometimes they'll go in there to get a coffee.

That's all positive emotion, feeling good about what you're doing in the moment. The next one is engagement. I want to make sure the things I'm doing are challenging, where I have enough skill to enjoy the challenge.

That's like the Mihaly Csikszentmihalyi concept of flow, playing basketball in competitive leagues. I mentioned to you earlier, Dan, that I played last night. My lungs are still recovering from whatever respiratory thing I had going on and that might not have been a good idea.

I was gasping for air. Reading academic finance papers to find useful insights that I can write about and then writing about them, get engagement from that. Mountain biking on difficult single tracks, that's a tough one to beat.

Those are all states of flow where time just melts away. I try and make sure that I'm doing those things from time to time. I'm usually doing one of those things at least every day.

Relationships is the next thing in the permamodel. I do try to make time with friends and family. Being on a basketball team and playing pickup basketball, I have this kind of one group of guys that I'm connected with.

I see them usually at least once, sometimes depending on the time of year, twice a week and that's awesome. Working with people at PWL is another. Dan, the fact that you and I get to do this podcast and hang out and chat about this stuff is pretty incredible.

Dan Bortolotti: Well, I'd rather do that than play basketball against you.

Ben Felix: That's fair. I'd rather do this than try and play guitar with you or jam. I'd be pretty incompetent there.

The next factor in the permamodel is meaning. To me, it's important I'm contributing to something that's greater than myself. Honestly, this podcast and the community around it goes a long way in checking that box.

It's a pretty big deal personally when people leave a review or send an email saying that the podcast or my videos have changed their life. It might seem like a small thing to do to write a review or send a note or whatever, but it really validates that what we're doing here is useful, which matters a lot. It's like the ultimate reflection of serving something larger than yourself is hearing from other people who are saying that you've changed their lives.

I do some volunteer work too that contributes to meaning. Then accomplishment is the last one in the model. I do try to do hard things.

Writing a video or a podcast episode is a hard thing. Completing more of a challenging mountain bike ride that I completed the last time. There are these really good single track rides around where I live.

They're really hard. I can usually complete 75% of one. If I can push it to 80% or 85%, that'll feel really good afterwards without getting off the bike.

Winning a basketball game is another one. Completing the CFA program. Man, I still remember that.

I was in the PWL office when I got the email that I'd passed level three. That was a crazy feeling. That was three years of just grinding.

Anyway, that's the base of my whole life right there. Things that don't fit into that stuff or if they conflict with those things, I'll just try to eliminate them or outsource them. I do go to Costco every week, which is something that I don't love, but I bring at least two kids with me when we go and it becomes a fun thing.

The kids love Costco. I don't think about blocks, but I do think about trying to do things that fit into those boxes every day and just check in with how I'm spending my time. If it starts to go off course, then I will reevaluate.

Dan Bortolotti: Yeah, I think this was a good question. It's interesting. I think it was sort of asking whether there are any parallels between a financial plan and then just your larger life plan and use the term, how do you diversify your life?

I think at the risk of torturing the metaphor, I mean, if you look at those things that you just mentioned, there's like five different elements that make a satisfying life. Like a diversified portfolio, you want to have all of those in your life at every given time. However, as you get older, your focus on the individual ones in that diversified mix might change.

You were probably a lot more focused on accomplishment when you were younger and you still are, but when you're much older, you will probably have moved on from that. And stressing more about the relationships or the positive emotion. I think the point here is that if you're going to look to a financial model to provide some kind of metaphor for life, get all of those important elements in there all the time, but there's a glide path as you get older and you may emphasize one more than another.

Ben Felix: I love it. That's a cool idea.

Dan Bortolotti: It's a good question. We all focus on certain things to the exclusion of others when we're younger. And then as you get a little older and wiser, you start to realize maybe I should spend less time working and more time with my friends and family.

The way you structure your life made sense at the time, but it's going to evolve just like your plan and your portfolio is going to.

Ben Felix: Now, the real question is, can we get Scott Cederberg to run a million bootstrap simulations to find the optimal life glide path?

Dan Bortolotti: The 100%, I don't know. Engagement, meaning, relationships, I don't know. I don't know either. No, I'm going to stick with the diversified mix, I think.

Ben Felix: I really like that analogy though. I think you're right to say that accomplishment probably used to be more important, but it's shifted toward other stuff over time. Makes a lot of sense. All right, two more questions.

Dan Bortolotti: The next one, what is a safe strategy to invest with leverage apart from a mortgage?

Ben Felix: It's inherently risky, so it's difficult to call any leverage strategy safe. By levering something up, you're definitionally making it riskier. Although there is that one paper from Ayres and Nalebuff that say that boring when you're young actually makes long-term outcomes safer.

Maybe I shouldn't say so unequivocally that leverage is risky, but that's a bit of a different use case maybe, or a different way to frame risk at least. For a retail investor who really wants to use leverage, products with a built-in leverage take a lot of the operational load away. They can have drawbacks, like they're going to be more expensive, for example.

I'm not by any means recommending them. We don't use leverage products at PWL either. As Robert Merton said when he was on this podcast, complex financial strategies like options, which you can use for leverage, are best delivered to retail investors in the form of a product rather than telling them to go and buy call options themselves.

As an example, there's inherent risk in a leverage strategy, but there's also a risk in executing that strategy properly. If you go and read the WallStreetBets subreddit, there are lots of people who have done pretty serious damage to their personal finances by using options inappropriately. I'm not saying that the person asking this question is going to go and use options in that way, but I do think that there is execution risk for someone who is not a sophisticated investor in using options just full stop.

We've talked about this, I think, in past AMA episodes that some of the newer financial products that do return stacking, which again, as we've talked about, I'm not crazy about the general concept, but I think if somebody really did want to use leverage to have exposure to multiple asset classes in a portfolio, those products are a really neat way to do that. I don't know if the listener was hoping that we would go through, well, you could use options, you could use a whole micro line of credit, you could use an unsecured loan, I don't know, all the different forms of leverage and what's the optimal one. I think it's going to depend on your situation and what exactly you're trying to accomplish.

For many of the use cases of leverage, I do think that productizing it is a pretty useful way for retail investors to access leverage if they want to do that, which I'm not recommending and we don't do, but if that's what you wanted to do, I think that's a pretty good way to do it.

Dan Bortolotti: My thoughts on this are that I don't really think there's any safe strategy to invest with leverage, although it's interesting that the questioner said apart from a mortgage. I would say there's really nothing apart from a mortgage because the mortgage is the one leverage strategy that's pretty easy to defend. I mean, there's a bunch of reasons for that.

If you mortgage your principal residence, first of all, you're getting enormous utility from the asset that you're buying, which isn't the case if you borrow to buy a portfolio of stocks. There isn't a whole lot of alternative. In other words, if you want to buy a house, most people can't buy part of a house and then add a little bit more every week or month like you can with a portfolio of stocks.

It's either you don't buy it or you buy it with leverage. Then I think the final thing is houses can certainly go up and down in value, but not to anywhere close to the level of volatility as a stock portfolio and what blows up the execution of a leverage strategy is an inability to deal with the volatility of the asset that you've purchased. Your house will go up and down in value, but not in the same way that a volatile portfolio of stocks can do.

Whenever you buy an asset that is not particularly volatile, your expected return on that asset should be relatively low. Borrowing at 3% and buying an asset that you expect to return 10% is probably overly optimistic, but borrowing to buy a home that you can comfortably make the payoffs and live in during that period. As we said before, no one panic sells houses.

When they fall in value, people do what they should do with stocks, which is I don't care what the value is except on the day I need to sell it. For all those reasons, I think leverage becomes quite important or quite productive in terms of a principal residence, but I can't think of any other investment situation that comes anywhere close to that.

Ben Felix: In theory, someone might argue that it makes sense to add a bunch of assets together that make the overall portfolio less risky and then lever that up to the risk of say the volatility level of a stock portfolio. That's a safer way to invest in using stocks and that's something that I wouldn't necessarily do in the name of simplicity and also that it's not super obvious that that's actually going to lead to a better outcome. It's one of those things where there's lots of really interesting things that we can model and say, look, this might have worked in the past, but the portfolio of gold long-term bonds, stocks and I don't know what else goes in there, something else.

With leverage, not a great strategy in my opinion. Maybe great for someone else, which is fine. All right, last question from Kushla.

What is your view on the potential impact of demographic changes and what is trendy in investment for those who buy and hold ETFs over the long haul? 20 plus years. They're super trending now for good reason, but what happens when the current wave of investors wants to cash out in retirement if trends or demographics have changed and there are fewer buyers?

Even if the underlying asset prices are good, could the sell price of the ETF suffer? Is there any research or modeling on this possibility and what is your view? On the last part of the question, it's fairly rare for there to be dislocations between the net asset value of an ETF and its unit price.

They can happen. Dave Nadig, who's got a lot of expertise in ETFs, told us way back in an older episode that he considers that to be an additional pricing vector for the underlying assets. If you have illiquid assets in an ETF and the ETF price, the unit price changes when the NAV doesn't.

He's saying the ETF price, because it's more liquid, is probably a better indication than the actual value of the underlying assets. He's arguing that's not really a dislocation. I think Marco Sammon disagreed with that when he was on.

He's done research on that too. Fairly rare for there to be big differences in the unit price and the net asset value of an ETF because of the arbitrage mechanism that's designed to keep those things pretty close. On the main question, I think it's important to remember that money doesn't leave the system.

When someone sells, someone else is buying. That has to be true. It's possible that the changing characteristics of asset owners can affect asset prices.

That is discussed in some of Ralph Koijen's work on the shift away from active and toward passive management. Assets shifting from investors with higher demand elasticities, like actively managed funds and hedge funds, to investors with lower demand elasticities, like index funds, does seem to have an effect on asset prices. He does look at that in the paper, which investors matter for equity valuations and expected returns.

To test the effects of the shift to index funds, him and his co-author hold demand elasticities for different types of investors constant. Then they compute the counterfactual asset prices in a world where the shift toward indexing had not happened. It's interesting to think about.

He did talk about this on his episode, his Rational Reminder episode, if people want to hear more. To the listener's question, how do changing demographics change asset prices? I don't know if we can know that.

If assets are shifting from one demographic group to another, are they going to have different demand elasticities in such a way that changes cross-sectional asset prices? Maybe, but not in a way that I think is either predictable or scary. Necessarily.

Now, index funds do seem to have made markets less elastic.

Dan Bortolotti: There's a lot of these trends that, yes, they might very well turn out to be true. Even if we're worried about them, what are we going to do about them?

Ben Felix: It could be scary if you want it to be. I just mean like it's not something that we should dwell on and think about, oh no, this thing is going to be really bad. A kind of related point is that index funds do seem to have made markets less elastic.

Index funds have inelastic demand for stocks. Their demand for stocks is completely insensitive to stock prices. They buy what is in the index without considering whether it's cheap or expensive.

Imagine going to the grocery store and planning to buy five apples when you go to Costco or whatever. I mostly shop at Costco. There's a delivery service out of Montreal that delivers fresh produce.

We've started getting a lot of our produce from there. They deliver it to where we live, which I was actually really surprised by. I still go to Costco every week.

Big fan. Lufa is the Montreal delivery service. They've been fantastic.

It's a lot of locally grown produce from around Montreal. Anyway, if apples are usually $1, but today they're $5, you might buy fewer apples or maybe no apples like I would. If apples 5X in price, I'm probably not going to buy apples that week.

Maybe I'll make grapes instead. I don't know. But that's because in that example, your demand for apples is elastic.

Now, if you had or if I had inelastic demand, if my job was to buy five apples, regardless of what their price was, I'm going to buy five apples. That's kind of what index funds are doing. They have inelastic demand.

They buy regardless of the price. It's possible that as index investing becomes more prevalent, the market could become increasingly inelastic. What that means is that a transaction, like investing $1 in the stock market in an inelastic market, increases the market's value by more than the $1.

Ralph Koijen has an estimate that puts that figure at $5. The same thing is true for individual stocks. We had Valentin Haddad on this podcast a while ago and he talked about his research on that.

Now, inelastic demand for stocks can lead to more volatile prices and more price impact from trading. In a perfectly competitive stock market, increasing the weight of index investors would not matter because their inelastic demand would be offset by active managers increasing their demand elasticity as they compete with each other to bring information to the market. That's the classical view of how markets work and why the shift index funds doesn't really matter.

The problem is that competition among active managers may not be as fierce as that simple model suggests. That's what Valentin's paper looks at. How competitive is the stock market paper?

He finds that while active investors do increase their demand elasticities to offset the effect of a shift indexing, the response only reduces the effect by about two thirds. He basically documents that prices have become less elastic over time as indexing has increased, which can increase volatility at the stock level and increasingly so when a stock has more passive investors. Does that mean that if people are en masse liquidating their retirement accounts to fund their spending, that we're going to see a massive decline in stock prices?

I don't know if it's that obvious to draw that conclusion, but it's something to think about. If markets are getting less elastic over time, maybe flows start to matter more. Maybe changing characteristics of investor bases start to matter more.

This is Mike Green's whole point, although he's a little more extreme on the expected impacts of it than I think I would be. I think the general direction of his thinking is probably right. Vanguard does have a paper on this topic, not on the price elasticity piece, which would probably drive Mike Green nuts.

The fact that Vanguard has looked at this and hasn't looked at that specific piece because he blames Vanguard for a lot of the stuff that he's worried about. Their paper is titled Megatrends, the economics of a graying world. They explain that lower fertility rates and longer life expectancies are expected to drive unprecedented shifts.

This is all a quote. In the composition of populations globally as the percentage of those age 65 and older is estimated to nearly double. This is an older paper from 8% in 2015 to 15% in 2045.

They say that demographics can only one factor affect the economic growth, but these changes do have important implications for how economies may evolve. They estimate that these demographic trends will have a neutral to negative impact on long-term GDP growth. Their idea there is that lower population growth and lower participation in the labor force are going to have one effect, but that may be offset by higher productivity growth that is needed for a shrinking number of workers to support a growing number of retirees.

They conclude that from an investor's perspective, although demographics may exert downward pressure on the risk-free interest rate, risk premia are not clearly linked to demographic changes, which makes sense. Vanguard concludes that in light of these conclusions, a low cost globally diversified portfolio provides the best chance of investment success through exposure to a variety of growth and demographic outlooks, which sounds like something that we'd say.

Dan Bortolotti: I was going to say, isn't it funny how that's the cadence of virtually every answer here? Yes, this is true. Yes, this is interesting research.

At the end of the day, your best chance of success is a low cost globally diversified portfolio of index funds, period. It's not to dismiss the importance of the question. I don't mean to come across that way, but there are a lot of things, a lot of trends that will affect investment performance in the long term, but at the end of the day, we don't truly understand how that's going to shake down.

Even if we did, I don't know what the alternative is. If you knew that was going to be true, that there would be more selling pressure as the population gets older, there's going to be more sellers than buyers, et cetera. I don't know how you react to that.

I don't know how you reposition your investment strategy in order to capitalize on that or to make that risk go away.

Ben Felix: When we've had Mike Green on this podcast, when I've talked to him, that's one of the most striking takeaways that I got, and maybe that's my own lens of listening to Mike, is that yeah, these things might be a big issue. Yes, it's very possible prices are becoming less elastic. Yes, it's very possible that could lead to big price declines in the event that there was a shift in dollars from one set of asset owners to another or a shift in overall asset allocations that people want to have, which can put increasingly large downward pressure on prices if prices are less elastic.

We can say all that's true, but what should you actually do? Okay, Mike, I hear what you're saying. That all makes a lot of sense.

What are we going to do about it? All you can do is stay invested and hope that it's mitigated by the time that it becomes a problem, if it is a problem, or hope that it doesn't happen in your lifetime. There's not a whole lot that you can do to fight against it.

Mike also acknowledges when we talk to him, even if we agree that all those things are issues that will eventually come to a head, we have no idea when that's going to happen.

Dan Bortolotti: It's a little bit like health concerns. There's a lot of parts of our health that we can control and there's a lot of parts of our health that we can't control. If we spend too much time worrying about the grave consequences of health issues that we can't control, I don't know that we're any further ahead.

Certainly, we have more anxiety. Maybe we have a lower quality of life now, but we haven't really done anything to protect ourselves. We're glad that there are other people out there researching these things.

It's not like they should be ignored, but at the level of the individual investor, you got to focus on what you can control. This doesn't seem to me like something you have any control over at all.

Ben Felix: I think people have a bias for action. They'll think about this big thing is scary, therefore, I should do something. That something can take so many different forms.

In many cases, that form is some of the stuff that we talked about during this episode. I'm going to buy these structured notes to protect my downside because I'm worried about the aging population crashing the stock market. I think that's one of the biggest challenges investors have, which speaks to one of the other questions that we had in this AMA about the boring middle and staying in your seat and not getting distracted.

Dan Bortolotti: People don't like uncertainty and they will do anything they can to try to get a little more certainty. Sometimes, those decisions end up meaning you pay more for a product that you think will deliver certainty, but it either doesn't or it does at too high of a price, or we just spent too much time with the anxiety that doesn't have any long-term benefits, unfortunately. A good round of questions for sure.

All right, that's it for the questions.

Ben Felix: Go to the after show. Let's go. I will mention, you talked about the health concerns analogy. I did have my six-month oncology check-in. I had done blood work two weeks beforehand and then I went in for a physical exam and that was all clear. At the six-month mark, all clear so far, which is good.

Great news. For anyone who doesn't know what I'm talking about, I was diagnosed with testicular cancer back in – I was told I had to have surgery in January. I had the surgery and then the diagnosis came sometime after that. That seems to be moving in the right direction or at least, just not moving at all, which is good. It's the right direction, exactly. The next check-up is in three months, which is another CT scan. Then, the frequency of those check-ins reduces by half. There's one more. The first year is more intense and then after that, the cadence drops in half.

Good news. Excellent. All right, do some reviews? Yeah, I'll take the first one here.

Dan Bortolotti: It's just titled, Thankful. I've been a fan of the show for many years. You recently did an episode dedicated to spicy discussions and I have to say, it is by far one of my favorites.

It was such a well-rounded discussion on the cult mentality that so many people fall into today. I'm very thankful to have found such a great podcast filled with so much rich value and sage wisdom. Sincerely, thank you for the work you do by Manny C4U from the United States.

Ben Felix: See man, I love getting those reviews. We're sitting here talking to each other, but then this person from somewhere in the United States is telling us how impactful it is. It's awesome.

I like sitting here and talking to you and we're having a good time separate from the reviews. Then you hear from people that are like, hey, you guys sitting there talking to each other really helped me improve my life. That's awesome.

Dan Bortolotti: I've really been amazed at the reach of this podcast since I joined you guys. I knew that it was popular here in Canada, but I had not appreciated the international reach. When we saw it today, we had a couple of questions from Italy.

I was commenting and we're getting people, not just from the US, but from around the world. That's pretty amazing.

Ben Felix: That is cool. All right, next review. Consistently great. Newer listener enjoying going through the backlog to get consistently great and informative discussions on finance by Sasahas. Oh man, from the United States of America. Easy for you to say.

Dan Bortolotti: For the record, I don't think that's a real name.

Ben Felix: I suspect not.

Dan Bortolotti: We're not making fun of somebody's name. I think that's just a alias.

Ben Felix: I would hope so. Yes. Otherwise, I apologize.

Dan Bortolotti: All right, next one is, awesome pod. Ben and team know how to bring the heat. This very educational and extremely relevant podcast bridges cutting edge research and practical advice.

I enjoy the pod every week. Very nice to hear from Canadian couch potato, Dan B. Awesome work lads, from Kimurar from Canada.

Oh, we actually have a Canadian reviewer.

Ben Felix: Got a couple in here actually. Five-star advice in regards to general investing advice, Ben and Cameron, they must have not listened to newer episodes. They didn't mention Mark and Dan.

Give better advice than 99% of people that I have ever heard by RA18888 from the United States of America on iTunes.

Dan Bortolotti: Just rounding these out, I've enjoyed this podcast for many years and I'm thankful for all of the financial and life learnings that Ben, Cameron, Dan and the RR team have brought me through this podcast. The content is delivered at a high level due to the team's professionalism, passion, humility and for the way they run their interviews. Thank you gentlemen for inspiring me in this area of life from Jay here to learn from Canada.

Very nice. Some very nice reviews today.

Ben Felix: And like I said during the recording and a minute ago, we really do appreciate them. The podcast is worth it for us for a lot of reasons. I enjoy preparing for it.

I enjoy doing it, like recording right now, but hearing from people that it's impacting is just another really important piece of why it's an enjoyable activity. If anyone is listening and has not yet left a review, we would love to hear from you. I do want to mention real quick before we go, I have some electricians doing work below me.

If you heard any banging throughout the recording, that's what that was. Sorry about the noise.

Disclosure:

Portfolio management and brokerage services in Canada are offered exclusively by PWL Capital, Inc. (“PWL Capital”) which is regulated by the Canadian Investment Regulatory Organization (CIRO) and is a member of the Canadian Investor Protection Fund (CIPF).  Investment advisory services in the United States of America are offered exclusively by OneDigital Investment Advisors LLC (“OneDigital”). OneDigital and PWL Capital are affiliated entities, however, each company has financial responsibility for only its own products and services.  Nothing herein constitutes an offer or solicitation to buy or sell any security. This communication is distributed for informational purposes only; the information contained herein has been derived from sources believed to be accurate, but no guarantee as to its accuracy or completeness can be made. Furthermore, nothing herein should be construed as investment, tax or legal advice and/or used to make any investment decisions. Different types of investments and investment strategies have varying degrees of risk and are not suitable for all investors. You should consult with a professional adviser to see how the information contained herein may apply to your individual circumstances. All market indices discussed are unmanaged, do not incur management fees, and cannot be invested in directly. All investing involves risk of loss and nothing herein should be construed as a guarantee of any specific outcome or profit. Past performance is not indicative of or a guarantee of future results. All statements and opinions presented herein are those of the individual hosts and/or guests, are current only as of this communication’s original publication date and are subject to change without notice. Neither OneDigital nor PWL Capital has any obligation to provide revised statements and/or opinions in the event of changed circumstances.

Is there an error in the transcript? Let us know! Email us at info@rationalreminder.ca. 

Be sure to add the episode number for reference.