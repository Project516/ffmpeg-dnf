%global commit0 %{?_commit0}
%global date %{?_date}
# Default to today if variable is missing (for local testing safety)
%global changelog_date %{?_changelog_date:%{_changelog_date}}%{!?_changelog_date:Mon Jan 01 2000}
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           ffmpeg
Version:        %{date}
Release:        1.git%{shortcommit0}%{?dist}
Summary:        Hyper fast Audio and Video encoder (Git Master)
License:        GPLv3+
URL:            https://ffmpeg.org/
Source0:        ffmpeg-%{commit0}.tar.gz

# Essential Build Tools
BuildRequires:  gcc make git nasm yasm pkgconfig

# Codec Dependencies (Canonical Names)
BuildRequires:  x264-devel x265-devel libvpx-devel
BuildRequires:  lame-devel opus-devel libvorbis-devel libtheora-devel
BuildRequires:  libaom-devel fdk-aac-devel
BuildRequires:  openssl-devel libass-devel freetype-devel zlib-devel bzip2-devel

%description
Weekly git master build of FFmpeg with full codec support.

%prep
%setup -q -n ffmpeg-%{commit0}

%build
# 1. Force -fPIC into standard flags
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
export LDFLAGS="%{?__global_ldflags}"

./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --shlibdir=%{_libdir} \
    --extra-cflags="-fPIC" \
    --enable-gpl \
    --enable-version3 \
    --enable-nonfree \
    --enable-shared \
    --disable-static \
    --disable-debug \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libvpx \
    --enable-libmp3lame \
    --enable-libopus \
    --enable-libvorbis \
    --enable-libtheora \
    --enable-libaom \
    --enable-libfdk-aac \
    --enable-libass \
    --enable-openssl

make -j$(nproc)

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.a' -delete
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/pkgconfig
rm -rf %{buildroot}%{_datadir}/ffmpeg/examples

%files
%{_bindir}/ffmpeg
%{_bindir}/ffprobe
%{_libdir}/*.so.*
%{_datadir}/ffmpeg
%{_mandir}/man1/*

%changelog
* %{changelog_date} Project516 <user@example.com> - %{version}-%{release}
- Automated weekly build with full codecs