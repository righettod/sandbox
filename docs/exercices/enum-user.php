<?php
$case = 2;
$login = $_POST["login"];
$password = $_POST["password"];

function auth($login, $password, $case)
{
    $logins_list = array('abbi', 'abbie', 'abby', 'abbye', 'abdalla');
    switch ($case) {
        case 1:
            //Case 1: With a discrepancy factor via the error message
            if (in_array($login, $logins_list)) {
                $rt = "Authentication succeed!";
            } else {
                $rt = "User not found.";
            };
            break;
        case 2:
            //Case 2: With a discrepancy factor via the processing time
            if (in_array($login, $logins_list)) {
                $options = ['cost' => 15];
                password_hash($password, PASSWORD_BCRYPT, $options);
            };
            $rt = "Authentication failure!";
            break;
        case 3:
            //Case 3: With account locking using attempt counter into a server side session
            if (in_array($login, $logins_list)) {
                session_start();
                if ($password != "1234567890") {
                    if (!isset($_SESSION["counter"])) {
                        $_SESSION["counter"] = 0;
                    }
                    $_SESSION["counter"] = $_SESSION["counter"] + 1;
                    if ($_SESSION["counter"] > 3) {
                        $rt = "Authentication failure (account locked)!";
                    } else {
                        $rt = "Authentication failure!";
                    }
                } else {
                    $rt = "Authentication failure !";
                    $_SESSION["counter"] = 0;
                    session_destroy();
                }
            } else {
                $rt = "Authentication failure!";
            }
            break;
        default:
            $rt = "Case not supported.";
    }

    return $rt;
}

if (isset($login) && isset($password)) {
    $status = auth($login, $password, $case);
} else {
    $status = "NA";
}
?>

<!DOCTYPE html>
<html>

<head>
    <title>Exo User Enum</title>
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
    Send a <b>POST</b> to the script using the content type <b>application/x-www-form-urlencoded</b> with the following field <b>login</b> and <b>password</b>.
    <br><br>
    <font color="green">Authentication status: <b><?php echo ($status) ?></b></font>
    <br><br>
    Login dict: <b>https://raw.githubusercontent.com/danielmiessler/SecLists/master/Usernames/Names/names.txt</b>
    <br><br>
    Take only ones starting with <b>a</b>
    <br><br>
    <code>curl -d "login=x&password=x" http://host/enum-user.php</code>
</body>

</html>