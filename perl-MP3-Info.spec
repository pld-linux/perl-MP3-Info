%include	/usr/lib/rpm/macros.perl
%define		pdir	MP3
%define		pnam	Info
Summary:	MP3::Info Perl module
Summary(cs):	Modul MP3::Info pro Perl
Summary(da):	Perlmodul MP3::Info
Summary(de):	MP3::Info Perl Modul
Summary(es):	Módulo de Perl MP3::Info
Summary(fr):	Module Perl MP3::Info
Summary(it):	Modulo di Perl MP3::Info
Summary(ja):	MP3::Info Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	MP3::Info ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul MP3::Info
Summary(pl):	Modu³ Perla MP3::Info
Summary(pt):	Módulo de Perl MP3::Info
Summary(pt_BR):	Módulo Perl MP3::Info
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl MP3::Info
Summary(sv):	MP3::Info Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl MP3::Info
Summary(zh_CN):	MP3::Info Perl Ä£¿é
Name:		perl-MP3-Info
Version:	1.01
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
Obsoletes:	perl-MPEG-MP3Info
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MP3::Info - fetches and manipulates info from MP3 audio files.

%description -l pl
MP3::Info - wyci±ga informacje z plików MP3 i umo¿liwia operowanie na
nich.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -f eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/MPEG
%{perl_vendorlib}/MP3
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
