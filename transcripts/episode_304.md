## Episode 304

Ben Felix: This is the Rational Reminder Podcast, a weekly reality check on sensible investing and financial decision-making from two Canadians. We're hosted by me, Benjamin Felix, and Cameron Passmore. Portfolio Managers at PWL Capital. 

Cameron Passmore: Welcome to episode 304. The band is back together again today. And we've got a pretty hot topic, I think it's safe to say, guys, with the recent announcement by the Federal Government of Canada for some proposed changes to the capital gains inclusion rate. How much tax people pay on capital gains? And this has been super-hot, which we'll talk about in the after-show. Because it was a pretty wild week on Twitter and other sources of media in Canada for you guys. But that's the main focus of today's podcast. Anything you want to add to that? 

Mark McGrath: Obviously, it's topical. It's something that I think people have been anticipating in some respects at different points. 

Cameron Passmore: It's been speculated for years. Every year it comes up, "Oh, it's time to raise the inclusion rate."

Mark McGrath: Yep. And I know advisers have made changes to client portfolios. Not here. but like in my old world. They made changes to client portfolios in anticipation of this, which in hindsight wasn't the right idea. But you're playing this kind of chicken and egg game. Trying to get ahead of it. 

Today we'll break down how capital gains works. How the new proposed inclusion rates work for both individuals and corporations. Ben's going to talk a bit about alternative minimum tax, or AMT, which is another proposed change in the budget that has some pretty significant impacts in certain cases. 

And I know Ben has been doing a ton of modelling on these new proposed inclusion rates. And the big decision for a lot of people is do they trigger capital gains now to get ahead of this change? And what are the impacts? And the answer is not always cut and dry. I know Ben's been doing a lot of work on that. If people have questions about that with respect to their own financial plan, obviously, they can reach out to us.

Cameron Passmore: It's interesting to dig into the decision points before you make a rash decision based on what the headline story might be. 

Ben Felix: We've been spending, like Mark said, a ton of time modeling this. I've spent more time writing Visual Basic code than I've probably ever in my – I don't usually use Visual Basic that much. But I have a tax function that I have written in Visual Basic that I used to do different types of modeling. And because of this change, I've had to rejig that tax code. And it's been difficult because of the way that all the stuff interacts with different parts of how taxes are calculated. That's been lots of fun. 

Yeah, like Mark said, we've spent a lot of time modeling it. And we've got our clients queued up for who needs to be contacted for what. Who it's going to be relevant for? And what we're going to advise them to do? But if anybody who's not a client has questions about their situation, feel free to reach out.

Mark McGrath: And, Ben, you made a publicly available calculator for personal capital gains taxes. Not for corporations at this point. But for personal capital gains where people can go for free, and model their own scenario, and get some insights.

Ben Felix: Yep. That one is up online. By the time this episode comes out, I'm hoping we'll have alternative minimum tax in there. In the initial release, we did not include that. And as we'll talk about later in the episode, that could be very important for some specific cases. Let's go ahead to the episode. 

***

Cameron Passmore: All right, guys. Let's get going. Episode 304: Increased Capital Gains Tax. Hot topic.

Ben Felix: As we said in the introduction, the federal budget in Canada. I do want to say before we get into it, yes, this is a very Canadian content. But I think it's interesting for anybody to listen to because there's a lot of interesting decision-making concepts in here. And we've done some cool modeling. And cool modeling is always fun for anybody anywhere. 

I talked to somebody about this morning on the day that we're recording this who is not in Canada. And we were talking about other stuff. And he asked about the budget. And I started talking about it. And I realized, "You're not from Canada. You don't care about this." And he's like, "No. This is super interesting. Please keep going." Anyway, all that to say, if you're not Canadian and this does not affect you directly, you may still find the discussion interesting.

Mark McGrath: And in the US, there was a recent proposal to change capital gains on – I think they're income-testing it or at least scaling it in based on income levels. While, obviously, that's not a complete analog to what's going on in Canada, our American listeners are dealing with decisions around capital gains as well. To your point, Ben, I think some of your thought processes that you're going to discuss might be relevant in some cases. At least how to approach the decisions.

Ben Felix: Yeah. Yeah. very good point. I'm always just wary of our Global audience when we're talking about such a Canada-specific topic. But I think it's going to be interesting for anybody. Okay. Anyway. Canada's federal budget recently proposed an increase in the capital gains tax rate. And we'll talk about the way that they did that. The mechanism they used in a second. 

But what that means is that when you're selling a taxable asset, like a business or a secondary real estate property, in Canada we have a primary real estate tax exemption. If you sell your primary residents, you don't pay tax. But a secondary property you would pay taxed. Or a taxable investment portfolio. You sell that for more than you put into it. That's a capital gain. You pay tax on that. They're proposing to increase the rate on that. 

One interesting piece about this is that, in the proposed change, it would not take effect until June 25th. Any gain realized before June 25th will be taxed at the old lower rates. And so, that is what opens the door to all of the analyses that we've been doing. People have between now and then potentially because it still hasn't passed into law. But assuming it does, between now and June 23rd, if you take settlement into account, to do stuff. 

Like you said Cameron, people can make a lot of mistakes too. Because if people run out and sell their assets now because they're worried about this, one, it's not passed into law. It could just go away, which that would be a whoops. But, also, even if it does pass into law, there are a lot of cases we'll talk about where actually it would not make sense to sell an asset now and pay tax at lower rates anyway. We'll get more into that in a sec.

Mark McGrath: Not all assets can even be sold on that short of a timeline. Depending on even secondary properties, rental properties, vacation properties. That just all depends on what the market's doing.

Ben Felix: Anything can sell for the right price. If people are really worried that they might sell their cottage for way under market. 

Cameron Passmore: You see some headlines of people rushing out to sell their cottage properties. You're likely going to take a bigger haircut on the price perhaps if you have to make a market.

Ben Felix: I saw that headline. But the sources we're all realtors. I'm always skeptical about realtors. 

Mark McGrath: Exactly. Yeah. But like a business, for example, even some investments just aren't liquid. They have liquidity windows. Only quarterly redemptions or annual redemptions. The portfolios we're talking about are generally, like you said, two-day settlement. Right? We click a couple buttons and it's sold. But there are others who have illiquid property that they don't have the luxury being able to click a couple times and make that decision.

Ben Felix: Can you talk a little bit more about what a capital gain is, Mark, just before we keep going so people are on the same page? 

Mark McGrath: Yeah. And you mentioned the rates are going up. And so, the tax rates are not necessarily changing. What's changing is the amount of the capital gain that gets included in your income. Traditionally, when you have a capital gain, you buy something for X and you sell it for more than X. The difference in value between your cost and the market value or the sale value of that asset, traditionally, only half of that gain would be included in your income for tax purposes. The other half, you stick in your jeans tax-free. 

If you have a $100,000 gross capital gain, half of it, $50,000, goes on your income tax return as income and is taxed at essentially your marginal rates or effective rates. The other half is tax-free. The proposed changes with certain limitations increase the inclusion rate. Instead of including half of the capital gain in your income, you would include two-thirds of it in your income. It's still going to be taxes income at your marginal rate. But the amount of the capital gain that you include is potentially going to go up. 

