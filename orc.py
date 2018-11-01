from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
tool = tools[0]

txt = tool.image_to_string(
    Image.open('/Users/user/open_cv/TrainingAssistant/static/img/2ah_resito.jpg'),
    lang="jpn",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
print(txt)
# txt is a Python string
