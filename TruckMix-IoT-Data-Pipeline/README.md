## Features

- Real-time data ingestion from cement mixture sensors
- Data cleaning, normalization, and enrichment
- Automated ETL pipeline with error handling and recovery
- Data quality assurance checks
- Performance optimization for large-scale data processing
- Integration with data warehouse and analytics platforms
- Basic dashboards for data monitoring
- Anomaly detection and predictive maintenance capabilities


## Installation

1. Clone the repository:

git clone https://github.com/anurag2505/Cement-Mixer-IoT-Data-Pipeline.git

2. Navigate to the project directory:

cd TruckMix-IoT-Data-Pipeline

3. Create a virtual environment:

python -m venv venv

4. Activate the virtual environment:
- On Windows: `venv\Scripts\activate`
- On macOS and Linux: `source venv/bin/activate`

5. Install the required packages:

- pip install -r requirements.txt

## Usage

1. Configure the project settings in `config/config.yaml`
2. Run the ETL pipeline: python src/pipeline/etl_pipeline.py
3. Monitor the pipeline: python src/pipeline/pipeline_monitor.py

