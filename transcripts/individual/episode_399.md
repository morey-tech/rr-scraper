## Episode 399

Ben Felix: This is the Rational Reminder Podcast, a weekly reality check on sensible investing and financial decision-making from two Canadians. We're hosted by me, Benjamin Felix, Chief Investment Officer, and Cameron Passmore, Chief Executive Officer at PWL Capital.

Cameron Passmore: And welcome to episode 399. Ben, we had feedback from a listener, at least one listener that they wished that kind of the podcast would go back to its more mathy roots. Well, I would suggest that today absolutely crushed that request. 

And this conversation with repeat guest, Professor James Choi, phenomenal, phenomenal and interesting person in terms of what he's up to and how he thinks and how he communicates, absolutely delivered on being more mathy, but also extremely practical. His whole brand is practical finance, right? Making complicated decisions easier, which is also what this podcast is all about. 

But wow, what a conversation. You have to queue it up, but man, I thought it was phenomenal.

Ben Felix: I saw James speak at a conference last year. He was actually speaking about Scott Cederburg's paper. He was a discussant. 

It was a great discussion of that paper. And he made a bunch of really interesting points that he covers in one of his new papers. So I, of course, read that paper, which I think was a work in progress last time we talked to him, if I remember correctly. 

But I went through this new paper that he has out, which is titled Practical Finance: An Approximate Solution to Lifecycle Portfolio Choice. And it's honestly so good. It's just such a good paper.

It's such a good discussion of portfolio choice, which is just how to pick how much you should invest in stocks versus bonds. This is a great discussion of that. But then let me back up. 

That is a complex problem to solve. We'll let James explain that during the episode. But how much should you have in stocks versus bonds? 

It's not a simple problem to solve. But what they did is they took the complex solution and created an approximation of that that is relatively easy to solve with relatively few inputs, but gets you very, very close to the numerically optimal solution. That's cool. 

Okay. But their whole thing is practical finance. They want you to be able to solve for the optimal asset allocation for your specific situation in a spreadsheet. 

So I read the paper and I'm thinking, okay, well, I've got to go build the spreadsheet. Then I started looking at the formulas that would be required. I'm like, okay. 

They did make this relatively simple, but it's still not super easy. This is going to be a hard spreadsheet to build. So then I think, James must have built the spreadsheet. 

There's no way he didn't. So I went back to the Yale website where the paper is posted. And right below the paper is a link to a Google sheet that he's built.

So you can solve the portfolio choice problem yourself with a few inputs. The paper is incredible. The discussion about asset allocation is incredible. 

The fact that they solved an approximate solution is incredible. The fact that they put that into a spreadsheet that anybody can use is just mind blowing. Anyway, so... 

Cameron Passmore: It's so nerdy.

Ben Felix: I asked James a while ago if he'd come back on and here we are with that episode. I knew it was going to be good because James is very, very good at speaking and talking about his research and the research itself is incredible, but this blew my expectations out of the water. As high as they were, blown out of the water. I'm feeling pretty excited right now. I don't know about you.

Cameron Passmore: I can tell.

Ben Felix: This is a great conversation. We've introduced James on the podcast before, but I'll do a quick bio before we jump in. So James is a professor of finance at the Yale School of Management. 

His research spans behavioral finance, behavioral economics, household finance, capital markets, health economics, and sociology. He has been, as you mentioned Cameron, pretty focused on this idea recently of practical finance. How do we take all this really nerdy stuff with all the equations from academia and make it useful to normal people who are making decisions in a noisy and complex world? 

That's exactly what this paper focused on. He's been published in all the top journals. I mean, he's kind of top of his field in financial economics. 

He's got his PhD in economics and an AB in applied mathematics from Harvard University. Brilliant guy, a great speaker. And as I mentioned, I knew this episode would be good. I didn't know it would be this good. Anything to add?

Cameron Passmore: No. Ben's happy. James Choi is awesome. Let's go to the conversation. 

Ben Felix: Let's go. 

Braden Warwick: Hey guys, it’s Braden here. Before we get to the interview with James, I just want to mention that I’ve built a web app for James’s model that’s available for free on our website. For Canadians, I’ve added our tax and CPP engines to make the after-tax income and net worth estimates more accurate.

If you’re outside of Canada, you can still use the tool exactly how James built it, entering in your after-tax income and net worth amounts directly. Feel free to check it out and let us know what you think. Now, on to the interview with James Choi.

Ben Felix: James Choi, welcome back to the Rational Reminder Podcast.

James Choi: Great to be here.

Ben Felix: Great to have you back. And we're talking about a new paper that you have that, as I was saying before we started recording, is like such a cool paper. To start talking about that, can you explain what the portfolio choice problem is?

James Choi: Seems like a deceivingly simple question. The portfolio choice question, obviously, is a fraction of our portfolio; should we be allocating to different assets, stocks versus bonds versus whatever, crypto. My paper is dealing with kind of a very simple version of that problem, which is just the stock market, broad index versus the risk-free asset. 

And the twist on this is that we're doing it in the context of the life cycle and in the context where you have wage income coming to you and you can't borrow against the wage income and the growth of your wages is not correlated with the stock market, but there is risk in your wage income. And so the question is, how do you adjust your asset allocation optimally, given the fact that you have this wage income that's coming to you?

Ben Felix: You said it's simple, but it's actually a super hard problem to solve. Can you describe how Robert Merton initially set up and solved the portfolio choice problem?

James Choi: Yeah. Good old Bob Merton back in 1971 published a paper that solved the simple version of the problem, which is when you have risk-free labor income, then things become quite simple. You, as you're taught in finance 101, should discount each cashflow in the future, according to its own risk, while your wage income is risk-free. 

So you just discount future wage income at the risk-free interest rate and you add up all those discounted values and you have a present value of all your future wage income. And this is just a risk-free bond in your portfolio. It just happens to be held in human capital form rather than dollars and cents. 

And now you just do your portfolio allocation, taking into account you have all of this money tied up in the risk-free bond in your human capital. So if you were supposed to be like a 50-50 stocks risk-free asset allocator, then you say, well, how much money do I actually still have allocated to the risk-free asset in my human capital? Okay, so I don't want to invest any more in the risk-free bond above and beyond half my wealth and my wealth is now my human capital plus my financial capital. 

And so now I'm just going to invest my financial portfolio to kind of get me to that 50-50 overall in my total wealth portfolio, the financial portfolio plus the human capital portfolio. So that's actually like pretty simple. Now where things get more complicated is when your human capital is not risk-free, which unfortunately for all of us is not the case. 

Our human capital in the future is going to come to us risk-free. So like how should our portfolio be adjusted when we have risky labor income?

Ben Felix: How did Merton solve whether it should be 50-50 or 60-40 or whatever? Like I understand incorporating the human capital, how is the risky share determined in the first place?

James Choi: Well, that's coming from a classic formula that he published, I think in 1969, where he asked the question, well, suppose that you just have this pot of money that you are managing the heck out of. You're allocating the heck out of this thing, but that's all you have to live on. This single pot of money, you have no labor income coming to you. 

