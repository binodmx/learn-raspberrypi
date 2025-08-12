from ollama import ChatResponse, chat
import wandb
import dotenv

dotenv.load_dotenv()

# Configure the model and device
model = "gemma3:4b"
device = "Raspberry Pi"
image_path = "car.jpg"

# Initialize wandb for logging
wandb.init(
    project="VLM Benchmark",
    name=device,
)

# Define the requests and responses
requests = [
    "Hello!", # This is a warm-up request to get the model ready.
    "What is the colour of the car in the image?",
    "What is the make and model of the car in the image?",
    "What is the licence plate number of the car in the image?",
    "Is the car in the image familiar to you?",
]
responses = []

# Load the image data from a file
with open(image_path, "rb") as f:
    image_data = f.read()

# Run the model on the requests
for request in requests:
  response: ChatResponse = chat(model=model, messages=[
    {
      "role": "user",
      "content": request,
      "images": [image_data]
    },
  ])
  wandb.log({
      "eval_duration": response.eval_duration/1e9,
      "prompt_eval_duration": response.prompt_eval_duration/1e9,
      "total_duration": response.total_duration/1e9,
      "eval_count": response.eval_count,
      "prompt_eval_count": response.prompt_eval_count,
  })
  responses.append(response.message.content)

# Create a wandb Table to log the requests and responses
my_table = wandb.Table(columns=["Request", "Response"], data=list(zip(requests[1:], responses[1:])))
wandb.log({"Messages": my_table})

# Finish the wandb run
wandb.finish()
