## Episode 432

Ben Felix: Welcome to episode 432 of the Rational Reminder Podcast. We're hosted by me, Benjamin Felix, Chief Investment Officer and Portfolio Manager at PWL Capital.

Dan Bortolotti: And I'm Dan Bortolotti, Portfolio Manager at PWL Capital.

Ben Felix: And today we are joined by Chris Murray and Marco Sammon for a fascinating conversation. Chris earned a master's degree in machine learning from Carnegie Mellon University in 2007. He then spent over a decade of working as an equity quant and trader at Goldman Sachs and J.P. Morgan.

In 2023, he joined Jiko as the head of trading. It's a bank that uses US treasury bills to offer a safe yield generating alternative to traditional cash management. It's just an interesting side note.

We don't talk about anything related to that. And then in that same year, he started working as a researcher at Harvard Business School with Marco Sammon. Marco has been a guest on this podcast twice in the past.

He's an assistant professor in the finance unit at Harvard Business School. We talked to them, Dan, about leveraged ETFs.

Dan Bortolotti: Yeah, this one was a real deep dive, but I think everyone's going to enjoy this one because both Marco and Chris are just so articulate at describing what are some pretty complex ideas, but a lot of insights in their papers. And I think we really teased out a lot of things from them during the discussion.

Ben Felix: Yep. So a warning before you get into listening to this one, it's up there with the nerdiest episodes we've ever done. Some of it, Dan, you and I were chatting earlier, it went over our heads too.

So I mean, do your best as you listen through. It was clear that for some of the conversation, Marco and Chris were talking to regular people, but for portions of it, they were definitely talking to other researchers, which is interesting to listen to. But I mean, I guess I'm just saying, if it goes over your head, don't feel too bad and stick around at the end to hear Dan and I give our thoughts on the conversation.

But for now, let's go ahead to our episode with Marco and Chris. Marco Sammon and Chris Murray, welcome to the Rational Reminder Podcast.

Marco Sammon: Thanks so much for having me back on.

Chris Murray: Looking forward to it.

Ben Felix: Yeah. Very nice to have you back, Marco and Chris, super excited to be talking to you for the first time. You guys wrote a very nerdy paper. I'm pretty sure I'm comfortable saying that this might be one of the nerdiest episodes we've ever done, but we'll let it speak for itself. 

To start off, guys, how do LETFs or leveraged ETFs work?

Chris Murray: Fantastic question. As people probably know if they read the prospectus, leveraged ETFs target a multiple of the daily return of a stock or an index. So they aren't trying to get 2x the annual return, they're trying to get 2x the daily return.

And one of the nuances of this is that this isn't free. There are benefits to this and there are costs to this. And when they're doing this, they have to borrow to get their leverage.

So leverage isn't something you can get for free. The extent to which leverage isn't free is related to borrowing rates. And as most of you listeners probably know, borrowing rates have gone up pretty substantially in the last few years relative to what they were through a lot of our sample.

That's one of the points that we'll talk on later. Usually what they do is they enter into a swap with a large bank to get that leverage. So if I'm a 2x leveraged ETF, I'm not sitting there holding the actual underlying stock.

I have a swap with a bank. And if my ETF has 100 million of assets, I have a swap for 200 million of the underlying asset. And I'm going to rebalance that swap every day against the bank to make sure that I can maintain my target leverage ratio.

Dan Bortolotti: Now, how significant have these leveraged ETFs become in the U.S. ETF market now?

Chris Murray: They're big, but they're not massive. If I was going to compare them to something like index funds or mutual funds, they're not even close. They definitively are not there, but they have grown a lot.

In the data set we were looking at, they're a little bit over $100 billion, which is real, but for the U.S. market, that's not too massive. Where they've been growing, the interesting thing is it's not the vanilla index ones. It's the single stock, it's the crypto, it's the hairy stuff. That's what's been taking off recently.

Ben Felix: Why do you think that hairy stuff is getting so popular?

Marco Sammon: I think that you already had an amazing nerdy episode with Hank where you talked about leveraged ETFs. I think Hank already touched on a lot of things. There's a lot of evidence that investors like lottery-like payoffs.

You say, hey, look, NVIDIA is up 1,000%. What if I was 3X that? I just thought about this as you guys were talking.

We're in maybe the Frontier Airlines world of finance, where now we're creating products that can cater to every possible type of investor. We have 3,500 ETFs that are from active to leveraged long, leveraged short, sector, broad market. I think it might be part of the broader trend of let's make products that cater to every little thing people want.

They know what people want, which is lottery tickets, and they're going to offer you very bespoke lottery tickets on different outcomes.

Chris Murray: In the past few years, you've seen options trading grow phenomenally. You've seen a lot of people buying zero-data expiry options. This is almost the definition of a lottery ticket.

Now you've gotten, the last few years, prediction markets. A few years ago, you had meme stocks. There's just a lot of quasi-regulated ways for people to have this gambling-like experience. Single-shot ETFs certainly serve that. Leveraged ETFs serve that need.

Marco Sammon: To take it a step back, I also think that, like Chris said, there are costs and benefits. They're offering you a service. For me to go in my interactive broker's account or whatever place you want to use and borrow money, lever up, figure out paying it back, maintain my leverage ratio, rebalance, they are offering a much simpler way to do leverage.

You never need to rebalance. If you want to sell your share, you can just sell it in the secondary market. That service is worth something.

Ben Felix: Right. Meeting demand for regulated lottery tickets aside, how does leveraged exposure to the stock market fit with economic theory?

Marco Sammon: I'll take the first stab at this because it reminds me a lot as I used to teach this investments class when I was at Kellogg in the evening MBA. There was always this graph we showed them, which is like, oh, you have a huge stock when you're young of human capital, and that's going to kind of go down over your lifetime. Your financial wealth is going to grow.

And given that you have this huge stock of human capital, it's perhaps not that risky. And so to get to your optimal level of risk, perhaps you should lever up early in your life. I think Chris will add on to this because him and I have talked a lot about the idea of a mild leverage ETF.

But there's a few caveats to this. One thing is it's got to be cheap. Fees, funding costs, everything are going to compound over your life.

And so if it's expensive over your whole life, even if leverage is good, that's going to be a big headwind. But the second thing is a lot of this advice is rooted in the CAPM. It's the idea of a diversified investor.

However, there's two pieces that don't hold here. So the first thing is you're probably going to lose your job at the same time the stock market goes down. This is going to suggest there might be a little bit more beta than you think in your human capital.

And the second thing is, is that you have some risk in your human capital that you can't diversify away. So if you don't mind, I have a little bit of a story about this in a little bit of a different context. I lived in Boston and a few years ago, I was looking to buy a house.

I still haven't bought a house yet. As Chris mentioned, interest rates have gone up. But the real estate agent showed me these pictures and they're like, wow, Back Bay and Cambridge, these neighborhoods are the only two neighborhoods in all of Boston that have just gone up and up and up.

So these are the two places to buy. One of my good friends, following this advice, bought a beautiful building in Cambridge on the Charles River, overlooking the Charles, two units, combined them. This was going to be a slam dunk.

Turns out he starts digging into it, building 70 years old, and the support beams have started to detach from the walls. Building can't be saved, condemned, building is collapsed, and that goes to zero. Why am I telling you this?

Because yes, on average, housing in Cambridge and housing in Back Bay have gone up over the last 30 years, every year. But that one house that he bought didn't. And it could be the same with your human capital.

You could be displaced by, I don't know, a technology shock like AI. That's, I guess, my issue with this advice of levering up early in your life, because you have a lot of risks that are hard to diversify. And those shocks might come exactly at the time that your levered exposure to the stock market goes down. I don't know. Chris, you should chime in on this too.

Chris Murray: I 100% agree. We have talked a lot about there's no logical reason that ratios of stocks to bonds from zero to 100 are reasonable, but then 100.01 is completely unreasonable. So it certainly makes sense to say, if you want exposure to the market, young people might want to lever it. One question we'd have is, is 2x really the right number for a long-term, boring, CAPM-type investor?

Probably not, but something like a 1.25 gets really interesting. And second is, because the question is, how do these fit with economic theory? The light leverage on the S&P fits really, really, really well.

The 2x leverage on crypto is like, you completely walk off the cliff. You're gone. Economic theory has left the building.

That's what's nice about these things is they're just this mix of products. And one of the points we try to make in our paper is, we're not going to say leveraged ETFs are, I mean, we never say good or bad. You couldn't say something like that because you have to describe what you're talking about. Leverage on what? How much leverage? Those are the questions.

Anyone who makes a blanket statement, leveraged ETFs are bad or good, that just isn't supported by the data.

Marco Sammon: And I guess one more thing on this that I also wanted to say is, when you invest in a risky thing like equities, your returns are volatile, but the payments you make on borrowing are fixed. And so that creates this sort of problem of, well, what if in a year I don't have enough returns to cover the borrowing costs and what, am I going to sell to my principal? And of course, that might happen when prices are low and expected returns are high.

So you're selling down at exactly the point that you don't want to. So that part of it also matters as well.

Dan Bortolotti: You guys have both touched on this already, like specifically with reference to the potential lack of diversification of your human capital, but what are some of the other ways that we need to approach this theory a little bit more cautiously? In other words, the appropriateness of leverage early in life.

Chris Murray: Like Marco said, there's correlation between your income and the economy. If you have levered equity exposure, you can get two things going bad at the same time, which isn't good. And I guess the second, which we'll talk to a little bit more is the long-run returns.

So the long-run returns of leverage exposure cannot be simply described as some multiple of the unlevered exposure. That's an important consideration. Again, that doesn't mean leverage is bad. 

It just means that you need to be thoughtful about applying leverage.

Ben Felix: All right, Chris, you touched on this. Now we're about to go into the rabbit hole of nerdiness. What do long horizon LETF investor level returns depend on?

Chris Murray: All right, getting to the meat of it. I'll begin with the intuitive baseline. The intuitive baseline is I've got a 2x long levered ETF.

It's on an index and the index is up 20% on the year. What should the 2x long be up? The logical naive person on the street is going to say, well, twice 20% is 40%.

Pretty easy. Even ignoring fees and financing, that's wrong for two reasons. One of those reasons is actually going to make the 2x levered ETF do better.

It's going to exceed that. And one of them is going to make the 2x levered ETF do worse. So the one that makes it do better is what we call a "convexity bonus."

And if that term isn't coined, we're going to coin it right here at 9:47 a.m. Pacific time on the podcast for the record. If someone else coined it, then so be it. But the reason this exists is a 2x levered ETF doesn't double the return. It squares the return. So what does that mean? This is before volatility.

So if the underlier is up 20% over a year, the 2x doesn't get 40, it gets 44 before volatility drag. If the underlier is up 40%, the 2x, it gets 40% squared, which gives you sort of a bonus 16. I think that'd be 96% if I can do math right.

When returns get big, that number gets bonkers. If you've got an underlier of 200%, now you're going to square it. 1 plus 200% is 3. Three squared is 9 minus 1 is 8. It's a big number. This convexity bonus always works in the levered ETF's favor if the underlier's up or down is positive.

So that's on the upside. On the downside is something that we call volatility drag. And this has been discussed a lot.

