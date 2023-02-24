<?php
$is_ffuf = strrpos(strtolower($_SERVER["HTTP_USER_AGENT"]), "ffuf");
if ($is_ffuf !== false) {
    header("Location: https://cdimage.kali.org/kali-2022.4/kali-linux-2022.4-installer-amd64.iso", true, 302);
} else {
    $wait = random_int(1, 10);
    header("Content-Type: text/plain", true);
    header("X-Wait: $wait", true);
    $v = $_GET["Sticky"];
    $d = $_GET["debug"];
    if (isset($d)) {
        header("Location: https://cdimage.kali.org/kali-2022.4/kali-linux-2022.4-installer-amd64.iso", true, 302);
    } else if (isset($v) && intval($v) === 1) {
        print("[V] Congratulations, you discovered the hidden parameter !!!!");
    } else {
        print("[X] Try again :)");
        sleep($wait);
    }
}
