Summary:	Tool ala dig from BIND
Name:		drill
Version:	0.9.2
Release:	8
License:	GPL
Group:		Networking/Other
URL:		https://www.nlnetlabs.nl/dnssec/drill.html
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




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-7mdv2011.0
+ Revision: 610282
- rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 0.9.2-6mdv2010.1
+ Revision: 537460
- rebuild

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.9.2-5mdv2010.0
+ Revision: 428373
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.9.2-4mdv2009.0
+ Revision: 244547
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9.2-2mdv2008.1
+ Revision: 170802
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.9.2-1mdv2008.1
+ Revision: 140722
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 02 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-1mdv2007.0
+ Revision: 131181
- Import drill

* Fri Feb 03 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-1mdk
- 0.9.2

* Fri Jan 07 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-1mdk
- 0.9.1

* Tue Nov 23 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.8.1-1mdk
- initial mandrake package

