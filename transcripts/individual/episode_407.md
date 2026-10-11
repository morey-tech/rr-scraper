## Episode 407

Ben Felix: This is the Rational Reminder Podcast, a weekly reality check on sensible investing and financial decision-making from two Canadians. We're hosted by me, Benjamin Felix, Chief Investment Officer, and Braden Warwick, Financial Planning Product Architect at PWL Capital. Welcome to episode 407.

Braden, I had to bring you on for this episode because, I mean, the listeners will figure it out pretty quickly. It was your kind of topic. I don't know, what are your quick thoughts?

Braden Warwick: Yeah, it was pretty cool. Last time I was on the podcast, I think I left some of the Rational Reminder community members wanting more nerdiness, wanting to go into more detail into my thought process and how I think about solving problems. And then, Ben, you showed me Michael's paper. 

I was pretty blown away by how he was able to create a mathematical model that really got all of those ideas into one model. And it's an impressively comprehensive model. It was just really cool to talk to him about how he approached building a model, and he had a lot of cool insights.

Ben Felix: It's a really cool model. I was talking to Ross, compliance Ross, a minute ago after we finished our conversation, before we started recording the introduction, about the level of precision in the paper, because it's this mathematical model where it's like, you could argue that it's too complex and trying to be too precise. But I think that the takeaway from the paper and from the research, and I think Mike would agree, is sort of a level of abstraction above that, where it's just like, forgetting about how precise the outputs are, he's able to quantify the importance of integrating all of the, in the way that he sets it up in this model, the six financial planning areas together, because the advice that you might give in one area will affect another financial planning area. And if you're not paying attention to those interactions, you can end up giving suboptimal advice, which he's able to quantify because he has the model.

But the fact that the model can quantify it precisely, I don't think is really the takeaway. I think just the general concept of the importance of integration, of integrating financial planning advice across all of the financial planning areas and integrating the preferences that the specific client has, that was really the takeaway. The work that he did is building this really impressive mathematical representation of the whole financial planning process. 

It's like a mathematical model of what a financial planner should be thinking about when they're giving advice to a client. And that's pretty cool. So I mean, in a lot of the episode, we talk about the model and about how he built it and how it works. 

We're basically just talking about financial planning, the way that he has represented it in his mathematical model. So hopefully it's not too much math nerdiness and there's enough sort of, this is why these modeling decisions are relevant to making financial planning decisions. I think we struck a reasonable balance, but that's really what the whole thing is about. 

It's thinking about financial planning decisions. He's done a lot of work to quantify that. Any other thoughts? 

I'll talk a little bit about who Michael is, but do you have any other thoughts before I do that?

Braden Warwick: I think in general, it's really cool. Like you said, Ben, to emphasize the importance of analyzing all six of those areas cohesively and that there's trade-offs between the two. I think Michael provides some examples in the episode, but being able to understand those trade-offs is a critical role of the planner, but then also understanding the client, understanding the client's objectives. 

And Michael's model, those two concepts are extremely important in coming up with the optimal solution.

Ben Felix: I agree. The guest that we talk about all this stuff with is Michael Kothakota. He's got his PhD in personal financial planning. 

He's also a CFP and his work really bridges academic research with financial planning practice. He's also a lecturer at Columbia University's wealth management program. He was previously the head of research at the CFP board in the US.

That's like the issuing body for the CFP in the US where he actually built the research department. He also oversaw the financial planning review and developed the financial planning index. His PhD is from Kansas State University, which is the top or one of the top financial planning PhD programs in the world. 

There's not a whole ton of those programs, but K-State is up there with the best of them. He also has a master's in predictive analytics from Northwestern University, which is pretty cool. Very qualified, nerdy guy. 

He's published a ton of papers in financial planning journals. He is the CEO of WolfBridge Wealth, which is a Durham, North Carolina-based financial planning firm that he founded in 2008. Sounds like he keeps a pretty small number of clients. 

He mentions that during our conversation, but it's still pretty cool. Yeah. So I think that's a pretty good overview of Michael and warning to listeners. 

It's very nerdy episode, but I think there are a lot of good financial planning takeaways that stem from the nerdy discussion about the model. Any other thoughts?

Braden Warwick: No. Let's get to the episode.

Ben Felix: Cool. Let's go to our conversation with Michael Kothakota. Michael Kothakota, welcome to the Rational Reminder Podcast.

Michael Kothakota: Thank you. I'm happy to be here.

Ben Felix: Very excited to be talking to you. We like to joke with our audience that they like nerdy episodes, and I'm pretty sure this is going to be a very nerdy episode.

Michael Kothakota: I actually went down the rabbit hole of listening to some of your past podcasts and I was like, oh yeah, this is really cool. I think I just listened to the James Choi one, which actually, I think Dr. Choi and I agree quite a bit on a number of things. So quite interesting.

Ben Felix: Yeah, that was another good nerdy episode. Let's start off here.

In plain language, what is interdependent integrative financial planning theory?

Michael Kothakota: In plain language it's a mouthful of words, but the purpose is to describe... It's both descriptive of what I think good financial planning should look like, and then prescriptive for the reasons of if you do these things, it's part of adding value. So recognizing that each of these domains are integrated and that there are interdependencies both across domains and then across time. 

And so that is essentially what it is. It's trying to capture the interdependencies between and the tensions between different planning activities and people managing their day-to-day financial lives. That's essentially what it is. 

It's also designed to capture the value that is provided using that process, using a full integrative approach. It's interesting. When I first started thinking about this, I started thinking of your financial life as a sphere. 

And depending on what you do, it changes the shape... Very topological. It changes the shape of that sphere. 

And obviously, that evolved. But I just remember thinking like, if I do this over here, it affects this. And then especially as you get into some of these more complex problems that you're trying to solve for clients, if you optimize for tax this year, you might affect something that is not exactly in line with what the client wants or not exactly even optimal, given the structure. 

It wasn't intended to be like this big mathematical structure, but essentially, it's just a mathematical structure to describe how financial planning can be more optimal.

Braden Warwick: So where did the well-known theories of lifestyle, portfolio choice, and consumption fall short in describing what financial planners do?

Michael Kothakota: I really like this question. First of all, everything builds on everything. This is certainly not to say that other people haven't had great ideas. 

I think one of the issues with something like economic theory is that a lot of times, it's great for policy. How can we provide the most value for the most good or provide the best advice to the most people? That's great.

If we can have a very parsimonious model, then we can really do some good things for humanity. Financial planning is very individualized. And people have a lot of idiosyncratic perspectives. 

They have idiosyncratic fact patterns. And then just different things happen to different people across time. A lot of those models in a couple of ways, Markowitz and Merton, portfolio optimization, brilliant. 

It's very difficult to top something like that. Consumption smoothing, life cycle. I think people have heterogeneous objectives that are vastly multidimensional that are affected by family, they're affected by different decisions that they make, different decisions that are made for them. 

Politicians or random events that occur. It's related so much more to consumption smoothing. A lot of times people don't want a smooth consumption. 

Consumption smoothing is a great theory and it describes very broadly how people can behave to optimize their financial life. But I feel like there's a lot of value loss. So there's a lot of deadweight loss in that process of doing that. 

It just doesn't capture that full scope of what we do as financial planners and working with clients. I used to think, oh yeah, I could apply all of this stuff to everything I do. And I think what's interesting is that's where you see a disconnect a lot of times where financial planners are like, I've been to research conferences, I've been to practitioner conferences, a financial planner will come in and say, okay, great. 