You're going to talk about this I know. But for individuals, they've put a $250,000 annual threshold. Under $250,000 of annual capital gains. You can still avail yourself of the 50% inclusion rate. Basically, the old rules. It's only on the dollars above that $250,000 threshold where they're talking about increasing the inclusion. 

However, for corporations and trusts, trusts that retain capital gains income, there is no threshold. If you have a small business corporation – I was on Twitter talking to professionals and doctors last week. But for them, there's no $250,000 threshold. The proposed changes are such that, inside a corporation, if you have a corporate Investment portfolio of whatever, stocks, bonds, ETFs, every dollar of capital gains inside the corporation would be subject to this new higher inclusion rate. That's how it works. And that's the proposed changes. 

Ben Felix: Yeah. That personal versus corporate thing/trust thing is super important. Because it's – yeah, you know what? I'm not going to continue making comments on that. Maybe we can come back to that later. That's the part that gets very contentious. Who should get the $250,000 of? Anyway, we'll leave that alone for now. 

Okay. A little bit of history. And, yes, this is Canadian. But trust me, it'll still be interesting. Capital gains in Canada were not taxed at all prior to 1972. I found some really interesting historical research on this detailing historical Canadian tax rates. Since 1972, the top combined Federal and provincial capital gains tax rate for individuals in Ontario. That's just the data I was able to find. And this is accounting for the inclusion rate that Mark was talking about. This is the top tax rate multiplied by the capital gains inclusion rate in that year. 

It's been as high as 39%. That was in the 1990s. And as low as 23% in the 2000s. That means you're paying 39% of your capital gain in the ‘90s, 23% in the 2000s. This budget proposal, by increasing the inclusion rate, like Mark was talking about, from 50%, to two-thirds, to 67%, it would increase the overall top tax rate in Ontario on a capital gain to a little more than 35%. Pretty close to the highest it's ever been at the highest rate in Ontario. 

Most of that variation historically is due to changes in the inclusion rate. Not due to changes in tax rates. Similar to what we're seeing now, tax rates aren't changing. But the inclusion rate is changing. It's causes a – historically, there's quite a bit of volatility in the capital gains tax rate. And it's largely due to the inclusion rate. 

The current inclusion rate, like we've mentioned, has been 50% since 2000. It was 75% from 1990 through 1999, 66% close to what it's going to be, proposed to be now, in 1988 and '89. And then it was 50% before that since 1972 when it was initially put into place. That's where we're at now. 

The corporation piece, as we've mentioned, is really important. If I look at – instead of the highest personal rate being 35% in Ontario, I won't explain the full mechanism. It's pretty complex. And it depends on a lot of different assumptions. But if we just assume somebody owns a corporation, they have an asset inside of their corporation that they sell for a gain, a capital gain, and they immediately distribute the proceeds, the after-tax corporate proceeds to a shareholder. We've got two layers of tax here. We've got corporate tax. We've got personal tax. We're assuming that they're paying that personal tax immediately, which would not always be the case. Because in a corporation, you could realize the gain inside the corporation and not flow it out personally to pay the personal tax. 

Anyway, probably getting too deep in the weeds there on corporate tax. But the top rate under this change would be 38.6% for somebody. Call it – whatever. 39% almost. Realizing a gain in a corporation and flowing it through to a shareholder. Previously, it was about 29%. Corporations, they don't get that $250,000 exemption for the old inclusion rate. And the overall rate they're paying is a decent chunk more than an individual earning a capital gain. 

Mark McGrath: And that's in Ontario. In different provinces, the math will be slightly different.

Ben Felix: Correct. Yeah. Those are all Ontario numbers for both the corporation and the individual. A lot of individuals will probably be protected by the $250,000 limit. How many? What proportion of people? That's another very contentious point. Because in the budget documents, they claimed it's a tiny fraction of people that will be affected by this change because of that exemption. To the extent, that's true. That's great. But I my judgment is that a lot more people than were indicated by the stat in the budget document will be affected by this. 

Because like anyone that has – and I know we have biased samples because we talked to people who have money generally because that's who's interested in what we have to say. And that's who our clients are. But a lot of people have secondary properties or taxable investment portfolios with gains above $250,000. They'll touch a lot of people. I'm not saying that's a bad thing.

Mark McGrath: Yeah. Agree. Without getting political about whether this is good or bad, I think my concern was that the way that the budget was presented, what they did in order to determine how many people were going to be impacted by this or how many corporations were going to be impacted by this, they looked at a single year and they said how many corporations had a realized capital gain in this single year? And the number I think was 307,000. It was a very small number. I think there's around 1.2 small businesses registered in the country. It wasn't a huge number. 

The problem with doing it that way in my opinion is, one, 2022 was not a great year for assets, right? Stocks were down. Real estate was down. Bonds were down. Behaviorally, many people may have just not triggered gains or losses in their corporation because it was not necessarily a good year to do that. Maybe many had losses instead of gains. But, also, to your point Ben, that doesn't capture the unrealized capital gain that everybody else has on all of these assets. 

A single year's data to me isn't a good way to look at this. Because anybody who has an unrealized capital gain in a corporation is affected. Anybody with perhaps a secondary property, a vacation property, a cottage, a cabin is going to be affected. And every estate. When somebody passes away in Canada, there's a deemed disposition on all of those assets. And so, many estates are going to be captured by this as well. And none of that was clear from the way that the budget was presented.

Ben Felix: That's a big one. That when you die – on the death of a second spouse typically, because you can do a tax-free rollover on the death of the first spouse most of the time, death of the second spouse, all of your taxable assets. There's usually a deemed disposition on death. Even if someone's deferred gains for their whole life, then in the year of death, they'll tend to have a large capital gain. 

And, again, maybe that's great. Maybe that's a good thing because it'll raise tax revenue and it'll on wealth transfer. And maybe that's – I'm not saying that's a bad thing. That's just what it is. That's what'll happen.

Cameron Passmore: Yeah. We're not tax policy wonks here.

Ben Felix: Yeah. And I don't want people to get upset with us for our opinions on tax. I'm trying not to have opinions. Just saying. What's happening one interesting point that I found going through the budget supplement was that employee stock options are also affected by these proposed changes. If you have qualified employee stock options in Canada, they previously received a stock option deduction for half of the stock option benefit. And that's proposed to be decreased to 1/3 for amounts over $250,000. Very similar to capital gains. 

One interesting point on that is that the $250,000 limit to get tax at the old rates is shared by stock option income and capital gains income. I thought that was an interesting point. 

Mark McGrath: That's quite important, right? Because depending on the sector you work in, like a lot of technology companies, part of the compensation they offer their employees is stock options. Now their compensation is potentially wrapped up in the capital gains changes. And I'm not sure that was the intention. Or at least when people are thinking about the $250,000 threshold, they're thinking about assets that have appreciated in value from just sitting on them. But now we're getting into potential compensation being affected too.

