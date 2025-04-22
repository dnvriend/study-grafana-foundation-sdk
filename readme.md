# study-grafana-foundation-sdk

A study project demonstrating the use of Grafana Foundation SDK to create and manage Grafana dashboards programmatically using Python.

## Overview

This project showcases how to use the Grafana Foundation SDK to create, manage, and deploy Grafana dashboards through code. It provides practical examples of creating different types of dashboards, from simple single-panel displays to more complex configurations with multiple panels and advanced features.

## Features

- 🐍 Python-based dashboard creation using Grafana Foundation SDK
- 📊 Progressive examples from basic to advanced dashboard configurations
- 🐳 Docker-based Grafana deployment
- 🔄 Automated dashboard generation

## Project Structure

```
.
├── src/                    # Python scripts for dashboard generation
│   ├── 001_single_panel.py
│   ├── 002_multiple_panels.py
│   ├── 003_http_response_status_panel.py
│   └── 004_treshold_config.py
├── build/                  # Generated dashboard JSON files
├── grafana/               # Grafana provisioning configuration
├── docker-compose.yaml    # Docker Compose configuration
└── Makefile              # Project automation
```

## Prerequisites

- Python 3.x
- Docker and Docker Compose
- Make (optional, but recommended)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/study-grafana-foundation-sdk.git
   cd study-grafana-foundation-sdk
   ```

2. Initialize the project:
   ```bash
   make init
   ```

3. Start Grafana:
   ```bash
   make up
   ```

4. Generate dashboards:
   ```bash
   make generate
   ```

## Usage

### Accessing Grafana

- URL: http://localhost:3000
- Default credentials:
  - Username: admin
  - Password: admin

### Available Make Commands

- `make up` - Start Grafana container
- `make down` - Stop Grafana container
- `make restart` - Restart Grafana container
- `make generate` - Generate dashboard JSON files
- `make clean` - Clean generated dashboard files
- `make logs` - View Grafana logs

### Example Dashboards

1. **Single Panel Dashboard** (`001_single_panel.py`)
   - Basic example of creating a single panel dashboard

2. **Multiple Panels Dashboard** (`002_multiple_panels.py`)
   - Example of creating a dashboard with multiple panels

3. **HTTP Response Status Dashboard** (`003_http_response_status_panel.py`)
   - Monitoring dashboard for HTTP status codes

4. **Threshold Configuration Dashboard** (`004_treshold_config.py`)
   - Example of configuring thresholds and alerts

## Development

To create new dashboards:

1. Create a new Python script in the `src/` directory
2. Use the Grafana Foundation SDK to define your dashboard
3. Run `make generate` to create the JSON files
4. Access the new dashboard in Grafana

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