So here we're going to be very precise what we mean about this. And volatility drag says that on any given path that the underlier follows, pick your path. There's a very simple equation that says this is what the levered ETF is going to get.

We'll get to it in a minute. That equation has a multiple that multiplies the squared underlier return by something that's related to the variance of the underlier as it gets to its final destination. So as the underlier has more and more variance, that multiplicatively reduces the wealth of the 2x levered ETF.

The exact form of the equation, again, sorry, we have to get really nerdy on this, is that the levered ETF's long-term return is basically the square of the underlier's return, 1 plus the underlier return, multiplied by, I'm going to simplify it, the exponentiated variance. So when the variance of the underlier goes up, it multiplicatively reduces the wealth of the levered ETF. And this is not making any assumptions about correlation or any assumptions about geometric Brownian motion.

This is something that's basically always true. In continuous time, it's always true. In discrete, it's a pretty good approximation.

So we've got, again, naive benchmark is twice the underlier. You got a bonus from the square of the underlier return. And then all the wealth gets dragged down multiplicatively based on the variance.

And this is probably the most nerdy deep dive piece that we'll have to get to. Marco, anything you want to add?

Marco Sammon: Yeah, I guess I just want to go way simpler. And we're going to try to give a few numerical examples to illustrate this.

And I think that there's two layers of this. One of these is the math of compounding. And one of these is volatility drag.

And so Chris, you should hold me honest on this because him and I have gone back and forth a lot on this, we want to be precise because people mix this stuff up. Ben and Dan, I have a good question for you to start, okay? This is a classic question you ask any first-year behavioral finance student.

A bat and a ball cost a dollar and 10 cents. A bat is a dollar more than the ball. How much is the ball?

Dan Bortolotti: The answer everybody wants to say is a dollar.

Marco Sammon: Yeah, exactly.

Dan Bortolotti: It's the bat and the ball together are a dollar.

Marco Sammon: A dollar and 10. And the bat is a dollar more than a ball.

Dan Bortolotti: So the ball is five and the bat is a dollar five.

Marco Sammon: Nice. So great. So now, you know, I have an asset that's up 10% one day and down 10% the next day. What's it at the end of the day?

Dan Bortolotti: Not zero.

Marco Sammon: Exactly. So that's the mathematics. Wow, Dan, I couldn't get you. I'm kind of embarrassed at this point. I really thought...

Ben Felix: I didn't answer on purpose.

Dan Bortolotti: Ben knew and he's like, I want to see if Dan can get this.

Marco Sammon: So yeah, you're right. You're down 1%. So, you know, you're up 10%, you're down 10%.

The arithmetic average of your returns, zero, but you're down 1%. Now let's imagine we have a levered ETF that targets two times the daily return. So first day, the levered ETF targets two times 10%, 20%.

Second day, two times minus 10%, minus 20%. You end up down 4% from your original investment. Now, this is surprising because you would have thought, like Chris said, oh, well, the underlying investment is down 1%.

My two times levered ETF should be down 2%, but it's not. And then here, now here's where we get really tricky. This is kind of a small return.

10% is a small return. The levered ETF is down 4%. And you would have expected if it was down two times the underlying, it would be down 2%.

Now this additional 2% loss reflects two things. As Chris said, there's going to be a convexity bonus. But here, because the returns are not that humongous, it's small at 0.01 percentage points or one basis point. And then there's a volatility drag of 2.01%, leading up to the total extra loss of 2%. And so that's in our mind, this idea of you're down and then you're down even more. But we need to separate the basic idea of compounding that applies even to non-levered assets.

And then on top of that, we have volatility drag. I guess that's kind of the idea we have in mind. If I can add two more things on this.

So first, Chris and I were talking this morning about, well, this is an example for a two times levered ETF. What if we have a three times levered ETF? And then maybe this is even nerdier.

But there, the convexity bonus is going to be three times the square return of the underlier plus the underlier return cubed. And now if you start taking this on stuff like NVIDIA and stocks that have had a massive run up, this can actually become a meaningful thing. In the little example I gave you, up and down 10%.

It's not huge, but up and down 100%, 1000%, this is huge. The second thing I want to say is, and again, what Chris said, that this always helps you. This is something that I'm going to give Chris a lot of compliments.

And I always say Chris is like the Wayne Gretzky of finance. He always is skating where the puck is going. I've been telling everyone this.

Chris and I wrote this paper together years ago about fast track IPOs. Everyone's like, why are you writing about this? SpaceX gets fast tracked and everyone's asking Chris and I what's up. I have to give credit. Chris is the Wayne Gretzky here. So Chris was telling me this.

And I said, how can this be true? And I had to really rack my brain. And then I thought about a simple example of imagine something goes down.

So I have an underlying asset starts at 100 bucks. First day, it goes down to 75 bucks. Next day, it goes down to 50 bucks.

The underlying has lost 50% in total, cumulatively. Now, if I levered once at 2x, after I repaid my debt, I would have nothing left. I would have went to zero.

Now imagine I have a two times daily levered reset ETF. First day underlying falls 25%. So the ETF falls 50% from say 100 to 50 bucks.

And then it resets exposure downward. And so on the second day, when the underlier goes from 75 to 50, the ETF loses 66 and two thirds percent of its remaining 50 bucks. But it ends with 16.67 instead of zero.

Now, of course, there's two components there. One of them is the convexity bonus. One of them is the volatility drag.

We can talk about decomposing that. But I think that there's in there, again, both of those components. Why didn't we go all the way to zero?

A little bit of that is the convexity bonus. And another 8.33 was loss of volatility track, basically.

Chris Murray: I think the key for listeners and for researchers looking at this later is there's one relatively simple equation that relates the levered ETF long-term return to the underlier. And we've decomposed and pointed to different components of that equation. And when we say VolDRAG, we're referring to the exponential drag at the end.

And when we say convexity bonus, we're referring to the R squared of the underlier.

Ben Felix: And the convexity bonus, if I understood you just now, Marco, that's coming from the resets?

Marco Sammon: Yeah. And this is something him and I've talked a lot about this. But yes, I would say that it is not there in a set leverage once and never reset leverage will not have the convexity bonus. So it is a feature of the daily resets.

Ben Felix: Interesting.

Marco Sammon: Or any reset over any interval.

Ben Felix: So you've got volatility drag that you're going to have regardless. Leverage is going to increase your volatility drag. And then you've got convexity based on how frequently you're resetting your leverage. Interesting. How do you estimate the effect of volatility on cumulative returns?

Chris Murray: That's just the volatility drag term. Scales like variance and volatility. That's an important thing.

Volatility drag was, I think someone coined that term a while ago. Unfortunately, the drag is technically related to quadratic variation, but effectively it's variance. So if the path-wise volatility doubles, the drag will quadruple.

If the path-wise volatility triples, the drag will multiply by a factor of nine. It becomes quite severe. The move from leveraged ETFs to single stock ETFs, where I think in our paper leveraged ETFs, the underlier's volatility was averaged about 1.3% a day. And in single stocks, the underlier's average volatility was like 3.5% a day. The volatility drag went up by a very large factor, like seven.

Marco Sammon: I would say we measure this empirically. And this idea we have is the log return gap. We can measure the difference between what we expect the return would have been if we had never reset leverage versus this formula we have for the terminal wealth, given the daily reset.

And that's one way we have a really nice figure one in the paper, which kind of shows that as volatility increases, how this gap grows and you're going to see it's, there's curvature in the function. It grows faster as volatility gets bigger.

Dan Bortolotti: So it's a good segue into talking about the daily rebalancing, because this is something I think, well, as you know, has been kind of misunderstood, portrayed in misleading ways. So can you talk a little bit about what effect daily rebalancing has on volatility drag?

Chris Murray: This is fun because this one was close to my heart because I've sat by people who actually did the rebalancing of leveraged ETFs and watched it happen in real time, especially during a financial crisis. And that was something because there was a lot of rebalancing to be done. So if anyone makes a broad claim that leveraged ETFs always create volatility in the underlying assets, that I would say is false as a broad claim.

So there's no magical mechanism by which the existence of a leveraged ETF creates volatility. The mental model I would suggest people have is leveraged ETFs can create volatility when the aggregate rebalance required across all the leveraged ETFs exceeds the available liquidity in the stock. So what does that mean?

To get there, I would actually think about three steps. Let's say we have a stock like MicroStrategy and we want to say, is it possible that the leveraged rebalances in MicroStrategy are impacting the stock? So the first thing we do is we look at every single leveraged ETF that follows that stock.

The long ones, the short ones, there could be different issuers. We look at all of them. And for each one, we take the assets in that leveraged ETF multiplied by a special leverage factor.

That factor is going to be two for the 2x and six for the 3x. So that'll give us leveraged weighted assets tracking a given underlier. So let's say the 2x leveraged ETF has a billion and the 3x is 500 billion.

The 2x leveraged weighted assets is a billion times two. The 3x is half a billion times three. That gets you to three and a half or four and a half billion, whatever.

Next, you say, okay, how big is the rebalance? The rebalance is different every day. It depends on the move.

So on a random, today's Thursday, if the stock is up eight-ish percent, then the size of the rebalance is 8% times those leveraged weighted assets. And lastly, you say, okay, now 8% of whatever is rebalancing, is that big enough to move the stock? So you have to say, is this order of quantity sent to the close going to actually change the close price?

Here's the function of how big that rebalance is versus daily volume. If it's a few percent of daily volume, it could have a small few basis points of impact. It's only when you get much larger than that that it becomes problematic.

Think about a stock like NVIDIA, which might have, maybe there's half a billion or a billion of levered assets. Yes, that's a lot. NVIDIA trades $25 billion a day.

A little leverage rebalance is not going to cause a problem in NVIDIA. But if you look at some of the South Korean ETFs, if you actually do the math on some of those, I'm sure there were days where you were getting big percentages of ADV thrown into the close. And then yes, you absolutely can get an effect where you see the close price move a little bit.

What's really interesting about this is you say, okay, we've got all this rebalancing happening. We can do this math and say, this is when they're going to affect the close. How does this show up in performance?

Where am I actually going to see this in performance? Because leveraged ETFs only rebalance at the close. They're not buying intraday.

And they're not paying a spread to the close. If a stock closes at 100, they're not going to buy at 101. They're always buying at the close and selling at the close.

So what happens, and it's pretty interesting, is let's say random Thursday stock is up 8%. Leveraged ETFs have to buy a lot. And because they bought a lot, now it closes up 9%.

Their trading costs, their impact shows up, not because they pay a spread to the close, but because they make the closing price different than it otherwise would have been. So it's different from a counterfactual world where they didn't exist. And because they pushed the close price, now that daily return got bigger.

And it works both ways. So the magnitude of the daily return went from 8 to 9. And when we talked about VolDRAG, what's the formula for VolDRAG?

Well, the formula for VolDRAG is the sum of the squared daily returns, to be super precise. And that's multiplicative. So the causal chain is big assets in a leveraged ETF, big stock move on the day, large rebalance, larger magnitude move on the close, and the larger magnitude move on the close leads to higher volatility drag in that exponentiated variance term.

It's a really, really subtle way that trade cost shows up. And think about that compared to a mutual fund. If you say, what's the trading cost for a mutual fund?

