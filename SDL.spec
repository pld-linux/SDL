#
# Conditional build:
# bcond_off_alsa - without ALSA support
# bcond_off_esound - without esound support
# bcond_off_arts - without arts support
# bcond_on_svgalib - with svgalib support
# bcond_on_aalib - with aalib support
#
Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Name:		SDL
Version:	1.1.7
Release:	3
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	http://www.libsdl.org/release/%{name}-%{version}.tar.gz
Patch0:		SDL-svga.patch
URL:		http://www.libsdl.org/
%{!?bcond_off_esound:BuildRequires:	esound-devel}
%{!?bcond_off_arts:BuildRequires:	arts-devel}
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	XFree86-devel
BuildRequires:	OpenGL-devel
%ifnarch sparc sparc64
%{!?bcond_off_alsa:BuildRequires:	alsa-lib-devel}
%endif
%{?bcond_on_svgalib:BuildRequires:	svgalib-devel}
%{?bcond_on_aalib:BuildRequires:	aalib-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable,
low level access to a video framebuffer, audio output, mouse, and
keyboard. It can support both windowed and DGA modes of XFree86, and
it is designed to be portable - applications linked with SDL can also
be built on Win32 and BeOS.

%description -l pl
SDL (Simple DirectMedia Layer) jest bibliotek± udostêpniaj±c±
przeno¶ny, niskopoziomowy dostep do bufora ramki video, wyj¶cia audio,
myszy oraz klawiatury, Moze obs³ugiwaæ zarówno okienkowy tryb XFree86
jak i DGA. Konstruuj±c j± miano na uwadze przeno¶no¶æ: aplikacje
konsolidowane z SDL mo¿na równie¿ budowac w systemach Win32 i BeOS.

%package devel
Summary:	SDL - Header files
Summary(pl):	SDL - Pliki nag³ówkowe
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description devel
SDL - Header files.

%description -l pl devel
SDL - Pliki nag³ówkowe.

%package static
Summary:	SDL - static libraries
Summary(pl):	SDL - biblioteki statyczne
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description static
SDL - static libraries.

%description -l pl static
SDL - biblioteki statyczne.

%prep
%setup -q
%patch -p1

%build
%configure \
%ifnarch sparc sparc64
	%{!?bcond_off_alsa:--enable-alsa} \
%endif
	--enable-nasm \
	--enable-pthreads \
	--with-x \
	--enable-video-x11-dga \
	--enable-video-x11-mtrr \
	--enable-video-x11-dgamouse \
	%{!?bcond_off_esound:--enable-esd} \
	%{!?bcond_off_arts:--enable-arts} \
	--disable-alsa \
	%{?bcond_on_svga:--enable-video-svga} \
	%{?bcond_on_aalib:--enable-video-aalib}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf BUGS README WhatsNew

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *gz docs.html docs
%attr(755,root,root) %{_bindir}/sdl-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/libSDLmain.a
%{_includedir}/SDL
%{_aclocaldir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
