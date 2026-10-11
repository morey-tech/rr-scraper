## Episode 393

Ben Felix: This is the Rational Reminder Podcast, a weekly reality check on sensible investing and financial decision-making from two Canadians. We're hosted by me, Benjamin Felix, Chief Investment Officer, and Braden Warwick, Financial Planning Product Architect at PWL Capital. Welcome to episode 393 and Braden, welcome back onto the podcast.

Braden Warwick: Thanks. It's exciting to be back.

Ben Felix: Yeah, you're back by a couple of reasons. 

People may notice that we have a couple of non-guest episodes in a row. We did have a guest cancellation that we were not able to recover from or fill in with another guest on short notice by popular demand that we knew we had to have Braden back on because when you were on with the other folks from the FP Canada panel, we got great feedback on your appearance and the nerdy folks in the Rational Reminder community loved your nerdiness, which is no surprise. We figured this was a great opportunity to have you back on to talk about engineering financial outcomes, which is a great topic. 

We are going to dive into that in a second. Real quick before we do that, we have a webinar coming up on February 12th, a live webinar that will have Q&A moderated by PWL financial planners. The topic of that webinar is how much do you need to retire in Canada? 

We have done this webinar once before and it was very well received. The older version is up on the PWL Capital YouTube channel and this one will be as well. But if you want to attend live and ask questions to PWL financial planners about the content, that is on February 12th at noon Eastern time and we'll put a sign up link in the episode description for this podcast episode. 

Now we're going to talk about engineering financial outcomes, which is kind of what you've been doing since you joined PWL, Braden. I don't know if I've mentioned this on a podcast in the past. You joined kind of to work with me doing research stuff.

Then we started doing stuff and I was like, oh, you can build applications and write code? You're like, yeah, I don't know, I guess. Then I was like, cool, can we build an app to do this thing? 

You learned a lot on the job. You became much more proficient at building applications, but we realized pretty quickly that you can actually build software that solves pretty complex financial planning problems, which has been awesome. We've really leaned into that and you've been able to focus on that a lot, which has been really exciting for PWL and our clients and I think for you too, which is awesome. 

To kick off this discussion about engineering financial outcomes, coming from an engineering background, which we can talk more about your background as we go here, what do you think in general about the current state of the financial planning process?

Braden Warwick: To give a little bit more color to Ben's commentary too, I think I joined PWL as someone who was already listening to the podcast. So I was a podcast listener first, joined PWL. And Ben, of course, has this whole list of problems that he needs me to solve. 

I think it was kind of lost a little bit before I joined that I was teaching courses, programming courses at the university. So I was already pretty proficient at coding coming in, but it's a completely different world coding to solve engineering problems, and then building software that other people are using that needs to be user friendly. So I think that's what I learned a ton of on the job. 

More recently, since 2024, I've been leading the deployment of Conquest Planning, which is a third party planning software. I would say it's industry leading planning software in Canada, at PWL. That's been a really cool opportunity because prior to that, my only experience was in the PWL bubble, so to speak. 

I went from academia to PWL. That was my only experience in the wealth management world. Deploying Conquest, I got the chance to meet more people. 

I got to talk to people that had a similar role to me that were working at other institutions in the industry, deploying Conquest, except they were at much larger institutions. So they were deploying Conquest for like 100 times more advisors and planners than I am at PWL. So it was interesting to talk about our challenges. 

And for us, it was pretty smooth deploying Conquest. Thinking back to 2024, we had Mark here still at the time, and he was already using Conquest. And he was a big advocate of moving forward with Conquest at PWL. 

So he was a power user of Conquest, but he's also a great communicator and great planner. And then we also had me that spent a full year basically trying to set up the configuration of Conquest so that it is kind of optimized for how we do things and how we solve problems at PWL. So putting the two of us together, it was pretty easy to train advisors and to get planners on board with making that change. 

It was incredibly eye-opening to talk to other people in the industry about their challenges with using or with deploying Conquest. And what really blew me away was when I talked to someone who said that their biggest challenge is not only having to train experienced financial planners, people that have been working with clients for decades on the new software, but then also at the same time having to train people that were literally selling furniture last week, how to use Conquest and all of the advanced features and functionality that Conquest has to offer. 

So just hearing that in person, hearing those words from someone who's experiencing and living those challenges was incredibly eye-opening because we hear the marketplace studies, we talk about it on the podcast, we kind of get a sense of what the state of the industry is. But then to actually talk to people that are going through those struggles, it was just wild to hear.

Ben Felix: It's an ongoing tension in the financial services industry and in Canada and I'm sure elsewhere as well, where the industry has this tension between wanting to accommodate people who were selling furniture last week and not making the bar too high for them to get their licenses, which is like, okay, but then they also want to be a profession and it's like, okay, we want to keep the bar low enough to let people who don't have a ton of financial background and knowledge get into the industry, but that doesn't really work if we want to be a profession. 

Some of that's changing slowly. I think the proficiency requirements are getting a little bit better. It's interesting that you noticed that from the perspective of deploying a financial planning software, where it's the same thing. 

The software and the people deploying it have to cater to and work with people who don't have the knowledge of the average advisor at PWL.

Braden Warwick: That's exactly it. When you look at from the software providers' perspective, if you think in terms of the volume of plans that are being created in Conquest, a very small percentage of those plans are being done by advisors like us at PWL or some of our counterparts in the industry that are doing high quality, in-depth, rigorous financial planning with a focus on improving client outcomes. And the bulk of their plans are being done by people that are looking to create an illustration to sell a product. 

That's just kind of the reality and talking to the people that are building the software at Conquest and other planning software companies, they all want to do what's best. It's not a commentary on them personally. It's just the reality of our industry. 

And I think the only way to change that is to shift consumer preferences away from those people that are just selling product and towards people that are doing in-depth, rigorous analysis so that that voice can be stronger and pushing on the product roadmap. So all of this eye-opening discussion with the peers in my industry got me reflecting on my own experience and my own skill set. And it led me to feel a certain amount of obligation to share what I've learned in academia, learning from some of the top minds, engineering and physics. 

So I think that's what we're going to do today.

Ben Felix: We kind of glossed over this. You have a PhD in mechanical engineering with a focus on aeronautics. You were working on research on aircraft vibration minimization prior to joining PWL and you were teaching. 

You came from that world of academia, research in engineering. I like to say that you're literally a rocket scientist because it's true and it sounds cool. But then you decided to make this career shift into financial planning. 

So I think your perspective on the financial planning process and how it's executed and how we think about it coming from where you've come from is super interesting. Like you said, that's kind of what we're going to focus on.

Braden Warwick: Thanks, Ben. I don't like to take too much credit, but I think just reflecting on the experience that I've had, my advisor, for instance, he developed courses of computational optimization at MIT. He's a super sharp mind. 

I learned a ton from him. I feel like this obligation to pass down that knowledge that I've learned from some of the top minds to help benefit this industry. And I think even when we think about some of the top financial planners in our industry, I think even just learning a little bit about the engineering approach to problem solving could benefit everybody. 

