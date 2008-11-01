Name: kdenetwork4
Version: 4.1.71
Release: %mkrel 8
Epoch: 3
Group: Development/KDE and Qt
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary: K Desktop Environment - Network Applications
License: GPL
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdenetwork-%version.tar.bz2
Patch0: kdenetwork-4.0.84-fix-desktop-files.patch
Patch1: kdenetwork-4.0.85-kopete.patch
Patch2: kdenetwork-4.1.71-activate-irc.patch
Patch3: kdenetwork-4.1.71-install-headers.patch
#Branch patches
#Patch100:

# Backport patches
#Patch200:

#Testing Patches
Patch300: kdenetwork-4.1.71-test-fixing-jabber-crash.patch

BuildRequires: kde4-macros
BuildRequires: qt4-devel
BuildRequires: freetype2-devel
BuildRequires: gettext
BuildRequires: kdelibs4-devel >= 4.0.83
BuildRequires: kdepimlibs4-devel >= 4.0.83
BuildRequires: kdebase4-workspace-devel >= 4.0.83
BuildRequires: libaudiofile-devel
BuildRequires: bzip2-devel
BuildRequires: jpeg-devel
BuildRequires: lcms-devel
BuildRequires: mng-devel
BuildRequires: png-devel
BuildRequires: libz-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: libopenslp-devel
BuildRequires: libiw-devel
BuildRequires: wireless-tools
BuildRequires: libopenssl-devel
BuildRequires: libidn-devel
BuildRequires: libgsmlib-devel
BuildRequires: mesaglut-devel
BuildRequires: X11-devel
BuildRequires: libxtst-devel
BuildRequires: gmp-devel
BuildRequires: libotr-devel
BuildRequires: mDNSResponder-devel
BuildRequires: libvncserver-devel >= 0.8.2-%mkrel 3
BuildRequires: qca2-devel 
BuildRequires: boost-devel
BuildRequires: qimageblitz-devel
BuildRequires: sqlite3-devel
BuildRequires: decibel-devel
BuildRequires: telepathy-qt-devel
BuildRequires: tapioca-qt-devel
BuildRequires: qca2-devel
BuildRequires: webkitkde-devel
BuildRequires: ortp-devel >= 0.13.1
#add back when WML protocol will be in trunk
#BuildRequires: libmsn-devel
Suggests: kdnssd
Suggests: kget
Suggests: kopete
Suggests: kppp
Suggests: krdc
Suggests: krfb
Suggests: kde4-filesharing
Obsoletes: kde4-lanbrowsing

%description
Networking applications for the K Desktop Environment.

- kdict: graphical client for the DICT protocol.
- kit: AOL instant messenger client, using the TOC protocol
- kpf: public fileserver applet
- krfb: Desktop Sharing server, allow others to access your desktop via VNC
- krdc: a client for Desktop Sharing and other VNC servers

%files
%defattr(-,root,root,-)
%doc README

#----------------------------------------------------------------------

%package core
Summary: %name core files
Group: Graphical desktop/KDE
Requires: kdelibs4-core
Obsoletes: %{_lib}kdenetwork42 <=  2:3.91-0.683133.1
%if %mdkversion >= 200900
Conflicts: kdenetwork-knewsticker < 2:3.5.9-2
Conflicts: kdenetwork-kopete < 2:3.5.9-2
Conflicts: lisa < 2:3.5.9-2
%endif

%description core
Core files for %{name}.

