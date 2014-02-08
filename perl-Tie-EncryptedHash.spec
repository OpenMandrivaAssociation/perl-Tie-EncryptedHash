%define upstream_name    Tie-EncryptedHash
%define upstream_version 1.24

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	Hashes (and objects based on hashes) with encrypting fields
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-Crypt-CBC
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-DES
BuildArch:	noarch

%description 
Tie::EncryptedHash augments Perl hash semantics to build
secure, encrypting containers of data. Tie::EncryptedHash
introduces special hash fields that are coupled with
encrypt/decrypt routines to encrypt assignments at STORE()
and decrypt retrievals at FETCH(). By design, encrypting
fields are associated with keys that begin in single
underscore. The remaining keyspace is used for accessing
normal hash fields, which are retained without
modification.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" echo | %__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README.html
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.240.0-5mdv2012.0
+ Revision: 765765
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.240.0-3
+ Revision: 676528
- rebuild

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.240.0-2
+ Revision: 658891
- rebuild for updated spec-helper

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.240.0-1mdv2010.0
+ Revision: 408092
- rebuild using %%perl_convert_version

* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2009.0
+ Revision: 236289
- update to new version 1.24

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 1.21-4mdv2008.1
+ Revision: 168173
- fix no-buildroot-tag
- kill (multiple!) definitions of %%buildroot on Pixel's request

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 1.21-4mdv2008.0
+ Revision: 23637
- rebuild


* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.21-3mdk
- Fix url
- Fix BuildRequires thanks guillomovitch for the explanations

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.21-2mdk
- rebuild for new perl

* Thu Nov 06 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 1.21-1mdk
- New package

