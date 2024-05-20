course_content = {
    "Week2": [
        {
            "name": "Typography",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Typography</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <h1 class="text-4xl font-bold">Heading 1</h1>
    <h2 class="text-3xl font-semibold">Heading 2</h2>
    <p class="text-lg">This is a paragraph with large text.</p>
    <p class="text-sm">This is a paragraph with small text.</p>
    <a href="#" class="text-blue-500 underline">This is a link</a>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Typography Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Typography

This example demonstrates how to use TailwindCSS typography utilities.

## HTML Code
The HTML file includes various text elements styled with TailwindCSS typography classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Buttons",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buttons</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Button 1</button>
    <button class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">Button 2</button>
    <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">Button 3</button>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Buttons Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Buttons

This example demonstrates how to use TailwindCSS button utilities.

## HTML Code
The HTML file includes buttons styled with TailwindCSS button classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Forms",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forms</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <form class="w-full max-w-lg">
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-first-name">
                    First Name
                </label>
                <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-first-name" type="text" placeholder="Jane">
            </div>
            <div class="w-full md:w-1/2 px-3">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-last-name">
                    Last Name
                </label>
                <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-last-name" type="text" placeholder="Doe">
            </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full px-3">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-password">
                    Password
                </label>
                <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-password" type="password" placeholder="******************">
            </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full px-3">
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" type="button">
                    Sign Up
                </button>
            </div>
        </div>
    </form>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Forms Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Forms

This example demonstrates how to use TailwindCSS form utilities.

## HTML Code
The HTML file includes a form styled with TailwindCSS form classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Cards",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cards</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="max-w-sm rounded overflow-hidden shadow-lg">
        <img class="w-full" src="https://via.placeholder.com/150" alt="Placeholder Image">
        <div class="px-6 py-4">
            <div class="font-bold text-xl mb-2">Card Title</div>
            <p class="text-gray-700 text-base">
                This is a simple card with an image, title, and description.
            </p>
        </div>
        <div class="px-6 pt-4 pb-2">
            <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#tag1</span>
            <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#tag2</span>
            <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#tag3</span>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Cards Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Cards

This example demonstrates how to use TailwindCSS card utilities.

## HTML Code
The HTML file includes a card component styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Tables",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tables</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <table class="min-w-full divide-y divide-gray-200">
        <thead>
            <tr>
                <th class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                <th class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Title</th>
                <th class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                <th class="px-6 py-3 bg-gray-50"></th>
            </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
            <tr>
                <td class="px-6 py-4 whitespace-nowrap">John Doe</td>
                <td class="px-6 py-4 whitespace-nowrap">Software Engineer</td>
                <td class="px-6 py-4 whitespace-nowrap">Active</td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                    <a href="#" class="text-indigo-600 hover:text-indigo-900">Edit</a>
                </td>
            </tr>
            <tr>
                <td class="px-6 py-4 whitespace-nowrap">Jane Smith</td>
                <td class="px-6 py-4 whitespace-nowrap">Product Manager</td>
                <td class="px-6 py-4 whitespace-nowrap">Inactive</td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                    <a href="#" class="text-indigo-600 hover:text-indigo-900">Edit</a>
                </td>
            </tr>
        </tbody>
    </table>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Tables Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Tables

This example demonstrates how to use TailwindCSS table utilities.

## HTML Code
The HTML file includes a table styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
    ]
}
