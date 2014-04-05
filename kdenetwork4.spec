Summary:	K Desktop Environment - Network Applications
Name:		kdenetwork4
Version:	4.12.4
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Suggests:	kdenetwork-filesharing
Suggests:	kdenetwork-strigi-analyzers
Suggests:	kdnssd
Suggests:	kget
Suggests:	kopete
Suggests:	kppp
Suggests:	krdc
Suggests:	krfb
Obsoletes:	kdenetwork4-devel < 3:4.11.0
BuildArch:	noarch

%description
Networking applications for the K Desktop Environment:
 - kdenetwork-filesharing: Samba filesharing dialog for KDE
 - kdenetwork-strigi-analyzers: KDE network strigi plugins
 - kdnssd: DNS-SD service discovery monitor
 - kget: Versatile and user-friendly download manager for KDE
 - kopete: KDE internet messenger
 - kppp: KDE tool to setup PPP (Point-to-Point Protocol) connections
 - krfb: Desktop Sharing server, allow others to access your desktop via VNC
 - krdc: a client for Desktop Sharing and other VNC servers

%files

#----------------------------------------------------------------------------

%prep

%build

%install

%changelog
* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.1-1
- New version 4.11.1

* Thu Aug 22 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.0-2
- Update Suggests
- Update description

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.0-1
- New version 4.11.0
- Just a metapackage from now on
- Fix description

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.5-1
- New version 4.10.5
- New subpackage kdenetwork-strigi-analyzers
- Update files for kget and for main package (now it's pure metapackage)

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.2-1
- New version 4.10.2
- Add new files

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.1-1
- New version 4.10.1
- Add patch to fix build with giflib5
- Add patch to fix krfb soversion
- Fix krdccore library package major version
- Add control over library major versions

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.0-1
- New version 4.10.0
- Add pkgconfig(xtst) to BuildRequires

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.1-1
- New version 4.9.1

* Wed Aug 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.0-2
- New version 4.9.0
- Add rpmlintrc

* Mon Jul 23 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.97-2
- Add pkgconfig(TelepathyQt4) to BuildRequires
- Update files

* Mon Jul 16 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.97-1
- New version 4.8.97
- Convert BuildRequires to pkgconfig style
- Make better usage of KDE4 path macros
- Add patch2 to fix build

* Sat Jun 30 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Wed May 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.3-69.2mib2010.2
- Add kde4-filesharing < 3:4.8.0 to krdc package to solve update issues
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.0-69.1mib2010.2
+ Revision: 762517
- Backport to 2010.2 for MIB users
- Import some patches from 2011 branch (not ported to Cooker yet)
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.8.0-1
+ Revision: 762517
- New upstream tarball
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.7.95-1
+ Revision: 748796
- New version

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.7.90-1
+ Revision: 739372
- New upstream tarball

* Mon Nov 28 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 3:4.7.80-1
+ Revision: 734582
- add a versioned buildrequires on qt4 to ensure we get the latest to build
- add new chatwindowaccessiblewidgetfactory.so plugin to kopete %%files
- add new files for kget
- drop kcm_kget_contentfetchfactory plugin, it's currently unmaintained & broken

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball 4.7.80

* Fri Sep 30 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.7.41-1
+ Revision: 702057
- Comment for now kde4-filesharing package
- Fix  %%setup
- New version / remove support of oldest mdv

* Mon Jun 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.6.4-2
+ Revision: 684408
- New version 4.6.4

* Fri May 20 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.6.3-2
+ Revision: 676293
- Requires kppp-provider ( #63336)
- Clean spec file

* Fri May 13 2011 Funda Wang <fwang@mandriva.org> 3:4.6.3-1
+ Revision: 674034
- New version 4.6.3

* Mon May 02 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.6.2-2
+ Revision: 662291
- Fix file list
- For now i comment the build of google talk, a better fix i in preparation.
- Remove patch0
- Remove mkrel
- New version 4.6.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - sync with MDVSA-2011:081

  + Funda Wang <fwang@mandriva.org>
    - disable v4l1 feature

* Mon Feb 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.6.1-2
+ Revision: 640730
- New version 4.6.1

* Sun Feb 06 2011 Funda Wang <fwang@mandriva.org> 3:4.6.0-2
+ Revision: 636496
- BR libktorrent for torrent plugin

* Wed Jan 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.6.0-1
+ Revision: 632968
- New version KDE 4.6 Final

* Thu Jan 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.5.95-1mdv2011.0
+ Revision: 629124
- New version KDE 4.6 RC2

* Fri Dec 24 2010 Funda Wang <fwang@mandriva.org> 3:4.5.90-1mdv2011.0
+ Revision: 624556
- update file list

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove patch101: Merged upstream
    - New upstream tarball

* Thu Dec 16 2010 Funda Wang <fwang@mandriva.org> 3:4.5.85-1mdv2011.0
+ Revision: 622331
- add upstream patch to detect vnc correctly

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove patch0
    - New upstream tarball

* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 3:4.5.80-1mdv2011.0
+ Revision: 601664
- new version 4.5.80 (aka 4.6 beta1)

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 3:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599248
- update file list
- tubes support disabled by upstream
- fix str fmt
- new version 4.5.77

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 3:4.5.74-0.svn1190490.1mdv2011.0
+ Revision: 591139
- new snapshot
- obsoletes core
- split core into sub packages

* Sun Oct 17 2010 Funda Wang <fwang@mandriva.org> 3:4.5.71-0.svn1185840.1mdv2011.0
+ Revision: 586253
- new snapshot
- update group

* Thu Sep 16 2010 Funda Wang <fwang@mandriva.org> 3:4.5.68-1mdv2011.0
+ Revision: 578996
- New snapshot 4.5.68
- simplify BRs

* Tue Sep 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.5.67-1mdv2011.0
+ Revision: 576502
- Fix file list
- New version 4.5.67

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.5.0-1mdv2011.0
+ Revision: 566572
- New upstream tarball
- Update to version 4.5.0

* Wed Jul 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.4.95-1mdv2011.0
+ Revision: 562867
- KDE 4.5 RC3

* Fri May 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.4.3-6mdv2010.1
+ Revision: 546482
- Do not remove krfb from menus
  CCBUG: 47260
- Rebuild in release mode

* Tue May 18 2010 Oden Eriksson <oeriksson@mandriva.com> 3:4.4.3-4mdv2010.1
+ Revision: 545176
- P5: security fix for CVE-2010-1000,1511

* Sat May 08 2010 Funda Wang <fwang@mandriva.org> 3:4.4.3-3mdv2010.1
+ Revision: 543556
- add missing requires on actural lib file

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.4.3-2mdv2010.1
+ Revision: 542105
- Update to version 4.4.3

* Wed Apr 07 2010 Ahmad Samir <ahmadsamir@mandriva.org> 3:4.4.2-2mdv2010.1
+ Revision: 532458
- add patch to fix fix libjingle build with openssl

  + Funda Wang <fwang@mandriva.org>
    - rebuild for new openssl

* Wed Mar 31 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.4.2-1mdv2010.1
+ Revision: 530110
- Fix buildRequires
- Update to version 4.4.2

* Mon Mar 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.4.1-1mdv2010.1
+ Revision: 515731
- Fix release
- Update to version 4.4.1

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 3:4.4.0-3mdv2010.1
+ Revision: 511584
- rebuilt against openssl-0.9.8m

* Fri Feb 12 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.4.0-2mdv2010.1
+ Revision: 504766
- add kget back on the menu

  + Funda Wang <fwang@mandriva.org>
    - rebuild for new libmsn

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.4.0-1mdv2010.1
+ Revision: 503461
- Fix file list
- Update to version 4.4.0

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.3.98-1mdv2010.1
+ Revision: 499232
- remove merged patches
- Update to version 4.3.98 aka "kde 4.4 RC3"
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Tue Jan 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.3.95-1mdv2010.1
+ Revision: 496514
- Fix file list
- Add patches to build against new kdewebkit
- Fix previous commit
- Update to version 4.3.95 aka "kde 4.4 RC2"
- Update to version 4.3.95 aka "kde 4.4 RC2"
- Add back menu customization patch
- Do not build the sms protocole
- Remove the cp trick as the icons belong to an other package
- Copy icons after make install step
- Fix cp macro
- Remove unused line from previous commit
- Add missing icons in hicolor

* Sun Jan 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.3.90-1mdv2010.1
+ Revision: 488617
- Fix file list
- Fix file list
- Update to kde 4.4 rc1
- Update agaisnt new libmsn

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.3.85-1mdv2010.1
+ Revision: 480753
- Update to kde 4.4 beta2

* Sun Dec 13 2009 Funda Wang <fwang@mandriva.org> 3:4.3.80-2mdv2010.1
+ Revision: 478053
- fix devel package requires

* Sat Dec 05 2009 Funda Wang <fwang@mandriva.org> 3:4.3.80-1mdv2010.1
+ Revision: 473705
- enable webkitkde

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix file list
      Fix requires on the devel package
    - Update to KDE 4.4 Beta1
    - Update to kde 4.3.77

* Mon Nov 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.3.75-1mdv2010.1
+ Revision: 469270
- properly install mozilla extension
- Do not build the mozilla plugin for the moment
- Update to kde 4.3.75
- Rebuild against new qt
- Update to kde 4.3.73

* Tue Oct 06 2009 Helio Chissini de Castro <helio@mandriva.com> 3:4.3.2-1mdv2010.0
+ Revision: 454428
- New upstream release 4.3.2.

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Requires nss_mdns in kdnssd (BUG: 54161)
    - Do not obsolete libs

* Thu Sep 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.3.1-3mdv2010.0
+ Revision: 444199
- Add obsolete for kde3 upgrade

  + Arthur Renato Mello <arthur@mandriva.com>
    - Let Kppp wizard uses default password if it is provided by Provider file

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream release 4.3.1.

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 3:4.3.0-1mdv2010.0
+ Revision: 409403
- New upstream release 4.3.0.

* Thu Jul 23 2009 Helio Chissini de Castro <helio@mandriva.com> 3:4.2.98-1mdv2010.0
+ Revision: 398746
- Update to KDE 4.3 RC3

* Sun Jul 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.2.96-1mdv2010.0
+ Revision: 394958
- Update to Rc2

* Thu Jun 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.2.95-1mdv2010.0
+ Revision: 389271
- Update to kde 4.3Rc1

* Fri Jun 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.2.90-1mdv2010.0
+ Revision: 382946
- Update to beta2

* Fri May 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.2.88-1mdv2010.0
+ Revision: 380896
- Update to kde 4.2.88
  Remove merged patches

* Sat May 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.2.87-1mdv2010.0
+ Revision: 379026
- Update to kde 4.2.87

* Sat May 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.2.85-1mdv2010.0
+ Revision: 373656
- Fix file list
- Fix file list
- Update to kde 4.2.85
- Update to kde 4.2.71

  + Funda Wang <fwang@mandriva.org>
    - gadu is still needed

* Sat May 02 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.2.70-0.svn954171.1mdv2010.0
+ Revision: 370803
- Update to kde 4.2.70

* Tue Apr 07 2009 Gustavo Pichorim Boiko <boiko@mandriva.com> 3:4.2.2-5mdv2009.1
+ Revision: 365007
- Make the search bar appear in a new line

* Mon Apr 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.2.2-4mdv2009.1
+ Revision: 364561
- Add some upstream patches from branch
    - Patch105: Automatically show the notification messages (green flags)  so people do not miss it.
- Add some upstream patches from branch
        - Patch101: Kopete: Fix icon on Pipes plugin
        - Patch102: Fix crash in kcm_sambaconf
        - Patch103: Remove the telepathy protocol
        - Patch104: Fix setting v4l2 controls with minimum values other than 0
  Remove old source tarball
  Remove unapplied patch
- [Branch] Fix crash when samba use unknown options by kde
- Remove dupplicate obsoletes

* Fri Mar 27 2009 Helio Chissini de Castro <helio@mandriva.com> 3:4.2.2-1mdv2009.1
+ Revision: 361719
- Update with 4.2.2 try#1 packages

* Sat Feb 28 2009 Helio Chissini de Castro <helio@mandriva.com> 3:4.2.1-1mdv2009.1
+ Revision: 346117
- KDE 4.2.1 try#1 upstream release

* Wed Feb 25 2009 Helio Chissini de Castro <helio@mandriva.com> 3:4.2.0-3mdv2009.1
+ Revision: 344978
- Add real requires. Suggests and lacking on proper entries in akonadi break standalone kopete install

* Mon Feb 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.2.0-2mdv2009.1
+ Revision: 340885
- Rebuild against qt4.5

* Tue Jan 27 2009 Helio Chissini de Castro <helio@mandriva.com> 3:4.2.0-1mdv2009.1
+ Revision: 334603
- Bring back the webkit part
- Update with official 4.2.0 upstream tarball

* Sun Jan 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.96-2mdv2009.1
+ Revision: 328359
- Remove the irc plugin that was activated for testing purposes

* Fri Jan 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.96-1mdv2009.1
+ Revision: 327436
- Fix File list
- Remove merged patches

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.96

* Tue Dec 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.85-2mdv2009.1
+ Revision: 318033
- Fix patch200
- Fix crash in jabber at logout

* Sun Dec 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.85-1mdv2009.1
+ Revision: 314075
- revert parts of commit 893898 to fix build

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.85

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.82-2mdv2009.1
+ Revision: 313429
- Add forgotten patch
- Update to kde 4.1.82

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Dec 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.81-1mdv2009.1
+ Revision: 308707
- Update to kde 4.1.81

* Wed Nov 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.80-4mdv2009.1
+ Revision: 306847
- Versionnate Obsoletes
  Clean spec file ( order obsoletes, provides, conflicts, ...)

* Mon Nov 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.80-3mdv2009.1
+ Revision: 306471
- Fix file list
- Remove wrong obsoletes
- Some more obsoletes
- first step to the removal of old kde3 kdenetwork
  Obsoletes the begining of the kdenetwork3 apps
  Step2 come later this day so please do not touch this for the moment
  ( help will be appreciated after ;) )

* Sun Nov 23 2008 Funda Wang <fwang@mandriva.org> 3:4.1.80-2mdv2009.1
+ Revision: 305966
- rebuild
- build meanwhile protocol
- revert last commitment (kget interact with workspace)
- kdenetwork only uses plasma

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix irc protocol activation
    - Remove merged patches

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.80

* Mon Nov 17 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.73-2mdv2009.1
+ Revision: 303855
- Add Windows Live Messenger protocol instead of the Old MSN protocol

* Fri Nov 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.73-1mdv2009.1
+ Revision: 302948
- Update to kde 4.1.73
  Fix Link in libiris
  Remove unneeded patches
- Show Kppp on Menu

* Sun Nov 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.71-9mdv2009.1
+ Revision: 299227
- Make use if cm variable

* Sun Nov 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.71-8mdv2009.1
+ Revision: 299192
- Bump release
- Enable back QQ protocol ( it is cooker :) )