You have no transfers coming to you in the future. This is it. Well, in that case, there's this classic formula that says the fraction that you want to put into the risky asset is what is the expected return on that risky asset above the risk-free interest rate. 

And then you divide that by the product of the risky assets return variance and what we call the coefficient of relative risk aversion. You can kind of think of this as a number where the higher it is, the more averse you are to risk. If that number is zero, then you're perfectly neutral towards risk. 

So 50-50 probability of zero or a million dollars versus $500,000 for sure, those are exactly as good to me. That's a risk aversion of zero. And then as you go from risk aversion to one to two to three, all the way up to 10, you get more and more risk averse. 

And actually, risk aversion can go to infinity. But it's commonly been thought among economists that anything above 10 is just endopathological. And we don't think that anyone actually has risk aversion above 10.

We kind of cap it at 10. But that's just for kind of plausibility reasons, not because there's anything mathematically inherent about that. And so you have this formula, the equity premium divided by the product of your relative risk aversion and the riskiness of the risky asset. 

And that gives you a number like 50% or 60% or 40%. And that's the fraction of your total wealth that you should be putting into the risky asset. And now, when we add human capital, we're just taking a more expansive view of what your total wealth is. 

But at the end of the day, you're still allocating that 40% or the 60% or whatever that 1969 formula told you do to the risky asset. And the remainder would be in the risk-free asset. The difference just being that you're already holding a ton of risk-free asset in the form of your human capital. 

Ben Felix: Is that the Merton share?

James Choi: The 1969 formula is the Merton share. It's adjusted for human capital.

And what that's going to do, actually, the presence of risk-free human capital is going to make your financial portfolio optimally much riskier in percent allocation terms. Because let's say that your total wealth is like $10 million when it comes to both your financial portfolio and your human capital. But you have to do all of your risky asset investment through your financial portfolio.

You can't do it through your human capital. And so a lot more of your financial portfolio is going to get put into the risky asset in order to get you to your 50-50, let's say, overall portfolio allocation to the risky asset.

Ben Felix: Yeah, okay. That makes sense. All else equal, just based on the way the Merton share works, if the expected risk premium is higher or the standard deviation of returns is lower or you're less risk averse, you're going to have a higher optimal equity share.

James Choi: Exactly, yes.

Ben Felix: That was all with risk-free human capital. I think it's a 2006 pretty famous paper by Cocco, Gomes and Maenhout. 

We did have Francisco Gomes on the podcast a while ago if people want to hear him describe that paper. How did they set up and solve the portfolio choice problem?

James Choi: They said quite reasonably that we know that human capital is not risk-free. It has risk, but when they look in the data, and this has been documented by many researchers, the risk of human capital is pretty uncorrelated with the stock market's return. That actually makes it mathematically hard to solve the problem. 

So there's not a nice algebraic expression for what your optimal risky share of portfolio should be when you have this human capital risk that is uncorrelated with the stock market and yet kind of substantial in size. They went about solving the problem numerically. They didn't have an algebraic expression for the optimal equity share, but they were able to just run a numerical optimizer to see what portfolio share to the risky asset would maximize the stream of expected utility over your lifetime. 

So they solved it for each age from 21 or whatever it was to 99. And they did it for a particular set of parameters. So a particular kind of preference parameter for how risk-averse you are, a particular expected return of equities above the risk-free asset, some particular values of how risky your labor income is. 

They solved this numerically, and then they presented the solutions to that particular set of parameters, values. One surprise that came out of that paper was that it's not obvious when you have risky labor income where the risk is uncorrelated with the stock market that that human capital would still behave like a bond in the force that it exerts upon your optimal financial portfolio allocation. But they found by running the numerical optimization that it does act a lot like a bond. 

It's as if you have this bond in your overall wealth portfolio, but it's just a smaller bond than the risk-free. So you can kind of think of it as we are supposed to discount future cash flows in accordance with their riskiness. The riskier the cash flow is, the higher the discount rate we would apply because risky future income is worth less to us in today's terms than for sure future income. 

They kind of showed in a bunch of graphs that indeed risky human capital behaves like a bond. But then that's kind of where they left it. They solved the model for a particular set of parameters. 

And now if I am trying to apply the lessons from their research, these graphs are very pretty, but those are not my parameter values. I have a different level of risk tolerance. I think the future expected return on the stock market is different. 

My labor income risk is different, so on and so forth. And I am kind of left without guidance from their paper because they never solved the model for my parameters. They solved it for the hypothetical parameters of their agent that they picked.

Ben Felix: Can you say more about why labor income, which as you noted is risky, why did they find that it behaves more bond-like in the portfolio selection process?

James Choi: It's just kind of a thing that was not mathematically proven. It just happened to be the case that when you run the optimization, as long as the risk is uncorrelated with the stock market, then it's going to behave like a bond. And the more correlated that risk becomes with the stock market, then the more your labor income is going to behave like a stock. 

For realistic values of labor income correlation with the stock market, it's going to not be completely like a stock, but it'd be like some mixture of the stock and the risk-free asset.

Cameron Passmore: Really interesting. Why don't we see many financial advisors or so-called normal people using these solutions in their portfolio decisions?

James Choi: For the reason that I outlined, it's tremendously hard to implement these solutions for yourselves. Cocco, Goves and Maenhout, they were kind of not in the business at the time of trying to help people out in this particular way. Now, this paper that they wrote is a classic paper. 

It's still the benchmark paper in this literature on lifecycle portfolio choice. So I don't want to throw too much shade at the paper because it was really a great piece of scholarship, endures to this day. That said, they were after some different fish, and they were not in the business or they did not think of themselves as being in the business of providing people advice or helping people construct their own portfolios. 

So they have a set of solutions for a set of parameters that probably apply to only a very, very small fraction of the population. Now, if I'm a financial advisor, or I'm a sophisticated individual, and I want to use their insights, there's no real easy way to do that. I need to kind of write my own Fortran code and run that numerical optimization for myself and see what comes out for my parameter values and my preferences and so on. 

Nobody's going to do that. Not even economists are going to do that. So without an easy on-ramp, I think that the methodology and the insights went largely unused.

Ben Felix: Based on what we know, can you talk in general about how variables like wealth, risk aversion, labor income characteristics, discount rates, how should those things affect normative asset allocation advice?

James Choi: With wealth, the more wealth that you have already accumulated, financial wealth that you've already accumulated to date, holding fixed your age. So let's say two different 40-year-olds, one has saved more than another to date. The person who has saved more to date should actually have a less aggressive financial portfolio. 

That's because a larger fraction of their lifetime resources are now in their financial portfolio, a smaller portion is in their human capital, which is acting like a bond. The fraction of their total lifetime resources that are implicitly tied up in a low-risk bond in the human capital is smaller. So they need to de-risk their financial portfolio a little bit in response to that. 

So the richer you are right now, relative to the future stock of your human capital, the more conservative you need to be in your financial portfolio. Now, sometimes you hear advice out there that has this flavor. You haven't really saved enough up to date, and so you're behind. 