%files core
%defattr(-,root,root)
%_kde_iconsdir/*/*/*/*

#----------------------------------------------------------------------

%package -n kde4-filesharing
Summary: %{name} filesharing
Group: Graphical desktop/KDE
Requires: %name-core >= %epoch:%version
Obsoletes: %name-filesharing < 2:3.93.0-0.714148.1

%description -n kde4-filesharing
%{name} filesharing.

%files -n kde4-filesharing
%defattr(-,root,root)
%_kde_libdir/kde4/fileshare_propsdlgplugin.so
%_kde_libdir/kde4/kcm_fileshare.so
%_kde_libdir/kde4/kcm_kcmsambaconf.so
%_kde_datadir/kde4/services/fileshare.desktop
%_kde_datadir/kde4/services/fileshare_propsdlgplugin.desktop
%_kde_datadir/kde4/services/kcmsambaconf.desktop
%_kde_datadir/kde4/services/ServiceMenus/smb2rdc.desktop

#---------------------------------------------

%package -n kdnssd
Summary:   %{name} kdnssd
Group:     Graphical desktop/KDE
Requires:  %name-core >= %epoch:%version
Obsoletes: %name-kdnssd < 2:3.93.0-0.714148.1
Obsoletes: kde4-lanbrowsing
Obsoletes: kde4-kdnssd < 3:4.0.68
Provides: kde4-kdnssd = %epoch:%version
Conflicts: kdenetwork-common < 2:3.5.9-2mdv

%description -n kdnssd
%{name} kdnssd.

%files -n kdnssd
%defattr(-,root,root)
%dir %_kde_appsdir/remoteview
%_kde_appsdir/remoteview/zeroconf.desktop
%_kde_libdir/kde4/kded_dnssdwatcher.so
%_kde_libdir/kde4/kio_zeroconf.so
%_kde_datadir/kde4/services/kded/dnssdwatcher.desktop
%_kde_datadir/kde4/services/zeroconf.protocol

#---------------------------------------------

%define libkgetcore %mklibname kgetcore 4

%package -n %libkgetcore
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkgetcore
KDE 4 library

%if %mdkversion < 200900
%post -n %libkgetcore -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkgetcore -p /sbin/ldconfig
%endif

%files -n %libkgetcore
%defattr(-,root,root)
%_kde_libdir/libkgetcore.so.*

#---------------------------------------------

%package -n kget
Summary: %{name} kget
Group: Graphical desktop/KDE
Requires: %name-core >= %epoch:%version
Obsoletes: %name-kget < 2:3.93.0-0.714148.1
Obsoletes: %{_lib}kdenetwork42-kget <=  2:3.91-0.683133.1
Obsoletes: kde4-kget < 3:4.0.68
Provides: kde4-kget = %epoch:%version

%description -n kget
An advanced download manager for KDE.

%files -n kget
%defattr(-,root,root)
%_kde_bindir/kget
%dir %_kde_appsdir/kget
%_kde_appsdir/kget/*
%_kde_libdir/kde4/kget_*
%_kde_libdir/kde4/khtml_kget.so
%_kde_libdir/kde4/plasma_engine_kget.so
%_kde_datadir/kde4/services/plasma-engine-kget.desktop
%_kde_datadir/applications/kde4/kget.desktop
%_kde_datadir/kde4/services/ServiceMenus/kget_download.desktop
%_kde_datadir/config.kcfg/kget*
%_kde_datadir/kde4/services/kget_*
%_kde_datadir/kde4/servicetypes/kget_*
%_kde_appsdir/khtml/kpartplugins/kget_plug_in.rc
%_kde_appsdir/webkitpart/kpartplugins/kget_plug_in.rc
%_kde_appsdir/desktoptheme/default/widgets/kget.svg
%_kde_libdir/kde4/kcm_kget_bittorrentfactory.so
%_kde_libdir/kde4/kcm_kget_contentfetchfactory.so
%_kde_libdir/kde4/kcm_kget_mirrorsearchfactory.so
%_kde_libdir/kde4/kcm_kget_multisegkiofactory.so
%_kde_libdir/kde4/plasma_kget_barapplet.so
%_kde_libdir/kde4/plasma_kget_panelbar.so
%_kde_libdir/kde4/plasma_kget_piechart.so
%_kde_datadir/kde4/services/kgetbarapplet-default.desktop
%_kde_datadir/kde4/services/kgetpanelbarapplet-default.desktop
%_kde_datadir/kde4/services/kgetpiechartapplet-default.desktop

%_kde_docdir/HTML/*/kget

#---------------------------------------------

%package -n kopete
Summary: %{name} kopete
Group: Graphical desktop/KDE
Requires: %name-core >= %epoch:%version
Obsoletes: %name-kopete < 2:3.93.0-0.714148.1
Obsoletes: %{_lib}papillon_kopete < 2:3.96.0-0.737162.1
Conflicts: %name-devel < 3:3.96.1-0.740247.1
Obsoletes: kde4-kopete < 3:4.0.68
Provides: kde4-kopete = %epoch:%version
# Provides TLS access to gtalk
Requires: qca2-plugin-openssl-%{_lib}

%description -n kopete
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

