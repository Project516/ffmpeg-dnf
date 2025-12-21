%global _binary_payload w9.xzdio

%global date %{?_date}
%global changelog_date %{?_changelog_date}

Name:           ffmpeg
Version:        %{date}
Release:        1%{?dist}
Summary:        FFmpeg (Static Build by BtbN)
License:        GPLv3
URL:            https://github.com/BtbN/FFmpeg-Builds
Source0:        ffmpeg-master-latest-linux64-gpl.tar.xz

# Conflicts and Provides
Conflicts:      ffmpeg-free
Provides:       ffmpeg = %{version}

# Disable debug packages
%global debug_package %{nil}

%description
A static build of FFmpeg master, repackaged from BtbN auto-builds.
Includes: ffmpeg, ffprobe.

%prep
%setup -q -n ffmpeg-master-latest-linux64-gpl

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_bindir}

# 1. Install binaries (Copies them AND sets permissions to 755)
install -m 755 bin/ffmpeg %{buildroot}%{_bindir}/ffmpeg
install -m 755 bin/ffprobe %{buildroot}%{_bindir}/ffprobe

# 2. AGGRESSIVE STRIP
# Modify the installed files in-place to remove symbols
strip --strip-all %{buildroot}%{_bindir}/ffmpeg
strip --strip-all %{buildroot}%{_bindir}/ffprobe

%files
%{_bindir}/ffmpeg
%{_bindir}/ffprobe

%changelog
* %{changelog_date} project516 - %{version}-1
- Repackaged upstream binary