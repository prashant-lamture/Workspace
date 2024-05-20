course_content = {
    "Week4": [
        {
            "name": "Hero Sections",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hero Sections</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="bg-gray-800 text-white p-8">
        <div class="container mx-auto text-center">
            <h1 class="text-4xl font-bold">Welcome to Our Website</h1>
            <p class="mt-4">This is the hero section of our website. It includes a title and a description.</p>
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4">Get Started</button>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Hero Sections Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Hero Sections

This example demonstrates how to create a hero section using TailwindCSS utilities.

## HTML Code
The HTML file includes a hero section with a title, description, and a button styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Pricing Tables",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pricing Tables</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="container mx-auto p-8">
        <div class="max-w-sm mx-auto bg-white rounded-lg shadow-md overflow-hidden">
            <div class="p-6">
                <h2 class="text-2xl font-bold mb-4">Basic Plan</h2>
                <p class="text-gray-700 mb-4">$9.99 / month</p>
                <ul class="list-disc list-inside text-gray-700 mb-4">
                    <li>Feature 1</li>
                    <li>Feature 2</li>
                    <li>Feature 3</li>
                </ul>
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Choose Plan</button>
            </div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Pricing Tables Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Pricing Tables

This example demonstrates how to create a pricing table using TailwindCSS utilities.

## HTML Code
The HTML file includes a pricing table with a title, price, features list, and a button styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Testimonials",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Testimonials</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="container mx-auto p-8">
        <div class="max-w-xl mx-auto bg-white rounded-lg shadow-md overflow-hidden">
            <div class="p-6">
                <p class="text-gray-700 mb-4">"This is a testimonial. The product is great!"</p>
                <div class="flex items-center">
                    <img class="h-10 w-10 rounded-full mr-4" src="https://via.placeholder.com/150" alt="Avatar">
                    <div>
                        <p class="text-gray-900 font-bold">John Doe</p>
                        <p class="text-gray-600">CEO, Company</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Testimonials Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Testimonials

This example demonstrates how to create a testimonial section using TailwindCSS utilities.

## HTML Code
The HTML file includes a testimonial section with text and an avatar styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Blog Cards",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Cards</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="container mx-auto p-8">
        <div class="max-w-sm mx-auto bg-white rounded-lg shadow-md overflow-hidden">
            <img class="w-full h-48 object-cover" src="https://via.placeholder.com/400" alt="Blog Image">
            <div class="p-6">
                <h2 class="text-2xl font-bold mb-2">Blog Post Title</h2>
                <p class="text-gray-700 mb-4">This is a summary of the blog post. It gives an overview of the content.</p>
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Read More</button>
            </div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Blog Cards Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Blog Cards

This example demonstrates how to create a blog card using TailwindCSS utilities.

## HTML Code
The HTML file includes a blog card with an image, title, summary, and a button styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Feature Sections",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feature Sections</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="container mx-auto p-8">
        <div class="flex items-center">
            <div class="w-1/2 p-4">
                <h2 class="text-2xl font-bold mb-2">Feature Title</h2>
                <p class="text-gray-700 mb-4">This is a description of the feature. It highlights the benefits and uses.</p>
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Learn More</button>
            </div>
            <div class="w-1/2 p-4">
                <img class="w-full h-48 object-cover" src="https://via.placeholder.com/400" alt="Feature Image">
            </div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Feature Sections Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Feature Sections

This example demonstrates how to create a feature section using TailwindCSS utilities.

## HTML Code
The HTML file includes a feature section with text and an image styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
    ]
}
