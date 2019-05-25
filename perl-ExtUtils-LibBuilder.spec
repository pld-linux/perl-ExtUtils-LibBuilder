#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	ExtUtils
%define		pnam	LibBuilder
%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils::LibBuilder - a tool to build C libraries
Summary(pl.UTF-8):	ExtUtils::LibBuilder - narzędzie do budowania bibliotek C
Name:		perl-ExtUtils-LibBuilder
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8ffe9e9a3c2f916f40dc4f6aed237d33
URL:		https://metacpan.org/release/ExtUtils-LibBuilder/
BuildRequires:	perl-ExtUtils-CBuilder >= 0.23
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Some Perl modules need to ship C libraries together with their Perl
code. Although there are mechanisms to compile and link (or glue) C
code in your Perl programs, there isn't a clear method to compile
standard, self-contained C libraries.

This module main goal is to help in that task.

%description -l pl.UTF-8
Niektóre moduły Perla muszą mieć dołączone do kodu perlowego
biblioteki C. O ile są mechanizmy do kompilowania i linkowania (czy
sklejania) kodu C do programów w Perlu, to nie ma prostej metody
kompilowania standardowej, samodzielnej biblioteki C.

Głównym celem tego modułu jest pomoc w tym zadaniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/LibBuilder.pm
%{_mandir}/man3/ExtUtils::LibBuilder.3pm*
