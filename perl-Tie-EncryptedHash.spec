%define modname	Tie-EncryptedHash
%define modver	1.24

Summary:	Hashes (and objects based on hashes) with encrypting fields
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	15
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-Crypt-CBC
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-DES

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
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*

