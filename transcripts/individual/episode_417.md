## Episode 417

Benjamin Felix: This is the Rational Reminder Podcast, a weekly reality check on sensible investing and financial decision-making from two Canadians. We're hosted by me, Benjamin Felix, Chief Investment Officer and Cameron Passmore, Chief Executive Officer at PWL Capital.

Cameron Passmore: Welcome to episode 417. Nice to be back in the seat with you, Ben.

Benjamin Felix: Very nice.

Cameron Passmore: This is another great conversation. I don't know how you keep finding these incredible guests, but this week's subject is life cycle finance, and it was an incredibly interesting conversation just about how to think about, as a rational human, to plan your savings and spending over a lifetime. But it's an amazing, kind of a refresher on how to think about this, is what I took away from this conversation with Dr. Paul Kaplan. I thought it was just terrific. Nice guy. Life's work comes together as conversation, and a little bit of a treat at the end. He will share his spreadsheet with everybody.

Benjamin Felix: Yes. We do have a link to a life cycle model spreadsheet that Paul and his co-author for the book that we largely talked about in this episode created. He takes us through it during the conversation, so you'll be able to see it if you're watching on YouTube or hear about it if you're listening.

We'll link to it in the show notes, and you can download the spreadsheet and have some fun if you're into that kind of thing. We are. I enjoyed seeing the outputs of the spreadsheet, and it's also interesting just to see impact of changing different parameter values.

Very cool. The fact that it's just available for anybody to take a look at is, I think, pretty impressive. We were just talking to Paul about this after we stopped recording.

A lot of the work in the spreadsheet is being done in VBA, in Visual Basic, which is code that you can write in an Excel spreadsheet. Actually, you can use Python now too, but this is done in VBA. It's open.

The code is available for you to review and, I guess, change if you wanted to, which I think is very cool that they were so open with it. In a lot of cases, that kind of stuff would not be available for people to view and edit. Very cool.

Like you said, Cameron, this is really a great overview of life cycle finance, which is just the idea of how people allocate their money over time, both between how much they consume and how they invest. It's really consumption and asset allocation is what a life cycle model helps you figure out. They've got a whole book that they've written on this, and it covers all angles of life cycle finance, how to think about risk tolerance, how to think about the overall investor profile, which includes many things that go far beyond risk tolerance.

We did talk a little bit about index investing. It's a great conversation. He's got a very nice way of explaining things.

Maybe I'm not a great sample here, but I did not find any of it to be cumbersome. He's explained everything in clear, plain language that I think most people can understand.

Cameron Passmore: He also tells a cool story about interviewing Harry Markowitz, so make sure you listen for that.

Benjamin Felix: Yes, that was very cool. Paul Kaplan, PhD CFA. He's now retired. He was the director of research for Morningstar Canada and a senior member of Morningstar's global research team.

He led the development of many of the quantitative methodologies behind Morningstar's fund analysis, which is pretty cool, their indexes, advisor tools, and other services. He conducted research on asset allocation, life cycle finance, portfolio construction, index methodologies, and other investment topics. Many of his papers have been published in professional books and publications, including his book, Frontiers of Modern Asset Allocation.

He's also contributed to various CFA Institute Research Foundation books, which is one of the books that we talked about for most of this episode. That book is Lifetime Financial Advice. At Morningstar, he served as quantitative research director for Europe and the United States.

Before joining Morningstar, he was vice president of Ibbotson Associates. That's Roger Ibbotson's former business that he sold to Morningstar in 2006. Then prior to that, he served on the economics faculty at Northwestern University.

He's got a bachelor's degree from New York University and his doctorate in economics is from Northwestern. Great conversation. Like you said, Cameron, comes with a bonus of an Excel spreadsheet.

Cameron Passmore: Yeah, people will love it for sure. Okay, ready to go?

Benjamin Felix: Let's go to the episode with Dr. Paul Kaplan. Dr. Paul Kaplan, welcome to the Rational Reminder Podcast.

Dr. Paul Kaplan: Thank you. Glad to be here.

Benjamin Felix: Very excited to be talking to you. Paul, to kick this off, what is life cycle finance?

Dr. Paul Kaplan: Life cycle finance is the branch of economics that deals with how individuals over the course of their entire lives should be making rational decisions regarding how much they consume year in and year out, how they save, how they invest, how they spend down their wealth, and how they should be smoothing their consumption over time so that when they go from their working years into their retirement years, there shouldn't be a big jump in their level of consumption. It should be a smooth transition.

Benjamin Felix: Makes sense. What is a life cycle model?

Dr. Paul Kaplan: Life cycle model is a model that comes out of life cycle finance. It's the actual models that people that work in this field develop.

Cameron Passmore: How does your life cycle model differ from others?

Dr. Paul Kaplan: Well, first, I think it's important to understand how our life cycle model is similar to others. We use the same basic framework that all life cycle models are based on, which is the idea of optimization over a lifetime, or it's a maximum lifetime utility model, and that the output of that model is basically consumption rules that come out, investments, savings during working years, drawing down during retirement years. It could also include the use of life insurance and annuities to deal with the uncertainty of a person's lifespan.

How does it differ? It's in some of the details and also in the way that we have linked together life cycle finance, life cycle models, we have linked it together with mean variance optimization models that came out of the work of Harry Markowitz.

