course_content = {
    "Week6": [
        {
            "name": "Responsive Grids",
            "html": '\n<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Responsive Grids</title>\n    <script src="https://cdn.tailwindcss.com"></script>    <link href="styles.css" rel="stylesheet">\n</head>\n<body>\n    <div class="container mx-auto p-8">\n        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">\n            <div class="bg-blue-500 text-white p-4">Item 1</div>\n            <div class="bg-green-500 text-white p-4">Item 2</div>\n            <div class="bg-red-500 text-white p-4">Item 3</div>\n            <div class="bg-purple-500 text-white p-4">Item 4</div>\n            <div class="bg-yellow-500 text-white p-4">Item 5</div>\n            <div class="bg-pink-500 text-white p-4">Item 6</div>\n        </div>\n    </div>\n    <script src="script.js"></script>\n</body>\n</html>\n            ',
            "js": '\nconsole.log("Responsive Grids Example Loaded");\n            ',
            "css": "\n@tailwind base;\n@tailwind components;\n@tailwind utilities;\n            ",
            "readme": "\n# Responsive Grids\n\nThis example demonstrates how to create responsive grids using TailwindCSS utilities.\n\n## HTML Code\nThe HTML file includes a responsive grid layout with six items styled with TailwindCSS classes.\n\n## JavaScript Code\nThe JavaScript file logs a message to the console.\n\n## CSS Code\nThe CSS file imports TailwindCSS base, components, and utilities.\n            ",
        },
        {
            "name": "Flexbox Utilities",
            "html": '\n<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Flexbox Utilities</title>\n    <script src="https://cdn.tailwindcss.com"></script>    <link href="styles.css" rel="stylesheet">\n</head>\n<body>\n    <div class="container mx-auto p-8">\n        <div class="flex space-x-4">\n            <div class="flex-1 p-4 bg-blue-500 text-white">Flex Item 1</div>\n            <div class="flex-1 p-4 bg-green-500 text-white">Flex Item 2</div>\n            <div class="flex-1 p-4 bg-red-500 text-white">Flex Item 3</div>\n        </div>\n    </div>\n    <script src="script.js"></script>\n</body>\n</html>\n            ',
            "js": '\nconsole.log("Flexbox Utilities Example Loaded");\n            ',
            "css": "\n@tailwind base;\n@tailwind components;\n@tailwind utilities;\n            ",
            "readme": "\n# Flexbox Utilities\n\nThis example demonstrates how to use TailwindCSS flexbox utilities.\n\n## HTML Code\nThe HTML file includes a flexbox layout with three flex items styled with TailwindCSS classes.\n\n## JavaScript Code\nThe JavaScript file logs a message to the console.\n\n## CSS Code\nThe CSS file imports TailwindCSS base, components, and utilities.\n            ",
        },
        {
            "name": "Buttons with Icons",
            "html": '\n<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Buttons with Icons</title>\n    <script src="https://cdn.tailwindcss.com"></script>    <link href="styles.css" rel="stylesheet">\n</head>\n<body>\n    <div class="container mx-auto p-8">\n        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded inline-flex items-center">\n            <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>\n            <span>Button with Icon</span>\n        </button>\n    </div>\n    <script src="script.js"></script>\n</body>\n</html>\n            ',
            "js": '\nconsole.log("Buttons with Icons Example Loaded");\n            ',
            "css": "\n@tailwind base;\n@tailwind components;\n@tailwind utilities;\n            ",
            "readme": "\n# Buttons with Icons\n\nThis example demonstrates how to create buttons with icons using TailwindCSS utilities.\n\n## HTML Code\nThe HTML file includes a button with an icon styled with TailwindCSS classes.\n\n## JavaScript Code\nThe JavaScript file logs a message to the console.\n\n## CSS Code\nThe CSS file imports TailwindCSS base, components, and utilities.\n            ",
        },
        {
            "name": "Image Gallery",
            "html": '\n<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Image Gallery</title>\n    <script src="https://cdn.tailwindcss.com"></script>    <link href="styles.css" rel="stylesheet">\n</head>\n<body>\n    <div class="container mx-auto p-8">\n        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">\n            <img class="w-full h-48 object-cover" src="https://via.placeholder.com/150" alt="Gallery Image 1">\n            <img class="w-full h-48 object-cover" src="https://via.placeholder.com/150" alt="Gallery Image 2">\n            <img class="w-full h-48 object-cover" src="https://via.placeholder.com/150" alt="Gallery Image 3">\n            <img class="w-full h-48 object-cover" src="https://via.placeholder.com/150" alt="Gallery Image 4">\n        </div>\n    </div>\n    <script src="script.js"></script>\n</body>\n</html>\n            ',
            "js": '\nconsole.log("Image Gallery Example Loaded");\n            ',
            "css": "\n@tailwind base;\n@tailwind components;\n@tailwind utilities;\n            ",
            "readme": "\n# Image Gallery\n\nThis example demonstrates how to create an image gallery using TailwindCSS utilities.\n\n## HTML Code\nThe HTML file includes an image gallery with four images styled with TailwindCSS classes.\n\n## JavaScript Code\nThe JavaScript file logs a message to the console.\n\n## CSS Code\nThe CSS file imports TailwindCSS base, components, and utilities.\n            ",
        },
        {
            "name": "Notifications",
            "html": '\n<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Notifications</title>\n    <script src="https://cdn.tailwindcss.com"></script>    <link href="styles.css" rel="stylesheet">\n</head>\n<body>\n    <div class="container mx-auto p-8">\n        <div class="bg-green-500 text-white p-4 rounded mb-4">\n            <p class="font-bold">Success!</p>\n            <p>Your operation was successful.</p>\n        </div>\n        <div class="bg-red-500 text-white p-4 rounded mb-4">\n            <p class="font-bold">Error!</p>\n            <p>There was an error processing your request.</p>\n        </div>\n    </div>\n    <script src="script.js"></script>\n</body>\n</html>\n            ',
            "js": '\nconsole.log("Notifications Example Loaded");\n            ',
            "css": "\n@tailwind base;\n@tailwind components;\n@tailwind utilities;\n            ",
            "readme": "\n# Notifications\n\nThis example demonstrates how to create notifications using TailwindCSS utilities.\n\n## HTML Code\nThe HTML file includes success and error notifications styled with TailwindCSS classes.\n\n## JavaScript Code\nThe JavaScript file logs a message to the console.\n\n## CSS Code\nThe CSS file imports TailwindCSS base, components, and utilities.\n            ",
        },
    ]
}
