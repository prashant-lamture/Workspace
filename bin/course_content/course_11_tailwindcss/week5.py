course_content = {
    "Week5": [
        {
            "name": "Responsive Grids",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Grids</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="container mx-auto p-8">
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            <div class="bg-blue-500 text-white p-4">Item 1</div>
            <div class="bg-green-500 text-white p-4">Item 2</div>
            <div class="bg-red-500 text-white p-4">Item 3</div>
            <div class="bg-purple-500 text-white p-4">Item 4</div>
            <div class="bg-yellow-500 text-white p-4">Item 5</div>
            <div class="bg-pink-500 text-white p-4">Item 6</div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Responsive Grids Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Responsive Grids

This example demonstrates how to create responsive grids using TailwindCSS utilities.

## HTML Code
The HTML file includes a responsive grid layout with six items styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Flexbox Utilities",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flexbox Utilities</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="container mx-auto p-8">
        <div class="flex space-x-4">
            <div class="flex-1 p-4 bg-blue-500 text-white">Flex Item 1</div>
            <div class="flex-1 p-4 bg-green-500 text-white">Flex Item 2</div>
            <div class="flex-1 p-4 bg-red-500 text-white">Flex Item 3</div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Flexbox Utilities Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Flexbox Utilities

This example demonstrates how to use TailwindCSS flexbox utilities.

## HTML Code
The HTML file includes a flexbox layout with three flex items styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Buttons with Icons",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buttons with Icons</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="container mx-auto p-8">
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded inline-flex items-center">
            <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
            <span>Button with Icon</span>
        </button>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Buttons with Icons Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Buttons with Icons

This example demonstrates how to create buttons with icons using TailwindCSS utilities.

## HTML Code
The HTML file includes a button with an icon styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Image Gallery",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="container mx-auto p-8">
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            <img class="w-full h-48 object-cover" src="https://via.placeholder.com/150" alt="Gallery Image 1">
            <img class="w-full h-48 object-cover" src="https://via.placeholder.com/150" alt="Gallery Image 2">
            <img class="w-full h-48 object-cover" src="https://via.placeholder.com/150" alt="Gallery Image 3">
            <img class="w-full h-48 object-cover" src="https://via.placeholder.com/150" alt="Gallery Image 4">
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Image Gallery Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Image Gallery

This example demonstrates how to create an image gallery using TailwindCSS utilities.

## HTML Code
The HTML file includes an image gallery with four images styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Notifications",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notifications</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="container mx-auto p-8">
        <div class="bg-green-500 text-white p-4 rounded mb-4">
            <p class="font-bold">Success!</p>
            <p>Your operation was successful.</p>
        </div>
        <div class="bg-red-500 text-white p-4 rounded mb-4">
            <p class="font-bold">Error!</p>
            <p>There was an error processing your request.</p>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Notifications Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Notifications

This example demonstrates how to create notifications using TailwindCSS utilities.

## HTML Code
The HTML file includes success and error notifications styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
    ]
}
