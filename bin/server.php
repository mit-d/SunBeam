/* Will create a UDP server on port 10000 */

<?php
$sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);

/* UDP port 10000 */
socket_bind($sock, '0.0.0.0', 10000);

// $voltages = fopen("/tmp/MCP3008_v0", "r") or die("Unable to open /tmp/MCP3008_v0");
$file = file("/tmp/MCP3008_v0");

for(;;){
	socket_recvfrom($sock, $message, 1024, 0, $ip, $port);
	// $reply = $fread($voltages);
	for($i = max(0,count($file-6)); $i < count($file); $i++) {
		$reply = $file[$i] . \n;
		socket_sendto($sock, $reply, strlen($reply), 0, $ip, $port);
	}
}
/* never reached */
fclose($voltages);
