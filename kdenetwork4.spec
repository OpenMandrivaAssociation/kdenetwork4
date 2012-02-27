Name:		kdenetwork4
Version:	4.8.0
Release:	2
Epoch:		3
Group:		Graphical desktop/KDE
Summary:	K Desktop Environment - Network Applications
License:	GPL
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%version/src/kdenetwork-%version.tar.bz2
Patch0:		kdenetwork-4.6.5-krdcxdg.patch
Patch1:		kdenetwork-4.6.5-krfbxdg.patch
BuildRequires:	qt4-devel >= 4:4.8.0-0.rc1.1
BuildRequires:	kdelibs4-devel >= 2:4.2.98
BuildRequires:	kdepimlibs4-devel
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	kdebase4-devel
BuildRequires:	libvncserver-devel >= 0.8.2-3
BuildRequires:	jpeg-devel
BuildRequires:	soprano-devel
BuildRequires:	shared-desktop-ontologies-devel
BuildRequires:	sqlite3-devel
BuildRequires:	strigi-devel
BuildRequires:	qca2-devel
BuildRequires:	pkgconfig(ortp)
BuildRequires:	speex-devel
BuildRequires:	idn-devel
BuildRequires:	libalsa-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	libotr-devel
BuildRequires:	libmsn-devel
BuildRequires:	linphone-devel
BuildRequires:	meanwhile-devel
BuildRequires:	gadu-devel
BuildRequires:	v4l-utils-devel
BuildRequires:	expat-devel
BuildRequires:	openssl-devel
BuildRequires:	boost-devel
BuildRequires:	qimageblitz-devel
BuildRequires:	libktorrent-devel >= 1.1
Suggests:	kdnssd
Suggests:	kget
Suggests:	kopete
Suggests:	kppp
Suggests:	krdc
Suggests:	krfb
Suggests:	kde4-filesharing
Obsoletes:	kdenetwork4-core < 3:4.5.72
Obsoletes:	kde4-lanbrowsing
Obsoletes:	kdenetwork-kxmlrpcd
Obsoletes:	kdenetwork_kroupware
Obsoletes:	kdenetwork_kroupware-kppp
Obsoletes:	libkdenetwork_kroupware2
Obsoletes:	libkdenetwork_kroupware2-devel
Obsoletes:	kit
Obsoletes:	kdenetwork-kmail < 3.1.6
Obsoletes:	kdenetwork-knode < 3.1.6
Obsoletes:	kdenetwork-korn < 3.1.6
Obsoletes:	lisa < 2:3.5.10-7

%description
Networking applications for the K Desktop Environment.

- kdict: graphical client for the DICT protocol.
- kit: AOL instant messenger client, using the TOC protocol
- kpf: public fileserver applet
- krfb: Desktop Sharing server, allow others to access your desktop via VNC
- krdc: a client for Desktop Sharing and other VNC servers

%files
%doc README

#----------------------------------------------------------------------

%package -n kde4-filesharing
Summary:	%{name} filesharing
Group:		Graphical desktop/KDE
Conflicts:	%{name}-core < 3:4.5.72
Obsoletes:	%{name}-filesharing < 2:3.93.0-0.714148.1

%description -n kde4-filesharing
%{name} filesharing.

%files -n kde4-filesharing
%{_kde_libdir}/kde4/sambausershareplugin.so
%{_kde_datadir}/kde4/services/sambausershareplugin.desktop

#---------------------------------------------

%package -n kdnssd
Summary:	%{name} kdnssd
Group:		Graphical desktop/KDE
Requires:	nss_mdns
Obsoletes:	%{name}-kdnssd < 2:3.93.0-0.714148.1
Obsoletes:	kde4-lanbrowsing
Obsoletes:	kde4-kdnssd < 3:4.0.68
Provides:	kde4-kdnssd = %{EVRD}

%description -n kdnssd
%{name} kdnssd.