* Sat Nov 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.71-7mdv2009.1
+ Revision: 299183
- account->protocol()->capabilitiesManager() check is really needed => adding it back

* Sat Nov 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.71-6mdv2009.1
+ Revision: 299176
- Comment BuildRequire
- Fix patch, no need to check account->protocol()->capabilitiesManager()
- Fix a crash in kopete when adding a jabber account
- Remove SOURCES/kdenetwork-4.1.71-add-wlm-skype-support.patch patch from svn
- Install header needed by WLM protocol (standalone)
- Fix patch number
- Remove WLM patch from playground(salem)  *sick*

* Wed Oct 29 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.71-3mdv2009.1
+ Revision: 298575
- Activate irc to make berthy happy :)
  Prepare to add the Windows Live Messenger and Skype plugins ( will be on on the next commit)

* Sat Oct 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.71-2mdv2009.1
+ Revision: 297065
- Versionnate ortp BuildRequire ( that add jingle support in jabber )

* Sat Oct 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.71-1mdv2009.1
+ Revision: 297030
- New version 4.1.71
- kdenetwork4 is a metapackage so change Requires into Suggests
  knewsticker is not anymore so remove it completly

* Tue Oct 21 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.70-1mdv2009.1
+ Revision: 295872
- Update to kde 4.1.70

