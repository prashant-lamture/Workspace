course_content = {
    "Week3": [
        {
            "name": "Navigation Bars",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Navigation Bars</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <nav class="bg-gray-800 p-4">
        <div class="container mx-auto flex justify-between items-center">
            <a href="#" class="text-white text-lg font-bold">Brand</a>
            <div>
                <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Home</a>
                <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">About</a>
                <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Services</a>
                <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Contact</a>
            </div>
        </div>
    </nav>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Navigation Bars Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Navigation Bars

This example demonstrates how to create a navigation bar using TailwindCSS utilities.

## HTML Code
The HTML file includes a navigation bar styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Footers",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Footers</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <footer class="bg-gray-800 text-white p-4 mt-8">
        <div class="container mx-auto text-center">
            <p>&copy; 2024 Your Company. All rights reserved.</p>
            <div class="flex justify-center mt-2">
                <a href="#" class="text-gray-400 hover:text-white mx-2">Privacy Policy</a>
                <a href="#" class="text-gray-400 hover:text-white mx-2">Terms of Service</a>
                <a href="#" class="text-gray-400 hover:text-white mx-2">Contact Us</a>
            </div>
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
console.log("Footers Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Footers

This example demonstrates how to create a footer using TailwindCSS utilities.

## HTML Code
The HTML file includes a footer styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Cards with Images",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cards with Images</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="max-w-sm rounded overflow-hidden shadow-lg m-4">
        <img class="w-full" src="https://via.placeholder.com/400" alt="Placeholder Image">
        <div class="px-6 py-4">
            <div class="font-bold text-xl mb-2">Card Title</div>
            <p class="text-gray-700 text-base">
                This is a card with an image, title, and description.
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
console.log("Cards with Images Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Cards with Images

This example demonstrates how to create a card with an image using TailwindCSS utilities.

## HTML Code
The HTML file includes a card component with an image, title, and tags styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Modal Dialogs",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modal Dialogs</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <div class="flex items-center justify-center h-screen">
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onclick="toggleModal()">Open Modal</button>
    </div>
    <div class="fixed z-10 inset-0 overflow-y-auto hidden" id="myModal">
        <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
            <div class="fixed inset-0 transition-opacity" aria-hidden="true">
                <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
            </div>
            <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
            <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                    <div class="sm:flex sm:items-start">
                        <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                            <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                                Modal Title
                            </h3>
                            <div class="mt-2">
                                <p class="text-sm text-gray-500">
                                    This is a simple modal dialog.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                    <button type="button" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-500 text-base font-medium text-white hover:bg-blue-700 sm:ml-3 sm:w-auto sm:text-sm" onclick="toggleModal()">
                        Close
                    </button>
                </div>
            </div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
function toggleModal() {
    const modal = document.getElementById('myModal');
    modal.classList.toggle('hidden');
}
console.log("Modal Dialogs Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Modal Dialogs

This example demonstrates how to create a modal dialog using TailwindCSS utilities.

## HTML Code
The HTML file includes a button that triggers a modal dialog styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file includes a function to toggle the modal visibility and logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
        {
            "name": "Forms with Validation",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forms with Validation</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="styles.css" rel="stylesheet">
</head>
<body>
    <form class="w-full max-w-lg mx-auto mt-8">
        <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
                Username
            </label>
            <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Username">
            <p class="text-red-500 text-xs italic hidden" id="usernameError">Please enter a username.</p>
        </div>
        <div class="mb-6">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
                Password
            </label>
            <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************">
            <p class="text-red-500 text-xs italic hidden" id="passwordError">Please enter a password.</p>
        </div>
        <div class="flex items-center justify-between">
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button" onclick="validateForm()">
                Sign In
            </button>
        </div>
    </form>
    <script src="script.js"></script>
</body>
</html>
            """,
            "js": """
function validateForm() {
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    const usernameError = document.getElementById('usernameError');
    const passwordError = document.getElementById('passwordError');
    
    if (username.value === '') {
        usernameError.classList.remove('hidden');
    } else {
        usernameError.classList.add('hidden');
    }

    if (password.value === '') {
        passwordError.classList.remove('hidden');
    } else {
        passwordError.classList.add('hidden');
    }
}

console.log("Forms with Validation Example Loaded");
            """,
            "css": """
@tailwind base;
@tailwind components;
@tailwind utilities;
            """,
            "readme": """
# Forms with Validation

This example demonstrates how to create a form with validation using TailwindCSS utilities.

## HTML Code
The HTML file includes a form with validation messages styled with TailwindCSS classes.

## JavaScript Code
The JavaScript file includes a function to validate the form and logs a message to the console.

## CSS Code
The CSS file imports TailwindCSS base, components, and utilities.
            """,
        },
    ]
}