Ben Felix: I agree. We work with a lot of people in technology who have stock option income. And, yeah, for sure. This will affect them on both levels. The big question, and we talked about this in the introduction, the big question everybody is wondering about is what should they do? We've got these proposed tax changes. And even though this something people have talked about as long as I've been in this business, that the capital gains rate is going to increase, it's actually been proposed now. We've never gotten this far before. We still don't know if it'll go through and be passed into law. But this is as far as we've ever – as close as we've ever come to that change happening. And we have this time limit until before June 25th to do something. People are wondering. As they should be, what they should do? 

I'll just go through a quick example. If an individual has a taxable asset worth $1.1 million with an adjusted cost base of $100,000, it's a $1 million capital gain. And, say, it's like an investment portfolio. It could be a cottage or rental property, whatever, some taxable asset. Paying the capital gains tax on that asset prior to June 25th would result in about $268,000 of tax at the top rate in Ontario. That means we're assuming there's this million-dollar capital gain and this person also has other income that pushes them to the top rate. 

Before June 25th at the old 50% inclusion, that's a $268,000 tax bill. After June 25th, the same tax year, they sell the same asset. On June 25th, I guess, they sell it. Because it's on or after. They would owe $335,000 in tax as opposed to 268. It's a big jump, for sure. But it's not obvious still. As we've alluded to a couple of times, that everyone should just be selling their assets before June. 

It does lower the tax bill today. But it also means that you have to pay that tax bill today. Not literally today. But next April when you file your taxes for 2024. If you're planning on selling an asset soon anyway, sure, sell it on June 23rd instead of June 26th. If you're planning on selling it this calendar year, say, or if you're planning on selling it in June, it's better to do it on 23rd than 26th. 

But if you were not planning on selling the asset in the near term, it's a lot less obvious that hurrying up to sell it makes sense. It can still make sense in some cases but it's just not as obvious. The reason is that deferring that tax bill into the future, even knowing that there's going to be a higher inclusion rate in the future, can still make sense because there's an opportunity cost to paying that tax bill now as opposed to deferring it far into the future. And the opportunity cost is going to be a function of your expected returns. It depends what the money's invested in or what the tax bill – the money that you pay the tax bill with would be invested in. And it's going to depend on your tax rate as well. 

This is what we've been feverishly modeling for both individuals and corporations since this news came out. And, yeah, it's been interesting. The way that we've set up our modeling is with a break-even number of years. You're better off deferring the gain rather than realizing it immediately at this number of years. I don't know if break-even is the right description. But, anyway. 

Back to the example of the million-dollar capital gain. Assuming 100% equity expected return, the break-even is seven or eight years depending on a couple of other assumptions that you can make. That means that if you're planning on holding the asset for seven years, or eight years, or whatever it is, or longer, then you would actually rather continue holding the asset and not pre-pay the tax at the current lower rate. That was an interesting finding. Do you guys have anything to add before I keep going? 

Mark McGrath: And like you said, it's going to be a function of the assumptions you use on the returns, right? And, obviously, we don't know what tax rates are going to be in the future. We don't know what inclusion rates are going to be in the future either. The trade-off is I think – and you've pointed this out in different topics before, Ben, but there's some tax certainty as well that can be considered, right? Because if you sell today, you at least know what the rates are today and what the inclusion rate is today. But if you run this modelling and it says, "Yeah, you got to hold off for seven years," there is some tax risk there too. What if the inclusion rate goes up to 100% by then? Or it could go back down. That's it. We don't know. There is a trade-off between certainty and uncertainty despite what the math says. 

But I think it's really fascinating that paying more tax later can still be better than paying less tax today. And it's just a function of those assumptions that you're going to use, right? 

Ben Felix: Yeah. It's really just the opportunity cost, which is a function of your future tax rate and your expected return, I think. So far, we've ignored AMT (alternative minimum tax). And people might be wondering what that means. A lot of people might be. Because I posted about this on Twitter and there are a few people that said, "I've been interested in tax and investing for years. And I had no idea that there was an alternative minimum tax in Canada." AMT means alternative minimum tax. 

Now in the examples that we talked through a minute ago, we assumed the highest marginal rate in Ontario, which means that the person had other sources of income, a large amount of other sources of income. And then they had this large capital gain. Usually, AMT is not going to come into play there. Where AMT is going to matter a lot is if someone has lower or no sources of other income and a large capital gain. And I'll explain why that's true in a second. 

Personal tax returns in Canada have two parallel tax calculations. They run side by side. There's the regular tax calculation and the AMT calculation. If AMT exceeds regular tax, you pay AMT. And the calculation for AMT is actually pretty simple. There's an adjusted taxable income calculation. The adjustments are – that's why I say relatively simple. Because the adjustments are a little bit complicated. Then you subtract a basic exemption. And the budget has proposed a change in that as well. We'll talk about that. And then you apply the AMT rate. 

You calculate your adjusted income. Subtract an exemption. Multiply by the AMT rate. If that number exceeds your regular federal tax bill, you pay AMT. Mechanism is really like however much AMT exceeds your federal tax bill by, the excess is AMT that gets added to your tax bill. 

Budgets 2023 and 2024 have both proposed changes to AMT. The 2023 proposals have not become law yet. The 2024 proposals are also affecting changing some of those 2023 proposals. Very confusing, honestly, in terms of what's been actually passed in a law and what hasn't.

Mark McGrath: As of today, there's been no change to AMT for quite some time. As you mentioned, in 2023 they proposed some changes. Nothing happened. The new budget makes changes to the 2023 proposals. But as of today, of recording this, on May 1st, there's no difference in AMT today versus, say, three or four years ago.

Ben Felix: Correct. The tricky thing is that these changes are proposed to happen now. If they get passed into law at the same time as the capital gains inclusion stuff that we've been talking about, it will have some pretty interesting interactions potentially. 

Okay. What were the changes? The basic exemption. Remember, you calculate your adjusted income. Subtract the exemption. Multiply by the AMT rate. The basic exemption is currently – as the current law, is $40,000. You subtract $40,000 from your adjusted income to find your AMT bill. That is proposed to increase to $173,000 and some change. That's, again, probably good for people with lower incomes. Not so good for people or lower amounts of adjusted income, I guess.

Mark McGrath: Is that exemption indexed to CPI? To inflation? 

Ben Felix: I'm not sure about that. I don't think the 40,000 is.

Mark McGrath: Just looking at the number, it seems like a flat rate. But I have to look this up. But I believe the 173 was supposed to approximate. One of the top tax brackets. Not the actual top. But maybe the second from the top tax bracket. That's where that threshold comes from. And I believe that is indexed. I could be wrong. And we didn't talk about this before the show. But just seeing the numbers, I'm curious.

Ben Felix: Yeah. Well, I think the budget said 173 in 2023. And the number I'm seeing now is 173 205. That does suggest that there's some indexing going on there. There were also changes to adjusted taxable income. That calculation for what are you actually getting charged AMT on. There's some changes that I'll talk about in a second. 

And then a big one is that the AMT rate has increased from 15% to 20.5%. Again, if you have a lower amount of adjusted income, if that exemption goes up, great. But if you exceed it and have to pay AMT, the rate has gone up. It's more penalizing. But there's also a higher threshold to actually hit AMT. 

