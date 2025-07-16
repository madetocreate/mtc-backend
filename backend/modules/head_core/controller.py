import os

def get_api_key(service: str):
    return os.getenv(f"{service.upper()}_API_KEY", "no-key")

def decide_module(task: str):
    if "video" in task.lower():
        return "video_gen"
    elif "image" in task.lower():
        return "image_gen"
    elif "3d" in task.lower():
        return "3d_render"
    elif "audio" in task.lower():
        return "audio_voice"
    elif "text" in task.lower():
        return "text_writer"
    elif "research" in task.lower():
        return "research_ai"
    return "unknown"
