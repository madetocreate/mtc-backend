def handle_input():
    msg = input("🤖 Aion > ")
    from .command_router import route
    route(msg)
