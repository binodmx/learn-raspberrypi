# Getting Started

## Setup Project Files
1. Download the repositoriy `git clone https://github.com/binodmx/learn-raspberrypi`.
2. Goto `vlm-benchmark` directory.
3. [Optional] Configure `model`, `device`, and `image_path` in `run-vlm-benchmark.py` file to customize.

## Setup WandB
1. Create an account on [WandB](https://wandb.ai/).
2. Get an API key and add it to `.env` file.
3. [Optional] Configure `project` and name in `wandb.init()`.

## Run Ollama in Docker
> [!NOTE]
> Host device should have at least 8GB memory.
1. Install docker engine in the host device as in [this](https://docs.docker.com/engine/install/).
2. Run ollama container `docker run -d -p 11434:11434 --name ollama ollama/ollama`.
3. Download the model `docker exec -it ollama ollama pull gemma3:4b`.

## Run Experiment
1. Run the benchmark `python run-vlm-benchmark.py`.
2. Observe results on WandB.
