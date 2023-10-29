# import asyncio
# from hume import HumeStreamClient
# from hume.models.config import ProsodyConfig

# def find_top_three_emotions(data):
#     emotions = data['prosody']['predictions'][0]['emotions']

#     # Sort the emotions by score in descending order
#     sorted_emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)

#     # Get the top three emotions
#     top_three_emotions = [emotion['name'] for emotion in sorted_emotions[:3]]

#     return top_three_emotions

# async def main(content):
#     client = HumeStreamClient("4pLMpdxQgho6hO7YaPvFrm4xssArylydAIgfUfAZrh6A44xu")
#     configs = [ProsodyConfig()]
#     async with client.connect(configs) as socket:
#         result = await socket.send_file(content)
#         return find_top_three_emotions(result)

from hume import HumeBatchClient
from hume.models.config import FaceConfig
from hume.models.config import ProsodyConfig



def get_top_emotions(data):
    emotions = []
    
    # Extract emotions from the data
    predictions = data[0]['results']['predictions'][0]['models']['prosody']['grouped_predictions'][0]['predictions'][0]['emotions']
    
    # Sort emotions by score in descending order
    sorted_emotions = sorted(predictions, key=lambda x: x['score'], reverse=True)
    
    # Get the top 5 emotions
    top_5_emotions = sorted_emotions[:5]
    
    # Extract emotion names and scores
    for emotion in top_5_emotions:
        emotions.append({
            'name': emotion['name'],
            'score': emotion['score']
        })
    
    print(emotions)
    return [x['name'] for x in emotions]
    

client = HumeBatchClient("4pLMpdxQgho6hO7YaPvFrm4xssArylydAIgfUfAZrh6A44xu")

configs = [ProsodyConfig()]

def run(content):
    files = [content]
    job = client.submit_job([],configs, files=files)
    print(job)
    print("Running...")
    job.await_complete()
    print(job.get_predictions())
    return job.get_predictions()