# The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents

“Composition over inheritance” has always been a good engineering rule. It may also be the unlock for useful AI. A Gmail agent is fundamentally more powerful than a Gmail skill — and when composed with Sheets, Notion, and GitHub agents, the system gets more capable, more reliable, and cheaper to run

Okay, so I'm going to be talking about domain-specific agents and why I really think that they are going to play an unbelievably important role in the future of AI and in the future of how we build agents. To get started real quick, my name's Justin Schrader. Uh you can find me on X at JP Schrader. And um I work at a small company called Standard Agents, which nobody's heard of right now cuz we're still kind of in stealth mode. Um after this talk, if you're interested, feel free to reach out to me and uh I can let you know a little bit more. [00:00:02 → 00:00:39]

Mostly, I'm known for doing a lot of different open-source projects. Uh Dmux, which is a great multiplexer for all of your coding agents. Uh ArrowJS, which is sort of like a UI framework, sort of like React for um the agentic era. A bunch more that I won't get into, but you know, maybe check them out if you're interested. Okay. [00:00:37 → 00:00:59]

I think we can all agree that the moment in time that we are in is very similar to the Industrial Revolution. Um in fact, it might be like an accelerated Industrial Revolution. Maybe it's a bigger deal, but it's certainly not smaller. I probably don't need to convince you of that if you're listening to one of these talks. Um but that is the moment we find us find ourselves in. [00:00:57 → 00:01:18]

So, I actually think it's helpful to go back and sort of look at what was the key catalyst of the Industrial Revolution. And ultimately, it was that we learned how to harness energy with machines. We learned how to harness energy with machines. And what's interesting is that in this next era, we are essentially learning to harness intelligence with agents. And agents, I think, can be thought of a little bit like the machine of yesteryear. [00:01:17 → 00:01:47]

It's the thing that is going to use the intelligence. Not so much us, but the agents. What's interesting about that is I bet if I was in an actual room with you guys and and we all put up our hands, I bet a lot of you when I say what is an agent instantly have examples that pop into mind, but also probably can't pull out a definition immediately. Some of you maybe can, um but the reality is that we haven't even coalesced on a definition of what an agent is, even though we're well into the agentic era at this point. And I think that's kind of interesting. [00:01:47 → 00:02:27]

Um here's my definition. You can feel free to agree with it or not, but agents are deterministic software that harness the non-deterministic results produced by models in pursuit of some desired objective. Now, deterministic software might make you think more like a harness, and I actually think the distinction between an agent and a harness is really pedantic, not very helpful, um and for the most part, in most cases, you can just conflate the two. A harness is an agent and an agent is a harness, okay? And for the for the purposes of this talk, we're going to go ahead and just move forward with that. [00:02:25 → 00:03:04]

I think you could probably make some good arguments for why one is the other and vice versa, but really not important right now. Now, if you did have some examples pop to mind, they might have been like Claude or Codex, um you know, OpenClaude, Hermes. But you know what's interesting is I bet if you went out onto, you know, the the streets of corporate America in any city, maybe not San Francisco, but any city in America, and you asked somebody just in an office building, could you name an agent by name? I think some people are going to get Claude. Some people might get Codex. [00:03:04 → 00:03:46]

And that's about it. I don't think hardly anybody's going to be getting OpenClaude or Hermes. Uh Uh, and and really even Claude, I don't know that people would even know that that's an agent. These things are not well understood. And yet, what's so crazy is everybody is building agents. [00:03:45 → 00:04:04]

I have a real estate agency down the street that's building agents. I know in like independent private insurance brokers building their own agents. I know Fortune 500 companies, lots of them, building their own custom agents. Everybody is trying to build their own custom agents. And I know people don't believe me, uh, but go talk to them. [00:04:04 → 00:04:26]

Just go talk to people. They are trying to build custom agents. And I can't help but wonder why. Nobody seems to be asking this question, why? There's already AI everywhere. [00:04:26 → 00:04:38]

You can get on ChatGPT all the way down to some open-source model from China on some, you know, rickety website. There's everything in between, but still people want to build custom agents. And ultimately, it comes down to integration. Businesses want their data properly integrated into AI. They They believe, and are probably right, that if they appropriately leverage AI, they're going to have these dramatic gains in their business and so on and so forth. [00:04:38 → 00:05:06]