In terms of capital gains, the reason that this is all relevant is that one of the proposals to adjust the taxable income is that capital gains would be included at 100%. Remember, for regular tax, it's currently 50% proposed to go to 67%. But for the AMT calculation, you include 100% of your capital gain income. That's a big one. 

Other stuff like deductions are reduced. Common deductions like employment expenses, childcare expenses, carrying charges, which is like interest and investment fees, those are all included at 50%. On your regular income, you can deduct those. On the AMT calculation, you can only deduct 50%. 

The donation tax credit is proposed to be included at 80%. Again, you lose some of that deduction. There's lots of funky stuff in there. You can find some pretty interesting scenarios where AMT would be relevant. But we'll just focus on capital gains because that's what we're talking about. 

If you have no other income – and, remember, earlier we used an example where somebody had some other source of a high amount of income. In this case, we're assuming no other income source. And they realized a $2 million capital gain personally before June 25th, regular taxes would be about $304,000 federal taxes. And we'll talk about the provincial side in a second. So, $304,000 of regular tax. 

The federal AMT would be about $374,000. The difference is what you'd pay as the AMT tax. You've got $304,000 of regular tax and you've got to add on $70,000 of AMT. Because the AMT calculation says the minimum tax is $374,000. That's that. 

And then there's also provincial AMT. And the way that's calculated is, generally, just a set percentage of federal AMT. For BC, for example, AMT is 33.7% of the federal AMT of the $70,000 in that previous example. Ontario drives me nuts with the surtax. Ontario's tax calculation is let – 

Cameron Passmore: Let it out, Ben. Let it out.

Ben Felix: Honestly, modeling it is just not fun. But instead of just doing a fixed percentage – there's a percentage. I think it's 33.67% for Ontario. But then they also charge surtax on the AMT. And it makes the whole calculation for Ontario tax super confusing. And then Quebec has a separate AMT calculation altogether. 

Mark McGrath: Didn't you open this by saying calculating AMT is relatively simple?

Ben Felix: Generally. For provinces.

Mark McGrath: Because this is not simple to me. I wrote an article on AMT last year or whatever when I was researching it. I was like, "This is quite –" and a lot of the difficulty comes from the things you've mentioned, which is, one, the provincial taxes are all different. In most provinces, it's actually not that difficult because it's just a percentage of the federal AMT. But more so, the deductions and how they're excluded or included in the AMT calculation. 

To actually calculate it for yourself, you'd have to see all the deductions that you've taken on your tax return and then apply different percentages to many of these deductions to calculate the AMT. As a concept, I think it's relatively simple. But to actually calculate your own AMT is not necessarily that easy. 

Cameron Passmore: Is the AMT stealing the capital gain thunder here in this episode? 

Ben Felix: It's super important.

Cameron Passmore: Yeah. Absolutely.

Ben Felix: But you'll hear why in a second why it's important, specifically the capital gain. We're not just going off on an AMT tangent here. This comes back to capital gains.

Cameron Passmore: That's my point. It's very rare that you dig into details on AMT like this.

Ben Felix: Yeah. I didn't put this in my Twitter thread. But I almost did. And I end up taking it out because I didn't like it. But I wrote that AMT is having a moment. In this specific case right now, AMT is super relevant. Usually, it's whatever. Somewhat obscure. But because of there's this incentive to realize capital gains before June 25th and because of proposed changes to AMT for the next couple of months, whatever it is, not even, is going to be super important for people to understand. 

Cameron Passmore: You see in that Twitter post, it was too click-baity. 

Ben Felix: I don't know. I just I didn't love it. 

Mark McGrath: I loved it. When you sent me the thread before you posted it, that was my favourite part of the thread. I'm upset you took it out. But whatever. 

Ben Felix: Oh, I shouldn't have taken it out. I reread that thread so many times. It's one of those ones where I spent more time on it than I got engagement. Sometimes you write like a useless tweet and it gets so much engagement. And then you spend hours researching with something and nobody cares. That's how it goes. 

Okay. For provincial AMT. In our example with the $2 million, we've got $70,000 of federal AMT. The provincial amount is going to correspond to that somewhat. Just a couple of examples. In Alberta, that would end up being 24,500 roughly on 70,000. 70,000 of federal AMT equals 24,500 of Alberta AMT. BC would be 23,500 roughly. Newfoundland, 40,500. And Ontario 37,000 including the regular AMT plus the surtax on AMT. It really starts to add up.

Mark McGrath: That's a huge difference though.

Ben Felix: Between the provincial AMTs? 

Mark McGrath: Newfoundland compared to BC is almost double in this example.

Ben Felix: Yeah. Newfoundland is one of the highest ones. That's why I put it in there as I think it is the highest. That's why I have it in my examples. BC might be the lowest. I can't remember. I have them all written down. But, anyway, those differences matter a ton. And I'll come back to that in a second. 

But in any case, we're at like $100,000. Maybe a little below or a bit above $100,000 of AMT. That's additional minimum tax that you're paying on your tax bill. On that $2 million capital gain, regular federal and provincial taxes would be about $493,000. That's in Ontario. Sorry. And then if we take AMT in Ontario, that's another $107,000. Someone planning to realize a capital gain, $2 million capital, gain and assuming a $493,000 tax bill, that would be a big whoops to realize, "Oh, there's another $117,000 of taxes." It would be quite a nasty surprise. 

One important detail about AMT is that it can be recovered. You can carry forward AMT for up to 7 years. And you can use it to offset regular income that exceeds – regular taxes that exceed AMT. If you have AMT in future years, you can't carry forward your AMT. It just keeps building up. But if you have regular taxes above AMT in future years, you can soak up your AMT carry forward using those taxes. 

If you have a regular tax bill in a future year, you can carry forward some of that AMT to reduce the taxes that you have owing. You can go back and mop up. It's effectively a prepayment of taxes in that case where you're actually able to go up and recover it. But there are a bunch of cases where it's not recoverable. In which case, it's not a prepayment of tax. It's just a straight-up extra tax. 

Those cases where it's not recoverable become super important, again, in this specific time period where AMT is going to be very relevant to capital gains. One case is if there are no future years with high income within seven years. If you have a $2 million capital gain now and no expectation of higher income years in the future, because, remember, in our $2 million capital gain example, there's no other income sources in that year, there's a good chance you won't recover all of your AMT. If you're invested in a portfolio of stocks and bonds that's earning some income, at least based on my modelling, you'll recover some of your AMT. But probably not all of it. Unless you have other sources of income. That's one. And if it's a cottage, if it's not an income-producing asset that you're selling, then that wouldn't generate income like a portfolio would. That would be even worse in that case. That's a loss of AMT. 

Another one is provinces. Mark, you mentioned earlier there's a big difference between some of the provinces. Provincial AMT is recovered again as a proportion of federal AMT but based on your current province of residence. If you have AMT in a high-rate province and then move to a low-rate province when you recover it, you lose that difference between the two provincial AMTs. 

Now the same is true. You could do some fun planning with this too. It's true in the other direction as well. If you have AMT in a low-rate province and then go recover it in a high-rate province, there's a positive delta there.