%files -n kdnssd
%dir %{_kde_appsdir}/remoteview
%{_kde_appsdir}/remoteview/zeroconf.desktop
%{_kde_libdir}/kde4/kded_dnssdwatcher.so
%{_kde_libdir}/kde4/kio_zeroconf.so
%{_kde_datadir}/kde4/services/kded/dnssdwatcher.desktop
%{_kde_datadir}/kde4/services/zeroconf.protocol

#---------------------------------------------

%define libkgetcore %mklibname kgetcore 4

%package -n %{libkgetcore}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkgetcore}
KDE 4 library

%files -n %{libkgetcore}
%{_kde_libdir}/libkgetcore.so.*

#---------------------------------------------

%package -n kget
Summary:	%{name} kget
Group:		Graphical desktop/KDE
Conflicts:	%{name}-core < 3:4.5.72
Obsoletes:	%{name}-kget < 2:3.93.0-0.714148.1
Obsoletes:	kde4-kget < 3:4.0.68
Provides:	kde4-kget = %{EVRD}


%description -n kget
An advanced download manager for KDE.

%files -n kget
%{_kde_appsdir}/kconf_update/kget*
%{_kde_bindir}/kget
%dir %{_kde_appsdir}/kget
%{_kde_appsdir}/kget/*
%{_kde_libdir}/kde4/krunner_kget.so
%{_kde_libdir}/kde4/kget_*
%{_kde_libdir}/kde4/plasma_engine_kget.so
%{_kde_libdir}/kde4/kcm_kget_checksumsearchfactory.so
%{_kde_libdir}/kde4/kcm_kget_metalinkfactory.so
%{_kde_libdir}/kde4/kcm_kget_bittorrentfactory.so
%{_kde_datadir}/kde4/services/plasma-engine-kget.desktop
%{_kde_datadir}/applications/kde4/kget.desktop
%{_kde_datadir}/kde4/services/ServiceMenus/kget_download.desktop
%{_kde_datadir}/config.kcfg/kget*
%{_kde_datadir}/kde4/services/kget_*
%{_kde_datadir}/kde4/servicetypes/kget_*
%{_kde_appsdir}/dolphinpart/kpartplugins/kget_plug_in.rc
%{_kde_appsdir}/dolphinpart/kpartplugins/kget_plug_in.desktop
%{_kde_appsdir}/khtml/kpartplugins/kget_plug_in.rc
%{_kde_appsdir}/khtml/kpartplugins/kget_plug_in.desktop
%{_kde_appsdir}/kwebkitpart/kpartplugins/kget_plug_in.desktop
%{_kde_appsdir}/kwebkitpart/kpartplugins/kget_plug_in.rc
#%_kde_libdir/kde4/kcm_kget_contentfetchfactory.so
%{_kde_libdir}/kde4/kcm_kget_mirrorsearchfactory.so
%{_kde_libdir}/kde4/kcm_kget_multisegkiofactory.so
%{_kde_libdir}/kde4/plasma_kget_barapplet.so
%{_kde_libdir}/kde4/plasma_kget_piechart.so
%{_kde_datadir}/kde4/services/kgetbarapplet-default.desktop
%{_kde_datadir}/kde4/services/kgetpiechartapplet-default.desktop
%{_kde_datadir}/kde4/services/plasma-runner-kget.desktop
%{_kde_datadir}/dbus-1/services/org.kde.kget.service
%{_kde_iconsdir}/*/*/apps/kget.*
%{_kde_docdir}/HTML/*/kget

#---------------------------------------------

%package -n kopete
Summary:	%{name} kopete
Group:		Graphical desktop/KDE
Conflicts:	%{name}-core < 3:4.5.72
Requires:	akonadi >= 1:1.1.95
Requires:	qca2-plugin-openssl-%{_lib}
Requires:	kdepimlibs4-core
Requires:	jasper
Obsoletes:	%{name}-kopete < 2:3.93.0-0.714148.1
Obsoletes:	kde4-kopete < 3:4.0.68
Conflicts:	%{name}-devel < 3:3.96.1-0.740247.1
Provides:	kde4-kopete = %{EVRD}

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
%{_kde_appsdir}/kconf_update/kopete-*
%{_kde_bindir}/kopete
%{_kde_bindir}/kopete_latexconvert.sh
%{_kde_bindir}/winpopup-install
%{_kde_bindir}/winpopup-send
%{_kde_libdir}/kde4/kcm_kopete_*
%{_kde_libdir}/kde4/kopete_*
%{_kde_libdir}/libqgroupwise.so
%{_kde_libdir}/kde4/libchattexteditpart.so
%{_kde_datadir}/applications/kde4/kopete.desktop
%{_kde_datadir}/config/kopeterc
%{_kde_datadir}/config.kcfg/historyconfig.kcfg
%{_kde_datadir}/config.kcfg/kopeteappearancesettings.kcfg
%{_kde_datadir}/config.kcfg/kopetebehaviorsettings.kcfg
%{_kde_datadir}/config.kcfg/latexconfig.kcfg
%{_kde_datadir}/config.kcfg/nowlisteningconfig.kcfg
%{_kde_datadir}/config.kcfg/webpresenceconfig.kcfg
%{_kde_datadir}/config.kcfg/translatorconfig.kcfg
%{_kde_datadir}/kde4/services/aim.protocol
%{_kde_datadir}/kde4/services/chatwindow.desktop
%{_kde_datadir}/kde4/services/emailwindow.desktop
%{_kde_datadir}/kde4/services/kconfiguredialog/kopete_*
%{_kde_datadir}/kde4/services/kopete_*
%{_kde_datadir}/kde4/services/xmpp.protocol
%{_kde_datadir}/kde4/services/callto.protocol
%{_kde_datadir}/kde4/services/skype.protocol
%{_kde_datadir}/kde4/services/tel.protocol
%{_kde_datadir}/kde4/servicetypes/kopete*
%{_kde_datadir}/sounds/Kopete_Event.ogg
%{_kde_datadir}/sounds/Kopete_Received.ogg
%{_kde_datadir}/sounds/Kopete_Sent.ogg
%{_kde_datadir}/sounds/Kopete_User_is_Online.ogg
%{_kde_datadir}/sounds/KDE-Im-Phone-Ring.wav
%{_kde_appsdir}/kopete
%{_kde_appsdir}/kopete_contactnotes
%{_kde_appsdir}/kopete_history
%{_kde_appsdir}/kopete_jabber
%{_kde_appsdir}/kopete_latex
%{_kde_appsdir}/kopete_wlm
%{_kde_appsdir}/kopete_privacy
%{_kde_appsdir}/kopete_statistics
%{_kde_appsdir}/kopete_translator
%{_kde_appsdir}/kopete_yahoo
%{_kde_appsdir}/kopete_groupwise
%{_kde_appsdir}/kopete_skype
%{_kde_appsdir}/kopeterichtexteditpart
%{_kde_iconsdir}/*/*/actions/account_offline_overlay.*
%{_kde_iconsdir}/*/*/actions/contact_away_overlay.*
%{_kde_iconsdir}/*/*/actions/contact_busy_overlay.*
%{_kde_iconsdir}/*/*/actions/contact_food_overlay.*
%{_kde_iconsdir}/*/*/actions/contact_invisible_overlay.*
%{_kde_iconsdir}/*/*/actions/contact_phone_overlay.*
%{_kde_iconsdir}/*/*/actions/contact_xa_overlay.*
%{_kde_iconsdir}/*/*/actions/emoticon.*
%{_kde_iconsdir}/*/*/actions/im-status-message-edit.*
%{_kde_iconsdir}/*/*/actions/mail-encrypt.*
%{_kde_iconsdir}/*/*/actions/metacontact_unknown.*
%{_kde_iconsdir}/*/*/actions/newmessage.*
%{_kde_iconsdir}/*/*/actions/status_unknown_overlay.*
%{_kde_iconsdir}/*/*/actions/status_unknown.*
%{_kde_iconsdir}/*/*/actions/view-user-offline-kopete.*
%{_kde_iconsdir}/*/*/actions/voicecall.*
%{_kde_iconsdir}/*/*/actions/webcamreceive.*
%{_kde_iconsdir}/*/*/actions/webcamsend.*
%{_kde_iconsdir}/*/*/apps/kopete-offline.*
%{_kde_iconsdir}/*/*/apps/kopete.*
%{_kde_iconsdir}/*/*/status/object-locked-finished.*
%{_kde_iconsdir}/*/*/status/object-locked-unverified.*
%{_kde_iconsdir}/*/*/status/object-locked-verified.*
%{_kde_datadir}/config.kcfg/urlpicpreview.kcfg
%{_kde_docdir}/HTML/*/kopete
%{_kde_libdir}/mozilla/plugins/skypebuttons.so
%dir %{_kde_libdir}/kde4/plugins/accessible
%{_kde_libdir}/kde4/plugins/accessible/chatwindowaccessiblewidgetfactory.so
%exclude %{_kde_appsdir}/kopete_latex
%exclude %{_kde_libdir}/kde4/kcm_kopete_latex.*
%exclude %{_kde_libdir}/kde4/kopete_latex.*
%exclude %{_kde_datadir}/kde4/services/kopete_latex.desktop
%exclude %{_kde_datadir}/config.kcfg/latexconfig.kcfg
%exclude %{_kde_bindir}/kopete_latexconvert.sh
%exclude %{_kde_datadir}/kde4/services/kconfiguredialog/kopete_latex_config.desktop
%exclude %{_kde_appsdir}/kopete/icons/oxygen/32x32/apps/latex.png
#---------------------------------------------

%package  kopete-latex
Group:		Graphical desktop/KDE
Summary:	Kopete latex plugin for write andd read mesages in latex
Requires:	kopete
Requires:	imagemagick

%description kopete-latex
Kopete latex plugin for write andd read mesages in latexinder

%files kopete-latex
%{_kde_appsdir}/kopete_latex
%{_kde_libdir}/kde4/kcm_kopete_latex.*
%{_kde_libdir}/kde4/kopete_latex.*
%{_kde_datadir}/kde4/services/kopete_latex.desktop
%{_kde_datadir}/config.kcfg/latexconfig.kcfg
%{_kde_bindir}/kopete_latexconvert.sh
%{_kde_datadir}/kde4/services/kconfiguredialog/kopete_latex_config.desktop
%{_kde_appsdir}/kopete/icons/oxygen/32x32/apps/latex.png

#---------------------------------------------

%define libkopetecontactlist %mklibname kopetecontactlist 1

%package -n %{libkopetecontactlist}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkopetecontactlist}
KDE 4 library

%files -n %{libkopetecontactlist}
%{_kde_libdir}/libkopetecontactlist.so.*

#---------------------------------------------

%define libkyahoo %mklibname kyahoo 1

%package -n %{libkyahoo}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkyahoo}
KDE 4 library

%files -n %{libkyahoo}
%{_kde_libdir}/libkyahoo.so.*

#---------------------------------------------

%define libkopete_videodevice %mklibname kopete_videodevice 4

%package -n %{libkopete_videodevice}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkopete_videodevice}
KDE 4 library

%files -n %{libkopete_videodevice}
%{_kde_libdir}/libkopete_videodevice.so.*

#---------------------------------------------

%define libkopeteaddaccountwizard %mklibname kopeteaddaccountwizard 1

%package -n %{libkopeteaddaccountwizard}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkopeteaddaccountwizard}
KDE 4 library

%files -n %{libkopeteaddaccountwizard}
%{_kde_libdir}/libkopeteaddaccountwizard.so.*

#---------------------------------------------

%define libkopete %mklibname kopete 4

%package -n %{libkopete}
Summary:	KDE 4 library
Group:		System/Libraries
Obsoletes:	%{_lib}kopete5 < 2:3.91-0.689748.1

%description -n %{libkopete}
KDE 4 library

%files -n %{libkopete}
%{_kde_libdir}/libkopete.so.*
%{_kde_datadir}/config.kcfg/kopetestatussettings.kcfg

#---------------------------------------------

%define libkopeteprivacy %mklibname kopeteprivacy 1

%package -n %{libkopeteprivacy}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkopeteprivacy}
KDE 4 library

%files -n %{libkopeteprivacy}
%{_kde_libdir}/libkopeteprivacy.so.*

#---------------------------------------------

%define libkopetechatwindow_shared %mklibname kopetechatwindow_shared 1

%package -n %{libkopetechatwindow_shared}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkopetechatwindow_shared}
KDE 4 library

%files -n %{libkopetechatwindow_shared}
%{_kde_libdir}/libkopetechatwindow_shared.so.*

#---------------------------------------------

%define libkrdccore %mklibname krdccore 1

%package -n %{libkrdccore}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkrdccore}
KDE 4 library

%files -n %{libkrdccore}
%{_kde_libdir}/libkrdccore.so.*

#---------------------------------------------

%define libkopete_otr_shared %mklibname kopete_otr_shared 1

%package -n %{libkopete_otr_shared}
Summary:	KDE 4 library
Group:		System/Libraries
Conflicts:	kopete-otr < 0.8

%description -n %{libkopete_otr_shared}
KDE 4 library

%files -n %{libkopete_otr_shared}
%{_kde_libdir}/libkopete_otr_shared.so.*
%dir %{_kde_appsdir}/kopete_otr
%{_kde_appsdir}/kopete_otr/*
%{_kde_datadir}/config.kcfg/kopete_otr.kcfg

#---------------------------------------------

%define libkopetestatusmenu %mklibname kopetestatusmenu 1

%package -n %{libkopetestatusmenu}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkopetestatusmenu}
KDE 4 library

%files -n %{libkopetestatusmenu}
%{_kde_libdir}/libkopetestatusmenu.so.*

#---------------------------------------------

%define libkopete_oscar %mklibname kopete_oscar 4

%package -n %{libkopete_oscar}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkopete_oscar}
KDE 4 library

%files -n %{libkopete_oscar}
%{_kde_libdir}/libkopete_oscar.so.*

#---------------------------------------------

%define liboscar %mklibname oscar 1

%package -n %{liboscar}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{liboscar}
KDE 4 library

%files -n %{liboscar}
%{_kde_libdir}/liboscar.so.*

#---------------------------------------------

%define libkopeteidentity %mklibname kopeteidentity 1

%package -n %{libkopeteidentity}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkopeteidentity}
KDE 4 library

%files -n %{libkopeteidentity}
%{_kde_libdir}/libkopeteidentity.so.*


#---------------------------------------------

%define libkrfbprivate %mklibname krfbprivate 4

%package -n %{libkrfbprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkrfbprivate}
KDE 4 library

%files -n %{libkrfbprivate}
%{_kde_libdir}/libkrfbprivate.so.*

#---------------------------------------------

%package -n kppp
Summary:	%{name} kppp
Group:		Graphical desktop/KDE
Conflicts:	%{name}-core < 3:4.5.72
Requires:	ppp
Requires:	kppp-provider
Obsoletes:	%{name}-kppp < 2:3.93.0-0.714148.1
Obsoletes:	kde4-kppp < 3:4.0.68
Provides:	kde4-kppp = %{EVRD}

%description -n kppp
%{name} kppp.

%files -n kppp
%{_kde_appsdir}/kppp
%{_kde_bindir}/kppp
%{_kde_bindir}/kppplogview
%{_kde_datadir}/applications/kde4/Kppp.desktop
%{_kde_datadir}/applications/kde4/kppplogview.desktop
%{_kde_docdir}/HTML/*/kppp
%{_kde_iconsdir}/*/*/apps/kppp.*
%exclude %{_kde_appsdir}/kppp/Rules
%exclude %{_kde_appsdir}/kppp/Provider

