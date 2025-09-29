# Advanced Usage Guide

## Customizing Security Rules
- Edit the `config.yaml` file to define whitelisted/blacklisted services.
- Set thresholds for anomaly detection (CPU/memory) in the config.

## Integrating with SIEM/SOAR
- Configure log export in `config.yaml` to send audit logs to your SIEM endpoint.
- Use the `logs/audit.py` module for custom log formatting.

## Using Threat Intelligence APIs
- Add your API keys for services like VirusTotal in `config.yaml`.
- Use the `security/threat_intel.py` module to check hashes of running processes.

## Scheduling Security Scans
- Integrate with tools like Lynis by editing `security/scanner.py`.
- Schedule scans via cron or systemd timers for regular reports.

## Extending Chomu
- Add new modules in `chomu/security/` or `chomu/monitoring/`.
- Register new CLI commands in the main CLI module.

## Example: Adding a Custom Alert
```python
# In chomu/monitoring/anomaly.py
from chomu.core.logger import logger
# ...
if mem_mb > self.mem_threshold_mb:
    logger.warning(f"High memory usage detected: {mem_mb:.1f} MB")
```

For more, see the [Contributing Guide](./contributing.md).