Mark McGrath: You got to move from BC to Newfoundland to get your taxes back and then move back if you so choose.

Ben Felix: If the AMT numbers are big enough if it's a huge gain, maybe somebody would do it. I don't know. 

Mark McGrath: People leave the country over taxes. Switching provinces isn't a big deal in the grand scheme of things, right? 

Ben Felix: Yes. That's actually another point on AMT, is if you have AMT and then leave Canada, that's it because you're not going to have any future regular taxes in Canada to mop up the AMT. 

Another one is Quebec. If you have AMT outside of Quebec and then move into Quebec, because they have a completely separate provincial AMT calculation, you lose your provincial carry forward in that case. These are all just points where I think it highlights why it's going to be important for people understand AMT if they're going to be thinking about realizing large capital gains this year. Because it ties into all your other plans. Where do you live now? Where do you expect to be living in the future? 

I talked to somebody recently who has a large capital gain in Canada and they wanted to know about this. Should I realize the capital gain? But they're planning on moving to a different country permanently in 2025. In that case, they have a low income this year. So they would pay the AMT. But then they'd be gone. That's it. They're effectively just paying capital gains tax at a much higher rate if they do that.

Mark McGrath: That would be true on what we call exit tax as well. When you become a non-resident of Canada for tax purposes, you are deemed to have disposed of your assets for tax purposes. If you have a large capital gain and you are becoming a non-resident, the act of leaving can trigger the capital gain. But now you have no way of recovering it. Exit tax in theory would be a lot higher because you can't recover the AMT if you're leaving.

Ben Felix: Yeah. It's a really interesting point. I think that I don't know why it would be different on exit tax. But assuming that is correct, that is a very good point for anyone saying, "I'm out of here. Canada's increased the gains. I'm leaving." 

We talked about the break-even numbers earlier is, whatever, seven or eight years that we found in that example as a break-even. The AMT – I won't throw a number out there because it varies a ton based on the assumptions. But AMT really changes this math, especially if it's someone who has low other sources of income. In the example we've been talking about with the $2 million gain and no other sources of income, because they won't mop up that AMT, it really messes up the breakeven calculation to the point where it's like it's pretty unlikely you'd actually want to sell the asset. 

Mark McGrath: And, sorry. To be clear, Ben, all of this math that you've just walked us through is before any of the budget changes. It's using the 50% inclusion rate on capital gains as well as the current AMT rules. 

Ben Felix: Yeah. Once the gains inclusion rate or if the gains inclusion rate increases to two-thirds as is proposed, the AMT on capital gains specifically – you could still make AMT appear. But like in this example for the $2 million example, AMT is lower than regular taxes at a two-thirds inclusion rate. That's why, again, AMT is having a moment. It's this specific set of circumstances right now that make AMT particularly important. 

Cameron Passmore: The lower your income, the less concerned you are, in general, with the proposed tax changes. 

Ben Felix: Yeah. In general, that's true, especially if you're not going to realize capital gains. 

Cameron Passmore: No. If you're realizing a big capital gain because of the AMT calculation. 

Ben Felix: If your income is lower, you'll still pay less tax overall if you have a lower income. But that's when AMT will be triggered. If you have low other sources of income and a large capital gain, that's when your AMT tax is going to exceed your regular tax. If you have a higher income, your regular tax is going to be higher overall. AMT is not going to be an issue.

Mark McGrath: Let's say this gets implemented, the budget, and you do sell all these assets today, the AMT calculation that you would actually use for the 2024 tax year, do you know if it would be the new AMT rules or the old ones? Because you're triggering the gain prior to the AMT taking effect. But the AMT calculation would be done when you go to do your taxes the following years. I don't know if you know the answer. It just occurred to me that I don't know if they're going to use the new AMT calculation for gains that are triggered before June 25th.

Ben Felix: That, I do not know the answer to. I mean, there's a lot of this stuff where I'm unsure if that's something that I don't know or if it's something that nobody knows yet. I don't know.

Mark McGrath: I'm just wondering if the higher exemption under the new AMT there. You're getting capital gains under the old inclusion rate. But, potentially, AMT calculations on the new AMT rate with a higher exemption. 

Ben Felix: My examples were based on the proposed AMT rules with 173 205 exemption. And the higher rate on the net AMT income. 

Mark McGrath: Just so I'm crystal clear, you're using the 50% inclusion rate today on this capital gain example. But you're using the new proposed AMT rules. Is that right?

Ben Felix: Yeah. Correct. If the budget proposes this new capital gains rate but after June 25th. And then it proposes the new AMT for the tax year 2024. I think looking at it this way does make sense. Happy to be corrected on that of someone with more tax expertise thinks otherwise. 

Keeping in mind how useful deferral can be even given these rate increases. I think it's important to remember that for long-term investors, realizing large capital gains is not something that you're doing every year. If you're not going to realize a gain within, whatever, seven years, then you probably don't want to realize it now. 

Most long-term investors shouldn't be realizing gains, all their gains in such a short period of time. Even someone who's retired, living off of their portfolio. Maybe they could realize enough gains for the next three years of income, or something, or five years of income. But not the whole portfolio. Because even retirees are not triggering all of their taxable gains in a single year to fund their retirement consumption. They're triggering bits and pieces. Or none if they're living off of just the distributions from the portfolio.

Mark McGrath: That's a really interesting point though, Ben. Sorry to interrupt you. Because I had this conversation with a client the other day. And they do have a large capital gain inside their corporation. And they are basically, essentially retired. To your point, it might not make sense to rip the band-aid off the entire capital gain. But because they are generating some capital gains every year inside their corporation to fund their retirement lifestyle, do they then take some number, say 3 to 5 years’ worth of capital gains? Within your 7-year break-even threshold, just for the example, trigger them all at once. It's a bit of a hedge, I guess.

Ben Felix: Corporations are different. And we didn't go into that because we'll cover that on a special Money Scope episode that Mark Soth and I will do. But corporations are different. When you realize a gain in a corporation, it creates something called capital dividend account, which can be paid out to a shareholder tax-free. 

And if someone's living off of their corporation, it means that they're taking taxable dividends out. There's an interesting planning opportunity corporations where you may want to realize all of your gains to create CDA. It depends on what the numbers look like. But that lets you stop taking taxable dividends out of the corporation for some number of years and live off of tax-free capital dividends. The break-even math on a corporation for someone who's spending dividends out of their corporation is quite a bit different. Because you give up on tax deferral on the capital gain. But you can get a lot of that back by gaining tax deferral on not having to take taxable dividends out personally. It's quite a bit different. But, again, that's a Money Scope topic. 

Cameron Passmore: It'd be a popular one.

Ben Felix: Within the group of 400 people that are interested in this stuff. 

Cameron Passmore: I know. But if you're interested, that's the place to go. 

Ben Felix: Mark mentioned tax rate risk earlier. I think this really highlights that's a real thing. We've talked about that on past episodes. Hey, tax rates can change. A change to the capital gains inclusion rate is a big shock to that tax. It's just a big one-time jump to taxes on assets. 

