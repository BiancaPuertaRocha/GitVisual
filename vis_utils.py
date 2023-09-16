
import pandas as pd
from wordcloud import WordCloud
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.plotting import show, output_notebook
from io import BytesIO
import base64

class Visualization:
    @staticmethod
    def wordcloud(df, col):
        df[col] = df[col].str.replace('.', '')
        df[col] = df[col].str.replace('-', '')
        df[col] = df[col].str.replace('_', '')
        df[col] = df[col].str.replace(' ', '')
        text_data = df[col].dropna()

        # Combine all the text data into a single string
        text = " and ".join(text_data)

        # Create a WordCloud object
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

        filename = f'generated_files/{col}.png'
        wordcloud.to_file(filename)
        image_bytes = BytesIO()
        wordcloud.to_image().save(image_bytes, format="PNG")
        image_bytes = image_bytes.getvalue()

        # Encode the image bytes as a base64 string
        wordcloud_image = base64.b64encode(image_bytes).decode('utf-8')
        return wordcloud_image