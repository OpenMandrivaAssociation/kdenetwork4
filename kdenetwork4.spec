%define revision  681220
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

%define lib_name_orig lib%{name}
%define lib_major 2
%define lib_name %mklibname kdenetwork4 %lib_major



Name: 		kdenetwork4
Version: 	3.91
Release: 	%mkrel 0.%revision.1
Epoch: 		2
Group: 		Development/KDE and Qt
Summary: 	K Desktop Environment - Network Applications
License: 	GPL
URL: 		http://www.kde.org
%if %branch
Source: 	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdenetwork-%version-%revision.tar.bz2
%else
Source: 	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdenetwork-%version.tar.bz2
%endif
Source1:        kdenetwork3-kppp.pamd
Source2:        kdenetwork-lisa
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:  freetype2-devel
BuildRequires:  gettext
%define mini_release %mkrel 0.%revision.1
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
%define release_min_mkrel %mkrel 3
BuildRequires:	libvncserver-devel >= 0.8.2-%{release_min_mkrel} 
#For kopete.
%define release_min_mkrel_qca2 %mkrel 8
BuildRequires: qca2-devel >= 2.0-0.beta2.${release_min_mkrel_qca2}
Requires: kde4-kget = %epoch:%version-%release
Requires: kde4-ktalk = %epoch:%version-%release
Requires: kde4-krfb = %epoch:%version-%release
Requires: kde4-kopete = %epoch:%version-%release
Requires: kde4-knewsticker = %epoch:%version-%release

%description
Networking applications for the K Desktop Environment.

- kdict: graphical client for the DICT protocol.
- kit: AOL instant messenger client, using the TOC protocol
- knewsticker: RDF newsticker applet
- kpf: public fileserver applet
- ktalkd: talk daemon
- lanbrowsing: lan browsing kio slave
- krfb: Desktop Sharing server, allow others to access your desktop via VNC
- krdc: a client for Desktop Sharing and other VNC servers

%files

#-----------------------------------------------------------

%package core
Summary:	Common files for kdenetwork
Group:		Graphical desktop/KDE

Obsoletes:      %name-common

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
%_kde_iconsdir/hicolor/16x16/apps/kcmsambaconf.png
%_kde_datadir/kde4/services/fileshare_propsdlgplugin.desktop

#-----------------------------------------------------------

%package kopete
Group: Graphical desktop/KDE
Summary: Kopete
Requires: %name-core >= %epoch:%version-%release
Provides: kopete4
BuildConflicts: xmms-devel
#Need for yahoo webcam
Requires:	jasper

%description kopete
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

%post kopete -p /sbin/ldconfig

%postun kopete -p /sbin/ldconfig

%files kopete
%defattr(-,root,root,-)
%_kde_bindir/kopete
%_kde_bindir/winpopup-install.sh
%_kde_bindir/winpopup-send.sh

%_kde_libdir/kde4/kcm_kopete_*
%_kde_libdir/kde4/kopete_*

%_kde_datadir/dbus-1/interfaces/org.kde.kopete.Client.xml

%_kde_appsdir/kconf_update/kopete-account-0.10.pl
%_kde_appsdir/kconf_update/kopete-account-kconf_update.sh
%_kde_appsdir/kconf_update/kopete-account-kconf_update.upd
%_kde_appsdir/kconf_update/kopete-nameTracking.upd
%_kde_appsdir/kconf_update/kopete-pluginloader.pl
%_kde_appsdir/kconf_update/kopete-pluginloader.upd
%_kde_appsdir/kconf_update/kopete-pluginloader2.sh
%_kde_appsdir/kconf_update/kopete-pluginloader2.upd
%_kde_datadir/applications/kde4/kopete.desktop
%_kde_appsdir/kconf_update/kopete-jabberpriorityaddition-kconf_update.sh
%_kde_appsdir/kconf_update/kopete-jabberpriorityaddition-kconf_update.upd
%_kde_appsdir/kconf_update/kopete-jabberproxytype-kconf_update.sh
%_kde_appsdir/kconf_update/kopete-jabberproxytype-kconf_update.upd

%_kde_datadir/kde4/services/kopete_*.desktop
%_kde_datadir/kde4/servicetypes/kopete*.desktop
%_kde_datadir/sounds/Kopete_*.ogg
%_kde_datadir/kde4/services/aim.protocol
%_kde_datadir/kde4/services/chatwindow.desktop
%_kde_datadir/kde4/services/emailwindow.desktop
%_kde_datadir/kde4/services/kconfiguredialog/kopete_*.desktop

%_kde_iconsdir/hicolor/22x22/apps/kopete.png
%_kde_iconsdir/hicolor/32x32/apps/kopete.png
%_kde_iconsdir/hicolor/48x48/apps/kopete.png
%_kde_iconsdir/hicolor/64x64/apps/kopete.png
%_kde_iconsdir/hicolor/scalable/apps/kopete2.svgz
%_kde_iconsdir/hicolor/128x128/apps/kopete.png
%_kde_iconsdir/hicolor/16x16/apps/kopete.png

