<?php
header("Content-Type: text/plain", true);
$is_allowed = strrpos(strtolower($_SERVER["HTTP_X_CLIENTIP"]), "0000:0000:0000:0000:0000:0000:0000:0001");
if ($is_allowed === false) {
    print("[X] Access restricted to call from hosts!");
    print(str_repeat("X", random_int(1, 1000000)));
} else {
    print("[V] Congratulations, you discovered a way to spoof your location !!!!");
}
