# app/core/config.py

from pathlib import Path

# Root project directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Dataset directory
DATASET_DIR = BASE_DIR / "datasets"

# Output directory
OUTPUT_DIR = BASE_DIR / "outputs"

# Graph directory
GRAPH_DIR = OUTPUT_DIR / "graphs"

# Route images
ROUTE_DIR = OUTPUT_DIR / "routes"

# Report directory
REPORT_DIR = OUTPUT_DIR / "reports"

# Create directories automatically
GRAPH_DIR.mkdir(parents=True, exist_ok=True)
ROUTE_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)