I hear this all the time, but I hear financial planners saying things like, the only thing that we know for certain about this plan is that it's wrong. And personally, this way of communicating drives me crazy. I understand the sentiment that they're trying to make, and I know that they're kind of saying it tongue in cheek, but it really doesn't matter.

Ben Felix: Can you describe the difference between a financial plan and a financial planning projection?

Braden Warwick: For sure. I think we need to do a much better job of communicating the difference between those two. And I'm sure some people will think I'm being pedantic about this, but it is a really important concept. 

The way I think about this as an engineer, I think that a financial plan is equivalent to a design for an engineer. It's a collection of the decisions that we make using the information that we have available to us today. We make these decisions using data and mathematical modeling to support those decisions, or in the financial planning world, those are the financial projections that we're doing. 

But the projection is not the plan. It's used to develop the plan and make those planning decisions, just like computational modeling is used to drive the real-world, data-driven decision-making process that's used to develop designs in the engineering world. As an example, just imagine an engineer that is designing tires for a car. 

And imagine the goal is to create the longest-lasting tires possible. Now, imagine the engineer saying, the only thing we know for sure is the design is wrong because we don't know for certain that these tires are going to last 102,670 kilometers. It sounds crazy. 

Of course, we don't know how long the tires are going to last. We don't know what type of vehicle the tires will be driven on. We don't know how fast the driver will be traveling on average, or what weather conditions they'll be driving in, or how well the roads are going to be maintained in the area that they're driving on.

The engineer doesn't know the answer to any of those questions. Does that make their design wrong? No, of course not. 

Just like not knowing what the stock market is going to return or what the client's RRIF minimum withdrawal in the year 2047 is going to be, it does not make the plan wrong. The plan is probably rock solid if it's done with care by an experienced financial planner. So I encourage people to stand by their work.

Another example of this could be in the medical world. Imagine Ben going through what you've gone through. And at the beginning of that process, the physician said, so Ben, here's your medical plan.

This is what we're going to do, these are your treatments. These are the tests that we're going to do. But the only thing we know for sure is that plan is wrong. 

It sounds absolutely crazy in that context, right? No physician's ever going to say that. But it's the same line of thinking. 

The physician doesn't know with certainty that that plan is going to work. They don't know if the cancer is going to spread. They're making decisions based on the information that they have available today, based on your test results and the medical literature. 

They also understand that there's a range of possible outcomes, and they try to prepare you for those possibilities. And as more information becomes available with new test results and so on, they can adjust and change the plan accordingly. Now, don't get me wrong. 

I think good financial planners are also doing this. But I think we should try to be more professional in the way we communicate planning and decision making under uncertainty. The wild thing is to me is that so many of our clients come from a technical background. 

We have a lot of physician clients, or we have a lot of engineering clients, or even business leaders. Business leaders is another example where if you are running a business and you don't know what the ROI of investing in technology is, or investing in more marketing is, or how do you make those decisions? How do you evaluate the trade-offs of investing in one area versus the other? 

A lot of our client profiles are making these similar types of decisions in their own world. Communicating this thought process properly and technically will resonate with them. And I think that can go a long way to help building that trust relationship from the onset.

Ben Felix: I like that framing of the issues a lot. I think you're right. I find physicians are generally quite good at explaining. 

Here's what the evidence says. We're doing this treatment because here's what the evidence says. Here's what the statistics say about whether this treatment is going to work or how it's going to work. 

Here's what we'll do if it doesn't work. Here's what we'll do if it does work. And laying things out that way, I think it's a really, really nice way to present information.

Evidence, range of outcomes, plan in either of those cases.

Braden Warwick: Totally. And I don't think there's any reason why we can't take that same communication approach with financial planning. And actually, when you think about the client profile of both the physician and the financial planner, the physician probably has to speak to a much wider range of skill sets and backgrounds and education levels than the financial planner does, which is typically working with higher net worth people. 

Financial planning is already severely undervalued in our industry. We see that even with our own content. Everyone wants to hear about the AI bubble or ETF slop or other investing related content, but nobody wants to hear about goal setting and taxes and death, which are all central topics to financial planning. 

And out of the two, financial planning will have a much bigger positive impact on the expected financial outcomes. I think avoiding a lot of that other stuff will make an impact, but it's usually just avoiding the negative stuff. But if you layer on financial planning on top of that, that's when you can actually start to increase the expected outcome beyond just markets work, invest in an index fund and so on. 

It's super important for planners to communicate professionally, but also take pride in their work and feel confident that they're making a difference in people's lives.

Ben Felix: It is crazy, though, how our audience, which tends to be nerdier, does tend to still appreciate the financial planning topics. We have done ones on goal setting. We've done ones on mostly other stuff that you mentioned there. 

But if we go and look at the data on viewership and downloads, those topics perform much worse. AI bubble, ETF slop, anything about investing does tend to perform way better. I think you're totally right that people are just less interested in the financial planning stuff. 

How would you describe the engineering approach to financial planning?

Braden Warwick: It all starts with goals and understanding your client's goals is the most important part of the financial planning process from my perspective. Because if you don't know the client's goals, the rest of the work is kind of meaningless. You're not really helping the client's money work for them in the way that will benefit them the most. 

But if you think about this in the engineering context, it seems obvious. If we're building a car, are we trying to build the fastest car or the most luxurious car or the best value proposition or the most family-friendly car for traveling and things like that? It's pretty obvious that you want to focus your efforts on specific goals and design the product accordingly. 

What's interesting about this is that it's also pretty obvious that those different goals require different solutions. If you're trying to build the fastest car, you're going to probably focus on having a very powerful engine and all this other stuff. And if you're building a very luxurious car, the focus might be on quality of materials and the quality of the ride and the smooth ride and a quiet ride and all those things that go into that more luxurious experience. 

It seems fairly obvious to think about it that way because you can see those things in real life. You can see how those cars differ just by looking at them. The same can be true in financial planning. 

Depending on goals, there might be different planning strategies that would be suitable for someone with one set of goals and then a completely different set of planning strategies that work for someone else with a different set of goals. In order to actually know which set of strategies to implement with the client, you need to figure out what their goals are first. And I think that, again, coming back to the software stuff, the software is kind of laid out for the person to take the happy path and not necessarily have to have these larger reflections. 

And that happy path could lead them potentially down the wrong road, which we'll see later on. So another point to this, too, is that in terms of goals, it's not really up to the engineer to figure out what those goals should be. Unless the engineer is, of course, running the company, and then that's another story. 

But for the average engineer that's responsible for designing the tires like I had in the previous example, the goal is set by the business need and the gap that the product's trying to fill in the marketplace. In a similar way, it's not up to the financial planner to set the goals for the client. But on the other hand, they can also coach the client through the goal setting process and the self-reflection process. 