A mutual fund is, well, the stock used to be 50, and then I bought it for $50 and 20 cents, and I paid 20 cents of trading costs. Easiest thing in the world. Leveraged ETFs are subtle.

It's because they actually cause the close price to change. And that feeds into this really weird quadratic variance formula these like professor guys came up with. But it works and it matters.

If closes are materially different because of this, it makes a big difference in wealth decreasing over time.

Marco Sammon: There's two things going on at once, because there's one idea to rebalance daily. And if we have volatility drag, you might say, well, why don't we rebalance weekly, quarterly? Or we can go the other way.

Why don't we rebalance hourly? And this is something that's being proposed right now. And I guess there's two things to consider here.

One of them is what's the probability that the fund is going to close? Chris has a great story of this, that if you have a two times leveraged ETF, they're not going to wait until the underlier is down 50% to close the product because the banks are going to get worried. But if you make the reset interval shorter, the chance that you hit that limit will also decrease.

The second thing is leverage drift. You want to buy what you think you're going to get. So if we have a stock that goes up in the middle of the day and then you buy that ETF in the middle of the day, you're not getting the leverage ratio necessarily that you think.

That leverage ratio moves around as the underlying moves around. Like Chris said, they'll reset at the close. That's the second thing.

But the kind of amazing thing, and this is again like the alchemy of what Chris and I have been talking about, is that imagine returns are independent. And which may not be true. Imagine they're independent and they're kind of small.

It turns out if that's the case, then changing the reset interval doesn't do much because we've lowered the volatility over each interval, but we have more intervals to have volatility over. And if returns are kind of independent, those two effects offset. Now imagine, however, if every hour when the leveraged ETF's rebalancing is rushing for the door, that people at the end of the hour, if it's up, start buying more.

Or if it's down, they start selling more. That could break this. And then that could make the volatility drag larger for the hourly reset products.

Chris Murray: There's one sort of subtlety that I think practitioners will appreciate, but might be news for your listeners, be they researchers or advisors, which is put yourself in the hands of a leveraged ETF provider. And it's actually impossible to rebalance exactly what you want on the closing price because you don't know the close till the end of the day. You need the close to know how much you need to rebalance.

So by the time you know exactly how much you need to rebalance, it's too late because the close already happened. Let me give an example to make it concrete. The markets close at 4 p.m. Eastern. And if you want to get an order to the close, you have to get it in a few minutes before. So if you're a leveraged ETF provider, you're sitting there five minutes before the close, you're like, well, it looks like it's up about 5%. I think I need to buy about $100 million.

You don't buy it. You send an order to your swap counterpart. You're like, hey, size this up by so many million dollars.

They do. But then by the time the stock closes, it's up another 30 basis points. You can't do anything because it already closed.

The actual mechanics of these things, it seems easy when you're like writing code to look at historical returns and just double stuff. But under the hood, it's pretty interesting.

Marco Sammon: This actually is a bigger point that I thought about. And it would be curious. This is true for anything.

It's true for regular non-levered indices. Because for example, imagine it's the reconstitution date. I know I'm adding some stocks, dropping some stocks.

And I have an idea of what my target weights are going to be. But I have a limited number of dollars. And if I'm going to put market on close orders, I have to respect my total AUM being invested.

There's nothing you could track perfectly. Just for levered ETFs, especially given this thing that the price will affect the size of rebalance, it makes it more dramatic. But it's kind of something I've been thinking more broadly.

Like when you design an index and you put dollars tracking it, you actually inherently make it impossible to track.

Ben Felix: Wild. So it sounds like what you guys are saying though, is that volatility drag from daily rebalancing, the way that it has historically been talked about is not so much an issue like mathematically speaking, but the actual implementation of daily resets could cause increased volatility in the underlying, which has a feedback loop to affect volatility drag.

Chris Murray: Yes, but in the very limited cases where the assets tracking the leveraged ETF are large relative to liquidity and there are large moves in the underlying. That's why these things can be a bit regime dependent because if it's a month when the underlying is moving 1.5% and then there's a crisis and the underlying starts moving 10%, that massively increases the rebalances. So it could be the case that there's a month where leveraged ETFs don't have much impact and then there's a month where they start to because of volatility.

Ben Felix: This is an assumption I'm making, but you can tell me if I'm right or wrong. This is probably more of an issue. You did mention that with Korean stocks, this is probably more of an issue with an LETF tracking a highly volatile thinly traded stock than it is with something tracking the U.S. stock market.

Chris Murray: 100%. But in a financial crisis, the levered rebalances on the market can start to matter because remember, you add them all together. You've got leveraged assets on Qs, leveraged assets on SPYs. And actually another subtle thing, which I should have mentioned at the intro, how do leveraged ETFs work?

A lot of academics look at the levered S&P 500 ETF and say, oh, it tracks SPY. It doesn't. It tracks the 500 S&P stocks.

And the leveraged Qs ETFs, it doesn't track Qs. It tracks the underlying 100-ish stocks. So the actual rebalances for the market at the end of the day, you can say, well, I've got 5 billion of leveraged ETFs tracking the S&P and another 3 billion tracking Qs and another 4 billion tracking TEMT index.

They're all buying the same stocks. Like there's a big overlap in the stocks they buy. So when you get in financial crisis mode, now you've got all these index leveraged ETFs buying all in the same direction with a high degree of overlap between the stocks being traded.

Ben Felix: I guess another interesting question is if this is an issue for the market, whether you invest in leveraged ETFs or not, but this isn't a downside of investing in leveraged ETFs. It's just an impact they have on the market, including everybody who's investing just in the market, not necessarily through a leveraged vehicle.

Chris Murray: Yes, but there's a point that saves you, which is that if I'm a long-term holder of the total market, if it bounces a tiny, tiny bit more on Wednesday and Thursday, it just doesn't matter to me. Whereas if I'm a leveraged holder, that tiny little bounce, and even if it's continuation, by the way, reversals or continuations, both have volatility drag. Whether the bounce is reversal or continuation, leveraged ETFs get banged up a little bit, but me, the long-term holder, I log into my 401k every three months and I'm like, eh, looks fine. And then I go and do something else.

Ben Felix: That's leveraged investors, period, right? Not just leveraged ETF investors.

Chris Murray: Yes, if there's people who took margin, I guess they're more likely to get a margin call.

Marco Sammon: But I think that what Chris is trying to say is that the leverage drag, and this effect that if we have like an additional pressure on the close that reverts the next morning, if you levered once and set it, that isn't necessarily a problem for you unless you get to the point that you're getting margin call.

Ben Felix: I see, okay.

Marco Sammon: And if you're someone who doesn't have leverage, you care about the terminal value and the beginning value, ignoring dividends. So that's, I guess, what Chris is trying to say. To add one more thing, like you said, maybe you're talking about like SK Hynix, there are some days levered ETFs rebalancing was like 36% of trading volume.

And for a long stretch, it was over 20%. Yeah, maybe that could have more of an effect. But those funds are also massive.

Their notional value is like around 1.5% of shares outstanding. I mean, they're humongous relative to the stuff in the US right now.

Dan Bortolotti: So if we zero in on this daily rebalancing issue again, I think you would agree, and maybe you can elaborate on how previous research and even regulatory guidance has gone wrong here. Because the idea, I think a lot of us, as I remember writing about these products years ago, and the conventional wisdom was the daily reset increases volatility drag. And that was a reason why these products were fatally flawed. Can you talk a little bit about that idea and its own fatal flaws?

Chris Murray: My take is if you just look at the equations, volatility drag doesn't depend on reset frequency. If you compare a weekly to a daily reset, the weekly is going to have five times more variance per period. You will have one fifth of the periods.

So under some reasonable assumptions, it'll look very, very roughly the same. I've always thought if there are disclaimers that say these should never be held for more than one day, frankly, that's just too absolute. Our research shows that pretty clearly.

The long-term returns of some of these leveraged ETFs and indexes, they just don't say that. It's also kind of silly because if no one holds them more than a day, they don't have AUM and they don't work. So I don't get how that would even exist as a product.

Marco Sammon: I guess to add on to that is where do we think people have gone wrong? It's that in our paper, we lay out some metrics we think are very intuitive. Like ultimately we think about what people care about is like how their dollars in these products grew.

Now, of course, people have other metrics they've looked at. For example, like expected terminal wealth. Well, you have expected terminal wealth.

You're taking an expectation. You have to have some data generating process. You're going to take draws from that distribution.

For example, this is an example that one of my friends, I was from NYU, we were talking about this. He had this example. So Tom, if you're listening, I got to shout you out here.

So I imagine I have a lottery ticket. It costs a dollar and it has a 1% chance of paying $108 and a 99% chance of paying nothing. So the expected payoff is 8%, which is just like the same on the stock market every year.

So the arithmetic average return over a long thing is going to be 8%. However, 99% of investors who invested in this thing would lose everything. What we're trying to say is that, like if you're looking at arithmetic average returns, given that returns compound, if I draw from the distribution a series of good returns, those things are going to compound.

And then when I take an arithmetic average of those things, that could still be a really, really big number. When Hank was on here, he talked about, you should also look at the median. He talked about the batting average.

And I think that's getting closer because in this example, the median investor who invests in these lottery tickets is also going to have zero. And that's going to highlight this. But we definitely want to highlight that this expected terminal wealth and arithmetic average returns are maybe not the best way to describe leveraged ETF performance.

Chris Murray: One thing I want to distinguish is that there are two ways to look at things. There's ex-post and ex-ante. Those are viewpoints.

Those aren't benchmarks. So even if you say my viewpoint is going to be ex-ante, you still need a benchmark. And if your viewpoint is ex-ante looking at the future, you can have a benchmark which is expected return or expected terminal wealth, or you can have a benchmark which is expected log return or expected log terminal wealth.

These are both very well-defined mathematical objects. You can just crank the math on these. They're just numbers.

You have a distribution, numbers come out. But unfortunately, from a language perspective, expected returns, the mathematical object doesn't really give you what sort of normal humans mean when they're talking about expected returns. And the mathematical object expected return is take a distribution, take its expectation, take the average across every single path, and then just return that average.

Expected log returns is do the same, but take the log of the terminal return on the path. Again, both valid mathematical objects, but we're going to point to some places where they give different answers to economic questions, both of which are mathematically valid. So one of them is, suppose you have two funds.

So fund A has a 10% annualized arithmetic average return. It's got 40% annual volatility. So in the past, it turned $100 into $102.

So maybe last year it had a 2% return. Fund B has an 8% arithmetic average return. So it's lower, but much lower annual volatility.

So last year it turned $100 into $107. So fund B had a higher historical return. When you plug that into the expectation, even though fund A, even though it only turned $100 to $102 and fund B turned it to $107, fund A has a higher expected average return and a higher expected terminal wealth.

The reason is it's just more volatile. Expected arithmetic return favors volatility. So in terms of ranking, expected arithmetic return gives a really weird ranking. It ranks a lower return fund above a higher return fund just because it has higher volatility.

Marco Sammon: But just to piggyback on that, just to make it crystal clear what Chris is saying, because he's 100% right, you can have a fund that has a higher average daily return, arithmetic average daily return, but more volatility and end the year with less. And so ranking those two funds, and that's like the lottery example, it could have had one amazing day and a bunch of terrible days and the terrible days are going to count more. That's kind of the issue with ranking on taking the average daily return.