%_kde_iconsdir/oxygen/128x128/actions/voicecall.png
%_kde_iconsdir/oxygen/128x128/actions/webcamreceive.png
%_kde_iconsdir/oxygen/128x128/actions/webcamsend.png
%_kde_iconsdir/oxygen/128x128/actions/kopeteavailable.png
%_kde_iconsdir/oxygen/16x16/actions/account_offline_overlay.png
%_kde_iconsdir/oxygen/16x16/actions/add_user.png
%_kde_iconsdir/oxygen/16x16/actions/contact_away_overlay.png
%_kde_iconsdir/oxygen/16x16/actions/contact_busy_overlay.png
%_kde_iconsdir/oxygen/16x16/actions/contact_food_overlay.png
%_kde_iconsdir/oxygen/16x16/actions/contact_invisible_overlay.png
%_kde_iconsdir/oxygen/16x16/actions/contact_phone_overlay.png
%_kde_iconsdir/oxygen/16x16/actions/contact_xa_overlay.png
%_kde_iconsdir/oxygen/16x16/actions/delete_user.png
%_kde_iconsdir/oxygen/16x16/actions/edit_user.png
%_kde_iconsdir/oxygen/16x16/actions/emoticon.png
%_kde_iconsdir/oxygen/16x16/actions/kopeteavailable.png
%_kde_iconsdir/oxygen/16x16/actions/kopeteaway.png
%_kde_iconsdir/oxygen/16x16/actions/kopeteeditstatusmessage.png
%_kde_iconsdir/oxygen/16x16/actions/kopetestatusmessage.png
%_kde_iconsdir/oxygen/16x16/actions/metacontact_away.png
%_kde_iconsdir/oxygen/16x16/actions/metacontact_offline.png
%_kde_iconsdir/oxygen/16x16/actions/metacontact_online.png
%_kde_iconsdir/oxygen/16x16/actions/metacontact_unknown.png
%_kde_iconsdir/oxygen/16x16/actions/newmsg.png
%_kde_iconsdir/oxygen/16x16/actions/search_user.png
%_kde_iconsdir/oxygen/16x16/actions/show_offliners.png
%_kde_iconsdir/oxygen/16x16/actions/status_unknown.png
%_kde_iconsdir/oxygen/16x16/actions/status_unknown_overlay.png
%_kde_iconsdir/oxygen/16x16/actions/voicecall.png
%_kde_iconsdir/oxygen/16x16/actions/webcamreceive.png
%_kde_iconsdir/oxygen/16x16/actions/webcamsend.png
%_kde_iconsdir/oxygen/16x16/mimetypes/kopete_emoticons.png
%_kde_iconsdir/oxygen/22x22/actions/account_offline_overlay.png
%_kde_iconsdir/oxygen/22x22/actions/add_user.png
%_kde_iconsdir/oxygen/22x22/actions/delete_user.png
%_kde_iconsdir/oxygen/22x22/actions/edit_user.png
%_kde_iconsdir/oxygen/22x22/actions/kopeteavailable.png
%_kde_iconsdir/oxygen/22x22/actions/kopeteaway.png
%_kde_iconsdir/oxygen/22x22/actions/kopeteeditstatusmessage.png
%_kde_iconsdir/oxygen/22x22/actions/search_user.png
%_kde_iconsdir/oxygen/22x22/actions/show_offliners.png
%_kde_iconsdir/oxygen/22x22/actions/voicecall.png
%_kde_iconsdir/oxygen/22x22/actions/webcamreceive.png
%_kde_iconsdir/oxygen/22x22/actions/webcamsend.png
%_kde_iconsdir/oxygen/22x22/apps/kopete_all_away.png
%_kde_iconsdir/oxygen/22x22/apps/kopete_offline.png
%_kde_iconsdir/oxygen/22x22/apps/kopete_some_away.png
%_kde_iconsdir/oxygen/22x22/apps/kopete_some_online.png
%_kde_iconsdir/oxygen/22x22/mimetypes/kopete_emoticons.png
%_kde_iconsdir/oxygen/32x32/actions/account_offline_overlay.png
%_kde_iconsdir/oxygen/32x32/actions/add_user.png
%_kde_iconsdir/oxygen/32x32/actions/delete_user.png
%_kde_iconsdir/oxygen/32x32/actions/edit_user.png
%_kde_iconsdir/oxygen/32x32/actions/kopeteavailable.png
%_kde_iconsdir/oxygen/32x32/actions/kopeteaway.png
%_kde_iconsdir/oxygen/32x32/actions/kopeteeditstatusmessage.png
%_kde_iconsdir/oxygen/32x32/actions/metacontact_away.png
%_kde_iconsdir/oxygen/32x32/actions/metacontact_offline.png
%_kde_iconsdir/oxygen/32x32/actions/metacontact_online.png
%_kde_iconsdir/oxygen/32x32/actions/metacontact_unknown.png
%_kde_iconsdir/oxygen/32x32/actions/newmessage.mng
%_kde_iconsdir/oxygen/32x32/actions/newmsg.png
%_kde_iconsdir/oxygen/32x32/actions/search_user.png
%_kde_iconsdir/oxygen/32x32/actions/show_offliners.png
%_kde_iconsdir/oxygen/32x32/actions/voicecall.png
%_kde_iconsdir/oxygen/32x32/actions/webcamreceive.png
%_kde_iconsdir/oxygen/32x32/actions/webcamsend.png
%_kde_iconsdir/oxygen/48x48/actions/kopeteavailable.png
%_kde_iconsdir/oxygen/48x48/actions/kopeteaway.png
%_kde_iconsdir/oxygen/48x48/actions/metacontact_away.png
%_kde_iconsdir/oxygen/48x48/actions/metacontact_offline.png
%_kde_iconsdir/oxygen/48x48/actions/metacontact_online.png
%_kde_iconsdir/oxygen/48x48/actions/voicecall.png
%_kde_iconsdir/oxygen/48x48/actions/webcamreceive.png
%_kde_iconsdir/oxygen/48x48/actions/webcamsend.png
%_kde_iconsdir/oxygen/48x48/actions/kopeteeditstatusmessage.png
%_kde_iconsdir/oxygen/64x64/actions/voicecall.png
%_kde_iconsdir/oxygen/64x64/actions/webcamreceive.png
%_kde_iconsdir/oxygen/64x64/actions/webcamsend.png
%_kde_iconsdir/oxygen/64x64/actions/kopeteavailable.png

