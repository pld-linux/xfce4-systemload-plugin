Summary:	XFce plugin which displays the current system load
Summary(pl):	Wtyczka XFce wy¶wietlaj±ca aktualne obci±¿enie systemu
Name:		xfce4-systemload-plugin
Version:	0.3.2
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	54f940ea77261bb61ca54dd77253c222
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	libxfce4util-devel >= 3.99
BuildRequires:	libxfcegui4-devel >= 3.99
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 3.99.2
Requires:	xfce4-panel >= 3.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A system load plugin for the XFce desktop environment. It displays the
current CPU load, the memory in use, the swap space and the system
uptime in the XFce panel.

%description -l pl
Wtyczka obci±¿enia systemu dla ¶rodowiska XFce. Wy¶wietla obecne
obci±¿enie procesora, u¿ycie pamiêci, pliku wymiany i czasu pracy
systemu w panelu XFce.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.a

%find_lang xfce4-systemload

%clean
rm -rf $RPM_BUILD_ROOT

%files -f xfce4-systemload.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
