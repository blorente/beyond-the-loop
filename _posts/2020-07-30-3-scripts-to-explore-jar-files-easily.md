---
layout: post
title: "1% Better: 3 scripts to explore jar files easily"
date: 2020-07-30
url: 3-scripts-to-explore-jar-files-easily.html
tags: [1% Better, jars, java, jvm]
call_to_action: ["You are now 1% better as an engineer!", "Subscibe to get the next 1% tip!"]
---

> **TL;DR**
>
> These three functions have been very useful for me when looking at the contents of a jar,
> I hope they are useful to you as well:
>
> ```bash
> # Pretty-ptrint the list of files in a jar
> # Example usage: `$ peek_jar path/to/my.jar`
> function peek_jar() {
>   jarfile=$1
>   jar tf "${jarfile}" | sort
> }
>
> # Get the contents of a file inside the jar
> # Example usage: `$ peek_jar_file path/to/my.jar com/oracle/Class.class`
> function peek_jar_file() {
>   jarfile=$1
>   file_to_peek=$2
>   unzip -p "${jarfile}" "${file_to_peek}"
> }
>
> # Get the contents of META-INF/MANIEST.MF, a very common file to query
> # Example usage: `$ peek_jar_manifest path/to/my.jar`
> function peek_jar_manifest() {
>   jarfile=$1
>   peek_jar_file "${1}" "META-INF/MANIFEST.MF"
> }
> ```

## The Problem

I work on build systems. Specifically, I work on programs that primarily compile Java and Scala code.

When that code gets compiled, it's usually put into [JAR](https://en.wikipedia.org/wiki/JAR_(file_format)) files, which are essentially Zip files with some extra files in the right locations so that `java` knows how to use them.

Very often, I need to explore JAR files to see their contents. I may need to check whether a file is missing, or what the contents of a specific file are.

There are a lot of great tutorials out there on how to explore JAR files. There's [this one by Mincong Huang](https://mincong.io/2019/04/30/viewing-the-contents-of-jar/) if you want to use the command line, or [this one from the great Alvin Alexander](https://alvinalexander.com/blog/post/java/read-text-file-from-jar-file/) if you want to read a JAR file from a program (I seem to end up in Alvin's tutorials at least once a week).

However, **I'm very lazy, and my memory is awful**. 

I don't want to Google "how to see files in a jar" every time I need to inspect one.

So, I decided to automate the three tasks that I perform the most with jars.

## The Solution

These are three little functions that you can copy into your `~/.bashrc` file, and they will be available everywhere in your shell.

**Sidenote:** If you're wondering what `~/.bashrc` is, you may want to check out this [introduction to the shell](https://codeburst.io/your-perfect-kickstart-to-shell-scripting-857b81c0939b/), and subscibe below to read my introduction to dotfiles.

You might notice that **these functions are not complicated**. They are not fancy, they are not smart.

That's not the point.

The point is to take 10 minutes to solve a frequent problem once and for all. **To reduce friction** with my tools, so that I can focus my mental energy into actually solving the problem.

**The value of a program** is not measured by how "smart" it is, but rather by **how well it solves a problem.** And these functions have proven plenty valuable.

Withouth further ado, here are the three little functions.

### List the files in a jar

```bash
# Pretty-ptrint the list of files in a jar
# Example usage: `$ peek_jar path/to/my.jar`
function peek_jar() {
  jarfile=$1
  jar tf "${jarfile}" | sort
}
```

This function lists the files in a jar, without any metadata, sorted alphabetically.
Not much to se here, but incredibly useful since I always forget the `jar tf` command.

As usual, you can pipe the output to other commands to form chains:

```bash
# Show only files in package "org/apache", then count them
peek_jar a.jar | grep "^org/apache" | wc -l

# Is the class "MyCats" in this jar?
peek_jar a.jar | grep "MyCats\.class"
```

And that's it!

### See the contents of a file in the jar

```bash
# Get the contents of a file inside the jar
# Example usage: `$ peek_jar_file path/to/my.jar com/oracle/Class.class`
function peek_jar_file() {
  jarfile=$1
  file_to_peek=$2
  unzip -p "${jarfile}" "${file_to_peek}"
}
```

The tip above is there because I didn't want to remember `jar tf`. This one is about not wanting to remember `unzip -p`.
It prints the contents of a file to stdout.

Seeing the contents of a file is great but more often than not I want to do some post-treatment to the file.
It's easy to do it with this command, by piping it to other commands:

```bash
# Interactively see and scroll through the file
peek_jar_file a.jar com/MyClass.class | less
```

The most common file I look up is `META-INF/MANIFEST.MF`, because it contains important metadata about how the package is formed.  You can learn more about the `MANIFEST.MF` file in this [great tutorial from baeldung.com](https://www.baeldung.com/java-jar-manifest).

`META-INF/MANIFEST.MF` is hard to type, and I'm lazy.

That's why the third little script is just a version of the last one that prints out the manifest file:

```bash
# Get the contents of META-INF/MANIEST.MF, a very common file to query
# Example usage: `$ peek_jar_manifest path/to/my.jar`
function peek_jar_manifest() {
  jarfile=$1
  peek_jar_file "${1}" "META-INF/MANIFEST.MF"
}
```

### Conclusion

These three scripts are nothing special, they are **very easy** to write.

They took me minutes to create, but they have saved me hours of time and mental energy, by not making me remember extra commands that I don't need.

**Consistently solving small problems** like these to make your day to day just that little bit more efficient will pay handsomely in the long run!

I encourage you to do the same: Actively look for little annoyances, "papercuts", that keep taking small amounts of mental energy. 

Then, solve them forever!

---

I hope these tips have been useful. If you've enjoyed it, please consider sharing it with other folks.

If not, I'd love to hear your thoughts!