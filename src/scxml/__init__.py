import logging
from . import pyscxml

logger = logging.getLogger("pyscxml")
#logger.addHandler(NullHandler())
logging.basicConfig(level=logging.DEBUG)