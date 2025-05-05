import openai
import time
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Provide the assistant ID recieved when querying it
assistant_id="asst_xxxxxxxxx"

# Step 2: Create a new Thread
thread = openai.beta.threads.create()

# Step 3: Add a message to the Thread
message = openai.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Give me a puzzle"
)

# Step 4: Run the Assistant on the Thread
run = openai.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant_id
)

print("Run started! Waiting for assistant to reply...")

# Step 5: Poll until the Run is completed
while True:
    # Check the status of the run
    current_run = openai.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    if current_run.status == "completed":
        break
    elif current_run.status == "failed":
        print("Run failed.")
        exit()
    else:
        time.sleep(1)  # Wait a second before checking again

# Step 6: Fetch the messages after the run is complete
messages = openai.beta.threads.messages.list(thread_id=thread.id)

# Step 7: Print the Assistant's reply
for msg in messages.data:
    if msg.role == "assistant":
        print("\nAssistant's Reply:")
        print(msg.content[0].text.value)