So, they need to figure out how to get integrated. And building their own custom agents is obviously a way to do that. And it's one of the first ways that they discover, um, as a mechanism for doing it. The problem, though, is that agents are really hard. You have to take very, very careful care of the agentic loop and make sure that it's properly orchestrated. [00:05:04 → 00:05:28]

There are a ton of different provider abstractions you need to think about. Um, fortunately, there's some good tools coming out around that, you know, like the the Vercel AI SDK is great. Um, durable execution, you need to make sure if there's faults, we can pick back up. These are relatively hard problems, um, especially if you're thinking about it at scale. And the reality is there's just tons more. [00:05:28 → 00:05:50]

There's all kinds of validations and stop conditions and so on and so forth. And so what often happens is people do try to build their own custom agents, and they sort of work as a demo, but but not much more than that. Um, and really it turns out that it's an absolute nightmare for people. Um, building robust agents is just hard. And if you go talk to anybody in an IT department, they are pulling their hair out because there are so many different concerns. [00:05:50 → 00:06:20]

Um, there's no defined way to build an agent right now. Like, actually no defined way. The closest thing maybe is, uh, Eve that just came out from Vercel is maybe like the closest thing. Um, but in reality, everybody's kind of coming up with their own way to do it. Um, telemetry and observability on these agents is unbelievably hard, especially at scale. [00:06:18 → 00:06:39]

Like, if you want to know exactly what is getting transmitted on every single step of every single turn of your agent, so that way you can diagnose it and fine-tune it and make sure things aren't going off the rails, that is very hard to do. Uh, agents are also not portable. So, if I do get a good agent working, if I've managed to climb to the top of, you know, this mountain and I've got a good agent that's finally working well, well, it works well on my machine. >> [laughter] >> But if I try to pass it off to somebody else, there's a very high likelihood that between all of the environment variable configurations and and system requirements and and runtimes, there's a good chance it's not going to run on that person's machine. And they're not composable. [00:06:39 → 00:07:23]

So, even if I get, you know, a really good chatbot working for my university, the chances that I'm going to then be able to reuse that for another thing is very, very low. I can't just easily share that. So, what often happens is after a short pursuit towards agents, people kind of back away and say, "Okay, fine. No more agents, no agents. Instead, we're going to do the MCP thing. [00:07:23 → 00:07:47]

We've heard about this, it works. " And sure enough, Model Context Protocol, it does work. And really, it it works pretty well to take, you know, your corporate information like Zillow's information and then shove that into one of these really large pre-existing agents, something like Claude or ChatGPT, which I would consider a large general-purpose agent. Um and it and it sort of works like that. Uh and and it works okay. [00:07:47 → 00:08:15]

But if you take a look, this is actually from the MCP website, and if you take a look at what is supported in MCP clients around the world, you will notice that only one of these columns is actually filled out all the way down. And that, of course, is tools. So, MCP has become a de facto tool distribution mechanism for agents. So, if I need to get my company's tools into that other agent, then MCP's a good way to do that. It has not proven to be great at providing other value yet. [00:08:15 → 00:08:57]

And frankly, tools are just not enough. You know, I I I I like to joke that we didn't land a man on the moon by giving one guy a ton of tools. That's not a realistic way to get a really large project done. So, uh you know, maybe MCP's not the way, but aha, we have skills. We have skills, and skills are great. [00:08:55 → 00:09:20]

Um I I I actually do enjoy skills. I'm sure you do, too. We install them all the time for all kinds of things. And fundamentally, what a skill is is a markdown file, which basically works as documentation. Now, interestingly, there's lots of research out there that shows that if you use very many of these, it actually makes your agent substantially worse. [00:09:20 → 00:09:42]

But, they do work as documentation for various complex things. So, you know, back to the analogy of a man getting to the moon, it's a little bit like just giving this guy, you know, a ton of documentation. And the documentation's going to help, but it's not the fundamental problem. So, what's the fundamental problem? Okay. [00:09:38 → 00:10:02]

