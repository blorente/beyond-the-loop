---
layout: post
title: "3 Programming milestones to work towards"
subtitle: "How to know when you're not a beginner anymore"
date: "2020-08-01"
url: 3-programming-milestones-to-work-towards.html
tags: [Programming Fundamentals]
call_to_action: ["Subscribe for tips to achieve each of these milestones", "I won't spam you, I promise!"]
---

I recently had a great conversation on Twitter with [@svpino](https://twitter.com/svpino) and others, about the line between beginner and advanced programmer:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I&#39;m curious: How do you know when to switch from &quot;beginner&quot; to &quot;seasoned&quot;?<br><br>Getting over the middle part was the hardest part of my dev journey.</p>&mdash; Beyond The Loop (@BeyondLoop) <a href="https://twitter.com/BeyondLoop/status/1289585379524268032?ref_src=twsrc%5Etfw">August 1, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

That got me thinking: **At some point, one stops being a beginner**. And that point is not very clear.

In this post, I outline 3 programming milestones that made me realize that I had leveled up, and resources to achieve each one.

**Every engineer I consider "advanced" has reached these milestones**, so I think they are worthy goals for anyone.

If you are interested in any of these goals, but would like advice or direction, **don't hesitate to contact me on Twitter**: [@BeyondLoop](https://twitter.com/BeyondLoop). I'll be happy to help however I can.

# Milestone: You are mindful about workflow friction

> Our most important resource is mental energy. Optimizing it is key to good engineering.

Our mental energy is limited. Experienced programmers don't have more energy than beginner programmers, they just use what they have more efficiently.

They **intentionally invest in maknig their workflow seamless**, so that they have as much energy as possible to actually solve hard problems.

For instance: While Googling things is perfectly normal and great, **Googling the same thing over and over again** is a waste of time and energy. Every time we Google something, we're forced to stop our "flow", which costs a lot of mental energy!

Here are some of the ways I've improved my workflow, that can help you too!

- **I have a big Google Doc** of knowledge: Every time I learn a complicated concept, I write **my explanation** into it. It's been going on for a couple of years, and it's about 50 pages long.
- **I got comfortable with the command line**. It's an incredibly useful tool, if you can use it correctly!
- **I have a [shortcuts repo](https://github.com/blorente/dotfiles)**, where I keep command-line shortcuts for commands I use often.
  `git add -p` becomes `gap`, `./bazel query --output build` is `bqb`, etc. Seconds of typing matter!
- I have learnt some **keyboard shortcuts** for most of the popular text editors. Editing code without breaking your train of thought can save you a lot of mental power!

All of these are gradual, and **built over the course of a whole career**. Don't worry if you don't have the perfect workflow now, worry about making it 1% Better every day!

> If you improved yout workflow by 1% every 3 days for a year, you'd be twice as good at the end of the year.

Now, not every workflow is worth being automated. You should focus on finding the sweet spot of *"easy improvements that save me large amounts of time over years"*.

If you're not sure about whether it's worth it, check out this graph by [XKCD](https://xkcd.com/1205/):

{% include image-with-caption.html url="https://imgs.xkcd.com/comics/is_it_worth_the_time.png" description="Source: https://xkcd.com/1205" extrastyle="width: 80%; margin: 0 auto;" %}

#### Resources

- [CodeNewbie Podcast, Ep. 7x2: How do I Level Up?](https://www.codenewbie.org/podcast/how-do-i-level-up) The [CodeNewbie Podcast](codenewbie.org) is a great all-around resource to learn from. In this episode, it 
- [Upcase](https://thoughtbot.com/upcase): The best resource for levelling up as an engineer. Tutorials on Vim, Bash and Git are great to improve your workflow!
- [The 1% Better Tag](/tags/#1%%20Better) **in this very blog** is a collection of workflow improvements I've found over the years! Browse it to see if any are useful, and Subscribe to get notified whenever there's a new one!
- [Getting Started With Dotfiles](https://medium.com/@webprolific/getting-started-with-dotfiles-43c3602fd789): An introduction to one of the best ways to automate your workflow.

So, **reduce friction in your workflows!** Next milestone:

# Milestone: Git is intuitive for you

> Every senior developer I've come across has a deep, intuitive understanding of Git

If you're going to be developing code professionaly to any extent, you're probably going to come across Git. When you *do* come across it, you might notice that it's not the most intuitive of tools.

_Note: If you haven't come across Git yet, I'd advise you to read one of the [Many](https://try.github.io/). [Great](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners). [Tutorials](https://www.youtube.com/watch?v=SWYqp7iY_Tc) out there. It's a great tool to keep track of changes on your code!_

I used Git for many years without really understanding what I was doing. I learned 4 commands (`git add`, `git commit`, `git pull`, `git push`) and asked my git-savant friend [@AlvarBer](https://twitter.com/alvarber) for help whenever I got stuck. Which was often. I felt that Git was not very user-friendly.

Okay, fine: **I thought it hated me**.

However, one summer I was introduced to a new command: `git rebase -i`.

The specifics deserve a whole separate post, but after a very frustrating weekend fiddling with it I had a realization:

> Git sees a repository as a series of **atomic immutable changes** (called *commits*) that can be **copied**, but **not changed, moved or deleted**.

Note a few important bits in that sentence:
- Commits are **atomic immutable changes**: Once you create a commit, it cannot be split into smaller pieces, or modified. If you want to split a commit, you need to create two new commits.
- Commits can be **copied**: Operations like `git cherry-pick` and `git rebase` may seem daunting at first, but once you understand them as essentially copying operations, they become very intuitive and useful.
- Commits cannot be **moved** or **deleted** (except very intentionally): Git is designed to make it really hard to lose work. Once you commit something, it's really hard to delete it. Therefore, **don't be afraid to experiment** with Git commands, as there's always a way to go back! Even if you think you've messed up, there's usually a way to recover your work.
  
  If you get in trouble, feel free to reach out in Twitter [@BeyondLoop](https://twitter.com/BeyondLoop).

Once you understand that, you deeply understand the rest of the commands (and even some of the error messages!).

With time, you develop an **intuition** for Git that allows you to do complex operations in a short amount of time, such as:

- Re-writing the commit history so that every commit makes sense independently of the others. This will make you an amazing Open Source contributor!
- Experimenting with different versions of solving problems in different branches, and easily pick from one and the other.

Every senior developer I've come across has a deep, intuitive understanding of Git, and for good reason. Spend time to learn it well, and it will reward that time tenfold.

#### Resources:

- [Git For Ages 4 and Up](https://www.youtube.com/watch?v=3m7BgIvC-uQ): The best Git tutorial I've seen to date. An in-depth explanation of what I've written here:

<div class="text-center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/3m7BgIvC-uQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

- [GitHub's Curated List of Tutorials](https://try.github.io/): GitHub is the biggest service that hosts Git repositories. They have extensive documentation to learn about Git.

And last, but not least:

# Milestone: You don't think in terms if/for statements anymore

> A mark of an experienced engineer is that they are able to look at increasingly bigger pictures.

Learning to program is very similar to learning to speak.

When you first start learning to code, you struggle with the syntax of languages. **You struggle to communicate simple concepts** to the computer, such as `if the color is "red", then stop`.

As you become used to the syntax, you also start finding it easier to express those concepts. They become second nature, you don't have to think about them anymore.

Now that you are comfortable with expressing simple concepts, **you can compose them into more complex ideas**, like functions.

When you master those more complex pieces, you can use _those_ to compose bigger and better things, like whole applications.

This cycle actually continues, almost forever. **Experienced engineers have deeply mastered many, many concepts**, so they are able to form very complex systems without being worried about the details of every small pieces.

**The more advanced you are, the bigger picture you can see**.

#### Resources

While **practice** is king to develop this intuitive understanding, here are some books that teach essential concepts:

- [Clean Code](https://amzn.to/317iqo9): It's a great handbook for solid Object Oriented Programming. Whether you like OOP or not, it has some great notions on how to keep OOP code neat and tidy.
- [The Pragmatic Programmer](https://amzn.to/2D0C6lK): The best programming book I've read, by far. It outlines best practices for engineers, and **how** to achieve the deep understanding I refer to in this book. I want to write a full review soon, so subscribe if you're interested!

**Full Disclosure:** These are all affiliate links, so I get a small amount of money if you buy them. These are my favourite books, and I really think you'll enjoy them.

## Conclusion

These milestones have been consistently met by senior developers around me, so I think you can benefit by working towards them!

If you are interested in any of these goals, but would like advice or direction, **don't hesitate to contact me on Twitter**: [@BeyondLoop](https://twitter.com/BeyondLoop). I'll be happy to help however I can.

Until then, happy journey!