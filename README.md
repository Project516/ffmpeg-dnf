# ffmpeg-dnf
 
```bash
sudo docker build --no-cache -t ffmpeg-builder .

sudo docker run --rm \
  -v "$(pwd):/workspace:z" \
  -v "$(pwd)/artifacts:/output:z" \
  ffmpeg-builder
  ```