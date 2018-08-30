#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-YAML
Version  : 1.26
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-1.26.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-1.26.tar.gz
Summary  : "YAML Ain't Markup Languageâ¢"
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-YAML-license
BuildRequires : buildreq-cpan
BuildRequires : perl(Spiffy)
BuildRequires : perl(Test::Base)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::YAML)

%description
NAME
YAML - YAML Ain't Markup Languageâ¢
VERSION
This document describes YAML version 1.26.

%package dev
Summary: dev components for the perl-YAML package.
Group: Development
Provides: perl-YAML-devel

%description dev
dev components for the perl-YAML package.


%package license
Summary: license components for the perl-YAML package.
Group: Default

%description license
license components for the perl-YAML package.


%prep
%setup -q -n YAML-1.26

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-YAML
cp LICENSE %{buildroot}/usr/share/doc/perl-YAML/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/YAML.pm
/usr/lib/perl5/site_perl/5.26.1/YAML.pod
/usr/lib/perl5/site_perl/5.26.1/YAML/Any.pm
/usr/lib/perl5/site_perl/5.26.1/YAML/Any.pod
/usr/lib/perl5/site_perl/5.26.1/YAML/Dumper.pm
/usr/lib/perl5/site_perl/5.26.1/YAML/Dumper.pod
/usr/lib/perl5/site_perl/5.26.1/YAML/Dumper/Base.pm
/usr/lib/perl5/site_perl/5.26.1/YAML/Dumper/Base.pod
/usr/lib/perl5/site_perl/5.26.1/YAML/Error.pm
/usr/lib/perl5/site_perl/5.26.1/YAML/Error.pod
/usr/lib/perl5/site_perl/5.26.1/YAML/Loader.pm
/usr/lib/perl5/site_perl/5.26.1/YAML/Loader.pod
/usr/lib/perl5/site_perl/5.26.1/YAML/Loader/Base.pm
/usr/lib/perl5/site_perl/5.26.1/YAML/Loader/Base.pod
/usr/lib/perl5/site_perl/5.26.1/YAML/Marshall.pm
/usr/lib/perl5/site_perl/5.26.1/YAML/Marshall.pod
/usr/lib/perl5/site_perl/5.26.1/YAML/Mo.pm
/usr/lib/perl5/site_perl/5.26.1/YAML/Node.pm
/usr/lib/perl5/site_perl/5.26.1/YAML/Node.pod
/usr/lib/perl5/site_perl/5.26.1/YAML/Tag.pm
/usr/lib/perl5/site_perl/5.26.1/YAML/Tag.pod
/usr/lib/perl5/site_perl/5.26.1/YAML/Types.pm
/usr/lib/perl5/site_perl/5.26.1/YAML/Types.pod

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
%defattr(-,root,root,-)
/usr/share/doc/perl-YAML/LICENSE