So you should take on more risk in your portfolio because you need those expected returns. That doesn't really make a lot of sense because if you don't have a lot of wealth and you're behind and you're feeling deprived, well, it sounds like maybe if there's a bad realization of risk in your portfolio, you're going to be terribly off. Maybe you should be de-risking your portfolio instead of up-risking your portfolio. 

So I think that that line of reasoning just doesn't make sense to me. But the line of reasoning that does make sense to me that says the person who has under-saved to date should take more risk in their portfolio is just that a smaller fraction of your lifetime resources is tied up in your financial portfolio right now. A bigger portion of your lifetime resources is tied up in this bond-like human capital. 

And so to get to your desired optimal total wealth fraction that is in the risky asset, you should be taking more risks in your financial portfolio. That's wealth. Risk aversion is kind of an easy thing. 

The more risk averse you are, all else equal, the less money you should be putting into the stock market. And similarly, the more you think the stock market is expected to return in relation to the risk-free asset, the more money you would put into the stock market. Now with discount rates, actually, it's kind of an interesting comparative stat. 

So we didn't directly vary the discount rate in our analysis ourselves. What we did was we didn't kind of have this mortality probability. So the probability that you're going to die at each given age, and that is matching mortality statistics in US government mortality tables. 

That's introducing a differential discounting at each age where obviously the older you are, the more likely you are to die. And so the higher your implicit discount rate is because tomorrow just might never come around. The insight there is that the discount rate does not directly affect your optimal asset allocation today in the sense that suppose there's a 50% chance that I'm going to die tomorrow and a 50% chance I'm going to remain alive tomorrow and then I'll consume the proceeds of my portfolio. 

Just because there's a 50% chance that I'm going to die tomorrow doesn't actually affect how I should allocate my portfolio today because that allocation decision only really applies if I remain alive tomorrow. But whether I'm alive with probability one tomorrow or probability 0.5 tomorrow, in the scenarios where my portfolio allocation decision matters, the optimal allocation is the same. So there's no direct effect. 

Now there is an indirect effect in so far as the discount rate is going to determine how much I save today versus how much I consume today. And so if I have a really high discount rate, so I'm really impatient or I have a very high probability of dying tomorrow, then I'm going to consume more today. And so that's going to leave me with less assets tomorrow. 

And that could indirectly exert a force on what my optimal asset allocation is today because I might find myself relatively liquidity constrained tomorrow if I do end up staying alive. That could exert a force. But I think that's more of a second order force, not kind of a first order force.

Ben Felix: Yeah, interesting. And the last one is labor income characteristics, but you kind of touched on that earlier. If you're more stock-like, it's like you've got a smaller bond position.

James Choi: Yeah, but there's an additional twist to that, which is there are two components of labor income risk. There is transitory labor income risk and then there's permanent labor income risk. So transitory labor income risk is like, you know, I get laid off, I'm out of work for six months and then I find another job and I'm back to normal. 

So these are risks that don't, in expectation, persist over time. And then there is that permanent risk, which we might call career risk. Do you make partner at your law firm? 

Do you get that promotion? Do you get demoted and there's a stigma on you for the rest of your life? That sort of thing. 

Now it turns out that the amount of permanent versus transitory income risk that you have is different by education level. So if you are a high school dropout, then you have relatively high transitory labor income risk. You're kind of getting laid off a lot more than a college graduate would, but you don't have a lot of career risk because when you're employed, you're kind of doing the same job to the first approximation. 

Whereas a college graduate doesn't have that much transitory labor income risk, not zero, but relatively low, but they have a lot of career risk, a lot of permanent income risk. And it turns out, and this is something that we discovered in our paper, by the way, I should mention that this is a paper that was coauthored with Canyao Liu and Pengcheng Liu, both Yale Finance PhD students. Pengcheng almost graduated, Canyao now graduated and working on Wall Street. 

So what we found was that the transitory labor income risk actually does very little to affect your optimal stock allocation. So that kind of rolls off the back of the agent that we're modeling. It's the permanent income risk that is really scary and causes you to choke up on the bat, essentially, and become more conservative in your portfolio. 

Maybe ironically, and people might've had a different instinct, it's the high school dropout, that, all else being equal, would be more aggressive in their portfolio allocation than the college graduate.

Ben Felix: That's counterintuitive. I think we have questions later about how people should think about estimating their future wages, which I think would be related to that, but we'll get there in a bit. For this paper, can you talk about how you and your coauthors set up and solved the portfolio choice problem?

James Choi: It was very simple on one dimension, which is we just took the Cocco, Gomes andf Maenhout model, and we solved it for thousands of different parameter sets that were within kind of a realistic range of what we thought would be relevant for people who would want to use the model. What turned out to be difficult, and this is why the paper kind of took six years to come to fruition, is when you're doing these numerical optimizations, it's a little bit of dark art to get these things to work. It's not like you just put it to Solver in Excel, and it gets to you the solution, and you're done. 

Then strange solutions come out, and you're like, that can't possibly be right, and so you kind of need to constrain the search in certain ways, and extrapolate off the grid in certain ways, and these things that you think shouldn't matter actually end up mattering. Now, when you're solving the model for one parameter set, you kind of look at it, and you're like, okay, that's funny, okay, we'll tweak it this way and that way, now that the solution is working out just fine, and then you're done. When you're solving for thousands of different parameter sets, you need a really general way to make the solution robust, and so that's what took up a lot of our time.

Cameron Passmore: How did you approximate your numerical solutions with a simplified model?

James Choi: Well, so we knew from the Cocco, Gomes and Maenhout paper that the solutions that came out looked a lot like the old Merton 1971 solutions, where you have risk-free human capital, and just the value of the bond appeared to be different than if you were discounting future labor income at the risk-free interest rate. That hint was there in the 2005 paper, but they didn't run with that very much. We said, well, if it looks like human capital when it's risky but uncorrelated with stock market return behaves like a bond, well, how do we value bonds?

We apply discount rates to future cash flows or future expected cash flows. What if we did the same thing with human capital? What is the discount rate that I should apply to my labor income at age 60 or my social security benefit at age 75, and so on? 

We just went about trying to find discount rates for future human capital, and there was no guarantee at the end of the day that we would be able to find discount rates that would result in present discounted values of human capital that then would closely match the solutions that were coming out of the numerical optimization of the Cocco, Gomes and Maenhout model. It just so happened that working off of this hunch and finding these discount rates, we were able to actually get a pretty close fit. That was a happy result, but not one that was a complete shock because we were able to eyeball the graph and say, gee, it really looks like these things are behaving like bonds that are discounted at higher rates than the risk-free interest rate. 

That was step one. You got a series of discount rates for different ages and for each parameter set. You have many, many thousands of discount rates. 

Next step is to provide an easy way for people like you and me, who are casual observers and users of this research, to calculate a discount rate for themselves. Then we just provided these arithmetic approximations as a function of the model parameters. How much do you multiply risk aversion by? 

How much do you multiply the risk premium by? Then you add up these products. Basically, we ran a regression to approximate the discount rates as a function of the model parameters. 

