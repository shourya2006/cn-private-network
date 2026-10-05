# Computer Networks - Phase 1

A four-Mac private-network service platform for the course project. The running system uses Mac 1 for DNS, Mac 2 for nginx/TLS and load balancing, and Macs 3 and 4 for two HTTP backends.

## Current status

As of 5 October 2026, the team has reported all 12 directed LAN pings and completed the DNS, backend, HTTP/HTTPS, TLS trust, caching, Wireshark, HTTP/2, and five controlled-failure demonstrations. Mac 1 directly verified the edge and both backends after the failure tests. These live results depend on the Macs remaining on the project LAN with their services running; check them again before a demo.

Raw evidence and actual network addresses are kept in each member's local, Git-ignored `runtime/` or `evidence/` folders. The private submission bundle and architecture index are being assembled. This public repository contains the implementation plan, backend source, demo runbook, and public certificate; it must never contain `tls/server.key`, credentials, or unreviewed packet captures.

## Team — Packet Pioneers

- Shourya Bafna — Mac 1: DNS and demo client
- Om Yadav — Mac 2: nginx edge and TLS load balancer
- Daksh Batra — Mac 3: Backend A and client
- Aditya Bhardwaj — Mac 4: Backend B and client

## Run the backends

Requires Python 3.9 or newer. From the repository root, run the appropriate command and leave it running during the demo.

Mac 3 / Backend A:

```bash
python3 -u backend/app.py --name A --port 3001
```

Mac 4 / Backend B:

```bash
python3 -u backend/app.py --name B --port 3002
```

The servers listen on all interfaces. nginx on Mac 2 connects to their current private LAN addresses. Recheck DHCP addresses before starting the edge.

## Get the project

```bash
git clone https://github.com/shourya2006/cn-private-network.git
cd cn-private-network
```

To get subsequent shared changes:

```bash
git pull
```

## Implementation instructions

Read [the full Phase 1 implementation plan](docs/CN_Phase1_Implementation_Plan.pdf). It contains the 20-step workflow, code and configuration examples, role-specific commands, checkpoints, packet evidence, and five required failure demonstrations. The plan is instructions; live validation and evidence were produced separately on the four Macs.

| Machine | Role | Project ports |
|---|---|---|
| Mac 1 | Private DNS and test client | UDP/TCP 53 |
| Mac 2 | nginx edge and TLS load balancer | TCP 8080/8443 |
| Mac 3 | Backend A and test client | TCP 3001 |
| Mac 4 | Backend B and test client | TCP 3002 |

See the [public network inventory template](architecture/network-inventory.md). Measured addresses, masks, gateways, and MACs remain in ignored local files. Recheck them if DHCP changes or a Mac moves to another network. The assignment requires a shared private LAN for evaluation.

The backend source is [backend/app.py](backend/app.py), and the [demo runbook](docs/Phase1_Demo_Runbook.md) gives the Phase 1 presentation order. The public certificate is [tls/server.crt](tls/server.crt). It is self-signed and must be explicitly trusted by project clients; never bypass certificate validation in demonstration requests.

Private keys, `runtime/`, and `config/network.env` are Git-ignored. Do not force-add them.
