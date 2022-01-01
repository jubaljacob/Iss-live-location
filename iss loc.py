import pandas as pd
import plotly.express as px
link = "http://api.open-notify.org/iss-now.json"
data_frame = pd.read_json(link)
data_frame['latitude'] = data_frame.loc['latitude', 'iss_position']
data_frame['longitude'] = data_frame.loc['longitude', 'iss_position']
data_frame.reset_index(inplace=True)
df = data_frame.drop(['index', 'message'], axis=1)
fig = px.scatter_geo(df, lat='latitude', lon='longitude')
fig.show()
