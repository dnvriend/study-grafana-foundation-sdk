from grafana_foundation_sdk.builders import (
    timeseries as timeseries_builder, 
    dashboard as dashboard_builder, 
    testdata as testdata_builder,
    text as text_builder,
    common as common_builder
)
from grafana_foundation_sdk.models import common as common_model, dashboard as dashboard_model
from grafana_foundation_sdk.models.dashboard import DashboardCursorSync, ValueMap, ValueMappingResult
from grafana_foundation_sdk.cog.encoder import JSONEncoder

NAME = "003-http-response-status"

# Define value mappings for HTTP status codes
HTTP_STATUS_VALUE_MAPPINGS = [
    ValueMap(
        options={
            # Mapping ranges to text and color
            "from": 200, "to": 299, "result": ValueMappingResult(text="2xx Success", color="green")
        }
    ),
    ValueMap(
        options={
            "from": 300, "to": 399, "result": ValueMappingResult(text="3xx Redirect", color="blue")
        }
    ),
    ValueMap(
        options={
            "from": 400, "to": 499, "result": ValueMappingResult(text="4xx Client Error", color="orange")
        }
    ),
    ValueMap(
        options={
            "from": 500, "to": 599, "result": ValueMappingResult(text="5xx Server Error", color="red")
        }
    ),
]

def text_description() -> text_builder.Panel:
    return (
        text_builder.Panel()
        .title("Description")
        .content("This panel displays the HTTP status codes for the current time range. It uses a random walk to simulate the data and it uses stacking to show the percentage of each status code and fill opacity to fill the areas under the lines with a solid color...")
        .grid_pos(dashboard_model.GridPos(x=0, y=0, w=12, h=5))                     
    )

def timeseries_http_status_codes() -> timeseries_builder.Panel:
    """
    Builds a Timeseries panel simulating HTTP status codes using random_walk.
    """
    return (
        timeseries_builder.Panel()
        .title("Response Statuses")
        .datasource("randomid1")
        .with_target(
            testdata_builder.Dataquery()
                .scenario_id("random_walk")
                .ref_id("A")
                .alias("2xx")
                .min(50).max(100)
                .start_value(0)
        )
        .with_target(
            testdata_builder.Dataquery()
                .scenario_id("random_walk")
                .ref_id("B")
                .alias("3xx")
                .min(1).max(10)
                .series_count(1)
        )
        .with_target(
            testdata_builder.Dataquery()
                .scenario_id("random_walk")
                .ref_id("C")
                .alias("4xx")
                .min(1).max(2)
                .series_count(1)
                .start_value(0)
        )
        .with_target(
            testdata_builder.Dataquery()
                .scenario_id("random_walk")
                .ref_id("D")
                .alias("5xx")
                .min(1).max(2)
                .start_value(0)
        )
        .mappings(HTTP_STATUS_VALUE_MAPPINGS)
        .unit("none")
        .height(8)
        .span(12)
        .draw_style(common_model.GraphDrawStyle.LINE)
        .line_width(2)
        .fill_opacity(100)
        .stacking(common_builder.StackingConfig().group("A").mode(common_model.StackingMode.PERCENT))
        .grid_pos(dashboard_model.GridPos(x=0, y=5, w=12, h=8))
    )


# Create a new dashboard builder
builder = (
    dashboard_builder.Dashboard(NAME)
    .uid(NAME)
    .tags(["tags", "tutorial", "testdata", "http-status"])
    .editable()
    .tooltip(DashboardCursorSync.CROSSHAIR)
    .refresh("1s")
    .time("now-24h", "now")
    .timezone("browser")
    .timepicker(
        dashboard_builder.TimePicker()
        .refresh_intervals(["5s", "10s", "30s", "1m", "5m"])
        .quick_ranges([
            dashboard_builder.TimeOption().from_val("now-1m").to("now").display("Last 1 minute"),
            dashboard_builder.TimeOption().from_val("now-5m").to("now").display("Last 5 minutes"),
            dashboard_builder.TimeOption().from_val("now-15m").to("now").display("Last 15 minutes"),
            dashboard_builder.TimeOption().from_val("now-1h").to("now").display("Last 1 hour"),
            dashboard_builder.TimeOption().from_val("now-1d").to("now").display("Last 1 day"),
            dashboard_builder.TimeOption().from_val("now-5d").to("now").display("Last 5 days"),
            dashboard_builder.TimeOption().from_val("now-1w").to("now").display("Last 1 week"),
        ])
    )
    .with_panel(text_description())
    .with_panel(timeseries_http_status_codes())
)

# Build the dashboard object
dashboard_model = builder.build()

# Encode the dashboard model to JSON and print to stdout
encoder = JSONEncoder(sort_keys=True, indent=2)
dashboard_json = encoder.encode(dashboard_model)

# Save the dashboard JSON to a file
import os
if not os.path.exists("build"):
    os.makedirs("build")

with open(f"build/{NAME}.json", "w") as f:
    f.write(dashboard_json)

print(f"Dashboard saved to build/{NAME}.json")