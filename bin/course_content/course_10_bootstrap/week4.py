course_content = {
    "Week4": [
        {
            "name": "Alerts",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alerts</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <h1>Alerts</h1>
    <div class="alert alert-primary" role="alert">
        This is a primary alert—check it out!
    </div>
    <div class="alert alert-secondary" role="alert">
        This is a secondary alert—check it out!
    </div>
    <div class="alert alert-success" role="alert">
        This is a success alert—check it out!
    </div>
    <div class="alert alert-danger" role="alert">
        This is a danger alert—check it out!
    </div>
    <div class="alert alert-warning" role="alert">
        This is a warning alert—check it out!
    </div>
    <div class="alert alert-info" role="alert">
        This is an info alert—check it out!
    </div>
    <div class="alert alert-light" role="alert">
        This is a light alert—check it out!
    </div>
    <div class="alert alert-dark" role="alert">
        This is a dark alert—check it out!
    </div>
</body>
</html>
        """,
            "readme": """
# Alerts

This example demonstrates how to use Bootstrap's alert classes.

## HTML Code
The HTML file includes several alert boxes with different styles using Bootstrap's alert classes.
        """,
        },
        {
            "name": "Badges",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Badges</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <h1>Badges</h1>
    <h2>Example heading <span class="badge badge-secondary">New</span></h2>
    <button type="button" class="btn btn-primary">
        Notifications <span class="badge badge-light">4</span>
    </button>
</body>
</html>
        """,
            "readme": """
# Badges

This example demonstrates how to use Bootstrap's badge classes.

## HTML Code
The HTML file includes headings and buttons with badges using Bootstrap's badge classes.
        """,
        },
        {
            "name": "Breadcrumbs",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Breadcrumbs</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <h1>Breadcrumbs</h1>
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="#">Home</a></li>
            <li class="breadcrumb-item"><a href="#">Library</a></li>
            <li class="breadcrumb-item active" aria-current="page">Data</li>
        </ol>
    </nav>
</body>
</html>
        """,
            "readme": """
# Breadcrumbs

This example demonstrates how to use Bootstrap's breadcrumb classes.

## HTML Code
The HTML file includes a breadcrumb navigation using Bootstrap's breadcrumb classes.
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
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <h1>Cards</h1>
    <div class="card" style="width: 18rem;">
        <img src="https://via.placeholder.com/150" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
    </div>
</body>
</html>
        """,
            "readme": """
# Cards

This example demonstrates how to use Bootstrap's card classes.

## HTML Code
The HTML file includes a card with an image, title, text, and a button using Bootstrap's card classes.
        """,
        },
        {
            "name": "Modals",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modals</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
        <script src="/lib/jquery/3.7.1/js/jquery-3.7.1.slim.min.js"></script>
    <script src="/lib/popperjs/2.11.8/js/popperjs-2.11.min.js"></script>
    <script src="/lib/bootstrap/5.3.3/js/bootstrap.min.js"></script>
</head>
<body>
    <h1>Modals</h1>
    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
        Launch demo modal
    </button>
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    This is the content of the modal.
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
        """,
            "readme": """
# Modals

This example demonstrates how to use Bootstrap's modal classes.

## HTML Code
The HTML file includes a button that triggers a modal using Bootstrap's modal classes.
        """,
        },
    ]
}
