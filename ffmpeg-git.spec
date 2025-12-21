%global commit0 %{?_commit0}
%global date %{?_date}
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Allow building master snapshots efficiently
Name:           ffmpeg
Version:        %{date}
Release:        1.git%{shortcommit0}%{?dist}
Summary:        Hyper fast Audio and Video encoder (Git Master)
License:        GPLv3+
URL:            https://ffmpeg.org/

# The Action will generate this source file dynamically
Source0:        ffmpeg-%{commit0}.tar.gz

BuildRequires:  gcc make git nasm yasm
BuildRequires:  libx264-devel x265-devel libvpx-devel
BuildRequires:  lame-devel opus-devel openssl-devel
BuildRequires:  libass-devel freetype-devel zlib-devel bzip2-devel

%description
Weekly git master build of FFmpeg.

%prep
%setup -q -n ffmpeg-%{commit0}

%build
./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --shlibdir=%{_libdir} \
    --enable-gpl \
    --enable-version3 \
    --enable-shared \
    --disable-static \
    --disable-debug \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libvpx \
    --enable-libmp3lame \
    --enable-libopus \
    --enable-libass \
    --enable-openssl \
    --enable-nonfree

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
# Remove exclude static libs/headers if you want a cleaner package
find %{buildroot} -name '*.a' -delete
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/pkgconfig
rm -rf %{buildroot}%{_datadir}/ffmpeg/examples

%files
%{_bindir}/ffmpeg
%{_bindir}/ffprobe
# %{_bindir}/ffplay # Requires SDL2
%{_libdir}/*.so.*
%{_datadir}/ffmpeg
%{_mandir}/man1/*

%changelog
* %{date} Project516 <project516.progress139@slmail.me> - %{version}-%{release}
- Automated weekly build