# Phase 1 network inventory template

Record measured addresses on the team LAN in a private local copy. The actual IP, gateway and MAC details are kept under Git-ignored `runtime/` on Mac 1 and the other team Macs. Recheck after changing Wi-Fi or renewing DHCP.

| Machine | Owner | Role | IPv4 | Subnet mask/prefix | Default gateway | Interface | Active MAC address | Service |
|---|---|---|---|---|---|---|---|---|
| Mac 1 | Shourya | Private DNS and client | Fill privately | Fill privately | Fill privately | Fill privately | Fill privately | UDP/TCP 53 |
| Mac 2 | Om | Edge and load balancer | Fill privately | Fill privately | Fill privately | Fill privately | Fill privately | TCP 8080/8443 |
| Mac 3 | Daksh | Backend A and client | Fill privately | Fill privately | Fill privately | Fill privately | Fill privately | TCP 3001 |
| Mac 4 | Aditya | Backend B and client | Fill privately | Fill privately | Fill privately | Fill privately | Fill privately | TCP 3002 |

The team reported twelve of twelve directed peer pings passed on 5 October 2026. Actual peer results and inventory are stored privately. Verify that all four Macs are on the same project LAN and that the measured addresses still match before evaluation.