This research is great. Okay, how does it help me with my client? And the answer is usually like, well, I mean, the honest answer is it's a starting point. 

It's, hey, this is a starting point to kind of talk to your clients, but your clients are going to have these specific issues. And so I feel like we needed something that was more appropriate for what financial planning actually is.

Ben Felix: Can you describe what you think the central insight of the theory is?

Michael Kothakota: There's several different elements to financial planning. There's the overall structure. If you're familiar with wave functions in quantum physics, where there's several different states that exist all at once. 

And then when decisions are made, the wave function collapses and then now you've got a new set of probabilities that you look at. There's the structure. So this is more of the physics, so to speak, of financial planning, where each domain interacts. 

There's investment theory, there's tax law, there's state law. There's actuarial calculations. So there are these objective pieces that we can point to to say, okay, well, these are how these things are going to interact both in the present and then over time. 

And so that's one piece of it. And I think where a lot of some of the other theories will include things like your indifference curves within the model. And I think that the problem with doing that is that I think you're going to have different preferences for different things. 

Because again, this is like a very multi-dimensional thing. And if you're just thinking of a single utility function, it's just not going to work. What people prioritize or their values can be applied to that structure for weighting purposes. 

So some people have no desire to leave an estate, but estate taxes may still affect them. And then there are people who say that they want to retire or they're going to work forever. So I don't know about you, but I know a ton of financial planners who are like, I'm just going to keep working. 

Why would I stop working? I can have 10 clients and have five hours a week and then just do that for the rest of my life. I was one of those people. 

But as I've gotten older, I'm like, hey, maybe retirement doesn't look so bad. The next piece would be how exigent is that actual domain? How much does it matter at this moment in time? 

So that does change over time. That's the temporal piece. And then all of those things connect together in the value function to say, okay, well, this is what is going to work best for this client at this time. 

That's what I think is the central insight. And I think the corollary to that is, well, if this is this point in time, then monitoring the plan and engaging with clients throughout their life is vital. Because all of those things are important and things will change and things will happen. 

There are a lot of people who do one-time financial plans. What this insight is, is basically, well, a one-time financial plan is not going to be effective to providing that value.

Ben Felix: You've basically taken mathematics, applied it to building a mathematical model of financial planning, broadly speaking, which itself is crazy. And then there's a preferential weighting to each of those categories based on what somebody cares about. And then there's a time dimension to how those things are going to change over time. 

And you've taken all of that, put it into a model. And then as you do in your paper, you kind of play with the model and test stuff out.

Michael Kothakota: And some people would say, and I think a lot of people have said, overly complex. The easy criticism is this is overly complex. And I don't know how long I've been, how long have you been a planner?

Ben Felix: 14 years.

Michael Kothakota: In your career, you've seen a lot where it's just complex.

Ben Felix: Yeah. Oh, it is.

Michael Kothakota: And we run into a lot of the ideas from economics where it's like, well, if you just do these things, you're going to be fine. Why don't you do these things, put all your money in S&P 500 fund. 

I mean, that's what we say in the US anyway. Spend less than you make. All of which is very good, sound advice. 

And I think Dr. Choi, he was on Freakonomics talking about this too. And I think he talked about it on your podcast as well, where he's like, individuals have different things going on in their lives that make them prioritize things differently. I think what I was trying to do was lean into the complexity as opposed to trying to lean away from it. 

I actually started trying to make it simple at first. But I was like, you know what? Parsimony doesn't work here. 

Because there are so many different pieces to this. So can we lean into the complexity? Braden may be able to confirm this, but complex engineering projects, sometimes they just need to be complex. 

Maybe you want to make it as simple as possible. But sometimes they just... In order for something to work, you've got to add a bunch of stuff to it. 

I don't know if you read that book, Subtract. That guy, I think he's an engineer. But it's basically like how to make things simpler. 

So I did actually try to do that. And I basically just confused myself.

Ben Felix: The reality is that it is just a really, really complex topic, especially when you start getting into people's individual preferences and what they want, what that specific person wants to optimize for. And you've taken that complexity and you've quantified it, which I think is the really interesting thing about what you've done here.

Michael Kothakota: That was the goal.

Braden Warwick: So what does the theory suggest about the heterogeneity of optimal financial advice, even for people with identical financial situations?

Michael Kothakota: If people both have the exact same structure, there's a sample in the paper that deals with that. The first thing is the connection between the domains only actually matters if a client assigns a positive weight to that domain. So I'll go back to the estate planning example. 

I work with a lot of divorced people. Interestingly enough, both people usually say, oh, well, my ex-spouse is going to leave everything to the kids so I don't have to. They've never really talked about it. 

So the kids aren't getting anything from a lot of these cases, but they don't prioritize their estate at all. And then conversely, I have some people who are like they would rather starve is probably a little extreme. But hey, inflation is hurting the budget. 

They're going to just be a little bit more frugal because they want to maximize an estate that they probably would never be able to spend down if they tried. So those priorities, I think, matter. Especially if you've got a structure that's the exact same, the optimal outcome is going to be different for different clients. 

That's what I think is the key part. Obviously, people don't have the exact same situation. It's extremely rare. 

I use examples of twins because I was trying to make everything as exact as possible. The only thing I didn't do was name them the same. It actually comes from... 

I have a couple of brothers who they weren't twins, but they had very similar jobs. They had very similar... They inherited the same amount of wealth from their parents, but just very different objectives about how they had the same number of kids, different objectives about how they wanted to live their lives, which is really fascinating. 

And then further from that, some things happened to that brother that didn't happen to the other brother that caused some changes. That's why I think it's so important that the one size fits all or just general advice is not really going to work. Even if you could precisely identify the structural interdependencies and you can say, okay, this is the most optimal for that structure. 

As soon as you get into what people want to do, you've now got a different problem that you've got to address. And so that's why it's separate. Because you can identify what the structure is and then you separate the values. 

So then it gets filtered through that in order to come up with the optimal outcome for that client.

Ben Felix: So you've got the structure, which is like the whatever, account types and entities that exist and assets and all that kind of stuff. And then you overlay on top of that, there's an individual component that... And that even if the structure is identical, you can have two very different people.

To your point, even something as... I don't want to call it subjective as one person's life experiences over the other's that can materially change the optimal financial advice in that case.

Michael Kothakota: It is subjective. To continue the physics analogy, if we've identified how much things weigh and how much mass they have, but then gravity is subjective, which is essentially what we've got here. If gravity is subjective, well, then everything changes. If gravity is different between estate planning and tax for this client than it is for the other, then it is a subjective thing. We don't have a universal objective thing to solve.

Ben Felix: I like that. Gravity is subjective in financial planning.

Michael Kothakota: Like I said, borrow from everything I possibly can.

Ben Felix: Yeah, I like that. We kind of talked about in general what the theory is trying to do. I want to get a little bit more into the details of how you set it up.

Can you talk about how multi-objective optimization is related to financial planning?

Michael Kothakota: In most cases, in financial planning, most people come in with multiple objectives. A lot of times people present with like, hey, can I retire? And that's great. 

Financial planners should address that. They should definitely say, Okay, yeah, we want to make sure that but then we want to talk about these other things because the things that we do now for retirement planning matter for other things. If you've got a business, it matters for, how are you going to transition that business?

How are you going to deal with key people? How are you going to fund that if something happens to...there are insurance questions. There are estate questions. 

I don't know what it's like in Canada. Here, estate for most people is pretty simple. If you're below 26 million, I mean, you can do a lot of different things. 

