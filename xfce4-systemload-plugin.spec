Summary:	Xfce plugin which displays the current system load
Summary(pl):	Wtyczka Xfce wy¶wietlaj±ca aktualne obci±¿enie systemu
Name:		xfce4-systemload-plugin
Version:	0.3.6
Release:	2
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	fd73efa3bd7a73e3f5fdf8d4ed848c1f
Source1:	%{name}-po.pl
Patch0:		%{name}-po_pl.patch
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 3.99.2
Requires:	xfce4-panel >= 3.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A system load plugin for the Xfce desktop environment. It displays the
current CPU load, the memory in use, the swap space and the system
uptime in the Xfce panel.

%description -l pl
Wtyczka obci±¿enia systemu dla ¶rodowiska Xfce. Wy¶wietla obecne
obci±¿enie procesora, u¿ycie pamiêci, pliku wymiany i czasu pracy
systemu w panelu Xfce.

%prep
%setup -q 
install %{SOURCE1} po/pl.po
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%find_lang xfce4-systemload

%clean
rm -rf $RPM_BUILD_ROOT

%files -f xfce4-systemload.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
