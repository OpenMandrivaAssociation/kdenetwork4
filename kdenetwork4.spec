%define revision 695413
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
Version: 3.92.0
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
Requires: kde4-filesharing
Requires: kde4-kdnssd
Requires: kde4-kget
Requires: kde4-knewsticker
Requires: kde4-kopete
Requires: kde4-kppp
Requires: kde4-krdc
Requires: kde4-krfb
Requires: kde4-lanbrowsing

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
%defattr(-,root,root,-)
%doc README

#----------------------------------------------------------------------

%package core
Summary: %name core files
Group: Graphical desktop/KDE
Requires: kdelibs4-core

%description core
Core files for %{name}.

%files core
%defattr(-,root,root)
%_kde_iconsdir/*/*/*/*

#----------------------------------------------------------------------

%package -n kde4-filesharing
Summary: %{name} filesharing
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-filesharing

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

#---------------------------------------------

%package -n kde4-kdnssd
Summary: %{name} kdnssd
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kdnssd

%description -n kde4-kdnssd
%{name} kdnssd.

%files -n kde4-kdnssd
%defattr(-,root,root)
%_kde_appsdir/remoteview
%_kde_appsdir/zeroconf
%_kde_libdir/kde4/kded_dnssdwatcher.so
%_kde_libdir/kde4/kio_zeroconf.so
%_kde_datadir/kde4/services/kded/dnssdwatcher.desktop
%_kde_datadir/kde4/services/zeroconf.protocol
%_datadir/dbus-1/interfaces/org.kde.kdnssd.xml

#---------------------------------------------

%define libkgetcore %mklibname kgetcore 4

%package -n %libkgetcore
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkgetcore
KDE 4 library

%post -n %libkgetcore -p /sbin/ldconfig
%postun -n %libkgetcore -p /sbin/ldconfig

%files -n %libkgetcore
%defattr(-,root,root)
%_kde_libdir/libkgetcore.so.*

#---------------------------------------------

%package -n kde4-knewsticker
Summary: %{name} knewsticker
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-knewsticker

%description -n kde4-knewsticker
%{name} knewsticker.

%files -n kde4-knewsticker
%defattr(-,root,root)
%_kde_appsdir/knewsticker
%_kde_appsdir/kconf_update
%_kde_appsdir/kicker
%_kde_bindir/knewstickerstub
%_kde_datadir/applnk/.hidden/knewstickerstub.desktop
%_kde_libdir/kde4/knewsticker_panelapplet.so
%_kde_datadir/applications/kde4/knewsticker-standalone.desktop
%_kde_docdir/HTML/*/knewsticker

#---------------------------------------------

%package -n kde4-kget
Summary: %{name} kget
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kget

%description -n kde4-kget
%{name} kget.

