# Computer Networks - Phase 1

Shared project scaffold for the Private Network Service Platform assignment.

## Current progress

- Step 3: project folders created.
- Step 4: Mac 1 network inventory recorded on 3 October 2026.
- Steps 5 onward: not executed. Backend, DNS, nginx, and TLS services are not configured or running by this repository.

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

Read [the full Phase 1 implementation plan](docs/CN_Phase1_Implementation_Plan.pdf). It contains all 20 steps, source code to create later, commands for each Mac, checkpoints, packet evidence, and required failure demonstrations. The PDF is instructions, not evidence of deployment.

| Machine | Role | Planned services |
|---|---|---|
| Mac 1 | DNS | UDP/TCP 53 |
| Mac 2 | Edge / load balancer | TCP 8080/8443 |
| Mac 3 | Backend A + client | TCP 3001 |
| Mac 4 | Backend B + client | TCP 3002 |

See the public [network inventory template](architecture/network-inventory.md). Actual Mac 1 measurements are kept in an ignored local file, runtime/mac1-network-inventory.private.md. Share measured addresses privately with your team and recheck them on the actual team LAN. Other machines remain pending. The assignment specifies a shared private LAN for evaluation; VPN-based remote preparation needs a separate agreed approach.

Empty tracked folders use .gitkeep so they exist after cloning. Each member can fill the folders for their role when that step is authorized.

Private keys, runtime files, and config/network.env are ignored. Never force-add private keys.
