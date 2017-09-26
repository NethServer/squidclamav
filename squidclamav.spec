%define _unpackaged_files_terminate_build 0

Name: squidclamav
Version: 6.16
Release: 1%{?dist}
Summary: A Clamav Antivirus Redirector for Squid
License: GPLv3+
URL: http://squidclamav.darold.net/
Source0: https://github.com/darold/squidclamav/archive/v%{version}.tar.gz
BuildRequires:	clamav-devel >= 0.82
BuildRequires:	curl-devel >= 7.12.1
BuildRequires:  c-icap-devel
Requires:	squid, c-icap

%description
%{name} Antivirus redirector for Squid proxy based on the Awards winnings
ClamAv anti-virus toolkit. Using it will help you securing your home or
enterprise network web traffic. SquidClamav is the most efficient Squid
Redirector anti-virus tool for HTTP traffic available for free, it is written
in C and can handle thousand of connections.

%prep
%setup -q

%build
%configure --prefix=/usr --with-c-icap=%{_libdir}/c_icap --libexecdir=/var/www/cgi-bin
%{__make}

%install
%{__rm} -rf %{buildroot}
# set up path structure
%{__install} -d -m 0755 %{buildroot}/%{_bindir}
%{__install} -d -m 0755 %{buildroot}/%{_sysconfdir}
%{__install} -d -m 0755 %{buildroot}/%{_libexecdir}

# Make distrib files
%{__make} install \
        DESTDIR=%{buildroot}

%{__install} -D -m 0644 doc/%{name}.1 \
    %{buildroot}/%{_mandir}/man1/%{name}.1

find %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/c-icap/%{name}.conf
%attr(0644,root,root) %{_mandir}/man1/%{name}.1.gz
%attr(0644,root,root) %{_datadir}/%{name}/README
%attr(0755,root,root) /var/www/cgi-bin/%{name}/clwarn.cgi
%attr(0755,root,root) /var/www/cgi-bin/%{name}/clwarn.cgi.de_DE
%attr(0755,root,root) /var/www/cgi-bin/%{name}/clwarn.cgi.en_EN
%attr(0755,root,root) /var/www/cgi-bin/%{name}/clwarn.cgi.fr_FR
%attr(0755,root,root) /var/www/cgi-bin/%{name}/clwarn.cgi.pt_BR
%attr(0755,root,root) /var/www/cgi-bin/%{name}/clwarn.cgi.ru_RU
%{_libdir}/c_icap/squidclamav.so

%changelog
* Tue Sep 26 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 6.16-1
- update to 6.16

* Wed Jan 20 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 6.15-1
- update to 6.15

* Thu May 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 6.10-1
- enable c-icap support
- update to 6.10

* Tue Nov 27 2012 Daniel Berteaud <daniel@firewall-services.com> - 5.11-1
- update to 5.11

* Tue Oct 16 2012 Daniel Berteaud <daniel@firewall-services.com> - 5.9-1
- update to 5.9

* Tue Sep 11 2012 Daniel Berteaud <daniel@firewall-services.com> - 5.8-1
- update to 5.8

* Wed Mar  3 2010 Gilles Darold <gilles@darold.net>
- Update to 5.2.
- Add copy of clwarn.cgi.ru_RU into libexecdir.

* Wed Feb 10 2010 Gilles Darold <gilles@darold.net>
- Update to 5.1.

* Wed Jan 27 2010 Gordan Bobic <gordan@bobich.net>
- Update for squidclamav 4.2

* Tue Jan 12 2010 Gordan Bobic <gordan@bobich.net>
- Initial fork from the PLD spec file, update for squidclamav 4.1

