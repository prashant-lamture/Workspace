course_content = {
    "Week8": [
        # Create directories and files for Week 8 examples
        {
            "name": "Spinners",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spinners</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <h1>Spinners</h1>
    <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
    </div>
    <div class="spinner-grow" role="status">
        <span class="sr-only">Loading...</span>
    </div>
</body>
</html>
        """,
            "readme": """
# Spinners

This example demonstrates how to use Bootstrap's spinner classes.

## HTML Code
The HTML file includes two types of spinners using Bootstrap's spinner classes.
        """,
        },
        {
            "name": "Toasts",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toasts</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
        <script src="/lib/jquery/3.7.1/js/jquery-3.7.1.slim.min.js"></script>
    <script src="/lib/popperjs/2.11.8/js/popperjs-2.11.min.js"></script>
    <script src="/lib/bootstrap/5.3.3/js/bootstrap.min.js"></script>
    <script>
        $(document).ready(function(){
            $('.toast').toast('show');
        });
    </script>
</head>
<body>
    <h1>Toasts</h1>
    <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
            <strong class="mr-auto">Bootstrap</strong>
            <small class="text-muted">just now</small>
            <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
        <div class="toast-body">
            See? Just like this.
        </div>
    </div>
</body>
</html>
        """,
            "readme": """
# Toasts

This example demonstrates how to use Bootstrap's toast classes.

## HTML Code
The HTML file includes a toast notification that shows on page load using Bootstrap's toast classes.
        """,
        },
        {
            "name": "Tooltips_Popovers",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tooltips and Popovers</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
        <script src="/lib/jquery/3.7.1/js/jquery-3.7.1.slim.min.js"></script>
    <script src="/lib/popperjs/2.11.8/js/popperjs-2.11.min.js"></script>
    <script src="/lib/bootstrap/5.3.3/js/bootstrap.min.js"></script>
    <script>
        $(function () {
            $('[data-toggle="tooltip"]').tooltip();
            $('[data-toggle="popover"]').popover();
        });
    </script>
</head>
<body>
    <h1>Tooltips and Popovers</h1>
    <button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="top" title="Tooltip on top">
        Tooltip on top
    </button>
    <button type="button" class="btn btn-secondary" data-toggle="popover" title="Popover title" data-content="And here's some amazing content. It's very engaging. Right?">
        Click to toggle popover
    </button>
</body>
</html>
        """,
            "readme": """
# Tooltips and Popovers

This example demonstrates how to use Bootstrap's tooltip and popover classes.

## HTML Code
The HTML file includes buttons that trigger tooltips and popovers using Bootstrap's tooltip and popover classes.
        """,
        },
        {
            "name": "Alerts_Dismissible",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dismissible Alerts</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
        <script src="/lib/jquery/3.7.1/js/jquery-3.7.1.slim.min.js"></script>
    <script src="/lib/popperjs/2.11.8/js/popperjs-2.11.min.js"></script>
    <script src="/lib/bootstrap/5.3.3/js/bootstrap.min.js"></script>
</head>
<body>
    <h1>Dismissible Alerts</h1>
    <div class="alert alert-warning alert-dismissible fade show" role="alert">
        <strong>Holy guacamole!</strong> You should check in on some of those fields below.
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
</body>
</html>
        """,
            "readme": """
# Dismissible Alerts

This example demonstrates how to use Bootstrap's dismissible alert classes.

## HTML Code
The HTML file includes a dismissible alert using Bootstrap's alert classes.
        """,
        },
        {
            "name": "Pagination_Advanced",
            "html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Pagination</title>
        <link href="/lib/bootstrap/5.3.3/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <h1>Advanced Pagination</h1>
    <nav aria-label="Page navigation example">
        <ul class="pagination">
            <li class="page-item disabled">
                <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
            </li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item">
                <a class="page-link" href="#">Next</a>
            </li>
        </ul>
    </nav>
</body>
</html>
        """,
            "readme": """
# Advanced Pagination

This example demonstrates how to use Bootstrap's advanced pagination classes.

## HTML Code
The HTML file includes a pagination component with disabled and active states using Bootstrap's pagination classes.
        """,
        },
    ]
}
