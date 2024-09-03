from typing import List

from singer_sdk import Tap, Stream

from singer_sdk import typing as th  # JSON schema typing helpers

from tap_staffwise.streams import StaffwiseStream, ReportingStream

STREAM_TYPES = [ReportingStream]

class TapStaffwise(Tap):
    """Staffwise tap class."""

    name = "tap-staffwise"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="API Key to authenticate requests and access the API",
        ),
        th.Property(
            "subdomain",
            th.StringType,
            required=True,
            description="Subdomain you would like to pull data from",
        ),
        th.Property(
            "reporting_id",
            th.StringType,
            required=True,
            description="Reporting ID of each report",
        ),
        th.Property(
            "start_date",
            th.StringType,
            description="The start date for filtering results in the API call",
        ),
        th.Property(
            "stop_date",
            th.StringType,
            description="The end date for filtering results in the API call",
        ),
    ).to_dict()
    
    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""

        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
