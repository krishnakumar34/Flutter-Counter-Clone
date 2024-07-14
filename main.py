import logging
import youtube_dl

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/hello/<url>')
def hello(url):
    print("hello" +str(url))
    urlk= str(url)
    from pytube import YouTube
    url='https://www.youtube.com/watch?v='+str(urlk)
    yt=YouTube(url)
    return yt.streams.get_highest_resolution().url




@app.route('/einthu/<id>')
def einthu(id):
  
  v=str(id)
  ydl = youtube_dl.YoutubeDL({'outtmpl': 
 '%(id)s.%(ext)s'})
  with ydl:
    result = ydl.extract_info(       'https://einthusan.tv/movie/watch/'+str(v),
        download=False # We just want to extract the info
    )
    if 'entries' in result:
    # Can be a playlist or a list of videos
      video = result['entries'][0]
    else:
    # Just a video
      video = result

    print(video['url'])
    return video['url']

@app.route('/songs/<id>')
def songs(id):
  
  v=str(id)
  t="https://einthusan.tv/movie-clip/watch/music-video/"+str(v)
  print(t)
  ydl = youtube_dl.YoutubeDL({'outtmpl': 
 '%(id)s.%(ext)s'})
  with ydl:
    result = ydl.extract_info(       'https://einthusan.tv/movie-clip/watch/music-video/'+str(v),
        download=False # We just want to extract the info
    )
    if 'entries' in result:
    # Can be a playlist or a list of videos
      video = result['entries'][0]
    else:
    # Just a video
      video = result

    print(video['url'])
    return video['url']


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__app__':
    app.run(host='0.0.0.0', port=8080)  
