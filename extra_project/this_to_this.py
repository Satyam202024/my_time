import moviepy.editor as moviepy


clip = moviepy.VideoFileClip('input_video.avi')
clip.write_videofile('myvideo/mp4')
    