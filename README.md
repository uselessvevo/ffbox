# Cloudyff - ffmpeg wrapper

> **Note**: `cloudyff` in deep development

Basic example - read file and get info

```py
# Create `Stream` instance
stream = Stream()

# Load audio file
stream.input("audio.mp3")

# Get file info
probe_result = stream.probe(output_format=OutputFormats.JSON)

# Print it
pprint.pprint(probe_result)
```

Exclude/include file formats

```py
stream = Stream()

# Pass list of file formats to exclude them
stream.exclude_formats("avi", "flv")

# Or include/allow only

stream.allow_formats("avi", "flv")

```

Load files from directory by pattern

```py
stream = Stream()

# Load mp3 files only
stream.input(pattern="*.mp3", directory="My Music")

# Or use `patterns`

stream.input(patterns=("*.mp3", "*.avi"), directory="My Music")

# Load everything, but it will take more time

stream.input(pattern="*.*", directory="My Music")

# All next operations will be applied for each file

stream.filter("filter_method", ...)

# Run ffmpeg
stream.run()
```

Change file metadata

```py
stream = Stream()

# Load audio file
stream.input("input.mp3")

# Set file's metadata
stream.set_metadata("input.mp3", metadata={...})

# If `overwrite` is `True` output file will be overwritten
# Unless, you need to set new filename
stream.output("output.mp3", overwrite=True/False)

# Run ffmpeg
stream.run()
```

Concat two files

```py
stream = Stream()

# Load video file
stream.input("silent movie.mp4")

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

# Set output filename
stream.output("noisy movie.mp4")

# Run ffmpeg
stream.run()
```

Additional parameters

```py
# Setup `Stream` instance with the next arguments:
# * async_run - run is separate processes
# * temp - copy files into temporary directory to prevent file corruption and loses
# * validate - use validators
#   if `validate` is True then it will validate all input files by ffprobe and filters
stream = Stream(async_run=True, temp=True, validate=True)

# Load video
stream.input("input.mp4")

# Will move this after new input
stream.filter(fps_method, fps=60)

# Also you can pass raw string as ffmpeg filter. Thanks to python-ffmpeg repo it's cool
stream.filter("fps", fps=60)

# Set output filename
stream.output("smooth video.mp4")

# Run ffmpeg
stream.run()
```

Convert from one to another file format

```py
stream = Stream()

# Load video
stream.input("video.mp4")

# Will raise exception if validation will fail
# Will use libmp3lame
# For example, it could be `ConverterNotFound` or `UnkownRateError/NotApplicableRateError`
stream.convert("mp3", bitrate="128k", raise_exception=True/False)

# Or just use `quality` argument
# Will raise `UknownQualityError` if it was passed as a raw data type
stream.convert("mp3", quality=Quality.HIGH, raise_exception=True/False)

# Or use your own filter
# Will ignore other arguments except `raise_exception`
stream.convert(raw="...", raise_exception=True/False)

# Set output filename
stream.output("output audio.mp3")

# Run ffmpeg
stream.run()
```

Raw/uncontrolled run

```py
stream = Stream()

# Load video file
stream.input("video.mp4")

# Use `raw` method to pass your ffmpeg query string
stream.raw("...", raise_exception=True/False)

# Set output filename
stream.output("new video.mp4")

# Run ffmpeg
stream.run()
```