It turned out the very simple functions of the model parameters provided pretty good fits to these discount rates that are popping out of our own optimization. Happily, and again, there was no guarantee that this was going to happen, relatively simple calculations allow you to come to pretty close approximations of the optimal solutions.

Ben Felix: You say pretty close. They're really close. Can you talk about how close the approximate solutions are to the precise numerical solutions?

James Choi: I'm talking a little bit of generalities because there are, of course, thousands of different parameter sets. Within those thousands of different parameter sets, there are 80 different ages. There are also different asset allocations that are associated with different levels of financial wealth that has been accumulated up to each age. 

Basically, if you were taking goodness of fit over the entire range of solutions that we computed for the entire range of parameter sets, talking about an average deviation of about three percentage points, four percentage points from what the actual numerical optimization would suggest. That's one way to look at it, just how much scatter there is. Another way to look at it is if you put best fit line, where I put on the vertical axis, the allocation that was coming out of the numerical optimization, and then on the horizontal axis, you put on the approximate solution that we were providing, and you look at what is the slope of that relationship, it's very, very close to one. 

We think the fit there is pretty good. The last thing that we did was we ran this exercise where we said, take a 22-year-old. If that 22-year-old followed the actual optimal asset allocation strategy over their entire life, what is the expected discounted stream of lifetime utility that they would get? 

Now, instead, let's have this 22-year-old follow our approximate strategy instead. Then we can measure how bad is the welfare loss from following our approximate strategy instead of the actually optimal strategy. It turned out that this was less than a 0.1% welfare loss over the course of the lifetime.

Ben Felix: That's one of the most exciting parts of the papers. It was thrilling. I'm not even kidding. That was such a fun part to read.

Cameron Passmore: You guys are such nerds. My gosh, I need to get out more.

Ben Felix: Oh, it was so good. Were there cases or parameter sets or whatever where the approximation was not good? Are there cases where we can say, well, it doesn't work as well for these parameters?

James Choi: That's a good question. I don't think that we drilled down to that level, but maybe that's something we should take a look at after this interview.

Ben Felix: That'd be interesting. Were you guys surprised when you saw how close it was, especially with the welfare loss analysis?

James Choi: You have to be cautiously optimistic when you do these research projects because if you're pessimistic, then you would never finish or even start these things. There's a positive illusion, maybe, that's associated with any research project. It worked out. 

It's like, of course, it worked out. I'm sure that somebody who's not involved in the research project may have been more surprised because they would have been more pessimistic.

Cameron Passmore: I have to ask James, how does your approximately optimal solution compare to rules of thumb like the classic 100 minus your age in stocks?

James Choi: The 100 minus age or 60-40, they're actually not bad. I think that's why evolutionarily, these rules have had their persistence. You do worse with these rules, but it's not awful.

I have this table in front of me. If you used 100 minus age in your percent of your portfolio in equities, then what we're calculating is across all the parameters that we consider that you would lose 2% of lifetime welfare as a 22-year-old. If you were just 60% equity for your entire life, then you would lose 3.75% of your lifetime utility across all our parameters. That's in contrast to our rule where you're losing 0.06% of your lifetime utility if you follow our rules instead of the optimal. Now, there are some things that you can do that are really quite terrible. So if you are 0% equity for your entire life, then you're losing 7.9% of lifetime welfare. So it's feeling quite big. If you're 100% equities for your entire life, then you lose 11.8% of your lifetime welfare. There's a lot of heterogeneity actually in that particular figure. 

If your relative risk aversion has value of 4, we talked about relative risk aversions being how afraid are you of risks. We think that 4 is a pretty reasonable number that a lot of people probably have. Then 100% equities for your entire life is only going to result in a 0.56% welfare loss. So actually, where we think a lot of people are, 100% equities for your entire life is actually pretty good. It's just that if your relative risk aversion is 10, which we think is on the border of pathologically risk averse, then you're losing 30% of your lifetime welfare by being 100% equities. But I think realistically, there's not a lot of people there. 

So I'd say that 100% equities probably for a lot of people is not a terrible strategy. I do have a faculty colleague here at Yale who is 100% equities, not a particularly young guy at this point, but he says he's just betting on the equity premium and he's done pretty well for himself.

Ben Felix: That part of the paper was super interesting where it's like I read the welfare loss from being 100% equities and it was worse on average across all the parameter sets than being just in cash. I was like, whoa, what is going on there? But then when you talk about the heterogeneity for a normal level of risk aversion, that welfare loss is actually really small. 

It's just for a really risk averse person, you're losing a ton of welfare by being in stocks.

James Choi: As a footnote to that, the 0% equity is really terrible for across all the different parameter sets. 0% equities is where a lot of people are. One of the lessons that comes out of this paper is an old lesson, but this is just bringing it back to the fore, is that when you have human capital, equities are awesome for you because you have this huge, huge bond-like asset in your implicit portfolio.

You should not be afraid of putting that money into stocks because if you do experience a loss, well, you're cushioned by that enormous stock of human capital you have. You can afford to take a 20% loss in your financial portfolio if you have a human capital stock that is like three, four, five, six times the amount of money that you've already saved to date.

Ben Felix: For someone with normal-ish risk aversion, 100% equities actually looks okay over the life cycle, but your optimal allocation is still better. If we think about that, what does the optimal portfolio look like over the life cycle of, I don't know, like a typical household?

James Choi: Well, it's just going to be very heavily stocks, like 100% stocks. We do cap the formula so that you can't have more than 100% stocks in your portfolio, and you'd be 100% stocks for a very long time during working life. Then eventually, you would start de-risking your portfolio, but that might not be until your 40s or your 50s. 

The reason that you de-risk the portfolio is that your human capital stock is getting run down. The depressing truth is every paycheck I get, in some sense, I'm not getting any richer or poorer. It's just my human capital is sublimated into financial capital, but it's the same number of dollars. 

Now, I need to make an allocation decision with the new dollars that have just been transferred from my human capital to my financial capital. As I get older, I have fewer paychecks coming to me in the future. My human capital stock is getting run down over time. 

More of my lifetime wealth is held in my financial portfolio rather than the human capital. I need to de-risk my financial portfolio as I get older because I have less and less of this bond-like human capital in my total wealth portfolio as time goes on.

Cameron Passmore: I just want to put a finer point on that. Why is your model often recommending higher equity allocations than we see in popular personal finance advice or even past academic papers?

James Choi: It really is about the human capital angle and the fact that most of this advice is ignoring human capital. For understandable reasons, human capital is hard to deal with. It's hard to calculate. 

We don't see human capital trading in markets. We don't have a valuation for it. It's just a hard mathematical problem. 

It's a hard conceptual problem. We do what we do with a lot of hard problems, which is we ignore the hard part and solve the part that is easy. If you have nothing but this pot of money that you saved up to now, then gosh, yeah, maybe we should be a little more conservative with that pot of money because it's all we got. 

If I have $2, $3 million of labor income coming to me in the future, then if I lose $20,000 in my financial portfolio, not that big of a deal.

Ben Felix: You mentioned one of your Yale colleagues who is 100% equities. Did the results of this paper have an effect on how you and your co-authors or anybody else maybe in academia that read it, how they think about their personal asset allocations?

