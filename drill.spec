Summary:	Tool ala dig from BIND
Name:		drill
Version:	0.9.2
Release:	%mkrel 2
License:	GPL
Group:		Networking/Other
URL:		http://www.nlnetlabs.nl/dnssec/drill.html
Source0:	http://www.nlnetlabs.nl/downloads/drill/%{name}-%{version}.tar.bz2
BuildRequires:	openssl-devel
BuildRequires:	autoconf2.5
BuildRoot:	%{_tmppath}/%{name}-root

%description
Drill is a tool ala dig from BIND. It was designed with DNSSEC in
mind and should be a useful debugging/query tool for DNSSEC. 

%prep

%setup -q -n %{name}
chmod 644 ChangeLog README

%build

%configure2_5x

%make CFLAGS="%{optflags} -fPIC"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 drill %{buildroot}%{_bindir}/
install -m0755 doc/drill.1 %{buildroot}%{_mandir}/man1/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc ChangeLog README 
%{_bindir}/drill
%{_mandir}/man1/drill.1*


