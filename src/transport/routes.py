from . import handlers

def get_routes():
    return [
        (r"/api/add", handlers.PayloadsKeeper),
        (r"/api/get", handlers.PayloadsKeeper),
        (r"/api/remove", handlers.PayloadsKeeper),
        (r"/api/update", handlers.PayloadsKeeper),

        (r"/api/statistic", handlers.PayloadsKeeperStatistic),
    ]