%files -n kopete
%defattr(-,root,root)
%_kde_appsdir/kconf_update/kopete-*
%_kde_bindir/kopete
%_kde_bindir/kopete_latexconvert.sh
%_kde_bindir/winpopup-install.sh
%_kde_bindir/winpopup-send.sh
%_kde_libdir/kde4/kcm_kopete_*
%_kde_libdir/kde4/kopete_*
%_kde_libdir/libqgroupwise.so
%_kde_libdir/kde4/libkrichtexteditpart.so
%_kde_datadir/applications/kde4/kopete.desktop
%_kde_datadir/config/kopeterc
%_kde_datadir/config.kcfg/historyconfig.kcfg
%_kde_datadir/config.kcfg/kopeteappearancesettings.kcfg
%_kde_datadir/config.kcfg/kopetebehaviorsettings.kcfg
%_kde_datadir/config.kcfg/latexconfig.kcfg
%_kde_datadir/config.kcfg/nowlisteningconfig.kcfg
%_kde_datadir/kde4/services/aim.protocol
%_kde_datadir/kde4/services/chatwindow.desktop
%_kde_datadir/kde4/services/emailwindow.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_*
%_kde_datadir/kde4/services/kopete_*
%_kde_datadir/kde4/services/xmpp.protocol
%_kde_datadir/kde4/services/irc.protocol
%_kde_datadir/kde4/servicetypes/kopete*
%_kde_datadir/sounds/Kopete_Event.ogg
%_kde_datadir/sounds/Kopete_Received.ogg
%_kde_datadir/sounds/Kopete_Sent.ogg
%_kde_datadir/sounds/Kopete_User_is_Online.ogg
%_kde_appsdir/kopete
%_kde_appsdir/kopete_contactnotes
%_kde_appsdir/kopete_history
%_kde_appsdir/kopete_jabber
%_kde_appsdir/kopete_latex
%_kde_appsdir/kopete_msn
%_kde_appsdir/kopete_privacy
%_kde_appsdir/kopete_statistics
%_kde_appsdir/kopete_translator
%_kde_appsdir/kopete_yahoo
%_kde_appsdir/kopete_irc
%_kde_appsdir/kopete_groupwise
%_kde_appsdir/kopeterichtexteditpart
%_kde_datadir/config.kcfg/urlpicpreview.kcfg
%_kde_docdir/HTML/*/kopete

#---------------------------------------------

%define libgadu_kopete %mklibname gadu_kopete 1

%package -n %libgadu_kopete
Summary: KDE 4 library
Group: System/Libraries

%description -n %libgadu_kopete
KDE 4 library

%if %mdkversion < 200900
%post -n %libgadu_kopete -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libgadu_kopete -p /sbin/ldconfig
%endif

%files -n %libgadu_kopete
%defattr(-,root,root)
%_kde_libdir/libgadu_kopete.so.*

#---------------------------------------------

%define libkyahoo %mklibname kyahoo 1

%package -n %libkyahoo
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkyahoo
KDE 4 library

%if %mdkversion < 200900
%post -n %libkyahoo -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkyahoo -p /sbin/ldconfig
%endif

%files -n %libkyahoo
%defattr(-,root,root)
%_kde_libdir/libkyahoo.so.*

#---------------------------------------------

%define libkopete_videodevice %mklibname kopete_videodevice 4

%package -n %libkopete_videodevice
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopete_videodevice
KDE 4 library

%if %mdkversion < 200900
%post -n %libkopete_videodevice -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkopete_videodevice -p /sbin/ldconfig
%endif

%files -n %libkopete_videodevice
%defattr(-,root,root)
%_kde_libdir/libkopete_videodevice.so.*

#---------------------------------------------

%define libkopeteaddaccountwizard %mklibname kopeteaddaccountwizard 1

%package -n %libkopeteaddaccountwizard
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopeteaddaccountwizard
KDE 4 library

%if %mdkversion < 200900
%post -n %libkopeteaddaccountwizard -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkopeteaddaccountwizard -p /sbin/ldconfig
%endif

%files -n %libkopeteaddaccountwizard
%defattr(-,root,root)
%_kde_libdir/libkopeteaddaccountwizard.so.*

#---------------------------------------------

%define libkopete %mklibname kopete 4

%package -n %libkopete
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kopete5 < 2:3.91-0.689748.1

%description -n %libkopete
KDE 4 library

%if %mdkversion < 200900
%post -n %libkopete -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkopete -p /sbin/ldconfig
%endif

%files -n %libkopete
%defattr(-,root,root)
%_kde_libdir/libkopete.so.*
%_kde_datadir/config.kcfg/kopetestatussettings.kcfg

#---------------------------------------------

%define libkopeteprivacy %mklibname kopeteprivacy 1

%package -n %libkopeteprivacy
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopeteprivacy
KDE 4 library

%if %mdkversion < 200900
%post -n %libkopeteprivacy -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkopeteprivacy -p /sbin/ldconfig
%endif

%files -n %libkopeteprivacy
%defattr(-,root,root)
%_kde_libdir/libkopeteprivacy.so.*

#---------------------------------------------

%define libkopetechatwindow_shared %mklibname kopetechatwindow_shared 1

%package -n %libkopetechatwindow_shared
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopetechatwindow_shared
KDE 4 library

%if %mdkversion < 200900
%post -n %libkopetechatwindow_shared -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkopetechatwindow_shared -p /sbin/ldconfig
%endif

%files -n %libkopetechatwindow_shared
%defattr(-,root,root)
%_kde_libdir/libkopetechatwindow_shared.so.*

#---------------------------------------------

%define libiris_kopete %mklibname iris_kopete 1

%package -n %libiris_kopete
Summary: KDE 4 library
Group: System/Libraries

%description -n %libiris_kopete
KDE 4 library

%if %mdkversion < 200900
%post -n %libiris_kopete -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libiris_kopete -p /sbin/ldconfig
%endif

%files -n %libiris_kopete
%defattr(-,root,root)
%_kde_libdir/libiris_kopete.so.*

#---------------------------------------------

%define libkopete_otr_shared %mklibname kopete_otr_shared 1

%package -n %libkopete_otr_shared
Summary: KDE 4 library
Group: System/Libraries
Conflicts: kopete-otr < 0.8

%description -n %libkopete_otr_shared
KDE 4 library

%if %mdkversion < 200900
%post -n %libkopete_otr_shared -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkopete_otr_shared -p /sbin/ldconfig
%endif

%files -n %libkopete_otr_shared
%defattr(-,root,root)
%_kde_libdir/libkopete_otr_shared.so.*
%dir %_kde_appsdir/kopete_otr
%_kde_appsdir/kopete_otr/*
%_kde_datadir/config.kcfg/kopete_otr.kcfg

#---------------------------------------------

%define libkopetestatusmenu %mklibname kopetestatusmenu 1

%package -n %libkopetestatusmenu
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopetestatusmenu
KDE 4 library

%if %mdkversion < 200900
%post -n %libkopetestatusmenu -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkopetestatusmenu -p /sbin/ldconfig
%endif

%files -n %libkopetestatusmenu
%defattr(-,root,root)
%_kde_libdir/libkopetestatusmenu.so.*

#---------------------------------------------

%define libkopete_oscar %mklibname kopete_oscar 4

%package -n %libkopete_oscar
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopete_oscar
KDE 4 library

%if %mdkversion < 200900
%post -n %libkopete_oscar -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkopete_oscar -p /sbin/ldconfig
%endif

%files -n %libkopete_oscar
%defattr(-,root,root)
%_kde_libdir/libkopete_oscar.so.*

#---------------------------------------------

%define libkopete_msn_shared %mklibname kopete_msn_shared 4

%package -n %libkopete_msn_shared
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kopete_msn_shared5 < 2:3.91-0.689748.1

%description -n %libkopete_msn_shared
KDE 4 library

%if %mdkversion < 200900
%post -n %libkopete_msn_shared -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkopete_msn_shared -p /sbin/ldconfig
%endif

%files -n %libkopete_msn_shared
%defattr(-,root,root)
%_kde_libdir/libkopete_msn_shared.so.*

#---------------------------------------------

%define liboscar %mklibname oscar 1

%package -n %liboscar
Summary: KDE 4 library
Group: System/Libraries

%description -n %liboscar
KDE 4 library

%if %mdkversion < 200900
%post -n %liboscar -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %liboscar -p /sbin/ldconfig
%endif

%files -n %liboscar
%defattr(-,root,root)
%_kde_libdir/liboscar.so.*

#---------------------------------------------

%define libkirc %mklibname kirc 1

%package -n %libkirc
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkirc
KDE 4 library

%if %mdkversion < 200900
%post -n %libkirc -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkirc -p /sbin/ldconfig
%endif

%files -n %libkirc
%defattr(-,root,root)
%_kde_libdir/libkirc.so.*

#---------------------------------------------

%define libkirc_client %mklibname kirc_client 1

%package -n %libkirc_client
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkirc_client
KDE 4 library

%if %mdkversion < 200900
%post -n %libkirc_client -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkirc_client -p /sbin/ldconfig
%endif

%files -n %libkirc_client
%defattr(-,root,root)
%_kde_libdir/libkirc_client.so.*

#---------------------------------------------

%define libkopeteidentity %mklibname kopeteidentity 1

%package -n %libkopeteidentity
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopeteidentity
KDE 4 library

%if %mdkversion < 200900
%post -n %libkopeteidentity -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkopeteidentity -p /sbin/ldconfig
%endif

%files -n %libkopeteidentity
%defattr(-,root,root)
%_kde_libdir/libkopeteidentity.so.*

#---------------------------------------------

%package -n kppp
Summary: %{name} kppp
Group: Graphical desktop/KDE
Requires: %name-core >= %epoch:%version
Requires: ppp
Obsoletes: %name-kppp < 2:3.93.0-0.714148.1
Obsoletes: kde4-kppp < 3:4.0.68
Provides: kde4-kppp = %epoch:%version

%description -n kppp
%{name} kppp.

%files -n kppp
%defattr(-,root,root)
%_kde_appsdir/kppp
%_kde_bindir/kppp
%_kde_bindir/kppplogview
%_kde_datadir/applications/kde4/Kppp.desktop
%_kde_datadir/applications/kde4/kppplogview.desktop
%_kde_docdir/HTML/*/kppp
%exclude %_kde_appsdir/kppp/Rules
%exclude %_kde_appsdir/kppp/Provider

