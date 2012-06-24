#
# Conditional build:
# _with_aalib - with aalib support
# _with_ggi - with GGI support
# _with_nas - with NAS audio support
# _with_svga - with svgalib support
#
# _without_alsa - without ALSA support
# _without_arts - without arts support
# _without_esound - without esound support
#
%ifarch	alpha
%define _without_arts 1
%endif

Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Summary(es):	Simple DirectMedia Layer
Summary(pl):	SDL (Simple DirectMedia Layer) - Biblioteka do gier/multimedi�w
Summary(pt_BR):	Simple DirectMedia Layer
Summary(ru):	Simple DirectMedia Layer
Summary(uk):	Simple DirectMedia Layer
Summary(zh_CN):	SDL (Simple DirectMedia Layer) Generic APIs - ��Ϸ/��ý���
Name:		SDL
Version:	1.2.5
Release:	4
License:	LGPL
Group:		X11/Libraries
Source0:	http://www.libsdl.org/release/%{name}-%{version}.tar.gz
Patch0:		%{name}-byteorder.patch
Patch1:		%{name}-fixlibs.patch
Patch2:		%{name}-amfix.patch
Patch3:		%{name}-lpthread.patch
Patch4:		%{name}-ac25x.patch
Patch5:		%{name}-no_rpath_in_sdl-config.patch
Patch6:		%{name}-noobjc.patch
Patch7:		%{name}-refresh_rates.patch
Patch8:		%{name}-am17.patch
URL:		http://www.libsdl.org/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel >= 4.0.2
%{?_with_aalib:BuildRequires:	aalib-devel}
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
%{!?_without_arts:BuildRequires:	arts-devel >= 1.1}
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_esound:BuildRequires:	esound-devel}
%{?_with_ggi:BuildRequires:	libggi-devel}
BuildRequires:	libtool
%{?_with_nas:BuildRequires:	nas-devel}
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	perl-modules
%{?_with_svgalib:BuildRequires:	svgalib-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable,
low level access to a video framebuffer, audio output, mouse, and
keyboard. It can support both windowed and DGA modes of XFree86, and
it is designed to be portable - applications linked with SDL can also
be built on Win32 and BeOS.

%description -l pl
SDL (Simple DirectMedia Layer) jest bibliotek� udost�pniaj�c�
przeno�ny, niskopoziomowy dost�p do bufora ramki video, wyj�cia audio,
myszy oraz klawiatury. Mo�e obs�ugiwa� zar�wno okienkowy tryb XFree86
jak i DGA. Konstruuj�c j� miano na uwadze przeno�no��: aplikacje
konsolidowane z SDL mo�na r�wnie� budowa� w systemach Win32 i BeOS.

%description -l pt_BR
Esse � o Simple DirectMedia Layer, uma API gen�rica que d� acesso de
baixo n�vel a �udio, teclado, mouse e v�deo em v�rias plataformas.

Essa biblioteca � usada por alguns jogos.

%package devel
Summary:	SDL - Header files
Summary(pl):	SDL - Pliki nag��wkowe
Summary(pt_BR):	Bibliotecas e arquivos de cabe�alho para aplica��es SDL
Summary(ru):	�����, ����������� ��� ���������� ��������, ������������ SDL
Summary(uk):	�����, ����Ȧ�Φ ��� �������� �������, �� �������������� SDL
Summary(zh_CN):	SDL (Simple DirectMedia Layer) ������
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	XFree86-devel >= 4.0.2
%ifnarch sparc sparc64
%{!?_without_alsa:Requires:	alsa-lib-devel}
%endif
%{!?_without_arts:Requires:	arts-devel}
%{!?_without_esound:Requires:	esound-devel}
%{?_with_nas:Requires:	nas-devel}

%description devel
SDL - Header files.

%description devel -l pl
SDL - Pliki nag��wkowe.

%description devel -l pt_BR
Esse pacote cont�m bibliotecas, arquivos de cabe�alho e outros
recursos para o desenvolvimento de aplicativos com SDL.

%description devel -l ru
���� ����� �������� �����, ����������� ��� ���������� ��������,
������������ SDL.

%description devel -l uk
��� ����� ͦ����� �����, ����Ȧ�Φ ��� �������� �������, ��
�������������� SDL.

%package static
Summary:	SDL - static libraries
Summary(pl):	SDL - biblioteki statyczne
Summary(pt_BR):	Biblioteca est�tica para desenvolvimento de aplica��es com a SDL
Summary(ru):	����������� ���������� ��� ���������� � �������������� SDL
Summary(uk):	������Φ ¦�̦����� ��� �������� � ������������� SDL
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
SDL - static libraries.

%description static -l pl
SDL - biblioteki statyczne.

%description static -l pt_BR
Biblioteca est�tica para desenvolvimento de aplica��es com a SDL.

%description static -l ru
���� ����� �������� ����������� ���������� ��� ���������� ��������,
������������ SDL.

%description static -l uk
��� ����� ͦ����� ������Φ ¦�̦����� ��� �������� �������, ��
�������������� SDL.

%package examples
Summary:	SDL - example programs
Summary(pl):	SDL - programy przyk�adowe
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description examples
SDL - example programs.

%description examples -l pl
SDL - przyk�adowe programy.

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
%patch8 -p1

%build
rm -f missing libtool
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
SED=sed ; export SED
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
	--enable-video-dga \
	--disable-video-directfb \
	--enable-video-x11-dgamouse \
	--enable-video-x11-vm \
	--enable-video-x11-xv \
	--enable-video-opengl \
	--enable-video-fbcon \
	%{?_with_aalib:--enable-video-aalib} \
	%{?_with_ggi:--enable-video-ggi} \
	%{!?_with_nas:--disable-nas} \
	%{?_with_svga:--enable-video-svga} \
%ifnarch sparc sparc64
	%{!?_without_alsa:--enable-alsa} \
%endif
	%{!?_without_esound:--enable-esd} \
	%{!?_without_arts:--enable-arts}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

SED=sed ; export SED
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -rf docs/man3 docs/Makefile* docs/html/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc BUGS CREDITS README TODO WhatsNew docs.html docs
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
