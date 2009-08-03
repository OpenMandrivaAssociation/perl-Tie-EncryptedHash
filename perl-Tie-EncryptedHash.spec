%define upstream_name    Tie-EncryptedHash
%define upstream_version 1.24

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:        Hashes (and objects based on hashes) with encrypting fields
License:        Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:perl-devel
%endif
BuildRequires:  perl-Crypt-CBC
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:  perl-Crypt-DES
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
