#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MP3
%define		pnam	Info
Summary:	MP3::Info - manipulate / fetch info from MP3 audio files
Summary(pl.UTF-8):	MP3::Info - odczyt i operowanie na informacjach z plików dźwiękowych MP3
Name:		perl-MP3-Info
Version:	1.20
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MP3/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ffb3427089a6b5f56e35e5b2ab902d29
URL:		http://search.cpan.org/dist/MP3-Info/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-MPEG-MP3Info
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MP3::Info Perl module fetches and manipulates info from MP3 audio
files.

%description -l pl.UTF-8
Moduł Perla MP3::Info wyciąga informacje z plików MP3 i umożliwia
operowanie na nich.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -f eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MP3
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
