COMMAND_360 = \
"-vf scale=w=640:h=360:force_original_aspect_ratio=decrease -c:a aac -ar 48000 -c:v h264 -profile:v main -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -hls_time 4 -hls_playlist_type vod  -b:v 800k -maxrate 856k -bufsize 1200k -b:a 128k -hls_segment_filename {foldername}/360p_%03d.ts {foldername}/360p.m3u8"

COMMAND_480 = \
"-vf scale=w=842:h=480:force_original_aspect_ratio=decrease -c:a aac -ar 48000 -c:v h264 -profile:v main -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -hls_time 4 -hls_playlist_type vod -b:v 1400k -maxrate 1498k -bufsize 2100k -b:a 128k -hls_segment_filename {foldername}/480p_%03d.ts {foldername}/480p.m3u8"

COMMAND_720 = \
"-vf scale=w=1280:h=720:force_original_aspect_ratio=decrease -c:a aac -ar 48000 -c:v h264 -profile:v main -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -hls_time 4 -hls_playlist_type vod -b:v 2800k -maxrate 2996k -bufsize 4200k -b:a 128k -hls_segment_filename {foldername}/720p_%03d.ts {foldername}/720p.m3u8"

COMMAND_1080 = \
"-vf scale=w=1920:h=1080:force_original_aspect_ratio=decrease -c:a aac -ar 48000 -c:v h264 -profile:v main -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -hls_time 4 -hls_playlist_type vod -b:v 5000k -maxrate 5350k -bufsize 7500k -b:a 192k -hls_segment_filename {foldername}/1080p_%03d.ts {foldername}/1080p.m3u8"


COMMANDS = {
    "360p": COMMAND_360,
    "480p": COMMAND_480,
    "720p": COMMAND_720,
    "1080p": COMMAND_1080
}


MANIFEST_ENTRY_360 = \
"#EXT-X-STREAM-INF:BANDWIDTH=800000,RESOLUTION=640x360\n360p.m3u8"

MANIFEST_ENTRY_480 = \
"#EXT-X-STREAM-INF:BANDWIDTH=1400000,RESOLUTION=842x480\n480p.m3u8"

MANIFEST_ENTRY_720 = \
"#EXT-X-STREAM-INF:BANDWIDTH=2800000,RESOLUTION=1280x720\n720p.m3u8"

MANIFEST_ENTRY_1080 = \
"#EXT-X-STREAM-INF:BANDWIDTH=5000000,RESOLUTION=1920x1080\n1080p.m3u8"

MANIFEST_ENTRIES = {
    "360p": MANIFEST_ENTRY_360,
    "480p": MANIFEST_ENTRY_480,
    "720p": MANIFEST_ENTRY_720,
    "1080p": MANIFEST_ENTRY_1080
}
