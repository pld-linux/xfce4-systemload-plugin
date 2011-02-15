Summary:	Xfce plugin which displays the current system load
Summary(pl.UTF-8):	Wtyczka Xfce wyświetlająca aktualne obciążenie systemu
Name:		xfce4-systemload-plugin
Version:	1.0.0
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-systemload-plugin/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	da4f0e8bfb57e18fe3e3e56507a681f7
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-systemload-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A system load plugin for the Xfce desktop environment. It displays the
current CPU load, the memory in use, the swap space and the system
uptime in the Xfce panel.

%description -l pl.UTF-8
Wtyczka obciążenia systemu dla środowiska Xfce. Wyświetla obecne
obciążenie procesora, użycie pamięci, pliku wymiany i czasu pracy
systemu w panelu Xfce.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/%{name}
%{_datadir}/xfce4/panel-plugins/systemload.desktop
