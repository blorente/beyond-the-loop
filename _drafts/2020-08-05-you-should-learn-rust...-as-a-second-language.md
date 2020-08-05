---
layout: post
title: "You should learn Rust... As a second language"
subtitle: "Leverage the powerful design decisions behind Rust to level up your core engineering skills"
date: "2020-08-05"
url: you-should-learn-rust-as-a-second-language.html
tags: [Programming Fundamentals]
call_to_action: []
---

So, you've taken your first steps into programming. Welcome!

You've taken some courses, and built some amazing things. You've caught the programming bug. Congratulations!

Maybe you started with Python, doing some neat data analysis. Maybe with CSS+HTML+JS, creating beautiful projects. Maybe something else.

Whatever the case, you're now comfortable with functions and loops, and your Googling has decreased considerably.

What's the next step? What can you get into that will be exciting and interesting?

I believe, for most people, the Rust programming language is a great answer to that question.

By the end of this post, I hope you will too.

If you are, stick around for some resources on getting started with Rust!

# What is Rust?

Let's start from the beginning. What is Rust?

According to the official webpage, [rust-lang.org](https://www.rust-lang.org/) Rust focuses on 3 things:

![Rust Second Language](img/for-posts/rust-second-langauge/rust-header.png)

Let's break it down:

- **Reliable** software: Rust, by design, will help you think hard about your software, and figure out where it can fail. This will make you ask yourself questions that you didn't even know to ask. It will train you to think like a great software engineer.
- **Efficient** software: Rust makes efficient code easy to write. Usually, the simplest way to do something is also the most efficient way. 
- For **everyone**: Rust takes inclusivity very seriously. The community cares deeply about everyone feeling safe and welcome. This shows in every interaction, from the great culture around tutorials and documentation, to the very friendly meetups organized all around the world.

With that alone, it sounds like a great language to me!

## Why second language?

Okay, so if Rust is so great, why learn it as a _second_ language?

Well, here's the thing: Rust achieves these goals by giving you **full control over your computer's resources**. You decide exactly how much space everything takes, down to the byte level. Other languages that do the same are C, C++ and Assembly.

Now, as we all know:

<div class="tenor-gif-embed" data-postid="4589950" data-share-method="host" data-width="100%" data-aspect-ratio="2.4057971014492754"><a href="https://tenor.com/view/spiderman-responsibility-gif-4589950">With Great Power Comes Great Responsibility GIF</a> from <a href="https://tenor.com/search/spiderman-gifs">Spiderman GIFs</a></div><script type="text/javascript" async src="https://tenor.com/embed.js"></script>

When you're first learning to code, **you don't need that much power**. Your projects will be small, so most computers will run them without issue. They don't have to be super reliable, either.

Therefore, **you shouldn't take that extra responsibility**. It will end up getting in the way.

But, once you're ready to take the next step and work on bigger projects and applications, you **will** need to learn all the things that Rust helps you think about.

So. What *does* Rust teach you?

# Rust makes you aware of mutability

Most popular programming languages are mutable by default. In both Python and JavaScript, a function can change its parameters. In other words, this is reasonable code in most languages:

```javascript
function doSomething(element) {
    element.color = "red"
}
```

When a function changes one of its parameters like that, it's called a **side effect**.

_There are many examples of why this is generally a bad thing, but it's not something I want to argue in this article. Instead, I'll direct you to this great piece of content on side effects: _


## 

## The promise of Rust

> At it's core, Rust is making you a promise:
>
> "I will ask you to think very hard about your code before shipping it.
> In return, I will make your code run fast and without errors forever"