Benjamin Felix: Can you talk more about how you link the life cycle model with those single period analyses?

Dr. Paul Kaplan: Well, in order to understand that, we first have to go back and talk about the life cycle model in some detail, because in a life cycle model, there are a couple of key components. One key component are the preferences of the investor, and we've identified three sets of preferences. One is what I call intertemporal consumption preferences, which is what are the preferences of an investor over the course of their lifetime, how much do they discount future consumption versus present consumption, also how flexible they are in changing consumption from one period to the next, so how much do they value consumption in one period versus another period.

Another component is bequests, preferences regarding their bequests, which would determine how big a bequest they're going to give, and then thirdly, the risk tolerance, and risk tolerance is something very distinct from risk capacity, and we can talk more about that, how in common practice, risk capacity and risk tolerance are often conflated, but they're really very different concepts. So the risk tolerance that we use in the life cycle component is also the same risk tolerance we use in the asset allocation part of the model, and then most importantly is this idea of the economic balance sheet, and just as a company has a balance sheet with assets and liabilities, so does any individual household. On the asset side, they have their financial wealth, but they also have their human capital, and on the liability side, they have what we call their liabilities, which is the present discounted value of future non-discretionary consumption, and then their net worth, and so that entire balance sheet gets fed into what we call a net worth optimization model, which then determines the asset allocation.

Benjamin Felix: What do you think of the unique insights that come from your model setup?

Dr. Paul Kaplan: The insights that just come of any life cycle model are very essential and important in financial planning, which is taking a holistic view of the whole process, focusing on consumption, because after all, the purpose of savings and investing is to be able to fund a person's consumption smoothly over the course of their lifetime. The conventional approach is that it might have a saving rule, it might have a spend-down rule during retirement, and it may have an asset allocation, all of which could also be disjointed from each other. So the fundamental insight is all these things work together, and that consumption should be the focus of any kind of plan for a lifetime.

We do have some unique features in our model. The net worth optimization I was just describing earlier is a unique component and an important insight, and also some of the details about consumption when there's uncertainty, when you're investing in assets that have uncertain future returns, how that should impact your consumption.

Benjamin Felix: We'll definitely come back to the consumption piece later. Can you talk more about the net worth optimization?

Dr. Paul Kaplan: What the net worth optimization does is it takes the economic balance sheet that comes from the life cycle model, it takes it into account so that human capital is treated as an asset held long. Human capital is subject to some of the same risks that financial assets are subject to, namely the risk of stocks and bonds, and we can go into some more detail about that, but for now just to say that the human capital side of the equation is modeled as an asset mix. And then on the liability side, the liabilities, the present discounted value of future non-discretionary consumption also is modeled as an asset mix as well.

So the optimization that we're performing is not on the assets in isolation as the traditional approach is, but rather on the net worth

Cameron Passmore: Interesting. What's included in quote, "holistic investor profiling" that most investors don't account for?

Dr. Paul Kaplan: Traditional risk tolerance questionnaires focus on risk tolerance. They also will typically include questions that are actually not really part of risk tolerance, they're really part of risk capacity. How much risk can you take with your financial assets?

And so they might ask questions basically related to when do you need the money? You're investing this money now and when do you need it? That's a crude way of trying to get at risk capacity.

We get at risk capacity in a more holistic way. The other types of preferences, which I mentioned earlier, which are simply not usually accounted for or even attempted to measure in any way, are those preferences related to consumption over time. There are two particular preferences.

There's one that's called the subjective discount rate, which is basically the idea that to an investor being able to consume something today is more valuable than being able to consume it in the future. So the model says that there's a discount rate that the investor is effectively applying to future consumption so that basically they can compare present and future consumption. This is a central feature of any life cycle model.

The other is called the elasticity of intertemporal substitution, which is how flexible the investor is between consuming between one period and another period. Those preferences are typically not accounted for. There's a similar set of preferences which we have developed for the bequest motive as well.

One is just how strong is the bequest motive. I like to use a phrase that I heard from Professor Moshe Milevsky at York University, who is one of the most renowned experts in this field. He referred to it as "me versus the kids."

How much consumption do I want for myself versus how much larger bequest do I want to leave for my beneficiaries? So that's part of it. And then there's also a similar idea.

There's an intergenerational elasticity, which is how flexible you are between consumption for yourself versus the bequest. These are important preferences which should be accounted for in forming a financial plan, but they're typically not considered.

Benjamin Felix: You mentioned measuring risk capacity directly. Can you talk more about how you're doing that?

Dr. Paul Kaplan: It really comes out of the model and you see it most clearly in the net worth optimization. I'm going to quote Professor Milevsky on this. He published a book some years ago called, Are You a Stock or Are You a Bond?

What he's talking about in that title is human capital. So if you are a tenured university professor, your human capital is very, very bond-like because the university is going to keep paying you year in and year out. You're never going to be fired, so it's like owning a bond for your life.

And so if you have very bond-like human capital, then you have a very high level of risk capacity in your asset allocation of your financial assets. So the university professor, this all, of course, will depend on what their risk tolerance is, but whatever their risk tolerance is, they have the capacity to hold more stocks than a traditional financial planner would say. Because a traditional financial planner might say, oh, well, you don't have that much risk tolerance, you can't hold too much in stocks.

