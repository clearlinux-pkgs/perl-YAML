#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v3
# autospec commit: c1050fe
#
Name     : perl-YAML
Version  : 1.31
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/I/IN/INGY/YAML-1.31.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IN/INGY/YAML-1.31.tar.gz
Summary  : "YAML Ain't Markup Language™"
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-YAML-license = %{version}-%{release}
Requires: perl-YAML-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Spiffy)
BuildRequires : perl(Test::Base)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::YAML)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
YAML - YAML Ain't Markup Language™
VERSION
This document describes YAML version 1.31.

%package dev
Summary: dev components for the perl-YAML package.
Group: Development
Provides: perl-YAML-devel = %{version}-%{release}
Requires: perl-YAML = %{version}-%{release}

%description dev
dev components for the perl-YAML package.


%package license
Summary: license components for the perl-YAML package.
Group: Default

%description license
license components for the perl-YAML package.


%package perl
Summary: perl components for the perl-YAML package.
Group: Default
Requires: perl-YAML = %{version}-%{release}

%description perl
perl components for the perl-YAML package.


%prep
%setup -q -n YAML-1.31
cd %{_builddir}/YAML-1.31
pushd ..
cp -a YAML-1.31 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-YAML
cp %{_builddir}/YAML-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-YAML/8ebf906fcf0eb467d966a6605855d9c003e76598 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/YAML.3
/usr/share/man/man3/YAML::Any.3
/usr/share/man/man3/YAML::Dumper.3
/usr/share/man/man3/YAML::Dumper::Base.3
/usr/share/man/man3/YAML::Error.3
/usr/share/man/man3/YAML::Loader.3
/usr/share/man/man3/YAML::Loader::Base.3
/usr/share/man/man3/YAML::Marshall.3
/usr/share/man/man3/YAML::Node.3
/usr/share/man/man3/YAML::Tag.3
/usr/share/man/man3/YAML::Types.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-YAML/8ebf906fcf0eb467d966a6605855d9c003e76598

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
