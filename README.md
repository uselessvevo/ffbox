# Cloudyff - ffmpeg wrapper

> **Note**: `cloudyff` in deep development

Basic example - read file and close it

```py
stream = Stream()
stream.input("audio.mp3")
probe_result = stream.probe(output_format=OutoutFormats.JSON)
stream.close()
```

As context manager

```py
with Stream(async_run=True) as stream:
    stream.input("audio.mp3")
    probe_result = stream.probe(output_format=OutputFormats.JSON)
```

Concat two files

```py
# Setup `Stream` instance with the next arguments:
# * async_run - run is separate processes
# * temp - copy files into temporary directory to prevent file corruption and loses
# * validate - use validators
#   if `validate` is True then it will validate all input files by ffprobe and filters
stream = Stream(async_run=True, temp=True, validate=True)

# Load video file
stream.input("silent video.mp4")

# Will move this after new input
stream.filter(fps_method, fps=60)

# Also you can pass raw string as ffmpeg filter. Thanks to python-ffmpeg repo it's cool
stream.filter("fps", fps=60)

stream.output("almost smooth video.mp4")

# Set video resolution
stream.filter(set_resolution, w=640, h=480)

# Will create new instance of `Node`
# Will not use `guess_format` method
# Will set stream segments to 0, because of the format type
# Will add "myaudio" key to `files_mapping`
stream.input("audio.mp3", name="myaudio", file_format="mp3")

# For example, you can use 
# `name/tag` to get query string and analyze it

# Will use concat filter
# Will use validator to check if it can be concatinated
# Use: ffprobe -show_streams -print_format json input.mov
stream.concat("video.mp4")

# If `output` was not called than 
# uuid4 will be added to the file's name
stream.output("video with the sound.mp4")

# Run ffmpeg
stream.run()
```

Convert from one to another file format

```py
# You can provide your own convert string
stream = Stream(async_run=True)
stream.input("video.mp4")

# Will raise exception if validation will fail
# For example, it could be `ConverterNotFound` or `UnkownRateError/NotApplicableRateError`
stream.convert("mp3", rate="128kb/s", raise_exception=True/False)

# Or just use `quality` argument
# Will raise `UknownQualityError` if it was passed as a raw data type
stream.convert("mp3", quality=Quality.HIGH, raise_exception=True/False)

# Or use your own filter
# Will ignore other arguments except `raise_exception`
stream.convert(raw="...", raise_exception=True/False)

# Optional method call
# method `convert` will name this file "video.mp3"
stream.output("output audio.mp3")

# Run ffmpeg
stream.run()
```

Raw/uncontrolled run

```py
stream = Stream()
stream.input("video.mp4")
stream.raw("...", raise_exception=True/False)
stream.run()
```