I think that the gold standard for goal setting in terms of financial goals is laid out in your work, Ben, in Finding and Funding a Good Life. And I don't want to go into all that here. But I will say that goal setting is going to require a lot more internal reflection than most people are expecting on the surface. 

So it's important to dedicate, to carve out time to actually think through those goals before you get too far along in the process.

Ben Felix: We had the Finding and Funding a Good Life paper. And then we also did the Goals Master List that we did that through our podcast audience and some of our clients. We surveyed a whole bunch of people to figure out common financial goals. 

A lot of people have, and we talked about research, showing that to people helps them set their own. Anyway, we've done a lot of work on goal setting, and we do try to apply that with clients for the reasons that you talked about. We as the planners need to make sure that the client is setting the right goals, which is often not the case on the first pass. 

If you sit down and ask someone, what are your goals? You might get information that's not actually what they care about when they reflect on it with the proper guidance.

Braden Warwick: That's exactly it. I think typically clients will show up with something in mind. And oftentimes it's, they want you to maximize their returns or to minimize their taxes. 

When you talk to the average Joe on the street, that's when they think of a financial advisor, they think about increasing returns and market beating returns and all of that. Or they think about from the accounting perspective of trying to minimize tax. I think both of those are kind of surface level goals.

They don't really get to the heart of what the client wants to accomplish with their life, what they prioritize and what their true wishes are. So I think going through that goals exercise helps you dig a little bit deeper than those surface level goals and get to the meat of what the client actually wants. And it's interesting too, the tax goal, I think is a super interesting one. 

I was listening to the Wealthy Barber podcast recently when Aravind was on and Dave made a great point that so many people focus on avoiding probate tax, which is literally one and a half percent in Ontario, that they put themselves in a significantly worse financial position than if they didn't worry about it at all. And I think this line of thinking that leads to avoiding tax or minimizing taxes at all costs, it's the same line of thinking that makes people scared of contributing to an RRSP because that gets taxed down the road. And it's the same line of thinking that leads people to take CPP as early as possible because they want to get rid of that payroll deduction as soon as they can at age 60 and start to collect those benefits as soon as they can. 

And I think there's so many reasons why people might think this way. I think a lot of it is due to a lack of education and understanding of these personal finance topics. But some of it's also due to a bit more of a deeper behavioral bias that's a lot more difficult to overcome. 

But nonetheless, I think it's important to challenge this goal if you're faced with this goal as a planner to challenge it, to present alternative views of what to focus on, to talk about their family, if they have a family, do you want to take more vacations? Do you want to save for your grandchildrens' education? Do you want to retire earlier to spend more time with your grandchildren? 

A lot of these goals are going to require paying a little bit more taxes because a higher income leads to higher taxes. They go hand in hand, but what actually matters more to you? Would you rather have more life experiences with your family and pay slightly higher taxes or do you want to minimize both your taxes and your life experiences?

Ben Felix: That's really interesting to think about. When we're doing financial planning and we've identified those goals that actually matter to the client, how is a financial plan evaluated against the specific goals that somebody has?

Braden Warwick: Once you have those goals, again, I think that's easier said than done, carve out actual time to go through that. Once you're there, we can start running the projections. There's a huge amount of emotional intelligence that's required by the advisor to help coach through the goal-setting period.

But now I think that's where that emotional intelligence switches to a need for a higher IQ. Because evaluating a plan against the client's true goals requires a little bit more work and a little bit more thought. If the client's goals are in line with maximizing their final estate value for the purposes of multi-generational wealth or for a charitable donation, I think it's pretty straightforward to solve for this using traditional planning software. 

Conquest, for example, has an estate value, a legacy goal KPI that you can plug right in and it will tell you what the after-tax estate value is for the projection. It's pretty easy just to use the software in the way that it's designed to come up with that answer directly. You can look at the expected outcome based on the expected assumptions, but you can also look at the expected range of outcome by introducing uncertainty into the assumptions, whether that's in a volatility analysis with market uncertainty, or you could look at what-if scenarios looking at introducing uncertainty to other assumptions like inflation or longevity and so on. 

And another term I'd love to add to a financial planner's vocabulary is a sensitivity analysis. And I remember Joe brought this up two episodes ago. We mentioned it, but we didn't really go into much detail about it. 

At its core, a sensitivity analysis is all about determining which variables make the biggest impact on client outcomes so that we can focus on what matters. And I think that's an extremely important concept to understand. It's really difficult. 

I think for planners, there's so many variables out there. There's so many different strategies and it's difficult. We want to help the most amount of clients possible, but we also want to dedicate enough time to each client scenario so that we can improve their outcome. 

But thinking through this framework of a sensitivity analysis allows us to prioritize what matters, what's going to make the biggest impact. For example, we were recently doing asset location research, and I don't want to get into too much detail about this now, but we're able to pinpoint exactly the client profile that asset location will make the biggest impact on. So then when we're thinking for an advisor that has 200 clients, they can focus on that for a small portion of their clients, and it's going to make the biggest impact for them. 

And then for those other clients, they can focus on something else that's going to make the biggest impact. That's really where the sensitivity analysis comes in mind. And I think coming back to that conversation about having the technical clients, I think a sensitivity analysis is a really nerdy word that people resonate with. 

If you're a technical person, like I remember when Joe said it for the first time, I was like, yes, this is what we need to talk about. It's just something that the technical person, they live and breathe doing a sensitivity analysis to figure out how to prioritize decision making in their world. So if you take a similar approach, then I think it can build that trust relationship from the onset.

Ben Felix: I think it's even for less technical people, a technical person like you gets excited when you hear the word sensitivity analysis, but a less technical person still gets excited when you explain to them, not necessarily what a sensitivity analysis is, but you explain to them why this specific variable matters for them. If you're able to explain, here's what happens. It's kind of like my medical analogy earlier, my extension of your analogy. 

The doctor can tell you the expected range of outcomes and which variable matters for that expected range of outcomes and how you're going to address the different types of outcomes that you can get, depending on what you end up getting. I think people do resonate with that, even if they're not technical. If you can say, here's what happens if returns are not as good as we expect, or here's what happens if we implement this planning strategy instead of that one. 

People do get that. I think normal people do get excited when you show them stuff like that and explain to them, here's the specific thing that you should focus on. Here's why it matters.

Braden Warwick: Totally. I think that's a great point. The technical people are going to love the details of a sensitivity analysis, but just the average everyday person is going to really resonate when you talk about these are the things that are going to have the biggest impact for you. 

And we're not just painting the same brush for all of our clients. We're actually doing a personalized analysis to figure out, given your situation, this will have the biggest impact. So let's focus our efforts there. 

I think it's super important. So I talked about the idea of having a net worth, a maximizing multi-generational type goal, or maximizing multi-generational wealth type of goal. But that's one type of client profile. 

I think it's probably more common for clients to want to be able to draw down from their portfolio to increase spending on... It could be spending on trips with their family. It could be spending more on their hobbies. 