And by the way, why are people focused on average daily returns? Well, these things are meant to be held for a day. And so that's kind of where this can go wrong. Sorry to interrupt, but I just wanted to make sure that that was crystal clear.

Chris Murray: The second example is this. So suppose I'm Chris Murray, the hedge fund manager. And suppose in a given year, I lost 15%.

That means I converted a million dollars into $850,000. And suppose I had 70% annual vol. So it's swinging around that year, I lost 15% at this point.

What's interesting is my fund actually had a positive average daily return. And if I translate that into an expectation for the future, I say, oh, my fund's expected arithmetic return is positive. So I write an annual letter, I say to my investors, great news, guys.

We did lose 15%, but our expected annual return is positive. And the reason it's positive is there's so much volatility under the hood that it drives the expected wealth to be positive. Intuitively, what's happening is when you simulate those returns going forward, you're saying like, wow, this fund was so volatile that if it happened to get the better returns, but not the worst ones, it would compound quite crazy.

And the even crazier thing is next year, if I lose another 15%, but I'm even more volatile, I'll be like, good news, guys. We did better than last year. Our expected annual return got higher, even though I just nuked another 15%.

The third thing that's a little weird about expected average return or expected terminal wealth as a benchmark is a question you might ask your client, which is how much leverage should I take to maximize my benchmark? Should I be in a 1x long? Should I be in a 2x long?

Should I be in 3x long? It's a pretty well-defined mathematical problem. Plug in L equals one, two, three, et cetera.

And if my benchmark is expected terminal wealth or expected average return, there's an easy way to optimize it. If the underlier is positive, the answer is infinity. Infinity leverage is always the answer.

Infinity leverage always gives you maximized expected terminal wealth. And expected log wealth doesn't have this problem. Expected log wealth, you'll get a totally reasonable answer that'll kind of sort of match what you'd get if you simulate it historically.

 Two, 1.5, 2.5, something like that. Those are things that in my mind, not at all saying expected terminal wealth is mathematically invalid. 100% real thing.

It's just that as a benchmark, it doesn't rank funds correctly. It gives weird answers to how to optimize wealth. I'd be careful assigning economic meaning to it.

And it's especially frustrating because as a word, it's great. As a word, if I say, expected log wealth has none of these problems. But if I go to you and I say, maximize expected log wealth, you'll say, what's a log?

I don't care about logs. I don't have a log utility function, it's weird. And we're not saying that log utility functions matter.

We're not saying some weird stuff like that. We're just saying that expected terminal wealth gives economically unintuitive answers to pretty reasonable questions. My last point on it is that there's a fix.

So there's a way you can fix expected terminal wealth or expected return. And that's just, you take the historical series, but instead of plugging in the series arithmetic mean to your expectation, you plug in the series geometric mean to your expectation. And once you do that, you just reintroduce volatility drag because the difference between geometric and arithmetic mean is volatility drag.

Last point is that expected arithmetic return introduces correlation as a thing that matters. In expected log return or final terminal wealth, correlation doesn't show up. So that's where anyone who's looking at this expected arithmetic return benchmark, you're going to see the correlation term show up there.

Marco Sammon: I think Chris, you hit it on the head. And then on top of that, this goes back to like an issue many people talk about evaluating leveraged ETFs. They talk about continuation, reversal.

And I think, yeah, we can look at the math, but just at a high level, the intuition of what Chris is saying is if we have a return of 10% and then a return of minus 10%, if we're compounded, we can just switch the order and it doesn't matter. We're going to end up at the same point. And so if we have expected log return inside that log, we can swap all the orders around and it doesn't matter.

Of course, correlation will affect the probability that we have a series of positive returns in a row or a series of negative returns in a row, but we can always rearrange the order of a series of returns and it shouldn't change the end inside the logarithm. And so that's another nice property of working with log terminal wealth is it takes out this autocorrelation. And Chris, also you should add onto this is that you did this exercise and I forget exactly where you tried to estimate empirically the effect of autocorrelation. Can you just kind of remind everyone of that?

Chris Murray: I don't remember the details because it was a while ago. We did see some negative autocorrelation during the crisis and then it went away, but we did a few regressions on actual realized leveraged ETF returns versus the underlier and correlation was never a relevant term in the regression. The other weird thing about correlation is it's been described before as kind of a rebalancing premium, but we would argue that that really can't be the case because correlation influences the expected terminal wealth of the stock as well as a leveraged ETF.

So if I just have a stock and I say, what's the expected terminal wealth of the stock? Correlation is a term that shows up for the exact same reason. It has to do with, it just increases the dispersion of the terminal price and that dispersion increases the expectation.

Marco Sammon: And if you have more autocorrelation, there's a chance that you're going to draw a few of those good, good returns in a row and then the distribution is capped at the bottom at zero and we're going to make the top higher and higher and then it's going to pull up the arithmetic average mean.

Chris Murray: I just thought live of a kind of cool example. So what if your autocorrelation is one? So every return is the same. So then basically you just draw one return once, you ride it forever.

So if you happen to draw like plus 20%, then all of a sudden your stock is worth more than the galactic economy in the year 2400. And because you're taking an expectation that just dwarfs everything. Whereas if you draw a negative 10%, your stock just goes to zero.

And if you average 2400 galactic economy plus zero, you get a big number. And I promise this will be the nerdiest section. We'll go back to kind of normal stuff after this.

Ben Felix: That was very nerdy. I think I get it. When you're talking about an expected value and you're using arithmetic returns, what you just said, Marco, you're going to have extreme values in there that are going to make the expected value look different than it probably should in an economically useful way. That make sense?

Marco Sammon: Yeah.

Ben Felix: Okay. We just talked about serial correlation and it sounded like it doesn't matter, at least in the way we were just talking about it. But does serial correlation matter when we're talking about leveraged ETF returns? Where does it matter if it does?

Chris Murray: I don't see it showing up in any of the work that we did.

Marco Sammon: I guess what Chris is saying is we looked at there's heterogeneity in realized serial correlation in the various leveraged ETF products. And so we asked empirically, is the relationship between realized performance of leveraged ETFs and estimated serial correlation? And we found nothing.

Now, like we said, if you're drawing from a distribution and that increases the probability of a run of positive returns, that will of course increase dispersion, increase the arithmetic average. But in the data, we did not find any evidence that empirically estimated serial correlation predicted differences in realized leveraged ETF performance.

Chris Murray: To be fair though, there is one place that it really could matter. And that's if you're saying, what should the reset interval be? If you're saying, should we reset daily or should we reset weekly or should we reset monthly?

If daily returns are just bouncing around a lot, but it ends up kind of flattish on the week, then it might be better to reset at a weekly than a daily interval. You would see that because when you actually computed the VolDRAG terms, the VolDRAG term says, how big are the moves between my resets? If you have big daily moves that cancel out between resets, then basically between resets, you're not losing that much.

Whereas if you have big daily moves that don't cancel out, then it's not going to matter so much. That's a good intuitive way to think about it.

Marco Sammon: Yeah, and it goes back to what we were saying is that, oh, if returns are independent, then the reset interval doesn't matter. But like Chris was just saying, if there's big reversals, then the reset interval does matter. Within the interval, then it matters.

Ben Felix: Interesting. Okay. Whether reset frequency matters or not, at least ex-post, if I'm understanding correctly, depends on serial correlation in the return series.

Marco Sammon: Yep.

Dan Bortolotti: Just to switch gears a little bit, I wanted to ask you about a term that you use in your research, and that is the break-even return. Can you explain a little bit about what that means and then maybe give us some examples of different scenarios so listeners can kind of get a feel for the concept?

Chris Murray: I can give some intuition. So in the research, we were not trying to answer the question, what's the best way to take leverage? That's not the question we were answering.

We were looking at, for a large number of individuals, they don't have access to margin. They're not going to trade options. They might have a view on some underlying asset.

You have a view on NVIDIA, you have a view on MicroStrategy, whatever you think is going to go up. So if I think an asset is going to go up, should I buy the asset or should I buy the 2x long leveraged ETF on the asset? What's weird is you can be right that the asset's going to go up, but the asset still would have been better than the 2x because the 2x lost from VolDRAG or whatever.

That was the question we were answering is, for a 2x long leveraged ETF to be useful, it has to do better than the underlying asset. Otherwise, why would it even exist? And that was where we came up with the concept of break-even return.

And we were saying, what return does the underlier need to achieve before the 2x leveraged ETF begins to exceed it? And that's always a positive number. I think, always positive.

So if the underlier is flat, the 2x is going to be down. If the underlier is up a little bit, the 2x is going to be down from VolDRAG. It won't catch it.

So the underlier needs a reasonably strong return to compensate for the volatility drag. And we haven't talked much about it, but the financing and the cost as well. Last point before I turn it over to Marco is, you can express the break-even in log terms or in simple terms.

That's just a different way to express the same thing. But conceptually, it's the point where you can say, this underlier did so well that the 2x or 3x levered ETF would have done better than the underlier.

Marco Sammon: And I think Chris is getting right to it, which is we say the importance of the benchmark really matters. And we'll come back to this when we talk about investor P&L, but we have this very simple benchmark, which is you could have bought 2x, 3x NVIDIA or you could have bought NVIDIA at the same time. And which would have done better?

And we like the hurdle rate because it's kind of like, you know, if you took my MBA corporate finance class and you think about like, oh, you're going to invest in a project. What's the hurdle rate? This is exactly that.

So I think that we can go through an example and maybe some numbers which will help put some structure on it. So like Chris said at the very beginning, leverage isn't free. And of course, also the cost of leverage depends on the risk.

But let's start with a simple example, like you have a levered ETF on a broad market product. So the risk-free rate, say it's 4%. And then we assume that in this case, a very simple thing, that there's a 50 basis point financing spread.

So you're going to be paying a total of 4.5% for each unit of leverage. Now imagine that this fund tracks something like an index. So something that has about 1% daily volatility.

Now in this case, the break-even return, the underlying stock has to be up, I think about 8.4% for the levered ETF and the underlier to have the same. It doesn't seem like much, but this is weird, right? You have a 2x that has the same return as the underlier, even though it went up.

Now it ramps up pretty quickly with volatility. So now imagine volatility is like 3% today. Now the hurdle rate is 32% a year.

Now imagine volatility is 5% today, like an NVIDIA. Now it's 100% a year. Now let's add another layer of leverage.

Now you got to finance that. How do you finance that? Well, you got to borrow and that's expensive.

For those, you could probably show the formula to the listeners. There's this like exponential term and inside the exponential, there's the quadratic variations, sum of spread returns, but there's also that drag from fees and financing costs. So the fees and financing costs are also going to multiplicatively decrease your terminal wealth.

So now you're paying fees and you're paying financing costs and you're financing more. So for a 3X fund with 5% daily volatility, the break-even return is 170%. So for your 3X return to beat the underlier, there has to be a return of at least 170%. When we saw that for the first time, who was the thinker?

Ben Felix: That is wild. If someone buys a single stock, leveraged ETF or whatever, thinking that they're going to get 2x or 3X to return the underlying, and it returns 4% and they end up losing to the underlying, it's like, oh, what happened?