James Choi: I don't know if it's changed anybody's allocations at the moment. First, it's a relatively new paper that's been released. That said, the insights of the paper, those qualitative insights of the paper are not new.

This has been known for at least 20 years. I have talked to faculty colleagues, not in finance, who say that they are not anywhere close to 100% of the box and say, there's this thing, human capital, Merton, Cocco, Gomes and Maenhout. Some non-finance colleagues know my views on this. 

I don't know if they changed their portfolios during those conversations. Then for my own personal asset allocation, I've been 100% stocks for a long time, until very recently. That's because actually, for me, I felt like the problem was much easier because I'm a tenured professor at a pretty creditworthy institution, very hard for them to fire me. 

If I discounted my future expected wages at the risk-free discount rate, I'm not going to be so far off. That's what I had been doing for a long time. Even if you fuss around the discount rate a little bit, it was just pretty hard to get myself away from the 100% equities boundary for the last couple of decades. 

Ben Felix: Makes sense.

Cameron Passmore: How did you decide which variables and specifications to include in your approximately optimal model?

James Choi: It was not that difficult. Cocco, Gomes and Maenhout did a lot of the hard work for us. They had all of these parameters that they had put into their model, saying that these are the variables that we think are the most important for determining what somebody's portfolio allocation would be over the life cycle. 

We just took those variables. For the most part, we just varied those variables over what we thought of as realistic ranges. The one thing that we did not vary among their parameters was just the time discount rate, the generic rate of impatience. 

That was basically because I don't think that people have a good sense of what their discount rate actually is. There's a great survey article that was published a couple of decades ago, where it outlined the attempts of economists over the decades to estimate what time discount rates are for people. They plotted each estimate as a point on this graph, and on the horizontal axis was the year in which the estimate was published. 

You see this big cloud of points. As time goes on, there's no narrowing of the cloud. You measure discount rates. 

You're just all over the place, no sign of converging to a consensus. I think just the way that you ask these questions greatly determine the parameter that you get. I think the introspection, it's a very hard task for people to be able to introspect and figure out what their discount rate is. 

We ended up not messing with that, because we just thought that if I ask you, is your discount rate 0.97, 0.98, 0.99, you're not going to know. It's just not that useful to vary that.

Ben Felix: In the abstract of the paper, you talk about practical finance, how you basically want to make this stuff solvable in a spreadsheet for a normal person. Can you take us through an example of calculating the optimal equity allocation using your model in a spreadsheet?

James Choi: I will do a screen share. I did post a Google Doc, where actually your listeners can go to the Google Doc. I'm sure you'll put it in some link on your website. 

It's also on my Yale faculty website, right underneath the PDF for this paper, which is called Practical Finance. You can go to a Google Doc. What the link in my website will go to is instructions on how to use the spreadsheet. 

Then you click on the link in the instructions, and it'll make a copy of the spreadsheet into your own Google Drive. What you'll get is a spreadsheet with two different tabs. One is full inputs. 

One is with weight imputed. I'll explain the difference in a minute. There are instructions up at the top here. 

Then it's going to ask you for certain parameters to be entered. The important one is how risk averse are you, 1 to 10. In the instructions that accompany the spreadsheet, there's this thought experiment that you can go through to figure out what is my level of risk aversion. 

Here, I put in five. Just ask you, how old is the first adult in the household? The spreadsheet does accommodate two adults, up to two adults in the household. 

How much have you saved to date? This would be your investable net worth. What do you think the stock market's real return is going to be going forward? 

5% is kind of a reasonable value given valuation ratios, but obviously, opinions will vary greatly on that. What is the real risk-free interest rate that you're facing right now? For a US user, I would say this would be like a 30-year TIPS real interest rate because you want a long-term interest rate that's going to apply for most of your life. 

In the blue is the inputs that it wants. Then in the green and the purple, you would just enter what you forecast your future labor income to be. Here, I've just kept things simple. 

You're going to earn $100,000 in today's dollars. These are all kind of inflation-adjusted terms up to age 64. Then I say at age 65, I'm going to stop working. 

I'm going to start collecting Social Security benefits. These would be any retirement benefits that are risk-free at the point they start being collected. Then I forecasted $40,000 of Social Security benefits for myself up through age 100. 

A crucial thing to know when you're using the spreadsheet is that you are supposed to put a forecast for each age up through age 100. Even if you think you're not going to make it to age 100, all that mortality risk is baked into the approximation. As long as you don't know that you are for sure not going to make it to age 100, you should put in a value for each age through 100. 

That's for the first adult. Then I have those equivalent values for the second adult in the household. It's the same pattern, $100,000 during working life all the way through age 100. 

I start collecting those $40,000 per year Social Security benefits. What the spreadsheet does is just uses the approximations that we came up with to compute what is the value of your human capital. Here, it's $2.2 million. For reference, I do have in the bottom here, if you had no human capital, what fraction of your portfolio should be allocated to equities? Here, it's 17%. Then given that you have the $2.2 million of human capital and that you've saved $500,000 to date, what fraction of your financial portfolio should be in equities? 

It's 91%. That's using the full range of inputs to the spreadsheet in order to get a recommendation. For a lot of us, it's going to be hard to forecast our wages over the course of an entire career and then to figure out what our Social Security benefit is going to be. 

In the second tab, I have this wage imputed methodology where you just need to enter, in addition to everything we'd entered before, what is your current wage and what is your current retirement benefit? For somebody in working life, the current retirement benefit would be zero because they're not collecting anything right now. Then we will grow automatically your current wage and the average growth rate over the life cycle for a college graduate. 

That reduces the data entry burden where the only thing you need to enter is the stuff here in the blue. There is a little extra input here where in the US, there's this thing called the Social Security spousal benefit, where if one member of the couple has a much shorter earnings history or a much lower earnings history than the primary earner, then they can get a bigger benefit by claiming the spousal benefit. This is just asking, when we do this imputation of your future Social Security benefit, should we consider one of the members of the household to be claiming the Social Security spousal benefit at retirement? 

Then you get to a similar output where you have, what is the value of your human capital, our estimate of that? What fraction of your portfolio should be in equities? If you had no human capital and then given that you have the human capital that you do, how much of your financial portfolio should be in equities? Here, it's 89%.

Ben Felix: How sensitive is the equity portfolio share to risk aversion? It's at five now, if you put it to four in the spreadsheet, what do we see?

James Choi: Now, you're up against 100% versus if I went up to six, then we dropped to 70%. Not surprisingly, your risk tolerance does matter for what you should be doing.

Ben Felix: You did mention that there's a thought experiment. Can you talk more about how people should approach figuring out what their risk aversion number is?

James Choi: The thought experiment that we use is, suppose that you are facing this lottery. You flip a coin, the coin comes up heads, then you need to live on $100,000 for the next year. You have to spend it, you can't save it, you can't borrow to spend more.

You're going to actually live on $100,000 for the next year. When it comes to tails, you have to live on $50,000 for the next year. So you have this 50-50 gamble, and then suddenly a genie appears and says, I can take this gamble away from you. 