#-----------------------------------------------------------

%package -n kppp-provider
Group: Graphical desktop/KDE
Summary: List of providers for pppd
Conflicts: kppp < 3:4.0.83-2

%description -n kppp-provider
List of providers for kppp

%files -n kppp-provider
%defattr(-,root,root,-)
%_kde_appsdir/kppp/Rules
%_kde_appsdir/kppp/Provider

#---------------------------------------------

%package -n krdc
Summary: %{name} krdc
Group: Graphical desktop/KDE
Requires: %name-core >= %epoch:%version
Obsoletes: %name-krdc < 2:3.93.0-0.714148.1
Obsoletes: kde4-krdc < 3:4.0.68
Provides: kde4-krdc = %epoch:%version

%description -n krdc
KDE Desktop Sharing allows you to invite somebody at a remote
location to watch and possibly control your desktop.

%files -n krdc
%defattr(-,root,root)
%_kde_bindir/krdc
%dir %_kde_appsdir/krdc
%_kde_appsdir/krdc/krdcui.rc
%_kde_appsdir/krdc/pics/*.png
%_kde_datadir/applications/kde4/krdc.desktop
%_kde_datadir/config.kcfg/krdc.kcfg
%_kde_datadir/kde4/services/rdp.protocol
%_kde_datadir/kde4/services/vnc.protocol
%_kde_docdir/HTML/*/krdc

