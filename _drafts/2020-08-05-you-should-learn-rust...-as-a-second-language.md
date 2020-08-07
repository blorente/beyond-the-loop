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

# Rust will teach you about types

Let's look at the following example in JavaScript:

```javascript
function add(a, b) {
    return a + b
}
```

What are `a` and `b`? Are they numbers? Letters? Lists?

It doesn't matter. As long as the `+` operation makes sense for them, you don't have to know anything else about `a` and `b`.

Most beginner programming languages don't enforce types. And that's a good thing! In small applications, types just get in the way.

However, as you start working on bigger and bigger projects, you start to realize that types have one benefit:

They give you information about other parts of the program **without having to read it**. If used right, types teach you how to use a function without having to read the body!

Let's look at the same function, in Rust:

```rust
fn add(a: i64, b: i64) -> i64 {
    return a + b
}
```

The signature of the function (`add(a: i64, b: i64) -> i64`) tells us exactly what the function does: 

> If you give me two numbers (`i64` is a type of number in Rust), I will `add` them and give you another number back (`-> i64`).

This is much more descriptive than the other example!

Eventually, you're bound to come across types in your programming career, and Rust will teach you all you need to know!

# Rust makes you aware of mutability

Most popular programming languages are mutable by default. In both Python and JavaScript, a function can change its parameters. In other words, this is reasonable code in most languages:

```javascript
function doSomething(number) {
    number = 5
}
```

When a function changes one of its parameters like that, it's called a **side effect**. Side effects are generally best avoided.

_There are many examples of why this is generally a bad thing, but it's not something I want to argue in this article. There are many great articles out there arguing for it. Search for "immutability"._

In Rust, **you need to say which of your variables are expected to change**. Let's look at the same function, written in Rust:

```rust
fn doSomething(number: &mut usize) {
    number = 2
}
```

Notice the little `&mut` after the parameter name: It tells you that 

As you can see, you always know whether a function will change what you pass to it, **just by the first line**!

Yet another piece of information that Rust gives us to **guess what a function does without reading it**.

# Rust will teach you about memory management

Earlier in this article, we talked about how Rust's type system is very powerful.

TODO RUst;s types are tied to memory!

