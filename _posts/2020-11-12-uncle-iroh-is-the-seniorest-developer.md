---
layout: post
title: "3 Programming Lessons From Uncle Iroh"
date: 2020-11-12
url: uncle-iroh-is-the-seniorest-developer.html
tags: []
call_to_action: []
---

Uncle Iroh, from _Avatar: The Last Airbender_ is one of my favourite characters in fiction. It's this guy:

![Uncle Iroh](https://anuradhaedirisuriya.files.wordpress.com/2011/03/untitled-12.jpg)

The quintessential mentor, he gives insightful advice to all the main characters in the series.

His attitude towards life - making the most of the circumstances, enjoying the moment, and detaching himself from his ego - brings a great deal of **perspective** to the struggling heroes. It makes them see the wider picture, and make sure they're doing the right thing for the right reasons. 

We can draw programming wisdom from many places, and Uncle Iroh happens to be a really good one.

In this post, I want to explore 3 ways in which Iroh's perspective can make us better programmers. Not by teaching a specific tool or service, but by directing us toward the right attitude.

It's short and sweet, so let's get started.

# Draw knowledge from many places

> It's important to draw wisdom from many different places.
> 
> If we only take wisdom from one place, it becomes rigid and stale.
>
> [...] Understanding others will help you become whole.
>
>  - Uncle Iroh

![Uncle Iroh's circle]({{site.baseurl}}/img/for-posts/iroh/iroh-circle.png)

There are many ways to write code. From Design Patterns to Functional Programming, trends and ideas about what code should look like come and go.

Most of these ideas have one goal in mind: To make programs easier to read and modify, easier to reason about.

Some of those trends tend to be exclusionary, meaning that they portray "opposing" trends as universally bad.

For instance, many people in favor of Functional Programming also reject any sort of mutable state outright, even when doing so results in a program that is harder to understand.

This often creates dogmatism, where writing any code outside of those practices is not an option anymore. We even refer to this as "preaching" or "evangelizing" a style. Even when that wasn't the original intention!

This teaching from Iroh reminds me to not settle on what I know.

It reminds me that there are very few universal truths about programming styles, and defaulting to one without considering the others is almost always a mistake.

We are not paid to deliver the purest or the best-tested program, we are paid to deliver value. **Testing practices, design patterns and programming paradigms should only be used if it allows us to deliver more value, faster**.

**TL;DR:** Never accept a programming approach as dogma and the rest as "wrong". Learn many approaches, understand their tradeoffs, and choose the right one for each job.

# Bugs are like an octopus

> You're fishing for an octopus! You need a tightly woven net, or he will **squeeze through the tiniest hole** and escape.
> 
> - You guessed it, Uncle Iroh

This one might sound like a far-fetched metaphore...

Okay, it is, but hear me out anyway.

In this metaphore, the net represents what you _know_ about the system, and holes represent things that you don't know.

To catch a bug, your net must not have holes. You realize you have no idea what a part of the system does, you learn about it, and fix the bug. Simple enough.

However, this goes deeper.

Some bugs very hard to catch. They don't need a hole in your net. A loose thread is enough for them to squeeze away!

These loose threads are the things you _think_ you know about the system, but you don't really.

These are the things you **assume**.

And assumptions are where the most complicated bugs lie.

We regularly assume things about the system and its environment - From the workings of a particular function, to the operating system, the resources available, or even other applications that might be interfering with our code.

Those assumptions are necessary - we can't keep everything in our head at once - but when the time comes to catch a slippery bug, we need to check every one of them.

When you want to catch a slippery bug, start by tightening the net. Start by checking your assumptions.

**TL;DR:** The hardest bugs don't hide in the things that you don't know, but in the things you assume you know. When debugging, check your assumptions!

# Tea

> Sharing tea with a fascinating stranger is one of life's true delights.
> 
> - You know who

![Uncle Iroh, sharing tea](https://imgix.bustle.com/uploads/image/2020/6/1/65220bb4-d554-403f-a682-d704bd217007-atla-iroh-tea.jpg?w=1200&h=630&q=70&fit=crop&crop=faces&fm=jpg)

I'm naturally shy, and it takes a lot for me to approach strangers.

Whenever I'm in a gathering (a conference, a meetup...), this quote reminds me that:

- Most people here know a lot more about _something interesting_ that I do, and
- Most people are super nice, and glad to talk about what they are passionate about.

This helps me get over that shyness, approach people, and ask them questions about the talk they just gave.

These interactions have created some of my most cherished memories and relationships. Plus, they have shaped my professional career!

I learned about my current job from a great chat I had with [Stu Hood (@stuhood)](https://twitter.com/stuhood) about build systems in Krakow!

**TL;DR:** Most people have something to teach you, and are happy to talk about it! Cherish opportunities to meet new and interesting folks.

## Conclusion

So, there you have it!

I hope you have enjoyed these pieces! If you'd like a very naive cartoon with amazingly-written characters and dialogues, I whole-heartedly recommend _Avatar: The Last Airbender_. There are many more things about Iroh that make me think, just not directly applicable to programming.

What did you think? Did this post make you think? Was this stuff you already knew?

I'd love to hear any feedback you have on Twitter, [@BeyondLoop](https://twitter.com/BeyondLoop)!

Have an amazing day,

Borja