# spec file for package poppler

%define poppler_soname 43
%define poppler_glib_soname 8
%define poppler_qt5_soname 1

Name:           poppler
Version:        0.24.0
Release:        1
License:        GPLv2
Summary:        PDF rendering library
Url:            http://poppler.freedesktop.org/
Group:          System/Libraries
Source0:        http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lcms)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Test)

%description
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package contains the shared library.

%package qt5
Summary:        PDF rendering library (Qt 5 based shared library)
Requires:       poppler = %{version}
Obsoletes:      poppler-qt

%description qt5
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package provides the Qt 5 based shared library for applications
using the Qt 5 interface to Poppler.

%package qt5-devel
Summary:        PDF rendering library (Qt 5 interface development files)
Group:          Development/Libraries
Requires:       qt5-qtcore-devel qt5-qtgui-devel qt5-qttest-devel qt5-qtwidgets-devel qt5-qtxml-devel
Requires:       poppler-devel = %{version}
Requires:       poppler-qt5 = %{version}
Obsoletes:      poppler-qt-devel

%description qt5-devel
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package provides a Qt 5 style interface to Poppler.

%package devel
Summary:        PDF rendering library (development files)
Group:          Development/Libraries
Requires:       libjpeg-devel
Requires:       pkgconfig
Requires:       poppler = %{version}

%description devel
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package contains the headers and development libraries needed to
build applications using Poppler.

%package glib
Summary:        PDF rendering library (GLib-based shared library)
Group:          System/Libraries
Requires:       poppler = %{version}

%description glib
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package provides the GLib-based shared library for applications
using the GLib interface to Poppler.

%package glib-devel
Summary:        PDF rendering library (GLib interface development files)
Group:          Development/Libraries
Requires:       glib2-devel
Requires:       poppler-devel = %{version}
Requires:       poppler-glib = %{version}

%description glib-devel
Poppler is a PDF rendering library based on xpdf PDF viewer.

This package provides a GLib-style interface to Poppler.

%package utils
Summary:        PDF utilitites (based on libpoppler)
Group:          Applications/Text
Requires:       poppler >= %{version}

%description utils
This package contains pdftops (PDF to PostScript converter), pdfinfo
(PDF document information extractor), pdfimages (PDF image extractor),
pdftohtml (PDF to HTML converter), pdftotext (PDF to text converter),
and pdffonts (PDF font analyzer).

%prep
%setup -q -n %{name}-%{version}/poppler

%build
autoreconf -vfi %configure \
  --enable-shared \
  --disable-static \
  --enable-xpdf-headers \
  --disable-libopenjpeg \
  --enable-zlib \
  --enable-libcurl \
  --enable-libjpeg \
  --enable-libpng \
  --enable-splash-output \
  --enable-cairo-output \
  --enable-poppler-glib \
  --disable-poppler-cpp \
  --disable-gtk-test \
  --enable-utils \
  --enable-cms \
  --enable-poppler-qt5

make %{?_smp_mflags}

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/*.la
%if 0%{?build_with_qt5}
cd %{buildroot}
find . -type f -o -type l | grep -v qt | xargs rm -v
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post qt5 -p /sbin/ldconfig
%postun qt5 -p /sbin/ldconfig

%post glib -p /sbin/ldconfig
%postun glib -p /sbin/ldconfig

%files qt5
%defattr(-,root,root,-)
%{_libdir}/libpoppler-qt5.so.%{poppler_qt5_soname}*

%files qt5-devel
%defattr(-,root,root,-)
%{_libdir}/libpoppler-qt5.so
%{_libdir}/pkgconfig/poppler-qt5.pc
%{_includedir}/poppler/qt5/

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_libdir}/libpoppler.so.%{poppler_soname}*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/poppler.pc
%{_libdir}/pkgconfig/poppler-splash.pc
%{_libdir}/libpoppler.so
%{_includedir}/poppler/

%files glib
%defattr(-,root,root,-)
%{_libdir}/libpoppler-glib.so.%{poppler_glib_soname}*

%files glib-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/poppler-glib.pc
%{_libdir}/pkgconfig/poppler-cairo.pc
%{_libdir}/libpoppler-glib.so

%files utils
%defattr(-,root,root,-)
%{_bindir}/pdffonts
%{_bindir}/pdfimages
%{_bindir}/pdfinfo
%{_bindir}/pdftohtml
%{_bindir}/pdftoppm
%{_bindir}/pdftops
%{_bindir}/pdftotext
%{_bindir}/pdfdetach
%{_bindir}/pdfseparate
%{_bindir}/pdftocairo
%{_bindir}/pdfunite
%{_mandir}/man1/pdffonts.*
%{_mandir}/man1/pdfimages.*
%{_mandir}/man1/pdfinfo.*
%{_mandir}/man1/pdftohtml.*
%{_mandir}/man1/pdftoppm.*
%{_mandir}/man1/pdftops.*
%{_mandir}/man1/pdftotext.*
%{_mandir}/man1/pdfdetach.1.gz
%{_mandir}/man1/pdfseparate.1.gz
%{_mandir}/man1/pdftocairo.1.gz
%{_mandir}/man1/pdfunite.1.gz