Let's build up a basic agent stack here. Let's start with a model. All agents start with a model. Big one, small one, doesn't matter. They start with a model. [00:09:59 → 00:10:10]

Then, you have something like a system prompt on top of that, which tells the model what its role in the grand universe is, sort of like its its life objective. Then, we have tools, the things that it can actually do, the effects it can take. And then, skills would be layered on top of that. And then, MCP would be layered on top of that. And then, finally, you have all the messages from the conversation. [00:10:08 → 00:10:34]

That is roughly the stack of information that gets passed along within the runtime of an agent. And if you take a look here, almost all of it is context. Basically, everything. The system prompt, tools, skills, all of that is stuff that ends up in the context of the agent. And so, basically, people are trying to solve the integration problem by working on the context or the model. [00:10:34 → 00:11:07]

These are the two areas where we constantly see new advances. We also see, you know, new new things come out like skills and and MCP, um new technologies, new protocols. They are all coming out in the in the area of the context and the model. So, how does it actually work then? Well, basically, you work at a company, you occasionally need to do some business travel, so you've got a couple travel MCPs installed. [00:11:07 → 00:11:36]

You've also got, you know, Figma and Playwright installed on yours. And all of these are building up in that context layer. And then you've got some, you know, Gmail MCPs to go check your mail for you and some Google Sheets to go fill out some other uh some other uh expense reports or something like that. And then you've got skills. You're a developer, so you've got some React fixers and linters. [00:11:36 → 00:11:59]

This is actually, I think, like, the number one or the number two most popular MCP server that's out there. Um maybe you've got uh Matt's uh grill me skill or or maybe you've got the GitHub skill. And basically, what you're doing is you are inflating that context layer. And we have a term for this in engineering. It's called inheritance. [00:11:59 → 00:12:20]

The idea of inheritance is you take an object and then you add more attributes to it to allow that one object to have other properties. Right? And that's exactly what we are doing here with an agent. We're saying, "This agent is pretty good, but if we add all of these addish- additional extra layers, then the agent can do stuff that it previously couldn't do before. " That is exactly what inheritance is. [00:12:20 → 00:12:47]

And the truth about inheritance is it works. It does work. That's why these things are out there and they are working. But, there's an old saying, "Composition over inheritance. " And it turns out this this is as old as time. [00:12:47 → 00:13:06]

Eventually, inheritance starts to break down. Imagine, like, you know, okay, I've got five skills on uh ChatGPT or on or on Claude, excuse me. And uh that works pretty well. Now, what if I have 100 skills? What if I have 1,000 skills? [00:13:04 → 00:13:21]

There's some point at which I get diminishing returns from adding additional context. That's That's just obvious. We all kind of understand that implicitly. So, is there an alternative? Well, composition is the alternative to inheritance. [00:13:20 → 00:13:35]

It looks something like this. So, like imagine we have another little agent, and again, we're trying to provide Figma as an as a as a thing that can be done by our primary agent. Well, what we could do is have a tiny little agent where the actual system prompt of the agent is written specifically to be a Figma agent. It knows everything about Figma. It it knows all of its all of its context, all of its API, all of the right places to click and the things to do and mouse movements to make and everything like that. [00:13:35 → 00:14:08]

And then it has these precise tools that it needs to perform all of those actions, and nothing more. Just that. And then a very small message history, which just has to do with the Figma portion of this. And then you can have more of these. You can still have your Gmail and your travel and your Google Sheets and all that kind of stuff, but each of them is a separate isolated agent, a full agent. [00:14:08 → 00:14:33]

Not just a little server with tools on it. It's a full agent with its own message history, its own agentic loop. And then above these, you have a coordinator. And the communication mechanism for all of these small agents speaking to the larger agent above it is just English. They just talk to each other the way a human does. [00:14:31 → 00:14:58]

So, if the primary agent is saying, "Oh, I should I should check my mail to see if there's anything about going on a trip. " Well, it knows to go ask Gmail for any new uh emails about a trip. Those funnel their way back up, says, "Oh, yeah, actually there's a trip coming up to Los Angeles this weekend. " And then it can go to our travel agent and start to make bookings. That's kind of a a rough idea of how something like this could work. [00:14:55 → 00:15:29]