But from a life cycle theory approach, we'd say that the professor can hold stocks in his financial assets because if you look at his overall asset allocation, he's got all these kind of bond-like assets already built in. So that's the tenured professor example. On the other extreme, let's say the stockbroker whose human capital is very much tied to the performance of the stock market.

That person has very little risk capacity because the human capital is so deeply tied in with the market. Even if they have a high level of risk tolerance and the traditional asset allocation approach would say, oh, they should hold a lot of stocks, taking their human capital into account would say, no, they really can't afford to hold a lot of stocks. They really do need to have more of a fixed income orientation.

Cameron Passmore: I'm curious, can you talk about the problems with mixing risk tolerance and capacity assessments?

Dr. Paul Kaplan: They're two different things. It's just conflating two completely different concepts. So if you conflate them, so you give someone a risk tolerance questionnaire and some questions are getting at their risk tolerance and other questions are getting at their risk capacity and then it kind of boils down to one number, which just is a mix of the two.

So that will have certain implications for their recommended asset allocation, but what is it? It's just mixing two different things. Whereas in the net worth optimization framework that we've developed, the two things are kept quite distinct and you can definitely then say, you know, if let's suppose your client was the tenured university professor, you can then explain to them why you're recommending a higher stock allocation because they have based on the risk capacity.

And of course, for the stockbroker, why you might recommend more bonds by keeping the two things separate and distinct and letting the model bring the two together rather than just some questionnaire bringing them together, which is not derived necessarily from any given theory. It's just sort of ad hoc.

Benjamin Felix: The stockbroker and the tenured professor are kind of the textbook, or I guess in the book examples from Moshe. But other than being at those two kind of obvious extremes, how can someone assess the riskiness of their human capital?

Dr. Paul Kaplan: That's where part of the role of the financial planner comes in. We were talking earlier about the profile, you know, how do you build the profile of the investor? And part of the profile are the preferences, but part of the profile also really comes down to what kind of asset allocation model are you going to use to the human capital and liability? It all should be part of the profiling process.

Benjamin Felix: Yeah, it's interesting to think about because the sort of optimal portfolio in isolation, like the mean variance optimal portfolio could be pretty suboptimal for someone when you're taking the full scope of wealth into account.

Dr. Paul Kaplan: Yes, and that's why we think it's important that financial planners use tools that do take a holistic approach.

Cameron Passmore: How do you apply utility theory and utility maximization to financial planning?

Dr. Paul Kaplan: First of all, you create software that implements the model kind of behind the scenes. We don't need to teach the financial planner utility theory, but we should give them a tool where it's applied and give them kind of an interface to that tool where they can express these different types of preferences. And if we have a truly comprehensive profiling tool, then as long as the investor and the financial planner know how to use that profiling tool, the results of it could go into the software, which then kind of behind the scenes do the utility maximization.

Benjamin Felix: How is risk tolerance connected to utility maximization?

Dr. Paul Kaplan: Risk tolerance is one of the preferences that goes into the utility theory. Utility theory is the idea that each investor has their own personal preferences regarding risk, regarding consumption, regarding bequests. And what we're trying to do is we want to try to figure out what those preferences are.

There's a literature within economics, I think it was developed originally by Paul Samuelson, called revealed preference. If you give people a series of choices, you could infer what their risk tolerance is.

Benjamin Felix: It makes sense for risk tolerance. We talked earlier about a bunch of other preferences, like intertemporal substitution. What kind of questions can people be asking themselves to understand what their preferences are?

Dr. Paul Kaplan: Well, we actually have some sample questions in the book. I'm going to turn to those.

Benjamin Felix: Perfect.

Dr. Paul Kaplan: It's called Chapter Two, Holistic Investor Profiling and Sample Questions. "Imagine that you expect to retire in 20 years, that you'll live for 20 years after retirement. Your total budget in real today's dollars, including labor income generated by your human capital and investment income generated by your financial capital is $100,000 per year for 40 years.

That is $4 million. As shown in the following table with option A, you can choose to spend the same real amount before retirement and after retirement. With option B, you spend less prior to retirement and more after retirement.

And option C, you spend more before retirement and less after retirement." So the idea is that, so people that would check option A, they want their consumption to be the same both before and after retirement. That's absolutely smooth consumption.

But the other options, maybe they prefer to have more consumption now, or maybe they prefer to have more consumption later. But that's the idea. This was kind of our attempt, just one of a number of different questions that we have in the book to try to illustrate how to do this.

I wouldn't regard this as a finished product. We would hope that people that have more expertise in investor profiling than we do would basically develop these things more thoroughly.

Benjamin Felix: Yeah, it's really interesting to think about, as opposed to just a risk tolerance questionnaire, like you said earlier, having thought experiments or questionnaires for all of these different parameters. For people watching on YouTube, we will put up that page from the book and show a couple of the questions as we're talking through this.

Cameron Passmore: What is being maximized in your life cycle model?

Dr. Paul Kaplan: Technically, it's the utility of consumption over your entire life. The idea is that you want consumption in every period, but you're facing what's called an intertemporal budget constraint. If I take my financial wealth and I take my human capital and I subtract my liabilities, this is how much net worth I have.

I could use my net worth in an infinite number of different ways over the course of my lifetime, but when we do the mathematical optimization, what we find is that the optimal solution is smooth consumption. That could mean constant consumption over your life or it could mean consumption growing or shrinking at some rate. That's the question I was just reading before I was trying to get at, but that's how it is.