It could be setting up an RESP for their grandchildren. Like I talked about, all of those cash flow-related goals, it requires a little bit different approach that often involves a little bit more work and more thinking involved. When we think about answering that question of how can we increase cash flow so that the client can spend more money on those goals, we need to figure out what is a safe amount that the client can be spending. 

We use something called a sustainable spending analysis. And that's where we use volatility analysis to determine what those range of outcomes are. And then we try to make sure that the client is comfortable with those lower than expected outcomes. 

We can solve for the amount of spending that the client can spend if we set a constraint on the success rate of those plans. I think when you approach it that way, it becomes super important to categorize spending into both needs and wants. So this way, we can make sure that the client can always meet their spending needs level, but then they can take a little bit more risk in their spending to try to maximize their wants. 

And I think that's super important because I don't imagine many people are going to want to maximize their spending at the cost of potentially being without a home during retirement or something. That's probably not an acceptable trade-off for most people. Most people want to make sure that their basic needs are met. 

If we can optimize for increasing the amount of trips that they can take, then I think they're a lot more comfortable with that, making sure that they have a baseline quality of life guaranteed. When we think about it that way, engineers like to think about problems in terms of objectives, which is the goals that we've talked about, and constraints. The way I've set this up with the spending needs, that's really a constraint on the problem. 

We need to guarantee that this level of spending is met. And I just want to highlight that for an engineer, it's super important to define these constraints. When you're designing cars, they have to pass the crash test. 

You can make a car as fast as possible, but if it doesn't pass the crash test, then it's not going to be allowed on the road. So there's a whole bunch of real-world constraints in the engineering process that we have to follow. It should be the same thing for financial planning. 

We need to figure out what the client's comfortable with and then set those up as constraints on the problem so that the solution actually works within the bounds that the client's comfortable with.

Ben Felix: Another big constraint for a lot of people would be the amount of risk or volatility they can endure. If someone doesn't want to take on very much volatility in their portfolio, it's a big constraint. We have to limit their expected return based on how much volatility they can take on. 

That's definitely super important. We do have an episode, so this is 393. In episode 395, so in a couple of weeks, we do have an episode with someone who has a ton of expertise on risk tolerance and risk profiling. 

We have some pretty good discussion around that stuff coming up in a couple of weeks. You've talked about how important it is to understand goals and constraints so that we can build plans around that to give clients the expected outcome that they want for a goal. What happens when a client, as they almost always do, has multiple goals that they care about? 

Braden Warwick: Generally speaking, this is where there sort of is this gap. I hear it all the time from experienced planners that they try to discount the value of the mathematical modeling because they think that the mathematical model doesn't reflect reality. This is just such a perfect example. 

Clients don't typically have one goal. They typically have a combination of goals. Oftentimes, those goals inherently have trade-offs between them. 

The software is not really designed to lead you down figuring out how to evaluate those trade-offs between multiple goals, especially multiple competing goals. I hear it all the time. It's a bit of a misconception that the mathematical results don't matter because they don't capture these interpersonal things or what the client really wants.

But I just disagree personally. I think that the existence of that gap in the software is actually an opportunity for the financial planner to add value. The software itself has a long way to go before it can handle this level of detail in a user-friendly way. 

But the existence of that gap allows the planner to come in and really have these deep conversations about the client or with the client about their goals. And they can run the analysis and present those trade-offs, quantify those trade-offs to the client to help them think through those trade-offs between the goals. So you can really use it to help drive the decision-making process in a data-driven, evidence-based way. 

As an example, let's continue along the spending goal example for someone that wants to spend as much as they can on taking more trips with their family, for example. Let's imagine they have a constraint on their retirement age, which I think you should always have no matter what. A lot of clients will say like, there's no way I'm working past age 65 or age 70 or whatever that is. 

But there could also be clients that say, you know what, I love work, I'm going to keep working forever. And I think that's where it's time for the planner to come in, step in and say, look, great, if you can, great. But let's not assume that is the expected outcome because you might not be able to work for your entire life. 

And then it's up to the planner to put a realistic constraint on that. But now let's assume for a second that that's not only just a constraint, that the client would also like to retire early if possible, which I think is a pretty reasonable case. They want to take as many trips as they can, but they also want to, if they can retire earlier than age 65, then that's also awesome. 

So how would you handle this? Of course, these goals clearly have an inverse relationship. If you want to retire early, you're going to accumulate less wealth, you're going to have less to spend. 

But if your goal is to spend more, then retiring later is an obvious way to do that. What do you do? Now, the answer to this is to quantify the trade-offs using a Pareto frontier. 

And I don't want to lose people in the technical jargon here, because a Pareto frontier is actually pretty simple. It's just a chart. It's really just about plotting the one goal on the x-axis and the other goal on the y-axis, and then showing that range of outcomes for different scenarios. 

In this example, we have spending on the y-axis, which is one goal. They want to maximize the amount of monthly spending that they can have for trips or whatever the case may be. And then we also have the retirement age on the x-axis. 

And then we're able to show what the spending level, what the maximum spending level is for each retirement age. The key is that every point on this line is an optimal solution. And I think this is also another misunderstanding from people that really aren't familiar with optimization. 

When you think about what's optimal, we always think about one thing being optimal. But when you introduce multiple goals or multiple objectives, that inherently results in multiple optimal solutions. If you're calculating this for a client, and you see this line of the Pareto frontier, it's all optimal solutions. 

So you as the advisor or the planner, it doesn't really matter what the client chooses on this line. They're all great solutions. The answer really depends on what the client's preference is for one goal versus the other. 

For example, if someone has their main goal, their main goal is clearly to spend as much as possible to take those trips, then maybe they would be okay. They would see this data and say, I can spend the most when I retire at 65. Retiring early is not worth it for me. 

I'm going to work all the way till 65. That gives me the most amount of money to spend on my main goal. Alternatively, you could have someone else with the opposite approach. 

Maybe someone has the main goal of retiring early. The trips, the extra cash flow is nice to have, but they don't really care. And then seeing this data also helps them to be able to understand that, okay, this amount of spending, retiring at age 55 is perfectly reasonable for me. 

I'm able to satisfy my spending needs. I've got the roof over my head. I've got all the stuff that I need to do. 

And I'm able to retire early, which is what I really want to do. It gives me more time to spend with my grandchildren when they're young or whatever. That's totally cool. 

It's all about presenting the data, allowing the client to make an informed decision about what they want, what path they want to take moving forward. But there's one more point that I want to talk about on this frontier, and it's something called the knee point, which again, is a bit of a technical thing, but these knee points are kind of these spikes in the curve. It's when the rate of change of the curve increases. 

So if we're looking at this particular example, the curve is pretty smooth up until age 61, and then there's a big spike. For people that are listening and not seeing the chart on the screen here, spending is increasing at about an extra $1,000 per month every additional year that they work until age 61. And then it spikes to get an additional $3,000 of spending per month. 