And the reality is it does work. And we know it works because this is actually how we got to the moon. There were teams of experts. Teams of experts with faces that looked like that and faces that looked like that. Each of them with different skills and capabilities. [00:15:27 → 00:15:46]

And faces that looked like that. This is the Apollo 11 launch day. And look right here, there's an agent. I just found an agent sitting right there. >> [laughter] >> That brain of his is that's his LLM. [00:15:44 → 00:15:58]

And here's his tools right there on the dashboard. Those are the tools. Now, he didn't have all the tools. He just had those tools. And he was really really really good at them. [00:15:58 → 00:16:08]

And then look at that mouth. That's the messages. Uh we are used to this. We can understand this. It implicitly works. [00:16:06 → 00:16:17]

It's almost a form of biomimicry for the agentic world. Um it works. And I call them domain-specific agents. Um I don't think I was the first person to utter the words domain-specific agents. Certainly not the first person to have this idea. [00:16:14 → 00:16:31]

Um but that is what I want to talk to you about. Agents that are just targeted to very specific domain. And we over here at Standard Agents have been building this ecosystem for quite some time. So we've gotten to have a really good inside look at how they actually work. And I'm not ready to come out here and announce a product or anything like that. [00:16:29 → 00:16:51]

Um but I can give you a little bit of a peek. First of all, they are far more token efficient. Far more token efficient. We regularly see over 80% token efficiency for any given task. Now, it's a little more complicated because you have to define those tasks a little bit more ahead of time. [00:16:51 → 00:17:12]

But if you can have an agent portability where I can take that Gmail agent, squeeze it up, and then send it to somebody else, we can create an ecosystem where we don't have to create every one of these skills and capabilities, but within that domain, you're going to get dramatic efficiency. Um and part of the reason is, if you think about the way that the context work works, I don't need to have the entire context of the conversation when I make a choice to do something. Instead, my primary coordinator level can just ask the Gmail uh hey, get that last email from Debbie. And that is the totality of the context. It literally just has the system message, its tools, and that message that came in. [00:17:10 → 00:17:57]

And so, it is then able to perform this very targeted, very specialized, tiny little thing without all of the surrounding context. It's also far more practical with small language models. If you look at the difference in two models like DeepSeek uh V4 Flash and uh Fable 5, the cost difference is mind-boggling. It is 137 times cheaper than Fable per task. 137 and 37 times. [00:17:57 → 00:18:39]

Now, granted, if DeepSeek V4 Flash fails over and over and over again to do the job, then not only is it going to be, you know, not that much cheaper, it's also going to be much more annoying to use it. But that's why domain-specific agents are so great, because you don't need to have the V4 Flash do everything. Instead, it only needs to do the tasks that have been specifically picked for it to do. And with a very minimal context, it can execute those very faithfully. So, you get these dramatic cost reductions not only with the token efficiency, but also because you can use much smaller language models and even non-language models. [00:18:37 → 00:19:23]

You can use image generation and diffusion models. You can use all kinds of other models for smaller tasks. >> [snorts] >> You can also enforce really strict limits on the capabilities. And I think you know what I'm talking about. I'm talking about this. [00:19:23 → 00:19:38]

Uh we are all flying awfully close to the sun nowadays. We're everybody's just bypassing permissions left and right. And of course, you have to because a coding agent with a big model can do anything. And so, we use it to do everything. In a world that would be powered by smaller domain-specific agents, those agents can't do everything. [00:19:38 → 00:20:03]

They can only do the things that are already explicitly approved for them to do. It doesn't mean that you still can't have permissions and permission dialogues, but you are opting into a much more controlled ecosystem. And I promise you, when you explain that to Doug in IT, he puts his heart at ease understanding the difference between those two. >> [snorts] >> And uh fourth, they these have excellent scaling characteristics. Because each of these agents is its own small little execution environment, you can parallelize them. [00:20:03 → 00:20:35]

You can put them on the cloud very easily without needing like a giant VPC up there. You can run thousands of instances all at the same time um in in all kinds of regions of the world. They don't actually need to be uh you know, geographically co-located or anything like that. Um so, they have very, very good scaling characteristics. Unfortunately, they don't exist. [00:20:35 → 00:21:02]

