<?php
//https://portswigger.net/web-security/access-control/idor
session_start();
if (!isset($_SESSION["secret-id"])) {
    $_SESSION["secret-id"] = uniqid();
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
    <title>Exo IDOR Enum</title>
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
    ID format is <b><?php echo (uniqid()); ?></b>, like <code>enum-idor.php?id=<?php echo (uniqid()); ?></code>
    <br><br>
    <font color="blue">Proposed: <b><?php echo ($id) ?></b></font>
    <br><br>
    <font color="green"><b><?php echo ($status) ?></b></font>
    <br><br>
</body>

</html>