And then it settles back down. If you see this as the advisor and are trying to help draw insights from this data, you can point out this retirement age of 62 and say, if you work an extra year from age 61 and retire at 62, you'll gain an extra $3,000 of spending. But then if you work an extra year beyond that, you'll only gain an extra $1,000 a month of spending. 

For the clients or for the person that really values both goals relatively equally, this point might jump out and say, yeah, you know what, that point makes a lot of sense to retire because I'm gaining that additional $3,000 a month spending, working until age 62, and then working a couple of additional years for only marginal increases in spending really isn't worth it to me. The knee point isn't the default best solution. It's really about presenting the trade-offs, quantifying the trade-offs for the client and helping them make an informed decision that really resonates with them.

Ben Felix: I got a couple of questions. Should financial planners be creating trade-off frontiers like this, or is it more of a mental model thought process?

Braden Warwick: They don't have to, but it's also a pretty quick and easy thing to do. I think it's super important regardless that they need to be able to present those plan alternatives. From what I've seen, I think, well, planners at PWL anyways are doing that. 

If the client wishes to retire early, they're able to create plan alternatives and say, okay, this is what it looks like at age 55. If you retire early, this is what your spending can be. If you're retiring at 60, this is what your spending could be. 

If you're retiring at 65, this is what your spending will be. They're doing that in general. This chart is a nice visual summary of that trade-off relationship. 

Again, it's a pretty easy thing to do. This is like a 10-row, two-column Excel table that I put into a chart. It's really nothing crazy. 

It's just about identifying what the goals are and then being able to communicate the data point that's actually relevant to the goal. That's the key. We'll see when I show the Conquest example as well that there's just so much on the screen at all times that it can be difficult to narrow in and focus in on what are the actual data points that are in alignment with my goals or with the client's goals that I need to focus on when comparing two different planning outcomes.

Ben Felix: My other question is, can we just use calculus to find the optimal solution?

Braden Warwick: Yeah, it's interesting because calculus would only work to find the optimal solution if there's no discontinuities in the curve. I think the reality of the tax code is that there's these discontinuities baked in because at certain ages, certain things apply or don't apply. CPP might turn on at age 70 and then that changes things completely. 

It's not like a gradual curve that we can use calculus to determine an optimal outcome. Typically, it's a bit of a technical way of saying that it's probably not that easy. That would be like a theoretical optimal. 

We can still find a computationally optimal solution using this type of approach, which in theory could be pretty close to the theoretically optimal if it did exist.

Ben Felix: Probably easier to communicate too. Just when I heard you say about the knee point, about the rate of change changing, I was like, sounds like a calculus application.

Braden Warwick: You can definitely use calculus to calculate the knee points and that's how they are actually done, but it's easy enough just to look at the chart and say like, okay, there's a spike here. I don't think that people need to worry too much about the calculus.

Ben Felix: Yeah, it's probably a stretch trying to communicate what calculus says about someone's financial plan is probably a little difficult.

Braden Warwick: Yes.

Ben Felix: Practically speaking, what does this actually look like when we do planning for clients?

Braden Warwick: Let's move on to a couple of case studies. I've got two case studies lined up. The first one I want to use Conquest for as more of a reflection on what a professional level financial plan would be for a bit more complicated of a scenario. 

Then the second one, I want to use our free retirement planning tool that's available on our website to use a more simplified case, to show how you can be thinking about solving for real goals using tools that are available to everybody.

Ben Felix: I do want to mention before you start that this first more complex example is specific to Canadians with corporations. A lot of our audience is not in Canada, but I think the thought process around the analysis and the optimization is still super relevant for anybody, even if their exact constraints and rules aren't the same. The thought process that you're going to talk through is applicable anywhere, just the details are very Canadian.

Braden Warwick: That's a great point. I wanted to model a business owner case, partially because I've done a lot of work on that particular case over the past five or so years at PWL. I'm not going to go into the details of compensation planning for business owners. 

You can always check out Moneyscope for more of that. Business owners come to us a lot trying to figure out how they should be paying themselves from their corporation. The two main options being, you could focus on dividends, which there's certain corporate tax advantages to paying dividends, or you could focus on paying a salary from the corporation, and this creates RRSP contribution room and it generates CPP contributions and increases the CPP benefit and so on. 

So there's kind of this dilemma of what should the focus be, and it's not obvious. For this case study, for this business owner, I'm going to simply assume that the client has one goal, and that's to maximize the amount of money that they're leaving to their children at death. So like I mentioned early on about this goal is that you can solve this pretty easily in Conquest using their estate planning or legacy goal. 

But if you're building a plan for the first time in Conquest, it's going to look something like this. For the viewers, you're able to see this. For the listeners, I'm going to try to communicate these numbers so that you can hopefully follow along. 

But you're going to see only one goal that shows up by default in Conquest and it's called the retirement goal. It looks like a percentage on the screen. And if you're new to financial planning or you're not thinking in depth about goals, you're not doing that goals reflection, this is going to be the first thing that you see. 

And if you're trying to answer the salary versus dividends question for the business owner client, it's really interesting. So the way I have this set up here is the base case of paying salary from the corporation. And if we look at this at first glance, we're seeing here a retirement goal that's greater than 150%. 

It looks great. The plan looks great from what we can tell. The percentage is over 100. 

Like how could it really be any better than that? But what's really interesting is when you set up the dividends case to compare it, which I did here, I created an alternative plan that got rid of the salary, and it changed the CPP benefit as well. And that actually decreases the retirement score. 

So again, for the listeners, it was 150% with salary, and now it's down to 135% with dividends. So you'd think if you're not really doing the goals exercise, you could potentially end this analysis right here and recommend taking salary because it gives you a higher retirement score. But if you've done the goals exercise appropriately, you've asked the client, and the client has said that they only care about maximizing their wealth. 

They're totally content with the amount that they're spending now. They don't want to spend any more money. They don't have any other cash flow related goals. 

They don't want to retire early. They only care about maximizing their estate value. You go in into Conquest and I'll show what happens when we add that. 

We can just click here and add a legacy goal. And we can add that pretty quickly. And now when you do that, now we have two little widgets here for two different goals.

We have the retirement goal, which is still showing up. And we have this legacy goal, which is also showing up. And for the legacy goal, it's now at $16.5 million for the salary case. But what happens when we flip over to the dividends case? And it's pretty crazy. Changing from salary to dividends increased the final net worth from $16.5 million up to $34.1 million. So a difference of almost $18 million down just to this one planning decision of whether you should pay yourself a salary or dividends. So again, coming back to the value of the financial plan, this is huge numbers. This is a big decision that this client would have to make.

Ben Felix: For the benefit of listeners, that's not universally true. You mentioned that you've done a lot of work on this. In this case, paying dividends makes more sense.

But in general, it's very nuanced. In some cases, paying salary will make things look better. In some cases, paying dividends. 

And in a lot of cases, it's some optimal combination of salary and dividends that usually changes over time that makes things look the best. So in this case, we're seeing that outcome but it's not a universal truth that dividends are superior.