In return, I will give you a for sure amount of money that you will have to live on for the next year. The thought experiment is, what is the for sure amount of money that would make you exactly indifferent between keeping the gamble and trading it in for that for sure amount? If you are perfectly risk neutral, if your risk aversion is zero, then your answer would be $75,000. 

I'm exactly indifferent between 50-50, $100,000 to $50,000 versus a for sure $75,000 amount. The more risk averse I am, the lower the for sure amount is going to be that's going to make me exactly indifferent between keeping the gamble and having the for sure amount. We have a table that we provide where we say, if your for sure amount is X, that corresponds to risk aversion of Y.

Cameron Passmore: I know you gave the easy option for this, but how should people approach forecasting their labor income?

James Choi: Most people will start with the easy option. Another way to go is there are some data out there on income trajectories for certain careers. That's imperfect, of course, but you could see, if I'm in this industry, for some person that is 20 years older than me, what are they making right now on average? 

For someone 40 years ahead of me, what are they making on average? That's the way to go. Now, that obviously excludes the effect of just generic economic growth.

If economic growth is like 2% per year until 20 years from now, then we should expect that to lift all the boats. Just taking the average income of people 20 years ahead of me in my career would be an underestimate of how I'd probably actually earn. Then there's the old problem of everything's changing anyway. 

Maybe we will all be AI slaves in the future and be depending on the largest of our AI overlords. The future is hard to predict, right?

Ben Felix: The thing that's cool about the spreadsheet though is that if you just took your current wage and projected forward, say it's constant in real terms, you can see the effect that different assumptions would have on your optimal equity allocation. If you're like, oh, what would happen if I do think I have an above inflation career trajectory for my income? You can see how that would affect it. 

Even if we can't predict the future, we can see how different futures should affect our current asset allocation, which I think is pretty useful for people.

James Choi: Yeah. I think that what people would also see is that for especially young people, even under some pessimistic views of what their income trajectory is, the formula would probably still recommend a pretty aggressive, probably 100% equity allocation for them because even under pretty negative scenarios, they probably have a lot of labor income coming to them in the future relative to the amount of money that they've already saved.

Ben Felix: One of the other inputs on the sheet is investable net worth. What does that include? Is your house in there? What's not in there? What is?

James Choi: This is the pain point actually. Turns out that housing is extraordinarily hard to model. It's illiquid. 

It has high transactions costs. The risks of housing are poorly understood. If my house value goes down by 10%, but I'm living in the neighborhood just fine, and I never plan to move, then no big deal. 

I haven't realized the loss at all versus my house value went down by 10%. It's because my neighborhood went to pot. That's terrible. 

It depends a lot. When I plan to move, when I move, am I moving to a neighborhood whose house price growth is pretty correlated with mine or not. If my house price falls by 10%, that neighborhood that I'm going to move to has house prices that have also fallen by 10%.

Again, no big deal. It was hedged. Those kinds of considerations, and then you have mortgages that are amortizing over time. 

That's another thing that you need to keep track of. Housing is a huge, huge headache for all models like this. What do we do in our case? 

Well, we don't have housing in our model. How do we deal with problems that are really, really hard? We ignore them for now. 

The model, very strictly speaking, is for a renter for life. The question is, well, a lot of people have housing. How do we deal with that? 

The off-label recommendation that I give is ignore housing. Take out home equity. Ignore the mortgage in your investment net worth calculation. 

Make the investable net worth all of your non-housing assets minus all of your non-housing debts, and that I would call that investable net worth. Now, surely that can't be the actual right answer, but it's kind of the best that we have right now. I was having a conversation with this very distinguished real estate professor who's at Wharton at UPenn.

I asked him, you're an expert in real estate, world-renowned scholar. How is your financial portfolio allocation affected by the fact that you own a house in Philadelphia? He said, not at all. 

I basically ignore the house and just allocate my portfolio as if the house didn't exist. So, yeah, at least I'm not alone here.

Ben Felix: That is so funny. You're right. It's like if you said, okay, should a renter or an owner have a riskier financial asset portfolio, you'd have to ask what neighborhoods do they live in? 

Where do they plan on living in the future? Do they have a mortgage? It's not a straightforward question to answer.

Cameron Passmore: No, not at all. How frequently should people be updating their assumptions and their portfolios?

James Choi: If you update it once a year, that will be perfectly fine. These things are not quickly moving, and so I don't think that your optimal portfolio allocation quickly moves. One time, I was personally more enamored with volatility timing. 

So this is this strategy that observes that the volatility of the market going forward is highly predictable, but the average return on the market is no different whether you're in a really volatile time or not volatile time. And so, voila, the obvious implication is pull back on the market when things are really volatile, be aggressive in the market when things are less volatile. It turns out that when you backtest the strategy, it's not like fantastic. 

A lot of the bloom on that has come off for me. And so that was kind of my one little carve out when you might want to maybe pay attention to your portfolio, adjust the portfolio more often. Absent that, I don't think there's a lot of justification for fiddling with your portfolio too often.

Ben Felix: It just comes back to Merton's share, I guess. If markets are more volatile and volatility predicts future volatility, you should be taking – well, your equity share should be lower when markets have been volatile.

James Choi: And that was how I did my personal portfolio. You have the Merton share and you have the variance of the market return in the denominator. Just stick in the VIX squared into the Merton share and then kind of take my Merton share, adjust it for my human capital. 

There was an equity allocation for me. For the vast majority of the time, even when things are a little scary, you are at 100% equity shares because human capital is pretty huge for people that aren't very close to retirement. But every once in a while, things pull off the 100% boundary even for somebody middle age, like during COVID, VIX went to like 83 or whatever it was. 

That was a scary time and I did pull back at that time. Liberation Day, Trump tariffs, scary time and pull back there. So during COVID, volatility timing worked quite well for me. 

The Trump tariffs, they did not work so well for me because the markets came back so quickly.

Ben Felix: So do you still do it?

James Choi: No. As I said, the bloom has come off for me. Since the Liberation Day episode, there hasn't been a huge VIX spike since then. So there hasn't been an opportunity to, but I think that I'm more reluctant to do it now than I would have been in the past.

Ben Felix: That's cool. You mentioned earlier about how there's no leverage. We're constrained at 100% equity. 

Do you have a sense of what would happen to the model's advice for a typical household over the life cycle if we relaxed the no leverage constraint?

James Choi: In the model, strictly speaking, the agent never wants to lever because returns are log-normally distributed in the model, which means that a negative 100% return is, or very close to negative 100% return has some tiny, tiny, tiny probability of happening, which means that if you lever up, you have some tiny, tiny probability of having negative wealth. You can't borrow in the model. And so that means that your consumption is like negative, then things blow up because that's just not allowed. 

You're kind of like infinitely unhappy if consumption is negative or zero. And so in the model, you never want to do that. Now, in real life, we don't think that the stock market has hardly any chance of going to negative 100%. 

Leverage, I think, can be advisable for somebody who is relatively young. And so I think that if you were to do that, probably the way to go is through one of these leveraged funds, 2X, 3X. They're actually surprisingly reasonable investments. 