* Thu Oct 02 2008 Frederic Crozat <fcrozat@mandriva.com> 3:4.1.2-2mdv2009.0
+ Revision: 290848
- Add conflicts to ease upgrade from Mdv 2008.1

* Thu Sep 25 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.1.2-1mdv2009.0
+ Revision: 288231
- KDE 4.1.2 arriving.

* Thu Sep 04 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.1.1-3mdv2009.0
+ Revision: 280883
- At first sight backporting kopete looks like a goos idea, but current issue, like protocol modifications and a lack of upstrema support due invalid backtraces show that we should stay with current 4.1.1 official version, even with some features missing. Going to safe net.

* Wed Sep 03 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.1.1-2mdv2009.0
+ Revision: 279944
- Use Kopete from trunk

* Sun Aug 31 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.1.1-1mdv2009.0
+ Revision: 277823
- Upgrade to forthcoming 4.1.1 packages

  + Funda Wang <fwang@mandriva.org>
    - do not build qq protocal, for it is not working now.
    - requires ppp

* Mon Aug 04 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.1.0-4mdv2009.0
+ Revision: 263302
- Update with current branch 4.1 patches

* Thu Jul 31 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 3:4.1.0-3mdv2009.0
+ Revision: 258581
- Added kdenetwork-4.0.85-kopete.patch from libv4l.

