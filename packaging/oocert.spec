Name:           oocert
Version:        0.2.0
Release:        1%{?dist}
Summary:        Manages local system trust roots under /etc/ssl/certs/ with revocation checking.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oocert
Source0:        oocert-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oocert is a sovereign, capability-bounded CERTIFICATE STORE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oocert
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oocert-uninstall

%files
/usr/bin/oocert
/usr/bin/oocert-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevate to pure native openOODA with dual CLI/MCP and tri-dist packaging