They get a bad rap in some circles because their leverage resets every day. I think that's a feature, not a bug. And that's a crucial feature for ensuring that these funds never return less than negative 100%. 

You need to understand that you're not going to get 2X or 3X the market exactly over longer investment horizons. There's a chart out there that these funds go to zero for sure, probability one, as the investment horizon goes. And that's just not true. 

I mean, you can run the simulation, see it's not true. And then you can actually see the experience of these funds themselves. They've been running for like 20 years now. 

And no, they have not gone to zero. In fact, they have vastly outperformed an unlevered investment in the S&P. Here, I'm talking about leveraged funds on the S&P 500. 

There's kind of crazy stuff like levered funds on Nvidia stock, which I would not recommend. The other thing that gives me more confidence is that these leveraged funds, having been around for 20 years, they went through the 2008 financial crisis. They went through COVID. 

They didn't blow up. There were kind of exotic products that did blow up under some of these circumstances. They didn't blow up. 

I really understand well how they're generating that leverage through equity swaps, very plain vanilla financial contracts. And we know that they borrow at very low rates, 70 basis points above treasuries is the estimate. So if you're going to do it, I think, especially for somebody who's young, it's not unreasonable. 

You just have to be emotionally, relationally prepared where sometimes you might lose 20% of your investment or 30% of your investment in a day. If you kind of have your why ready, I know why I'm doing this. I know the theory. 

I know I have this human capital buffer behind me, then I lose 20% in a day. It's painful, but it's not like the end of the world. But if I need to sit at the dinner table with my spouse and try to think, am I ruining my family's future because I just lost 20% of our wealth in a day? There are other considerations that you have to think about.

Ben Felix: That makes me think of John Cochrane's analogy about the inflation index perpetuity and how it's technically risk-free, but good luck explaining that to your spouse when it's mark-to-market value drops by 40% or whatever.

James Choi: Absolutely.

Ben Felix: It's funny. Really interesting about leverage ETFs. The episode that was released today, the day that we're recording, was with Hank Bessembender. He's got a paper out on single stock constant leverage ETFs. 

You mentioned those being not the ones you want to touch, but we did have quite a bit of discussion about index constant leverage ETFs, like the 2X and the 3X and all that kind of stuff. I'm hoping that he'll include analysis of those in a future update of his single stock ETF paper, because one of the things he looks at is, he calls them fictional costs. How much does it cost to use those products versus just borrowing and investing in something? 

I think he does a lot to debunk the concept of volatility decay, which is, I think, what's been used historically to argue against these constant leverage funds. Super interesting. That's the second very smart person in the last little while that's told us that volatility decay is probably misunderstood and that the constant leverage funds, like the fund providers say that these are designed for daily replication. 

But like you said, you shouldn't expect to get 2X the return of the index in the long run. You're going to get less than that. But the fact that they have the daily resets and the volatility decay is probably not as much of an issue as people have been historically told.

James Choi: Well, if you're going to borrow on margin, then you're dealing with margin calls. Enormous headache. Do you really need that headache in your life? 

Big virtue of these leverage funds, you never get a margin call. There's a separate thing of like, I have student loans. I'm paying a 4% interest rate on my student loans. 

Should I keep that alive so I can invest more in the stock market? That seems quite reasonable to me. There, you don't face margin calls until your liquidity is preserved in those types of cases.

Ben Felix: Access to leverage too. If a typical person wants to go and borrow 2X at a reasonable interest rate, it's not that easy to do to invest in stocks.

James Choi: These funds do equity swaps, highly collateralized. That's why they're borrowing it. Try to do plus 70 basis points. Good luck getting that for yourself.

Ben Felix: Yeah, yeah, exactly. Really interesting. I'm glad that you brought that up and that we had that part of this discussion. 

Something I've been thinking about a lot. Leverage in general, but then using these constant leverage ETFs as a source of leverage for a typical person. Great perspective on that. 

Last couple of questions here. There's a paper that I know you've seen because I've seen you speak about it. Beyond the Status Quo: A Critical Assessment of Lifecycle Investment Advice. 

We've had one of the co-authors, Scott Cederburg on this podcast a few times to talk about that research. They find that 100% equity portfolio with one-third domestic and one-third international stocks is optimal over the full life cycle for any level of risk aversion, I believe. Can we recreate their result using your model and the inputs from their paper or the return assumptions from their paper?

James Choi: You misspoke. It's one-thirds domestic, two-thirds international, not one-third, one-third.

Ben Felix: Oh, sorry. Yeah, thank you.

James Choi: I'll talk about that as a separate issue because in our model, we just have a single stock market that you're investing in. The virtue of the paper is that it brings to the fore the fact that for somebody with labor income, stocks are kind of awesome. That's basically the message of the paper. 

Stocks are awesome, so awesome that you should be 100% equities for your entire life. Now, there are a couple things that drive that result. One is just the generic, stocks are awesome for people with labor income. 

The second is, at least for the draft that I saw, at least the baseline calibration, they were using a fairly low level of risk aversion. It was like 3.8 or something like that. Not crazy low, but it's on the lower side.

They say that the historical return on the stock market is what you can kind of expect going forward. We know that historically, the equity premium has been enormous. Currently, valuation ratios have gone up a lot over the last 50 years. 

If you combine relatively low risk aversion, high equity premium, a lot of labor income, then you can kind of get pushed towards a lot of equity. Then the last thing I'll mention is that they, at least in the baseline calibration they have, is they're kind of assuming a 10% constant savings rate over the course of the entire working life. I haven't checked this, and I'm not sure that they have exhibits in the paper that let you necessarily judge this, but it did seem like a kind of lowish savings rate relative to what an optimal model would suggest. 

Now you have this agent in the model who is not accumulating like a ton of financial wealth. If you have less financial wealth relative to your human capital, that's another force that pushes you towards more aggressive portfolio allocation. You have kind of all these different forces in their setup that pushes you towards 100% equities for your entire life. 

Indeed, that's what they end up finding. I think the virtue of the paper is that it does kind of make salient, again, that stocks are awesome, and you should have more stocks probably than you do. Now on the one-third domestic, two-thirds international allocation, I think that is something that's generated by the way that they do their simulations. 

When I first saw that result, I was surprised because if they were relying upon historical performance for the forecast, well, the US has had an incredible century. Since the inception of the MSCI World Index, the US stock market has had a higher average return and a lower variance. So kind of the international diversification just didn't pay off over the last half century. 

So that's why I was surprised. How can you get this recommendation in the model to be two-thirds non-US, one-third US? What turned out to happen is that they take the position that there is nothing special about the US during this time period. 

So a US investor could have had a domestic stock market experience that matched Belgium's stock market experience, or matched France's stock market experience, or matched Sweden's stock market experience. So they're just randomly picking one of the countries in their dataset and saying, this is going to be the domestic stock market return sequence you're going to get. And everything else is the internationals. 

And so it turns out that when they're simulating the problem for the US investor, only 5% to 6% of their simulations is the US stock market, actually the domestic stock market for the US investor. And now the US had this extraordinary half-century run, or a century-long run. And so now, what do you want to do as an agent in this model? 