* Mon Jul 28 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.1.0-2mdv2009.0
+ Revision: 251666
- Update with Release Candidate 1 - 4.1.0
- Update with Release Candidate 1 - 4.1.0

* Mon Jul 21 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.0.98-2mdv2009.0
+ Revision: 239568
- Add patch1 that Find media players that were started after the plugin was created

* Thu Jul 10 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.0.98-1mdv2009.0
+ Revision: 233186
- Update with Release Candidate 1 - 4.0.98

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix Kppp menu entry ( KDE menu cleaning task)

* Mon Jul 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.0.85-1mdv2009.0
+ Revision: 232465
- New version kde 4.0.85

* Tue Jul 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.0.84-2mdv2009.0
+ Revision: 230422
- Add patch0 to fix menu entries of Kppp krfb and kget

* Fri Jun 27 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.0.84-1mdv2009.0
+ Revision: 229412
- Update with new snapshot tarballs 4.0.84
- Remove patch since is already included in upcoming 4.0.84

* Thu Jun 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.0.83-4mdv2009.0
+ Revision: 229363
- Add patch1: Do not call postNewEvent if events are not to be appended.

  + Helio Chissini de Castro <helio@mandriva.com>
    - Wrong conflicts for 2008.1 and lower

* Tue Jun 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.0.83-2mdv2009.0
+ Revision: 228657
- Add epoch in conflicts
- Add kppp-provider package