Marco Sammon: Fees, financing costs and VolDRAG happened.

Ben Felix: How high are the fees typically for leveraged ETFs?

Marco Sammon: These fees we estimate for broad market ETFs are around 1%, maybe for stuff like crypto and volatility linked products, like 1.6%. But it's important to have, again, the benchmark in mind. If you buy VTI, you're paying three basis points. And again, over the course of five years or 10 years, these things could really be eating up your wealth, even if the underlier is flat and there's very little volatility.

Ben Felix: What are the mechanics of how leveraged ETFs themselves actually trade from a practitioner's perspective?

Chris Murray: I touched on a lot of this before, but some of the nuances, they aren't really trading. They're simply asking their banks to resize the swaps and the banks resize the swaps on the close. I kind of walked through that.

The one thing I didn't touch on, which might be interesting is, let's say that you have an underlying asset like the gold miners index, GDX. So GDX historically had a lot of leveraged assets tracking it relative to the liquidity of the underlying stocks. Remember, for your listeners, the leveraged ETF isn't tracking GDX, the ETF.

It's tracking the index of underlying gold miners. So let's say there's actually a lot of assets tracking this. That means when gold miners are up a lot, the leveraged ETF has to buy a lot on the close. And everybody knows this. This is public knowledge. It's not even like a tiny bit hard to find.

You can spend eight seconds on Google and figure it out. So there's a lot of people who are in the business of saying, oh, gold miners are up today. Right now is 2.30. Leveraged ETFs probably have to buy. I'm going to go ahead and buy a little bit of it right now because I know leveraged ETFs have to buy on the close. And then I can dump it to the leveraged ETFs when they buy. That's a game that I'm sure a lot of hedge funds play.

It's interesting because when people do this, when they buy, they push the index up more and pushing the index up more makes the ETF have to buy even more. It's this weird thing where you're kind of trading against somebody who's got gamma. And it can also unwind in spectacular fashion.

You can have it be the case that suppose GDX is up 10% on a given day. The market as a whole, remember no one's coordinating. There's a whole bunch of individuals making individual decisions.

The market's up, GDX is up 10%. People start buying because they think leveraged ETFs have to buy on the close. But then collectively they kind of buy too much.

And then GDX reverts a little bit. Now it's up 8%. You've got all these people owning a bunch of GDX thinking, oh crap, I thought I could sell it to a leveraged ETF.

But now they're not going to buy much. And then they start dumping it. And as they dump it, because they already pushed the price up too much.

Now it's 7%, 6%, 5%. Then it gets really nasty and the front runners lose a whole bunch of money. It's a pretty risky game.

Marco Sammon: Just two other things is that, you know, in fact, we've talked about this in the podcast before that this is a generic feature of any kind of these predictable rebalancing trades. Like it could be for index rebalancing. It could be for a regular add or drop from an index.

I can't stop you from buying SpaceX. You can't stop me from buying SpaceX. And if we buy too much and we all try to sell on the close, we might get nervous.

It's kind of like a prisoner's dilemma. Once the first front runner gets scared and they start selling out, you want to be the first one out the door. You don't want to wait till the end.

Chris Murray: That highlights something that I think is relevant for researchers looking at this is you might think, oh, I want to see how much the leveraged ETFs move the index. I can just look at the gap on the close because if they move it, it's just going to be nice and smooth till four o'clock when the gap's up. And that is not remotely what happened.

The market is very, very, very efficient. Anytime there's expected demand, that demand becomes reflected in the price earlier just through a whole bunch of individuals not coordinating, making intelligent decisions. And it kind of works on average, but sometimes doesn't.

So that's one kind of unique nuance of how they trade. The other is if I can touch on the Lucid example. So this is something that Matt Levine talked about, but there was, there isn't anymore, a 2x long leveraged ETF on Lucid.

Lucid is a highly volatile stock. And one day it opened down a lot on bad news. And the leveraged ETF, I think they just called the note intraday and the bank counterparty unwound it.

And you had this really weird situation where you walk in the day, you're long a 2x leveraged ETF on Lucid. By the end of the day, Lucid only closed down 16%. So opened down a lot on bad news.

Bank panics. The bank unwinds the note because the bank, I'm guessing here, I was not involved. The bank probably had an under margin swap and they got nervous because they see that the stock is down a ton.

So they're like, it's game over. They bang out of it. As the bank bangs out of it, they're pushing the stock down more.

Again, presumably, but that's just mechanically what's going to happen. And then they're done. They're done liquidating.

Stock bounces back a little bit. It only closes down 16%. But if you own the 2x leveraged ETF, you got a big zero.

To researchers who are looking at these things, it's really important to say when we're doing the simulation of what would have happened in a leveraged ETF. You can't just be like, oh, it closed down minus 16%. I would have lost 32% that day. No, you guys zeroed. You got nothing. That's relatively hard to model.

But this is obviously much more of an issue with single stock ETFs than it is with indexes. Has this ever happened within index? We're having a bad day.

I guess the last point is in a world where people who kind of, for lack of a better word, trade ahead of these rebalances exist. I don't know if the Lucid leveraged ETF was big, but it's conceivable that some people in the market could have been like, Lucid has a lot of levered assets tracking it. It's 10 a.m. It's down 40%. The bank is probably going to dump it. I'm going to short a little stock because I think it's going down more. Conceivably, that could happen.

I'm trying to kind of put together the theoretician looking at daily data, doing simulations, and the dirtiness that happens when people are managing risk in real life.

Chris Murray: Let's say there's a 2x leveraged ETF on a stock. So imagine I'm the ETF provider. I won't name one.

Someone gives me $100. I need $200 worth of exposure. I can buy the first hundred of stock, but the next has to be financed.

So I've got to borrow at A, the risk-free rate. So whatever the borrowing rate is, treasuries, Fed funds, it's all basically the same. And then I've got to pay a little fee to the bank that provides the exposure.

On the 2x, you're borrowing one times the notional. On the 3x, you're borrowing two times the notional. And you're paying Fed funds plus this little spread to the bank.

How do we guesstimate what that is? We don't have a way to know for sure. Those terms are between the bank and the ETF provider.

But if you simply look at the daily returns and you see how much do the daily returns lag the theoretical perfect expectation, then you can kind of guesstimate that a lot of what's in there is financing costs. And the reason this works is because the thing I explained earlier. Leveraged ETF trading costs are already baked into the closing price.

So they're not a separate component. If leveraged ETFs paid a lot above the close to trade, if they were paying a spread, then you'd have to say, oh, I don't know if it's financing costs or trading costs. Because leveraged ETFs' trading costs are embedded in the closing price, you can say with confidence, well, any slippage can't be trading costs. So it must be financing, expense ratio, and risk-free funding.

Marco Sammon: And to give an example of just how fast this could add up. Again, let's go back to our simple case that the risk-free rates are around 4%. You say 40, 50 basis point funding spread, 90 basis point expense ratio.

For like a broad index product, levered product, this is like 5.3, 5.4% a year. We estimate the costs are much, much higher for single stock leveraged ETFs. Now I think Chris's example provides a really good case of that.

If you're the counterparty on the Lucid swap, you want to be compensated for the fact that there's some possibility that this thing moves really fast and your swap is maybe under collateralized temporarily. And so you're going to charge a lot more. And so we find that on average, this all-in cost for single stocks is about 12%.

So let's take a step back from volatility drag and just think about the effect of fees and financing costs on terminal wealth over five years. This is not an eternity. This is just a few years.

And let's start with QQQ. So QQQ is still quite high for an ETF, about 20 basis points a year as a fee. After five years, you'd get to keep about 99% of the wealth, the index generated, and you give about 1% to the index provider.

Now for the 2x levered equity index ETF with the numbers I gave you, 4% risk-free rate, 40 basis point funding spread, 90 basis point expense ratio, that's going to add up to about 5.3% a year and then compound that. Remember, it's going to be compounding. We have this awesome case we teach at Tremblant Capital about this idea of if you can lower the fees, it makes a huge difference because remember, your wealth will be lower the first year.

And then even if you have a good return, it's on a smaller base and smaller base and smaller base. With a 5.3% annual fee, you're only going to get to keep about 76% of the terminal wealth. Now imagine TQQQ.

It's a three times fund. And using the same assumptions, we find out in fact that you would pay 40% of your wealth to financing costs and fees over just five years. It grows really fast because of the compound. And that's what Chris was saying. It's multiplicative. In that formula, you'll see it.

In the exponential, costs are there and it multiplies the whole squared return of the underlying asset.

Chris Murray: Some of this is why a very low leveraged ETF on a broad index is so interesting. Because if you had a 1.25x leveraged ETF, now the financing costs, you're not financing a dollar per dollar. You're financing a quarter per dollar.

Your financing costs are roughly a quarter's big. You have effectively no extra financing costs for blowing up. You basically aren't going to go to zero.

And your volatility drag, if you do the math, it's like 80 some percent lower. This volatility drag is super linear in leverage. Very low fee, very low leverage ratio ETF on broad index would be a really interesting product.

Ben Felix: They are interesting. The fees can still be a challenge, even when they're low, but there's a product like that in Canada. And when you account for the fee on the fund and the internal financing costs, they use cash leverage in this case. I think I found you're about 60 basis points over the cost of using margin.

Chris Murray: It's similar.

Ben Felix: Is that expensive or cheap? I don't know. You're paying for convenience, I guess. But if they dropped their fees by 10 basis points, it would be about the same as margin.

So I've asked them if they'll do that. We'll see if they listen. How do financing spreads and therefore financing costs vary across all the different leveraged ETFs?

Chris Murray: The big trend I remember is just single stock versus index. We didn't estimate it for things like crypto because you would need the underlying data to estimate it. So things like the leveraged ETF and oil futures or something like that, we're not going to try and estimate financing costs or God forbid a leveraged ETF on the VIX, which is something else entirely.

Marco Sammon: We have something like 10% a year for single stock, which is well above the risk-free rate.

Ben Felix: Yeah, it's crazy. I think it was 9.8% on the cap weighted portfolio of single stock ETFs, if I remember correctly.

Marco Sammon: Yeah, that's right.

Ben Felix: And that's the spread. That's on top of the risk-free rate.

Marco Sammon: And then compound that for two or three years and how much of your terminal wealth you have left.

Ben Felix: Plus the volatility drag, plus the fee. These don't seem like very good investments. I don't know.

Chris Murray: What's crazy is they still generated positive wealth for investors, if I remember, even versus the underlier on average. I think some of that might be when you get these home runs from the NVIDIAs that convexity bonus, that kind of plus 100%, plus 200% that can undo a lot of damage. The problem is you need it in the future, not just in the past.

You can't just hit the one home run. You need to hit the home runs every year to offset the damage.

Ben Felix: But at a certain point, it's like, just buy a leveraged index.

Chris Murray: Yes, eventually NVIDIA will be the index.

Dan Bortolotti: Just to pull these numbers together. So, cause we've been talking about a couple of different elements. Can we estimate a range?

If you add up the risk-free rate, the spread, the typical expense ratio, I realize this is going to vary a lot between index ETFs versus single stock ETFs. But if you can give us kind of a single number of what the total cost you might expect to pay to own one of these ETFs.

