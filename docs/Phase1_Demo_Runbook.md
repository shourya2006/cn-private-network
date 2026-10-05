# Phase 1 live demo runbook

Use this after all four Macs are back on the project LAN. Each member should work from their own clone and source `config/network.env` in every new testing terminal. Keep the original DNS settings saved on each client so they can be restored after the review. Do not use `curl -k` or an IP address in the final application URL.

## Before the evaluator arrives

1. Recheck the four current IPv4 addresses against each Mac's private inventory and `config/network.env`. If DHCP changed an address, update the team configuration, dnsmasq record, and nginx upstreams before the demo. Confirm the certificate is still within its validity period and matches both private names.
2. Mac 3: confirm Backend A is listening on 3001. Mac 4: confirm Backend B is listening on 3002. Start them with `python3 -u backend/app.py --name A --port 3001` or `--name B --port 3002` only if they are not already running.
3. Mac 1: confirm the project dnsmasq is listening on UDP/TCP 53 and answers both names with `$EDGE_IP`. Do not start a duplicate dnsmasq instance.
4. Mac 2: test the existing nginx configuration with `nginx -p "$PWD/" -c "$PWD/nginx/nginx.conf" -t`; reload the existing instance only if the config has changed. Confirm 8443 is listening, both backends return direct HTTP 200, and the edge returns validated HTTPS 200.
5. Mac 3 and Mac 4: confirm ordinary `dig "$APP_HOST" A` uses Mac 1 and returns Mac 2. Open `https://app.team1.test:8443/` in the trusted browser. Secure DNS in a browser may bypass the system resolver; Safari was the browser used for the team trust check.

## Live sequence

| Order | Who | Show | Evidence or command |
|---|---|---|---|
| 1 | Mac 1 | Topology, roles, IP/subnet/gateway/ports, cloud equivalents | Private `runtime/submission/architecture.md` and current `ifconfig` / route checks |
| 2 | All Macs | Same LAN and peer reachability | Private 12-direction ping matrix plus a fresh short ping to a peer |
| 3 | Mac 3 or 4 | Private DNS resolution | `dig "$APP_HOST" A` and `dig "$API_HOST" A`; point out Mac 1 as DNS server and Mac 2 as the answer |
| 4 | Mac 3 or 4 | Secure application by domain | Trusted browser and `curl --noproxy '*' --cacert tls/server.crt -i "$APP_URL/api/status"` |
| 5 | Mac 1 or 4 | Load balancing | Six sequential validated requests; show HTTP 200 and both `X-Backend` values |
| 6 | Mac 3 | One captured DNS → TCP → TLS flow | Saved `mac3-phase1-flow.pcapng` and readable frame screenshots: DNS 37/38, SYN/SYN-ACK/ACK 39–41, ClientHello 42, ServerHello/Certificate 45, ChangeCipherSpec 47/49, encrypted data 51/53 |
| 7 | Mac 3 | HTTP caching | `/cache` headers with `Cache-Control` and ETag; matching `If-None-Match` gives 304, nonmatching gives 200 |
| 8 | Mac 3 then Mac 1 | Backend A failure and recovery | Only on evaluator request: stop A, show B-only 200 responses, restart A, wait for passive `fail_timeout`, show both A/B again |
| 9 | Team | Other Phase 1 failures | Show saved Step 17A/B/D/E raw outputs and explain the affected layer; do not leave a failure active |
| 10 | Each member | Individual explanation | Answer from understanding, without reading notes |

Mac 3's saved TLS capture deliberately used TLS 1.2 so the Certificate and ChangeCipherSpec are visible. The live edge also supports TLS 1.3 and HTTP/2. Wireshark cannot read the encrypted application body; pair the packet view with the matching certificate-validated curl output.

## Short explanations each member should know

- DNS maps the private name to the edge IP. It does not guarantee a TCP connection. A wrong resolver breaks lookup; a wrong record sends the client to the wrong destination.
- An IP identifies the host; a TCP port identifies the service. A successful ping does not prove HTTPS is available on 8443 or 9443.
- TCP's SYN/SYN-ACK/ACK establishes the connection; sequence and acknowledgment numbers let the peers detect loss and keep bytes ordered. The client's source port is ephemeral.
- TLS authenticates the edge name/certificate and encrypts HTTP between client and nginx. nginx terminates TLS and creates a separate HTTP connection to a backend.
- nginx normally rotates A/B. Its passive failure handling retries a failed A request on B, so a client can receive 200 while the log records a failed upstream attempt. With both backends down, nginx returns 502 but its own `/edge-health` can still return 200.
- `Cache-Control: public, max-age=60` permits a fresh response to be reused. An ETag lets a stale response be revalidated; a matching validator gives 304 without a response body. This does not imply nginx proxy caching is enabled.
- HTTP/2 is negotiated between client and edge through ALPN; the edge-to-backend connection remains HTTP/1.1.

The evidence index and raw files remain private. Keep services running for the Phase 1 review. Run the plan's Step 20 shutdown and original-DNS restoration only after the live review is finished.