You're looking at consumption holistically over the course of your lifetime and you're taking into account how much benefits you're receiving from consumption each year.

Benjamin Felix: It's maximizing utility of consumption, but taking into account all of the preferences that we've been talking about.

Dr. Paul Kaplan: You're intertemporal budget constraint too. This is actually one of the most fundamental principles in economics, not just in life cycle theory. Every actor in the economy, they face a budget constraint.

You can't buy an infinite amount of anything. There are trade-offs. Some of the trade-offs might be between food and clothing or whatever, but here the trade-offs are between consumption in one year, consumption in two years, consumption in three years, and so on.

So those are the things that we're trying to juggle, but we have to do it in a way that's consistent with intertemporal budget constraint. We can't spend more than we have.

Benjamin Felix: You could have two people that have the same intertemporal budget constraint and otherwise the same overall, whatever finances call it, maybe the same balance sheet, but they could have different preference parameters and they would have two completely different life cycle plans.

Dr. Paul Kaplan: Yeah. They would have different life cycle plans even if their circumstances are the same. One of the ways I like to summarize, what does life cycle finance take into account?

It takes into account three things, preferences, needs, which is the money you must spend on your essentials, so we call that non-discretionary consumption, present discount value of that is liabilities, and circumstances. So your circumstances include your own mortality. In the book, we use a model of mortality that was recommended by Moshe Milevsky.

And then the market, what are your assumptions about the market? What do you think the expected returns on stocks versus bonds is? How risky do you think stocks and bonds are?

How correlated are stocks and bonds? So all these things are all kind of your circumstances. So everything then comes down to preferences, needs, and circumstances.

And that's what we're trying to get through. We're trying to get to the profiling process. That's really what we're trying to get at because we have to gather all this information about the investor in order to construct a consumption plan and an investment plan.

Benjamin Felix: I've got what might seem like a really simple question, but what is the output of the model? We put all this information in, what is it actually giving the user?

Dr. Paul Kaplan: The main output of the model is the consumption plan. How much are you going to consume each year? And another output of the model is how to invest your financial assets.

Benjamin Felix: That makes sense. Consumption implies savings. So it's telling you how much you can spend, which implies how much you should be saving throughout your life cycle. And it's telling you how to allocate between risky and less risky assets.

Dr. Paul Kaplan: So typically it's telling you how much you can translate that into savings before retirement. But after you retire, it flips over to spending down. So for someone who's retired, they're withdrawing money out of their financial assets.

Cameron Passmore: How do life insurance and annuities fit into optimal life cycle capital allocation?

Dr. Paul Kaplan: Life insurance and annuities are important in bequest planning and generating a smooth consumption for your entire life. If you annuitize, you get a stream of income that will continue so long as you live. Versus let's suppose if you don't annuitize, if you just keep everything in conventional assets, you could run out of money.

So annuities help you sort of stretch that over your life. They also will give you a higher rate of return than conventional assets. And Professor Milevsky calls these mortality credits.

It's how much more of a return you get by using an annuity than not using an annuity. And then life insurance is important if you want to set the size of your request over the time of life. Because if you don't use life insurance or annuities, then you accumulate wealth.

And let's suppose during your accumulation phase, you die. You may not be leaving to your heirs as much as you would have liked. So life insurance does help you smooth that out.

In chapter five of the book in particular, it goes into a lot of detail on how to use life insurance and annuities. And the basic takeaway from that is use life insurance when your financial assets are lower than level of bequest. Fill in the gap with term life.

Once you've accumulated enough in financial assets, you don't need life insurance anymore. Now you can start using annuities to extend your consumption out.

Benjamin Felix: How does the optimal annuity allocation get affected by uncertainty about future inflation? Because most annuities are nominal.

Dr. Paul Kaplan: Yeah. Well, that is a problem with annuities, which is, yeah, if they're nominal only, they are subject to inflation risk. I mean, I think there are some annuities which have some kind of inflation protection in them.

It does raise an important practical problem if you can't guarantee their value in real dollars.

Benjamin Felix: In Canada, I don't know markets outside of Canada as well in terms of products, but we don't have, as far as I know, any truly inflation protected. You can buy like a fixed 2% indexation, but it's not indexed to inflation. But we have our Canada pension plan, which is indexed at least to CPI.

That's not exactly an annuity that you buy, but you kind of do as you contribute to it.

Dr. Paul Kaplan: The government's just giving you this annuity, so you don't have to go out and buy it.

Benjamin Felix: To come back to the output to the model, it'll spit out the consumption plan and asset allocation plan. How do uncertain future returns affect the outputs of a life cycle model?

Dr. Paul Kaplan: Well, one way they affect it is in the consumption rule. In the model presented in the book, it's presented mathematically exactly this is how you should vary your consumption in the face of changing asset returns in the asset allocation. Of course, the expected returns, the risks and the correlations are all going to go into the asset allocation model. They will affect it that way.

Cameron Passmore: Why is the probability of survival at each age a key factor in the optimal lifetime financial planning?

Dr. Paul Kaplan: Because it is a lifetime plan. If you're planning for your entire life, it's crucial to have some indication of what's the probability of surviving out to each age. That kind of becomes a really important component of this.

