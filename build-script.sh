#!/bin/bash
set -e

# 1. Configure CCache to use the mounted volume
export CCACHE_DIR="/ccache_mount"
export CCACHE_MAXSIZE="500M" # Limit cache size
mkdir -p $CCACHE_DIR

# 2. Add ccache to the PATH so it intercepts gcc/g++ calls
# On Fedora, ccache links are in /usr/lib64/ccache
export PATH="/usr/lib64/ccache:$PATH"

echo ">>> CCache Status (Before):"
ccache -s

OUTPUT_DIR="/output"

# Setup directories
rpmdev-setuptree
cp /workspace/ffmpeg-git.spec ~/rpmbuild/SPECS/

# Clone and Pack
echo ">>> Cloning FFmpeg..."
git clone --depth 1 https://git.ffmpeg.org/ffmpeg.git ffmpeg-source
cd ffmpeg-source
COMMIT=$(git rev-parse HEAD)
SHORT_COMMIT=${COMMIT:0:7}
VERSION_DATE=$(date +%Y%m%d)
CHANGELOG_DATE=$(date "+%a %b %d %Y")

cd ..
mv ffmpeg-source ffmpeg-$COMMIT
tar --exclude-vcs -czf ffmpeg-$COMMIT.tar.gz ffmpeg-$COMMIT
mv ffmpeg-$COMMIT.tar.gz ~/rpmbuild/SOURCES/

# Build
echo ">>> Building RPM..."
rpmbuild -bb ~/rpmbuild/SPECS/ffmpeg-git.spec \
  --define "_commit0 $COMMIT" \
  --define "_date $VERSION_DATE" \
  --define "_changelog_date $CHANGELOG_DATE"

# Output
cp ~/rpmbuild/RPMS/x86_64/*.rpm $OUTPUT_DIR/
echo ">>> Success!"

echo ">>> CCache Status (After):"
ccache -s