"""Stream type classes for tap-staffwise."""

from __future__ import annotations

import sys

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_staffwise.client import StaffwiseStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = importlib_resources.files(__package__) / "schemas"


class ReportingStream(StaffwiseStream):
    """Define custom stream."""
    @property
    def path(self):
        return f"/reporting/api/get-data/{self.config['reporting_id']}"
    
    name = "reporting"
    replication_key = None
    schema = th.PropertiesList(
        th.Property("Shift ID", th.StringType),
        th.Property("Location", th.StringType),
        th.Property("Location code", th.StringType),
        th.Property("Salesforce ID", th.StringType),
        th.Property("Type", th.StringType),
        th.Property("Region", th.StringType),
        th.Property("Date", th.StringType),
        th.Property("Submission date", th.StringType),
        th.Property("Staff", th.StringType),
        th.Property("Parent Question", th.StringType),
        th.Property("Question", th.StringType),
        th.Property("Subject", th.StringType),
        th.Property("Response", th.StringType)
    ).to_dict()