But in the UK, for example, I think they just raised it to a million. I think it was like 400,000 pounds or something like that before. And they have a seven-year lookback period. 

So it's incredibly important there. I assume it's probably incredibly important in Canada. I'm not 100% sure. 

But when we think about all of these different objectives, it has to be a multi-objective problem. They compete with each other. Some of these objectives work together.

If you're trying to increase your risk-adjusted return on investment, that should help some of these other things. But at the margins, they compete with each other. So improving tax efficiency, that could reduce retirement security depending on how your objective function is set up. 

If you maximize estate planning, remove a bunch of stuff from the estate, well, that can impact your cash flow. It could impact how you educate your children. There are a number of things that can happen there. 

And then the way that the theory works is that it uses that priority matrix to aggregate those multiple objectives into this single priority-weighted reward. This is the value for this particular set of facts. Each domain gets that weight. 

Basically, how much the client or household cares, which, by the way, purposely did not include talking about couples where there might be tensions, because it really got hairy trying to think through that problem. But basically, it then can blend into that single objective optimization problem by pulling from these multiple dimensions. And so that's very similar to Keeney and Raiffa. 

So they did a lot of multi-attribute decision theory. So a lot of decision scientists... I suspect that that's who my paper went to is decision scientists. 

So I'm sure they're going to have a lot of good feedback. They've been working with some of this stuff for years because a lot of decision making is multi-objective.

Ben Felix: Ralph Keeney. We actually had Ralph on this podcast a while ago.

Michael Kothakota: Great. I'm glad he wasn't here so he could just tell me how I'm wrong.

Ben Felix: That was episode 238, Ralph Keeney. That was a cool one.

Michael Kothakota: Very cool.

Braden Warwick: Your paper does a lot of great work. It introduces a lot of detailed mathematics to this world of financial planning. You also included dynamic programming.

I'd like to understand how does dynamic programming contribute to the understanding of financial decisions?

Michael Kothakota: When I first posted the article, I thanked a bunch of people. This thought process came from Michael O'Leary. So I'd had a number of conversations with him when I was head of research at CFP Board. 

I started talking to him about my thought process on the interdependencies. And then he was like, hey, well, I've been working with the Bellman equation to affect this. His background is nuclear engineering, very similar to mechanical engineering framework. 

He and I talked deeply about that. And so I ended up spending a lot of time with him. And so Richard Bellman, I don't know if he's the founder of dynamic programming, but it's basically trying to break these complex sequential tasks into a simpler sub-problem.

In my paper, the extension or the HJB equation or the Hamilton-Jacobi-Bellman equation is designed to characterize optimal behavior. When we talk about how this can possibly work at scale, we'll get into why that is so challenging. Because having the formula is one thing, deriving it for an actual household is extremely complex and very difficult to do.

The big thing dealing with dynamic programming is that in this particular case, we have these value functions that are non-smooth. There are discontinuities in different parts of the plan. Some planning strategies don't exist until you reach a certain age. 

Sometimes they're gone after a certain age. Sometimes they don't exist in certain countries, for example, or if you're an expat. So there are a number of things that create these kinks. 

Sometimes people write in their papers, they call it kinky. So there are kinks at these transition points. Basically, the idea is that the value function is basically to say, okay, if we track all of these things, and we optimize for this particular case with these peoples' particular values, then that's better than not integrating. 

That's better than somebody coming along and saying, hey, I'm going to build a retirement plan for you. And then you go to your tax advisor and they file your taxes and they do your tax planning. It's better than that siloed approach because we're considering all of those different things in order to make it optimal.

Ben Felix: This theory kind of explains why integrative financial planning is valuable, which is interesting. You're able to sort of quantify why that advice is valuable. I have a question. 

Empirically, is there evidence that the financial planning profession actually offers measurable benefits to households?

Michael Kothakota: Sort of. I think the challenge is in the datasets. So Sherman Hanna had an article a number of years ago. 

I talked about it in the paper. But basically, we use a lot of these in graduate school. In social sciences, we use a lot of these large datasets. 

Other than probably in the last few years, none of them are designed for actual financial planning. They're household finance. They're generally designed for decision making. 

They're designed for economists to make decisions about and observe changes in household dynamics, and then make some policy recommendations. And so that paper, it will identify, okay, these people have a financial planner. Are they better off? 

And it'll make some comparisons and make some assumptions. And so you'll see a lift based on that. So the idea is that if people who are advised are going to have better financial outcomes than people who don't. 

And then more recently, so the project that I started at CFP board was the longitudinal study. So basically, the idea was, okay, well, let's look at financial planning outcomes. Let's do this longitudinally. 

The questions are designed to be more financial planning-specific and to deal with financial well-being. So it pulls in the objective pieces and then also pulls in some of those more mental well-being, psychological well-being pieces so that it is a little bit easier to identify. And so that's what Dr. Heckman, Dr. Lutter, Dr. Koochel, and what's Michael's last name? A guy from Wisconsin. I'm blanking on his name right now, but he's brilliant as well. So they've been working on this project. 

I think they're in their third year of data collection. They have been able to see both in the first year, a lift in people who are advised versus not advised across almost every dimension. So there is some empirical evidence there. 

I think where you run into things is like, well, what's the quality of that? What are they actually doing? So okay, great.

We know that they're doing it. But what are they actually doing to provide this service? Maybe they're just like there and the stuff I'm talking about doesn't matter. 

Or maybe they're saying, okay, look, I'm really going to take a look at how everything is going to affect you. But because we don't know that, and it's really difficult to get at, we need a different set of research designs to actually get at that information. Which something like that large scale is not designed to do, and nor would it do. 

And then I think Swarn Chatterjee had pretty similar results. But again, it was one of these big datasets that is less useful.

Ben Felix: There's always that selection bias issue too in the large studies like that, because financial planners are going to be more likely to seek out clients that have better financial situations because they're more profitable to serve.

Michael Kothakota: Are they coachable or do they have less mental health barriers? Absolutely. And I think it's interesting. 

So when we drafted the initial FPLS survey, Dr. Heckman spent probably, I want to say months on like trying to figure out selection problem. And so it's about as good as it can be. Dr. Heckman was actually my dissertation advisor. It's about as good as it can be from a selection perspective, but you're absolutely right. You're just never going to get all that eliminated.

Braden Warwick: How would you describe the integrated financial planning architecture that underlies your theory?

Michael Kothakota: The first piece is that structure, which is the structural tensor. So tensors can be an abstract principle, but basically kind of think about it as like a multi-dimensional object. Financial planning has got a lot of dimensions to it. 

So it's just a way of capturing that. We know that there are all of these dimensions. Part of the financial planning problem is to how can we reduce that dimensionality to make it solvable?

Because if it's too complex, nobody can solve it. Those structures exist regardless of what clients do or feel. Obviously, they can enhance their financial position using that structure. 

But in general, it's things like tax law and stuff. And then there's the priority piece. And so that's how do people prioritize so that all those weights sum to one. 

One of the things that's interesting about this that I've been playing around with is I did use the CFP domains. If you think about it, that's kind of arbitrary. These are some domains that you could actually split it up a number of different ways. 

The Ultra High Net Worth Institute has 10 domains. You could look at it that way. There's a variety. 

If you've included businesses, where does that flow? Is that an investment? Is it part of retirement? 

There are different pieces. And depending on how you define the objective functions, you could change a lot of this. The idea was to make it a little bit... 

