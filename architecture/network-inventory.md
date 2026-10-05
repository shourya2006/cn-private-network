# Phase 1 network inventory template

Record actual addresses on the team LAN. Keep measured IP, gateway, and MAC details in a private local copy instead of this public repository. Mac 1 measurements have already been saved locally in runtime/mac1-network-inventory.private.md, which Git ignores.

| Machine | Owner | Role | IPv4 | Subnet mask/prefix | Default gateway | Interface | Active MAC address | Planned service |
|---|---|---|---|---|---|---|---|---|
| Mac 1 | Shourya | Private DNS server | Fill privately | Fill privately | Fill privately | Fill privately | Fill privately | UDP/TCP 53; not started |
| Mac 2 | Pending | Edge / load balancer | Fill privately | Fill privately | Fill privately | Fill privately | Fill privately | TCP 8080/8443 |
| Mac 3 | Pending | Backend A + client | Fill privately | Fill privately | Fill privately | Fill privately | Fill privately | TCP 3001 |
| Mac 4 | Pending | Backend B + client | Fill privately | Fill privately | Fill privately | Fill privately | Fill privately | TCP 3002 |

Recheck the measurements after changing Wi-Fi or renewing DHCP.

The other machines' details and all-pair connectivity remain unverified. No DNS settings or services have been changed.
