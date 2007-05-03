# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/

%define branch_date 20070502
%define support_ldap 1

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
Version: 	3.80.3
Release: 	%mkrel 0.%branch_date.3
Epoch: 		2
Group: 		Development/KDE and Qt
Summary: 	K Desktop Environment - Network Applications
License: 	GPL
URL: 		http://www.kde.org
Packager:       Mandriva Linux KDE Team <kde@mandriva.com>
%if %branch
Source: 	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdenetwork-%version-%branch_date.tar.bz2
%else
Source: 	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdenetwork-%version.tar.bz2
%endif
Source1: kdenetwork3-kppp.pamd
Source2: kdenetwork-lisa
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires: freetype2-devel
BuildRequires: gettext
%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release
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
BuildRequires: kdebase4-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: libidn-devel
BuildRequires: libgsmlib-devel
BuildRequires: mesaglut-devel
BuildRequires: X11-devel
BuildRequires: libxtst-devel
BuildRequires:	mDNSResponder-devel
%define release_min_mkrel %mkrel 3
BuildRequires:	libvncserver-devel >= 0.8.2-%{release_min_mkrel} 
#For kopete.
%define release_min_mkrel_qca2 %mkrel 8
BuildRequires: qca2-devel >= 2.0-0.beta2.${release_min_mkrel_qca2}
Requires: %name-kdict  = %epoch:%version-%release	
Requires: %name-kget = %epoch:%version-%release
Requires: %name-ktalk = %epoch:%version-%release
Requires: %name-krfb = %epoch:%version-%release
Requires: %name-kopete = %epoch:%version-%release
Requires: %name-knewsticker = %epoch:%version-%release

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

%package common
Summary:	Common files for kdenetwork
Group:		Graphical desktop/KDE

#Requires: kdebase4-progs 
Requires: %lib_name-common = %epoch:%version-%release

%description common
Common files for kdenetwork

%files common
%defattr(-,root,root,-)
%_libdir/kde4/kio_zeroconf.*

