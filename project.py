import pandas as pd
import plotly.express as pe

data = pd.read_csv("data.csv")

mean = data.groupby(["student_id" , "level" ] , as_index = False )["attempt"].mean()

graph = pe.scatter(mean , x = "student_id" , y = "level" , color = "attempt" )

graph.show()










