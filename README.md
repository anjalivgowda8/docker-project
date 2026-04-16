# NGINX High Availability Project with Docker

This project simulates a high-availability web architecture locally using Docker containers.

A browser sends requests to an NGINX load balancer, which distributes traffic between two NGINX web servers. If one server goes down, traffic is automatically routed to the remaining healthy server.

---

## Architecture

```text
Browser
  │
NGINX Load Balancer (container)
  │
 ┌───────────────┬───────────────┐
 │               │
NGINX Server 1   NGINX Server 2
(container)     (container)
Serving HTML    Serving HTML