%_datadir/apps/remoteview/*

%dir %_datadir/apps/zeroconf/
%_datadir/apps/zeroconf/*
%_datadir/kde4/services/kded/dnssdwatcher.desktop
%_libdir/kde4/kded_dnssdwatcher.*
%_datadir/kde4/services/zeroconf.protocol

%dir %_docdir/HTML/en/kpf/
%doc %_docdir/HTML/en/kpf/*.bz2
%doc %_docdir/HTML/en/kpf/*.docbook

%_libdir/kde4/fileshare_propsdlgplugin.so
%_libdir/kde4/kcm_fileshare.so
%_libdir/kde4/libkcm_kcmsambaconf.so
%_datadir/applications/kde4/fileshare.desktop
%_datadir/applications/kde4/kcmsambaconf.desktop
%_iconsdir/hicolor/16x16/apps/kcmsambaconf.png

%_datadir/kde4/services/fileshare_propsdlgplugin.desktop


#-----------------------------------------------------------

%package -n %lib_name-common
Group:      Development/KDE and Qt
Summary:    Libraries for kdenetwork
Provides:   %lib_name = %epoch:%version-%release

%description -n %lib_name-common
Libraries for kdenetwork.

%post -n %lib_name-common -p /sbin/ldconfig
%postun -n %lib_name-common -p /sbin/ldconfig

%files -n %lib_name-common
%defattr(-,root,root,-)

#-----------------------------------------------------------

%package  -n %lib_name-common-devel
Summary:	Header files for kdenetwork
Group: Development/KDE and Qt

Provides: %name-devel = %epoch:%version-%release

Provides: %lib_name-devel = %epoch:%version-%release

Requires: %lib_name-common = %epoch:%version-%release

%description -n %lib_name-common-devel
Header files for kdenetwork.

%files -n %lib_name-common-devel
%defattr(-,root,root,-)
%_datadir/dbus-1/interfaces/org.kde.kdnssd.xml
#-----------------------------------------------------------

%package kopete
Group: Graphical desktop/KDE
Summary: Kopete
Requires: %name-common >= %epoch:%version-%release
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
%_bindir/kopete
%_bindir/winpopup-install.sh
%_bindir/winpopup-send.sh
%_datadir/apps/kconf_update/kopete-account-0.10.pl
%_datadir/apps/kconf_update/kopete-account-kconf_update.sh
%_datadir/apps/kconf_update/kopete-account-kconf_update.upd
%_datadir/apps/kconf_update/kopete-nameTracking.upd
%_datadir/apps/kconf_update/kopete-pluginloader.pl
%_datadir/apps/kconf_update/kopete-pluginloader.upd
%_datadir/apps/kconf_update/kopete-pluginloader2.sh
%_datadir/apps/kconf_update/kopete-pluginloader2.upd
%_datadir/applications/kde4/kopete.desktop
%_datadir/apps/kconf_update/kopete-jabberpriorityaddition-kconf_update.sh
%_datadir/apps/kconf_update/kopete-jabberpriorityaddition-kconf_update.upd
%_datadir/apps/kconf_update/kopete-jabberproxytype-kconf_update.sh
%_datadir/apps/kconf_update/kopete-jabberproxytype-kconf_update.upd

%_datadir/kde4/services/kopete_*.desktop
%_datadir/kde4/servicetypes/kopete*.desktop
%_datadir/sounds/Kopete_*.ogg
%_datadir/kde4/services/aim.protocol
%_datadir/kde4/services/chatwindow.desktop
%_datadir/kde4/services/emailwindow.desktop
%_datadir/kde4/services/kconfiguredialog/kopete_*.desktop

%_iconsdir/hicolor/22x22/actions/kopeteavailable.png
%_iconsdir/hicolor/22x22/actions/kopeteaway.png
%_iconsdir/hicolor/22x22/apps/kopete.png
%_iconsdir/hicolor/32x32/actions/kopeteavailable.png
%_iconsdir/hicolor/32x32/actions/kopeteaway.png
%_iconsdir/hicolor/32x32/actions/newmessage.mng
%_iconsdir/hicolor/32x32/apps/kopete.png
%_iconsdir/hicolor/48x48/actions/kopeteavailable.png
%_iconsdir/hicolor/48x48/actions/kopeteaway.png
%_iconsdir/hicolor/48x48/apps/kopete.png
%_iconsdir/hicolor/64x64/apps/kopete.png
%_iconsdir/hicolor/scalable/apps/kopete2.svgz
%_iconsdir/crystalsvg/32x32/actions/edit_user.png
%_iconsdir/crystalsvg/32x32/actions/kopeteavailable.png
%_iconsdir/crystalsvg/32x32/actions/kopeteaway.png
%_iconsdir/crystalsvg/32x32/actions/kopeteeditstatusmessage.png
%_iconsdir/crystalsvg/32x32/actions/metacontact_away.png
%_iconsdir/crystalsvg/32x32/actions/metacontact_offline.png
%_iconsdir/crystalsvg/32x32/actions/metacontact_online.png
%_iconsdir/crystalsvg/32x32/actions/metacontact_unknown.png
%_iconsdir/crystalsvg/32x32/actions/newmessage.mng
%_iconsdir/crystalsvg/32x32/actions/newmsg.png
%_iconsdir/crystalsvg/32x32/actions/search_user.png
%_iconsdir/crystalsvg/32x32/actions/show_offliners.png
%_iconsdir/crystalsvg/32x32/actions/voicecall.png
%_iconsdir/crystalsvg/32x32/actions/webcamreceive.png
%_iconsdir/crystalsvg/32x32/actions/webcamsend.png
%_iconsdir/crystalsvg/48x48/actions/kopeteavailable.png
%_iconsdir/crystalsvg/48x48/actions/kopeteaway.png
%_iconsdir/crystalsvg/48x48/actions/metacontact_away.png
%_iconsdir/crystalsvg/48x48/actions/metacontact_offline.png
%_iconsdir/crystalsvg/48x48/actions/metacontact_online.png
%_iconsdir/crystalsvg/48x48/actions/voicecall.png
%_iconsdir/crystalsvg/48x48/actions/webcamreceive.png
%_iconsdir/crystalsvg/48x48/actions/webcamsend.png
%_iconsdir/crystalsvg/64x64/actions/voicecall.png
%_iconsdir/crystalsvg/64x64/actions/webcamreceive.png
%_iconsdir/crystalsvg/64x64/actions/webcamsend.png
%_iconsdir/crystalsvg/scalable/actions/account_offline_overlay.svgz
%_iconsdir/hicolor/128x128/apps/kopete.png
%_iconsdir/hicolor/16x16/actions/emoticon.png
%_iconsdir/hicolor/16x16/actions/kopeteavailable.png
%_iconsdir/hicolor/16x16/actions/kopeteaway.png
%_iconsdir/hicolor/16x16/actions/newmsg.png
%_iconsdir/hicolor/16x16/actions/status_unknown.png
%_iconsdir/hicolor/16x16/actions/status_unknown_overlay.png
%_iconsdir/hicolor/16x16/apps/kopete.png
%_iconsdir/crystalsvg/16x16/actions/kopeteaway.png
%_iconsdir/crystalsvg/16x16/actions/kopeteeditstatusmessage.png
%_iconsdir/crystalsvg/16x16/actions/kopetestatusmessage.png
%_iconsdir/crystalsvg/16x16/actions/metacontact_away.png
%_iconsdir/crystalsvg/16x16/actions/metacontact_offline.png
%_iconsdir/crystalsvg/16x16/actions/metacontact_online.png
%_iconsdir/crystalsvg/16x16/actions/metacontact_unknown.png
%_iconsdir/crystalsvg/16x16/actions/newmsg.png
%_iconsdir/crystalsvg/16x16/actions/search_user.png
%_iconsdir/crystalsvg/16x16/actions/show_offliners.png
%_iconsdir/crystalsvg/16x16/actions/status_unknown.png
%_iconsdir/crystalsvg/16x16/actions/status_unknown_overlay.png
%_iconsdir/crystalsvg/16x16/actions/voicecall.png
%_iconsdir/crystalsvg/16x16/actions/webcamreceive.png
%_iconsdir/crystalsvg/16x16/actions/webcamsend.png
%_iconsdir/crystalsvg/16x16/mimetypes/kopete_emoticons.png
%_iconsdir/crystalsvg/22x22/actions/account_offline_overlay.png
%_iconsdir/crystalsvg/22x22/actions/add_user.png
%_iconsdir/crystalsvg/22x22/actions/delete_user.png
%_iconsdir/crystalsvg/22x22/actions/edit_user.png
%_iconsdir/crystalsvg/22x22/actions/kopeteavailable.png
%_iconsdir/crystalsvg/22x22/actions/kopeteaway.png
%_iconsdir/crystalsvg/22x22/actions/kopeteeditstatusmessage.png
%_iconsdir/crystalsvg/22x22/actions/search_user.png
%_iconsdir/crystalsvg/22x22/actions/show_offliners.png
%_iconsdir/crystalsvg/22x22/actions/voicecall.png
%_iconsdir/crystalsvg/22x22/actions/webcamreceive.png
%_iconsdir/crystalsvg/22x22/actions/webcamsend.png
%_iconsdir/crystalsvg/22x22/apps/kopete_all_away.png
%_iconsdir/crystalsvg/22x22/apps/kopete_offline.png
%_iconsdir/crystalsvg/22x22/apps/kopete_some_away.png
%_iconsdir/crystalsvg/22x22/apps/kopete_some_online.png
%_iconsdir/crystalsvg/22x22/mimetypes/kopete_emoticons.png
%_iconsdir/crystalsvg/32x32/actions/account_offline_overlay.png
%_iconsdir/crystalsvg/32x32/actions/add_user.png
%_iconsdir/crystalsvg/32x32/actions/delete_user.png

%dir %_datadir/apps/kopete_history/
%_datadir/apps/kopete_history/historychatui.rc
%_datadir/apps/kopete_history/historyui.rc
%dir %_datadir/apps/kopete_msn/
%_datadir/apps/kopete_msn/msnchatui.rc
%dir %_datadir/apps/kopete_privacy/
%_datadir/apps/kopete_privacy/privacychatui.rc
%_datadir/apps/kopete_privacy/privacyui.rc
%dir %_datadir/apps/kopete_translator/
%_datadir/apps/kopete_translator/translatorchatui.rc
%_datadir/apps/kopete_translator/translatorui.rc
%dir %_datadir/apps/kopete_yahoo/
%_datadir/apps/kopete_yahoo/yahoochatui.rc
%_datadir/apps/kopete_yahoo/yahooconferenceui.rc
%_datadir/apps/kopete_yahoo/yahooimui.rc
%_datadir/apps/kopeterichtexteditpart/kopeterichtexteditpartfull.rc
%_datadir/config.kcfg/historyconfig.kcfg
%_datadir/config.kcfg/kopeteappearancesettings.kcfg
%_datadir/config.kcfg/kopetebehaviorsettings.kcfg
%_datadir/config.kcfg/kopetegeneralsettings.kcfg
%_datadir/config.kcfg/kopeteidentityconfigpreferences.kcfg
%_datadir/config.kcfg/nowlisteningconfig.kcfg
%_datadir/dbus-1/interfaces/org.kde.kopete.Client.xml
%_datadir/icons/crystalsvg/128x128/actions/voicecall.png
%_datadir/icons/crystalsvg/128x128/actions/webcamreceive.png
%_datadir/icons/crystalsvg/128x128/actions/webcamsend.png
%_datadir/icons/crystalsvg/16x16/actions/account_offline_overlay.png
%_datadir/icons/crystalsvg/16x16/actions/add_user.png
%_datadir/icons/crystalsvg/16x16/actions/contact_away_overlay.png
%_datadir/icons/crystalsvg/16x16/actions/contact_busy_overlay.png
%_datadir/icons/crystalsvg/16x16/actions/contact_food_overlay.png
%_datadir/icons/crystalsvg/16x16/actions/contact_invisible_overlay.png
%_datadir/icons/crystalsvg/16x16/actions/contact_phone_overlay.png
%_datadir/icons/crystalsvg/16x16/actions/contact_xa_overlay.png
%_datadir/icons/crystalsvg/16x16/actions/delete_user.png
%_datadir/icons/crystalsvg/16x16/actions/edit_user.png
%_datadir/icons/crystalsvg/16x16/actions/emoticon.png
%_datadir/icons/crystalsvg/16x16/actions/kopeteavailable.png


%_datadir/apps/kopete/styles/Konqi/Contents/Resources/main.css
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/puce.png
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/Footer.html
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/Header.html
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/Incoming/Action.html
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/Incoming/Content.html
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/Incoming/NextContent.html
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/Incoming/buddy_icon.png
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/Outgoing/Action.html
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/Outgoing/Content.html
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/Outgoing/NextContent.html
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/Outgoing/buddy_icon.png
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/Status.html
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/Variants/Big_pictures.css
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/Variants/Contact_color.css
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/images/action.png
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/images/important.png
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/images/system.png
%_datadir/apps/kopete/styles/Kopete/Contents/Resources/main.css
%_datadir/apps/kopete/styles/Retropete/Contents/Resources/Footer.html
%_datadir/apps/kopete/styles/Retropete/Contents/Resources/Header.html
%_datadir/apps/kopete/styles/Retropete/Contents/Resources/Incoming/Action.html
%_datadir/apps/kopete/styles/Retropete/Contents/Resources/Incoming/Content.html
%_datadir/apps/kopete/styles/Retropete/Contents/Resources/Incoming/NextContent.html
%_datadir/apps/kopete/styles/Retropete/Contents/Resources/Outgoing/Action.html
%_datadir/apps/kopete/styles/Retropete/Contents/Resources/Outgoing/Content.html
%_datadir/apps/kopete/styles/Retropete/Contents/Resources/Outgoing/NextContent.html
%_datadir/apps/kopete/styles/Retropete/Contents/Resources/Status.html
%_datadir/apps/kopete/styles/Retropete/Contents/Resources/main.css
%_datadir/apps/kopete/webpresence/webpresence_html.xsl
%_datadir/apps/kopete/webpresence/webpresence_html_images.xsl
%_datadir/apps/kopete/webpresence/webpresence_xhtml.xsl
%_datadir/apps/kopete/webpresence/webpresence_xhtml_images.xsl
%_datadir/apps/kopete_contactnotes/contactnotesui.rc
%_datadir/apps/kopete_cryptography/cryptographychatui.rc
%_datadir/apps/kopete_cryptography/cryptographyui.rc
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Variants/Dark2.css
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Variants/Light-Noback.css
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Variants/Light.css
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Variants/Light2-Noback.css
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Variants/Light2.css
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/images/background.png
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/images/background2.png
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/images/kopete.png
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/main.css
%_datadir/apps/kopete/styles/Hacker/README
%_datadir/apps/kopete/styles/Hacker/gpl.txt
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Footer.html
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Header.html
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Incoming/Content.html
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Incoming/NextContent.html
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Incoming/buddy_icon.png
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Outgoing/Content.html
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Outgoing/NextContent.html
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Outgoing/buddy_icon.png
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Status.html
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/Side_blue.css
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/Side_blue_moon.css
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/Side_blue_moon_without_transparency.css
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/Side_blue_without_transparency.css
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/Side_green.css
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/Side_green_without_trans.css
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/Side_green_without_transparency.css
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/konqui/cadre1.png
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/konqui/cadre2.png
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/konqui/cadre3.png
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/konqui/cadre4.png
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/konqui/cadre5.png
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/konqui/cadre6.png
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/konqui/konqui-blue.png
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/konqui/konqui-green.png
%_datadir/apps/kopete/styles/Konqi/Contents/Resources/Variants/konqui/konqui-moon.jpg
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/Footer.html
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/Header.html
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/Incoming/Action.html
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/Incoming/Content.html
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/Incoming/NextContent.html
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/Outgoing/Action.html
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/Outgoing/Content.html
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/Outgoing/NextContent.html
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/Status.html
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/Variants/Contact-Colors.css
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/Variants/Name-Colors.css
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/Variants/No-Colors.css
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/Variants/Status-Colors.css
%_datadir/apps/kopete/styles/Gaim/Contents/Resources/main.css
%_datadir/apps/kopete/styles/Hacker/COPYRIGHT
%_datadir/apps/kopete/styles/Hacker/Contents/Info.plist
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Footer.html
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Header.html
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Incoming/Action.html
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Incoming/Content.html
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Incoming/Context.html
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Incoming/NextContent.html
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Incoming/NextContext.html
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Incoming/buddy_icon.png
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Outgoing/Action.html
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Outgoing/Content.html
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Outgoing/Context.html
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Outgoing/NextContent.html
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Outgoing/NextContext.html
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Outgoing/buddy_icon.png
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Status.html
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Variants/Dark-Noback.css
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Variants/Dark.css
%_datadir/apps/kopete/styles/Hacker/Contents/Resources/Variants/Dark2-Noback.css
%_datadir/apps/kopete/styles/Clear/Contents/Resources/Outgoing/Action.html
%_datadir/apps/kopete/styles/Clear/Contents/Resources/Outgoing/Content.html
%_datadir/apps/kopete/styles/Clear/Contents/Resources/Outgoing/NextContent.html
%_datadir/apps/kopete/styles/Clear/Contents/Resources/Outgoing/buddy_icon.png
%_datadir/apps/kopete/styles/Clear/Contents/Resources/Status.html
"%_datadir/apps/kopete/styles/Clear/Contents/Resources/Variants/No avatars.css"
%_datadir/apps/kopete/styles/Clear/Contents/Resources/images/*.png
%_datadir/apps/kopete/styles/Clear/Contents/Resources/main.css
%_datadir/apps/kopete/styles/Gaim/Contents/Info.plist

%_datadir/apps/kopete/icons/hicolor/16x16/actions/icq_ffc.png
%_datadir/apps/kopete/icons/hicolor/16x16/actions/icq_invisible.png
%_datadir/apps/kopete/icons/hicolor/16x16/actions/icq_na.png
%_datadir/apps/kopete/icons/hicolor/16x16/actions/icq_occupied.png
%_datadir/apps/kopete/icons/hicolor/16x16/actions/icq_offline.png
%_datadir/apps/kopete/icons/hicolor/16x16/actions/icq_online.png
%_datadir/apps/kopete/icons/hicolor/16x16/apps/aim_protocol.png
%_datadir/apps/kopete/icons/hicolor/16x16/apps/icq_protocol.png
%_datadir/apps/kopete/icons/hicolor/32x32/apps/aim_protocol.png
%_datadir/apps/kopete/icons/hicolor/32x32/apps/icq_protocol.png
%_datadir/apps/kopete/kopete.notifyrc
%_datadir/apps/kopete/kopetechatwindow.rc
%_datadir/apps/kopete/kopetecommandui.rc
%_datadir/apps/kopete/kopeteemailwindow.rc
%_datadir/apps/kopete/kopeteui.rc
%_datadir/apps/kopete/nowlisteningchatui.rc
%_datadir/apps/kopete/nowlisteningui.rc
%_datadir/apps/kopete/styles/Clean/Contents/Resources/Footer.html
%_datadir/apps/kopete/styles/Clean/Contents/Resources/Header.html
%_datadir/apps/kopete/styles/Clean/Contents/Resources/Incoming/*.html
%_datadir/apps/kopete/styles/Clean/Contents/Resources/Incoming/buddy_icon.png
%_datadir/apps/kopete/styles/Clean/Contents/Resources/Outgoing/Content.html
%_datadir/apps/kopete/styles/Clean/Contents/Resources/Outgoing/NextContent.html
%_datadir/apps/kopete/styles/Clean/Contents/Resources/Outgoing/buddy_icon.png
%_datadir/apps/kopete/styles/Clean/Contents/Resources/Status.html
%_datadir/apps/kopete/styles/Clean/Contents/Resources/images/action.png
%_datadir/apps/kopete/styles/Clean/Contents/Resources/images/important.png
%_datadir/apps/kopete/styles/Clean/Contents/Resources/images/internal.png
%_datadir/apps/kopete/styles/Clean/Contents/Resources/main.css
%_datadir/apps/kopete/styles/Clear/Contents/Resources/Footer.html
%_datadir/apps/kopete/styles/Clear/Contents/Resources/Header.html
%_datadir/apps/kopete/styles/Clear/Contents/Resources/Incoming/Action.html
%_datadir/apps/kopete/styles/Clear/Contents/Resources/Incoming/Content.html
%_datadir/apps/kopete/styles/Clear/Contents/Resources/Incoming/NextContent.html
%_datadir/apps/kopete/styles/Clear/Contents/Resources/Incoming/buddy_icon.png
%_datadir/apps/kopete/icons/crystalsvg/32x32/apps/*.png
%_datadir/apps/kopete/icons/crystalsvg/48x48/actions/qq_connecting.mng
%_datadir/apps/kopete/icons/crystalsvg/48x48/apps/*.png
%_datadir/apps/kopete/icons/crystalsvg/64x64/actions/qq_connecting.mng
%_datadir/apps/kopete/icons/crystalsvg/64x64/apps/*.png
%_datadir/apps/kopete/icons/hicolor/16x16/actions/*.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/msn_brb.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/msn_busy.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/msn_connecting.mng
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/msn_invisible.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/msn_lunch.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/msn_na.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/msn_newmsg.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/msn_offline.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/msn_online.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/msn_phone.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/qq_connecting.mng
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/wp_away.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/yahoo_away.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/yahoo_busy.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/yahoo_connecting.mng
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/yahoo_idle.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/yahoo_invisible.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/yahoo_mobile.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/yahoo_stealthed.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/yahoo_tea.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/apps/aim_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/apps/gadu_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/apps/icq_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/apps/msn_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/apps/qq_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/apps/sms_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/apps/testbed_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/apps/wp_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/apps/yahoo_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/22x22/actions/qq_connecting.mng
%_datadir/apps/kopete/icons/crystalsvg/22x22/actions/yahoo_stealthed.png
%_datadir/apps/kopete/icons/crystalsvg/22x22/apps/qq_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/32x32/actions/qq_connecting.mng
%_datadir/apps/kopete/icons/crystalsvg/32x32/actions/yahoo_stealthed.png
%_datadir/apps/kopete/icons/hicolor/16x16/actions/aim_connecting.mng
%_datadir/apps/kopete/icons/hicolor/16x16/actions/icq_connecting.mng
%_datadir/apps/kopete/icons/crystalsvg/128x128/apps/sms_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/128x128/apps/testbed_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/128x128/apps/wp_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/128x128/apps/yahoo_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/aim_away.png
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/*.mng
%_datadir/apps/kopete/icons/crystalsvg/16x16/actions/*.png
%_datadir/apps/kopete/icons/crystalsvg/128x128/apps/aim_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/128x128/apps/icq_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/128x128/apps/msn_protocol.png
%_datadir/apps/kopete/icons/crystalsvg/128x128/apps/qq_protocol.png

%dir %_docdir/HTML/en/kopete/
%doc %_docdir/HTML/en/kopete/*.bz2
%doc %_docdir/HTML/en/kopete/*.docbook

%package  kopete-latex
Group: Graphical desktop/KDE
Summary: Kopete latex plugin for write andd read mesages in latex
Requires: kopete4
Requires: ImageMagick	

%description kopete-latex
Kopete latex plugin for write andd read mesages in latexinder

%files kopete-latex
%defattr(-,root,root,-)
%_bindir/kopete_latexconvert.sh
%_datadir/apps/kopete_latex/latexchatui.rc
%_datadir/config.kcfg/latexconfig.kcfg
%_libdir/kde4/kopete_latex.so


#-----------------------------------------------------------

%package -n %lib_name-kopete-devel
Summary: Devel file.
Group:		Development/KDE and Qt 
#Provides: libkopete1-devel = %{epoch}:%version-%release
Requires: %lib_name-kopete = %{epoch}:%version-%release

%description -n %lib_name-kopete-devel
Kopete Devel files

%files -n %lib_name-kopete-devel
%defattr(-, root, root)
%_libdir/libkopete.so
%_libdir/libkopete_msn_shared.so
%_libdir/libkopete_oscar.so
%_libdir/libkopete_videodevice.so
%_libdir/libgadu_kopete.so
%_libdir/libkopeteaddaccountwizard.so
%_libdir/libkopetechatwindow_shared.so
%_libdir/libkopeteprivacy.so
%_libdir/libkyahoo.so
%_libdir/liboscar.so
%dir %_includedir/kopete/
%dir %_includedir/kopete/ui/
%_includedir/kopete/ui/*.h
%_includedir/kopete/*.h

#-----------------------------------------------------------

%package -n %lib_name-kopete
Summary: Multi-protocol plugin-based instant messenger
Group: 		Development/KDE and Qt
#Provides:	libkopete1 = %epoch:%version-%release

%description -n %lib_name-kopete
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

%post -n %lib_name-kopete -p /sbin/ldconfig
%postun -n %lib_name-kopete -p /sbin/ldconfig

%files -n %lib_name-kopete
%defattr(-, root, root)
%_libdir/kde4/kcm_kopete_*.so
%_libdir/kde4/kopete_*.so
%_libdir/kde4/libkrichtexteditpart.so
%_libdir/libkopeteprivacy.so.*
%_libdir/libkyahoo.so.*
%_libdir/liboscar.so.*
%_libdir/libkopeteaddaccountwizard.so.*
%_libdir/libkopetechatwindow_shared.so.*
%_libdir/libgadu_kopete.so.*
%_libdir/libkopete.so.*
%_libdir/libkopete_msn_shared.so.*
%_libdir/libkopete_oscar.so.*
%_libdir/libkopete_videodevice.so.*


#-----------------------------------------------------------

%package -n lisa4
Group: Graphical desktop/KDE
Summary: Lisa server
Requires: %name-common >= %{epoch}:%version-%release

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
%_libdir/kde4/kcm_lanbrowser.so
%_libdir/kde4/kio_lan.so
%_prefix/sbin/lisad
%dir %_datadir/apps/konqsidebartng/virtual_folders/services/
%_datadir/apps/konqsidebartng/virtual_folders/services/lisa.desktop
%dir %_datadir/apps/konqueror/dirtree/remote/
%_datadir/apps/konqueror/dirtree/remote/lan.desktop
%_datadir/apps/konqueror/servicemenus/smb2rdc.desktop
%_datadir/apps/lisa/README
%_datadir/kde4/services/kcmkiolan.desktop
%_datadir/kde4/services/kcmlisa.desktop
%_datadir/kde4/services/lan.protocol
%_datadir/kde4/services/rdp.protocol
%dir %_docdir/HTML/en/lanbrowser/
%doc %_docdir/HTML/en/lanbrowser/*.docbook
%doc %_docdir/HTML/en/lanbrowser/*.bz2
%dir %_docdir/HTML/en/lisa/
%doc %_docdir/HTML/en/lisa/*.docbook
%doc %_docdir/HTML/en/lisa/*.bz2

#-----------------------------------------------------------

%package kppp
Group: Graphical desktop/KDE
Summary: Dialer and front end for pppd
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
%attr(4755,root,root) %_bindir/kppp
%_bindir/kppplogview
%dir %_datadir/apps/kppp
%_datadir/apps/kppp/*
%_datadir/applications/kde4/Kppp.desktop
%_datadir/applications/kde4/kppplogview.desktop
%_iconsdir/*/*/*/kppp.png
%_datadir/dbus-1/interfaces/org.kde.kppp.xml
%exclude %_datadir/apps/kppp/Rules
%exclude %_datadir/apps/kppp/Provider

%dir %_docdir/HTML/en/kppp/
%doc %_docdir/HTML/en/kppp/*.docbook
%doc %_docdir/HTML/en/kppp/*.bz2
%doc %_docdir/HTML/en/kppp/*.png

#-----------------------------------------------------------

%package kppp-provider
Group: Graphical desktop/KDE
Summary: List of providers for pppd

%description kppp-provider
List of providers for kppp

%files kppp-provider
%defattr(-,root,root,-)
%_datadir/apps/kppp/Rules
%_datadir/apps/kppp/Provider

#-----------------------------------------------------------


%package kwifimanager
Group: Graphical desktop/KDE
Summary: KWifimanager
Requires: %lib_name-kwifimanager = %{epoch}:%version-%release
Provides: kwifimanager4
Requires: wireless-tools

%description kwifimanager
A wireless LAN connection monitor.

%post kwifimanager -p /sbin/ldconfig

%postun kwifimanager -p /sbin/ldconfig

%files kwifimanager
%defattr(-,root,root,-)
%_bindir/kwifimanager
%_datadir/applications/kde4/kwifimanager.desktop
%dir %_datadir/apps/kwifimanager/
%_datadir/apps/kwifimanager/*
%_iconsdir/*/*/*/kwifimanager*
%_datadir/config.kcfg/kwifimanager.kcfg

%dir %_docdir/HTML/en/kwifimanager/
%doc %_docdir/HTML/en/kwifimanager/*.docbook
%doc %_docdir/HTML/en/kwifimanager/*.bz2

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

%package kdict
Group: Graphical desktop/KDE
Summary: Kdict program
Provides: kdict4
Requires:	%lib_name-kdict = %{epoch}:%version-%release

%description -n %name-kdict
Kdict is a graphical client for the DICT Protocol. It enables you 
to search through dictionary-like databases for a word or phrase, then 
displays suitable definitions. 

%post kdict -p /sbin/ldconfig

%postun kdict -p /sbin/ldconfig

%files kdict
%defattr(-,root,root,-)
%_bindir/kdict
%_datadir/apps/kdict/icons/crystalsvg/16x16/actions/define_clip.png
%_datadir/apps/kdict/icons/crystalsvg/16x16/actions/query_erase.png
%_datadir/apps/kdict/icons/crystalsvg/22x22/actions/define_clip.png
%_datadir/apps/kdict/icons/crystalsvg/32x32/actions/define_clip.png
%_datadir/apps/kdict/kdictui.rc
%_datadir/apps/kicker/applets/kdictapplet.desktop
%_datadir/applications/kde4/kdict.desktop
%dir %_docdir/HTML/en/kdict/
%doc %_docdir/HTML/en/kdict/*.bz2
%doc %_docdir/HTML/en/kdict/*.docbook
%doc %_docdir/HTML/en/kdict/*.png

%_iconsdir/hicolor/128x128/apps/kdict.png
%_iconsdir/hicolor/16x16/apps/kdict.png
%_iconsdir/hicolor/32x32/apps/kdict.png
%_iconsdir/hicolor/48x48/apps/kdict.png
%_iconsdir/hicolor/64x64/apps/kdict.png
%_iconsdir/hicolor/scalable/apps/kdict.svgz

%package -n %lib_name-kdict
Group:      Development/KDE and Qt 
Summary:    Libraries for kdict

%description -n %lib_name-kdict
Libraries for kwifimanager

%files -n %lib_name-kdict
%defattr(-,root,root,-)
%_libdir/kde4/kdict_panelapplet.so
%_libdir/libkdeinit_kdict.so
%_datadir/dbus-1/interfaces/org.kde.kdict.xml

#-----------------------------------------------------------

%package kget
Group: Graphical desktop/KDE
Summary: Kget program
Provides: kget4
Requires:	%lib_name-kget = %{epoch}:%version-%release

%description kget
An advanced download manager for KDE.

%post kget -p /sbin/ldconfig

%postun kget -p /sbin/ldconfig

%files kget
%defattr(-,root,root,-)
%dir %_docdir/HTML/en/kget/
%doc %_docdir/HTML/en/kget/*.bz2
%doc %_docdir/HTML/en/kget/*.docbook
%doc %_docdir/HTML/en/kget/*.png
%_bindir/kget
%_datadir/applications/kde4/kget.desktop
%_iconsdir/crystalsvg/16x16/apps/kget.png
%_iconsdir/crystalsvg/16x16/mimetypes/kget_list.png
%_iconsdir/crystalsvg/22x22/apps/kget.png
%_iconsdir/crystalsvg/22x22/mimetypes/kget_list.png
%_iconsdir/crystalsvg/32x32/apps/kget.png
%_iconsdir/crystalsvg/32x32/mimetypes/kget_list.png
%_iconsdir/crystalsvg/48x48/apps/kget.png
%_iconsdir/crystalsvg/48x48/mimetypes/kget_list.png
%_datadir/kde4/services/kget_kiofactory.desktop
%_datadir/kde4/services/kget_metalinkfactory.desktop
%_datadir/kde4/services/kget_multisegkiofactory.desktop
%_datadir/kde4/servicetypes/kget_plugin.desktop
%_datadir/sounds/KGet_Added.ogg
%_datadir/sounds/KGet_Finished.ogg
%_datadir/sounds/KGet_Finished_All.ogg
%_datadir/sounds/KGet_Started.ogg
%_datadir/apps/kget/icons/crystalsvg/32x32/actions/transfers_list.png
%_datadir/apps/kget/kget.notifyrc
%_datadir/apps/kget/kgetui.rc
%_datadir/apps/kget/pics/kget_splash.png
%_datadir/apps/khtml/kpartplugins/kget_plug_in.rc
%_datadir/apps/konqueror/servicemenus/kget_download.desktop
%_datadir/config.kcfg/kget.kcfg
%_datadir/config.kcfg/kget_multisegkiofactory.kcfg


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
%_libdir/kde4/khtml_kget.so
%_libdir/kde4/libkget_kiofactory.so
%_libdir/kde4/libkget_metalinkfactory.so
%_libdir/kde4/libkget_multisegkiofactory.so
%_libdir/libkgetcore.so.*


#-----------------------------------------------------------

%package  -n %lib_name-kget-devel
Summary:        Header files for kget
Group: Development/KDE and Qt

Provides: kget4-devel = %epoch:%version-%release

%description -n %lib_name-kget-devel
Header files for kget.

%files -n %lib_name-kget-devel
%defattr(-,root,root,-)
%_libdir/libkgetcore.so

#-----------------------------------------------------------

%package krfb
Group: Graphical desktop/KDE
Summary: Krfb, Krdc program
Provides: krdc4, krfb4

%description krfb
KDE Desktop Sharing allows you to invite somebody at a remote 
location to watch and possibly control your desktop.

%post krfb -p /sbin/ldconfig

%postun krfb -p /sbin/ldconfig

%files krfb
%defattr(-,root,root,-)
%_bindir/krdc
%_datadir/kde4/services/vnc.protocol
%dir %_datadir/apps/krdc/
%_datadir/apps/krdc/*
%_iconsdir/*/*/*/krdc*
%_datadir/applications/kde4/krdc.desktop



%dir %_docdir/HTML/en/krdc/
%doc %_docdir/HTML/en/krdc/*.png
%doc %_docdir/HTML/en/krdc/*.docbook
%doc %_docdir/HTML/en/krdc/*.bz2

%dir %_docdir/HTML/en/krfb/
%doc %_docdir/HTML/en/krfb/*.png
%doc %_docdir/HTML/en/krfb/*.bz2
%doc %_docdir/HTML/en/krfb/*.docbook


#-----------------------------------------------------------

%package knewsticker
Group: Graphical desktop/KDE
Summary: RDF newsticker applet
Provides: knewsticker4
Requires: %lib_name-knewsticker = %{epoch}:%version-%release

%description knewsticker
Knewsticker: RDF newsticker applet

%post knewsticker -p /sbin/ldconfig

%postun knewsticker -p /sbin/ldconfig

%files knewsticker
%defattr(-,root,root,-)
%_bindir/knewstickerstub 
%_datadir/applications/kde4/knewsticker-standalone.desktop
%dir %_datadir/apps/knewsticker/
%_datadir/apps/knewsticker/*
%_datadir/apps/kicker/applets/knewsticker.desktop
%dir %_datadir/apps/kconf_update/
%_datadir/apps/kconf_update/knewsticker.upd
%_datadir/apps/kconf_update/knt-0.1-0.2.pl
%_iconsdir/*/*/*/knewsticker.png
%_datadir/applnk/.hidden/knewstickerstub.desktop

%dir %_docdir/HTML/en/knewsticker/
%doc %_docdir/HTML/en/knewsticker/*.png
%doc %_docdir/HTML/en/knewsticker/*.docbook
%doc %_docdir/HTML/en/knewsticker/*.bz2


#-----------------------------------------------------------

%package -n %lib_name-knewsticker
Group:      Development/KDE and Qt 
Summary:    Librarie for knewsticker

%description -n %lib_name-knewsticker
Library for knewsticker

%post -n %lib_name-knewsticker -p /sbin/ldconfig
%postun -n %lib_name-knewsticker -p /sbin/ldconfig

%files -n %lib_name-knewsticker
%defattr(-,root,root,-)
%_libdir/kde4/knewsticker_panelapplet.*

#-----------------------------------------------------------

%prep
%setup -q -nkdenetwork-%version-%branch_date

%build
cd $RPM_BUILD_DIR/kdenetwork-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make


%install
rm -fr %buildroot
cd $RPM_BUILD_DIR/kdenetwork-%version-%branch_date/build/

make DESTDIR=%buildroot install

install -d -m 0755 %buildroot/etc/rc.d/init.d
install -m 0755 %SOURCE2 %buildroot/etc/rc.d/init.d/lisa4


#TODO install it into real sysconfig dir
install -d -m 0755 %buildroot/%_sysconfdir/pam.d/
install -m 0644 %SOURCE1 %buildroot/%_sysconfdir/pam.d/kppp


mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/Kppp.desktop "Internet/Remote Access" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/krdc.desktop "Internet/Remote Access" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/knewsticker-standalone.desktop Internet/Other 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kppplogview.desktop "Internet/Remote Access" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kcmktalkd.desktop System/Configuration/KDE/Network kde 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kcmkrfb.desktop System/Configuration/KDE/Network kde 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/krfb.desktop "Internet/Remote Access" kde
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kdict.desktop "Office/Accessories" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kcmwifi.desktop System/Configuration/KDE/Network kde 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kwifimanager.desktop  System/Monitoring kde 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kopete.desktop "Internet/Instant Messaging" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/fileshare.desktop "System/Configuration/KDE/Network" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kcmsambaconf.desktop "System/Configuration/KDE/Network" 

%clean
rm -fr %buildroot



