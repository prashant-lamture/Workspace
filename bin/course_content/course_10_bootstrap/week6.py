course_content = {
    "Week6": [
        {
            "name": "Tooltips",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tooltips</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
        <script src="/lib/jquery/3.7.1/js/jquery-3.7.1.slim.min.js"></script>
    <script src="/lib/popperjs/2.11.8/js/popperjs-2.11.min.js"></script>
    <script src="/lib/bootstrap/5.3.3/js/bootstrap.min.js"></script>
    <script>
        $(function () {
            $('[data-toggle="tooltip"]').tooltip()
        })
    </script>
</head>
<body>
    <h1>Tooltips</h1>
    <button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="top" title="Tooltip on top">
        Tooltip on top
    </button>
    <button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="right" title="Tooltip on right">
        Tooltip on right
    </button>
    <button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="bottom" title="Tooltip on bottom">
        Tooltip on bottom
    </button>
    <button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="left" title="Tooltip on left">
        Tooltip on left
    </button>
</body>
</html>
        """,
            "readme": """
# Tooltips

This example demonstrates how to create tooltips using Bootstrap's tooltip classes.

## HTML Code
The HTML file includes buttons with tooltips that appear on different sides using Bootstrap's tooltip classes.
        """,
        },
        {
            "name": "Popovers",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Popovers</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
        <script src="/lib/jquery/3.7.1/js/jquery-3.7.1.slim.min.js"></script>
    <script src="/lib/popperjs/2.11.8/js/popperjs-2.11.min.js"></script>
    <script src="/lib/bootstrap/5.3.3/js/bootstrap.min.js"></script>
    <script>
        $(function () {
            $('[data-toggle="popover"]').popover()
        })
    </script>
</head>
<body>
    <h1>Popovers</h1>
    <button type="button" class="btn btn-lg btn-danger" data-toggle="popover" title="Popover title" data-content="And here's some amazing content. It's very engaging. Right?">
        Click to toggle popover
    </button>
</body>
</html>
        """,
            "readme": """
# Popovers

This example demonstrates how to create popovers using Bootstrap's popover classes.

## HTML Code
The HTML file includes a button that triggers a popover using Bootstrap's popover classes.
        """,
        },
        {
            "name": "Carousel",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carousel</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
        <script src="/lib/jquery/3.7.1/js/jquery-3.7.1.slim.min.js"></script>
    <script src="/lib/popperjs/2.11.8/js/popperjs-2.11.min.js"></script>
    <script src="/lib/bootstrap/5.3.3/js/bootstrap.min.js"></script>
</head>
<body>
    <h1>Carousel</h1>
    <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="https://via.placeholder.com/800x400" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
                <img src="https://via.placeholder.com/800x400" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
                <img src="https://via.placeholder.com/800x400" class="d-block w-100" alt="...">
            </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
    </div>
</body>
</html>
        """,
            "readme": """
# Carousel

This example demonstrates how to create a carousel using Bootstrap's carousel classes.

## HTML Code
The HTML file includes a carousel with multiple items using Bootstrap's carousel classes.
        """,
        },
        {
            "name": "Collapse",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Collapse</title>
    <link href="https://stackpath.amazonaws.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <script src="/lib/jquery/3.7.1/js/jquery-3.7.1.slim.min.js"></script>
    <script src="/lib/popperjs/2.11.8/js/popperjs-2.11.min.js"></script>
    <script src="/lib/bootstrap/5.3.3/js/bootstrap.min.js"></script>
</head>
<body>
    <h1>Collapse</h1>
    <p>
        <a class="btn btn-primary" data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
            Link with href
        </a>
        <button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
            Button with data-target
        </button>
    </p>
    <div class="collapse" id="collapseExample">
        <div class="card card-body">
            Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
        </div>
    </div>
</body>
</html>
        """,
            "readme": """
# Collapse

This example demonstrates how to create a collapsible element using Bootstrap's collapse classes.

## HTML Code
The HTML file includes links and buttons that trigger a collapsible element using Bootstrap's collapse classes.
        """,
        },
        {
            "name": "Scrollspy",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scrollspy</title>
    <link href="https://stackpath.amazonaws.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <script src="/lib/jquery/3.7.1/js/jquery-3.7.1.slim.min.js"></script>
    <script src="/lib/popperjs/2.11.8/js/popperjs-2.11.min.js"></script>
    <script src="/lib/bootstrap/5.3.3/js/bootstrap.min.js"></script>
    <style>
        body {
            position: relative;
        }
        .scrollspy-example {
            position: relative;
            height: 200px;
            margin-top: .5rem;
            overflow: auto;
        }
    </style>
</head>
<body data-spy="scroll" data-target="#navbar-example2" data-offset="0">
    <h1>Scrollspy</h1>
    <nav id="navbar-example2" class="navbar navbar-light bg-light">
        <a class="navbar-brand" href="#">Navbar</a>
        <ul class="nav nav-pills">
            <li class="nav-item">
                <a class="nav-link" href="#fat">@fat</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#mdo">@mdo</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#one">one</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#two">two</a>
            </li>
        </ul>
    </nav>
    <div class="scrollspy-example">
        <h4 id="fat">@fat</h4>
        <p>...</p>
        <h4 id="mdo">@mdo</h4>
        <p>...</p>
        <h4 id="one">one</h4>
        <p>...</p>
        <h4 id="two">two</h4>
        <p>...</p>
    </div>
</body>
</html>
        """,
            "readme": """
# Scrollspy

This example demonstrates how to use Bootstrap's scrollspy classes to automatically update nav targets based on scroll position.

## HTML Code
The HTML file includes a navbar and a scrollable content area using Bootstrap's scrollspy classes.
        """,
        },
    ]
}