In the book, we talk about this. If you don't have annuities, if you're just, let's say, investing in conventional financial assets, then your optimal consumption plan is no longer going to just be sort of a smooth curve. What's the probability of me living to age 110, let's say?

It's pretty small. I don't want to hold on to my assets just because I might live to 110. We call this a rescheduling factor.

If you start with a, let's say, a smooth consumption curve, we're going to take consumption at the end, extremely high ages, which are very unlikely that you're going to live to, and we're going to spend more when you're younger when it's more likely you'll be alive to enjoy that consumption. If you do want to take the annuity route, then what is the fair price of an annuity? To know that, you have to have a model of survival probabilities.

Benjamin Felix: How do you actually take all this and solve utility maximization problems like we've been talking about that incorporate all of these different pieces?

Dr. Paul Kaplan: In a lot of the life cycle finance literature, they have some really complicated ways of doing that, something called dynamic programming. Anyway, so they don't have a formula for it. They just have a method of solving for it.

We made some simplifying assumptions in the book that do allow us to actually give a mathematical formula for how much your level of consumption be year in and year out, depending on market returns. Your exposure to those market returns depends on your risk tolerance. If you have a very low level of risk tolerance, it's going to be less volatile.

If you have a high level of risk tolerance, it'll be more volatile.

Cameron Passmore: How do spending rules, like the commonly used 4% rule, interact with lifestyle optimization?

Dr. Paul Kaplan: One way to look at life cycle finance is as a critique of those methods. Those methods are ad hoc. They have no economic theory behind them.

The 4% rule in particular came from a study done decades ago using historical data. Then every so often, somebody reruns the study and they come up with a different number. We don't think that's a very useful exercise.

We think investors should be advised to take a holistic way and to focus on their consumption and not on a spending percentage.

Benjamin Felix: That's a great critique. I think it does make a lot of sense. How would the spending path of a retiree using a life cycle model, like we've been talking about, compare to somebody using something like the 4% rule?

Dr. Paul Kaplan: In chapter six of the book, we present all the math and everything behind that. If the person is retired, they're living off their savings that are invested, and the asset allocation being according to their risk tolerance, then year in and year out, they're going to vary their consumption basically on the performance of their portfolio versus, say, the 4% rule. You spend the same amount of money year in and year out adjusted for inflation.

If market returns go very badly for you, particularly at the beginning of your retirement, you can run out of money. I mean, a lot's been written about that, but why run out of money? Why not have a flexible spending rule that's grounded in good theory instead of taking the risk of running out of money?

Benjamin Felix: Could there be a set of parameters in a life cycle model that ends up looking like the spending path of something like the 4% rule, like if somebody really didn't want to have variable consumption in retirement?

Dr. Paul Kaplan: To get to an absolutely flat consumption like that, two things would have to be true. Number one, their elasticity of intertemporal substitution, those consumption preference parameters, more importantly would be the subjective discount rate. If the subjective discount rate equaled the market rate of return, then regardless of the intertemporal elasticity of substitution, that would result in a flat consumption rule.

The other condition, the person would have to take no certainty. They would have to invest all their money in riskless assets. But of course, the 4% rule is all about spending your money if you have risky assets.

So the conditions you need to get to that spending rule, you are completely at odds with the assumptions.

Benjamin Felix: Yeah, that's interesting. How does the path of retirement spending for someone using life cycle model interact with annuities?

Dr. Paul Kaplan: If you can annuitize, you get those mortality credits. Also, it means you can plan on a smooth level of consumption that actually does not depend upon the possibility that you might not live to an old age. I was describing before, if you don't have annuities, your planned level of consumption might be for age 110, it's probably going to be pretty small.

Whereas if you have annuities, your planned level of consumption at age 110 is just going to be on the same curve as your whole life. So annuities allow you to create that smooth consumption pattern. Then you don't have to worry about when you're going to die because it's all been baked into the annuity.

Cameron Passmore: Should consumption be an input or output for financial planning models?

Dr. Paul Kaplan: It should be an output. As we've been discussing here, in a life cycle model, any life cycle model, consumption is the output.

Benjamin Felix: That of course makes sense. It could almost be treated as an input based on the parameters that somebody specifies. If someone has a strong preference for current consumption, that's sort of making consumption an input, I guess as a second order effect of specifying their time preference. Does that make sense?

Dr. Paul Kaplan: Preferences are not the same thing. I mean, the preferences are the inputs. The consumption level is the output.

It would violate the basic assumptions of the model to say that, oh, I've got this level of consumption that I want to have because the level of consumption should be the result of the preferences, not a substitute for the preferences.

Benjamin Felix: Yeah, it's interesting to think about because usually in financial planning, it's like you meet with a client who is spending this amount and you're kind of working backwards from there, which is just very different from consumption being an output.

Dr. Paul Kaplan: Tom Idzorek, my co-author on the book, we also co-authored a paper in the Financial Planning Review, the Hybrid Model. One of the things we do to illustrate, we do illustrate numerically the difference between doing things in this ad hoc traditional way versus in an optimal life cycle way. So pre-retirement, it's saving.

So that's called saving smoothing. That means at each year, as your salary changes over time, that would make your savings different over time, but it would have nothing to do with your consumption. It would just be related to salary.

Then after you retire, there's a rule that says, take your final salary pre-retirement and take 90% of that and spend that for the rest of your life. Those kinds of rules lead to very suboptimal results.

