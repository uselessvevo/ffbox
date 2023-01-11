# Cloudyff - ffmpeg wrapper

> **Note**: `cloudyff` in deep development

# How to setup?

To setup ffmpeg, ffprobe and ffplay path you can to set environment variables:
* CLOUDY_FFMPEG_PATH - ffmpeg relative path
* CLOUDY_FFPROBE_PATH - ffprobe relative path
* CLOUDY_FFPLAY_PATH - ffplay relative path

Alternatively you can pass `ffmpeg_path`, `ffprobe_path`, `ffplay_path` arguments into `Stream` class

# Query format

`ffmpeg -i <input file> {global input filters} -filter_complex={complex/mapped filter} {global output filter} <output file>`

# Examples

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

Concat audio with video

```py
stream = Stream()

# Load video file
stream.input("video.mp4")

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
stream.concat(["video.mp4", "myaudio"])

# Set output filename
stream.output("noisy movie.mp4")

# Run ffmpeg
stream.run()
```

Concat two streams

```py
stream_video = Stream()

# Load video file
stream_video.input("video.mp4", name="video")

# Load audio file
stream_audio = Stream()

# Load audio file
stream_audio.input("audio.mp3", name="audio")

stream = Stream()

# Should we add `stream.add_streams(stream_a, stream_b)`?

# Concat two streams
# Will use `filter_complex` query
stream.concat([stream_video, stream_audio])

# Run ffmpeg
stream.raw()
```

Additional parameters

```py
# Setup `Stream` instance with the next arguments:
# * async_run - run is separate processes
# * temp - copy files into temporary directory to prevent file corruption and loses
# * validators - list of validators; will be applied for each file and filters
stream = Stream(async_run=True, temp=True, validators=[...])

# Load video
stream.input("input.mp4")

# Will move this after new input
stream.filter(fps_method, fps=60)

# Also you can pass raw string as ffmpeg filter. Thanks to python-ffmpeg repo it's cool
# In this example this filter uses `OUTPUT` scope
# Use: -filter:v output.ff
stream.filter("fps", scope=FilterScope.[INPUT, INNER, OUTPUT], fps=60)

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

Validation

```py
stream = Stream(
	validators=[
		FormatValidator(allow=["mp3", "avi"]),
		BitrateValidator(min_bitrate="128k", max_bitrate="320k"),
	]
)

# Load audio file
stream.input("audio.mp3")

...

# Run ffmpeg
stream.run()
```

Add validators manually

```py
stream = Stream()

# Add validators
stream.add_validators(
  FormatValidator(allow=["mp3", "avi"]),
  BitrateValidator(min_bitrate="128k", max_bitrate="320k"),
)
```

Validate per input/filter

```py
stream = Stream()

# Load audio file
stream.input("audio.mp3", validators=[BitrateValidator(min_bitrate="128k", max_bitrate="320k")])

...

# Run ffmpeg
stream.run()
```
