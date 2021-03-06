#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : ktp-common-internals
Version  : 19.08.1
Release  : 12
URL      : https://download.kde.org/stable/applications/19.08.1/src/ktp-common-internals-19.08.1.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.1/src/ktp-common-internals-19.08.1.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.1/src/ktp-common-internals-19.08.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1
Requires: ktp-common-internals-bin = %{version}-%{release}
Requires: ktp-common-internals-data = %{version}-%{release}
Requires: ktp-common-internals-lib = %{version}-%{release}
Requires: ktp-common-internals-license = %{version}-%{release}
Requires: ktp-common-internals-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : doxygen
BuildRequires : knotifyconfig-dev
BuildRequires : kpeople-dev
BuildRequires : ktexteditor-dev
BuildRequires : pkg-config
BuildRequires : telepathy-qt-dev

%description
No detailed description available

%package bin
Summary: bin components for the ktp-common-internals package.
Group: Binaries
Requires: ktp-common-internals-data = %{version}-%{release}
Requires: ktp-common-internals-license = %{version}-%{release}

%description bin
bin components for the ktp-common-internals package.


%package data
Summary: data components for the ktp-common-internals package.
Group: Data

%description data
data components for the ktp-common-internals package.


%package dev
Summary: dev components for the ktp-common-internals package.
Group: Development
Requires: ktp-common-internals-lib = %{version}-%{release}
Requires: ktp-common-internals-bin = %{version}-%{release}
Requires: ktp-common-internals-data = %{version}-%{release}
Provides: ktp-common-internals-devel = %{version}-%{release}
Requires: ktp-common-internals = %{version}-%{release}
Requires: ktp-common-internals = %{version}-%{release}

%description dev
dev components for the ktp-common-internals package.


%package lib
Summary: lib components for the ktp-common-internals package.
Group: Libraries
Requires: ktp-common-internals-data = %{version}-%{release}
Requires: ktp-common-internals-license = %{version}-%{release}

%description lib
lib components for the ktp-common-internals package.


%package license
Summary: license components for the ktp-common-internals package.
Group: Default

%description license
license components for the ktp-common-internals package.


%package locales
Summary: locales components for the ktp-common-internals package.
Group: Default

%description locales
locales components for the ktp-common-internals package.


