import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Florence's website", page_icon=":shark:")

st.caption("Demo by HKBU")
st.title("Learn Creating Website")

with st.sidebar:
    st.write("By Florence")
    st.markdown("[Email Me](mailto:wyfok@hkbu.edu.hk.com)")

filepath ="ust_data.xlsx"
data = pd.read_excel(filepath, sheet_name='data')

data1 = data.copy()
data1.rename(columns={'year published':'year'}, inplace=True)
def grouped_year(year):
  if 1501 <= year <= 1600:     # if the value of year is larger than or equal to 1501 AND smaller than or equal to 1600
    return "16th century"      # then, assign "16th century" to the "Period" column for this row
  elif 1601 <= year <= 1700:
    return "17th century"
  elif 1701 <= year <= 1800:
    return "18th century"
  elif 1801 <= year <= 1900:
    return "19th century"
  elif 1901 <= year <= 2000:
    return "20th century"
  else:
    return "Ungrouped"         # in case any values fall outside the above scope, show "Ungrouped" in the "Period" column for this row
# make a copy of the original dataframe "data", and named the copy as "data1"

# create a new column called "Period", and assign label to each row
data1["Period"] = data1["year"].apply(lambda year: grouped_year(year))
data1


plotly_chart1 = px.histogram(data1, x='Period', y='number of items')
plotly_chart1.update_layout(
    title = 'Number of Items by Century',
    yaxis_title='Number of items',
    xaxis_title='Century',
)
# show the plotly chart
st.plotly_chart(plotly_chart1, use_container_width=True)
# another plotly chart 
plotly_chart3 = px.bar(data1, x='year', y='number of items',
            color='Period',
            color_discrete_sequence=["#ffb7b2", "#ffdac0", "#e3f0cb", "#b5ead9", "#c7cee9"])
plotly_chart3.update_layout(
    title = 'Number of Items by Year',
    yaxis_title='Number of items',
    xaxis_title='Year',
    paper_bgcolor = 'white', 
    plot_bgcolor = 'white', 
    xaxis = dict(
        showline = True,
        linecolor = 'rgb(102, 102, 102)',
        tickfont_color = 'rgb(102, 102, 102)',
        showticklabels = True,
        dtick = 10,
        ticks = 'outside',
        tickcolor = 'rgb(102, 102, 102)',
    ),
    yaxis = dict(
        showline = True,
        linecolor = 'rgb(102, 102, 102)',
        tickfont_color = 'rgb(102, 102, 102)',
        showticklabels = True,
        dtick = 5, 
        ticks = 'outside',
        tickcolor = 'rgb(102, 102, 102)',
    ),
)
plotly_chart3.add_hline(y = data1['number of items'].mean(), annotation_text = 'average line', line_width = 1, line_color = '#edc982')
plotly_chart3.update_layout(hovermode='x unified')
# show the plotly chart
st.plotly_chart(plotly_chart3, use_container_width=True)


#print() in ipynb, When developing Streamlit application, st.write() and st.markdown() would be good choices to do so.
#The only difference is that, we wrote plotly_chartname.show() to display the chart in Jupyter Notebook while writing st.plotly_chart(plotly_chartname, use_container_width=True) in the .py file for Streamlit application.