%files -n kde4-kget
%defattr(-,root,root)
%_kde_bindir/kget
%_kde_appsdir/kget
%_kde_libdir/kde4/khtml_kget.so
%_kde_libdir/kde4/libkget_*
%_kde_datadir/applications/kde4/kget.desktop
%_kde_datadir/config.kcfg/kget*
%_kde_datadir/kde4/services/kget_*
%_kde_datadir/kde4/servicetypes/kget_*
%_kde_datadir/apps/khtml/kpartplugins/kget_plug_in.rc
%_kde_datadir/sounds/KGet*
%_kde_docdir/HTML/*/kget

#---------------------------------------------

%package -n kde4-kopete
Summary: %{name} kopete
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kopete

%description -n kde4-kopete
%{name} kopete.

%files -n kde4-kopete
%defattr(-,root,root)
%_kde_appsdir/kconf_update
%_kde_appsdir/kopete_privacy
%_kde_appsdir/kopeterichtexteditpart
%_kde_appsdir/kopete_latex
%_kde_appsdir/kopete_yahoo
%_kde_appsdir/kopete_contactnotes
%_kde_appsdir/kopete_jabber
%_kde_appsdir/kopete_translator
%_kde_appsdir/kopete
%_kde_appsdir/kopete_msn
%_kde_appsdir/kopete_history
%_kde_bindir/kopete
%_kde_bindir/kopete_latexconvert.sh
%_kde_bindir/winpopup-install.sh
%_kde_bindir/winpopup-send.sh
%_kde_libdir/kde4/kcm_kopete_accountconfig.so
%_kde_libdir/kde4/kcm_kopete_addbookmarks.so
%_kde_libdir/kde4/kcm_kopete_alias.so
%_kde_libdir/kde4/kcm_kopete_appearanceconfig.so
%_kde_libdir/kde4/kcm_kopete_autoreplace.so
%_kde_libdir/kde4/kcm_kopete_behaviorconfig.so
%_kde_libdir/kde4/kcm_kopete_chatwindowconfig.so
%_kde_libdir/kde4/kcm_kopete_highlight.so
%_kde_libdir/kde4/kcm_kopete_history.so
%_kde_libdir/kde4/kcm_kopete_identityconfig.so
%_kde_libdir/kde4/kcm_kopete_latex.so
%_kde_libdir/kde4/kcm_kopete_nowlistening.so
%_kde_libdir/kde4/kcm_kopete_pluginconfig.so
%_kde_libdir/kde4/kcm_kopete_privacy.so
%_kde_libdir/kde4/kcm_kopete_texteffect.so
%_kde_libdir/kde4/kcm_kopete_translator.so
%_kde_libdir/kde4/kcm_kopete_webpresence.so
%_kde_libdir/kde4/kopete_*
%_kde_libdir/kde4/libkrichtexteditpart.so
%_kde_datadir/applications/kde4/kopete.desktop
%_kde_datadir/config.kcfg/historyconfig.kcfg
%_kde_datadir/config.kcfg/kopeteappearancesettings.kcfg
%_kde_datadir/config.kcfg/kopetebehaviorsettings.kcfg
%_kde_datadir/config.kcfg/kopetegeneralsettings.kcfg
%_kde_datadir/config.kcfg/kopeteidentityconfigpreferences.kcfg
%_kde_datadir/config.kcfg/latexconfig.kcfg
%_kde_datadir/config.kcfg/nowlisteningconfig.kcfg
%_kde_datadir/kde4/services/aim.protocol
%_kde_datadir/kde4/services/chatwindow.desktop
%_kde_datadir/kde4/services/emailwindow.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_addbookmarks_config.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_alias_config.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_autoreplace_config.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_highlight_config.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_history_config.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_latex_config.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_nowlistening_config.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_privacy_config.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_texteffect_config.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_translator_config.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_webpresence_config.desktop
%_kde_datadir/kde4/services/kopete_accountconfig.desktop
%_kde_datadir/kde4/services/kopete_addbookmarks.desktop
%_kde_datadir/kde4/services/kopete_aim.desktop
%_kde_datadir/kde4/services/kopete_alias.desktop
%_kde_datadir/kde4/services/kopete_appearanceconfig.desktop
%_kde_datadir/kde4/services/kopete_autoreplace.desktop
%_kde_datadir/kde4/services/kopete_behaviorconfig.desktop
%_kde_datadir/kde4/services/kopete_chatwindowconfig.desktop
%_kde_datadir/kde4/services/kopete_connectionstatus.desktop
%_kde_datadir/kde4/services/kopete_contactnotes.desktop
%_kde_datadir/kde4/services/kopete_gadu.desktop
%_kde_datadir/kde4/services/kopete_highlight.desktop
%_kde_datadir/kde4/services/kopete_history.desktop
%_kde_datadir/kde4/services/kopete_icq.desktop
%_kde_datadir/kde4/services/kopete_identityconfig.desktop
%_kde_datadir/kde4/services/kopete_jabber.desktop
%_kde_datadir/kde4/services/kopete_latex.desktop
%_kde_datadir/kde4/services/kopete_messenger.desktop
%_kde_datadir/kde4/services/kopete_msn.desktop
%_kde_datadir/kde4/services/kopete_nowlistening.desktop
%_kde_datadir/kde4/services/kopete_pluginconfig.desktop
%_kde_datadir/kde4/services/kopete_privacy.desktop
%_kde_datadir/kde4/services/kopete_qq.desktop
%_kde_datadir/kde4/services/kopete_sms.desktop
%_kde_datadir/kde4/services/kopete_testbed.desktop
%_kde_datadir/kde4/services/kopete_texteffect.desktop
%_kde_datadir/kde4/services/kopete_translator.desktop
%_kde_datadir/kde4/services/kopete_webpresence.desktop
%_kde_datadir/kde4/services/kopete_wp.desktop
%_kde_datadir/kde4/services/kopete_yahoo.desktop
%_kde_datadir/kde4/services/xmpp.protocol
%_kde_datadir/kde4/servicetypes/kopeteplugin.desktop
%_kde_datadir/kde4/servicetypes/kopeteprotocol.desktop
%_kde_datadir/kde4/servicetypes/kopeteui.desktop
%_kde_datadir/sounds/Kopete_Event.ogg
%_kde_datadir/sounds/Kopete_Received.ogg
%_kde_datadir/sounds/Kopete_Sent.ogg
%_kde_datadir/sounds/Kopete_User_is_Online.ogg
%_datadir/dbus-1/interfaces/org.kde.kopete.Client.xml
%_kde_docdir/HTML/*/kopete

