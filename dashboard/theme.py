import streamlit as st

def load_theme():

    st.markdown(
        """
<style>

# Halaman
.stApp{
    background:#FFFFFF;
    color:#1F2937;

}

# Layout
.main .block-container{
    max-width:1450px;
    padding-top:2rem;
    padding-bottom:2rem;
}

# Judul
h1{
    color:#111827 !important;
    font-size:2.5rem !important;
    font-weight:700 !important;
}

h2{
    color:#111827 !important;
    font-size:1.8rem !important;
    font-weight:700 !important;
}

h3{
    color:#111827 !important;
    font-size:1.35rem !important;
    font-weight:600 !important;
}

h4,h5,h6{
    color:#111827 !important;
    font-weight:600 !important;
}

# Text
p,
label,
span{
    color:#374151 !important;

}

# Devider atau Pembatas
hr{
    border:none !important;
    border-top:2px solid #D1D5DB !important;
    margin-top:32px !important;
    margin-bottom:32px !important;
}

# Input Tanggal
.stDateInput input{
    background:#FFFFFF !important;
    color:#111827 !important;
    border:1px solid #D1D5DB !important;
    border-radius:8px !important;
}

# Tombol
.stButton>button{
    background:#FFFFFF !important;
    color:#111827 !important;
    border:1px solid #D1D5DB !important;
    border-radius:8px !important;
    height:42px;
    transition:0.2s;
}

.stButton>button:hover{
    background:#F3F4F6 !important;
}

# Segmented Control
[data-testid="stSegmentedControl"]{
    border:1px solid #D1D5DB;
    border-radius:10px;
    padding:4px;
    background:#FFFFFF;
}

# Streamlit Container
[data-testid="stVerticalBlockBorderWrapper"]{
    border:1px solid #D1D5DB !important;
    border-radius:12px !important;
    background:#FFFFFF !important;
    box-shadow:0 2px 8px rgba(0,0,0,.04);
    padding:14px;
}

# Metric Card
.metric-card{
    background:#FFFFFF;
    padding:4px;
}

.metric-title{
    color:#6B7280;
    font-size:15px;
    margin-bottom:8px;
}

.metric-value{
    color:#111827;
    font-size:28px;
    font-weight:700;
}

# Dataframe
[data-testid="stDataFrame"]{
    border-radius:10px;
    overflow:hidden;
}

# Caption
[data-testid="stCaptionContainer"]{
    color:#6B7280 !important;
}

# Plotly Modebar
.modebar{
    background:transparent !important;
}

# Scrollbar
::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-thumb{
    background:#C7C7C7;
    border-radius:20px;
}

::-webkit-scrollbar-thumb:hover{
    background:#A8A8A8;
}

</style>
""",
        unsafe_allow_html=True,
    )
