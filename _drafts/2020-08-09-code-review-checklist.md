---
layout: post
title: "My Code Review Checklist"
subtitle: "A systematic approach to make Code Review less overwhelming"
date: "2020-08-07"
url: code-review-checklist.html
tags: [Programming Fundamentals, Code Review]
call_to_action: ["I'm planning on making this into a nice infographic.", "Subscribe to get notified when that happens."]
---

Code Review is a fundamental skill for engineers.

Being able to read a set of changes and derive useful insights and constructive feedback will make you invaluable as a colleague. Plus, it will result in better code!

However, it can be very intimidating at first. It's normal to see your first 100 line change Pull Request, and not even know where to begin.

I know I had this problem when I first started, and so I did what's always worked for me:

I asked my senior colleagues for their thought process. How do _they_ approach code review? What do they look for?

Taking all those answers into account, I commpiled my own checklist. A series of questions I can use to guide my thoughts during a review.

Having a defined, repeatable process helps me break down the process of reviewing into smaller chunks, making it a lot less overwhelming.

This list has been invaluable for me over the years. I hope it will be valuable to you as well.

**Note:** This is a very long post, but it's worth reading! If you're in a hurry, I'll leave the condensed version of the list at the end.

# Fist: Read the description

**Before you jump into any code at all**, you need to have answers to some questions. It's important to do this before even reading the code, because it's really easy to get lost in the nitty-gritty of code style and micro-optimization, where these are the important questions to ask.

**What problem is this PR trying to solve?**:
This is a vital question. Every PR should solve one (and only one) problem.
The problem could be "we need this feature, and it's missing", or "there is a bug, and we need to fix it".
Evaluating a PR is essentially finding out how well it solves the problem, so it's vital that you understand it.
Make sure you understand the problem, how it manifests, and how it affects users.
  
**How would you solve this problem?**:
Before learning how the author solved the problem, take a moment to think about how **you** would solve it. 

It doesn't have to be a full solution, just the general idea of how it would look like. You'll be suprised at how quickly you can come up with it!

This is useful for two reasons:
- It will tell you whether you really understand the problem. If you can't come up with an idea of a solution, it's very likely that you're missing some context, and should find out more about the parts of the codebase involved with the change.
- Having a fresh set of ideas on the problem can lead to a completely different, better solution! If this is the case, that's great! Talk to the author, and discuss the new solution.

When you have your idea for what a solution would look like, the next question is:

**What solution did the author go with?**
This should be clear from the description of the PR. Make sure you understand (and agree with) the solution and all its pieces.

Some common results of asking this question are:
- You don't quite understand some piece of the solution: If this happens, you need to figure out what exactly you don't understand, and read code and documentation until you do!
- You don't agree with some part of the solution: If this is the case, **stop the review**, and focus on discussing this with the author. Present your concerns, add some alternatives, and find a solution that satisfied both you and the author!

**You made it!**
If you made it this far, it means you now have a deep understanding of the problem, and agree that the solution is the right one.

Great!

This thought process alone will make your reviews incredibly impactful, because you will be identifying big problems first, and not getting lost in the minutia.

Now that that's done with, you're ready to begin reviewing the implementation!

# Second: Make different passes through the changes, looking for different things each time



