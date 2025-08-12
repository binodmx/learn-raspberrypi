# Getting Started

## Setup Project Files
1. Download the repositoriy `git clone https://github.com/binodmx/learn-raspberrypi`.
2. Goto `vlm-benchmark` directory.
3. Add an image file.
4. Configure `model`, `device`, and `image_path` in `run-vlm-benchmark.py` file.

# Run Ollama in Docker
1. Install docker in the host device.
2. Run ollama container `docker run -d -p 11434:11434 --name ollama ollama/ollama`.
3. Download the model `docker exec -it ollama ollama pull gemma3:4b`

# Setup WandB
1.

# Run Experiment
1. Run the benchmark `python run-vlm-benchmark.py`
