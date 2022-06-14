import ffmpeg

import subprocess

def get_output(in_filename: str) -> str:
    try:
        return "/".join(in_filename.split('/')[:-1]) + '/Image'
    except:
        return 'Image'

def extract_certain_scene(in_filename: str, out_filename:str) -> None:
    probe = ffmpeg.probe(in_filename)
    vid_len = float(probe['streams'][0]['duration'])
    # 9 / 15 because personally i like it more than 2 / 3
    time = 0 if vid_len - (vid_len * 9 / 15) <= 9 else vid_len * 9 / 15
    output = get_output(in_filename=in_filename)
    (
        ffmpeg
        .input(in_filename, ss=time)
        .filter('scale', 600, -1)
        .filter('fps', fps='6', round='up')
        .trim(start_frame=0, end_frame=60)
        .output(f'{output}%02d.jpg', start_number=0) # change this
        .overwrite_output()
        .run(quiet=True)
    )

def gifify_certain_scene(in_filename: str, out_filename: str) -> None:
    output = get_output(in_filename=in_filename)

    subprocess.run(f'convert -delay 10 -loop 0 {output}*.jpg {out_filename}', shell=True) # change this
    subprocess.run(f'rm -rf {output}*.jpg', shell=True)

def generate_thumbnail(in_filename: str, out_filename: str) -> None:
    extract_certain_scene(in_filename=in_filename, out_filename=out_filename)

    gifify_certain_scene(in_filename=str, out_filename=out_filename)
    

def extract_images(in_filename: str) -> None:
    probe = ffmpeg.probe(in_filename)
    vid_len = float(probe['streams'][0]['duration'])
    # width = probe['streams'][0]['width']    # Set how many spots you want to extract a video from. 
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
            .run(quiet=True)
        )
        i += 1

def extract_and_gifify(in_filename: str, out_filename: str) -> None:
    extract_images(in_filename=in_filename)

    subprocess.system(f'convert -delay 60 -loop 0 Image*.jpg {out_filename}', shell=True)
    subprocess.system(f'rm -rf Image*.jpg', shell=True)