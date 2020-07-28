---
layout: post
title: "1% Better: Make git status interactive with -p"
date: 2020-07-29
url: make--interactive-with-.html
tags: [1% Better, git]
call_to_action: ["You are now 1% better as an engineer!", "Subscibe to get the next 1% tip!"]
---

> **TL;DR**
> 
> Use `git add -p` to interactively stage chunks of files.
> 
> It's one of the few git flags I have memorized and use every day.

Tell me if this sounds familiar:

You're coding a project, implementing a feature, making changes, "in the zone"... And you're done!

Good job! Now we just have to commit it.

You type `git status` to know how it looks, and:

![Git status madness]({{site.baseurl}}/img/for-posts/git-add-p/git-status-madness.png)

That's a lot of touched files! Ideally we would like to have commits be distinct units of change, that implement one thing.

However, it's really hard to form a good commit history when we've gone that long without committing.

To the rescue: [**git add -p**](https://git-scm.com/docs/git-add#Documentation/git-add.txt--p)

### The flag

`--paragraph` (or `-p`) is a flag that allows you to interactively stage (or "add") chunks of files.

It will look at the changes you've made to your already tracked files (you have added them previously to a commit). For each change, it will ask you: "Do you want to add this?"

![Git add paragraph example]({{site.baseurl}}/img/for-posts/git-add-p/git_add_p_example.png)

It's a magical feature that I use every day. Some of its uses include:

- Giving a second look to each of your changes before commiting it (lots of typos were caught like that).
- Creating a cleaner commit history by enabling smaller commits.

### Extras

`-p` is incrediby powerful. When it asks you whether to stage a change, `y` and `n` are not the only answers you can give it. Some of my favourites include:

- `s`: Try to split the change into smaller hunks, for even finer-grained control over the changes you commit.
- `e`: Open a text editor and change the diff. Be careful, whenever you save the diff and close the editor, those changes will be staged automatically.
- `?`: Explain all the possible commands.

The best way of getting a feel for everything it can do is to try it out and explore. Don't be afraid to experiment!

### Conclusion

`git add -p` is a magical command that has made my life so much easier. If you didn't know about it, I'm confident it will improve yours too.

What do you think? Was this useful? Was it not? What other git concepts would you like to learn about? What other flags do you use?

I want to make these tips as useful as possible, so don't hesitate to give feedback.