I said I was leaning into the complexity, but at some point it becomes unwieldy. And then you have the discount matrix, which interacts directly with both the structural tensor and then the priority weights. And the idea there is that you then get this discount-adjusted coupling matrix where you can assess the strength of the coupling between the domains based on how somebody values them at a certain point in time. 

It's just a way to assess how the planning strategies can affect somebody's financial picture. And so in order to do that, you have to build a structure that can support that kind of thinking.

Ben Felix: You talk about this in the paper, but the human financial planner is kind of this processing machine that thinks about all this stuff sort of subjectively. And we do it. We will go through a financial planning projection and show, well, if you do this, this is the outcome. 

If you do that, this is the outcome. And then we'll kind of get a feel for how the client responds to that. But you've quantified that, which I think is really cool.

Michael Kothakota: And I want to talk about where my thinking of that came from is that something as simple as if I throw a baseball to you and you catch it, your brain did a bunch of stuff. A lot of it was unconscious, but essentially, it did some calculus. It figured out what the trajectory was.

Actually, I did talk to somebody who disagrees with me who's a mathematician. But I think that you basically applied this math to it because you figured out how to catch it. You've identified where it's going. 

You put your hand out in time. You squeezed your hand in time. That complex thing was distilled very quickly. 

You didn't have to write out an equation on how you were going to catch it. I think it's very similar in this respect. So if you're an experienced advisor who's trained, you start to kind of understand how to kind of reduce those dimensions naturally. 

And yes, it is a little subjective, but based upon some experience.

Ben Felix: It's intuition gained from professional experience. You mentioned the tensors. I learned a bunch of words from your paper that I hadn't really seen in this context before. 

So your paper also talks about curved surfaces, cornered spaces, binding constraints, manifolds, and corners. I'm reading this like, what is happening? Can you talk about what that stuff means? 

What is the shape of financial planning and why does that matter to the understanding of the overall system?

Michael Kothakota: So I'll be the first to say it's weird. I thought about this as spheres and then I thought about it as a series of interconnected spheres. And then as you start to think about it, there are a lot of constraints in financial planning or most constructs. 

So a sphere is not infinitely expandable debt, there are borrowing limits. And so if you have all of these different interconnected things, which at first I thought, well, that was how I was going to solve it with just topological spheres. By the way, I thought that that was what I thought the breakthrough was. 

And then I started running into all these problems. And so what a manifold is, and it actually doesn't have to be a manifold. Manifold is just, you can think of it as like the financial state. 

If we go back to the wave function, it's like the financial state at any given point in time. And there are different probabilistic outcomes to that financial state based on decisions that are made. So that is what the manifold is.

I think there's this guy at... What's the name of that university? It's in Kansas, not Kansas State.

This guy, he studies ring theory. And so if you know what a torus is, which I didn't know what a torus was either, but a torus is basically like a donut, a ring, essentially. This theory can work in that if you can imagine that space. 

But I also felt like that even that just seemed pretty hard. So the manifold is just like, we're just going to say, hey, look, this is the state space. And this is your financial state and the probabilistic structure of a client's financial state, their life. 

And so a lot of the constraints will bind at the same time. And so that will produce these corners. You can't have negative wealth in any account. 

If you have negative wealth, it's basically debt. Assets, really, they can only go to zero. So you have that. 

You have borrowing limits that are tied to income. You have liquidity requirements that are for upcoming expenses. You got a number of issues. 

And so what happens when two or three of those will bind at the same time, when they occur at the same time, given the set of circumstances. So if you reach your borrowing limits, you don't have enough liquidity for your expenses, then you've got what we would call a corner. Why does that matter? 

Who cares if you've got a corner? If you were trying to move around in this room, we've got a lot of corners in this room. But if you're moving around a room and the walls are curved, then you've got three or four walls meeting together. 

Let's say like a T or something like that. You can't move around that wall specifically because it's bound in multiple places. I think that's the easiest way to think about it. 

It's a little bit more complex than that. That's why that matters. But then why does it matter for this paper? 

Standard optimization assumes smoothness, smooth, unconstrained, which makes it easier. And it makes it a much easier problem to solve. So a lot of the optimization that we do and a lot of the optimization that operations research and decision scientists do, they start with smoothness. 

But we've got these kinks because of how financial planning works. We live in a non-smooth world. And so we've got to respect that with whatever math we're going to use to describe it.

Ben Felix: Like simple two-dimensional calculus, you can fairly easily do an optimization. But you're talking about doing optimization over a three-dimensional surface that is not smooth. I mean, that's what you're trying to solve.

Michael Kothakota: Exactly. It's not differentiable at that corner. That's actually a way better way of saying it.

Braden Warwick: So how do the fiber bundles come into your theory?

Michael Kothakota: So if the state space is the manifold of people's financial states, well, we as financial planners or even individuals, we execute strategies to optimize our financial life. In most utility functions, we wouldn't typically have things that change. The fiber bundles are your strategy space. 

And it's just a way to think about that the strategy affects the manifold. And so the way it's visualized in the paper is that the fiber bundles sit above the state space, and then they're going to change. So your strategy space changes for a variety of reasons. 

Here we have Medicare age. Things you do with Medicare when that occurs are different than what you would do before. Social Security exists for the time being here.

And at some point, you can draw on that, even though you die. A lot of times, a lot of estate planning is, well, what happens after you die? A lot of strategies that can occur up to that point, but then less that can occur after or maybe even more that can occur after. 

So they change. And so fiber bundles, they're a way of thinking about how the strategy space evolves over time as well. In addition to those structures, those things that happen, a lot of other things can happen. 

Legislative changes. One of the things I do with clients is we do an annual simulation where we'll simulate a macro event. And then we'll start to also simulate some smaller level things that are idiosyncratic to them that could affect their lives. 

I don't use this one because it's pretty catastrophic. But if Yellowstone erupts, that's a pretty big deal. That's going to affect a lot of things.

That changes everything. The collapse of the dollar, the current decoupling and transactional relationship that my government is currently engaged in, that has changed how we interact across borders. That changes a lot of things. 

And so that's what those fiber bundles are supposed to represent. It's to see at these different phase transitions and then different events that occur, the strategy space changes and we need to adapt to those changes. That's how it captures it.

Ben Felix: We've got this kinky three-dimensional space that's all weird and stuff. And then we're trying to solve it with strategies that exist. And so you can do that optimization at a point in time. 

But then as we move through time, the available strategies are going to change and that's going to change the optimization process.

Michael Kothakota: That's essentially what's happening is that your strategy does change. And what you do for a client at a particular time, divorce. That's another thing, death of a spouse, the strategy set changes. 

This is actually my counter argument when people say it's a little too complex is that we don't have access to the same strategies or need of the same strategies throughout the life cycle. We need to have the ability to adapt and that's the point of the fiber bundles.

Ben Felix: In the mathematical model, what domain objective functions are being optimized over?

Michael Kothakota: So cashflow, that's a very simple one. It's margin between income and expenses, liquidity reserves, debt service coverage, retirement security. In this case, this particular one is maintaining a target income through life expectancy. 

You could use replacement ratios, you could use shortfall probabilities. I actually modeled a number of different ones. In some cases where the numbers can be higher, frankly, depending on what objective function you use.

Tax efficiency. So that's tax rate, current and future. That's a little bit hard to model because although I always feel like in this country, like, okay, well, they're gonna get lowered every 4 to 8 years and then they raised every 4 to 8 years, just in general. 

So I just modeled them as based on income and whatever the current rate is. Estate effectiveness. So that's how effectively were assets transferred to heirs versus charities. 

