%include	/usr/lib/rpm/macros.perl
Summary:	MP3-Info perl module
Summary(pl):	Modu³ perla MP3-Info
Name:		perl-MP3-Info
Version:	0.91
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MP3/MP3-Info-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
Obsoletes:	perl-MPEG-MP3Info
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MP3-Info - fetches and manipulates info from MP3 audio files.

%description -l pl
MP3-Info - wyci±ga i umo¿liwia operowanie na informacjach z plików
MP3.

%prep
%setup -q -n MP3-Info-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz eg
%{perl_sitelib}/MPEG/MP3Info.pm
%{perl_sitelib}/MP3/Info.pm
%{_mandir}/man3/*
