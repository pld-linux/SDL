Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Name:		SDL
Version:	0.9.13
Release:	1
Group:		X11/Libraries
Copyright:	LGPL
Source:		http://www.devolution.com/~slouken/projects/SDL/SDL-0.9/src/%{name}-%{version}.tar.gz
URL:		http://www.devolution.com/~slouken/projects/SDL/
BuildPrereq:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable, low
level access to a video framebuffer, audio output, mouse, and keyboard. It
can support both windowed and DGA modes of XFree86, and it is designed to be
portable - applications linked with SDL can also be built on Win32 and BeOS.

%package devel
Summary:	SDL - Header files
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description devel
SDL - Header files.

%package static
Summary:	SDL - static libraries
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description static
SDL - static libraries.

%prep
%setup -q
%build
make config <<EOF

EOF
make DEBUG="$RPM_OPT_FLAGS -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/SDL}

install lib/lib{*.a,*.so.*.*.*} $RPM_BUILD_ROOT%{_libdir}
ln -sf libSDLx11.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libSDLx11.so
install include/* $RPM_BUILD_ROOT%{_includedir}/SDL

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README TODO WhatsNew docs.html
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/SDL

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
