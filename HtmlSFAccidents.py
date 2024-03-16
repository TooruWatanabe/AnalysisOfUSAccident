import folium
import pandas as pd

# ファイルからデータ読み込み
df = pd.read_csv('SFAccidents.csv')

# NaN を含む行を取り除く
df = df.dropna(subset=['Start_Lat', 'Start_Lng'])

# 地図の作成
map = folium.Map(location=[df.iloc[0]['Start_Lat'], df.iloc[0]['Start_Lng']], zoom_start=10)

# マーカーの追加
for i, r in df.iterrows():
    folium.Marker(location=[r['Start_Lat'], r['Start_Lng']], popup=r['Start_Time']).add_to(map)

# 地図を保存
map.save("SFAccidents.html")