%_kde_iconsdir/oxygen/scalable/actions/account_offline_overlay.svgz
%_kde_iconsdir/oxygen/scalable/actions/kopeteavailable.svgz
%_kde_iconsdir/oxygen/scalable/actions/kopeteeditstatusmessage.svgz
%_kde_iconsdir/oxygen/scalable/actions/voicecall.svgz
%_kde_iconsdir/oxygen/scalable/actions/webcamreceive.svgz
%_kde_iconsdir/oxygen/scalable/actions/webcamsend.svgz

%dir %_kde_appsdir/kopete_history/
%_kde_appsdir/kopete_history/historychatui.rc
%_kde_appsdir/kopete_history/historyui.rc
%dir %_kde_appsdir/kopete_msn/
%_kde_appsdir/kopete_msn/msnchatui.rc
%dir %_kde_appsdir/kopete_privacy/
%_kde_appsdir/kopete_privacy/privacychatui.rc
%_kde_appsdir/kopete_privacy/privacyui.rc
%dir %_kde_appsdir/kopete_translator/
%_kde_appsdir/kopete_translator/translatorchatui.rc
%_kde_appsdir/kopete_translator/translatorui.rc
%dir %_kde_appsdir/kopete_yahoo/
%_kde_appsdir/kopete_yahoo/yahoochatui.rc
%_kde_appsdir/kopete_yahoo/yahooconferenceui.rc
%_kde_appsdir/kopete_yahoo/yahooimui.rc
%_kde_appsdir/kopeterichtexteditpart/kopeterichtexteditpartfull.rc
%_kde_datadir/config.kcfg/historyconfig.kcfg
%_kde_datadir/config.kcfg/kopeteappearancesettings.kcfg
%_kde_datadir/config.kcfg/kopetebehaviorsettings.kcfg
%_kde_datadir/config.kcfg/kopetegeneralsettings.kcfg
%_kde_datadir/config.kcfg/kopeteidentityconfigpreferences.kcfg
%_kde_datadir/config.kcfg/nowlisteningconfig.kcfg
%_kde_appsdir/kopete/icons/crystalsvg/16x16/actions/aim_connecting.mng
%_kde_appsdir/kopete/icons/crystalsvg/16x16/actions/gg_con.mng
%_kde_appsdir/kopete/icons/crystalsvg/16x16/actions/icq_connecting.mng
%_kde_appsdir/kopete/icons/crystalsvg/16x16/actions/msn_connecting.mng
%_kde_appsdir/kopete/icons/crystalsvg/16x16/actions/qq_connecting.mng
%_kde_appsdir/kopete/icons/crystalsvg/16x16/actions/yahoo_connecting.mng
%_kde_appsdir/kopete/icons/crystalsvg/22x22/actions/qq_connecting.mng
%_kde_appsdir/kopete/icons/crystalsvg/32x32/actions/qq_connecting.mng
%_kde_appsdir/kopete/icons/crystalsvg/48x48/actions/qq_connecting.mng
%_kde_appsdir/kopete/icons/crystalsvg/64x64/actions/qq_connecting.mng
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/aim_away.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/aim_connecting.mng
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/aim_offline.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/aim_online.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_away.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_connecting.mng
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_dnd.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_ffc.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_invisible.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_na.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_occupied.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_offline.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_online.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus0.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus1.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus10.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus11.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus12.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus13.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus14.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus15.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus16.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus17.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus18.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus19.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus2.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus20.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus21.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus22.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus23.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus24.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus25.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus26.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus27.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus28.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus29.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus3.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus30.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus31.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus4.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus5.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus6.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus7.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus8.png
%_kde_appsdir/kopete/icons/hicolor/16x16/actions/icq_xstatus9.png
%_kde_appsdir/kopete/icons/hicolor/16x16/apps/aim_protocol.png
%_kde_appsdir/kopete/icons/hicolor/16x16/apps/icq_protocol.png
%_kde_appsdir/kopete/icons/hicolor/32x32/apps/aim_protocol.png
%_kde_appsdir/kopete/icons/hicolor/32x32/apps/icq_protocol.png
%_kde_appsdir/kopete/icons/oxygen/128x128/apps/aim_protocol.png
%_kde_appsdir/kopete/icons/oxygen/128x128/apps/icq_protocol.png
%_kde_appsdir/kopete/icons/oxygen/128x128/apps/msn_protocol.png
%_kde_appsdir/kopete/icons/oxygen/128x128/apps/qq_protocol.png
%_kde_appsdir/kopete/icons/oxygen/128x128/apps/sms_protocol.png
%_kde_appsdir/kopete/icons/oxygen/128x128/apps/testbed_protocol.png
%_kde_appsdir/kopete/icons/oxygen/128x128/apps/wp_protocol.png
%_kde_appsdir/kopete/icons/oxygen/128x128/apps/yahoo_protocol.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/aim_away.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/aim_offline.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/aim_online.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/aim_overlay.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/gg_away.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/gg_busy.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/gg_busy_d.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/gg_connecting.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/gg_ignored.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/gg_invi.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/gg_invi_d.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/gg_offline.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/gg_offline_d.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/gg_online.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/gg_online_d.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/icq_away.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/icq_dnd.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/icq_ffc.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/icq_invisible.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/icq_na.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/icq_occupied.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/icq_offline.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/icq_online.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/icq_overlay.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/kgpg_key1.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/kgpg_key2.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/kgpg_key3.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/msn_away.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/msn_blocked.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/msn_brb.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/msn_busy.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/msn_invisible.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/msn_lunch.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/msn_na.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/msn_newmsg.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/msn_offline.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/msn_online.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/msn_phone.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/wp_away.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/yahoo_away.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/yahoo_busy.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/yahoo_idle.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/yahoo_invisible.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/yahoo_mobile.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/yahoo_stealthed.png
%_kde_appsdir/kopete/icons/oxygen/16x16/actions/yahoo_tea.png
%_kde_appsdir/kopete/icons/oxygen/16x16/apps/aim_protocol.png
%_kde_appsdir/kopete/icons/oxygen/16x16/apps/gadu_protocol.png
%_kde_appsdir/kopete/icons/oxygen/16x16/apps/icq_protocol.png
%_kde_appsdir/kopete/icons/oxygen/16x16/apps/msn_protocol.png
%_kde_appsdir/kopete/icons/oxygen/16x16/apps/qq_protocol.png
%_kde_appsdir/kopete/icons/oxygen/16x16/apps/sms_protocol.png
%_kde_appsdir/kopete/icons/oxygen/16x16/apps/testbed_protocol.png
%_kde_appsdir/kopete/icons/oxygen/16x16/apps/wp_protocol.png
%_kde_appsdir/kopete/icons/oxygen/16x16/apps/yahoo_protocol.png
%_kde_appsdir/kopete/icons/oxygen/22x22/actions/yahoo_stealthed.png
%_kde_appsdir/kopete/icons/oxygen/22x22/apps/qq_protocol.png
%_kde_appsdir/kopete/icons/oxygen/32x32/actions/yahoo_stealthed.png
%_kde_appsdir/kopete/icons/oxygen/32x32/apps/aim_protocol.png
%_kde_appsdir/kopete/icons/oxygen/32x32/apps/autoreplace.png
%_kde_appsdir/kopete/icons/oxygen/32x32/apps/gadu_protocol.png
%_kde_appsdir/kopete/icons/oxygen/32x32/apps/highlight.png
%_kde_appsdir/kopete/icons/oxygen/32x32/apps/icq_protocol.png
%_kde_appsdir/kopete/icons/oxygen/32x32/apps/latex.png
%_kde_appsdir/kopete/icons/oxygen/32x32/apps/msn_protocol.png
%_kde_appsdir/kopete/icons/oxygen/32x32/apps/qq_protocol.png
%_kde_appsdir/kopete/icons/oxygen/32x32/apps/sms_protocol.png
%_kde_appsdir/kopete/icons/oxygen/32x32/apps/testbed_protocol.png
%_kde_appsdir/kopete/icons/oxygen/32x32/apps/texteffect.png
%_kde_appsdir/kopete/icons/oxygen/32x32/apps/wp_protocol.png
%_kde_appsdir/kopete/icons/oxygen/32x32/apps/yahoo_protocol.png
%_kde_appsdir/kopete/icons/oxygen/48x48/apps/aim_protocol.png
%_kde_appsdir/kopete/icons/oxygen/48x48/apps/icq_protocol.png
%_kde_appsdir/kopete/icons/oxygen/48x48/apps/msn_protocol.png
%_kde_appsdir/kopete/icons/oxygen/48x48/apps/qq_protocol.png
%_kde_appsdir/kopete/icons/oxygen/48x48/apps/sms_protocol.png
%_kde_appsdir/kopete/icons/oxygen/48x48/apps/testbed_protocol.png
%_kde_appsdir/kopete/icons/oxygen/48x48/apps/wp_protocol.png
%_kde_appsdir/kopete/icons/oxygen/48x48/apps/yahoo_protocol.png
%_kde_appsdir/kopete/icons/oxygen/64x64/apps/aim_protocol.png
%_kde_appsdir/kopete/icons/oxygen/64x64/apps/icq_protocol.png
%_kde_appsdir/kopete/icons/oxygen/64x64/apps/msn_protocol.png
%_kde_appsdir/kopete/icons/oxygen/64x64/apps/qq_protocol.png
%_kde_appsdir/kopete/icons/oxygen/64x64/apps/sms_protocol.png
%_kde_appsdir/kopete/icons/oxygen/64x64/apps/testbed_protocol.png
%_kde_appsdir/kopete/icons/oxygen/64x64/apps/wp_protocol.png
%_kde_appsdir/kopete/icons/oxygen/64x64/apps/yahoo_protocol.png

