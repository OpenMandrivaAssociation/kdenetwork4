%define revision 689748
%define support_ldap 1

%define _kde_includedir %_kde_prefix/include
%define _kde_sbindir %_kde_prefix/sbin

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %unstable
%define dont_strip 1
%endif


Name: kdenetwork4
Version: 3.91
Release: %mkrel 0.%revision.1
Epoch: 2
Group: Development/KDE and Qt
Summary: K Desktop Environment - Network Applications
License: GPL
URL: http://www.kde.org
%if %branch
Source: 	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdenetwork-%version.%revision.tar.bz2
%else
Source: 	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdenetwork-%version.tar.bz2
%endif
Source1: kdenetwork3-kppp.pamd
Source2: kdenetwork-lisa
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires:  freetype2-devel
BuildRequires:  gettext
BuildRequires:  kdelibs4-devel
BuildRequires:  libaudiofile-devel
BuildRequires:  bzip2-devel
BuildRequires:  jpeg-devel
BuildRequires:  lcms-devel
BuildRequires:  mng-devel
BuildRequires:  png-devel
BuildRequires:  libz-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  libopenslp-devel
BuildRequires:  libiw-devel
BuildRequires:  wireless-tools
BuildRequires:  libopenssl-devel
BuildRequires:  kdebase4-devel
BuildRequires:  kdepimlibs4-devel
BuildRequires:  libidn-devel
BuildRequires:  libgsmlib-devel
BuildRequires:  mesaglut-devel
BuildRequires:  X11-devel
BuildRequires:  libxtst-devel
BuildRequires:	mDNSResponder-devel
BuildRequires:	libvncserver-devel >= 0.8.2-%mkrel 3
BuildRequires:  decibel-devel
BuildRequires: qca2-devel 
Requires: kde4-kget
Requires: kde4-krfb
Requires: kde4-kopete
Requires: kde4-knewsticker
Requires: kde4-kppp

%description
Networking applications for the K Desktop Environment.

- kdict: graphical client for the DICT protocol.
- kit: AOL instant messenger client, using the TOC protocol
- knewsticker: RDF newsticker applet
- kpf: public fileserver applet
- lanbrowsing: lan browsing kio slave
- krfb: Desktop Sharing server, allow others to access your desktop via VNC
- krdc: a client for Desktop Sharing and other VNC servers

%files

#-----------------------------------------------------------

%package core
Summary:	Common files for kdenetwork
Group:		Graphical desktop/KDE
Obsoletes: %name-common
Obsoletes: %{_lib}kdenetwork42-kwifimanager

%description core
Common files for kdenetwork

%files core
%defattr(-,root,root,-)
%_kde_libdir/kde4/kio_zeroconf.*

