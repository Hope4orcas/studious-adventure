import pandas as pd


death_valley = [36.612522776588335, -117.07273898100844]
bermuda = [25.00186509860103, -70.99905617134607]
reno = [39.53043105766029, -119.81004728442414]

sitios = []
sitios.append(death_valley)
sitios.append(bermuda)
sitios.append(reno)

st.write(sitios)

sitios_df = pd.DataFrame(sitios,columns=['lat','lon'])

st.write(sitios_df)

st.map(sitios_df)