You want to maximize the chances that the US ends up having a big weight in your portfolio. And the way you do that is to put two-thirds of your portfolio into international stocks, so that you catch that US rise with a big portion of your portfolio. So that's kind of what's happening. 

And so I think the critique I'd have of that is, the US is this enormous stock market, well over half the global market cap at this point. And so do we really think that it's reasonable to think that the Belgian stock market historically is going to be a good proxy for the US's stock market return performance going forward? This is kind of an untestable assumption, and it really is almost philosophical in nature. 

But I guess that's what gives me pause, is do I want to really deviate so much from market cap weights in my non-US/US portfolio by going only one-third US, two-thirds international, when in fact, the ratios by market cap weight are kind of flipped?

Ben Felix: They did find a pretty flat difference. The utility loss, or however they measured it, was pretty flat from kind of 5% domestic to 50%. You probably could still be market cap weights and be pretty close. 

We loved the result because we, and many Canadians, have about a one- third home country allocation already. That's just for whatever reason, a very common home country bias for Canadian investors. So we saw the result and we're like, sweet, that's a great confirmation bias.

James Choi: Yeah. I mean, I think it's just going to depend upon what country you're coming from as the investor. Not all home countries are created equal. 

To have 70% of your portfolio in your home country as a US investor means a very different thing than if you're a Belgian investor.

Ben Felix: For sure. Here's an interesting question for you. Given where US market valuations are, is the historical US experience a good proxy for the expected future US market experience?

James Choi: Valuation ratios are very high right now. We just know that valuation ratios cannot keep on drifting upwards forever. From kind of the old work of Bob Shiller or John Campbell, we would expect returns going forward in stocks to be lower. 

Now, that being said, we also know that if you had tried to use price dividend ratios to form portfolios over the last 30, 40 years, you would have done pretty poorly. You and your fancy math, if you just guessed the historical average as your forecast, you would have done much better. This is kind of the Amit Goyal and Ivo Welch critique that none of these predictors do very well. They certainly don't do better than just guessing the historical average to date.

Ben Felix: In this paper we're talking about there, I'm just looking at it. It's in table seven, panel D. They have risk aversion parameters from 0.5 up to 10. The optimal portfolio is pretty much the same. It's risk aversion 0.5. It's 32% domestic and 68% international. It's like a tiny, tiny difference compared to the kind of baseline result. Why do you think their result is so insensitive to risk aversion when yours is so sensitive to it?

James Choi: In our results, if you have a very high equity premium and you haven't accumulated a lot of wealth, then you're up against 100% boundary basically for a pretty wide range. I think it's kind of a function of the fact that they're assuming a very high equity premium going forward and the fact that their agent, I think, is not accumulating a lot of wealth over time because the savings rate is relatively low.

Ben Felix: One of the things that I thought was pretty interesting in that paper was that it kind of shows that, and they have some other older papers that look at this more specifically, but nominal bonds, especially when you look at all the countries in their sample, have been pretty risky historically for long-term investors with real liabilities. I thought maybe that was driving some of their result. Do you think there's anything to that idea?

James Choi: There could be. I mean, I think from investing perspective today, it's puzzling to me that any retail investor would hold anything but inflation index bonds if they have that option within the US. It's kind of been shown that just regular treasuries have this convenience yield that's negative. 

And so basically, because treasuries are the grease that lubricates the wheels of the entire global financial system, there's a tremendous demand for collateral and all sorts of other things. And so the interest rate gets depressed for regular treasuries and TIPS just don't serve that function. And so there was a paper a few years ago just showing that actually you get a better deal on all-in basis by investing in TIPS. 

And so treasuries, if you don't need the security as collateral or all this other stuff, other than just a source of return for a regular investor, there's not really any reason to hold anything but TIPS if you're going to have fixed income exposure in the government bond market.

Ben Felix: Yeah, that's really interesting.

Cameron Passmore: So the concept of making academic finance accessible to people with a spreadsheet is obviously brilliant. Asset allocation is a natural place to start. What do you want to tackle next?

James Choi: There are things that I would like to tackle that I don't quite have a handle on how to do it yet. So I think housing is like a huge black hole in our knowledge. It's only like the biggest asset that most people have. 

How that should affect our asset allocation, things like I have a big mortgage. I have some money that I've saved up. Should I invest that money in the stock market or should I try to pay down my mortgage more quickly? 

We don't have all that much to say about it. And it's only like a major, major question that pretty much every homeowner faces for many, many years during their homeownership spell. Housing is this huge black hole in our knowledge, but it's a huge black hole in our knowledge because it's really hard to figure out the solutions to these things. 

So that's what I would like to tackle, but I don't think that I'm going to tackle that soon because it's a really, really hard problem. There are other easier problems that one could think about tackling where I think there's not necessarily that much academic glory in tackling them. But an example would be like the 4% withdrawal rule, which everybody knows and talks about. 

This is not the optimal withdrawal rule. It cannot be in the most obvious level. If the level of interest rate falls, then the 4% withdrawal rule becomes less sustainable. 

There are possibly approximations to what a sustainable withdrawal rate would be as a function of some market parameters that one could create. This is, in some sense, simple-minded, which is why there's no academic glory in creating these types of things. But that said, the 4% withdrawal rule, I think it's been so influential. 

It has exerted such a big cultural footprint on our society that could be worth writing up a short little piece. Given this equity premium, given this interest rate, given this asset allocation, consumption growth rate that you want in retirement, and there are a lot of models that say that actually, we should be expecting and desiring to consume less and less as we get older and older. In that case, if you have preference parameters of such and such, that suggests a consumption decline rate of this amount. 

Now, how much should you be consuming in retirement in each year? That could be an example of something that is at least provide better guidance than the 4% rule. It's not going to be perfect. 

I think that there are all sorts of other complications with spending in retirement, medical expenses and government programs. I think that your utility function just changes when you get older. My 80-year-old self, what does he want? 

I don't know. He's a stranger. He's kind of related to me, but does he want to travel the world? 

Does he want to stay at home? I don't know this guy. I have to plan for him. 

That's kind of a first order problem that is unsolved when it comes to like, how much should I be spending at age 72 when I'm early in retirement?

Ben Felix: You call it simple-minded, which is true. I think the 4% rule has been so influential and popular because it is so simple. Any person with even limited numerical ability and no financial knowledge can take that number and figure out how much they can spend or how much they need to save. Yeah, doing a better version of that that's similarly simple, I think would be incredible.

James Choi: No academic glory in it, but maybe a big societal impact.

Ben Felix: Practically useful, which has been your thing recently, I think, with the practical finance idea. Well, I said at the beginning that this paper was super cool and I think you've proven that. Our listeners, I'm pretty sure are going to love this episode. I know I did.

Cameron Passmore: Oh my, they are going to lose it. This is pure gold, James.

Ben Felix: This is great. We really appreciate you coming on the podcast, James, and congratulations on another fantastic paper.

James Choi: Thank you. Pleasure to be here.

Cameron Passmore: Great to see you again.

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