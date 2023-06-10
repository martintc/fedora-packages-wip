Name:     blogc
Version:  0.20.1
Release:  %autorelease
Summary:  A blog compiler.
License:  BSD-3-Clause
URL:      https://blogc.rgm.io/
Source:   https://github.com/blogc/blogc/releases/download/v%{version}/blogc-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
Blogc is a static site generator written mostly in C using makefiles to build the website.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%{_bindir}/blogc
%{_mandir}/man1/blogc.1.*
%{_mandir}/man7/blogc-*

%changelog
%autochangelog