%_kde_appsdir/remoteview/*

%dir %_kde_appsdir/zeroconf/
%_kde_appsdir/zeroconf/*
%_kde_datadir/kde4/services/kded/dnssdwatcher.desktop
%_kde_datadir/kde4/services/fileshare.desktop
%_kde_datadir/kde4/services/kcmsambaconf.desktop
%_kde_libdir/kde4/kded_dnssdwatcher.*
%_kde_datadir/kde4/services/zeroconf.protocol
%_kde_datadir/dbus-1/interfaces/org.kde.kdnssd.xml
%_kde_libdir/kde4/fileshare_propsdlgplugin.so
%_kde_libdir/kde4/kcm_fileshare.so
%_kde_libdir/kde4/kcm_kcmsambaconf.so
%_kde_libdir/kde4/libkrichtexteditpart.so
%_kde_datadir/kde4/services/fileshare_propsdlgplugin.desktop
%_kde_iconsdir/*/*/*/*

#-----------------------------------------------------------

%package -n kde4-kopete
Group: Graphical desktop/KDE
Summary: Kopete
Requires: %name-core
Requires: decibel
Requires: jasper
Obsoletes: kdenetwork4-kopete
BuildConflicts: xmms-devel

%description -n kde4-kopete
Kopete is a flexible and extendable multiple protocol instant messaging
system designed as a plugin-based system.

All protocols are plugins and allow modular installment, configuration,
and usage without the main application knowing anything about the plugin 
being loaded.

The goal of Kopete is to provide users with a standard and easy to use 
interface between all of their instant messaging systems, but at the same
time also providing developers with the ease of writing plugins to support
a new protocol.

The core Kopete development team provides a handful of plugins that most
users can use, in addition to templates for new developers to base a 
plugin off of.

%files -n kde4-kopete
%defattr(-,root,root,-)
%_kde_bindir/kopete
%_kde_bindir/winpopup-install.sh
%_kde_bindir/winpopup-send.sh
%_kde_libdir/kde4/kcm_kopete_*
%_kde_libdir/kde4/kopete_*
%_kde_datadir/dbus-1/interfaces/org.kde.kopete.Client.xml
%_kde_appsdir/kconf_update/kopete*
%_kde_datadir/applications/kde4/kopete.desktop
%_kde_datadir/kde4/services/kopete_*.desktop
%_kde_datadir/kde4/servicetypes/kopete*.desktop
%_kde_datadir/sounds/Kopete_*.ogg
%_kde_datadir/kde4/services/aim.protocol
%_kde_datadir/kde4/services/chatwindow.desktop
%_kde_datadir/kde4/services/emailwindow.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_*.desktop
%_kde_appsdir/kopete*
%_kde_datadir/config.kcfg/historyconfig.kcfg
%_kde_datadir/config.kcfg/kopete*
%_kde_datadir/config.kcfg/nowlisteningconfig.kcfg
%_kde_docdir/HTML/en/kopete
%exclude %_kde_appsdir/kopete_latex

#-----------------------------------------------------------

%package  -n kde4-kopete-latex
Group: Graphical desktop/KDE
Summary: Kopete latex plugin for write andd read mesages in latex
Requires: kde4-kopete
Requires: ImageMagick	

%description -n kde4-kopete-latex
Kopete latex plugin for write andd read mesages in latexinder

%files -n kde4-kopete-latex
%defattr(-,root,root,-)
%_kde_bindir/kopete_latexconvert.sh
%_kde_appsdir/kopete_latex
%_kde_datadir/config.kcfg/latexconfig.kcfg
%_kde_libdir/kde4/kopete_latex.so

#-----------------------------------------------------------

%package -n kde4-lisa
Group: Graphical desktop/KDE
Summary: Lisa server
Requires: %name-core 
Obsoletes: lisa4

%description -n kde4-lisa
LISa is intended to provide a kind of "network neighbourhood" but only
relying on the TCP/IP protocol stack, no smb or whatever.

%post -n kde4-lisa
%_post_service kde4-lisa

%preun -n kde4-lisa
%_preun_service lisa4

%files -n kde4-lisa
%defattr(-,root,root)
%config(noreplace) /etc/rc.d/init.d/lisa4
%_kde_libdir/kde4/kcm_lanbrowser.so
%_kde_libdir/kde4/kio_lan.so
%_kde_sbindir/lisad
%dir %_kde_appsdir/konqsidebartng/virtual_folders/services/
%_kde_appsdir/konqsidebartng/virtual_folders/services/lisa.desktop
%dir %_kde_appsdir/konqueror/dirtree/remote/
%_kde_appsdir/konqueror/dirtree/remote/lan.desktop
%_kde_appsdir/konqueror/servicemenus/smb2rdc.desktop
%_kde_appsdir/lisa/README
%_kde_datadir/kde4/services/kcmkiolan.desktop
%_kde_datadir/kde4/services/kcmlisa.desktop
%_kde_datadir/kde4/services/lan.protocol
%_kde_datadir/kde4/services/rdp.protocol
%dir %_kde_docdir/HTML/en/lanbrowser/
%doc %_kde_docdir/HTML/en/lanbrowser/*.docbook
%doc %_kde_docdir/HTML/en/lanbrowser/*.bz2
%dir %_kde_docdir/HTML/en/lisa/
%doc %_kde_docdir/HTML/en/lisa/*.docbook
%doc %_kde_docdir/HTML/en/lisa/*.bz2

#-----------------------------------------------------------

%package -n kde4-kppp
Group: Graphical desktop/KDE
Summary: Dialer and front end for pppd
Obsoletes: knetwork4-kppp
Obsoletes: kdenetwork4-kppp-provider
Requires: %name-core
Requires: ppp 

%description -n kde4-kppp
Kppp is a dialer and front end for pppd.

%files -n kde4-kppp
%defattr(-,root,root,-)
%dir %_sysconfdir/pam.d/
%config(noreplace) %_sysconfdir/pam.d/kppp
%attr(4755,root,root) %_kde_bindir/kppp
%_kde_bindir/kppplogview
%dir %_kde_appsdir/kppp
%_kde_appsdir/kppp
%_kde_datadir/applications/kde4/Kppp.desktop
%_kde_datadir/applications/kde4/kppplogview.desktop
%_kde_datadir/dbus-1/interfaces/org.kde.kppp.xml
%doc %_kde_docdir/HTML/en/kppp

#-----------------------------------------------------------

%package -n kde4-kget
Group: Graphical desktop/KDE
Summary: Kget program
Obsoletes: kdenetwork4-kget
Requires: %name-core

%description -n kde4-kget
An advanced download manager for KDE.

%files -n kde4-kget
%defattr(-,root,root,-)
%doc %_kde_docdir/HTML/en/kget
%_kde_bindir/kget
%_kde_datadir/applications/kde4/kget.desktop
%_kde_datadir/kde4/services/kget_kiofactory.desktop
%_kde_datadir/kde4/services/kget_multisegkiofactory.desktop
%_kde_datadir/kde4/servicetypes/kget_plugin.desktop
%_kde_datadir/sounds/KGet_Added.ogg
%_kde_datadir/sounds/KGet_Finished.ogg
%_kde_datadir/sounds/KGet_Finished_All.ogg
%_kde_datadir/sounds/KGet_Started.ogg
%_kde_appsdir/kget
%_kde_appsdir/khtml/kpartplugins/kget_plug_in.rc
%_kde_appsdir/konqueror/servicemenus/kget_download.desktop
%_kde_datadir/config.kcfg/kget.kcfg
%_kde_datadir/config.kcfg/kget_multisegkiofactory.kcfg
%_kde_libdir/kde4/khtml_kget.so
%_kde_libdir/kde4/libkget_kiofactory.so
%_kde_libdir/kde4/libkget_multisegkiofactory.so

#-----------------------------------------------------------

%define libkgetcore %mklibname kgetcore 4

%package -n %libkgetcore
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdenetwork42-kget
Obsoletes: %{_lib}kgetcore5

%description -n %libkgetcore
KDE 4 library.

%post -n %libkgetcore -p /sbin/ldconfig
%postun -n %libkgetcore -p /sbin/ldconfig

%files -n %libkgetcore
%defattr(-,root,root)
%_kde_libdir/libkgetcore.so.*

#-----------------------------------------------------------

%package -n kde4-krfb
Group: Graphical desktop/KDE
Summary: Krfb, Krdc program
Obsoletes: kdenetwork4-krfb
Requires: %name-core

%description -n kde4-krfb
KDE Desktop Sharing allows you to invite somebody at a remote 
location to watch and possibly control your desktop.

%files -n kde4-krfb
%defattr(-,root,root,-)
%_kde_bindir/krdc
%_kde_bindir/krfb
%_kde_datadir/kde4/services/vnc.protocol
%dir %_kde_appsdir/krdc/
%_kde_appsdir/krdc/*
%_kde_datadir/applications/kde4/krdc.desktop
%_kde_datadir/applications/kde4/krfb.desktop
%_kde_appsdir/krfb
%doc %_kde_docdir/HTML/*/krdc
%doc %_kde_docdir/HTML/*/krfb

#-----------------------------------------------------------

%package -n kde4-knewsticker
Group: Graphical desktop/KDE
Summary: RDF newsticker applet
Obsoletes: kdenetwork4-knewsticker
Requires: %name-core

%description -n kde4-knewsticker
Knewsticker: RDF newsticker applet

%files -n kde4-knewsticker
%defattr(-,root,root,-)
%_kde_bindir/knewstickerstub 
%_kde_libdir/kde4/knewsticker_panelapplet.so
%_kde_datadir/applications/kde4/knewsticker-standalone.desktop
%_kde_appsdir/knewsticker
%_kde_appsdir/kicker/applets/knewsticker.desktop
%dir %_kde_appsdir/kconf_update/
%_kde_appsdir/kconf_update/knewsticker.upd
%_kde_appsdir/kconf_update/knt-0.1-0.2.pl
%_kde_datadir/applnk/.hidden/knewstickerstub.desktop
%doc %_kde_docdir/HTML/en/knewsticker

#-----------------------------------------------------------

%define libpapillon_kopete %mklibname papillon_kopete 1

%package -n %libpapillon_kopete
Summary: KDE 4 library
Group: System/Libraries

%description -n %libpapillon_kopete
KDE 4 library.

%post -n %libpapillon_kopete -p /sbin/ldconfig
%postun -n %libpapillon_kopete -p /sbin/ldconfig

%files -n %libpapillon_kopete
%defattr(-,root,root)
%_kde_libdir/libpapillon_kopete.so.*

#-----------------------------------------------------------

%define libgadu_kopete %mklibname gadu_kopete 1

%package -n %libgadu_kopete
Summary: KDE 4 library
Group: System/Libraries

%description -n %libgadu_kopete
KDE 4 library.

%post -n %libgadu_kopete -p /sbin/ldconfig
%postun -n %libgadu_kopete -p /sbin/ldconfig

%files -n %libgadu_kopete
%defattr(-,root,root)
%_kde_libdir/libgadu_kopete.so.*

#-----------------------------------------------------------------------------

%define libkopete %mklibname kopete 5

%package -n %libkopete
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopete
KDE 4 library.

%post -n %libkopete -p /sbin/ldconfig
%postun -n %libkopete -p /sbin/ldconfig

%files -n %libkopete
%defattr(-,root,root)
%_kde_libdir/libkopete.so.*

#-----------------------------------------------------------------------------

%define libkopete_msn_shared %mklibname kopete_msn_shared 5

%package -n %libkopete_msn_shared
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopete_msn_shared
KDE 4 library.

%post -n %libkopete_msn_shared -p /sbin/ldconfig
%postun -n %libkopete_msn_shared -p /sbin/ldconfig

%files -n %libkopete_msn_shared
%defattr(-,root,root)
%_kde_libdir/libkopete_msn_shared.so.*

#-----------------------------------------------------------------------------

%define libkopete_oscar %mklibname kopete_oscar 5

%package -n %libkopete_oscar
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopete_oscar
KDE 4 library.

%post -n %libkopete_oscar -p /sbin/ldconfig
%postun -n %libkopete_oscar -p /sbin/ldconfig

%files -n %libkopete_oscar
%defattr(-,root,root)
%_kde_libdir/libkopete_oscar.so.*

#-----------------------------------------------------------------------------

%define libkopete_videodevice %mklibname kopete_videodevice 5

%package -n %libkopete_videodevice
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopete_videodevice
KDE 4 library.

%post -n %libkopete_videodevice -p /sbin/ldconfig
%postun -n %libkopete_videodevice -p /sbin/ldconfig

%files -n %libkopete_videodevice
%defattr(-,root,root)
%_kde_libdir/libkopete_videodevice.so.*

#-----------------------------------------------------------------------------

%define libkopeteaddaccountwizard %mklibname kopeteaddaccountwizard 1

%package -n %libkopeteaddaccountwizard
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopeteaddaccountwizard
KDE 4 library.

%post -n %libkopeteaddaccountwizard -p /sbin/ldconfig
%postun -n %libkopeteaddaccountwizard -p /sbin/ldconfig

%files -n %libkopeteaddaccountwizard
%defattr(-,root,root)
%_kde_libdir/libkopeteaddaccountwizard.so.*

#-----------------------------------------------------------------------------

%define libkopetechatwindow_shared %mklibname kopetechatwindow_shared 1

%package -n %libkopetechatwindow_shared
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopetechatwindow_shared
KDE 4 library.

%post -n %libkopetechatwindow_shared -p /sbin/ldconfig
%postun -n %libkopetechatwindow_shared -p /sbin/ldconfig

%files -n %libkopetechatwindow_shared
%defattr(-,root,root)
%_kde_libdir/libkopetechatwindow_shared.so.*

#-----------------------------------------------------------------------------

%define libkopeteprivacy %mklibname kopeteprivacy 1

%package -n %libkopeteprivacy
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopeteprivacy
KDE 4 library.

%post -n %libkopeteprivacy -p /sbin/ldconfig
%postun -n %libkopeteprivacy -p /sbin/ldconfig

%files -n %libkopeteprivacy
%defattr(-,root,root)
%_kde_libdir/libkopeteprivacy.so.*

#-----------------------------------------------------------------------------

%define libkyahoo %mklibname kyahoo 1

%package -n %libkyahoo
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkyahoo
KDE 4 library.

%post -n %libkyahoo -p /sbin/ldconfig
%postun -n %libkyahoo -p /sbin/ldconfig

%files -n %libkyahoo
%defattr(-,root,root)
%_kde_libdir/libkyahoo.so.*

#-----------------------------------------------------------------------------

%define liboscar %mklibname oscar 1

%package -n %liboscar
Summary: KDE 4 library
Group: System/Libraries

%description -n %liboscar
KDE 4 library.

%post -n %liboscar -p /sbin/ldconfig
%postun -n %liboscar -p /sbin/ldconfig

%files -n %liboscar
%defattr(-,root,root)
%_kde_libdir/liboscar.so.*

#-----------------------------------------------------------

%package devel
Summary: Devel stuff for kdenetwork
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel
Requires: %name-core
Requires: %libkgetcore
Requires: %libpapillon_kopete
Requires: %libgadu_kopete
Requires: %libkopete
Requires: %libkopete_msn_shared
Requires: %libkopete_oscar
Requires: %libkopete_videodevice
Requires: %libkopeteaddaccountwizard
Requires: %libkopetechatwindow_shared
Requires: %libkopeteprivacy
Requires: %libkyahoo
Requires: %liboscar
Obsoletes: %{_lib}kdenetwork42-devel
Obsoletes: %{_lib}kdenetwork42-kopete-devel
Obsoletes: %{_lib}kdebetwork42-kget-devel

%description  devel
This package contains header files needed if you wish to build applications based on kdegraphics.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%_kde_prefix/include/*

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdenetwork-%version

%build
cd $RPM_BUILD_DIR/kdenetwork-%version

%cmake_kde4 \
       -DDBUS_SERVICES_DIR=%_kde_datadir/dbus-1/services \
       -DDBUS_INTERFACES_DIR=%_kde_datadir/dbus-1/interfaces \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=debugfull
%endif


%make


%install
rm -fr %buildroot
cd $RPM_BUILD_DIR/kdenetwork-%version/build/

make DESTDIR=%buildroot install

install -d -m 0755 %buildroot%_sysconfdir/rc.d/init.d
install -m 0755 %SOURCE2 %buildroot%_sysconfdir/rc.d/init.d/lisa4


#TODO install it into real sysconfig dir
install -d -m 0755 %buildroot/%_sysconfdir/pam.d/
install -m 0644 %SOURCE1 %buildroot/%_sysconfdir/pam.d/kppp

%clean
rm -fr %buildroot


