#
# Conditional build:
%bcond_with	aalib		# with aalib graphics support
%bcond_with	caca		# with caca graphics support
%bcond_with	directfb	# with DirectFB graphics support
%bcond_with	ggi		# with GGI graphics support
%bcond_with	nas		# with NAS audio support
%bcond_with	svga		# with svgalib graphics support
%bcond_without	alsa		# without ALSA audio support
%bcond_without	arts		# without aRts audio support
%bcond_without	esd		# without EsounD audio support
%bcond_without	xlibs
#
Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Summary(pl):	SDL (Simple DirectMedia Layer) - Biblioteka do gier/multimediów
Summary(zh_CN):	SDL (Simple DirectMedia Layer) Generic APIs - ÓÎÏ·/¶àÃ½Ìå¿â
Name:		SDL
Version:	1.2.7
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://www.libsdl.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	d29b34b6ba3ed213893fc9d8d35e357a
Patch0:		%{name}-byteorder.patch
Patch1:		%{name}-amfix.patch
Patch2:		%{name}-lpthread.patch
Patch3:		%{name}-no_rpath_in_sdl-config.patch
Patch4:		%{name}-mmx-constraints.patch
Patch5:		%{name}-caca.patch
Patch6:		%{name}-gcc34.patch
URL:		http://www.libsdl.org/
%{?with_directfb:BuildRequires:	DirectFB-devel >= 0.9.15}
BuildRequires:	OpenGL-devel
%if %{with xlibs}
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
%else
BuildRequires:	XFree86-devel >= 4.0.2
%endif
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
%{?with_arts:BuildRequires:	artsc-devel >= 1.1}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_esd:BuildRequires:	esound-devel >= 0.2.8}
%{?with_caca:BuildRequires:	libcaca-devel}
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
Requires:	%{name} = %{version}-%{release}
%if %{with xlibs}
Requires:	libX11-devel
Requires:	libXext-devel
%else
Requires:	XFree86-devel >= 4.0.2
%endif
%{?with_alsa:Requires:	alsa-lib-devel}
%{?with_caca:Requires:	libcaca-devel}
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
Requires:	%{name}-devel = %{version}-%{release}

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
Requires:	%{name}-devel = %{version}-%{release}

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

# get COPY_ARCH_SRC, remove the rest
head -n 20 acinclude.m4 > acinclude.tmp
mv -f acinclude.tmp acinclude.m4

find . -type d -name CVS -print | xargs rm -rf {} \;

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
CPPFLAGS="-DALSA_PCM_OLD_HW_PARAMS_API"
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
	%{?with_caca:--enable-video-caca} \
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