And then align it with whatever their legacy intentions were. Actually, the Ultra High Net Worth Institute has this really interesting function that they developed for how that works. Risk management adequacy just deals with coverage, making sure that the risks that we typically manage can be managed, although that can be adjusted too. 

And then across countries, I think there's a lot of fascinating ways to do that. The investment performance is just a risk-adjusted return using like Sharpe ratio. But even that, you can use any sort of model to include in there. 

And I did test a few others, but basically very similar results. The challenge is like how you can actually simulate this across all domains. It's really difficult. 

Those are the objective functions that kind of flow. They become unitless. They result in the effective tensor, and then they're recalculated out in the value function.

Braden Warwick: In your paper, you assigned a weighting function to each of the domains like cash flow, weighting on cash flow, tax, retirement, and so on. But would you think about assigning a weighting factor to each objective? Would you potentially change the objective function depending on client preferences? 

Or would you just leave it at the level of assigning weights to each domain?

Michael Kothakota: I was presenting this at Texas Tech. Nobody asked the question, but I did mention it. You could argue that it's arbitrary. 

I chose these functions. A, I didn't think of the idea of weighting them. I like it. 

I also didn't think of this objective function as best for a particular client. I like that too. What I did think about was that I want researchers to say, okay, well, let's test these.

Let's go through and let's actually test to see on real situations if we can, what is the best objective function. But my guess is it's very similar to the priority matrix and that it's idiosyncratic. That's a really good idea. 

I like both of those. The point is for people to take this, test it, see what's working, what's not. Maybe things need to be adjusted. 

Maybe it's not actually representing what I think it represents, but I like that.

Braden Warwick: We talked about the natural kinkiness of financial planning.

Michael Kothakota: It's very kinky.

Braden Warwick: How do you solve for that? When the objective functions aren't smooth and the topology is not smooth, how do you actually work around that from a mathematical perspective?

Michael Kothakota: There are two ways. One was to deal with the non-smoothness, used what we call viscosity solution. So you guys think about it as if it's non-smooth, if you have like a thick liquid over a corner, and that's the way I visualize it.

You put it over some honey over a corner. It's kind of smooth at that point. And then there's Clarke generalized calculus. 

So they're integral differential equations. So I had to spend a lot of time learning. It's a combination of integrals and derivatives for folks who don't know what those are. 

But the Clarke generalized calculus kind of helps with handling the kinks. It's a way to capture a set of all the possible limiting directions. So if you kind of think about, you know, if you've got your function that's moving, it could kink up or could kink down. 

It's a way of capturing like those potential changes. In most cases, things like a tax bracket is kind of easy because it's probably going to go up. But I mean, if you're talking about estate or something like that, and you're trying to optimize in the US anyway, we have very low thresholds for like higher estate tax. 

If you're trying to optimize between how much for the trust to pay versus how much for the beneficiary to pay, there's a lot of interesting things that can happen there. That's essentially the two methods that I used. I think you could actually use viscosity solutions on both. 

I think I tried that. And then what happened is you lose the assumptions of uniqueness and existence in the Hamilton-Jacobi-Bellman equation.

Ben Felix: Viscosity solutions in financial planning is not something that I would have...

Michael Kothakota: But it's a word though that makes sense.

Ben Felix: I get it. Yeah, yeah, yeah. 

Michael Kothakota: Clarke generalized calculus is just like a guy who had it, you know, it's named after him. So that's a little bit more challenging. But if you know what integrals and derivatives are, and they combine, and how you can deal with those different directions, I think financial planners should be able to be like, okay, I get that. I get what that means.

Ben Felix: Oh yeah, it makes sense once you've explained it all. If someone told me that we're going to be talking about viscosity in a financial planning conversation, I would be like, what are you talking about?

Michael Kothakota: I think financial planning is like the stepchild of research. And so every other field has all these really cool things if we just look to those other fields, we can pull them in and then they start to make sense.

Ben Felix: Can you talk more about how the priority matrix in the model works?

Michael Kothakota: Six by six matrix, diagonal matrix. There are weights for each of the domains, each of the planning domains. And so it's designed to capture what's important to a particular client. 

The idea being, in general, this is how somebody will prioritize these things. And so the big deal from my perspective is I think a lot of the things that we say are irrational behaviors are just preferences. There certainly are things that are irrational. 

Originally in economics, when we talked about people behaving rationally, it was consistent. It was behavior that was consistent with how they wanted to live their life. And then in order to make things work, we were like, no, these are the things that are rational. 

Wealth maximization, all of these things, these are the things that are rational. So if you deviate from that, then that's irrational as opposed to, well, wait a minute, people have these different preferences, which of course, we attempted to capture in a variety of things, but in economics, generally like indifference curves and things like that. So each one of those categories is weighted. 

So you ask people like, how important is this to you? And there are a variety of ways to do this. Financial planners do some of these things naturally. 

And some of the questions to make it work in the paper, like, hey, rank order these. That's hard for people to conceptualize. Well, what do you mean rank order them? 

And then now you've got to still move the weights around to make sure that it works. Revealed preference tests are a possibility. You could do like some pairwise comparison of how people think about the different ones. 

And so then essentially what you do is you end up with a set of weights that then get applied to each domain. And then when the structural tensor gets filtered through that, then you now have something that's more appropriate for that client. And originally, there was no discount matrix in this. 

It was basically like, okay, well, yeah, this makes sense. But then I started thinking things change over time and how that works.

Braden Warwick: Can you dig into that a little bit more? How does the relative urgency of various goals get reflected in the model?

Michael Kothakota: So in my class, I teach a weird combination of financial mathematics and ethics. One of the things that I have students do is, especially in the age of AI, if they're solving a simple time value of money problem, I actually have them create the discount rate. And discount rate construction in a normal problem, a CFP exam, CFA exam, you're usually given a discount rate. 

Business evaluation, sometimes you're given a bunch of things that you create a buildup rate. You'll create a discount rate through a variety of approaches. Intuitively, what we do is we apply those discount rates to different priorities. 

So something like retirement, maybe I'm putting money in a 401k at 25 or I'm thinking a little bit about retirement, but it's not urgent. At 50, and I realized I've saved 50,000. Well, it starts to become a little bit more urgent. 

I start thinking a little bit more about it. And so the discount rate, it gets applied to that priority. It's like, okay, it's important, but it's not important right now. 

The higher the discount rate is typically the more urgent it is. Risk management has a half-life of 10 months because you need coverage now. You need to make sure that if you get in a car wreck, that you're able to buy a new car, you're able to pay your medical bills, etc.

But estate planning, typically, that might be really far off. I started thinking about that a little bit more too. I'm like, but are those fixed? 

I don't think they are. So they can be treated as random because there are a number of things that happen in your life that change, that change you and change how you think about stuff. I started out in the Army and now I'm a financial planner talking about tensor mathematics, fiber bundles and manifolds with corners.

You've got that baseline, which would be the long run mean, basically how you think about that particular thing. And then you've got those endogenous adjustments. So as your financial state changes, you start to think and your age changes, you think more about different things. 

And then you've got the exogenous shocks, the divorce, the death of a spouse, the birth of a child. And all of those things now change how you think about stuff. And so that will affect those rates.

And so they're treated stochastically in the paper because of those things. Because we actually don't know how all of those things are going to play out.

Ben Felix: The discount rate for estate planning will be one thing now, like when you're sitting here recording a podcast, it's one thing. But if you have a near-death experience or if a spouse dies or if you get some kind of diagnosis, the discount rate on that could change. Is that kind of what you mean?

