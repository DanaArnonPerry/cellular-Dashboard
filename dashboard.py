
import streamlit as st
st.set_page_config(page_title="דשבורד מדד הסלולר", layout="wide")

import pandas as pd

@st.cache_data
def load_data():
    xls = pd.ExcelFile("cell_data_full_expanded.xlsx")
    return {
        "🎮 גיימינג": pd.read_excel(xls, "גיימינג"),
        "📲 סושיאל": pd.read_excel(xls, "סושיאל"),
        "🔋 תלות בנייד": pd.read_excel(xls, "תלות בנייד"),
        "🎧 פודקאסטים": pd.read_excel(xls, "פודקאסטים"),
        "👨‍👩‍👧‍👦 המשפחה הסלולרית": pd.read_excel(xls, "המשפחה הסלולרית"),
    }

data = load_data()
st.title("📱 דשבורד אינטראקטיבי – מדד הסלולר בישראל")

# ניווט בין נושאים
tab_names = list(data.keys())
tabs = st.tabs(tab_names)

for tab, name in zip(tabs, tab_names):
    with tab:
        st.subheader(f"{name} – נתונים מלאים")
        df = data[name]
        st.dataframe(df, use_container_width=True)

        st.markdown("### 🔍 בחר מדד להצגה גרפית")
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        if len(numeric_cols) > 0:
            selected = st.selectbox("בחר מדד להצגה", numeric_cols, key=name)
            chart_df = df.set_index(df.columns[0])[[selected]]
            st.bar_chart(chart_df)
        else:
            st.info("אין עמודות מספריות להצגה גרפית בגיליון זה.")
