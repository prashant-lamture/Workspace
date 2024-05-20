course_content = {
    "Week3": [
        {
            "name": "Setting_Up_Bootstrap",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bootstrap Setup</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <h1 class="text-center">Hello, Bootstrap!</h1>
</body>
</html>
        """,
            "readme": """
# Setting Up Bootstrap

This example demonstrates how to set up Bootstrap in an HTML document.

## HTML Code
The HTML file includes a link to the Bootstrap CSS file using a CDN and displays a centered heading.
        """,
        },
        {
            "name": "Basic_Grid_Layout",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Grid Layout</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-sm-4">Column 1</div>
            <div class="col-sm-4">Column 2</div>
            <div class="col-sm-4">Column 3</div>
        </div>
    </div>
</body>
</html>
        """,
            "readme": """
# Basic Grid Layout

This example demonstrates how to create a basic grid layout using Bootstrap.

## HTML Code
The HTML file includes a container with a row and three columns, each taking up one-third of the row's width.
        """,
        },
        {
            "name": "Responsive_Grid_Layout",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Grid Layout</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-6 col-lg-4">Column 1</div>
            <div class="col-md-6 col-lg-4">Column 2</div>
            <div class="col-md-6 col-lg-4">Column 3</div>
        </div>
    </div>
</body>
</html>
        """,
            "readme": """
# Responsive Grid Layout

This example demonstrates how to create a responsive grid layout using Bootstrap.

## HTML Code
The HTML file includes a container with a row and three columns, which adjust their size based on the screen width.
        """,
        },
        {
            "name": "Nested_Grid_Layout",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nested Grid Layout</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                Column 1
                <div class="row">
                    <div class="col-6">Nested 1</div>
                    <div class="col-6">Nested 2</div>
                </div>
            </div>
            <div class="col-md-6">Column 2</div>
        </div>
    </div>
</body>
</html>
        """,
            "readme": """
# Nested Grid Layout

This example demonstrates how to create a nested grid layout using Bootstrap.

## HTML Code
The HTML file includes a container with a row and two columns, where the first column contains a nested row with two columns.
        """,
        },
        {
            "name": "Offset_Columns",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Offset Columns</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-4 offset-md-4">Centered Column</div>
        </div>
    </div>
</body>
</html>
        """,
            "readme": """
# Offset Columns

This example demonstrates how to use offset classes to center a column using Bootstrap.

## HTML Code
The HTML file includes a container with a row and a single column that is offset to the center using Bootstrap offset classes.
        """,
        },
    ]
}