Benjamin Felix: We've talked a lot about life cycle finance and a bit about asset allocation, touch on asset location. How important is asset location?

Dr. Paul Kaplan: Asset location is important because holding stocks and bonds in a taxable account is very different than holding them in a tax-advantaged account. The return on stocks typically comes more in the form of capital gains, and capital gains are typically taxed at a lower rate than ordinary, than dividend income. Then with bonds, they mainly pay interest, which is taxed at the ordinary rate.

So the kinds of after-tax behavior of the same asset in two different accounts can be quite different from each other.

Cameron Passmore: How does optimal asset location deal with the uncertainty of future asset class returns?

Dr. Paul Kaplan: The same way that any other asset allocation model does. Every asset allocation model has baked into it assumptions about the uncertainty of future returns.

Benjamin Felix: Why is solving asset allocation and location sequentially a mistake?

Dr. Paul Kaplan: It's not a sequential problem. You have to invest the money. It's a joint decision.

How do I invest between the taxable and the tax-advantaged? One of the things we do in our net worth optimization framework is that we take that all into account. We look at stocks, how they return in the two different accounts, and how bonds, how they return in the two different accounts.

All that is taken together simultaneously, so you get to an optimal, not just an optimal asset allocation, but also an optimal asset location. You can't get there if you do them sequentially.

Benjamin Felix: Just in terms of the magnitude of the impact of optimal asset location, if you didn't solve for it in one case and did in another, how much of a benefit are you giving up by not solving for optimal asset location?

Dr. Paul Kaplan: I can't really say that unless we're talking about a particular numerical example where we can show the difference, but we do know with any kind of optimization framework, it's suboptimal to optimize in isolation. You're always going to get to a better place if you do one grand optimization taking everything into account.

Cameron Passmore: Why is it important to have a target asset allocation before selecting funds?

Dr. Paul Kaplan: Asset allocation is really important in the investment process. I'd like to read a quotation from Markowitz on this. I had the opportunity some years ago to interview him, and I asked him a question about what's important to happen in investing since he did his famous mean variance optimization paper back in 1952.

Then in 1959, he published a book which gave all the math and everything about how to do this mean variance optimization. He says, "I think the most important thing that happened between 1959 and the present is that the notion of doing your analysis of asset classes in the first instance, this has become part of the infrastructure that we now rely on. In 1959, I had a theory, I had a rationale, and so on.

Now we have an industry." Asset allocation is kind of what made Markowitz's theory into an industry. We recognize now that it's really at the asset class level are the basic drivers between risk and return.

Sometimes we call the asset allocation decision the beta decision, the underlying drivers of return, and that when you pick individual managers of different digital funds, that's the alpha decision where you kind of decided on your asset allocation, and then you pick managers that you believe will add value without adding too much risk.

Benjamin Felix: You've made all of this seem very easy to understand, and you've explained it all in plain English, which is an incredible skill. I'm sure our listeners will appreciate it, but underlying everything you've said is a tremendous amount of math and quantitative complexity. What tools can investors use to put everything we've talked about into practice?

Dr. Paul Kaplan: Tom and I, my co-author, Tom Idzorek, we believe it's really important to get these tools into software. In the end of our book, we have these calls to action on the industry, and one of them is develop financial planning software that is based on life cycle theory, rather than just sort of these ad hoc tools that we've mentioned before. Now, as a step in that direction, I've developed a spreadsheet that actually implements most of what we've talked about in the model, at least on the life cycle part about that.

Now, the focus of the spreadsheet is on consumption and very high-level asset allocation. The rest of the model, in the book, we divide the three parts, the parent model, which is the life cycle model, life cycle theory, the child model, which is the net worth optimization asset allocation model, and then the third part, which we haven't discussed too much here today, is what we call the grandchild model, which is basically how do you take the outputs of the child model and pick actual funds. And to pick actual funds, you have to come up with these alphas or these additional expected returns, and you also have to take into account the additional risk that you're adding when you use an active manager. You can stop just at the asset allocation level and just use index funds, in which case you're getting the beta effects, just the risk and return of the different asset classes.

When you use active managers, you may or may not get an alpha, but you definitely will get more risk in the portfolio. So that's what the grandchild model does, it manages all that. So if you like, I could just go and pull up the spreadsheet model.

Benjamin Felix: I would absolutely love that.

Dr. Paul Kaplan: So what I have in these yellow cells are all the inputs to the model. So the age, the sex, one of the features of the model. It's very easy to change a person's longevity assumption.

That's again because of the model that Professor Milevsky recommends, it makes it very easy to do that. Then how far off do you want to model? And then we have these preference parameters, which ideally should come from some kind of profiling tool, but this is just a spreadsheet, so I just put some numbers in here.

Your non-discretionary consumption is $50,000 a year. I break down your asset allocation of your current assets between stocks, domestic stocks, global stocks, bonds and cash. When you retire, so you're going to retire at 66.

What your current salary is, there's also a piece in here where you can include an employee match. In this example, you're contributing $15,000 a year and your employer is matching that at 50%. So in other words, the employer is adding $7,500 to your account each year.

How much do you want to annuitize? Bequest preferences, again, they should come from, okay, what type of bequest do you want? Then we get into income.