%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/main.css
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/puce.png
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/Footer.html
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/Header.html
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/Incoming/Action.html
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/Incoming/Content.html
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/Incoming/NextContent.html
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/Incoming/buddy_icon.png
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/Outgoing/Action.html
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/Outgoing/Content.html
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/Outgoing/NextContent.html
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/Outgoing/buddy_icon.png
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/Status.html
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/Variants/Big_pictures.css
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/Variants/Contact_color.css
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/images/action.png
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/images/important.png
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/images/system.png
%_kde_appsdir/kopete/styles/Kopete/Contents/Resources/main.css
%_kde_appsdir/kopete/styles/Retropete/Contents/Resources/Footer.html
%_kde_appsdir/kopete/styles/Retropete/Contents/Resources/Header.html
%_kde_appsdir/kopete/styles/Retropete/Contents/Resources/Incoming/Action.html
%_kde_appsdir/kopete/styles/Retropete/Contents/Resources/Incoming/Content.html
%_kde_appsdir/kopete/styles/Retropete/Contents/Resources/Incoming/NextContent.html
%_kde_appsdir/kopete/styles/Retropete/Contents/Resources/Outgoing/Action.html
%_kde_appsdir/kopete/styles/Retropete/Contents/Resources/Outgoing/Content.html
%_kde_appsdir/kopete/styles/Retropete/Contents/Resources/Outgoing/NextContent.html
%_kde_appsdir/kopete/styles/Retropete/Contents/Resources/Status.html
%_kde_appsdir/kopete/styles/Retropete/Contents/Resources/main.css
%_kde_appsdir/kopete/webpresence/webpresence_html.xsl
%_kde_appsdir/kopete/webpresence/webpresence_html_images.xsl
%_kde_appsdir/kopete/webpresence/webpresence_xhtml.xsl
%_kde_appsdir/kopete/webpresence/webpresence_xhtml_images.xsl
%_kde_appsdir/kopete_contactnotes/contactnotesui.rc
%_kde_appsdir/kopete_cryptography/cryptographychatui.rc
%_kde_appsdir/kopete_cryptography/cryptographyui.rc
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Variants/Dark2.css
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Variants/Light-Noback.css
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Variants/Light.css
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Variants/Light2-Noback.css
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Variants/Light2.css
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/images/background.png
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/images/background2.png
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/images/kopete.png
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/main.css
%_kde_appsdir/kopete/styles/Hacker/README
%_kde_appsdir/kopete/styles/Hacker/gpl.txt
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Footer.html
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Header.html
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Incoming/Content.html
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Incoming/NextContent.html
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Incoming/buddy_icon.png
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Outgoing/Content.html
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Outgoing/NextContent.html
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Outgoing/buddy_icon.png
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Status.html
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/Side_blue.css
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/Side_blue_moon.css
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/Side_blue_moon_without_transparency.css
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/Side_blue_without_transparency.css
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/Side_green.css
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/Side_green_without_trans.css
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/Side_green_without_transparency.css
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/konqui/cadre1.png
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/konqui/cadre2.png
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/konqui/cadre3.png
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/konqui/cadre4.png
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/konqui/cadre5.png
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/konqui/cadre6.png
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/konqui/konqui-blue.png
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/konqui/konqui-green.png
%_kde_appsdir/kopete/styles/Konqi/Contents/Resources/Variants/konqui/konqui-moon.jpg
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/Footer.html
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/Header.html
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/Incoming/Action.html
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/Incoming/Content.html
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/Incoming/NextContent.html
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/Outgoing/Action.html
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/Outgoing/Content.html
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/Outgoing/NextContent.html
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/Status.html
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/Variants/Contact-Colors.css
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/Variants/Name-Colors.css
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/Variants/No-Colors.css
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/Variants/Status-Colors.css
%_kde_appsdir/kopete/styles/Gaim/Contents/Resources/main.css
%_kde_appsdir/kopete/styles/Hacker/COPYRIGHT
%_kde_appsdir/kopete/styles/Hacker/Contents/Info.plist
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Footer.html
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Header.html
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Incoming/Action.html
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Incoming/Content.html
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Incoming/Context.html
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Incoming/NextContent.html
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Incoming/NextContext.html
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Incoming/buddy_icon.png
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Outgoing/Action.html
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Outgoing/Content.html
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Outgoing/Context.html
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Outgoing/NextContent.html
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Outgoing/NextContext.html
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Outgoing/buddy_icon.png
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Status.html
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Variants/Dark-Noback.css
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Variants/Dark.css
%_kde_appsdir/kopete/styles/Hacker/Contents/Resources/Variants/Dark2-Noback.css
%_kde_appsdir/kopete/styles/Clear/Contents/Resources/Outgoing/Action.html
%_kde_appsdir/kopete/styles/Clear/Contents/Resources/Outgoing/Content.html
%_kde_appsdir/kopete/styles/Clear/Contents/Resources/Outgoing/NextContent.html
%_kde_appsdir/kopete/styles/Clear/Contents/Resources/Outgoing/buddy_icon.png
%_kde_appsdir/kopete/styles/Clear/Contents/Resources/Status.html
"%_kde_appsdir/kopete/styles/Clear/Contents/Resources/Variants/No avatars.css"
%_kde_appsdir/kopete/styles/Clear/Contents/Resources/images/*.png
%_kde_appsdir/kopete/styles/Clear/Contents/Resources/main.css
%_kde_appsdir/kopete/styles/Gaim/Contents/Info.plist

%_kde_appsdir/kopete/kopete.notifyrc
%_kde_appsdir/kopete/kopetechatwindow.rc
%_kde_appsdir/kopete/kopetecommandui.rc
%_kde_appsdir/kopete/kopeteemailwindow.rc
%_kde_appsdir/kopete/kopeteui.rc
%_kde_appsdir/kopete/nowlisteningchatui.rc
%_kde_appsdir/kopete/nowlisteningui.rc
%_kde_appsdir/kopete/styles/Clean/Contents/Resources/Footer.html
%_kde_appsdir/kopete/styles/Clean/Contents/Resources/Header.html
%_kde_appsdir/kopete/styles/Clean/Contents/Resources/Incoming/*.html
%_kde_appsdir/kopete/styles/Clean/Contents/Resources/Incoming/buddy_icon.png
%_kde_appsdir/kopete/styles/Clean/Contents/Resources/Outgoing/Content.html
%_kde_appsdir/kopete/styles/Clean/Contents/Resources/Outgoing/NextContent.html
%_kde_appsdir/kopete/styles/Clean/Contents/Resources/Outgoing/buddy_icon.png
%_kde_appsdir/kopete/styles/Clean/Contents/Resources/Status.html
%_kde_appsdir/kopete/styles/Clean/Contents/Resources/images/action.png
%_kde_appsdir/kopete/styles/Clean/Contents/Resources/images/important.png
%_kde_appsdir/kopete/styles/Clean/Contents/Resources/images/internal.png
%_kde_appsdir/kopete/styles/Clean/Contents/Resources/main.css
%_kde_appsdir/kopete/styles/Clear/Contents/Resources/Footer.html
%_kde_appsdir/kopete/styles/Clear/Contents/Resources/Header.html
%_kde_appsdir/kopete/styles/Clear/Contents/Resources/Incoming/Action.html
%_kde_appsdir/kopete/styles/Clear/Contents/Resources/Incoming/Content.html
%_kde_appsdir/kopete/styles/Clear/Contents/Resources/Incoming/NextContent.html
%_kde_appsdir/kopete/styles/Clear/Contents/Resources/Incoming/buddy_icon.png

%dir %_kde_docdir/HTML/en/kopete/
%doc %_kde_docdir/HTML/en/kopete/*.bz2
%doc %_kde_docdir/HTML/en/kopete/*.docbook

#-----------------------------------------------------------

%package  kopete-latex
Group: Graphical desktop/KDE
Summary: Kopete latex plugin for write andd read mesages in latex
Requires: kopete4
Requires: ImageMagick	

%description kopete-latex
Kopete latex plugin for write andd read mesages in latexinder

%files kopete-latex
%defattr(-,root,root,-)
%_kde_bindir/kopete_latexconvert.sh
%_kde_appsdir/kopete_latex/latexchatui.rc
%_kde_datadir/config.kcfg/latexconfig.kcfg
%_kde_libdir/kde4/kopete_latex.so

#-----------------------------------------------------------

%package -n %lib_name-kopete-devel
Summary: Devel file.
Group:		Development/KDE and Qt 
Requires: %lib_name-kopete = %{epoch}:%version-%release

%description -n %lib_name-kopete-devel
Kopete Devel files

%files -n %lib_name-kopete-devel
%defattr(-, root, root)
%_kde_libdir/libkopete.so
%_kde_libdir/libkopete_msn_shared.so
%_kde_libdir/libkopete_oscar.so
%_kde_libdir/libkopete_videodevice.so
%_kde_libdir/libgadu_kopete.so
%_kde_libdir/libkopeteaddaccountwizard.so
%_kde_libdir/libkopetechatwindow_shared.so
%_kde_libdir/libkopeteprivacy.so
%_kde_libdir/libkyahoo.so
%_kde_libdir/liboscar.so

%dir %_kde_includedir/kopete/
%dir %_kde_includedir/kopete/ui/
%_kde_includedir/kopete/ui/*.h
%_kde_includedir/kopete/*.h

#-----------------------------------------------------------

%package -n lisa4
Group: Graphical desktop/KDE
Summary: Lisa server
Requires: %name-core >= %{epoch}:%version-%release

%description -n lisa4
LISa is intended to provide a kind of "network neighbourhood" but only
relying on the TCP/IP protocol stack, no smb or whatever.

%post -n lisa4
/sbin/ldconfig
%_post_service lisa4

%preun -n lisa4
%_preun_service lisa4

%postun -n lisa4 -p /sbin/ldconfig

%files -n lisa4
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

%package kppp
Group: Graphical desktop/KDE
Summary: Dialer and front end for pppd
Requires: %name-core >= %epoch:%version-%release
Requires: ppp, %name-kppp-provider
Provides: kppp4

%description kppp
Kppp is a dialer and front end for pppd.

%post kppp -p /sbin/ldconfig

%postun kppp -p /sbin/ldconfig

%files kppp
%defattr(-,root,root,-)
%dir %_sysconfdir/pam.d/
%config(noreplace) %_sysconfdir/pam.d/kppp
%attr(4755,root,root) %_kde_bindir/kppp
%_kde_bindir/kppplogview
%dir %_kde_appsdir/kppp
%_kde_appsdir/kppp/*
%_kde_datadir/applications/kde4/Kppp.desktop
%_kde_datadir/applications/kde4/kppplogview.desktop
%_kde_iconsdir/*/*/*/kppp.png
%_kde_datadir/dbus-1/interfaces/org.kde.kppp.xml
%exclude %_kde_appsdir/kppp/Rules
%exclude %_kde_appsdir/kppp/Provider

%dir %_kde_docdir/HTML/en/kppp/
%doc %_kde_docdir/HTML/en/kppp/*.docbook
%doc %_kde_docdir/HTML/en/kppp/*.bz2
%doc %_kde_docdir/HTML/en/kppp/*.png

#-----------------------------------------------------------

%package kppp-provider
Group: Graphical desktop/KDE
Summary: List of providers for pppd

%description kppp-provider
List of providers for kppp

%files kppp-provider
%defattr(-,root,root,-)
%_kde_appsdir/kppp/Rules
%_kde_appsdir/kppp/Provider

#-----------------------------------------------------------

%package -n %lib_name-kwifimanager
Group:      Development/KDE and Qt 
Summary:    Libraries for kwifimanager
BuildRequires:	wireless-tools

%description -n %lib_name-kwifimanager
Libraries for kwifimanager

%post -n %lib_name-kwifimanager -p /sbin/ldconfig
%postun -n %lib_name-kwifimanager -p /sbin/ldconfig

%files -n %lib_name-kwifimanager
%defattr(-,root,root,-)

#-----------------------------------------------------------

%package kget
Group: Graphical desktop/KDE
Summary: Kget program
Provides: kget4
Requires: %name-core >= %epoch:%version-%release

%description kget
An advanced download manager for KDE.

%post kget -p /sbin/ldconfig

%postun kget -p /sbin/ldconfig

%files kget
%defattr(-,root,root,-)
%dir %_kde_docdir/HTML/en/kget/
%doc %_kde_docdir/HTML/en/kget/*.bz2
%doc %_kde_docdir/HTML/en/kget/*.docbook
%doc %_kde_docdir/HTML/en/kget/*.png
%_kde_bindir/kget
%_kde_datadir/applications/kde4/kget.desktop
%_kde_iconsdir/crystalsvg/16x16/apps/kget.png
%_kde_iconsdir/crystalsvg/16x16/mimetypes/kget_list.png
%_kde_iconsdir/crystalsvg/22x22/apps/kget.png
%_kde_iconsdir/crystalsvg/22x22/mimetypes/kget_list.png
%_kde_iconsdir/crystalsvg/32x32/apps/kget.png
%_kde_iconsdir/crystalsvg/32x32/mimetypes/kget_list.png
%_kde_iconsdir/crystalsvg/48x48/apps/kget.png
%_kde_iconsdir/crystalsvg/48x48/mimetypes/kget_list.png
%_kde_datadir/kde4/services/kget_kiofactory.desktop
%_kde_datadir/kde4/services/kget_multisegkiofactory.desktop
%_kde_datadir/kde4/servicetypes/kget_plugin.desktop
%_kde_datadir/sounds/KGet_Added.ogg
%_kde_datadir/sounds/KGet_Finished.ogg
%_kde_datadir/sounds/KGet_Finished_All.ogg
%_kde_datadir/sounds/KGet_Started.ogg
%_kde_appsdir/kget/icons/crystalsvg/32x32/actions/transfers_list.png
%_kde_appsdir/kget/kget.notifyrc
%_kde_appsdir/kget/kgetui.rc
%_kde_appsdir/kget/pics/kget_splash.png
%_kde_appsdir/khtml/kpartplugins/kget_plug_in.rc
%_kde_appsdir/konqueror/servicemenus/kget_download.desktop
%_kde_datadir/config.kcfg/kget.kcfg
%_kde_datadir/config.kcfg/kget_multisegkiofactory.kcfg


#-----------------------------------------------------------

%package -n %lib_name-kget
Group:      Development/KDE and Qt
Summary:    Libraries for kget
Provides:   %lib_name = %epoch:%version-%release

%description -n %lib_name-kget
Libraries for kget.

%post -n %lib_name-kget -p /sbin/ldconfig
%postun -n %lib_name-kget -p /sbin/ldconfig

%files -n %lib_name-kget
%defattr(-,root,root,-)
%_kde_libdir/kde4/khtml_kget.so
%_kde_libdir/kde4/libkget_kiofactory.so
%_kde_libdir/kde4/libkget_multisegkiofactory.so
%_kde_libdir/libkgetcore.so.*

#-----------------------------------------------------------

%package  -n %lib_name-kget-devel
Summary:        Header files for kget
Group: Development/KDE and Qt

Provides: kget4-devel = %epoch:%version-%release

%description -n %lib_name-kget-devel
Header files for kget.

%files -n %lib_name-kget-devel
%defattr(-,root,root,-)
%_kde_libdir/libkgetcore.so

#-----------------------------------------------------------

%package krfb
Group: Graphical desktop/KDE
Summary: Krfb, Krdc program
Provides: krdc4, krfb4
Requires: %name-core >= %epoch:%version-%release

%description krfb
KDE Desktop Sharing allows you to invite somebody at a remote 
location to watch and possibly control your desktop.

%post krfb -p /sbin/ldconfig

%postun krfb -p /sbin/ldconfig

%files krfb
%defattr(-,root,root,-)
%_kde_bindir/krdc
%_kde_bindir/krfb
%_kde_datadir/kde4/services/vnc.protocol
%dir %_kde_appsdir/krdc/
%_kde_appsdir/krdc/*
%_kde_iconsdir/*/*/*/krdc*
%_kde_datadir/applications/kde4/krdc.desktop
%_kde_datadir/applications/kde4/krfb.desktop

%_kde_appsdir/krfb/krfb.notifyrc
%_kde_appsdir/krfb/pics/connection-side-image.png
%_kde_appsdir/krfb/pics/eyes-closed24.png
%_kde_appsdir/krfb/pics/eyes-open24.png
%_kde_iconsdir/hicolor/16x16/apps/krfb.png
%_kde_iconsdir/hicolor/32x32/apps/krfb.png
%_kde_iconsdir/hicolor/48x48/apps/krfb.png

%dir %_kde_docdir/HTML/en/krdc/
%doc %_kde_docdir/HTML/en/krdc/*.png
%doc %_kde_docdir/HTML/en/krdc/*.docbook
%doc %_kde_docdir/HTML/en/krdc/*.bz2

%dir %_kde_docdir/HTML/en/krfb/
%doc %_kde_docdir/HTML/en/krfb/*.png
%doc %_kde_docdir/HTML/en/krfb/*.bz2
%doc %_kde_docdir/HTML/en/krfb/*.docbook


#-----------------------------------------------------------

%package knewsticker
Group: Graphical desktop/KDE
Summary: RDF newsticker applet
Provides: knewsticker4
Requires: %name-core >= %epoch:%version-%release
Requires: %lib_name-knewsticker = %{epoch}:%version-%release

%description knewsticker
Knewsticker: RDF newsticker applet

%post knewsticker -p /sbin/ldconfig

%postun knewsticker -p /sbin/ldconfig

%files knewsticker
%defattr(-,root,root,-)
%_kde_bindir/knewstickerstub 
%_kde_libdir/kde4/knewsticker_panelapplet.so
%_kde_datadir/applications/kde4/knewsticker-standalone.desktop
%dir %_kde_appsdir/knewsticker/
%_kde_appsdir/knewsticker/*
%_kde_appsdir/kicker/applets/knewsticker.desktop
%dir %_kde_appsdir/kconf_update/
%_kde_appsdir/kconf_update/knewsticker.upd
%_kde_appsdir/kconf_update/knt-0.1-0.2.pl
%_kde_iconsdir/*/*/*/knewsticker.png
%_kde_datadir/applnk/.hidden/knewstickerstub.desktop

%dir %_kde_docdir/HTML/en/knewsticker/
%doc %_kde_docdir/HTML/en/knewsticker/*.png
%doc %_kde_docdir/HTML/en/knewsticker/*.docbook
%doc %_kde_docdir/HTML/en/knewsticker/*.bz2


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

%define libkgetcore %mklibname kgetcore 5

%package -n %libkgetcore
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkgetcore
KDE 4 library.

%post -n %libkgetcore -p /sbin/ldconfig
%postun -n %libkgetcore -p /sbin/ldconfig

%files -n %libkgetcore
%defattr(-,root,root)
%_kde_libdir/libkgetcore.so.*

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

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdenetwork

%build
cd $RPM_BUILD_DIR/kdenetwork

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
cd $RPM_BUILD_DIR/kdenetwork/build/

make DESTDIR=%buildroot install

install -d -m 0755 %buildroot%_sysconfdir/rc.d/init.d
install -m 0755 %SOURCE2 %buildroot%_sysconfdir/rc.d/init.d/lisa4


#TODO install it into real sysconfig dir
install -d -m 0755 %buildroot/%_sysconfdir/pam.d/
install -m 0644 %SOURCE1 %buildroot/%_sysconfdir/pam.d/kppp

%clean
rm -fr %buildroot