Marco Sammon: I think based on our estimates for the broad index stuff, it's like around five, 6%. For the single stock stuff on average, all in with the spread plus the fees, 15, 16%.

Ben Felix: Yeah, it's wild.

Dan Bortolotti: Yeah, that's a pretty big hurdle.

Ben Felix: And that's not including volatility drag effects. Like that's just the cost.

Marco Sammon: Yeah, all those numbers where I said, you're only going to get to keep 60% of your wealth are not net of volatility drag. You're keeping 60% of your wealth. If there was no volatility drag, just paying the fees and financing costs.

Ben Felix: Yeah, it's crazy. I mentioned the example that I've looked at with the 1.25 times leveraged ETFs in Canada. For the stuff that you guys looked at, how competitive do you think the financing costs and leveraged ETFs are when you include the fees, the higher fee of owning that ETF relative to just like an index fund, or I guess a stock. How competitive do you think the overall cost of obtaining leverage through this structure is?

Chris Murray: Compared to margin or compared to no leverage?

Ben Felix: Yeah, compared to other forms of leverage, whether that's margin or whatever else.

I guess margin is probably the best example for a retail audience.

Chris Murray: So for retail, my guess is futures and options. I haven't looked at this, probably give you the cheapest leverage because they're just institutional products. The one thing I defer to you guys on is taxes.

So that's the one place where I could say, well, if you're paying 6% margin, can you write that off versus your investing gains? Is there any weird tax thing? And same thing with futures.

If I'm long futures, but they're rolling, so I'm paying taxes every year at the futures as opposed to a leveraged ETF that I can just make a cap gains in 40 years or give to my heirs, taxes can be a really big deal. That's where I'd put a big asterisk in any comparison that we make.

Marco Sammon: And I would add to that, I don't want to say too much because this stuff is under heavy scrutiny, but some of these new tax aware strategies set up an LP for an individual, structure the LP as a trader, and then swap financing costs can be offset against ordinary income in the United States. And so this can break normally, you can only offset up to $3,000 of ordinary income. But when you structure it this way, you can now make the swap financing costs go against your income.

And now it unlocks a whole gold mine of tax deferral and reduction strategies. So yeah, this is a very important big asterisk about whether you can write that swap financing costs and how long that will last.

Ben Felix: That's interesting.

Chris Murray: I would guess if you have access to it and taxes aren't the problem, my guess would be that futures are probably the cheapest way to do it to gain leverage, just because futures are institutional. So the funding is set by a competitive market.

Dan Bortolotti: So if we change gears again a bit to get back to the single stock ETFs, which have been proliferating in the marketplace, can you talk a little bit about what types of stocks leveraged ETFs tend to get launched on?

Marco Sammon: And this goes back to the very beginning of the discussion, which is why have these things become popular? And if you believe people have a preference for lottery-like payoffs, unsurprisingly, Chris and I find that the median underlying stock that gets levered ETF is around the 94th percentile of past volatility and 92nd percentile of past six months return. So these are extremely volatile recent winners.

And by the way, this is a broader property of products that get launched. So for example, Zahi Ben-David has this great paper, Competition for Attention in the ETF Space, which shows that there's a bunch of indices that index providers make up, but don't have any assets tracking them. And then when those indices do really well, all of a sudden they launch a product on them.

Of course, then those products end up doing pretty badly, but this is like a general feature of the fact that people launch things on recent winners. And here in particular, the idea of magnifying a gain on a recent winner seems very intuitive from a marketing perspective.

Chris Murray: What's funny is while we were working on this on various forums and stuff, I would start getting advertisements for the SpaceX levered ETFs. There'd be one that said, do you want to be double long or double short? And they were just popping up.

I guess my trackers knew that I liked levered ETFs and I thought I might want myself a bit of SpaceX, which I mean, I guess technically that's a recent winner because it went public above its pre-IPO price, but it's definitely a volatile one.

Ben Felix: Which funds that launch attract the most assets?

Marco Sammon: It's going to be the exact same thing. Chris and I have this regression in the paper where we're going to look at which things gather assets. And it turns out, even though this has launched on volatile recent winners, among those, the ones that are even more volatile and even more winners are the ones that end up gathering assets, which again, perhaps is unsurprising, but that's what happens.

Ben Felix: Yeah, that's wild. Just in thinking through how this market works, do you guys think, based on the work you've done in this space, that this creates a conflict between the issuers of these products and investors? Because we talked about how damaging volatility is. Those are the launches that are picking up assets. That to me seems like a bit of a dicey situation.

Chris Murray: I get what you're saying. It's fun to launch on spicy stuff completely. I wouldn't think of it at all as malintent from the issuers.

If they want chicken, broccoli, and brown rice, then people will give them chicken, broccoli, and brown rice. Look, maybe if these were marketed to Bogleheads, then nobody would be buying the SpaceX one and they'd be buying, like me, buying the 1.1X to S&P.

Marco Sammon: I guess I'm going to get on my soapbox a little bit here for a second and talk about a few things that I think are going to seem not related, but are going to be related. I teach this MBA corporate finance class and we talk about the idea of equity and option-based compensation. And we have this awesome case where we're like, look, you're starting out at this startup and your employer says you could swap $100,000 of your salary for options.

Now, of course, the key lessons of the case is that, well, you have options on ordinary common stock. The private equity company that's funding you has options on preferred equity. And so they're senior to you.

And so it turns out your options are not as valuable as you'd think they'd be under the right assumptions. However, there's nothing that protects them, the employees, from being made this offer. And so I say in the class, at the end of the class, look, we've shown that basically you're paying $2 for an option that under very generous assumptions. Now we're ignoring everything. Diversification. We talked at the beginning.

You're now holding risk that's correlated with your employer. That should be given another discount. You're holding something that's not tradable in the secondary market.

That should be another discount. I say, why not go out and buy a NASDAQ 100 out-of-the-money option? If you just want some fun, some risk, you have some preference for a lottery ticket, why not buy it that way? It's traded on the exchange. Like Chris said, it's a competitive price. You can retrade it. It's diversified. It holds a whole bunch of things. And everyone's like, no, no, no.

I don't want to do that. This is going to be a unicorn. This maybe goes back to Hank's point about overconfidence that he talked about on the podcast.

But I guess there's nothing that stops the funder of the company from offering people these options because they want it. And it's like Chris said, if they want to YOLO on the startup they're in, great. They can do that.

I guess the second thing here I want to go with is that there's a competition for attention in this space. So now we have PolyMarket. Price of Bitcoin in 15 minutes.

S&P 500 in 15 minutes. We have digital options, binary options, all this kind of parlays. We're living in a world where we realize that like with the airline, if I want to bring an extra bag, I've got to pay.

If I want a seat that has a slightly more recline, I've got to pay. We could now go deep into the microeconomics of when should I bundle things together versus when should I separate them out. But this seems to work really well in finance.

And again, the leveraged ETFs have to compete with PolyMarket and Kalshi. Maybe that's why they want hourly reset leveraged ETFs or whatever. The place where I think this goes wrong, and I would love to hear what you think about this, is when things that are very different look the same.

Now you go on your trading app on your phone and you can buy Apple stock. On average, Apple stock is going to earn the equity premium. That's going to be good for you.

Right next to it, you see the option to buy an option on Apple stock. This is a bilateral contract between two people that is not going to earn the equity premium. Now on top of that, you see a digital option that's going to be priced because now this is probably not going to be fairly priced.

I've looked at some of this stuff and there's Indira Puri at NYU has shown that these digital options are not priced competitively. That's going to be even worse. But when I'm looking at my phone and seeing, oh, Apple stock, Apple option, Apple digital option, these things all look kind of similar, but one of them makes sense for the long run with the equity premium better than one of them doesn't.

And that's kind of where I think there could be something going not great. For investors, if that makes sense.

Ben Felix: Yeah, it does.

Chris Murray: It's like offering them on a brokerage platform gives kind of an implicit stamp of approval. It's not explicit, but it's kind of implicitly like, you know what? Your sports parlay that you can buy in your brokerage thing is kind of the same as your Vanguard index fund. I'm sorry, it's just not.

Ben Felix: They're in the conversation though. Prediction markets, because they're on those platforms, they're in this conversation about what should be in your investment portfolio and they shouldn't be. They shouldn't be even be in that discussion, but they're there because they're present.

Chris Murray: I'm curious if you get that question from your clients, like, hey, how much should I allocate to sports? It sounds weird to say, even the fact that we're having this conversation. Hey, advisor, how much should I allocate to sports betting? That's just a weird sentence in the context of actual finance.

Ben Felix: We don't, we don't get that question. We did field a lot of questions about crypto when not so much recently, but when that was becoming a thing, we answered that question many, many times. When Cathie Woods' ARKK fund was really taking off for a period of time and she had a whole narrative about why traditional financial markets were basically broken.

Dan Bortolotti: Well, it's funny. I did an interview with somebody not long ago when they talked about the potential launch of these ETFs that are tied to individual NHL teams. I don't know if you guys have heard about these.

And then they said to me, like, does this blur the line between gambling and investing? I'm like, it's no line to, like, it's a very, very thick line. There's no blurring here.

One is gambling. One's investing. Just because you wrap up gambling in an ETF doesn't change the fundamental nature that it's just gambling.

So I think you're right. When you trade them in these conventional ways, it does give this air of credibility around them. Not necessarily putting leveraged ETFs in the same category as sports gambling, but there is this idea that ETFs are an investing tool and yeah, a plain vanilla index fund or a triple leveraged ETF, they're kind of the same thing.

Clearly, I think for a lot of investors who don't have the sophistication to understand the subtleties, maybe there is a bit of blurring there.

Marco Sammon: I do want to add one point here, which is interesting. We haven't talked about it yet is inverse funds. We talked about what's the purpose of these things.

Now, I think people who work for these prediction market things will say, oh, well, you can hedge, you know, right? You make World Series apparel for Yankees hats. I'm like, you're worried the Yankees are going to be knocked out of the playoffs so you can hedge the Yankees losing. I'm like, okay, maybe.

Dan Bortolotti: Too late, by the way, it's too late. Now they are out of the playoffs.

Marco Sammon: They should have hedged. They should have been buying those contracts to protect themselves. And you could say, oh, well, you know, I really want to bet on an FOMC announcement.

So I need this exact choice exposure, fine. But Chris and I show, and we don't belabor it in the paper because we imagine that inverse ETFs are likely used for hedging. Maybe you have something you're long and you want to protect yourself and so you're going to buy the inverse fund.

We found that over our sample, there was $93 billion, including launches of flows into inverse ETFs. And now they have 13 billion. So 86% of the capital in inverse ETFs has disappeared.

Now, again, it could have been offset by other pieces of those people's portfolio, but we should mention the fact that the volatility drag and everything we talked about, all that applies on the inverse as well. And so it could be offering a targeted debt or it could be vaporizing capitals, Chris would say.

Dan Bortolotti: So what are some of the ways that investor outcomes in leveraged ETFs can actually be measured? And what does each of these measures tell us specifically?

Chris Murray: We talked about expected terminal wealth for a long time. So I'm not going to belabor that. One thing we can look at is just the fund returns, the cumulative return of each fund.