So we use a model here that was developed at Morningstar where basically you put in a person's education level and their sex and it comes up with a salary curve. This part here, you put in your allocation of human capital. So your human capital here, I say it's 20% as an equity exposure, 25% of which is global stocks.

Then my liability, I just said it's 15% equity and 0% global. Then it calculates for you a bunch of numbers which are described in the book. So there's the match.

It has built into it an estimate of U.S. social security. So if you want to use a model like this in Canada, we would have to substitute the social security model with the CPP model. Your financial wealth is $1.2 million. It calculates your net worth. This is your balance sheet, how much you have in financial wealth, how much you have and how much you have in net worth, how big your bequest is, $1.5 million. Then you go here.

These little charts are probabilistic projections. We start with the most important one, which is total consumption. The heavy blue line, that's the expected value.

In this example, we have consumption growing at an expectation at a constant rate. I think I have the rate here. So the growth rate is 0.45%, which is derived mathematically from the model. Then each of these things represent probabilistic forecast. So if markets go really, really well, if the market is very kind to you, it shows you can really increase your consumption quite a bit. If markets go very, very badly for you, well, you still have something you can consume, but you consume a lot less.

Unlike the 4% rule, it doesn't go to zero. You still have something. You modify the amount of money you spend.

The next one is the financial wealth. The shape of it makes sense. You grow your financial wealth while you're working, and once you retire, these numbers come down.

And again, the top one is the 95th percentile. So there's a 1 out of 20 chance things will be this good, and there's a 1 out of 20 chance things will be that bad at the bottom. So we think this kind of output is important in financial planning.

Give the investor a picture of how their consumption and financial wealth might change over time. The next picture is human capital, which you can see human capital, remember we said it was 20% equity. It's a lot less riskier than your financial wealth.

Mainly, it goes down over time, right? That makes sense because human capital is the present discounted value of your future salary. So as you get older, you have less and less future salary, so you discount it to the present.

It's going to be lower. And then the net worth, which is really important because that's what really drives everything. That's what the intertemporal budget constraint is all about.

How much net worth you have is what determines how much consumption you can do. And you can see it kind of spreads out at the beginning, and eventually over time, it's going to decline as your human capital is declining, as your financial wealth is declining. It makes sense that you expect your net worth to decline over time as well.

Over here, we have some economic balance sheets.

Benjamin Felix: Did I understand correctly, Paul, that the output is consumption, but asset allocation is an input in the model?

Dr. Paul Kaplan: No, asset allocation is also an output.

Benjamin Felix: Oh, okay, okay.

Dr. Paul Kaplan: This is just to give you an idea of what an economic balance sheet is. The green areas are in dollars. So there you can see we have your financial wealth and your human capital on the one side.

Then we break it down between asset mixed representations of each of these things, domestic, global stocks, total stocks, bonds, cash, and total. On the other part is the liabilities and net worth. So there you can see liabilities is broken down based upon how much life insurance has an impact on your liabilities.

Because if you want to commit to having a certain level of bequest, you also are committing to holding life insurance. So anyway, it breaks it down here again the same way. And then what we do right below it is we just do it in percentage terms.

If you're thinking about asset allocation, this is saying your financial wealth is 37.5% in stocks, 50% in bonds, and 12.5% in cash.

Benjamin Felix: This is normative. This is telling you what you should be doing.

Dr. Paul Kaplan: This is telling you where you're at right now. That's why up here it says your current asset allocation. So this is where you are, and this is the direction where things might go.

In order to get the actual asset allocations, you can't get it from the spreadsheet. You have to use the net worth optimization model. But this is just designed to give you a sense of where you would go on this.

You might end up with a more cash-oriented portfolio. Human capital is really big in bonds, 76%. And then the same thing, liabilities and net worth.

So it breaks it down. So these are meant to be indicative.

Benjamin Felix: I know this is just an example, but what would drive such a high cash allocation when human capital in this example is so safe?

Dr. Paul Kaplan: If you have a very cash-like liability, like the life insurance in this case, it's very cash-like because life insurance premiums aren't going to fluctuate with the stock market. You just pay them year in and year out. So that's, in this example, what's leading to a high cash allocation.

Benjamin Felix: Which parameters, like if we go back to the inputs, which parameters would have the biggest impact on those optimal allocations?

Dr. Paul Kaplan: Risk tolerance, for sure, because that's going to determine your overall asset allocation. It's going to be driven by that risk tolerance. And so risk tolerance here is set to 55%.

What we've done in this example is we said, then your total asset allocation, ideally we would like to get your asset allocation of your net worth to be at 55% equity. I think that's probably going to be the single most important parameter here in driving this. Now, the other parameters that are going to drive the asset allocation of your financial assets are going to be the things that set the size of human capital, which is your salary, the main parameter, your liabilities, which is the example we just set it here to $50,000 a year, and then these asset allocations that you put here.

The numbers you put here in this part of the spreadsheet, that gets back to the stock broker versus the tenure professor.

Benjamin Felix: Super, super interesting. This spreadsheet is available online. People can use it.

Dr. Paul Kaplan: Yes.

Benjamin Felix: Very, very cool. I'm sure a ton of listeners are going to be spending way too much time in here.

Cameron Passmore: You bet they will.

Benjamin Felix: Yeah, they will for sure. Why is it that the financial services industry, which has some pretty great financial planning softwares, great in terms of user experience and they're comprehensive and that they incorporate all kinds of taxes and all that kind of stuff. Why don't we have this type of software?

