# Getting Started

## Minimum Requirements
1. Host device should have at least 8GB memory.
2. 

## Setup Project Files
1. Download the repositoriy `git clone https://github.com/binodmx/learn-raspberrypi`.
2. Goto `vlm-benchmark` directory.
3. [Optional] Configure `model`, `device`, and `image_path` in `run-vlm-benchmark.py` file to customize.

## Run Ollama in Docker
1. Install docker engine in the host device as in [this](https://docs.docker.com/engine/install/).
2. Run ollama container `docker run -d -p 11434:11434 --name ollama ollama/ollama`.
3. Download the model `docker exec -it ollama ollama pull gemma3:4b`

## Setup WandB
1.

## Run Experiment
1. Run the benchmark `python run-vlm-benchmark.py`