#---------------------------------------------

%define libgadu_kopete %mklibname gadu_kopete 1

%package -n %libgadu_kopete
Summary: KDE 4 library
Group: System/Libraries

%description -n %libgadu_kopete
KDE 4 library

%post -n %libgadu_kopete -p /sbin/ldconfig
%postun -n %libgadu_kopete -p /sbin/ldconfig

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

%post -n %libkyahoo -p /sbin/ldconfig
%postun -n %libkyahoo -p /sbin/ldconfig

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

%post -n %libkopete_videodevice -p /sbin/ldconfig
%postun -n %libkopete_videodevice -p /sbin/ldconfig

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

%post -n %libkopeteaddaccountwizard -p /sbin/ldconfig
%postun -n %libkopeteaddaccountwizard -p /sbin/ldconfig

%files -n %libkopeteaddaccountwizard
%defattr(-,root,root)
%_kde_libdir/libkopeteaddaccountwizard.so.*

#---------------------------------------------

%define libkopete %mklibname kopete 4

%package -n %libkopete
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopete
KDE 4 library

%post -n %libkopete -p /sbin/ldconfig
%postun -n %libkopete -p /sbin/ldconfig

%files -n %libkopete
%defattr(-,root,root)
%_kde_libdir/libkopete.so.*

#---------------------------------------------

%define libpapillon_kopete %mklibname papillon_kopete 1

%package -n %libpapillon_kopete
Summary: KDE 4 library
Group: System/Libraries

%description -n %libpapillon_kopete
KDE 4 library

%post -n %libpapillon_kopete -p /sbin/ldconfig
%postun -n %libpapillon_kopete -p /sbin/ldconfig

%files -n %libpapillon_kopete
%defattr(-,root,root)
%_kde_libdir/libpapillon_kopete.so.*

#---------------------------------------------

%define libkopeteprivacy %mklibname kopeteprivacy 1

%package -n %libkopeteprivacy
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopeteprivacy
KDE 4 library

%post -n %libkopeteprivacy -p /sbin/ldconfig
%postun -n %libkopeteprivacy -p /sbin/ldconfig

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

%post -n %libkopetechatwindow_shared -p /sbin/ldconfig
%postun -n %libkopetechatwindow_shared -p /sbin/ldconfig

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

%post -n %libiris_kopete -p /sbin/ldconfig
%postun -n %libiris_kopete -p /sbin/ldconfig

%files -n %libiris_kopete
%defattr(-,root,root)
%_kde_libdir/libiris_kopete.so.*

#---------------------------------------------

%define libkopete_oscar %mklibname kopete_oscar 4

%package -n %libkopete_oscar
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopete_oscar
KDE 4 library

%post -n %libkopete_oscar -p /sbin/ldconfig
%postun -n %libkopete_oscar -p /sbin/ldconfig

%files -n %libkopete_oscar
%defattr(-,root,root)
%_kde_libdir/libkopete_oscar.so.*

#---------------------------------------------

%define libkopete_msn_shared %mklibname kopete_msn_shared 4