%prep
%setup -q -n ktp-common-internals-19.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567711448
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1567711448
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktp-common-internals
cp COPYING %{buildroot}/usr/share/package-licenses/ktp-common-internals/COPYING
cp COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/ktp-common-internals/COPYING.GPLv2
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/ktp-common-internals/cmake_modules_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd
%find_lang ktp-debugger
%find_lang ktp-common-internals

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ktp-debugger

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/128x128/apps/telepathy-kde.png
/usr/share/icons/hicolor/16x16/actions/im-groupwise.png
/usr/share/icons/hicolor/16x16/actions/im-irc.png
/usr/share/icons/hicolor/16x16/actions/im-local-xmpp.png
/usr/share/icons/hicolor/16x16/apps/telepathy-kde.png
/usr/share/icons/hicolor/22x22/actions/im-aim.png
/usr/share/icons/hicolor/22x22/actions/im-facebook.png
/usr/share/icons/hicolor/22x22/actions/im-gadugadu.png
/usr/share/icons/hicolor/22x22/actions/im-google-talk.png
/usr/share/icons/hicolor/22x22/actions/im-groupwise.png
/usr/share/icons/hicolor/22x22/actions/im-icq.png
/usr/share/icons/hicolor/22x22/actions/im-jabber.png
/usr/share/icons/hicolor/22x22/actions/im-local-xmpp.png
/usr/share/icons/hicolor/22x22/actions/im-msn.png
/usr/share/icons/hicolor/22x22/actions/im-qq.png
/usr/share/icons/hicolor/22x22/actions/im-skype.png
/usr/share/icons/hicolor/22x22/actions/im-yahoo.png
/usr/share/icons/hicolor/22x22/actions/show-offline.png
/usr/share/icons/hicolor/22x22/actions/sort-name.png
/usr/share/icons/hicolor/22x22/actions/sort-presence.png
/usr/share/icons/hicolor/22x22/apps/telepathy-kde.png
/usr/share/icons/hicolor/32x32/actions/im-aim.png
/usr/share/icons/hicolor/32x32/actions/im-facebook.png
/usr/share/icons/hicolor/32x32/actions/im-gadugadu.png
/usr/share/icons/hicolor/32x32/actions/im-google-talk.png
/usr/share/icons/hicolor/32x32/actions/im-groupwise.png
/usr/share/icons/hicolor/32x32/actions/im-icq.png
/usr/share/icons/hicolor/32x32/actions/im-irc.png
/usr/share/icons/hicolor/32x32/actions/im-jabber.png
/usr/share/icons/hicolor/32x32/actions/im-local-xmpp.png
/usr/share/icons/hicolor/32x32/actions/im-msn.png
/usr/share/icons/hicolor/32x32/actions/im-qq.png
/usr/share/icons/hicolor/32x32/actions/im-skype.png
/usr/share/icons/hicolor/32x32/actions/im-yahoo.png
/usr/share/icons/hicolor/32x32/apps/telepathy-kde.png
/usr/share/icons/hicolor/48x48/actions/im-aim.png
/usr/share/icons/hicolor/48x48/actions/im-facebook.png
/usr/share/icons/hicolor/48x48/actions/im-gadugadu.png
/usr/share/icons/hicolor/48x48/actions/im-google-talk.png
/usr/share/icons/hicolor/48x48/actions/im-groupwise.png
/usr/share/icons/hicolor/48x48/actions/im-icq.png
/usr/share/icons/hicolor/48x48/actions/im-jabber.png
/usr/share/icons/hicolor/48x48/actions/im-local-xmpp.png
/usr/share/icons/hicolor/48x48/actions/im-msn.png
/usr/share/icons/hicolor/48x48/actions/im-qq.png
/usr/share/icons/hicolor/48x48/actions/im-skype.png
/usr/share/icons/hicolor/48x48/actions/im-yahoo.png
/usr/share/icons/hicolor/48x48/apps/telepathy-kde.png
/usr/share/icons/hicolor/64x64/apps/telepathy-kde.png
/usr/share/icons/hicolor/scalable/apps/telepathy-kde.svgz
/usr/share/katepart5/syntax/ktpdebugoutput.xml
/usr/share/knotifications5/ktelepathy.notifyrc
/usr/share/kservicetypes5/ktp_logger_plugin.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/KTp/Logger/abstract-logger-plugin.h
/usr/include/KTp/Logger/ktplogger_export.h
/usr/include/KTp/Logger/log-entity.h
/usr/include/KTp/Logger/log-manager.h
/usr/include/KTp/Logger/log-message.h
/usr/include/KTp/Logger/log-search-hit.h
/usr/include/KTp/Logger/pending-logger-dates.h
/usr/include/KTp/Logger/pending-logger-entities.h
/usr/include/KTp/Logger/pending-logger-logs.h
/usr/include/KTp/Logger/pending-logger-operation.h
/usr/include/KTp/Logger/pending-logger-search.h
/usr/include/KTp/Logger/scrollback-manager.h
/usr/include/KTp/Models/abstract-grouping-proxy-model.h
/usr/include/KTp/Models/accounts-list-model.h
/usr/include/KTp/Models/accounts-tree-proxy-model.h
/usr/include/KTp/Models/contacts-filter-model.h
/usr/include/KTp/Models/contacts-list-model.h
/usr/include/KTp/Models/contacts-model.h
/usr/include/KTp/Models/groups-tree-proxy-model.h
/usr/include/KTp/Models/ktpmodels_export.h
/usr/include/KTp/Models/presence-model.h
/usr/include/KTp/Models/rooms-model.h
/usr/include/KTp/Models/text-channel-watcher-proxy-model.h
/usr/include/KTp/OTR/channel-adapter.h
/usr/include/KTp/OTR/channel-proxy-interface.h
/usr/include/KTp/OTR/constants.h
/usr/include/KTp/OTR/ktpotr_export.h
/usr/include/KTp/OTR/proxy-service-interface.h
/usr/include/KTp/OTR/types.h
/usr/include/KTp/OTR/utils.h
/usr/include/KTp/Widgets/accounts-combo-box.h
/usr/include/KTp/Widgets/add-contact-dialog.h
/usr/include/KTp/Widgets/contact-grid-dialog.h
/usr/include/KTp/Widgets/contact-grid-widget.h
/usr/include/KTp/Widgets/contact-info-dialog.h
/usr/include/KTp/Widgets/contact-view-widget.h
/usr/include/KTp/Widgets/join-chat-room-dialog.h
/usr/include/KTp/Widgets/notification-config-dialog.h
/usr/include/KTp/Widgets/settings-kcm-dialog.h
/usr/include/KTp/Widgets/start-chat-dialog.h
/usr/include/KTp/abstract-message-filter.h
/usr/include/KTp/actions.h
/usr/include/KTp/circular-countdown.h
/usr/include/KTp/contact-factory.h
/usr/include/KTp/contact.h
/usr/include/KTp/core.h
/usr/include/KTp/debug.h
/usr/include/KTp/error-dictionary.h
/usr/include/KTp/global-contact-manager.h
/usr/include/KTp/global-presence.h
/usr/include/KTp/ktpcommoninternals_export.h
/usr/include/KTp/logs-importer.h
/usr/include/KTp/message-context.h
/usr/include/KTp/message-filter-config-manager.h
/usr/include/KTp/message-processor.h
/usr/include/KTp/message.h
/usr/include/KTp/outgoing-message.h
/usr/include/KTp/pending-wallet.h
/usr/include/KTp/persistent-contact.h
/usr/include/KTp/presence.h
/usr/include/KTp/service-availability-checker.h
/usr/include/KTp/telepathy-handler-application.h
/usr/include/KTp/text-parser.h
/usr/include/KTp/types.h
/usr/include/KTp/wallet-interface.h
/usr/include/KTp/wallet-utils.h
/usr/lib64/cmake/KTp/KTpConfig.cmake
/usr/lib64/cmake/KTp/KTpConfigVersion.cmake
/usr/lib64/cmake/KTp/KTpTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KTp/KTpTargets.cmake
/usr/lib64/libKTpCommonInternals.so
/usr/lib64/libKTpLogger.so
/usr/lib64/libKTpModels.so
/usr/lib64/libKTpOTR.so
/usr/lib64/libKTpWidgets.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKTpCommonInternals.so.19.08.1
/usr/lib64/libKTpCommonInternals.so.9
/usr/lib64/libKTpLogger.so.19.08.1
/usr/lib64/libKTpLogger.so.9
/usr/lib64/libKTpModels.so.19.08.1
/usr/lib64/libKTpModels.so.9
/usr/lib64/libKTpOTR.so.19.08.1
/usr/lib64/libKTpOTR.so.9
/usr/lib64/libKTpWidgets.so.19.08.1
/usr/lib64/libKTpWidgets.so.9
/usr/lib64/qt5/plugins/kpeople/actions/ktp_kpeople_plugin.so
/usr/lib64/qt5/plugins/kpeople/datasource/im_persons_data_source_plugin.so
/usr/lib64/qt5/plugins/kpeople/widgets/imdetailswidgetplugin.so
/usr/lib64/qt5/plugins/kpeople/widgets/kpeople_chat_plugin.so
/usr/lib64/qt5/qml/org/kde/telepathy/libktpqmlplugin.so
/usr/lib64/qt5/qml/org/kde/telepathy/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktp-common-internals/COPYING
/usr/share/package-licenses/ktp-common-internals/COPYING.GPLv2
/usr/share/package-licenses/ktp-common-internals/cmake_modules_COPYING-CMAKE-SCRIPTS

%files locales -f ktp-debugger.lang -f ktp-common-internals.lang
%defattr(-,root,root,-)

