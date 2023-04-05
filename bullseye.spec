%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name: bullseye
Version: 9.1.1
Release: 1%{?dist}
Summary: BullseyeCoverage
License: Proprietary
Url: https://www.bullseye.com/index.html
Source: https://www.bullseye.com/download/BullseyeCoverage-%{version}-Linux-x64.tar

%description
The BullseyeCoverage compiler

%prep
%autosetup -n BullseyeCoverage-%{version}

%build
exit 0

%install
./install --quiet --key %{key} --prefix %{buildroot}/opt/BullseyeCoverage

%files
/opt/*

%changelog
* Fri Mar 31 2023 Brian J. Murrell <brian.murrell@intel.com> - 9.1.1-1
- Update to 9.1.1

* Fri Feb 19 2021 Brian J. Murrell <brian.murrell@intel.com> - 8.21.4-1
- First packaged version