We try to do stuff to mitigate this. We had Scott Cedarburg on a while ago talking about how you can optimize RSP and TFSA. Although, he was talking with the American equivalence. Contributions based on hedging future tax rate on certainty. We don't tend to do that because our clients tend to be in a position to max everything out. But we do do other stuff. Like if someone has a low-income year, realizing some capital gains to mop up their low-income brackets and increase their adjusted cost base. That does two things. It reduces tax rate risk, which is what we're potentially seeing now. It also helps to lower the terminal tax bill. There's a little bit of lifetime tax smoothing by doing stuff like that. 

And, also, for people with corporations, again, we'll typically recommend taking some money out of the corporation at least to fund RSPs, TFSAs and, RESPs. Again, those are just registered savings accounts with tax-preferred treatment in Canada. I think that idea of tax diversification. I know you're big on this too, Mark. Just having money in different buckets with different types of tax treatment really does protect you against stuff like what we're seeing right now.

Mark McGrath: You end up with a concentration risk. In reality, many people were organizing their affairs this way for decades where they were using their corporation as a retirement account. And there's nothing wrong with that. It's part of the rules. And maybe they were funding some RSPs and TFSAs. But maybe not. And I know clients who had done this where they had used their corporation as their primary retirement savings vehicle. They paid themselves only dividends so that they wouldn't have to pay into the Canadian pension plan. And the corporation has now a massive amount of concentration risk from a tax perspective, right? 

And to your point, tax diversification by using tax-free savings accounts. Paying a salary to get Canadian pension plan and RSP room, filling up those RSPs, it insulates you from some of these adverse tax changes like the one we're seeing right now. 

And I have to say, I had an accountant that I work with who I talked with like maybe last year about this. And I was telling him how I'm big on tax diversification. And he was like, "No. No. Stuff everything in the holding company." And the day after the budget, he emailed me, he's like, "You were right. I can't believe it. But you were right." And this isn't to say I was right. But this is the exact type of risk we're trying to defend against by using up all these other registered accounts. And so, there are people, unfortunately, that are going to be disproportionately affected because they didn't take advantage of that in the past.

Ben Felix: Yep. Exactly. And you can't do it all in one year. Because to take money out of the corporation, typically, you got to pay personal tax, which means if you bled money out of the corporation over time at lower tax rates, great. Now you don't have that concentration risk. But if you decide, in this year, I've got $500,000 I want to take out my corporation, you're going to pay half or more of it in tax. 

And that's another thing on the corporate planning stuff. There are even potentially cases where we would recommend taking money out personally even if there is no registered account room available to invest in a personal taxable account. Doesn't always make sense. But it can make sense in some cases. And, again, it gives you that tax diversification.

Mark McGrath: There's two other I think interesting proposals in the budget that are just worth maybe touching on at a high level. One is the lifetime capital gains exemption. For business owners selling a business, it has to qualify if there's a number of different restrictions to access the lifetime capital gains exemption. But for those that qualify, the first $1.25 million of gross capital gains would in theory be exempt if you sell the shares of the business and you qualify for that exemption. 

The previous limit was I think just over a million dollars. It was indexed to inflation. And I believe it just crossed a million dollars this year. The new proposal bumps it up to 1,250,000. It will not be indexed in 2025. And then indexing will resume in 2026. There are cases when those selling a business decide, depending on the size of the business, may benefit from that extra rate. 

And then the last one was the entrepreneurs' incentive, which is interesting. This is a brand-new proposal. It's not a modification of anything else. And what that does is, up and above that lifetime capital gains exemption of $1.25 million over the next 10 years, they're proposing to phase this in at $200,000 per year. Until after 10 years, there's a new $2 million exemption limit above the lifetime capital gains exemption. 

And within that $2 million band, if you sell a business, the capital gain's inclusion rate instead of being two-thirds will be one-third. If you sold your business for $3.25 million 10 years from now and it qualified, the first $1.25 million would be tax-exempt. The next $2 million would be subject to a one-third inclusion rate instead of two-thirds. There is some benefit in those cases. But they excluded a ton of sectors from those that are eligible for that benefit. 

Financial companies, insurance companies, real estate companies, food and accommodation, many service businesses, and any professional corporation. None of those benefit. If you eliminate all that, I think what you're looking at is a lot of technology companies or small startups and that type of thing that could benefit from it. It's an interesting proposed change. Though it has some tax planning implications as well. 

Cameron Passmore: As we pivot to the after-show, I have to ask you guys, when the budget came out a couple of weeks ago, there was so much activity in various parts of the media. Newspapers reached out to you and other outlets reached out. You went to Twitter right away with lots of threads. Created the tool. Just tell me where your head was at once it came out. And what's your default go-to activity? 

Mark McGrath: I wrote a thread that evening. The budget proposal came out at, I want to say, 4pm on the Tuesday I think it was. And as we were chatting about it, Ben, and I, and some other adviser and planner friends that we have outside of PWL. And so, we were all trying to wrap our head around these changes. 

And for me, again, my bias being having worked with many physicians, the corporate capital gains issue for me was the biggest issue that I could see from my own experience. 

Cameron Passmore: And you saw that right away. It didn't take a while to seminate through Twitter-verse.

Mark McGrath: I saw it right away just because of the language they used. It was very clear that they said, “Capital gains above $250,000 for individuals and all capital gains in a corporation or a trust.” And I like reread that line 10, 15 times to make sure that I wasn't missing some language there. After realizing this is going to impact a lot of people that I don't think realize they are going to be impacted, I decided to write a thread and just walk through the math of it. Here's the old rules. Here's the new rules. Make some assumptions around a capital gain inside your corporation. And you're paying this out to yourself. What is the change in taxes that you're going to pay? And in the example, you're basically paying a third more in taxes at the end of it for somebody who's taking capital gains in a corporation and then paying themselves out the gains as dividends. 

I wrote the thread and I scheduled it for the next morning, I think around 9am my time in BC, and it got a lot of attention. And it got a lot of attention from Physicians. I know the previous head of the Canadian Medical Association, he retweeted that. Obviously, some journalists picked it up. It was just a frenzy. And what I realized is a lot of people, A, don't know how capital gains work in the first place. There's a lot of confusion about that.

Cameron Passmore: Really? 

Mark McGrath: Yeah. I was having conversations with people that didn't understand how capital gains worked in the first place. Many thought that business owners could just choose to pay themselves in capital gains instead of salary and dividends. And so, they were happy with this tax change because they felt that it made business owners' incomes closer to a regular salaried person's income. Because they thought that people who had a business could just choose to pay themselves in capital gains instead. There were ways to potentially do this in some cases. But that wasn't the point. 

My point here is that the spectrum of understanding of taxes is very wide in the first place. And then when you get into these tax changes, and then when you get into the changes specifically for how it's going to affect incorporated business owners who have an unrealized capital gain, it gets into some really niche stuff. It became clear to me that some people just didn't want to understand that and they just wanted to say good tax the rich kind of thing. 

And so, there came a point for me where I had to just start ignoring comments on Twitter. I got direct messages with some really nasty comments and insults. And I'd never experienced that type of vitriol on the internet before. I had to take a break.