* Thu Jun 19 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.0.83-1mdv2009.0
+ Revision: 226125
- Update with new snapshot tarballs 4.0.83

* Wed Jun 11 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.0.82-1mdv2009.0
+ Revision: 218028
- Update with new snapshot tarballs 4.0.82

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Funda Wang <fwang@mandriva.org>
    - conflicts with kopete-otr

* Tue Jun 03 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.0.81-1mdv2009.0
+ Revision: 214716
- Update with new snapshot tarballs 4.0.81

* Sat May 24 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.0.80-1mdv2009.0
+ Revision: 210786
- New upstream kde4 4.1 beta1

* Mon May 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.0.74-2mdv2009.0
+ Revision: 209218
- Fix descriptions of subpackages

* Fri May 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.0.74-1mdv2009.0
+ Revision: 208236
- Versionnate BuildRequires

  + Funda Wang <fwang@mandriva.org>
    - New version 4.0.74

* Wed May 14 2008 Anssi Hannula <anssi@mandriva.org> 3:4.0.73-2mdv2009.0
+ Revision: 207177
- Add old kde3 conflicts for smooth upgrade

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix typo on file list
    - Fix File list
    - Update to kde 4.0.73

* Wed May 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.0.72-2mdv2009.0
+ Revision: 202607
- Fix BuildRequire
- Remove patch0 (unneeded )
- Update to kde 4.0.72
- Add webkitkde as buildrequire
  Fix file list
- Fix file list
- New snapshot 4.0.70
- New snapshot 4.0.69

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 alpha 1
    - Starting to push new infrastructure for devel KDE 4.1. KDE 4 will be on / now. KDE is dead. Long live KDE vi kdenetwork4/SPECS/kdenetwork4.spec ;-)

* Wed Apr 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.0.3-2mdv2008.1
+ Revision: 191545
- Add upstream patch to fix a segfault in kopete

* Fri Mar 28 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.0.3-1mdv2008.1
+ Revision: 190990
- Update for last stable release 4.0.3

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:4.0.2-2mdv2008.1
+ Revision: 182253
- Rebuild against new qt4 changes

* Sat Mar 01 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.0.2-1mdv2008.1
+ Revision: 177443
- New upstream bugfix release 4.0.2

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - fix description-line-too-long

* Sun Feb 10 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.0.1-1mdv2008.1
+ Revision: 164806
- Updating for stable KDE 4.0.1
- No more branches. From now, we will be using the monthly official KDE tarballs, as discussed by Mandriva KDE Team