Dr. Paul Kaplan: It is a paradox. One of the things we have in the book is we actually have a list of all the Nobel Prize winners who have made an important contribution to life cycle finance. This includes Milton Friedman, Franco Modigliani, Paul Samuelson, Robert Merton.

Their work has been recognized among economists, but why hasn't it worked its way into financial planning practice? I don't know. There is a disconnect between sort of what we know is right, there's so much theory behind it, and what we actually do in practice.

Benjamin Felix: What role do you see just more generally for financial advisors in life cycle financial decision-making for households?

Dr. Paul Kaplan: Financial planners, I think, play a very important role in coaching and leading their clients towards rational approaches. Obviously, there's now been a lot of literature on behavioral economics and behavioral finance. We know that real human beings do not behave anything like the agents in economic models.

There has been a disconnect between economic theory and practice. So we think that the role that the financial advisor has, if the financial advisor has, let's say, a life cycle-based tool that they can use, then it really is to advise their clients to behave in this rational way, in a way to save the clients from themselves.

Benjamin Felix: We've always kind of thought about it as not necessarily tell the client what to do, but tell them what a rational person in their situation would do so they can understand the trade-offs of doing something different, which they may still want to do because they're not a perfectly rational agent, but they can at least understand the trade-offs that they're making. How has your research on this stuff influenced your own finances over time, as you've studied this and modeled it?

Dr. Paul Kaplan: I have to admit that I haven't actually run a life cycle model, but I'm in good company. Harry Markowitz, the father of modern portfolio theory, was once asked, how do you do your asset allocation? His answer was, well, I know I should be running an optimizer, but what I actually do is I do 50% stocks and 50% bonds.

I'm kind of in that school, yeah. I know the theory and everything, but I retired a little over three years ago now, and I haven't changed my consumption patterns when I retired, so I think I am on a smooth consumption path. The other thing, and this is not directly related to this research, that is the value of indexing.

I mentioned earlier that an active manager may or may not add alpha or additional return to your portfolio, but they're certainly going to add risk. I do some indexing as well, and I think that's pretty consistent with my approach. In some ways, I do think about the asset class level more than I do about any individual product.

Benjamin Felix: We think about it the same way and spend a lot of time on this podcast talking about the benefits of indexing. We did talk a little bit about factor investing and tilting toward sources of higher expected returns within an asset class, but broadly speaking, we would be in agreement with you.

Dr. Paul Kaplan: There's a whole other line of research that I've been doing together with Tom Idzorek, the co-author in this book, and also Professor Roger Ibbotson at Yale, who Tom and I used to work for at one time, was called Ibbotson Associates. It was bought out by Morningstar in 2006, but we've been working with Professor Ibbotson on these very issues. We have another book.

Also, it's published by the CFA Institute Research Foundation called Popularity: A Bridge Between Classical and Behavioral Finance. There, in that book, you'll find our whole theory about why there are these factor premiums, basically. We also did an article called Domesticating the Factor Zoo, I think in the Journal of Portfolio Management, where we talk about how you even identify a factor.

It can't just be that it pops out of the data. It's got to also be backed up by economic theory. You have to come up with an economic theory about why a particular factor should pay off.

Then there's another paper we did in the Journal of Investment Management, which I'm proud to say we received the Harry M. Markowitz Award called the CAPM, APT, and the PAPM. The PAPM comes from our popularity book, the Popularity Asset Pricing Model.

That goes more into where we think factors should come from. We think it comes from preferences. We did incorporate these preferences in the third part of the book, The Grandchild Model, where we take into account for every fund, we have it exposed to certain characteristics.

Then we combine that with what investors' preferences might be regarding those characteristics. That would lead to certain factors paying off.

Benjamin Felix: Very interesting. We actually talked about your popularity book in episode 174, which was back in November 2021. We did an episode on whether a "good company," in air quotes, is a good investment.

It relates directly to your book. We talked a whole bunch about what you guys talk about in the book and the research findings in there as well.

Dr. Paul Kaplan: Who did you interview for that?

Benjamin Felix: Nobody. We alternate between having a guest and doing an episode where Cameron and I do a deep dive on a topic. That episode was a deep dive where we were just talking about that general idea of asking the question of whether a good company is a good investment.

Your book was an obvious source for that discussion.

Cameron Passmore: Our final question for you, Paul, how do you define success in your life?

Dr. Paul Kaplan: Let me talk about it maybe first and just in terms of my career, which is I think I've made some positive contributions here and there. And doing things with rigor and integrity, I think is important. If you look at all my work, be it this book on life cycle finance or the book on popularity or my first book called Frontiers of Modern Asset Allocation, published in 2012 by Wiley, everything I write in there, everything has to follow from first principles.

I was trained in economics where your conclusions have to be based upon the first principles. I've tried to apply that principle to everything I've done professionally.

Benjamin Felix: Incredible. We very much appreciate the work that you've done in this book and your other work and research. This has been a fantastic conversation.

I know listeners will get a lot from it and even more so because they can take what they've heard and bang around in your Excel spreadsheet to see things for themselves.

Cameron Passmore: It's great to have you on. Great to meet you, Paul. Thank you.

Dr. Paul Kaplan: Thank you. Good to be here.

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