And that can be either express, normal or log. The other thing that we look at in the paper is how much money do investors actually make? It doesn't matter if a fund went up a thousand percent, if investors got in when it was up two thousand percent, and then they get out when it was only up a thousand percent, they lost money.

I think a lot of the punchline of our paper is more about these investor outcomes, which combine both the raw fund returns and the timing that investors use when they put money into and out of these funds. Investors' net performance can lag the fund's net performance in two ways. One is they can get in late and miss something or even lose money, and then you can say, oh, that's bad.

Another is they can just get in early, make a ton of money, and then pull out before future gains happen. And that's something that we've seen as well. That was one of the biggest drivers of some of the negative investor timing effect that we've seen.

It wasn't that people lost a ton of money. It was that they made a ton and then they just started pulling money out and then the fund just kept doing very, very well. Just the fact that investors have negative timing, we don't want that to be seen as, oh, bad outcome.

Marco Sammon: What I think Chris is saying is that we can imagine for each time a dollar goes into the levered ETF, we identify that, and we imagine the counterfactual where that same dollar went into the underlier. And we can compare the relative performance of those two things. I'm going to give some numbers in a second, but the timing thing is, well, you could imagine when did the dollars go in versus what if I had almost randomly, within the lifetime of the fund, reallocated when that dollar went in and how would I have done?

Going back to what Chris said, for the broad equity index ETFs, if we had looked at when the dollars went into those and put them in a counterfactual, investors got an additional $50 billion over our sample by being in the levered index products versus being in the underlying. That was surprising to me is that everyone says, all the headwinds we talked about, volatility drag, fees, financing costs. Well, it turns out the market went up a lot and investors were in these things at not a terrible time.

They didn't buy in January 2020 and sell in March 2020. They were in a not a terrible time and they generated an extra $50 billion for themselves relative to being in the underlines. The gap is much smaller for single stock levered ETFs.

They generated about $13 billion for themselves versus $12 billion if they had put the same dollars in the underlying at the same point in time. These things are levered and so it's surprising that the gap is that small and that's, of course, all the factors we talked about, but it is important to say that at least over the sample that we saw, they weren't terrible for investors.

Ben Felix: On average, but that's that skewness thing, right? We can say that single stock ETFs on average in the sample were okay, but I think there's a ton of skewness in that result.

Chris Murray: Kind of. Our results are all in dollars. It's all in how many dollars investors made.

It's real money in investors' pockets. There's nothing theoretical. It's literally like investors put in $50 billion and now they have $100 billion. If it's skewness, it's sort of ex-post skewness that was realized and the money's in the bank.

Marco Sammon: To say what Chris is saying a different way maybe, sorry to interrupt, is that maybe it could be that there's a small number of people who made a lot of money in these and a large number of people who've lost a small amount of money in these versus a bunch of people who made a medium amount of money. That, Chris and I, cannot distinguish between, but we are saying that, yeah, in terms of you literally take the dollars that went into these funds at the time the dollars went in and you track those dollars relevant that they put in the underlying, that's the difference. That $13 billion is what they got.

Ben Felix: That makes sense. I guess I'm just thinking, you explained it. That could have been a few people buying NVIDIA leveraged ETFs and a whole lot of people losing money in other ETFs, but because NVIDIA did so well, it looks pretty good.

Chris Murray: One nice thing about this is I like to think of myself as an objective researcher, but you go in with a prior. I didn't start thinking, oh, leveraged ETFs will have made not only many tens of billions for investors, but tens of billions above and beyond the underlier. I'm the person who was sitting on the trading desk watching these things move around in the financial crisis, but you go in with a prior and you do work and like, the prior was wrong. That's fine. It was enlightening in that sense.

Ben Felix: Yeah, it's super interesting. Morningstar has an article that not in the way that you guys did, not in the performance evaluation metric that you just described, but they just looked at the performance relative to the underlying, not with investor flows or anything like that. They found that 19% of single stock ETFs have lost over 75% since inception and 18% outperformed the stock they track. It's pretty bad.

Marco Sammon: Yeah. It's important to weight those things by dollars because there could have been a bunch of tiny leveraged ETFs that didn't do well.

Ben Felix: Yes. It makes sense. Asking how investors did, it's definitely more relevant to look at it the way that you did it. Asking whether leveraged single stock ETFs are expected to be good investments. I don't know.

Marco Sammon: I think what you're saying is if we pick a random stock and launch a leveraged ETF on it, how should we think about what's going to happen?

Ben Felix: Right. I guess your results might show that investors might pick stocks that are going to go up. Does that make sense? More than not?

Chris Murray: It might be biased because they all went up during the period.

Ben Felix: Right. Okay.

Chris Murray: If I had to guess.

Marco Sammon: You're doing a layer of like issuers endogenously decide to launch leveraged ETFs on some stocks. In our short sample of three years when they were doing this, they happened to pick some really, really good ones.

Again, I keep calling it out because everyone should watch Hank's episode on leveraged ETFs. Amazing that the average stock in the market underperforms treasury bills. So in that sense, if you picked a random stock and launched a leveraged ETF, it'd be terrible. However, it just so happens that the ones issuers decided to launch on over our sample did well.

And by the way, those things also attracted a lot of assets. And so that ended up being good for investors, but definitely might not be true going forward.

Ben Felix: That's exactly where my mind was going.

Chris Murray: That's going to be interesting when we do an update and see how things worked over the last year.

Ben Felix: I want to ask about pre-sample too. So your sample starts in 2006, at least for the leveraged index ETFs. How does leveraged index fund performance look prior to your sample period?

Marco Sammon: It's funny that there's not that many super long run levered products, but we actually did find two levered mutual funds. I don't have the tickers off the top of my head, that were launched in the late 90s. When we plotted them or we have a note that's going to come out and hopefully by the time the podcast comes out, everyone can see this.

We show the cumulative performance of these things from the 90s to today relative to the underlying asset. And they look not that good along the NASDAQ 100, even though the NASDAQ 100 has been up a lot. Now, what happened?

These things were high fees. So these things had over 1% annual expense ratio, plus expensive financing. And you compound that over 30 years, you already have a massive structural headwind.

And then on top of that, they went through the tech bust in 2001. So you have two things, one giant drawdown, which is hard to recover from, combine that with high fees and over the long run. And that's a super tough headwind to overcome.

Ben Felix: So interesting. The ticker is ULPIX for the S&P 500, not for the NASDAQ. When you look at the chart over time, if you had invested in that when it launched, you mostly trailed just SPY until basically the last few months recently.

You just now pulled ahead. So you spent many, many years trailing the underlying and just recently pull ahead. Like you said, it's fees, but then the financing cost piece is so interesting.

I don't know. I wouldn't have really thought about that, but 2006 to now, maybe less so now, but 2006 to recently, it was a period of pretty low financing costs. And so you take that plus the high returns of the S&P 500 over that period or the NASDAQ.

And you look at some of these products, it's mind blowing how high the returns have been. But it's also, it's like a very specific set of circumstances over that period that allowed them to do as well as they have. It's not obvious to me that people should extrapolate from that.

Chris Murray: The financing costs are a big deal. If you go from risk rate of 1.5 to 4.5 over 10 years, an incremental 3%, that crushes you multiplicatively. So that's an extra what?

I can't do the compounding in my head, but ballpark, and maybe 30% of your wealth that's gone. And then for a 20, 30, 40 year investment, it's more than half of your wealth.

Ben Felix: Yeah.

Dan Bortolotti: Just to tie all of this up and we'll give each of you a chance to answer. You touched on it a little bit, Chris, when you talked about your priors going into the research.

Chris Murray: I think broad-based, lower leverage, index leveraged ETFs could be fantastic. I've said before, but I think a very low leverage S&P 500 index would be fantastic. I would happily suggest that my daughters put some in it.

I never suggest any investments for any other people, but for my daughter, I think I could talk to her about it. The higher leverage ones, the things that we just brought up about financing costs, I'd be a little bit questionable long-term. Is a 2x leveraged S&P going to beat plain old super cheap S&P over the long run?

Maybe, but with higher financing costs, the hurdle gets a lot higher. For regulators, I don't really see low leverage as a problem. I'd be a little concerned about the daily resets.

If I was doing regulatory stuff, we didn't touch on this too much, but one of the nice things about leveraged ETFs rebalancing in the close is the closing auction is huge. Now it's probably like 10% of ADV. There's tons of HFTs who come in to provide liquidity.

It's easy to trade there. If, however, you're trying to reset at 10 a.m., you walk in, the market's down 20%. You've got to rebalance at 10 a.m. so you offload over 10 minutes, and you've got to sell a bunch of stock, that could be a catastrophe. And the problem is, it's the kind of catastrophe it doesn't show up the day you launch. It shows up a year and a half later. Then after that, you have the issues.

Marco Sammon: And just to build on that, the closing auction is an auction. Like Chris said, you can submit a market on close order. There's no guaranteed 10 a.m., five minute before 10 a.m. time weighted average close price auction business. You're going to have to go out and trade this. Now it gets into exactly what Chris said before is, if everyone starts running for the door in those last 10 minutes, that's, of course, going to change things. And there's no way to have a guaranteed way to trade at that price so they could have more track in Europe.

I agree. Just to jump on this, I think that my thing has always been, for a very old school reference, those who like the three stooges, there's this episode where like every time Mo hears Niagara Falls, he goes crazy. And that's like me with fees.

I just got to tell a great story. Vanguard launched VOL, the oldest retail index fund, about 50 years ago. Does anyone here on the call know if you had bought one share, it's $10,000 in 1976, what would it be worth today? That one share? $3 million.

Dan Bortolotti: 50 years of compounding on the S&P 500?

Ben Felix: $3 million.

Marco Sammon: Yep, exactly.

Ben Felix: Wild.

Marco Sammon: My dad was 26 years old if he had bought one share of VOL, the mutual fund share class version of it, for $10,000 in 76, he'd have $3 million today. And of course, the market has done well. But on top of that, you paid a very low fee for a very long period of time.

You pay for that service to have the easy exchange-traded access to a levered product. But for the long run, I don't quite see it.

Ben Felix: Does mixing a 2x leveraged ETF with just a regular ETF, can you get to a lightly levered position that way? Like, does that still work? Or is there some nuance there that makes it not work?

Chris Murray: Probably close, but off the top of my head, my guess is it's not exactly the same. I'm not sure. It's a good question. We probably should work out that math.

Ben Felix: I tried it with just like a very, very, very simple back test. I did exactly what I just described with some Canadian products with those 1.25X levered products that I mentioned and a 2x product mixed with just a regular ETF. They haven't been around super long, only for a few years, but I was within a few basis points in annualized returns.

But I don't know if that was just that specific period and there's something I'm missing in thinking about it.

Chris Murray: I guess it's up to you how to rebalance it then. If you're kind of under your 1.2x target, do you do it monthly or annually? It's a really good question.

Marco Sammon: So I was going to say, it's like the opposite is like you could have a 60-40 stock bond portfolio, right? If stocks are up, you're going to have to sell stocks. How frequently do you do that?

