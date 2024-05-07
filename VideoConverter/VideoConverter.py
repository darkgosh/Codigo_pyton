import ffmpeg

def convert_mkv_to_mp4(input_file, output_file):
    try:
        stream = ffmpeg.input(input_file)
        stream = ffmpeg.output(stream, output_file, vcodec='libx264', acodec='aac')
        ffmpeg.run(stream)
        print(f"Conversión exitosa: {output_file}")
    except ffmpeg.Error as e:
        print('Error durante la conversión:', e.stderr, e.stdout)

# Ejemplo de uso
input_file = 'video.mkv'
output_file = 'video.mp4'
convert_mkv_to_mp4(input_file, output_file)

