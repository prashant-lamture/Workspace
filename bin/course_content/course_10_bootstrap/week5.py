course_content = {
    "Week5": [
        {
            "name": "Navbar",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Navbar</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Features</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Pricing</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
                </li>
            </ul>
        </div>
    </nav>
</body>
</html>
        """,
            "readme": """
# Navbar

This example demonstrates how to create a responsive navbar using Bootstrap's navbar classes.

## HTML Code
The HTML file includes a navbar with links and a toggle button for responsive behavior using Bootstrap's navbar classes.
        """,
        },
        {
            "name": "Dropdowns",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dropdowns</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
        <script src="/lib/jquery/3.7.1/js/jquery-3.7.1.slim.min.js"></script>
    <script src="/lib/popperjs/2.11.8/js/popperjs-2.11.min.js"></script>
    <script src="/lib/bootstrap/5.3.3/js/bootstrap.min.js"></script>
</head>
<body>
    <h1>Dropdowns</h1>
    <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Dropdown button
        </button>
        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <a class="dropdown-item" href="#">Action</a>
            <a class="dropdown-item" href="#">Another action</a>
            <a class="dropdown-item" href="#">Something else here</a>
        </div>
    </div>
</body>
</html>
        """,
            "readme": """
# Dropdowns

This example demonstrates how to create a dropdown menu using Bootstrap's dropdown classes.

## HTML Code
The HTML file includes a button that triggers a dropdown menu using Bootstrap's dropdown classes.
        """,
        },
        {
            "name": "Navs_and_Tabs",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Navs and Tabs</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <h1>Navs and Tabs</h1>
    <ul class="nav nav-tabs" id="myTab" role="tablist">
        <li class="nav-item">
            <a class="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">Home</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" id="profile-tab" data-toggle="tab" href="#profile" role="tab" aria-controls="profile" aria-selected="false">Profile</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" id="contact-tab" data-toggle="tab" href="#contact" role="tab" aria-controls="contact" aria-selected="false">Contact</a>
        </li>
    </ul>
    <div class="tab-content" id="myTabContent">
        <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">Home content...</div>
        <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">Profile content...</div>
        <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">Contact content...</div>
    </div>
</body>
</html>
        """,
            "readme": """
# Navs and Tabs

This example demonstrates how to create navigational tabs using Bootstrap's nav and tab classes.

## HTML Code
The HTML file includes a set of tabs and corresponding tab content using Bootstrap's nav and tab classes.
        """,
        },
        {
            "name": "Pagination",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pagination</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <h1>Pagination</h1>
    <nav aria-label="Page navigation example">
        <ul class="pagination">
            <li class="page-item"><a class="page-link" href="#">Previous</a></li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item"><a class="page-link" href="#">Next</a></li>
        </ul>
    </nav>
</body>
</html>
        """,
            "readme": """
# Pagination

This example demonstrates how to create pagination using Bootstrap's pagination classes.

## HTML Code
The HTML file includes a pagination component using Bootstrap's pagination classes.
        """,
        },
        {
            "name": "Progress_Bars",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Progress Bars</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <h1>Progress Bars</h1>
    <div class="progress">
        <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">25%</div>
    </div>
    <div class="progress mt-3">
        <div class="progress-bar bg-success" role="progressbar" style="width: 50%;" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">50%</div>
    </div>
    <div class="progress mt-3">
        <div class="progress-bar bg-info" role="progressbar" style="width: 75%;" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">75%</div>
    </div>
    <div class="progress mt-3">
        <div class="progress-bar bg-warning" role="progressbar" style="width: 100%;" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100">100%</div>
    </div>
</body>
</html>
        """,
            "readme": """
# Progress Bars

This example demonstrates how to create progress bars using Bootstrap's progress bar classes.

## HTML Code
The HTML file includes several progress bars with different styles and colors using Bootstrap's progress bar classes.
        """,
        },
    ]
}
