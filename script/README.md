### How to Run
```
docker build -t image_name .
```
```
docker run -v /path/to/video/:/app/resources image_name generate_thumbnail input_file output_file.gif -rm
```

### Options
- `generate_thumbnail`: If the video is long enough, then jumps to the 9/15th timestamp of the video and generate a GIF thumbnail with frames in the next 10 seconds, otherwise, choose the first 10 seconds if the video isn't long enough
- `extract_and_gifify`: Get 10 frames (given the video is long enough) from 10 different timestamps and generate a GIF thumbnail with those frames