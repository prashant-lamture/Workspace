#!/usr/bin/env python

import os
import sys
import argparse

from ollama import Client

from course_toc_php import toc_php
from course.content.rust.toc import toc_php


def log(line):
    print(f"LOG: {line}")


# --------------------------------------------------------------------------------------------------
host = "ubuntu"
ollama = Client(host=host)


# --------------------------------------------------------------------------------------------------
parser = argparse.ArgumentParser(description="Course Generator with AI.")

parser.add_argument("topic", type=str, help="The Topic of the course.")
parser.add_argument("--short", type=str, default=None, help="Short name of topic.")
parser.add_argument(
    "--output", type=str, default="course", help="Generate Table of Conent for Course."
)
parser.add_argument(
    "--toc", action="store_true", help="Generate Table of Conent for Course."
)
parser.add_argument("--content", action="store_true", help="Generate Content from TOC.")
parser.add_argument("--nrofchapters", default=20, help="Number of Chapters.")
parser.add_argument("--nrofexamples", default=5, help="Number of Examples.")


args = parser.parse_args()

topic = args.topic
nrofchapters = args.nrofchapters
nrofexamples = args.nrofexamples


if topic == "":
    print("Missing Topic")
    sys.exit()


# --------------------------------------------------------------------------------------------------
def generate_response(prompt: str):
    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response["message"]["content"]


# --------------------------------------------------------------------------------------------------
def generate_toc(topic: str):
    prompt = (
        f"""The topic is '{topic}'.

Create a course for this topic that consists of 3 parts with {nrofchapters // 3} chapters each, total if {nrofchapters} chapters.
- Part One overs the basic elements of the topic, syntax and language elements.
- Part Two covers the patterns, components and framework basics.
- Part Three covers best practices, features, and tips and tricks.

The final course contains content for 60 weeks.
The level for the weeks should range from beginner to advanced to expert level.

Create the table of content with all parts and chapters, structured in part, chapter, topic.

Create content for all parts in only one output dictionary.
"""
        + """
The structure of the output dictionary should be:
toc = [
  { "part": 1, "chapter": 1, "content": topic },
  { "part": 1, "chapter": 2, "content": topic },
  { "part": 1, "chapter": 3, "content": topic },
]

Only show the structure, no additonal information, comment or text.
"""
    )

    return generate_response(prompt)


# --------------------------------------------------------------------------------------------------
def generate_lesson(topic: str, lesson: str):
    prompt = (
        f"""
Here is a lesson title of a programming course:
{lesson}

The topic of the couse is :
{topic}
"""
        + """
Using the lesson title, create the content to learn all about this lesson:
- create 5 examples with solutions, including the code required to run the example
- create a README.md file in Markdown that describes the lesson.
- create a LESSON01, LESSON02 for each lesson describing the lesson.

Finale, create a python dictionary containing all created files

The structure of the python dictionary is:
lessons = {
    '<LESSON>': [
        {
          "example": <LESSON>
          "description": <README-md>,
          "examples": [
            "name": <EXAMPLE>,
            "html": <HTML CODE>,
            "css": <CSS CODE>,
            "js": <JAVASCRIPT CODE>,
            "code": <PROGRAM CODE>
            "readme": <LESSON.md>
          ]
        },
    ]
}

Only show the lessons python dictionary, no additonal information, comment or text.
"""
    )

    return generate_response(prompt)


# --------------------------------------------------------------------------------------------------
print(f"Generate Course material for {topic}")

short = args.short
if short is None:
    short = args.topic.replace(" ", "_").replace(")", "_").lower()

if args.toc:
    root_fldr = f"{args.output}/{short}"

    os.makedirs(root_fldr, exist_ok=True)

    print(f"Generate TOC {topic}")
    response = generate_toc(args.topic)

    output_file = f"{root_fldr}/toc.py"
    with open(output_file, "w") as f:
        print(f"Save TOC for {args.output}")
        f.write(response)

if args.content:
    root_fldr = f"{args.output}/{args.short}/content"
    os.makedirs(root_fldr, exist_ok=True)

    for item in toc:
        part = item["part"]
        chapter = item["chapter"]
        lesson = item["content"].replace("/", "_")

        print(f"- generate lesson for '{lesson}'")
        response = generate_lesson(args.topic, lesson)

        output_file = f"{root_fldr}/{part}_{chapter}_{lesson}.py"
        with open(output_file, "w") as f:
            print("- save lesson")
            f.write(response)