That's the downside. >> [laughter] >> These domain-specific agents don't really exist. Um not in a big public way. Like I said, here at Standard Agents, we have them. We are working with them on a daily basis, but they are not out there in public very much yet. [00:21:00 → 00:21:22]

However, that's changing. That is going to change very quickly. We're about halfway through 2026, and and I'm here to make a public prediction that I think as we roll on from from this point to the end of 2026, we are going to see a dramatic uptick in people talking about building domain-specific agents, frameworks around them. All kinds of things are coming down the pipe. And it's not going to be a small trickle. [00:21:19 → 00:21:50]

It's it's going to accelerate rapidly, and this will become a one of the main players in the agentic ecosystem. And 2027, I would say, is basically the year of multi-agent orchestration. That's another word you'll start to hear a lot, I think. So, that's my big bold public prediction. I was really excited just a few days ago when Vercel released Eve. [00:21:50 → 00:22:17]

This is the first time I actually saw the term that I had been blasting out into the void come back and hit me in my own face. The framework for building agents build a company brain, personal assistant, or domain-specific agent. So, there we go. About halfway through the year, we're going to start picking up steam. That's my prediction. [00:22:14 → 00:22:39]

And there's a number of reasons. One of them is something that most people believe right now is that the cost of intelligence is going down. That trend reversed in 2026, actually. We track this on on a website. Tokens are not getting cheaper anymore. [00:22:37 → 00:22:57]

They are actually going up even when adjusted for IQ. They're up 29% when you adjust for IQ just this year, halfway through the year, we're already up 30% and that can be caused by lots of different things. Of course, um we've got this memory crunch and and you know, probably the long-term trend over a 10-year cycle or something is that intelligence will go down, but that does not mean that we need to be paying 137 times the cost for something that can be done just as effectively. The problem is it's harder to break those things apart. Now, if you don't account for IQ, tokens are up 76% this year, almost 100% increase in tokens just this year. [00:22:54 → 00:23:43]

Um and we're we're not even halfway through it. So, we are really trending upwards on on token costs. So, anything we can do, especially with large businesses, to bring that down is going to be really important. Um the other the other use case to really consider is putting AI in front of customers. You can't put Fable in front of a customer, um unless that customer has a massive lifetime value. [00:23:41 → 00:24:06]

It's just too expensive. So, you need to find a way to create great efficacy while being efficient. And domain-specific agents are going to be the way to do that. So, I'm going to leave you here in momentarily, um but before I do, let's just dream a little bit. Let me dig in a little bit deeper to how an agent could be orchestrated and what an ideal agent would actually look like. [00:24:06 → 00:24:32]

And then, I promise to leave you alone. Here we go. So, remember we got that model and we got the system prompt. And then, at the tool layer, let's break that apart a little bit. On one hand, we have these like functions. [00:24:32 → 00:24:45]

This would be like an actual function that can get executed, like write a file to the file system. Then, we have prompts. Prompts are a lot like the system prompt, but they are smaller individual prompts that can get injected and and sub prompts that can you know, you can run a function that actually calls an LLM. So, let's say I have a main agent running, but I want to use Nano Banana just to generate an image when I'm using GLM you know, 5. 2 as my primary. [00:24:45 → 00:25:18]

Well, you can just have a tool that's a prompt. That would be really cool if you could do that. And then another type of tool could be another full-blown agent, like a complete other domain specific agent could just be one of the tools. So, that's the tool layer. And then you have hooks. [00:25:18 → 00:25:40]

Uh what are hooks? Well, in this ideal world, a hook might be something that can kind of harness or change or mutate or perform side effects. So, let me give you an example. LLMs have no idea what time it is at any given point in time. Turns out a really great way to tell them what time it is is you inject an artificial message or an artificial tool call in the message history. [00:25:37 → 00:26:06]

So, [snorts] it looks like somebody just said, "Hey, what time it is? " and the other person replied, "Oh, it's 6:45 p. m. Pacific time. " Pretty simple. [00:26:06 → 00:26:17]