Braden Warwick: Totally. And I think that ties in exactly with what I've been saying all along in this episode is that there's really no one size fits all for everybody. We need to be doing custom analysis, looking at custom strategies that actually tie into what the client's real goals are. 

So in this particular case, like you said, Ben, dividends look a lot better from a legacy standpoint. And that's because of how I set it up. But it's still true. 

This is a legitimately reasonable client scenario. But what's super interesting about this too, again, if you're not doing the proper goals exercise, and actually nailing down on how we should be evaluating the plan based on what goal the client actually has, we still have two competing things here. We have this dividend strategy that has a lower retirement score and a higher legacy amount. 

And vice versa for the salary case, it looks like it has a much higher retirement score, but then a lower legacy goal. What should you do if you're not doing this goals exercise? It's not very clear. 

And just to be clear, you cannot turn this off. You cannot turn the retirement score off at all in Conquest. It's there and you can't get rid of it. 

There's always going to be these kind of two competing things. But I think it's also important to dig a little bit deeper and understand why. How is it possible that the legacy score is higher for one case, but then has a lower retirement score? In order to answer that question, you need to understand how this percentage that's on the retirement goal is being calculated. 

So what this is, when you dig deeper, you go to the knowledge base of Conquest, or you talk to your subject matter expert at your firm, you realize that this retirement goal is representative of the funded status of the financial plan, meaning that it looks at all of the liabilities and retirement, and then it compares them to the amount of personal assets that are available to cover those liabilities. The key word there is that it looks at personal assets only, meaning that it's not looking at the money that's inside the corporation that could be used to fund that retirement. 

It's only looking at the personal assets. So when you pay a salary, you're increasing RRSP contribution room, you're effectively increasing the amount of money that you have personally. But in this case, that's at the cost of your overall wealth. 

But for the purposes of the retirement score, that makes it look really good because you have more money available personally. And then in the dividends case, it's the opposite, you're keeping more money in your corporation, and then those assets aren't in the personal accounts that are being used to calculate the score. This data point is pretty much not relevant in this case. 

And it can be potentially very misleading to people that don't understand how it's being calculated. And I really want to emphasize this case for two reasons. One is because I think it's important for the informed client to be able to question these types of things. 

If the advisor is saying that one strategy is better than the other, because this retirement score is higher, then you need to ask the advisor, what is this percentage actually? And why does it matter to me? And if they're not able to answer that question, then I think you have your answer.

You should be pretty skeptical. And then also for advisors too, because I think it's pretty easy. I bet if we look at the percentage of the Conquest users that actually know how the score is being calculated and what the limitations are, I bet it's a pretty small percentage. 

So I wanted to make that point to really cover both cases.

Ben Felix: Super interesting and complicated. These softwares are so powerful and they can do such complex calculations. Not that it's impossible because we've done it, you and I have done it. 

Not that it's impossible, but it's really hard to model something like this in Excel. You start to push the limits of what Excel can do, or at least can do in a way that's easy to use. So the softwares are incredible, but they're like a complex piece of machinery.

If I want to dig a hole, it's definitely easier to use an excavator than a shovel for me. But if I don't know how to drive an excavator, I might destroy my house.

Braden Warwick: Yeah, exactly. It's a great point. And you also mentioned that you and I have done this modeling in Excel and we've pushed the limits of Excel, which is true. 

But also, you and I don't speak with clients on a regular basis. So imagine the regular advisor trying to build that level of model, but then also trying to service 200 clients. It doesn't make sense as a proper use of their time. 

We have to rely on these tools, but it's really important to understand what's being calculated and how that relates to what the client actually wants to accomplish.

Ben Felix: Okay. So in that example, we saw that there was a financial planning decision that did matter. It mattered depending on which goal you're trying to optimize for. 

And you showed a limitation of the financial planning software because it is not looking at all assets in defining the attainment of one of those goals of the retirement goal. So we get from that, the importance of looking at different variables, but also the importance of understanding what's actually going on under the hood with the financial planning software. That's a pretty complex decision. 

It's common among our clients because we deal with a lot of people who have higher net worth, who are more likely to have corporations. What about a more straightforward financial planning decision like when to take Canada Pension Plan and old age security pensions?

Braden Warwick: That's a great question. Very relevant. So for this one, we'll use the free retirement planning tool just so that, again, it's something that people have access to that they can help use to drive this decision-making and to evaluate these trade-offs. 

And for this example, we'll use the other goal, meaning they want to maximize spending on trips, hobbies, it doesn't matter, but they want to maximize the amount that they can spend and draw down their portfolio, but also want to make sure that that plan is viable even for worse than expected outcomes. What I've done, I haven't really done anything yet for the people viewing this. You can see the retirement tool on the screen. 

And again, for the listeners, I'm going to try and talk through it. But the only thing I've done to this point is just entered in the birth date for someone that's age 40 right now, just so that, again, it's more realistic. I think the first thing we need to do is we need to figure out what the sustainable spending amount is for the base case. 

And this is the base case here. How do we think about this? This is exactly why I've added this outcome dropdown under the expected return section. 

And you have the options to choose from amazing, great, expected, bad or terrible outcomes. And what those actually mean, those are calculated using the standard error of the mean. And the reason why I'm using this as opposed to standard deviation is because planning outcomes are driven more by the standard error of the mean than they are the standard deviation of one year. 

And I think this is another point that I don't think is super well understood is how does a distribution of outcomes for one year of stock returns, how does that translate to a distribution of planning outcomes over the course of a 50-year time horizon? And this is where we need the standard deviation of the one year, but also the length of the time horizon is another relevant variable. You can use both of those variables together to calculate the standard error of the mean. 

And let me explain a little bit more. The distribution of stock returns, of annual stock returns, you have your expected mean of, say, 6% or 7%. And then you've got the standard deviation of like 15% or 20% or something like that.

Most of the listeners can probably wrap their head around that. They're familiar with that. But then what happens when you take 50 samples from that distribution for a 50-year time horizon? 

It's simply the law of large numbers that the more samples you take from a distribution, that the average of those samples is going to converge towards the expected outcome. What that means in practice is that that standard deviation is effectively going to decrease the more samples we take from that. So if you're taking 50 samples, then that distribution is going to shrink more than what it would for someone that only takes 10 samples, for example. 

I think a lot of people think about mean reversion, for example. That same phenomenon of a decreasing distribution over a longer time horizon can also just be attributed to the law of large numbers. A little bit of a nerdy detour there, but that's how we're calculating these different outcomes. 

It's based on the standard deviation, but then also the time horizon. If you're trying to solve for sustainable spending, we can look at the bad outcome, for example.

Ben Felix: Can I explain this to people in a way that's less nerdy?

Braden Warwick: Sure.

Ben Felix: Correct me if I'm wrong here, if I'm remembering the wrong thing. When you're figuring this out, you did a study to show that this approximation that you've created corresponds to running Monte Carlo simulations, right?

