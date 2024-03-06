<!-- index.php -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <title>We love PHP</title>
</head>

<body>
    <h1>Hello from PHP site!</h1>
    <form method="GET">
        <label for="imageSelect">Select an image:</label>
        <select name="imageSelect" id="imageSelect">
            <option value="image1.jpg">Image 1</option>
            <option value="image2.jpg">Image 2</option>
            <option value="image3.jpg">Image 3</option>
        </select>
        <input type="submit" value="Display Image">
    </form>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET["imageSelect"])) {
        $selectedImage = $_GET["imageSelect"];
        $allowedImages = ['image1.jpg', 'image2.jpg', 'image3.jpg'];
        if (in_array($selectedImage, $allowedImages)) {
            $selectedImage = basename($selectedImage);
            $imgPath = "/img/" . $selectedImage;
            echo "<img src='" . $imgPath . "' alt=\"Selected Image\">";
        } else {
            echo "Invalid image selection!";
        }
    }
    ?>
</body>

</html>