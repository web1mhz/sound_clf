# 출처 : https://towardsdatascience.com/audio-classification-with-pre-trained-vgg-19-keras-bca55c2a0efe


from __future__ import unicode_literals
import youtube_dl


# https://www.youtube.com/watch?v=eN6GDqWnQFg 팔색조
# https://www.youtube.com/watch?v=pS1ofc3yLn0 렛잇비
# https://www.youtube.com/watch?v=CN4fffh7gmk 다이너마이트
# https://www.youtube.com/watch?v=dyRsYk0LyA8 블랙핑크
# for bike sounds : https://www.youtube.com/watch?v=sRdRwHPjJPk
# for car sounds : https://www.youtube.com/watch?v=PPdNb-XQXR8
# https://www.youtube.com/watch?v=6-szbJtedw4 눈누누나

url = ["https://www.youtube.com/watch?v=2TVqynlKEkg"]

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url) # 유투브 주소는 리스트형태로 입력해야함