%package -n %libkopete_msn_shared
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkopete_msn_shared
KDE 4 library

%post -n %libkopete_msn_shared -p /sbin/ldconfig
%postun -n %libkopete_msn_shared -p /sbin/ldconfig

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

%post -n %liboscar -p /sbin/ldconfig
%postun -n %liboscar -p /sbin/ldconfig

%files -n %liboscar
%defattr(-,root,root)
%_kde_libdir/liboscar.so.*

#---------------------------------------------

%package -n kde4-kppp
Summary: %{name} kppp
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kppp

%description -n kde4-kppp
%{name} kppp.

%files -n kde4-kppp
%defattr(-,root,root)
%_kde_appsdir/kppp
%_kde_bindir/kppp
%_kde_bindir/kppplogview
%_kde_datadir/applications/kde4/Kppp.desktop
%_kde_datadir/applications/kde4/kppplogview.desktop
%_datadir/dbus-1/interfaces/org.kde.kppp.xml
%_kde_docdir/HTML/*/kppp
%exclude %_sysconfdir/pam.d/kppp

#---------------------------------------------

%package -n kde4-krdc
Summary: %{name} krdc
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-krdc

%description -n kde4-krdc
%{name} krdc.

%files -n kde4-krdc
%defattr(-,root,root)
%_kde_appsdir/krdc
%_kde_appsdir/zeroconf
%_kde_bindir/krdc
%_kde_datadir/applications/kde4/krdc.desktop
%_kde_datadir/config.kcfg/krdc.kcfg
%_kde_datadir/kde4/services/rdp.protocol
%_kde_datadir/kde4/services/vnc.protocol
%_kde_docdir/HTML/*/krdc

#---------------------------------------------

%package -n kde4-krfb
Summary: %{name} krfb
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-krfb

%description -n kde4-krfb
%{name} krfb.

%files -n kde4-krfb
%defattr(-,root,root)
%_kde_appsdir/krfb
%_kde_bindir/krfb
%_kde_datadir/applications/kde4/krfb.desktop
%_kde_docdir/HTML/*/krfb

#---------------------------------------------

%package -n kde4-lanbrowsing
Summary: %{name} lanbrowsing
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-lanbrowsing
Obsoletes: %name-lisa

%description -n kde4-lanbrowsing
%{name} lanbrowsing.

%files -n kde4-lanbrowsing
%defattr(-,root,root)
%attr(4755,root,root) %_kde_prefix/sbin/lisad
%_kde_appsdir/lisa
%_kde_appsdir/remoteview
%_kde_appsdir/konqsidebartng
%_kde_appsdir/konqueror
%_kde_libdir/kde4/kcm_lanbrowser.so
%_kde_libdir/kde4/kio_lan.so
%_kde_datadir/kde4/services/kcmkiolan.desktop
%_kde_datadir/kde4/services/kcmlisa.desktop
%_kde_datadir/kde4/services/lan.protocol
%_kde_docdir/HTML/*/lanbrowser
%_kde_docdir/HTML/*/lisa

#---------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel
Requires: %libkgetcore = %version
Requires: %libgadu_kopete = %version
Requires: %libkyahoo = %version
Requires: %libkopete_videodevice = %version
Requires: %libkopeteaddaccountwizard = %version
Requires: %libkopete = %version
Requires: %libpapillon_kopete = %version
Requires: %libkopeteprivacy = %version
Requires: %libkopetechatwindow_shared = %version
Requires: %libiris_kopete = %version
Requires: %libkopete_oscar = %version
Requires: %libkopete_msn_shared = %version
Requires: %liboscar = %version
%description  devel
This package contains header files needed if you wish to build applications based on %{name}.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%_kde_prefix/include/*

#-------------------------------------------

%prep
%setup -q -n kdenetwork-%version

%build
%cmake_kde4 

%make


%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

install -d -m 0755 %buildroot%_sysconfdir/rc.d/init.d

#TODO install it into real sysconfig dir
install -d -m 0755 %buildroot/%_sysconfdir/pam.d/
install -m 0644 %SOURCE1 %buildroot/%_sysconfdir/pam.d/kppp

%clean
rm -fr %buildroot


