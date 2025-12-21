%global date %{?_date}

Name:           ffmpeg
Version:        %{date}
Release:        1%{?dist}
Summary:        FFmpeg (Static Build by BtbN)
License:        GPLv3
URL:            https://github.com/BtbN/FFmpeg-Builds
Source0:        ffmpeg-master-latest-linux64-gpl.tar.xz

# We provide ffmpeg, but we conflict with the official packages
# so we don't accidentally break system dependencies.
Conflicts:      ffmpeg-free
Provides:       ffmpeg = %{version}

# No debug info needed for static builds
%global debug_package %{nil}

%description
A static build of FFmpeg master, repackaged from BtbN auto-builds.
Includes: ffmpeg, ffprobe.

%prep
# The BtbN tarball usually unpacks to a directory named like the tarball
# We use -n to match the folder inside the tarball
%setup -q -n ffmpeg-master-latest-linux64-gpl

%build
# Nothing to build!

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 bin/ffmpeg %{buildroot}%{_bindir}/ffmpeg
install -m 755 bin/ffprobe %{buildroot}%{_bindir}/ffprobe

# Install manpages if they exist in the tarball
mkdir -p %{buildroot}%{_mandir}/man1
if [ -d doc ]; then
    cp doc/*.1 %{buildroot}%{_mandir}/man1/ || true
fi

%files
%{_bindir}/ffmpeg
%{_bindir}/ffprobe
%{_mandir}/man1/*

%changelog
* %{date} Project516 - %{version}-1
- Repackaged upstream binary