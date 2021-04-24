import moviepy.editor as mp

clip = mp.VideoFileClip('./greenscreen.mp4')
# Mountains background
background = mp.ImageClip('https://www.worldatlas.com/r/w728-h425-c728x425/upload/66/14/d8/kangchenjunga.jpg')

masked_clip = clip.fx(mp.vfx.mask_color, color=[0, 255, 8], thr=100, s=5)
# You can remove this resize, it's just for test...
masked_clip = masked_clip.resize(0.3).set_pos(('center', 'bottom'))

final_clip = mp.CompositeVideoClip([
    background,
    masked_clip
]).set_duration(1)

final_clip.write_videofile('test.mp4')