#-----------------------------------------------------------

%package -n kppp-provider
Group:		Graphical desktop/KDE
Summary:	List of providers for pppd

%description -n kppp-provider
List of providers for kppp

%files -n kppp-provider
%{_kde_appsdir}/kppp/Rules
%{_kde_appsdir}/kppp/Provider

#---------------------------------------------

%package -n krdc
Summary:	%{name} krdc
Group:		Graphical desktop/KDE
Obsoletes:	%{name}-krdc < 2:3.93.0-0.714148.1
Obsoletes:	kde4-krdc < 3:4.0.68
Provides:	kde4-krdc = %{EVRD}

%description -n krdc
KDE Desktop Sharing allows you to invite somebody at a remote
location to watch and possibly control your desktop.

%files -n krdc
%{_kde_bindir}/krdc
%{_kde_appsdir}/krdc
%{_kde_datadir}/applications/kde4/krdc.desktop
%{_kde_datadir}/config.kcfg/krdc.kcfg
%{_kde_datadir}/kde4/services/rdp.protocol
%{_kde_datadir}/kde4/services/vnc.protocol
%{_kde_libdir}/kde4/kcm_krdc_rdpplugin.so
%{_kde_libdir}/kde4/kcm_krdc_vncplugin.so
%{_kde_libdir}/kde4/krdc_rdpplugin.so
%{_kde_libdir}/kde4/krdc_testplugin.so
%{_kde_libdir}/kde4/krdc_vncplugin.so
%{_kde_datadir}/kde4/services/krdc_rdp.desktop
%{_kde_datadir}/kde4/services/krdc_rdp_config.desktop
%{_kde_datadir}/kde4/services/krdc_test.desktop
%{_kde_datadir}/kde4/services/krdc_vnc.desktop
%{_kde_datadir}/kde4/services/krdc_vnc_config.desktop
%{_kde_datadir}/kde4/servicetypes/krdc_plugin.desktop
%{_kde_datadir}/kde4/services/ServiceMenus/smb2rdc.desktop
%{_kde_docdir}/HTML/*/krdc

#---------------------------------------------

%package -n krfb
Summary:	%{name} krfb
Group:		Graphical desktop/KDE
Obsoletes:	%{name}-krfb < 2:3.93.0-0.714148.1
Obsoletes:	kde4-krfb < 3:4.0.68
Provides:	kde4-krfb = %{EVRD}

%description -n krfb
KDE Desktop Sharing allows you to invite somebody at a remote
location to watch and possibly control your desktop.

%files -n krfb
%{_kde_bindir}/krfb
%{_kde_appsdir}/krfb
%{_kde_datadir}/applications/kde4/krfb.desktop
%{_kde_libdir}/kde4/krfb_*.so
%{_kde_datadir}/kde4/service*/krfb*.desktop
%{_kde_docdir}/HTML/*/krfb

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Conflicts:	kdepim <= 3.1.92
Requires:	kdelibs4-devel >= 2:4.2.98
Requires:	kdepimlibs4-devel >= 2:4.2.98
Requires:	%{libkgetcore} = %{EVRD}
Requires:	%{libkopetecontactlist} = %{EVRD}
Requires:	%{libkyahoo} = %{EVRD}
Requires:	%{libkopete_videodevice} = %{EVRD}
Requires:	%{libkopeteaddaccountwizard} = %{EVRD}
Requires:	%{libkopete} = %{EVRD}
Requires:	%{libkopeteprivacy} = %{EVRD}
Requires:	%{libkopetechatwindow_shared} = %{EVRD}
Requires:	%{libkrdccore} = %{EVRD}
Requires:	%{libkopete_oscar} = %{EVRD}
Requires:	%{liboscar} = %{EVRD}
Requires:	%{libkrfbprivate} = %{EVRD}
Requires:	%{libkopete_otr_shared} = %{EVRD}
Requires:	%{libkopeteidentity} = %{EVRD}
Requires:	%{libkopetestatusmenu} = %{EVRD}

%description  devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde_libdir}/*.so
%exclude %{_kde_libdir}/libqgroupwise.so
%{_kde_includedir}/*
%{_kde_datadir}/dbus-1/interfaces/*

#-------------------------------------------

%prep
%setup -q -n kdenetwork-%{version}
%patch0 -p1 -b .krdcxdg
%patch1 -p1 -b .krfbxdg

%build
%cmake_kde4 -DWITH_GOOGLETALK=OFF
%make

%install
%makeinstall_std -C build