Ben Felix: Yeah. It got pretty intense. 

Mark McGrath: It was intense. 

Cameron Passmore: Wow. And, Ben, with the tool, you and Braden met up and started brainstorming this? 

Ben Felix: My reaction was to start modelling it, first thing I did. 

Cameron Passmore: You do. 

Ben Felix: And then Braden messaged me that he wanted to build an app. And I was like, "Great. I've already started modelling it." I shared what I'd done. And then he turned it into a web app, which was pretty cool. 

He was off this past week, which was somewhat unfortunate because I wanted him to keep modelling with me. But we are able to get this app up before he left, which was awesome. And then he's back next week or this week when this episode comes out and we will have done a few modifications to the first iteration of the model. And we'll likely release one for corporations as well. It's a very slick tool. And people seem to appreciate it.

Cameron Passmore: As you said earlier, brought up in the Money Scope with our good friend, Alini doc. 

Ben Felix: Yeah. Mark Soth's reaction was similar to mine. He's been also feverishly modelling stuff. I think both of us have slogged many hours in Excel over the last couple of weeks. We'll do a special Money Scope episode once we both have our heads straight in terms of what people should do. That'll be coming at some point.

Cameron Passmore: And if anyone is even remotely interested in this topic, the Money Scope, I know I say this every other week when we're on here, is fantastic. Deep-dive quality conversation. And you give it the oxygen and time these topics deserve. And it's so well done. And Dr. Mark is so great with you, of course.

Ben Felix: They seem to be appreciating the Money Scope, which is good. It was quite a venture when Mark and I started it. Because we were putting tons of time into it and hadn't released an episode yet. And we kept saying to each other, "Man, I hope people like this." But they seem to like it so far. That's good.

Cameron Passmore: You want to jump into the reviews?

Mark McGrath: Yeah. This one's from Guplets50 in Australia, "Addictive and informative. Terribly addictive podcast, the fantastic mix of topics, guests, and breadth of discussion. Not only very useful for beginners, but even for people who have an above average background in finance and personal finance. Canadian investing topics are great because it allows me to immediately compare and contrast with my Australian situation. I have used your work to set our goals, find a financial advisor and to invest in DFA, dimensional funds. If you were in Australia, I would be a client. Keep up the good work." 

Should we move to Australia? Should we open an Australian Branch? 

Ben Felix: It's not a bad idea. That review makes me feel better about our pretty hardcore Canadian episode today. 

Cameron Passmore: I've heard from a bunch of people on LinkedIn, from Christian, who is a fellow Canadian adviser, "Hi, Cameron. Your post popped up in my feed that link to a very useful capital gains calculator your firm created. Just a quick note to thank you and the team for putting together so promptly. Nice to have a tool that advisors and clients can engage with, especially when you're helping them to make seemingly complex decisions. Really enjoy your podcast as well. Cheers." Thanks for that, Christian. 

Also from Leno, "Hope you, Ben, and the PWL team and, of course, you, Mark, the podcast continues to be absolutely amazing. I genuinely can't describe the impact they have had on my financial journey. Further to our conversations above since we last spoke, I moved from a boutique firm to a wealth management advising role at a bank in Australia." We're popular down under. And then I just got one today from Nater in Toronto. He wanted to let us know that he is a huge, longtime fan of the podcast. And also thanks us for educating Canadians. 

Ben, you want to do your best at this email? I tried to shorten it a bit.

Ben Felix: Yeah. It's a lot of text. “Following the 300-episode milestone, I would like to share with you some thoughts as a longtime listener. I started listening to your podcast sometime in 2019 before for was replaced with from two —” Remember that? We used to say for Canadians. And then we had too many International listeners. And they were like, "Can you change the introduction? Because it's going to scare off other international listeners." Then we changed it to from two Canadians. And now it's from three Canadians.

“And well before the dedicated theme music” – oh, yeah, the new music. Oh, man. The history of the podcast. 

Mark McGrath: Taking you back, hey? 

Ben Felix: “Boy, have you come a long way.” Is that a compliment or an insult? A little bit of both? I'm just joking. “Your podcast has helped me a great deal in shaping my own personal investment philosophy. The weekly reminders continue to provide useful, sometimes necessary oversight to stay the course in the face of challenges. To me, the podcast is a treasure of invaluable investing knowledge and a bastion of critical financial thinking in a world where reason and common sense rarely prevail. Your podcast shines a reassuring light through the noise and helps bring focus to long-term goals. 

Although I'm lucky enough to consider myself mathematically and financially savvy, I can say that sensible investing requires some degree of mindful steadfastness. There is no shortage of temptations or biases. And staying true to one's investment plan can at times time be hard work even for the pros. 

It is no surprise therefore that there are swaths of like-minded people who find the podcast as valuable as I do. I would like to express my heartfelt gratitude for the work you're doing and for providing the service free of charge making it accessible to anyone with a smartphone. Having followed your journey for half a decade – oh, crazy. I am thrilled to see you go from strength to strength and grateful for everything I have learned. Keep up the good work.” Very nice. 

Cameron Passmore: We're coming up in six years this summer. 

Ben Felix: Crazy. 

Mark McGrath: That's wild, hey? 

Cameron Passmore: Mark, you want to quickly go through this next one, which has been shortened? 

Mark McGrath: “Hi, Ben, Mark, and Cameron. Thanks for your excellent work on bringing so many interesting personal finance topics on your podcast and YouTube for the benefit of everyone. You are doing really good service. I am an Italian working in Singapore and listen to your podcast every weekend. 

In your latest episode 299, you bring such a good summary of years of experience and study on investing. I like the multi-disciplinary approach you follow when discussing investing topics and improve your understanding of investing. Personal finance, behavioural finance, decision-making, psychology, and even philosophy. That is evident from the hosts.” I think they meant guests. “That's evident from the hosts you bring to the podcast. In this sense, you really nailed it. And I like when you summarize on the most sensible, broad-based advice that can help us investors in navigating personal finance.” That's from Marco in Singapore. 

Cameron Passmore: Cool. Now, the Mike Green episode. Wild engagement on that. 

Ben Felix: Listen, Mike is controversial because he has a theory. And he's very assertive about promoting his theory. I thought it was interesting to learn about. I saw some people say that they wish that we'd pushed back on Mike more. But I've said this before. People say that when they personally disagree with Mike and they want us to express their opinions to Mike, I don't know if I have enough information to agree or disagree with Mike. 

Either way, I don't think that what Mike is saying is factually true. It's a theory. And I definitely want to do more investigating. But we are having – I've talked to Ralph Koijen about this. And I'll hopefully talk to him again we've got Valentine Haddad, who Mike references coming up on the podcast. We'll be able to ask him about his research and how he thinks about Mike's ideas. 

We've also got Antoinette Schoar, who's written – co-author of another paper that Mike often references on this stuff. She's coming up later this year as well. Super interesting. But my mind's not made up. And there's more thinking and investigating to do on this topic. Yeah, very lively discussion. If people want to see a lively discussion about very geeky topics, there's one happening ongoing in the Rational Reminder Community on this.

