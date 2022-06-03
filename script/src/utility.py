import ffmpeg

import os

def generate_thumbnail(in_filename: str, out_filename: str) -> None:
    probe = ffmpeg.probe(in_filename)
    vid_len = float(probe['streams'][0]['duration'])
    # 9 / 15 because personally i like it more than 2 / 3
    time = 0 if vid_len - (vid_len * 9 / 15) <= 9 else vid_len * 9 / 15
    (
        ffmpeg
        .input(in_filename, ss=time)
        # resize to width 600
        .filter('scale', 600, -1)
        # get 10 s of video with 6 fps 
        .filter('fps', fps=6, round='up')
        .output(out_filename, vframes=60, loop=0) # 6 fps * 10 s = 60 frames
        .overwrite_output()
        .run(capture_stdout=True, capture_stderr=True)
    )

def extract_images(in_filename: str, out_filename: str) -> None:
    probe = ffmpeg.probe(in_filename)
    vid_len = float(probe['streams'][0]['duration'])
    # width = probe['streams'][0]['width']
    # Set how many spots you want to extract a video from. 
    parts = int(vid_len) if vid_len < 20 else 20

    intervals = int(vid_len // parts)
    interval_list = [(i * intervals, (i + 1) * intervals) for i in range(parts)]
    i = 0
    for item in interval_list:
        (
            ffmpeg
            .input(in_filename, ss=item[1])
            .filter('scale', 600, -1)
            .output(f'Image{i:02d}.jpg', vframes=1)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        i += 1

def extract_and_gifify(in_filename: str, out_filename: str) -> None:
    extract_images(in_filename=in_filename, out_filename='Image')

    os.system(f'convert -delay 60 -loop 0 Image*.jpg {out_filename}')
    os.system(f'rm -rf Image*.jpg')