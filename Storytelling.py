import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

df = pd.read_csv('data_saudi_used_cars.csv')
df_z = df[(df['Negotiable'] == False) & (df['Price'] == 0)]
df_o = df[(df['Negotiable'] == False) & (df['Price'] == 1)]
df = df.drop( index = df_z.index)
df = df.drop( index = df_o.index)

df_more_2019 = df[(df['Price'] == 0) & (df['Year'] >= 2019)]

st.title('The Best Deal in the Used Car Market')
st.markdown('#')

st.markdown(' Abo Khalid, a father of three, is preparing for a significant change. With the arrival of his third baby, he’s looking to upgrade from his smaller Toyota Camry to a spacious SUV. This makes him both a buyer and a seller in the used car market. Fortunately, the used car market in Riyadh, where he resides, is large and thriving.')
image = Image.open('image1.jpg')
st.image(image, width=700, caption="Abo khalid's family")
st.markdown('#')
st.markdown("In Saudi Arabia, 40% of cars are used, indicating strong interest and high purchasing power. As a buyer, Abo Khalid is in a competitive market, which works in his favor. With many options available and a wide range of prices, there are plenty of choices.")
Q2 = pd.DataFrame( {"Region": ['Riyadh', 'Jeddah', 'Dammam', 'Qassim', 
                               'Al-Medina', 'Aseer', 'Al-Ahsa', 'Khobar', 
                               'Makkah', 'Arar', 'Jazan', 'Abha', 
                               'Taef', 'Jubail', 'Hail', 'Sakaka', 
                               'Al-Baha', 'Besha', 'Hafar Al-Batin', 'Wadi Dawasir',
                                'Al-Jouf', 'Qurayyat', 'Najran'], 
                    "%" : [41.9, 
                              15.2, 
                              6.5, 
                              4.9, 4.9, 
                              3.2, 
                              2.8, 
                              2.4, 2.4, 2.4, 
                              2.0, 
                              1.6, 
                              1.2, 1.2, 1.2, 
                              0.8, 0.8, 0.8, 0.8, 0.8, 
                              0.4, 0.4, 0.4]})
st.bar_chart(
    Q2,
    x="Region",
    y="%",
    color=["#FF0000"],  # Optional
)

st.markdown('#')
st.markdown("Additionally, 41.9% of people in Riyadh are open to price negotiations, with some buyers even starting bids at zero, giving Abo Khalid a chance to secure a good deal. In contrast, Jeddah, the closest major region offering similar deals, has only 15% of people willing to negotiate, making Riyadh the ideal place for Abo Khalid's transaction.")
Q1 = df_more_2019.groupby(by = 'Region').size().sort_values(ascending=False)
Q1 = pd.DataFrame( { "Count" :  Q1.values, "Region" : Q1.index})
Q1 = Q1.sort_values("Count", ascending=False)

st.bar_chart(
    Q1,
    x="Region",
    y="Count",
    color=["#FF0000"],  # Optional
)

st.markdown('#')

st.markdown('From the perspective of a seller, Abo Khalid owns a Toyota Camry, a car that holds significant value. Toyota is the best-selling car brand in Saudi Arabia, which means Abo Khalid’s Camry is likely to sell at a good price. Data shows a strong correlation between a car’s price and its brand, and since the Camry is part of the popular Toyota family, it has a solid resale value.')
image3 = Image.open('image3.png')

st.image(image3)
st.markdown('#')
st.markdown('As a buyer looking for an SUV, Abo Khalid also has numerous attractive options. Among these is the Chinese brand Changan, which ranks fourth in popularity for its reasonable prices and appealing style. This makes Changan a highly preferred option for budget-conscious buyers.')
suv = ['CS35', 'CS95', 'CS35 Plus', 'CS75']
df_more_2019 = df[(df['Price'] >= 0) & (df['Year'] >= 2019)]
changan = df_more_2019[(df_more_2019['Make'] == 'Changan') & (df_more_2019['Type'].isin(suv))].sort_values('Price',     ascending=False)

blankIndex= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
changan.index=blankIndex

st.dataframe(changan)
#st.markdown("![Alt Text](https://cdn.dribbble.com/users/330915/screenshots/4880950/1_header_animation_dribbble.gif)")
st.markdown('#')

st.markdown('In the end, Abo Khalid finds himself in a favorable position. He can sell his high-demand Toyota Camry at a good price and purchase an SUV like the Changan for a reasonable cost. He may even make a profit in the process, as the price gap between the well-regarded Toyota and the more affordable Changan works to his advantage.')
st.image("image2.gif")