Michael Kothakota: Yes, all of those. And then they see what their parents had to go through. They had to settle the estate. 

And they're like, wait a minute, I don't want my kids or my wife to have to do any of that. So now all of a sudden, it's much more of a priority. We need to get these things fixed. 

And so something like if you get a health diagnosis, how that's going to affect all of the different domains, right? So it's going to increase urgency in a lot of things. It's going to increase urgency in estate planning, your risk management, and your cash flow.

Because you're like, well, wait, I got all these bills. Maybe I can't work. And I need to make sure that my family is taken care of.

Ben Felix: The reality is that can change over time. And so when you're building an optimization, like, okay, how do we build an optimal financial plan? What does that look like? 

You have to account for the stochastic nature of that variable.

Michael Kothakota: You have to try to. I mean, I think I went back and forth on this a lot because I thought, well, the wave function, like we just don't know what that state's going to be. Estimating is the best that we can do. 

I think we should treat them stochastically because they are going to change. And we don't know ahead of time, but people do think they know how they feel at that moment about each of those priorities. They can weight them then, and they can think about how urgent is it. 

They can think about that now, but then when things change, those things change. So we can both take their word for it and not take their word for it because of all those things that can occur.

Ben Felix: Should financial planners be influencing those discount rates?

Michael Kothakota: I think they should explain them. I think they should be talked about. I think it's a useful exercise to talk to clients about these things, how they weight things. 

A good example is because people use risk tolerance all the time. And so sometimes it doesn't matter what somebody's risk tolerance is. Maybe they have a really high risk tolerance, but they've already got $400 million. 

Well, who cares? They can do whatever they want. But if somebody's got a really low risk tolerance, but they're not going to be able to meet any of their objectives, they need to be educated. 

And so I think it's similar in this sense. We could spend a whole other podcast on risk tolerance and my thoughts on that. It's similar here where it's like, you're not prioritizing retirement, but you will. 

You're 30, you're unmarried, you love your job. So you're not thinking about it, but here are all the things that can occur. You need to think about how you would prioritize that. 

Same thing with insurance. People don't get life insurance because they think nothing can happen to them. Well, let's actually look at... 

First of all, low probability events happen all the time. It can happen to you. Is it likely? 

No, but what are the costs associated with that? And then you could dial in a discount rate. I think if you can show people what that means mathematically, I think it's a useful exercise.

Ben Felix: To re-anchor listeners, we're talking about how important the different financial planning domains are to someone who is making financial decisions today. And someone who's very far away from retirement might not think that retirement is very important to think about. But we're saying that the financial planner in that situation should maybe be talking to them about why they are going to care about that one day, which should influence how much they care about it today.

Because with compounding and stuff, you can't solve for it later the same way you can solve for it now.

Michael Kothakota: The way I would approach it with a young client is to say, I get it. I understand why you're not prioritizing that. Absolutely.

I want to walk you through some things. Even if you're a new planner, you could say things like, I've seen cases where XYZ has occurred and then all of a sudden it's too late to think about retirement. Or you now have to sublimate a different value.

People talk about like work-life balance and flexibility, temporal flexibility, and stuff like that. Well, if that's a priority for you, now you can't do it because you're 50 and you didn't save for retirement. So let's think about it.

That's important to you. So let's talk about that. I think it's absolutely something we should be talking to people about.

Ben Felix: Super interesting to think about. Can you describe the four-tier architecture that summarizes your model?

Michael Kothakota: The structural tensor is a rank-three tensor. So basically you can think of that as like a three-dimensional object. And then it's basically, what it's doing is it's, you've got different domains and they affect each other. 

A affects B, which affects C, which affects D. But A also affects C, which affects D, which affects E, and so on and so forth. So there's a lot of different interconnectedness. 

If you do something in one area, it's going to affect all these other things. To a certain extent. So some of the couplings are strong. 

Some of them aren't. One thing doesn't always affect something else. That is the objective mechanics. 

And then what matters most to the client, which is the priority weights. We get those through discovery meetings. We get those through learning about the client. 

I don't think you really know a client completely and for a few years, at least. And then there's the discount matrix. That's the urgency structure. 

So how urgent is something to you? And then those get synthesized together, which is the complete change from the objective structure, the subjective priorities, and then the urgency. The practical purpose is that, theoretically, we can pre-compute the structural tensor. 

We can update that as regulations change or social dynamics change or whatever. We can update those things. And then the priority matrix, we have to get that from clients. 

That part makes sense to separate. The other thing it does is it reduces computational burden. Because if you try to do all that at once, it's a lot of parameters.

It's more personal if you do it that way. That's the architecture in short.

Braden Warwick: So how are you capturing uncertainty in your model?

Michael Kothakota: Some piece of it gets captured in the discount matrix as far as how people feel and how people think about each of the domains. We have to think about, so there are the things that we can plan for, that we do. Okay, you need X insurance adequacy. 

And so we can treat that uncertainty with either self-insurance or risk sharing or risk transferring to something else. In investments, for example, investment volatility, that's exogenous. But portfolio exposure, it's endongenous. 

It's how you created it. It's within the system. You created the exposure. 

Longevity risk is exogenous. But the financial consequence of longevity risk is endogenous. You've got the endogenous uncertainty and then you've got exogenous uncertainty, things that are outside of the client's control, but we could anticipate. 

Things like tax law changes, macroeconomic conditions, regulatory changes, pandemic. So we can anticipate that, but we don't always do it. Before I even finished this, this was a piece that I thought about really deeply and also was unsure how it would actually fit into the theory. 

I do this with clients. I actually talked about a lot of these exogenous shocks. And what is interesting from the perspective of the client is that just planning for it, something that may never happen. 

The year before, simulation was China invades Taiwan. I usually try to pick something that's not too on the nose, but that could happen. We looked at the cascading effects of how that would affect them. 

Just going through that process is really helpful in showing that you care and that you're thinking about things. But also it creates a little bit more connection, involves them in the process, makes them feel a little bit more in control of a lot of these things that are actually outside of their control. It's not something they can do anything about. 

We can only react to those things. That's how we capture exogenous uncertainty. There's the priority uncertainties, priorities shift as life unfolds. 

And then there's the rate uncertainty with the discount rate. Those are the four ways that I try to capture uncertainty in the model.

Ben Felix: I love that point about we don't do specific simulations like what you're talking about, like event simulations, but we do basic Monte Carlo type stuff. And it's such a powerful thing to be able to say to a client when the market's down 10% or whatever to be able to say, well, we factored this type of outcome into your financial plan and it's still good. That's why we did it this way. 

I think that's always reassuring. But the idea of doing a specific event is a pretty cool idea.

Michael Kothakota: I don't have hundreds of clients, so I try to keep it small on purpose. So it is time consuming. Somebody with 500 clients should not do it. 

100 or less. It's probably something that's doable and they love it. It's kind of a fun thing to do.

Ben Felix: You built this wild model that we've been talking about. What are the main theoretical results from the model?

Michael Kothakota: Somebody actually mentioned this the other day saying it was empirical proof. It is not empirical proof. This is theory.

It's using client fact patterns that exists for me and then like kind of anonymizing a bunch of it. It's very theorem heavy and I felt like that was necessary to show what was happening. So there's the structural piece of it. 

That structural coupling really only matters if a client assigns priority to it. So that's one. There's the stability and separability. 

So that's essentially like if you have a systemic event, the stochastic separability conditions are more strict than a deterministic one. Time value of money projections are very deterministic, but obviously don't capture a lot of things. When we treat those domains independently, it can destroy that separability. 

