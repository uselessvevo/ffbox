from __future__ import annotations

import os
from typing import Union

import aiomultiprocess

from filters import IFilter
from validators import IValidator

from ffmpeg import FFmpeg
from ffprobe import FFprobe
from ffplay import FFplay


class Stream:

    def __init__(
        self,
        validators: set[IValidator] = None,
        tempfolder: str = None,
        ffmpeg_path: str = os.getenv("FFMPEG_PATH"),
        ffprobe_path: str = os.getenv("FFPROBE_PATH"),
        ffplay_path: str = os.getenv("FFPLAY_PATH")
    ) -> None:
        # List of validators
        self._validators = validators

        # Temporary folder
        self._tempfolder = tempfolder

        # ffmpeg instance
        self._ffmpeg = FFmpeg(ffmpeg_path)

        # ffprobe instance
        self._ffprobe = FFprobe(ffprobe_path)

        # ffplay instance
        self._ffplay = FFplay(ffplay_path)

        # Input file
        self._input_nodes: dict = None

        # Output file
        self._output_nodes: dict = None

    def probe(self, filename: str, *args, **kwargs) -> None:
        """
        Use ffprobe to get file info
        """

    def exclude_formats(self, *formats: tuple[str]) -> None:
        """
        Exclude these file formats for all nodes

        Args:
            formats (tuple[str]): array of file formats
        """

    def allow_formats(self, *formats: tuple[str]) -> None:
        """
        Allow these file formats for all nodes

        Args:
            formats (tuple[str]): array of file formats
        """

    def input(
        self,
        filename: str,
        name: str = None,
        file_format: str = None,
        guess_format: str = None,
        validators: list[IValidator] = None,
        **options,
    ) -> None:
        """
        Load input file

        Args:
            filename (str): input filename or path
            name (str): filename alias/tag
            file_format (str): manually specify file format to skip `guess_format`
            guess_format (bool): will invoke `guess_format` method
            validators (str): list of validators for this operation only
            options (dict): options for `Node` based class
        """

    def output(
        self,
        filename: str,
        validators: list[IValidator] = None,
        **options
    ) -> None:
        """
        Set output file name

        Args:
            filename (str): output filename or path
            validators (str): list of validators for this operation only
            options (dict): options for `Node` based class
        """

    def filter(
        self,
        file_filter: Union[str, callable, IFilter],
        filename: str,
        validators: list[IValidator] = None,
        **options
    ) -> None:
        """
        Build filter query for specified file by string, method or `IFilter` based class

        Args:
            file_filter (str, callable, IFilter): filter query builder
            filename (str): file name or path
            validators (list[IValidator, ...]): list of validators
            options (dict): options for `Node` based class
        """

    def convert(
        self,
        converter: Union[str, callable],
        filename: str,
        validators: list[IValidator] = None,
        **options
    ) -> None:
        """
        Build converter query for specified file by string, method or `IFilter` based class

        Args:
            converter (str, callable, IFilter): filter query builder
            filename (str): file name or path
            validators (list[IValidator, ...]): list of validators
            options (dict): options for `Node` based class
        """

    def concat(
        self,
        first_stream: Union[str, Stream],
        second_stream: Union[str, Stream]
    ) -> None:
        """
        Concat two files or streams

        Args:
            first_stream (str, Stream):
            second_stream (str, Stream):
        """

    def validate(self, node_name: str) -> None:
        """
        Validate file by its node name
        """

    def set_metadata(self, metadata: dict) -> None:
        """
        Set metadata for file
        """
        
    def add_validators(self, *validators: tuple[IValidator]) -> None:
        for validator in validators:
            if not isinstance(validator, IValidator):
                raise TypeError(f"Validator {validator.__class__.__name__} is not a `IValidator` based class")

            self._validators.add(validator)

    def run(
        self,
        run_async: bool = False, 
        **runner_options
    ) -> Union[str, None]:
        """
        Run ffmpeg in standard or async mode
        """
        self._ffmpeg.run(run_async, **runner_options)
