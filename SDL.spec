#
# Conditional build:
%bcond_with	aalib		# with aalib graphics support
%bcond_with	directfb	# with DirectFB graphics support
%bcond_with	ggi		# with GGI graphics support
%bcond_with	nas		# with NAS audio support
%bcond_with	svga		# with svgalib graphics support
%bcond_without	alsa		# without ALSA audio support
%bcond_without	arts		# without aRts audio support
%bcond_without	esd		# without EsounD audio support

Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Summary(es):	Simple DirectMedia Layer
Summary(pl):	SDL (Simple DirectMedia Layer) - Biblioteka do gier/multimediów
Summary(pt_BR):	Simple DirectMedia Layer
Summary(ru):	Simple DirectMedia Layer
Summary(uk):	Simple DirectMedia Layer
Summary(zh_CN):	SDL (Simple DirectMedia Layer) Generic APIs - ÓÎÏ·/¶àÃ½Ìå¿â
Name:		SDL
Version:	1.2.6
Release:	3
License:	LGPL
Group:		X11/Libraries
Source0:	http://www.libsdl.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	9011f147f23ec535515291d0c9c6904c
Patch0:		%{name}-byteorder.patch
Patch1:		%{name}-fixlibs.patch
Patch2:		%{name}-amfix.patch
Patch3:		%{name}-lpthread.patch
Patch4:		%{name}-no_rpath_in_sdl-config.patch
Patch5:		%{name}-lt15.patch
Patch6:		%{name}-dlopen-acfix.patch
Patch7:		%{name}-mmx-constraints.patch
URL:		http://www.libsdl.org/
%{?with_directfb:BuildRequires:	DirectFB-devel >= 0.9.15}
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel >= 4.0.2
%{?with_aalib:BuildRequires:	aalib-devel}
%ifnarch sparc sparc64
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
%endif
%{?with_arts:BuildRequires:	arts-devel >= 1.1}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_esd:BuildRequires:	esound-devel >= 0.2.8}
%{?with_ggi:BuildRequires:	libggi-devel}
BuildRequires:	libtool >= 2:1.4d
%{?with_nas:BuildRequires:	nas-devel}
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	perl-modules
%{?with_directfb:BuildRequires:	pkgconfig >= 0.7}
%{?with_svgalib:BuildRequires:	svgalib-devel >= 1.4.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable,
low level access to a video framebuffer, audio output, mouse, and
keyboard. It can support both windowed and DGA modes of XFree86, and
it is designed to be portable - applications linked with SDL can also
be built on Win32 and BeOS.

%description -l pl
SDL (Simple DirectMedia Layer) jest bibliotek± udostêpniaj±c±
przeno¶ny, niskopoziomowy dostêp do bufora ramki video, wyj¶cia audio,
myszy oraz klawiatury. Mo¿e obs³ugiwaæ zarówno okienkowy tryb XFree86
jak i DGA. Konstruuj±c j± miano na uwadze przeno¶no¶æ: aplikacje
konsolidowane z SDL mo¿na równie¿ budowaæ w systemach Win32 i BeOS.

%description -l pt_BR
Esse é o Simple DirectMedia Layer, uma API genérica que dá acesso de
baixo nível a áudio, teclado, mouse e vídeo em várias plataformas.

Essa biblioteca é usada por alguns jogos.

%package devel
Summary:	SDL - Header files
Summary(pl):	SDL - Pliki nag³ówkowe
Summary(pt_BR):	Bibliotecas e arquivos de cabeçalho para aplicações SDL
Summary(ru):	æÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ, ÉÓÐÏÌØÚÕÀÝÉÈ SDL
Summary(uk):	æÁÊÌÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ SDL
Summary(zh_CN):	SDL (Simple DirectMedia Layer) ¿ª·¢¿â
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	XFree86-devel >= 4.0.2
%ifnarch sparc sparc64
%{?with_alsa:Requires:	alsa-lib-devel}
%endif
%{?with_nas:Requires:	nas-devel}

%description devel
SDL - Header files.

%description devel -l pl
SDL - Pliki nag³ówkowe.

%description devel -l pt_BR
Esse pacote contém bibliotecas, arquivos de cabeçalho e outros
recursos para o desenvolvimento de aplicativos com SDL.

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÆÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ,
ÉÓÐÏÌØÚÕÀÝÉÈ SDL.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÆÁÊÌÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ
×ÉËÏÒÉÓÔÏ×ÕÀÔØ SDL.

%package static
Summary:	SDL - static libraries
Summary(pl):	SDL - biblioteki statyczne
Summary(pt_BR):	Biblioteca estática para desenvolvimento de aplicações com a SDL
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ SDL
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ SDL
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
SDL - static libraries.

%description static -l pl
SDL - biblioteki statyczne.

%description static -l pt_BR
Biblioteca estática para desenvolvimento de aplicações com a SDL.

%description static -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÓÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ,
ÉÓÐÏÌØÚÕÀÝÉÈ SDL.

%description static -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÓÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ
×ÉËÏÒÉÓÔÏ×ÕÀÔØ SDL.

%package examples
Summary:	SDL - example programs
Summary(pl):	SDL - programy przyk³adowe
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description examples
SDL - example programs.

%description examples -l pl
SDL - przyk³adowe programy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# get COPY_ARCH_SRC, remove the rest
head -n 16 acinclude.m4 > acinclude.tmp
mv -f acinclude.tmp acinclude.m4

find . -type d -name CVS -print | xargs rm -rf {} \;

%build
rm -f missing libtool
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
%ifarch %{ix86}
	--enable-nasm \
%else
	--disable-nasm \
%endif
	--enable-pthreads \
	--enable-pthread-sem \
	--with-x \
	--enable-dga \
	%{?with_aalib:--enable-video-aalib} \
	--enable-video-dga \
	%{?with_directfb:--enable-video-directfb} \
	--enable-video-fbcon \
	%{?with_ggi:--enable-video-ggi} \
	--enable-video-opengl \
	%{?with_svga:--enable-video-svga} \
	--enable-video-x11-dgamouse \
	--enable-video-x11-vm \
	--enable-video-x11-xv \
	%{!?with_alsa:--disable-alsa} \
	%{!?with_arts:--disable-arts} \
	%{!?with_esd:--disable-esd} \
	%{!?with_nas:--disable-nas}

# automake chooses to use CXXLINK because of seen unused C++ sources
# (which are for BeOS and MacOS+QTopia, not Linux)
%{__make} \
	CXXLINK="\$(LINK)"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -rf docs/man3 docs/{Makefile*,.cvsignore} docs/html/{Makefile*,.cvsignore}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS CREDITS README TODO WhatsNew
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs.html docs
%attr(755,root,root) %{_bindir}/sdl-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/libSDLmain.a
%{_includedir}/SDL
%{_aclocaldir}/*
%{_mandir}/man3/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL.a
