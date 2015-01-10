Name:           libass
Version:        0.12.1
Release:        0
Summary:        Portable library for SSA/ASS subtitles rendering

Group:          Multimedia/Libraries
License:        ISC
URL:            https://github.com/libass
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  fontconfig-devel
BuildRequires:  fribidi-devel
BuildRequires:  libpng-devel

%description
Libass is a portable library for SSA/ASS subtitles rendering.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
autoreconf -fiv

%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc Changelog
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libass.pc
