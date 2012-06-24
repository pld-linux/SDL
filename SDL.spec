#
# Conditional build:
# _without_alsa - without ALSA support
# _without_esound - without esound support
# _without_arts - without arts support
# _with_svga - with svgalib support
# _with_aalib - with aalib support
# _with_ggi - with GGI support
#
%ifarch	alpha
%define _without_arts 1
%endif

Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Summary(pl):	SDL (Simple DirectMedia Layer) - Biblioteka do gier/multimedi�w
Name:		SDL
Version:	1.2.2
Release:	3
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Source0:	http://www.libsdl.org/release/%{name}-%{version}.tar.gz
Patch0:		%{name}-byteorder.patch
Patch1:		%{name}-fixlibs.patch
URL:		http://www.libsdl.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_esound:BuildRequires:	esound-devel}
%{!?_without_arts:BuildRequires:	arts-devel}
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	XFree86-devel >= 4.0.2
BuildRequires:	OpenGL-devel
BuildRequires:	perl-modules
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
%{?_with_svgalib:BuildRequires:	svgalib-devel}
%{?_with_aalib:BuildRequires:	aalib-devel}
%{?_with_ggi:BuildRequires:	libggi-devel}
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
SDL (Simple DirectMedia Layer) jest bibliotek� udost�pniaj�c�
przeno�ny, niskopoziomowy dostep do bufora ramki video, wyj�cia audio,
myszy oraz klawiatury, Moze obs�ugiwa� zar�wno okienkowy tryb XFree86
jak i DGA. Konstruuj�c j� miano na uwadze przeno�no��: aplikacje
konsolidowane z SDL mo�na r�wnie� budowac w systemach Win32 i BeOS.

%package devel
Summary:	SDL - Header files
Summary(pl):	SDL - Pliki nag��wkowe
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}
%{!?_without_esound:Requires:	esound-devel}
%{!?_without_arts:Requires:	arts-devel}

%description devel
SDL - Header files.

%description -l pl devel
SDL - Pliki nag��wkowe.

%package static
Summary:	SDL - static libraries
Summary(pl):	SDL - biblioteki statyczne
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description static
SDL - static libraries.

%description -l pl static
SDL - biblioteki statyczne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf
automake -a -c
%configure \
%ifnarch sparc sparc64
	%{!?_without_alsa:--enable-alsa} \
%endif
	--enable-nasm \
	--enable-pthreads \
	--enable-pthread-sem \
	--with-x \
	--enable-video-x11-vm \
	--enable-video-x11-dga \
	--enable-video-x11-mtrr \
	--enable-video-x11-dgamouse \
	--enable-video-opengl \
	%{!?_without_esound:--enable-esd} \
	%{!?_without_arts:--enable-arts} \
	%{?_with_svga:--enable-video-svga} \
	%{?_with_aalib:--enable-video-aalib} \
	%{?_with_ggi:--enable-video-ggi}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

rm -rf docs/man3 docs/Makefile* docs/html/Makefile*

gzip -9nf BUGS CREDITS README TODO WhatsNew

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {BUGS,CREDITS,README,TODO,WhatsNew}.gz docs.html docs
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