* Tue Jan 08 2008 Helio Chissini de Castro <helio@mandriva.com> 3:4.0.0-1mdv2008.1
+ Revision: 146897
- Update for final stable 4.0.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:3.97.1-0.752200.1mdv2008.1
+ Revision: 137400
- New snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:3.97.1-0.746684.2mdv2008.1
+ Revision: 117080
- New snapshot

* Fri Nov 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:3.96.1-0.743004.2mdv2008.1
+ Revision: 114093
- New snapshot

* Sun Nov 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:3.96.1-0.740247.2mdv2008.1
+ Revision: 111926
- Obsoletes libkdenetwork42

* Fri Nov 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:3.96.1-0.740247.1mdv2008.1
+ Revision: 111504
- New Snapshot
  Move libqgroupwise.so from devel package to kopete one (Bug #35740)
- Add Obsoletes for libkdenetwork42-kget libkopete5 and libkopete_msn_shared5 (Bug #35188)

* Sat Nov 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:3.96.0-0.737162.1mdv2008.1
+ Revision: 109176
- KDE4 Rc1
  libpapillon_kopete have been removed

* Sun Nov 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:3.95.2-0.734821.1mdv2008.1
+ Revision: 107583
- New snapshot

* Fri Nov 02 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:3.95.1-0.732092.1mdv2008.1
+ Revision: 105411
- New Snapshot
- Fix file list
- New snapshot post Rc1
- Fix file list
- add back missing patch
- New snashot
- Activate Kopete again

  + Funda Wang <fwang@mandriva.org>
    - should be sqlite3 instead of sqlite2

* Thu Oct 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:3.94.1-0.729249.2mdv2008.1
+ Revision: 102140
- Add conflict to ease upgrade

* Thu Oct 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:3.94.1-0.729249.1mdv2008.1
+ Revision: 102071
- New snapshot

* Wed Oct 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:3.94.1-0.728807.1mdv2008.1
+ Revision: 101874
- Add BuildRequire
- Fix file list
- Fix patch fo the build without kopete
- New svn snapshot
- Fix file list ( remove duplicate files)

* Fri Oct 19 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:3.94.0-0.726703.1mdv2008.1
+ Revision: 100228
- Fix Buildrequires
- Fix BuildRequires
- Kde 4 beta3
  Fix file list

* Fri Sep 21 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 3:3.93.0-0.714148.1mdv2008.0
+ Revision: 91909
- update svn snapshot
- make all obsoletes tags versioned
- bump epoch to fix revision number

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with revision 713092

* Thu Sep 13 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.93.0-2mdv2008.0
+ Revision: 85042
- Fix build when we do not package kopete
- New svn snapshot of beta3
- Add Decibel as buildrequires for kopete

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update to revision 695413
    - Updated to revision 694391
    - Cleanup whole specfile.
    - Put back providers inside kppp package ( never understood why are separated )
    - Killed independent devel packages, one devel package to rule then all
    - Reenabled qca2
    - Update to revision 689748

* Wed Jul 04 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.91-0.683133.1mdv2008.0
+ Revision: 48119
- New snapshot

* Sun Jul 01 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:3.91-0.680437.1mdv2008.0
+ Revision: 46800
- Fix File List
- start to port spec file to the new kde layout

* Thu May 10 2007 Laurent Montel <lmontel@mandriva.org> 2:3.90.1-0.20070502.1mdv2008.0
+ Revision: 25913
- new snapshot

* Thu May 03 2007 Laurent Montel <lmontel@mandriva.org> 2:3.80.3-0.20070502.3mdv2008.0
+ Revision: 21556
- new snapshot
- Necessary to use good version (header pb with c++)
- Fix buildrequires
- new snapshot


* Sun Mar 11 2007 Laurent Montel <lmontel@mandriva.com> 3.80.3-0.20070311.3mdv2007.1
+ Revision: 141316
- new snapshot
- new snapshot
- Fix spec file
- Resumit it
- new snapshot
- 3.80.3
- Fix spec file
- new snapshot
- Fix spec files
- new snapshot
- new snapshot
- update
- Fix group
- Rename to lisa4

* Tue Jan 09 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070109.1mdv2007.1
+ Revision: 106464
- Update
- Clean up
- Import kdenetwork4

* Mon Nov 06 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-6mdv2007.0
- First package

