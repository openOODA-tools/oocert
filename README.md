# oocert: Sovereign CERTIFICATE STORE

<div align="center">

```
================================================================================
                                oocert
                Sovereign openOODA CERTIFICATE STORE
================================================================================
```

**Sovereign CERTIFICATE STORE**  
*Manages local system trust roots under /etc/ssl/certs/ with revocation checking and X.509 auditing.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oocert/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oocert-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oocert/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oocert/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oocert-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oocert/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oocert [options] [CERT_OR_STORE_PATH]

Manages local system trust roots under /etc/ssl/certs/ with revocation checking.

Options:
  -s, --store [PATH]   scan system or custom trust store directory/bundle [default]
  -i, --inspect <FILE> inspect single X.509 PEM certificate and cryptographic parameters
  -a, --audit          audit trust store certificates for expired roots and weak hashes
  -f, --fingerprint    calculate SHA-256 fingerprint for certificate
  -t, --to <FORMAT>    target format: panel, json, diag
      --json           output formatted as structured JSON
      --demo           use built-in sample trust anchor and certificate
      --mcp            run as Model Context Protocol stdio server
  -h, --help           display this help and exit
  -v, --version        output version information and exit
```

### Examples
```bash
# Scan default system trust store (/etc/ssl/certs/ca-certificates.crt)
oocert

# Audit trust store for expired roots and weak algorithms
oocert -a

# Inspect a specific PEM certificate
oocert -i /etc/ssl/certs/example.pem

# Calculate SHA-256 fingerprint
oocert -f /etc/ssl/certs/example.pem

# Structured JSON telemetry
oocert --json
```

---

## 3. Model Context Protocol (MCP)

When invoked with `--mcp`, `oocert` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

```bash
oocert --mcp
```

### Exported Tools
* `cert_inspect`: Inspect X.509 certificate subject, issuer, validity, and parameters.
* `cert_verify`: Verify expiration and trust validity of an X.509 certificate.
* `cert_store_list`: List installed root CA certificates from system trust store.
* `cert_audit`: Audit trust store certificates for expired roots and weak algorithms.
* `cert_fingerprint`: Compute SHA-256 fingerprint of a PEM certificate.

---

## 4. Theming Integration (`oote`)

`oocert` synchronizes visual styles and status colors with [oote](https://github.com/openOODA-tools/oote):
* **Configuration:** Reads active palette from `~/.openooda/theme.oot`.
* **Environment Overrides:** Respects `$OODA_THEME` and `$NO_COLOR`.

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`, `&McpCap`). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
