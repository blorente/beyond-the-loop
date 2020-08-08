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

# Rust teaches you to read (and understand) the output of your tools

Rust will try to catch and fix a lot of your bugs before it runs your code.

This is great, because it means that it will teach you to think about things that you weren't thinking before (more on that later), but it also means that it will produce **a lot** of error messages.

In fact, programming in Rust is often described as **"a conversation with the tools"**, where you tell the tool "is my code allright?" and the tool responds with great error messages.

Inevitably, this means that you'll need to **get into the habit of reading erorr messages carefully**. Rust's error messages are thoughtfully crafted to be informative and actionable.

Sometimes, Rust will even guess what concept you need to understand to solve the error, and **point you to the right documentation!**

Let me repeat that.

Rust will see the bug, catch it, guess "this user doesn't quite understand X", and it will give you a link to it!

If you get into the habit of carefully reading and understanding error messages, your productivity and learning will skyrocket.

Now, let's dive into some more concrete things Rust will teach you.

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

Let's take a look at this code:

```javascript
var hello = "Hello World!"
console.log(hello)
console.log(hello)
```

For this code to work, the computer has to remember what the value of `hello` is, **all the way until the end of the program**. In other words, it has to **store** it in **memory**.

A computer has a finite amount of memory, or things it can remember at any given time. Incidentally, this is one of the reasons why your phone closes background apps, or why your whole computer becomes slow when you have too many tabs open.

For small applications, this is not really a concern. There aren't _that_ many things the project needs to remember.

However, it's not uncommon for big applications to have to remember several Gigabyte's worth of data at once, which can quickly become a problem.

Let's say we want to represent a 2D point in JavaScript. We could write the following:

```javascript
var p = {
  x: 0,
  y: 0
}
```

How much memory do we need in order to remember `p`?

Trick question, the code doesn't tell us.

Rust, however, lets you choose **exactly how much memory** it takes to remember something, and **how long the computer needs to remember it for**.

Let's see how we can implement that same point in Rust:

```rust
struct Point {
  x: i64,
  y: i64,
}

let p: Point = Point{x: 0, y: 0}
```

How much memory does it take to remember one `p`?

Well, a `Point` has one `x` and one `y`. They are both `i64`. An `i64` takes exactly 64 bits of memory. So, a `Point` will take exactly 128 bits of memory.

Most types in Rust can be broken down this way. Thinking about code this way will make you aware of when you're remembering too much!

Now, there is a lot more Rust does about memory management that I won't get into here. Suffice to say that it's **a great language if you want to learn about it!**

# Sounds great! Where do I start?

These are just a few reasons why I think Rust is great as a second language.

If I've convinced you and you want to give it a try, check out these resources!

- The [Rustlings Course](https://github.com/rust-lang/rustlings): An open source series of exercises that guide you through setting up your Rust environment and writing your first lines of Rust! If in doubt, start here.
- The official website has a [Learn Page](https://rust-lang.org/learn) with the most popular and amazing resources.
- Rust has an amazing community that is more than ready to welcome newcomers. Check out the official website's [Community Section](https://rust-lang.org/community) for more links.
- If you're an experienced developer coming from another language, check out [intorust.com](http://intorust.com). It's a series of videos explaining the fundamental differences that Rust has with other languages like C++ or Java.

# Conclusion

Rust is an amazing language, and I personally love it. I wouldn't recommend it as a first language, but it's a fantastic tool to guide you in those next steps beyond the beginner phase!

What do you think? Whether you agree or disagree, I'd love to hear from you!