There's an integration premium. So there's the value that you provide in each of those domains. So like as a financial planner, even if you're not fully thinking about the interdependent nature, you're still providing value. 

So like if you think about things like Morningstar Alpha or Morningstar Gamma, Vanguard Alpha, we use all the Greek stuff here. Priority Lambda is what we have here. There is an appreciable difference from the actual integration. 

If the separability conditions are not met, what ends up happening is the integration premium goes away and so it doesn't actually matter. That really doesn't even make sense, but it will never be less than zero. So the integration premium will never be less than zero if it's done correctly. 

Dealing with like the jump rates for like the uncertainty events, if you're accounting for things like that, that can boost the premium even more. It would be great to be able to see this happen in the wild. Those are the main theoretical results. 

Although in the paper, I think I mentioned this at the beginning, I also added a value loss. If you don't have a good idea of what the client's values are, if it's misaligned, it's like a mean 4.8% loss in value if you don't actually identify the client's priorities well, which doesn't sound like a lot. It can be quite a bit depending on how long that lasts. 

And I'm not saying that we always will have perfect alignment on priorities. That's one of the reasons it's a big deal. That's one of the reasons I think that human advisors matter is because it's very difficult to do. 

They change. There are some significant costs to that.

Braden Warwick: So how should financial planners think about applying your mathematical model to real financial planning scenarios?

Michael Kothakota: The first thing is to really think through how a course of action they might be thinking of recommending or their firm is telling them to recommend or however it works, wherever somebody is, think through like, well, what are the effects in the other areas of this client's life, both now and in the future? We have a strong tradition here in the US of a lot of insurance companies leading with insurance products. There's not anything wrong with leading with insurance products inherently. 

If we are not thinking about how a whole life policy or universal life policy affects somebody's cashflow now and how they prioritize things, then I think that we're definitely not providing a lot of value. So I think the first thing is to think, okay, well, here's a strategy we would normally use in this particular fact pattern. What are all of the effects that it can have for this particular client? 

That's one piece of it because we're not going to get their values initially. And when people present, they give you their financial information. So you do already have to start thinking about that stuff. 

But also along the way is to start thinking about how can we identify what this person values? I had a student read the paper, requested to talk to me. And he mentioned in his email that he thought that if we're bending to somebody's priorities, then they can actually end up with ill-being. 

So they end up worse off. And the example he used was, well, if somebody is looking for prioritizing financial success, that could theoretically affect their mental health, and it can affect all these other things. And so my question to him was, okay, well, is financial success the actual need and value? 

He got it. He realized, okay, yeah, well, maybe... Because the financial success is like a strategy. 

Financial success is a strategy to solve something else. So what are you really trying to do here? To demonstrate how difficult it is to elicit values from people, train on that. 

There are a lot of programs that help identify certain priorities. Asking them directly, sometimes can be helpful, at least as a starting point. Asking them questions. 

Have you thought about your legacy? Have you thought about when you might need these investments? So if you're in a whole life policy and you need some money in a few years, well, maybe that's not the best place for it. 

But conversely, maybe it's useful for somebody who's late in life, who needs to pay estate tax or whatever. If I'm thinking about real-world scenarios, I want to be thinking about how it's going to affect other things. I want to try to model that to the best of my ability. 

And then I want to make sure that what I'm presenting is aligned with what the client wants. To your point, Ben, I think it would be a great exercise to walk them through, how are they feeling about these things? And then how does that relate to how they would feel about them in the future or if certain events happen? 

And then you've captured the three main portions. I don't expect people to compute a structural tensor or an effective tensor. I don't expect that.

But thinking about these things, especially for newer planners, older planners, skilled planners, they're already doing some of these things naturally. It's hard to be successful if you don't know what your client wants and you're misaligned. So I think they're already doing some of those things. 

But if you're a newer planner, I just really start thinking about these things. If you're an experienced planner and you're not thinking about them, think about them.

Ben Felix: So it's really thinking about how if you're making a recommendation that's designed for whatever, estate planning, it's really thinking through, okay, how does that interact with the retirement goal? How does that interact with cashflow? How does it interact with other investments, risk management, tax, all those pieces together and how they affect each other. 

And then that is informed by what the client says they care about among those different financial planning areas. And you've basically shown with your model that there can be pretty significant value gain or loss by thinking about those things together properly.

Michael Kothakota: Yeah.

Ben Felix: Very cool. Can you walk us through an example of the sort of pitfalls or costs or whatever, however you want to frame it when expert domain specific advice is delivered in silos? So if you have like the investment expert and the tax expert working separately as opposed to integrated.

Michael Kothakota: The best one is the Delgado scenario, which is she's a business owner. I see this a lot with like high net worth people where they've got a person who does like whatever and maybe they don't have somebody to coordinate it all. So they've got a tax person, they've got an investment guy, they've got an insurance guy, they've got an estate gal, all those things.

They say all of these things and they go to those people and they say, hey, here's my situation. I've got this business, here are the things that I want to do. That person will ask really good questions about their domain. 

They will ask really good questions about, okay, well, how is your business structured? How many kids do you have? Is anybody working in the business? 

They ask all of those things. But they often don't think about what the effects are on any of the other domains. So in the Delgado example, the estate planning attorney recommended these family limited partnerships with this nice grass structure. 

It's going to save like $1.8 million in taxes. But this particular client was prioritizing cash flow. She started this company because she was worried about money. 

She needed money. And that's kind of never gone away in this particular case. She's really worried about financial security. 

So moving all this money into these trusts, it eliminated a lot of business distribution. So A for saving taxes, A for estate planning, F for making sure that this client got what they needed. And so that $1.8 million in taxes, that's great. That sounds fantastic. Insurance agent proposed this huge insurance policy with a big premium, again, cutting into cash flow, which is duplicative of what was going to happen through the estate transfer. Retirement, especially a lot of people say in the US, we always talk about delaying. 

There's a big debate between delaying Social Security and taking it early. And an economist will tell you like, well, it's dumb to take it early because you get 8% per year. So you take it early, that's costing you an 8% with no standard deviation. 

So other than inflation, actually, even with inflation, because inflation is included typically. So they'll tell you that that's not optimal to take it early. So they're going to recommend taking it to 70. 

But then in this particular case, the portfolio was depressed because of downturn, which now makes this person have to take withdrawals in a suboptimal situation. If somebody integrated that where there's claiming at 62, retaining some portion of the business for a period of time, insurance that actually kind of fit what was actually going to cover things. Well, now you've got, instead of the 1.8 million estate taxes that are saved, or the transfer of risk to this insurance policy that would have saved some money, or even transferring some of the risk to later years for the investment, the integration premium here was like 2.2 million. And so that's in addition to some of the other savings, because this wasn't going to be a full 1.8 million in estate taxes that was saved, but some portion was going to be there. So it's 2.2 plus 800,000 plus say another 1.2. And so now you're starting to see a lot more value. So that's where the pitfalls of that siloed advice comes from. 

Firms have goals. If you're an insurance company, your most profitable item is a whole life insurance policy. So I get it. 

I'm not trying to say like, you shouldn't try to find people who need that. But if you're going to be an advisor, and you're going to be somebody who is going to have a fiduciary obligation to a client, you have to think about all of these things. And even people who work at the big brokerages, like they don't say they're investment people.  

They say they're full financial planners, but they lead with investments. Definitely think about that as part of the pie, but we should be thinking about how this affects other things. And I think what ends up happening is it's like, well, we need to get assets in the door.

