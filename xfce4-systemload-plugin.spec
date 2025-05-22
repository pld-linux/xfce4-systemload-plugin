Summary:	Xfce plugin which displays the current system load
Summary(pl.UTF-8):	Wtyczka Xfce wyświetlająca aktualne obciążenie systemu
Name:		xfce4-systemload-plugin
Version:	1.4.0
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-systemload-plugin/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	9ccd2912fd985e5bc7265b7e687a2505
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-systemload-plugin
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libgtop-devel >= 2.32.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	libxfce4util-devel >= 4.17.2
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	upower-devel >= 0.99.0
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
BuildRequires:	xfconf-devel >= 4.16.0
Requires:	xfce4-panel >= 4.16.0
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
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS COPYING
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libsystemload.so
%{_datadir}/xfce4/panel/plugins/systemload.desktop
%{_iconsdir}/hicolor/*x*/apps/org.xfce.panel.systemload.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.panel.systemload.svg
