FROM fedora:43

# 1. Install RPM Fusion Repositories
# This automatically enables them.
RUN dnf -y install --nogpgcheck \
    https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-43.noarch.rpm \
    https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-43.noarch.rpm

# 2. Refresh Metadata
RUN dnf clean all && dnf makecache

# 3. Install Build Tools
RUN dnf -y install \
    git rpm-build rpmdevtools make gcc gcc-c++ tar createrepo_c wget xz nasm yasm \
    openssl-devel zlib-devel bzip2-devel freetype-devel libass-devel

# 4. Install Codecs (Using Canonical Names)
# Note: x264-devel (not libx264) and fdk-aac-devel (not libfdk-aac)
RUN dnf -y install \
    x264-devel x265-devel libvpx-devel lame-devel opus-devel \
    libvorbis-devel libtheora-devel libaom-devel fdk-aac-devel

# 5. Setup Builder
COPY build-script.sh /usr/local/bin/build-script.sh
RUN chmod +x /usr/local/bin/build-script.sh

CMD ["/usr/local/bin/build-script.sh"]