Braden Warwick: Yeah, let me explain a little bit more. In theory, if you neglect cash flows, which is important, if you neglect cash flows, and you just look at the distribution of returns, and how that changes the expected return, what I was saying there is that is the theoretical model for how the distribution should change. I was able to do that and run a Monte Carlo just looking at the sampling of returns, and I was able to show that that is true empirically as well. 

The missing piece is that cash flows and the timing of cash flows do also matter in terms of planning outcomes. It's not as good as actually running a full Monte Carlo analysis with the actual financial planning projection being calculated a thousand different times, but it's a pretty close approximation because the main driver is being captured, and it's a free tool, and it's a lot less computational overhead.

Ben Felix: Yeah, that's the thing. You created this methodology where we can map out a bad outcome that corresponds to what we would consider a bad outcome when we run Monte Carlo in Conquest for our client. Conquest doesn't use Monte Carlo exactly, but when we run a volatility analysis or whatever, people are used to seeing, okay, this plan fails 50% of the time or 60% of the time, whatever, that's a bad outcome. 

You were able to do an approximation of what a bad Monte Carlo would look like, which is going to change depending on the time horizon using this methodology that you described. The benefit of that methodology is that we can map out the bad outcome and the good outcome and the terrible outcome without actually running a Monte Carlo, but getting a very, very similar result. That's great because this tool that we're referring to right now is available for free on the PWL Capital website.

Braden Warwick: Research-tools.pwlcapital.com. We'll bring it to the homepage, and then you can get to the specific tools from there.

Ben Felix: Anybody can use these tools. If we were giving the ability for anybody to run a Monte Carlo, that would get expensive for us pretty quickly because it is more computationally intensive. The main takeaway for people listening is that this retirement planning tool that's on the PWL website has basically an approximation of Monte Carlo simulation using the nerdy mathematics that you just described.

Braden Warwick: That's exactly it, to take the nerdiness one step further. For this bad outcome here, just based on stats 101, you can calculate what the viability of that outcome is. Based on the fact that this is one standard deviation below the mean, that corresponds to roughly 84% of plans being viable. 

If we drew down the portfolio perfectly to zero in this outcome, that means 84% of those plans would still have money left at the end of the day. If we wanted to look at the terrible outcome, it's two standard deviations below the mean, so that corresponds to, if we drew this down perfectly to zero, it would be about a 97.5% success rate. That's quite high. 

That's probably higher than we would plan for most of our clients. For this example, let's assume that the person is comfortable with planning for the bad outcome, which has an 84% viability of the plan if we plan for it to draw down to zero. Let's start here. 

What we can do to solve for the sustainable spending under this bad outcome is that we can just increase spending so that the portfolio goes to basically zero at the end of the time horizon. I've cheated a bit and I already knew what this answer is going to be, but it's roughly $53,600 of spending per year, which is about $4,467 a month of spending. It basically draws down the portfolio to pretty much nothing at the end of the time horizon. 

That's our base case. If we actually want to see how the strategies impact our goal of increasing the spending amount, we can look at changing our assumptions. Let's start with OAS because the default in the tool is to take it at 65.

But now if we're bumping that up to 70, we can see that with the same spending amount, we have a higher net worth, so that means we can probably increase spending a bit further. Again, I'm going to cheat because I already know what the answer is. It ends up being about $53,800 per year, which is $200 a year of spending, but that's also $200 a year over 50 years for this time horizon.

For one planning decision, it's still a moderate impact. But now let's look at what happens when we change the CPP assumption. By default, the tool is going to optimize this for you based on the results of the CPP tool for your specific case, but we can change that to a custom defined benefit.

Ben Felix: For the benefit of listeners, that's on that research tools website. There is this retirement planning calculator that Braden's talking about primarily, but then we also have separately a CPP, the Canada Pension Plan calculator, that calculates how much you can expect from CPP. This retirement tool is drawing from that CPP tool. 

It's kind of like automatically inputting the information into the CPP tool when you use the retirement tool and it'll default to the optimal timing of taking CPP, but now Braden's showing what happens if you change that figure.

Braden Warwick: You summed it up pretty well, Ben. It's worth pointing out since we're talking about understanding how things are being calculated in the software that the CPP tool determines the optimal CPP age by the present value of CPP and which age has the higher present value of CPP when you look at lifetime contributions and lifetime benefits. It's not necessarily optimized for the goals like we've been talking about in this exercise and that's maybe why you want to enter in a custom value here and see what actually happens to your goals when you change the age.

We'll do that now. It was at 70. Let's dial this back to 60 and we'll recalculate it and we see that it's a pretty dramatic change. 

The person was essentially drawing down their portfolio at end of life, but now we're drawing it down basically 10 years earlier because we've taken CPP earlier. As a result, we'd have to dial spending way back in order to prolong our assets. We can pretty much rule this out as being optimal just by looking at how quickly it runs out of money. 

But I think another thing that I wanted to touch on too that is really interesting and goes with the theme of being able to quantify the trade-off relationships is that we've been able to show that in this case, deferring CPP and OAS are optimal for this person's goals of spending the most amount of money, but we can also get a little bit more insights into how things would go wrong or what things would look like if they go wrong. Let's just dial spending up a little bit more so that they run out of money a little bit earlier. 

If we look at cash flows, in this case, I increased spending so that person runs out of money about halfway through retirement. We see that again, we're deferring CPP and OAS until age 70 and we're spending $54,500 per year in retirement. That's the goal. 

But then when we run out of assets, our spending only drops to $44,889. So it drops by roughly $10,000 a year. And again, if we set up this problem, understanding we have our spending wants and we have our spending needs, it's totally possible that spending needs could be covered by CPP and OAS. 

And also remembering that this projection is for one person. If you have a spouse that has the same outcome, it would be double. That could potentially be enough to cover that person's spending needs, even if they run out of money in their portfolio, because they've been able to defer their CPP and OAS the longest. 

Essentially, the reason why that's powerful is because you're effectively purchasing an annuity. You're guaranteeing that a higher threshold of spending is covered by deferring CPP and OAS. And then you're able to take a little bit more risk potentially with your spending if you're comfortable with that. 

A key theme from this whole episode is understanding those ranges of outcomes, being able to think through what you actually want to accomplish and what you're comfortable with, and then making a data-driven decision based on the insights that you're getting from these projections.

Ben Felix: Very cool. Can you talk a little bit more about on the theme of having the right tools to quantify these decisions, what makes the CPP tool that we have up on the PWL site different from most of the CPP calculators that exist out there in the marketplace?

Braden Warwick: One key difference that our tool, and actually it's the origin of the CPP tool, Ben, when we talked about this, is that we think a lot of people are thinking through the CPP decision in the wrong way, that they're looking at these break-even ages. If I live past age X, then deferring makes sense. But if I don't make it to that age, then I should have taken it early. 

