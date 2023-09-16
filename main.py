from bokeh.plotting import figure, show
from bokeh.embed import components
from bokeh.resources import CDN

from flask import Flask, render_template

from vis_utils import Visualization
from csv_utils import DataUtils

app=Flask(__name__)

@app.route('/plot')
def plot():
    x = [1, 2, 3, 4, 5]
    y = [4, 5, 5, 7, 2]

    # create a new plot with a title and axis labels
    p = figure(title="Glyphs properties example", x_axis_label="x", y_axis_label="y")

    # add circle renderer with additional arguments
    p.circle(
        x,
        y,
        legend_label="Objects",
        fill_color="red",
        fill_alpha=0.5,
        line_color="blue",
        size=80,
    )
    script, div = components(p)
    cdn_js = CDN.js_files[0]
    # cdn_css = CDN.css_files[0]
    cdn_css = "http://cdn.pydata.org/bokeh/release/bokeh-0.9.0.min.css"
    return render_template('index.html', script=script, div=div, cdn_css=cdn_css, cdn_js=cdn_js)


@app.route('/wordcloud')
def plot_wordcloud():
    df = DataUtils.load_csv_df('files/commits/all/cassandra-bug-fix-comment-log-dataset.csv')
    image = Visualization.wordcloud(df, 'Author')
    return render_template('image.html', wordcloud_image=image)



@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)