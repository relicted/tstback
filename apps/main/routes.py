from apps.main import endpoints


routes = (
    dict(method="POST", path="/", handler=endpoints.Handler, name='get_data'),
    dict(method="GET", path="/", handler=endpoints.Handler),
    # dict(method="GET", path="/ws", handler=endpoints.websocket_handler, name='ws_handler'),

)