And I think we've seen the data on this that that leads people to end up taking their CPP earlier to hedge against that. That's intentionally not how we've set up our tool. We've set it up so that it compares the present value or the lifetime loss, which is essentially the two same metrics, just the inverse of each other. 

What is the present value of your CPP cash flows at each age that you take it? Or in terms of the lifetime loss, how much are you losing by taking CPP early? The way we've set this up is that we're using the life expectancy from the FP Canada table as the default. 

And of course, you can change that. You could still, in theory, do that similar analysis of changing the life expectancy to see what happens. But this is our starting point is that expected outcome.

And then we are calculating what is the maximum amount of present value you can get from CPP at that time. That's at the highest level. What our tool does differently is it thinks through that decision completely differently. 

But then there's a whole ton of detail as well that our tool does that I think it's pretty easy to gloss over. And even honestly, when I started building the tool, I didn't fully appreciate how much detail goes into those types of calculations when we're thinking about disability dropouts or post-retirement benefits and all this other stuff. It can get pretty detailed. 

So we wanted to make sure that we included all of that so that people can make the correct decision.

Ben Felix: And the way it's indexed too. I think that's one of the big ones that sets the way that we've modeled it apart from how most people tend to think about it.

Braden Warwick: Yes, big time. So there's two assumptions for the CPP tool. There's the wage inflation assumption and expected inflation. 

And those two are different. And they're intentionally different. By default, our tool assumes that the expected wage inflation is a half percentage point above the CPI inflation. 

And I think Ben, correct me if I'm wrong, but the historical data on that is closer to 1% delta for expected wage inflation. But we're making a bit more of a conservative assumption here.

Ben Felix: It depends when you look at it. Over the full history that we have data available, I think it's been around 1%. In more recent history, it's been lower.

Any positive delta where wage inflation is higher than CPI inflation will make deferring look better. So if we assume it's 2%, then people would always want to defer. If it's 1%, it looks even better. 

But we're using 0.5% to try not to be too aggressive with that assumption. But I think assuming zero, assuming that they grow at the same rate, that wages and CPI grow at the same rate, I think that's also a mistake. And it would tend to bias people towards taking CPP earlier, all else equal.

Braden Warwick: That's right. When there's real wage inflation, there ends up being two drivers of the advantage to deferring. You have the one that most people understand, which is you get that additional percentage to your benefit each year you defer up until age 70 for CPP or age 72 for QPP.

And I think most people understand that. But there's also an additional benefit to deferring. The wage inflation is expected to be higher than CPI inflation. 

So even just deferring in and of itself without all the excess benefit to deferral, the projected benefit will still grow in real terms over time.

Ben Felix: The amount that you get when you start CPP is indexed to wages. Once you take CPP, your benefit is indexed to CPI going forward. So every year that you defer, as long as wages are growing faster than CPI, you're bumping up your starting benefit by that delta in real terms. 

And like you said, Braden, there's statutory increases. You're going to get an increase for deferring in the age ranges that you mentioned. But then there's also this, I don't know what you call it. 

It's not statutory, but it's just implied by the way that the benefits are calculated, additional benefit from deferring as long as wages are growing faster than CPI. There have been cases where that has not been the case and that changes the timing decision a little bit. But in general, I think from a modeling perspective, that's something that we built into this tool that most other CPP estimation calculators just aren't considering.

Braden Warwick: And there's a ton more detail too, just based on the five-year average of YMPE and how that's being calculated and how there's even some nuances. So if you simplify that, like some other tools are doing, that can decrease what the projected benefits are. I think we're trying to do everything as detailed and correct as possible with this tool.

Ben Felix: What's our summary to wrap this up here? Approaching financial planning from an engineer's perspective. What are your closing thoughts?

Braden Warwick: Closing thoughts, I think the themes of this episode, one, make sure that you understand the client's goals, their real goals, not their surface level goals, and then make sure that you're evaluating the plan according to those goals. And oftentimes that might not involve using the happy path of the software, so to speak. Even in the tool that I've created, you'll notice that we were looking at the spending amount, which is an assumption. 

And that was never like pop-in-your face KPI that makes it obvious that that is what you should be looking at. But it is what you should be looking at if that's what you want to accomplish with your financial plan and what you want your financial outcomes to be. Beyond that, it's super important. 

Sensitivity analysis allows you to examine which variables drive the best planning outcomes and are the ones that make the biggest difference to client outcomes so that you can prioritize those with your clients. I think that's super important. And it's also super important to examine the trade-offs and to quantify the trade-offs.

And real world scenarios oftentimes have multiple competing rules. And the software doesn't natively handle that very well. But that provides more opportunity for you as a financial planner. 

Or if you're a client of financial planning, you should be making sure that your financial planner is capturing all of that. It provides more opportunity to add value and more opportunity to really quantify those trade-offs. It makes presenting the data more important and not less important. 

When there's things that fall out of scope, out of the software, you should be doing more work, more rigorous analysis, and not less. You shouldn't be trying to wipe your hands of it. You should be digging even deeper to be able to quantify those trade-offs for your client because it is important.

Ben Felix: And all the same applies to someone who's doing this themselves and thinking about this stuff themselves. They are the financial planner and the client, I guess, in that scenario. I've got nothing else. 

I think that was a really interesting discussion. It's cool to see the way that you think through this stuff and the tools that you've created that anybody can use to help think through this stuff. That whole concept of multi-objective optimization is super interesting to think about on its own. 

Then you combine that with the requirement to have a model that is able to capture the objectives that you're trying to optimize for, which is not always the case, not always easy to find. That makes the whole thing that much more complicated but also interesting. There's a whole other conversation around there. 

We had an episode with Ben Mathew last year, I think, where he's built the TPAW planner, which is approaching financial planning from a whole different perspective. That's another thing. It's like, what model are you using to build the financial plan and decide how much you should be spending?

Conquest is doing it one way. Ben Mathew's model is doing it a whole different way. There's a whole lot of – I don't know what you'd call that – model risk or just model uncertainty in financial planning. 

It's an interesting field because it is highly consequential to people's lives. We know a lot about finance. We know a lot about psychology. 

We know a lot about financial planning. But, the science, the engineering approach, as we're calling it, to solving these problems, I think is pretty new. It's not something that's well-developed and everybody agrees in the systematic process, the systematic way to do this. 

It's overall, all things considered, a pretty new field and a pretty new discipline that is still being figured out in real time. You're contributing to that, which is cool.

Braden Warwick: Thanks. Super interesting. Like I said at the beginning, I love to share my thoughts, be able to have the opportunity to share what I've learned from super smart people in other fields and help apply it to bring this field up another level.

Ben Felix: Very cool. All right. Well, I hope the listeners enjoyed the episode. 

Braden is active in the Rational Minder community. If anybody wants to talk to him about the stuff he talked about in this episode, he will answer you. All right. 

Thanks everyone for listening and thanks Braden for coming on.

Braden Warwick: Thank you.

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

Be sure to add the episode number for reference