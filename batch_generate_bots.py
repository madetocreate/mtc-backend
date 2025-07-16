import subprocess

bots_to_generate = [
    {
        "bot": "VoiceBot",
        "hub": "Content Hub",
        "path": "modules/content/voicebot.py",
        "desc": "Erzeugt Audio aus Texten, unterstützt RealTalkBox",
        "tech": "ElevenLabs, Whisper, GPT-4o"
    },
    {
        "bot": "RouterBot",
        "hub": "Core",
        "path": "modules/core/routerbot.py",
        "desc": "Semantisches Routing eingehender Prompts",
        "tech": "GPT-4o, LangChain, Claude"
    },
    {
        "bot": "MemoryManagerBot",
        "hub": "Core",
        "path": "modules/core/memorymanager.py",
        "desc": "Verwaltet Einträge, filtert irrelevante Inhalte, speichert sie sortiert",
        "tech": "Pinecone, Mem0, GPT"
    }
]

for bot in bots_to_generate:
    cmd = [
        "python3", "aion_generate_bot.py",
        "--bot", bot["bot"],
        "--hub", bot["hub"],
        "--path", bot["path"],
        "--desc", bot["desc"],
        "--tech", bot["tech"],
        "--doc", "--test", "--push"
    ]
    subprocess.run(cmd)
