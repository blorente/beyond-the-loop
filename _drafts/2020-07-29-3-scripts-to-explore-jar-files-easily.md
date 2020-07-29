---
layout: post
title: "1% Better: 3 scripts to explore jar files easily"
date: "2020-07-29"
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

I work on build systems. Specifically, I work on programs that primarily compile Java and Scala code.

When that code gets compiled, it's usually put into [JAR](https://en.wikipedia.org/wiki/JAR_(file_format)) files, which are essentially Zip files with some extra files in the right locations so that `java` knows how to use them.

Very often, I need to explore JAR files to see their contents. I may need to check whether a file is missing, or what the contents of a specific file are.

There are a lot of great tutorials out there on how to explore JAR files. There's [this one by Mincong Huang](https://mincong.io/2019/04/30/viewing-the-contents-of-jar/) if you want to use the command line, or [this one from the great Alvin Alexander](https://alvinalexander.com/blog/post/java/read-text-file-from-jar-file/) if you want to read a JAR file from a program (I seem to end up in Alvin's tutorials at least once a week).

However, **I don't want to Google every time** I need to open a jar, and I also **don't want to memorize** all the `unzip` and `jar` comands and flags.

So, I decided to automate the three tasks that I perform the most with jars.

These are three little functions that you can copy into your `~/.bashrc` file, and they will be available everywhere in your shell

**Sidenote:** If you're wondering what `~/.bashrc` is, you may want to check out this [introduction to the shell](https://codeburst.io/your-perfect-kickstart-to-shell-scripting-857b81c0939b/).

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
Not much to se here, but incredibly useful since I always have to look up the `jar tf` command.

### See the contents of a file in the jar

- You can pipe the output to whatever you want

- Use peek_jar_manifest, the manifest is a very common file to check.


