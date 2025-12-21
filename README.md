# ffmpeg-dnf

Custom Fedora repository that auto-builds RPMs from the latest FFmpeg `master` on a weekly schedule.

## Install the repository

1. Drop the repo file into dnf/yum config:
	```bash
	sudo curl -L https://raw.githubusercontent.com/project516/ffmpeg-dnf/main/ffmpeg-dnf.repo \
	  -o /etc/yum.repos.d/ffmpeg-dnf.repo
	```
2. Refresh metadata:
	```bash
	sudo dnf clean all
	sudo dnf makecache
	```
3. Install FFmpeg from the repo (common packages):
	```bash
	sudo dnf install ffmpeg
	```

## Updating

- Weekly builds track upstream `master`. Pull updates as usual:
  ```bash
  sudo dnf upgrade --refresh
  ```

## Removing the repo

```bash
sudo rm /etc/yum.repos.d/ffmpeg-dnf.repo
sudo dnf clean all
# Optionally reinstall Fedora/RPM Fusion FFmpeg
sudo dnf install ffmpeg --enablerepo=fedora,updates --disablerepo=ffmpeg-dnf
```
