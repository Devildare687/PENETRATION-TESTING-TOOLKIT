# Penetration Testing Toolkit

This toolkit includes the following modules for penetration testing:

## 1. Port Scanner

This module scans for open ports on a target system.

### Usage:

```python
from pen_test_toolkit.port_scanner import port_scanner

target_ip = "192.168.1.1"
ports_to_scan = [22, 80, 443, 8080]
open_ports = port_scanner(target_ip, ports_to_scan)
print("Open ports:", open_ports)
