#/usr/bin/python3

import argparse
import re
import sys
from pathlib import Path

def printerr(*args):
    print(*args, file=sys.stderr)

def parse_args():
    parser = argparse.ArgumentParser(description='Process blogs')
    subparsers = parser.add_subparsers(dest="subcommand_name")
    devto_subcommand = subparsers.add_parser(
        name='devto', help='Make the post Dev.to compliant.'
    )
    devto_subcommand.add_argument(
        '--outdir',
        type=Path,
        help="Directory to output the post to",
        default=Path("_devto/")
    )
    devto_subcommand.add_argument(
        "file", type=Path, help='Post to process'
    )
    return parser.parse_args()

SITE_BASEURL = "https://beyondtheloop.dev"

YAML_HEADER_REGEX = re.compile(r"---(.*\n)*?---", re.MULTILINE)
def _remove_yaml_header(text: str) -> str:
    printerr(" * Removed YAML header")
    return YAML_HEADER_REGEX.sub("", text)

BLOG_LINK_STRING = """
**Note:** This content was originally posted in my blog, [Beyond The Loop](https://beyondtheloop.dev/3-programming-milestones-to-work-towards/).
If you like it, head over there or follow the blog on Twitter ([@BeyondLoop](https://twitter.com/BeyondLoop)) for more!
"""
def _add_blog_links(text: str) -> str:
    printerr(" * Added blog link")
    return BLOG_LINK_STRING + text

TWITTER_LINK_REGEX = re.compile(r"^.*https://twitter\.com/.*?/status/([^?]*).*$", re.MULTILINE)
def _replace_twitter_links(text: str) -> str:
    def _process_match(matchobj):
        printerr(f"    * Twitter link found {matchobj.group(1)}")
        return "{% twitter " + matchobj.group(1) + " %}"
    printerr(" * Cleaning twitter links")
    return TWITTER_LINK_REGEX.sub(_process_match, text)

YOUTUBE_LINK_REGEX = re.compile(r"^.*https://www.youtube\.com/embed/([^\"]*).*$", re.MULTILINE)
def _replace_youtube_links(text: str) -> str:
    def _process_match(matchobj):
        printerr(f"    * Youtube link found {matchobj.group(1)}")
        return "{% youtube " + matchobj.group(1) + " %}"
    printerr(" * Cleaning youtube links")
    return YOUTUBE_LINK_REGEX.sub(_process_match, text)

IMAGE_WITH_CAPTION_REGEX = re.compile(r"^.*include image-with-caption\.html.*url=[\"\']([^\"\']*).*description=[\"\']([^\"\']*).*.$", re.MULTILINE)
def _replace_image_with_caption_links(text: str) -> str:
    def _process_match(matchobj):
        printerr(f"    * Image-with-caption link found {matchobj.group(1)}")
        return f"![{matchobj.group(2)}]({matchobj.group(1)})"
    printerr(" * Cleaning image-with-caption links")
    return IMAGE_WITH_CAPTION_REGEX.sub(_process_match, text)

BASEURL_LINK_REGEX = re.compile(r"\{\{site\.baseurl\}\}", re.MULTILINE)
def _replace_baseurl_links(text: str) -> str:
    printerr(" * Replace baseurl links")
    return BASEURL_LINK_REGEX.sub(SITE_BASEURL, text)

def process_devto(file: Path, outdir: Path):
    dest = outdir / file.name
    with open(dest, 'wb') as destfile:
        contents = file.read_text()
        contents = _remove_yaml_header(contents)
        contents = _replace_baseurl_links(contents)
        contents = _replace_twitter_links(contents)
        contents = _replace_youtube_links(contents)
        contents = _replace_image_with_caption_links(contents)
        contents = _add_blog_links(contents)
        printerr("*** DONE! ***")
        destfile.write(contents.encode('utf-8'))

def main():
    args = parse_args()
    if args.subcommand_name:
        if args.subcommand_name == "devto":
            process_devto(args.file, args.outdir)

if __name__ == '__main__':
    main()