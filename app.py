import streamlit as st
import pandas as pd
import re
import io

st.set_page_config(page_title="FiberCop Analytics", page_icon="🏠")

st.title("🏠 FiberCop - Analytics Immobiliare")
st.write("Tool professionale per analisi dati immobiliari")

# Upload file Excel
uploaded_file = st.file_uploader("📊 Carica file Excel", type=['xlsx', 'xls'])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success(f"✅ File caricato: {len(df)} records")
    
    # Analisi automatica
    for col in df.columns:
        if any(keyword in col.lower() for keyword in ['descriz', 'note', 'testo']):
            st.info(f"🔍 Analisi colonna: {col}")
            
            # Estrazione anno
            def estrai_anno(testo):
                if pd.isna(testo): return "non specificato"
                match = re.search(r'\b(20[0-2][0-9])\b', str(testo))
                return match.group(0) if match else "non specificato"
            
            df['Anno Costruzione'] = df[col].apply(estrai_anno)
            break
    
    # Risultati
    st.dataframe(df)
    
    # Download
    output = io.BytesIO()
    df.to_excel(output, index=False)
    st.download_button("📥 Scarica Risultati", output.getvalue(), "analisi_fibercop.xlsx")

st.markdown("---")
st.write("FiberCop Analytics v1.0")
