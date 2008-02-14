Name:           perl-Tie-EncryptedHash
Version:        1.21
Release:        %mkrel 4
License:        Artistic
%define module  Tie-EncryptedHash
Group:          Development/Perl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:        Hashes (and objects based on hashes) with encrypting fields
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}
Prefix:         %{_prefix}
%if %{mdkversion} < 1010
Buildrequires:perl-devel
%endif
BuildRequires:  perl-Crypt-CBC
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:  perl-Crypt-DES
BuildArch:      noarch

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
%setup -q -n %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.html
%{perl_vendorlib}/*
%{_mandir}/*/*