Mark McGrath: I went into watching that episode with a pretty heavy bias. Because Mike blocked me on Twitter a long time ago. And I've never interacted with him. Never and I just went to somebody like "tweeted" one of his tweets to me and I was like, "I can't see this. Who is this guy?" And I looked and I was blocked. I, of course, knew who he was. But I was like I've never engaged with him. Why did he block me? I think it's just because I talk about index funds so much, he's just like, "This clown," and just blocked me like without even interacting with me. 

I went into that episode going, "Okay, this guy who doesn't like me. I'm going to go watch this episode." And I have to admit, it was a really fascinating episode. He's clearly brilliant. I had to slow it down and go back and watch a couple of segments a couple of times. Because his level of knowledge just far exceeds my own. But it was a really good episode. Very eye-opening. It's not a perspective that I had considered before. Very good.

Ben Felix: I didn't get it before. I had made two videos because people would send me Mike Green, what do you think about index funds breaking the market, whatever? I made two videos about market efficiency and whether index funds are breaking market efficiency. And Mike saw one of those videos and that's what led to him coming on for an episode is he got super upset about my video. Wrote a whole post about it on his Substack, which was unnecessarily mean. But, anyway, I read that post and sent a message. I'm like, "Listen, Mike. If you have such a strong opinion, why don't you come tell us about it?" 

And then in preparing for it, I actually went and read his stuff and understood that he was not in fact talking about market efficiency at all, which then helped me understand why he was so upset. Because I think everyone dismisses him for the same reason. And it's not even what he's talking about. Anyway, end-to-end interesting experience. I think I enjoyed it. 

Cool thing just happened while we were talking here, while we've been recording. The Wealthy Barber, David Chilton, who in Canada is a very well-known figure in personal finance, he wrote a popular book, like the book.

Cameron Passmore: Way beyond Canada. He's huge in the US too.

Ben Felix: I didn't actually even realize that. I knew he was very famous in Canada.

Cameron Passmore: I think he was back in the day one of the leading fundraisers for PBS, if I'm not mistaken. He was very popular in the US.

Ben Felix: Yeah. Okay. Didn't know that. David Chilton, The Wealthy Barber. That sounds like more people than I expected will know who he is. I got a notification on my phone as we were sitting here on my YouTube channel on The Most Important Lessons in Investing video that listeners may have seen or they at least us talk about that topic on Rational Reminder. He commented, "Hey, Ben. It's Dave Chilton, The Wealthy Barber." Yes, Dave. I know who you are. "I enjoy your videos and podcasts, especially this one. You're well-informed and very genuine. It's clear you really want to help people. Well done." 

Mark McGrath: High praise. 

Cameron Passmore: I saw some tweets today that he has a new service coming out to help people. 

Mark McGrath: I just saw the headline. I didn't see what the service is all about.

Cameron Passmore: I just saw the headline as well and looked into it. Just came through. We invited him on and he was unable to join us.

Ben Felix: I'm going to reply his YouTube comment and tell him to DM me on Twitter. And we'll see where that goes. 

Mark McGrath: Nice.

Cameron Passmore: I had a few people asking about meetups. Hopefully, this fall, we can get you to town, Mark. Because I think there's a good chance that our very good friend and soon to be your co-author, I guess, Dan Solin, will be in town.

Ben Felix: Why would Mark come here? Why don't we go to BC? 

Cameron Passmore: That's actually not a bad idea. But Dan may be coming to Ottawa. That's all. That's a chance. It'd be cool to do it. But no reason why we can't go to BC anyways. We've never had a BC meetup. That's actually a very good idea.

Ben Felix: Why wouldn't Dan want to go to BC also? 

Cameron Passmore: That's also a very good question. We could pull that to him. Anyways, in the fall, somewhere in Canada, we're hoping to have a meet-up with us and – 

Ben Felix: Somewhere in Canada. 

Cameron Passmore: We'll pin that down.

Ben Felix: One end or the other. One side or the other. Somewhere in the country, we'll be there.

Cameron Passmore: Today we're recording this, May 1st. How's the book coming?

Mark McGrath: Yeah. Good. I'm about, I'd say, a quarter of the way through. The book itself – and I'm just measuring that by chapter count. The book itself has about ballpark 40 chapters. And I finished off chapter 10 yesterday. It's really interesting. Because as you guys know, Dan is a huge proponent of an evidence-based approach to everything. And so, his book has I don't know how many hundreds of references to surveys, and studies, and everything else. And he basically never makes a point unless he can back it up with some kind of reference and study, which is awesome. 

The problem I'm finding is that there aren't necessarily analogues to a lot of these studies in Canada. The US just has such incredible data. Things like – just yesterday, I was writing a chapter on debt and spending specifically for millennials. And the points he's making in some cases having difficulty finding a correlation in Canada that can back it up. A lot of the time being spent on the book is really just looking to see if I can actually find analogous data for what he's saying in the US to see if it exists in Canada. 

It's great. I'm enjoying the process. Dan's a great writer. I think the book's going to be quite popular. And I'm really hoping to get it written, at least the first draft, by the end of this month. It's now May 1st. 

Cameron Passmore: Love it. Speaking of evidence-based, we have an upcoming webinar on May 22nd at noon Eastern time, Compensation Strategies for Canadian Business Owners. We've done a bunch of webinars in the past. This one will be co-hosted by our colleague, Brady Plunkett, who's a portfolio manager here at PWL. And, also, Spencer Brooks, who's a partner at Henrdy Warren, which is an Ottawa-based tax and accounting firm for presentation on an evidence-based approach to business owner compensation techniques. We'll have the link in the show notes to register for that. That's May 22nd at noon. 

Ben Felix: those guys are phenomenal. All three of them. Brady's great. Spencer and Jacob at Hendry Warren, they helped us on one of the Money Scope episodes on this same topic on corporate compensation strategies because Mark Soth and I, we were looking at each other, we know enough about this stuff to say what we're saying. But, we should probably have someone check it because this is really, really complicated. 

And so, Spencer and Jacob, they both contributed to reviewing that episode and their input was just incredible. The little stuff they pick up, "This is technically correct. But it would be more technically correct to say this." Mark and I were just like," Man, this is crazy." But those guys are super knowledgeable on tax. 

Cameron Passmore: Insanely good firm. As always, connect with us all over the place, Twitter, LinkedIn. Easy to reach. Easy to connect with. Please leave a review. Any final thoughts? 

Ben Felix: No. I'd love to see some more reviews. Total number of views is getting pretty high. I like watching that number go up. 

Cameron Passmore: Closing in on 1,200, I believe? 

Ben Felix: Yeah. If you're enjoying the show, leave us a review. Or if you're not, we've had some – have we ever had bad reviews? Maybe a couple. 

Cameron Passmore: A couple in there.

Ben Felix: We'll take anything we can get. 

Cameron Passmore: As always, thanks for listening. 

Mark McGrath: See you next time. 

Ben Felix: See you.

Is there an error in the transcript? Let us know! Email us at info@rationalreminder.ca. 

Be sure to add the episode number for reference.