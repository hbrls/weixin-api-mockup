from appl import create_app
from appl.configs.production import ProductionConfig

application = create_app(config=ProductionConfig())
