# import the builders; you create panels, datasources, rows, etc with builders!
from grafana_foundation_sdk.builders import timeseries, dashboard, testdata
# configuration
from grafana_foundation_sdk.models.dashboard import DashboardCursorSync 
from grafana_foundation_sdk.models.common import TimeZoneBrowser
# import the encoder
from grafana_foundation_sdk.cog.encoder import JSONEncoder

NAME="001-single-panel"

"""
Grafana Terms
-------------

| Term       | Description                                      |
|------------|--------------------------------------------------|
| Dashboard  | A collection of panels                           |
| Panel      | A single chart                                   |
| Row        | A collection of panels                           |
| Datasource | A source of data                                 |
| Query      | A request for data from a datasource            |
| Scenario   | A collection of queries                          |
| Simulation | A collection of scenarios                        |
| Key        | A unique identifier for a query                 |
| Target     | A query that is used to create a panel          |
| ref_id     | A unique identifier for a query                 |
| uid        | A unique identifier for a dashboard             |
"""

def timeseries_random_walk() -> timeseries.Panel:
    """
    Builds a Timeseries panel displaying a random walk from TestData.    
    """
    # Return the built Timeseries panel
    return (
        # Create a new Timeseries panel builder
        timeseries.Panel()
        # Set the title of the panel
        .title("Random Walk")
        # Set the datasource for the panel
        .datasource("randomid1")
        # Add a data query (target) to the panel
        .with_target(
            # Create a new TestData data query builder
            testdata.Dataquery()
                # Set the scenario ID for the TestData query
                .scenario_id("random_walk")
                # Set the reference ID for the query
                .ref_id("A")
        )
        # Set the height of the panel in grid units
        .height(8)
        # Set the width (span) of the panel in grid units (12 is full width)
        .span(12)
    )

# Create a new dashboard builder
builder = (
    dashboard.Dashboard(NAME)
    .uid(NAME)
    .tags(["single-panel", "tutorial", "testdata"])
    .editable()
    .tooltip(DashboardCursorSync.CROSSHAIR)
    .refresh("1m")
    .time("now-1h", "now")
    .timezone(TimeZoneBrowser)
    .timepicker(
        dashboard.TimePicker()
        .refresh_intervals(["5s", "10s", "30s", "1m", "5m"])
        .quick_ranges([
            dashboard.TimeOption().from_val("now-1m").to("now").display("Last 1 minute"),
            dashboard.TimeOption().from_val("now-5m").to("now").display("Last 5 minutes"),
            dashboard.TimeOption().from_val("now-15m").to("now").display("Last 15 minutes"),
            dashboard.TimeOption().from_val("now-1h").to("now").display("Last 1 hour"),
            dashboard.TimeOption().from_val("now-12h").to("now").display("Last 12 hours"),
            dashboard.TimeOption().from_val("now-1d").to("now").display("Last 24 hours"),
            dashboard.TimeOption().from_val("now-7d").to("now").display("Last 7 days"),
            dashboard.TimeOption().from_val("now-30d").to("now").display("Last 30 days"),
        ])
    )
    # Add a row with multiple panels showing different TestData scenarios
    .with_row(dashboard.Row("TestData Examples"))
    # Add panels to the row using the defined functions
    .with_panel(timeseries_random_walk())
)

# Build the dashboard object
dashboard_model = builder.build()

# Encode the dashboard model to JSON and print to stdout
encoder = JSONEncoder(sort_keys=True, indent=2)
dashboard_json = encoder.encode(dashboard_model)

# Save the dashboard JSON to a file
with open(f"build/{NAME}.json", "w") as f:
    f.write(dashboard_json)

print(f"Dashboard saved to build/{NAME}.json")