And like, does that help you or hurt you? And how correlated are stocks and bonds? And how often you rebalance at the aggregate portfolio level to get back to the 1.25X leverage, I think is going to be the key thing here. So I would love to see what you did and we can play with it ourselves a little bit too.

Ben Felix: I can send you my very simple data later. I did play with different rebalancing frequencies just to see, and I don't remember there being a huge difference. We can chat more later.

Chris Murray: I didn't have a prepped answer for that. I thought I'd try and do it on the spot. First, like family versus work stuff, family is always just categorically higher.

I've got three daughters and a wife, so being a good husband, good father, it trumps everything career-wise. An observation I've had, I was on Wall Street a long time, is it's very extractive, not in a bad way, but just so much money between, if you take investor returns going up, so much ends up going to Wall Street. If you just look at net aggregate trading profits of all the big banks, it's just a mind-blowing number.

If through education like this and some other things that I'm doing, if we can help investors keep more of that, I think career-wise, that's a win for my professional life. The personal non-professional life, it's a family first. I like exercise and staying in shape, so staying healthy as I get older would be a big win.

Ben Felix: Great answer. Marco, have your views on success changed since the last time we asked you that question?

Marco Sammon: No, not really, and I think I love Chris's answer, and I think that it's been really great to be on the podcast. Chris and I have thought a lot about this for a long time, and being able to share, you know, as I said, we had a lot of realizations doing this project. The convexity boost, our patented convexity boost, the fact that some levered products have delivered good returns for investors, the fact that a counterintuitive thing of launching on recent winners actually hasn't been that bad.

Ben Felix: Awesome. Well, I'm glad you guys wrote this paper. I had started researching the topic, and I just, in a regular Google search, I found your paper, and I was like, no way, because obviously we'd had you on the podcast a couple times already, Marco, so I was very excited to see it, and it's been super cool to watch it go through its iterations, and now to talk to you about it, it's awesome.

Marco Sammon: Well, thank you.

Chris Murray: Thank you so much for having us on. The key is it's not just publishing, but the opportunity to sort of get this out there and get people like yourselves, your clients, and your listeners informed. It's huge, so thank you.

Ben Felix: Awesome. Thanks a lot, guys. We really appreciate you coming on the podcast.

Marco Sammon: Thank you.

Dan Bortolotti: Thanks for sharing your work.

Chris Murray: Thanks.

Ben Felix: Well, Dan, as I said in the introduction, it's got to be up there with the nerdiest episodes we've ever done.

Dan Bortolotti: Yeah, I feel privileged to be a part of it. As someone who does not have an advanced math background, a lot of that went over my head, but I think, as always, we try to bring the guests back to a point where we're talking about how this is going to affect everyday investors and potentially advisors. But I think there's an audience here, probably includes some researchers as well. I'm sure that they got an extra level out of the discussion.

Ben Felix: For sure. Researchers and non-finance researchers who have a predisposition for math and equations and thinking in formulas and expected values. I think speaking about levels, it's great because I often hear from people who have expertise in some different field, how much they enjoy applying just advanced thinking.

I don't know if that's the right description for it, to finance, because it makes it relatable to somebody who has expertise in some other quantitative or technical field.

Dan Bortolotti: Yeah, and I think in this case, these products have been quite misunderstood. We talked about this on our previous episode when we discussed leveraged ETFs. That includes us.

I think we had a lot of misunderstandings about how they worked in the daily resets and the dangers supposedly of holding them long-term. I think they just had good instincts and sort of scratched the surface and said, I think a lot of this stuff won't hold up to scrutiny, so let's do that. And they had the math horsepower to actually do it. And I think some of the insights were really interesting.

Ben Felix: Oh, it's so cool to think about which of the things that they're talking about apply to leverage, just broadly speaking, and which of them apply to the daily resets that many people used to be so concerned about with leveraged ETFs. And they had talked about the convexity boost that they sort of discovered, or at least they're now going to popularize. That was super interesting.

And just interesting to think about how these products may or may not fit into investment portfolios. I mean, even there were some comments that each of them made at one point about taxes and how taxes play into all this stuff and whether the type of financing that you're going to get in these funds may not be tax deductible. And so for a taxable investor, there's a whole other layer of considerations.

I thought that part of the discussion was really useful. And then just the philosophical side of all of these single stock leveraged ETFs that are being launched and whether that's a good thing. I find it hard to argue that it could be, but it's also hard to argue that choice is bad, but I don't know, maybe not all choice is good.

Dan Bortolotti: Yeah, well, overwhelming choice, I think has often been proven to be detrimental. I think it is going to be interesting to see how this product space evolves as people learn more and more about how these products work. Chris, for example, came back a couple of times to talk about a type of ETF with very modest leverage.

Nevermind this 2x, 3x, 1.1x, which is quite modest, very low financing cost. And this could conceivably something he said himself that he would be comfortable holding it in his own portfolio or recommending it to a family member. I think it's at least worth seeing how popular they become.

Ben, you mentioned that there are some products in Canada already with one and a quarter. I don't know. I mean, that seems to me less of a speculative product and more of something that is at least worth a conversation in a traditional portfolio.

Ben Felix: I agree with all that. We talked about this a little bit during the conversation. The challenge comes down to fees, as is so often the case with financial products.

I think the fees can very easily make the overall financing costs of those products uncompetitive with just borrowing yourself. And so unless there's some constraint, like the type of account you're in, which is real thing, like an RRSP or a TFSA in Canada where you can't use margin, those can make a little bit more sense. The tax deductibility of interest or borrowing interest is another one.

In the case of those products that you're mentioning, Dan, they do use cash borrowing. So there is actual interest that can be deducted from the income inside the fund. This gets a little bit technical in a different direction than our conversation with those guys.

But if you have a Canadian equity ETF with leverage inside of it, you're deducting the interest against dividend income, in which case you would have probably rather had the interest deduction outside of the ETF and receive the full, you know what I mean?

Dan Bortolotti: Yeah, because of the dividend tax credit, you mean?

Ben Felix: Exactly. So for non-taxable accounts, these are probably more interesting products. But to your point, Dan, about how interesting they'll be to the market, there are two of these funds that exist in Canada with a 1.25 times leverage, and they're tiny in terms of assets under management.

Dan Bortolotti: Probably poorly understood still by people. And I don't know, I feel like if you're the type of person who wants to use leverage in an ETF, you might as well go all in and do two or three acts. The idea that I want to use leverage, but I want it to be modest is a prudent strategy, but maybe not one that attracts people who are generally looking at this type of ETF. It's like, if I'm in, I want to go in all the way.

Ben Felix: That's a really interesting point. I think it could be part of it. I mean, I want to go in all the way.

The other thing it could be is if someone's taken the time to listen to a podcast like this and they've decided, yep, leverage makes sense for me, even if they wanted to do lighter leverage, that person is probably more comfortable with just using margin or whatever other means of leverage they have. Like these products, you're basically paying a convenience premium for them. Or in the case of account types, you may be getting past a regulatory hurdle.

But in either case, they're not probably the most efficient way to get leverage. And so for someone who's gone down that path of learning and made that decision, maybe that's why. Also in the U.S. there was, I think it closed in 2018, there was a 1.25 times S&P 500 fund. But again, like it didn't pick up assets. And so it closed.

Dan Bortolotti: Right.

Ben Felix: It's funny. Like we have this whole conversation about these products. What these guys are saying is kind of sensible.

And what we're saying is kind of sensible, gets no traction from the market. And the ones that are literally just gambling tools are picking up assets.

Dan Bortolotti: Three times the NASDAQ. Yeah, people are all over that.

Ben Felix: But even worse, like three times some random stock.

Dan Bortolotti: If there's one simple takeaway from the discussion, it's probably that is avoid the leverage single stock ETFs. If you want to consider leverage with a diversified index, you can make an argument for it as long as you understand it. But it doesn't seem like a winning formula to me at all to leverage up a volatile, single, undiversified asset. I think you're just asking for trouble.

Ben Felix: Well, the volatility drag part of the conversation. I agree, Dan. I don't know how those can make sense unless you're betting on short-term returns for one of those stocks.

Dan Bortolotti: What was the number? He said it was like if a stock has 5% volatility, it needs to deliver 100% return in a 2x leverage format in order to just outperform the original underlying stock. Wow.

You're buying a stock and you're expecting 100% return over what time frame? That is a lottery ticket.

Ben Felix: It's a lottery ticket. I don't think that number included fees.

Dan Bortolotti: I think you're right. That's right. That was just gross of fees. I don't think there's too much you can do to talk people out of things like that if they really want to do it. I'm more interested in like, ok, let's not just dismiss these things out of hand. Let's understand them.

I'm not going to use them. I'm not going to recommend them to my clients, but that's fine. Let's understand them and let's see when they could conceivably be appropriate and whoever is going to use them should go in with their eyes open. And they dispelled a lot of myths that I think needed to be dispelled.

Ben Felix: I agree. That's it. That was why we wanted to talk to these guys because they've done the work to have us reconsider some of the past beliefs that we had on these products.

And even if we're not going to use them, I think it's worth making sure people have good information.

Dan Bortolotti: For sure.

Dan Bortolotti: Thanks a lot. See you next time.

Disclaimer:

Portfolio management and brokerage services in Canada are offered exclusively by PWL Capital, Inc. (“PWL Capital”) which is regulated by the Canadian Investment Regulatory Organization (CIRO) and is a member of the Canadian Investor Protection Fund (CIPF).  Investment advisory services in the United States of America are offered exclusively by OneDigital Investment Advisors LLC (“OneDigital”). OneDigital and PWL Capital are affiliated entities, and they mostly get on really well with each other. However, each company has financial responsibility for only its own products and services.

Nothing herein constitutes an offer or solicitation to buy or sell any security. Occasionally we tell you not to buy crappy investments in the first place, but that’s not the same thing as telling you to sell them.

This communication is distributed for informational purposes only; the information contained herein has been derived from sources believed to be “truthy,” but not necessarily accurate. We really do try, but we can’t make any guarantees. Even if nothing we say is fundamentally wrong, it might not be the whole story.

Furthermore, nothing herein should be construed as investment, tax or legal advice. Even though we call the podcast “your weekly reality check on sensible investing and financial decision making,” you should not rely on us when making actual decisions, only hypothetical ones.

Different types of investments and investment strategies have varying degrees of risk and are not suitable for all investors. You should consult with a professional adviser to see how the information contained herein may apply to your individual circumstances. It might not apply at all. Honestly, you can probably ignore most of it.

All market indices discussed are unmanaged, do not incur management fees, and cannot be invested in directly. Which is a shame, because it would be awesome if you could.

All investing involves risk of loss: including loss of money, loss of sleep, loss of hair, and loss of reputation. Nothing herein should be construed as a guarantee of any specific outcome or profit.

Past performance is not indicative of or a guarantee of future results. If it were, it would be much easier to be a Leafs fan.

All statements and opinions presented herein are those of the individual hosts and/or guests, are current only as of this communication’s original publication date. No one should be surprised if they have all since recanted. Neither OneDigital nor PWL Capital has any obligation to provide revised statements and/or opinions in the event of changed circumstances.

Is there an error in the transcript? Let us know! Email us at info@rationalreminder.ca. 

Be sure to add the episode number for reference.