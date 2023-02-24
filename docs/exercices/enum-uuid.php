<?php
//https://gist.github.com/dahnielson/508447
include 'UUID.php';
session_start();
if (!isset($_SESSION["key"])) {
    $date = new DateTime();
    $key = $date->format('YmdHi');
    $_SESSION["key"] = $key;
}
if (!isset($_SESSION["secret-id"])) {
    $v5uuid = UUID::v5('6ba7b814-9dad-11d1-80b4-00c04fd430c8', $_SESSION["key"]);
    $_SESSION["secret-id"] = $v5uuid;
}
$id = $_GET["id"];
if ($id == $_SESSION["secret-id"]) {
    $status = "Congratulations, you find me !!!!";
} else {
    $status = "Try again :)";
}
?>
<!DOCTYPE html>
<html>

<head>
    <title>Exo UUID Enum</title>
    <style>
        body {
            background-color: white;
            color: black;
            font: normal 14px Consolas, Arial, sans-serif;
            padding-left: 5px;
            padding-right: 5px;
            padding-top: 5px;
            padding-bottom: 5px;
        }
    </style>
</head>

<body>
    You must find the ID of the document hidden into your session.<br><br>
    Propose the ID via the query parameter <b>id</b>.<br><br>
    ID format is UUID like <b>e50eaaa3-7f23-567e-a7b6-526974889570</b>, Call is like <b>enum-uuid.php?id=e50eaaa3-7f23-567e-a7b6-526974889570</b>
    <br><br>
    <font color="red">[i] Documentation to read:</font><br>
    https://www.uuidtools.com/uuid-versions-explained
    <br><br>
    <font color="red">[i] Page generated on</font> <b><?php echo ($_SESSION["key"]) ?></b>
    <br><br>
    <font color="blue">Proposed: <b><?php echo ($id) ?></b></font>
    <br><br>
    <font color="green"><b><?php echo ($status) ?></b></font>
</body>

</html>