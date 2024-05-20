#!/usr/bin/env python

import os
import zipfile

# from course_content.course_02_javascript import course_content
# from course_content.course_10_bootstrap import course_content
from course_content.course_11_tailwindcss import course_content

ROOT = "02_javascript"
ROOT = "10_bootstrap"
ROOT = "11_tailwindcss"


def create_zipfile(week):
    # Create a zip file for the week
    zip_filename = f"{week}_JavaScript_Course.zip"
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for foldername, _, filenames in os.walk(week):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                zipf.write(filepath, os.path.relpath(filepath, week))


# Function to create files and zip them
def create_week_files(folder, html, css, js, readme):
    if html is not None:
        with open(os.path.join(folder, "index.html"), "w") as html_file:
            html_file.write(html.strip())

    if css is not None:
        with open(os.path.join(folder, "styles.css"), "w") as js_file:
            js_file.write(js.strip())

    if js is not None:
        with open(os.path.join(folder, "script.js"), "w") as js_file:
            js_file.write(js.strip())

    # Write README file
    with open(os.path.join(folder, "README.md"), "w") as readme_file:
        readme_file.write(readme.strip())


def create_course_files(course_content):
    for week, exercises in course_content.items():
        for exercise in exercises:
            exercise_name = exercise["name"]

            exercise_dir = os.path.join(ROOT, week, exercise_name, "exercise")
            os.makedirs(exercise_dir, exist_ok=True)

            create_week_files(exercise_dir, None, None, None, exercise["readme"])

            solution_dir = os.path.join(
                ROOT,
                week,
                exercise_name,
                "solution",
            )
            os.makedirs(solution_dir, exist_ok=True)

            html = exercise["html"] if "html" in exercise else ""
            js = exercise["js"] if "js" in exercise else None
            css = exercise["css"] if "css" in exercise else None

            print(f"create {solution_dir} ({len(html)})")

            create_week_files(solution_dir, html, css, js, exercise["readme"])


# Call the function to create the course files and zip them
create_course_files(course_content)