So you need to generate assets. And one way to do that is to say, well, here's how our investments have performed over 10 years, assuming that we can actually continue to do that for the foreseeable future.

Braden Warwick: Does this value of integration and financial planning scale linearly with wealth?

Michael Kothakota: I don't...no. It's a little bit more nuanced than that. I think it scales with complexity. 

A very simple thing where somebody has served in the military, they're going to get a pension, they're going to get social security, they don't have any assets. So there's not really a whole lot of estate to kind of plan. That premium is going to be a lot lower. 

They probably need some insurance. They need to make sure they have enough cashflow. But the couplings are going to be a lot weaker. 

On the other end, if you do have that, it could be wealth. It could just be complexity. If somebody is a gig worker and they got 20 different gigs, and then those turn into like, well, now I've got four Airbnb properties and I've got some people working for me who are driving.

I transitioned my Uber business out of Uber, but I'm still providing driving services. But I've got three people who work for me to do that. That complexity, the value, I think, increases when you have more of that complexity.

It's intuitive. It also kind of bore out in the examples. As things were more complex, there was more value generated.

Ben Felix: What do you think the theory suggests about the role of human financial planners?

Michael Kothakota: Well, that they're necessary. We have a hard time articulating what our goals are, even what we value. Like we go through life, we take hits, we move.

We very seldom have time to think those things through. And I think one of the things that planners do is that they can think about the various consequences for certain actions. And we have training. 

We have financial training. We have... It's not really legal training, but we understand how a lot of these structures work. 

We pay attention to the economy. So we understand a lot of the exogenous issues, but then we also get to know people on a personal level. And I think what happens is people in general, they think that some of these big macro things are things that they always need to be concerned about, or it's going to affect everything they do, and that there's no way to really plan for it. 

Or that, hey, well, I listened to XYZ Influencer. I've already got it figured out. I'm gonna be rich, sort of thing.

What's missing is the fact that a lot of this, I think, is done intuitively. These ideas came from practice. Like I've practiced for years. 

I've been doing this almost 21 years. And so I've observed what happens and what I do and how I've changed how I practice to account for a lot of these things. What humans do is we have that ability to talk to a client, look at a situation, and realize like, okay, well here, we can narrow the choice set significantly, it becomes much more manageable for people.

I think a lot of times people come in, and especially even wealthy people, they've got a massive choice set. I have a client who his anxiety is so high because his choices are like, at this point in his life, are basically unlimited. I'm like, man, you just gotta start making decisions. 

Not that we're gonna fix anxiety or anything like that. But if we can help people narrow their choice set, become more optimal for them, people talk about the optimal outcome. And so a lot of times that's like, it's wealth maximization or higher investment return. 

And one of the things I tell students is that optimal is not always best. And so what's best for a client may not be what you think or what I think is the most optimal or what an economist thinks or anybody else who does optimization for a living. This essentially describes the complexity of what we do and why it has to be a human to do these things.

Braden Warwick: So AI is the hot topic these days. From your perspective, how does AI interact with the value of a human advisor?

Michael Kothakota: AI is pretty useful in a lot of ways. It can create some content. It can be a good thinking partner to think through certain problems. 

It's not gonna think of all of the consequences for a particular course of action. So there are do-it-yourself people who probably can do this. So I don't wanna be like, hey, they can't just use AI to come up with a good financial plan. 

A, there's a lot of friction there because now you gotta check in with AI all the time about what's happening. The AI has to ask you some of these questions. Maybe you could program something that says, hey, we're gonna update your discount rate. 

We're gonna update that today. Maybe that can happen. But also people have lives to live as opposed to the planner who's like, hey, I'm gonna dedicate this time to deal with these XYZ functions. 

That's a big part of where I think humans can have that value. But we could use the LLMs to be like, okay, look, I've got this client. Here's the situation. 

And then when it spits something out, you can then think of, here are the second, third, fourth order effects that the model didn't think of or didn't want to expend the token to provide you with that information or both. It can make for a better product. I don't know if it really makes people more productive because my wife and I both have been using it a lot for a lot of things. 

And sometimes we end up with the same result. But also, we spend a lot of time fixing things, asking questions, checking. Not that these errors are massive errors.

It's just that if we delegate the whole thing to AI, it's not going to think of the follow-on things to do. It's not gonna be monitoring things because it's not a person. It's not a real thinking machine. 

It's not proactively thinking about what happens. There are times where I'll just sit in my office where I'm thinking about a particular... Or up at night, thinking about a particular client case, something that I hadn't thought of or some sort of epiphany or I realized, okay, what they told me about what their priorities were is not exactly accurate. 

How can I ask them in a way that doesn't get them defensive? All of those things that I do not see AI doing, but I do seeing it say, hey, look, this is the situation as I see it. And then it giving me some information that I can be like, oh, okay, yeah. 

I think that makes sense. Or that's a good direction, but let's think about it this other way. This is how I think about AI. 

This is how I think about how useful it can be. Avengers: Endgame, Tony Stark, there's a scene where he figures out time travel, right? He's talking to the AI.

He tells it what to do. And it outputs basically the model for time travel or whatever. But it was his insights that crafted. 

Now he had to go back and check because you can actually see after that scene, he's like looking at a few things. He's double checking to make sure that the artificial intelligence actually did it right. And then he tells his wife that he solved time travel. 

That's how I think about it. I think it can be that useful if we know how to do it, but it's not going to solve that. It's not gonna solve something like that on its own. 

I think it's the same thing with clients. I can ask it some things that are very specific to a client's situation and I can probably get some good insights. And then I can say, well, let's do this instead and let's see what happens. 

One of the interesting things I think, especially around tax planning, especially around things where there's some ambiguity for like in the tax code. Here, there's a lot of ambiguities for certain things like business owners. There's a rule, but that rule is not codified in any way that you can quantify what somebody should do.

But you can get information about it. We have this thing called the S corporation and S corp allows you to avoid payroll tax on distributions. But the IRS is like, hey, if your salary component is not high enough, then we're gonna come get you.

But there's no threshold. There's no number on that. They say it has to be reasonable. 

So reasonable means a lot of things to a lot of different people. So you can actually have the conversation and say, we're like, all right, these are my job functions or this is the client's job functions. Give me some information on what that job function costs in this area or whatever. 

Maybe they're a CEO, they're a financial planner, they're also the custodian. They may be all those people rolled in one. So their value is split among those things. 

And so building in, well, what is the salary component versus what is the distribution component now becomes a much more complex problem. The LLM is not gonna know. It's just gonna say, well, it could be too high, it could be too low, but you can use it. 

So there are a number of things like that, I think, in planning that make us way more valuable if we can use the tool. So that's my personal take on it. It can be useful. 

I certainly don't see it replacing it. I just don't understand how that would occur, I guess.

Ben Felix: All right, last question for you, Mike. How do you define success in your life?

Michael Kothakota: This paper has been kind of a journey in that. So success for me is being able to, on a whim, stop the day and go sit on the deck with my wife and have a beverage, provided the weather is not as cold as it is in Canada, or by the fireplace, which probably would be more appropriate for you guys. And to be able to spend time thinking of things like this, to spend time in an endeavor that engages my brain, to me, that's success. 

If I have the time to do those things, then I'm successful.

Ben Felix: It's a great answer. Awesome. All right. 

Well, I don't think listeners are going to be disappointed in the level of nerdiness in this episode. So we appreciate that, Mike. Thanks a lot for coming on the podcast to talk about your paper.

Michael Kothakota: Thanks. I really appreciate it.

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