#---------------------------------------------

%package -n krfb
Summary: %{name} krfb
Group: Graphical desktop/KDE
Requires: %name-core >= %epoch:%version
Obsoletes: %name-krfb < 2:3.93.0-0.714148.1
Obsoletes: kde4-krfb < 3:4.0.68
Provides: kde4-krfb = %epoch:%version

%description -n krfb
KDE Desktop Sharing allows you to invite somebody at a remote
location to watch and possibly control your desktop.

%files -n krfb
%defattr(-,root,root)
%_kde_bindir/krfb
%dir %_kde_appsdir/krfb
%_kde_appsdir/krfb/krfb.notifyrc
%_kde_datadir/applications/kde4/krfb.desktop
%_kde_docdir/HTML/*/krfb

#---------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel
Requires: %libkgetcore >= %version
Requires: %libgadu_kopete >= %version
Requires: %libkyahoo >= %version
Requires: %libkopete_videodevice >= %version
Requires: %libkopeteaddaccountwizard >= %version
Requires: %libkopete >= %version
Requires: %libkopeteprivacy >= %version
Requires: %libkopetechatwindow_shared >= %version
Requires: %libiris_kopete >= %version
Requires: %libkopete_oscar >= %version
Requires: %libkopete_msn_shared >= %version
Requires: %liboscar >= %version
Requires: %libkirc_client >= %version
Requires: %libkirc >= %version

%description  devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%exclude %_kde_libdir/libqgroupwise.so
%_kde_includedir/*
%_kde_datadir/dbus-1/interfaces/*

#-------------------------------------------

%prep
%setup -q -n kdenetwork-%version
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch300 -p1

%build
%cmake_kde4 

%make


%install
rm -fr %buildroot

make -C build DESTDIR=%buildroot install

%clean
rm -fr %buildroot


