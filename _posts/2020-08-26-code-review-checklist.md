---
layout: post
title: "Fearless Code Review Checklist"
subtitle: "A systematic approach to surviving your first 5 Code Reviews"
date: 2020-08-26
url: code-review-checklist.html
tags: [Programming Fundamentals, Code Review]
call_to_action: ["I'm planning on making this checklist into a nice infographic that you can print and have beside you when you review.", "Subscribe to get notified when that happens!"]
---

> **Note:** This is a very long post, but it's worth reading! If you're in a hurry, I'll leave the condensed version of the list at the end.

Code Review is a fundamental skill for engineers.

Being able to read a set of changes and derive useful insights and constructive feedback will make you invaluable as a colleague. Plus, it will result in better code!

However, it can be very intimidating at first. It's normal to see your first Pull Request and not even know where to begin.

I had this problem when I first started, and so I did what's always worked for me:

**I asked my senior colleagues about their thought process**. How do _they_ approach code review? What do they look for? What questions do they ask?

Taking all those answers into account, I compiled my own checklist. A series of questions I can use to guide my thoughts during a review.

Having a defined, repeatable process helps me break down the process of reviewing into smaller chunks, making it a lot less overwhelming.

This list has been invaluable for me over the years. I hope it will be valuable to you as well.

# Step 1: Read the description

> Reviewing code is the act of finding out how well it solves a problem.

**Before you jump into any code at all**, you need to have answers to some questions. It's important to do this before even reading the code because it's really easy to get lost in the nitty-gritty of code style and micro-optimization, forgetting to think about how these changes affect the big picture.

In fact, most of the value of a code review will come from answering these questions, not from reading the code!

**What problem is this change trying to solve?**

This is a vital question. Every PR should solve one (and only one) problem.

The problem could be "We need this feature, and it's missing", or "There is a bug, and we need to fix it".

Reviewing a PR is the process of finding out how well it solves a problem. Therefore, a deep understanding of the problem is a vital first step.

Make sure you understand the problem, how it manifests, and how it affects users.

I've used the word "problem" a lot, but that's because it's important!

{% include mailing-list-form.html %}

**How would you solve this problem?**

Before learning how the author solved the problem, take a moment to think about how **you** would solve it. 

It doesn't have to be a full solution, just the general idea of how it would look like. You'll be surprised at how quickly you can come up with the general structure for it!

This is useful for two reasons:
- It will tell you whether you really understand the problem. If you can't come up with an idea of a solution, it's very likely that you're missing some context, and should find out more about the parts of the codebase involved with the change.
- Having a fresh set of ideas on the problem can lead to a completely different, better solution! If this is the case, that's great! Talk to the author, and discuss the new solution.

When you have your idea for what a solution would look like, the next question is:

**What solution did the author present in this change?**

This should be clear from the title and description. Remember, we haven't even looked at the code yet. Make sure you understand (and agree with) the solution and all its pieces.

Asking this question often results in us realizing that:
- We don't quite understand some piece of the solution: If this happens, you need to figure out what exactly you don't understand, and read existing code and documentation until you do!
- We don't agree with the solution: If this is the case, **stop the review**, and focus on discussing this with the author. Present your concerns, add some alternatives, and find a solution that satisfied both you and the author!

**Do you agree with the effects of the solution?**

In most engineering problems, there are tradeoffs. A more complicated solution might run faster, but be harder to maintain down the line. It may require more memory than a slower solution. On the other hand, a simpler solution might be slower, but a lot easier to maintain, and it may not be performance-critical.

Before jumping into the code, we need to make sure we understand what the tradeoffs are, and we agree that those are the right tradeoffs to make.

## You made it!

If you made it this far, it means you now have a deep understanding of the problem, and agree that the solution is the right one.

Great!

**This thought process alone will make your reviews incredibly impactful** because you will be identifying big problems first, and not getting lost in the minutia.

Now, with this deep understanding, we're ready to dive into the code.

Take a deep breath, and let's get into the nitty-gritty!

![Diving into the code](https://media1.tenor.com/images/4b69ddfc8225092fddc1973283490ddd/tenor.gif?itemid=15960012)

# Step 2: Read the code... several times

> ... we're going to go through the changes multiple times, answering a different question each time.


Let's jump into the code!

Now... where do we start?

It can feel very intimidating to just jump into the review page and start reading. It's overwhelming! Where do you even look?

The main problem here is that we're **trying to think about everything at once**. I don't know about you, but I can't do it.

When we're reviewing code, there are many things we should look for:
- Does the code actually implement the solution described in the description?
- Are there any performance concerns?
- Is the code well-tested?
- Does the code conform to formatting and style standards?

That's a lot to think about! So, instead of trying to answer all of these the first time we see the changes, **we're going to go through the changes multiple times**, answering a different question each time.

This will reduce the scope of what we're thinking about to just one question.

For instance, let's see how we'd answer the following question: "Is the code well-tested?"

Well, there's a clear path forward: We know we should **start with the tests**, and see if they cover all the cases we think should be covered. It's definitely not as intimidating!

The trick is to do the same for each question:

1. Pick one question.
2. Go through the code changes to validate that question.
3. Leave comments.
4. Go to 1.

We want to check performance? If we understand the pieces involved, we should have a good idea of which ones are sensitive to being slow (because they run often). We should focus on those first.

We want to check formatting and naming? We can forget about what the code does, and just read the words and symbols.

You should build your own list of questions to ask the code, but here's mine:

- Does the code implement the solution described?
- Does it have conscious performance tradeoffs?
- Does it have unconscious performance inefficiencies?
- Does it conform to the naming and style guidelines?
- Is it well-tested?
- Are there any hard-to-understand parts? Do they _have_ to be there? If so, are they properly isolated and documented?

# One More Time From the Top

I promised a condensed checklist, so here it is! I'm planning on making this into a free infographic that you can print, so subscribe to the mailing list to get notified when that happens!

```markdown
**Before Reading Code**
These should be checked by reading the description and existing code, not the changes themselves!
- [ ] I understand the problem this change is trying to solve.
  - [ ] I understand and agree with why we need this feature or bug solved.
  - [ ] I understand all the pieces involved in causing the problem.
- [ ] I have a general idea of how I'd solve the problem.
- [ ] I agree with the solution proposed.
  - [ ] I agree with the performance tradeoffs presented in the solution (if the change is perf-sensitive).
  - [ ] If not, I have talked with the author until we've reached consensus.

**When Reading the Code**
We should make one pass for each of these questions.
- [ ] The code implements what's actually described as the solution.
- [ ] The code doesn't have unintentional inefficiencies.
- [ ] The code conforms to naming and code style guidelines.
- [ ] There are no unnecessary hard-to-understand parts.
  - [ ] The ones that are there are properly isolated and document.
- [ ] The code is well-tested.
```

A review that looks at all of these things will be invaluable in generating better code!

# The End

That's it!

Code Review Checklist: Done!

Granted, this is a very time-consuming process. But keep in mind that **your first 5 reviews will be about learning to review correctly**. Code Review is a skill, people are expected to take some time to learn!

And the good news is, once you get the hang of it, it gets a lot faster.

After those reviews, you start asking questions one by one unconsciously, and you develop an intuition of where to start.

After dozens of reviews, I rarely go step by step in the checklist anymore, but I'm glad I have it for those tricky reviews!

What's on your checklist? I'd love to know either via Twitter [@BeyondLoop](https://twitter.com/BeyondLoop), or [email](mailto:blorente.me@gmail.com).



