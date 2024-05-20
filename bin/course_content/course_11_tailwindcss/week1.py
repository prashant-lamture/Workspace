course_content = {
    "Week1": [
        {
            "name": "Setup TailwindCSS",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Setup TailwindCSS</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <h1 class="text-4xl font-bold text-center text-blue-500">Hello, TailwindCSS!</h1>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("TailwindCSS Setup Complete");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Setup TailwindCSS

This example demonstrates how to set up TailwindCSS in an HTML document.

## HTML Code
The HTML file includes a link to the TailwindCSS file and displays a centered heading.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Responsive Design",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Design</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="container mx-auto p-4">
        <div class="md:flex">
            <div class="md:flex-shrink-0">
                <img class="rounded-lg md:w-56" src="https://via.placeholder.com/150" alt="Placeholder Image">
            </div>
            <div class="mt-4 md:mt-0 md:ml-6">
                <div class="uppercase tracking-wide text-sm text-indigo-600 font-bold">TailwindCSS</div>
                <p class="block mt-1 text-lg leading-tight font-semibold text-gray-900">Responsive Design Example</p>
                <p class="mt-2 text-gray-600">This example demonstrates how to use TailwindCSS for responsive design.</p>
            </div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Responsive Design Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Responsive Design

This example demonstrates how to use TailwindCSS for responsive design.

## HTML Code
The HTML file includes a responsive layout with an image and text content.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Utility First",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Utility First</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="p-4 max-w-sm mx-auto bg-white rounded-xl shadow-md space-y-4">
        <div class="flex items-center space-x-4">
            <div class="shrink-0">
                <img class="h-12 w-12" src="https://via.placeholder.com/150" alt="Placeholder Image">
            </div>
            <div>
                <div class="text-xl font-medium text-black">TailwindCSS</div>
                <p class="text-gray-500">Utility First Example</p>
            </div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Utility First Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Utility First

This example demonstrates how to use TailwindCSS utility-first classes.

## HTML Code
The HTML file includes a card component styled using TailwindCSS utility classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Flexbox Layout",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flexbox Layout</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="flex space-x-4 p-4">
        <div class="flex-1 p-4 bg-blue-500 text-white">Flex Item 1</div>
        <div class="flex-1 p-4 bg-green-500 text-white">Flex Item 2</div>
        <div class="flex-1 p-4 bg-red-500 text-white">Flex Item 3</div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Flexbox Layout Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Flexbox Layout

This example demonstrates how to use TailwindCSS flexbox utilities.

## HTML Code
The HTML file includes a flexbox layout with three flex items.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Grid Layout",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grid Layout</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="grid grid-cols-3 gap-4 p-4">
        <div class="p-4 bg-blue-500 text-white">Grid Item 1</div>
        <div class="p-4 bg-green-500 text-white">Grid Item 2</div>
        <div class="p-4 bg-red-500 text-white">Grid Item 3</div>
        <div class="p-4 bg-purple-500 text-white">Grid Item 4</div>
        <div class="p-4 bg-yellow-500 text-white">Grid Item 5</div>
        <div class="p-4 bg-pink-500 text-white">Grid Item 6</div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Grid Layout Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Grid Layout

This example demonstrates how to use TailwindCSS grid utilities.

## HTML Code
The HTML file includes a grid layout with six grid items.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
    ],
    # Continue the same pattern for Week 2 to Week 8 with appropriate examples
}
