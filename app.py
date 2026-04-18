import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Financial Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------
# Custom CSS
# -----------------------
st.markdown("""
<style>
.stApp {
    background-color: #f5f7fb;
}

.main-title {
    font-size: 40px;
    font-weight: 800;
    color: #1d3557;
    margin-bottom: 0.15em;
}

.sub-title {
    font-size: 17px;
    color: #5c677d;
    margin-bottom: 1.2em;
}

.section-title {
    font-size: 26px;
    font-weight: 700;
    color: #243b55;
    margin-top: 1.2em;
    margin-bottom: 0.7em;
}

.text-card {
    background: linear-gradient(135deg, #ffffff 0%, #f9fbff 100%);
    padding: 24px;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
    border-left: 6px solid #457b9d;
    line-height: 1.75;
    color: #2f3e46;
    font-size: 16px;
}

.advice-card {
    background: linear-gradient(135deg, #ffffff 0%, #f6fffb 100%);
    padding: 24px;
    border-radius: 16px;
    border-left: 6px solid #2a9d8f;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
    margin-top: 12px;
}

.insight-card {
    background: linear-gradient(135deg, #ffffff 0%, #fffaf3 100%);
    padding: 22px;
    border-radius: 16px;
    border-left: 6px solid #f4a261;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
    margin-top: 8px;
    line-height: 1.8;
    color: #33415c;
    font-size: 16px;
}

.mini-note {
    font-size: 14px;
    color: #6c757d;
    margin-bottom: 10px;
}

.year-select-label {
    font-size: 24px;
    font-weight: 500;
    color: #243b55;
    margin-top: 10px;
    margin-bottom: 12px;
    line-height: 1.2;
    letter-spacing: 0.2px;
}

.metric-box {
    background-color: white;
    border-radius: 14px;
    padding: 14px 18px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    border: 1px solid #edf1f7;
    margin-bottom: 10px;
    min-height: 115px;
}

.metric-box-title {
    font-size: 14px;
    color: #6c757d;
    margin-bottom: 4px;
}

.metric-box-value {
    font-size: 22px;
    font-weight: 700;
    color: #1d3557;
}

hr {
    border: none;
    border-top: 1px solid #d9e2ec;
    margin-top: 2em;
    margin-bottom: 1em;
}

/* ===== Tabs container ===== */
.stTabs [data-baseweb="tab-list"] {
    gap: 22px;
    background-color: transparent;
    padding: 6px 0 14px 0;
    border-bottom: none;
    justify-content: flex-start;
    flex-wrap: nowrap;
}

/* ===== Equal width tabs ===== */
.stTabs [data-baseweb="tab-list"] > button {
    flex: 1 1 0 !important;
}

/* ===== Individual tab buttons ===== */
.stTabs [data-baseweb="tab"] {
    height: 54px !important;
    width: 100% !important;
    border-radius: 999px !important;
    padding: 0 24px !important;
    background: #ffffff !important;
    border: 2px solid #dbe4f0 !important;
    color: #355070 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    transition: all 0.2s ease-in-out;
}

/* ===== Force tab text larger ===== */
.stTabs [data-baseweb="tab"] > div {
    font-size: 20px !important;
    font-weight: 500 !important;
    color: #355070 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 100% !important;
    text-align: center !important;
}

/* ===== Force all text inside tab larger ===== */
.stTabs [data-baseweb="tab"] * {
    font-size: 20px !important;
    font-weight: 500 !important;
    color: #355070 !important;
}

/* ===== Hover ===== */
.stTabs [data-baseweb="tab"]:hover {
    color: #1d3557 !important;
    background: #f2f7fd !important;
    border-color: #c9d9ea !important;
    transform: translateY(-1px);
}

/* ===== Selected tab ===== */
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    color: #1d3557 !important;
    background: linear-gradient(135deg, #f4f9ff 0%, #eaf4ff 100%) !important;
    border: 2px solid #bcd3ea !important;
    box-shadow: 0 4px 12px rgba(69, 123, 157, 0.12);
}

/* ===== Focus ===== */
.stTabs [data-baseweb="tab"]:focus {
    outline: none !important;
    box-shadow: 0 0 0 2px rgba(69, 123, 157, 0.18) !important;
}

/* ===== Blue underline ===== */
.stTabs [data-baseweb="tab-highlight"] {
    background-color: #457b9d !important;
    height: 4px !important;
    border-radius: 2px;
}

/* ===== Compact Company Cards ===== */
.company-card {
    background: linear-gradient(135deg, #f8fbff, #eef5fc);
    border: 1px solid #dbe7f3;
    border-radius: 18px;
    padding: 18px 18px 16px 18px;
    box-shadow: 0 4px 14px rgba(31, 78, 121, 0.08);
    min-height: 220px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

.company-card-title {
    font-size: 24px;
    font-weight: 800;
    color: #1d3557;
    margin-bottom: 12px;
}

.company-card-item {
    font-size: 14px;
    color: #33415c;
    line-height: 1.6;
    margin-bottom: 7px;
}

.company-card-label {
    font-weight: 700;
    color: #1d3557;
}

.company-card-tag {
    margin-top: 10px;
    display: inline-block;
    background: #eaf4ff;
    color: #355070;
    font-size: 13px;
    font-weight: 600;
    padding: 6px 12px;
    border-radius: 999px;
}

.suggested-company {
    font-size: 22px;
    font-weight: 700;
    color: #111111;
    margin-bottom: 10px;
}

.advice-text {
    font-size: 16px;
    line-height: 1.7;
    color: #333333;
}

/* ===== Optional: make selectbox area cleaner ===== */
div[data-baseweb="select"] > div {
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# Load Data
# -----------------------
df = pd.read_csv("final_financial_dataset.csv")
df["year"] = df["year"].astype(int)

# -----------------------
# Metric Mapping
# -----------------------
metric_options = {
    "revenue_growth": "Revenue Growth",
    "net_income_growth": "Net Income Growth",
    "roa": "ROA",
    "roe": "ROE",
    "net_profit_margin": "Net Profit Margin",
    "debt_ratio": "Debt Ratio",
    "r_and_d_ratio": "R&D Ratio",
    "capex_ratio": "CAPEX Ratio"
}

# -----------------------
# Metric Preference
# True = higher is better
# False = lower is better
# -----------------------
metric_preference = {
    "revenue_growth": True,
    "net_income_growth": True,
    "roa": True,
    "roe": True,
    "net_profit_margin": True,
    "debt_ratio": False,
    "r_and_d_ratio": True,
    "capex_ratio": True
}

# -----------------------
# Explanations
# -----------------------
metric_explanations = {
    "Revenue Growth": "Revenue growth shows how fast a company is expanding its sales. A higher value usually suggests stronger market demand, successful expansion, or product competitiveness. In the automotive industry, it is especially important for evaluating EV-driven growth and scale expansion.",

    "Net Income Growth": "Net income growth measures how quickly a company’s profit is increasing. It highlights whether revenue growth is being translated into actual earnings. This metric reflects profit quality, cost control, and operational efficiency.",

    "ROA": "ROA (Return on Assets) measures how efficiently a company uses its assets to generate profit. A higher ROA suggests stronger asset utilization and better operating efficiency. It is particularly important in the automotive industry because the sector is highly asset-intensive.",

    "ROE": "ROE (Return on Equity) shows how effectively a company generates returns from shareholders’ equity. A higher ROE often indicates stronger value creation for investors. However, it should be viewed together with debt-related indicators.",

    "Net Profit Margin": "Net profit margin shows how much profit a company keeps from each unit of revenue. A higher margin suggests better profitability, cost control, and pricing power. It is a key indicator of overall business performance.",

    "Debt Ratio": "Debt ratio measures how much of a company’s assets are financed by debt. A lower ratio usually means lower financial risk and greater stability, while a higher ratio suggests heavier reliance on borrowing. This metric is useful for assessing leverage and financial resilience.",

    "R&D Ratio": "R&D ratio shows how much revenue is invested in research and development. A higher ratio often reflects stronger innovation commitment and long-term competitiveness. In the automotive industry, it is especially relevant for EVs, batteries, and smart technologies.",

    "CAPEX Ratio": "CAPEX ratio measures how much revenue is spent on capital investment such as factories, equipment, and production expansion. A higher ratio may indicate stronger future growth planning and capacity building. However, it may also create short-term cash flow pressure."
}
# -----------------------
# Investment Advice
# -----------------------
investment_advice = {
    "Conservative": """
    <div class="suggested-company">Suggested company: Toyota</div>
    <div class="advice-text">
    Toyota may be more suitable for <b>conservative investors</b> because its overall financial profile is generally linked to stronger <b>stability</b> and more consistent <b>profitability</b>. 
    Compared with faster-growing but more volatile firms, Toyota is more likely to appeal to investors who value balanced <b>ROA</b>, <b>ROE</b>, and profit margin performance over time. 
    Its relatively mature business model may also make returns more predictable, which is important for investors focused on <b>capital preservation</b> and lower risk. 
    However, its growth potential may be less aggressive than that of companies more deeply driven by EV expansion.
    </div>
    """,

    "Balanced": """
    <div class="suggested-company">Suggested company: BYD</div>
    <div class="advice-text">
    BYD may be an attractive choice for <b>balanced investors</b> because it combines strong <b>revenue growth</b> with expanding market presence and improving competitive strength in the EV sector. 
    Its performance suggests meaningful growth potential, while its broader industrial base may provide more support than firms that rely mainly on high market expectations. 
    This makes BYD suitable for investors seeking a balance between <b>return potential</b> and a reasonable degree of <b>operational stability</b>. 
    In this sense, BYD may serve as a middle ground between highly stable traditional manufacturers and more volatile innovation-led firms.
    <br><br>
    <b>Additional note:</b> Ford may also be monitored by investors who prefer traditional automakers with possible recovery or transformation potential.
    </div>
    """,

    "Aggressive": """
    <div class="suggested-company">Suggested company: Tesla</div>
    <div class="advice-text">
    Tesla may be more attractive to <b>aggressive investors</b> because its investment profile is more strongly associated with <b>innovation</b>, higher <b>R&D intensity</b>, and growth-oriented expansion. 
    The company may offer greater long-term upside potential, particularly for investors who place more emphasis on future technological leadership and market disruption than on short-term earnings stability. 
    At the same time, this profile may come with higher <b>volatility</b>, meaning returns may be less predictable in the short run. 
    As a result, Tesla is more suitable for investors who are willing to tolerate higher risk in exchange for potentially higher long-term returns.
    </div>
    """
}
# -----------------------
# Company Profiles
# -----------------------
company_profiles = {
    "BYD": {
        "country": "China",
        "founded": "1995",
        "focus": "EVs & batteries",
        "strength": "Vertical integration"
    },
    "Toyota": {
        "country": "Japan",
        "founded": "1937",
        "focus": "Autos & hybrids",
        "strength": "Operational stability"
    },
    "Tesla": {
        "country": "USA",
        "founded": "2003",
        "focus": "EVs & energy",
        "strength": "Innovation leadership"
    },
    "Ford": {
        "country": "USA",
        "founded": "1903",
        "focus": "Autos & mobility",
        "strength": "Manufacturing legacy"
    }
}

# -----------------------
# Header
# -----------------------
st.markdown('<div class="main-title">📊 Automotive Financial Insights Dashboard</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">A comparative analysis of BYD, Toyota, Tesla, and Ford using key financial ratios, trend visualization, and investor-oriented insights.</div>',
    unsafe_allow_html=True
)

# -----------------------
# Company Profiles
# -----------------------
st.markdown('<div class="section-title">Company Profiles</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="mini-note">A quick snapshot of the four automotive companies in this dashboard.</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

company_list = list(company_profiles.items())
cols = [col1, col2, col3, col4]

for col, (company, profile) in zip(cols, company_list):
    with col:
        st.markdown(f"""
        <div class="company-card">
            <div class="company-card-title">{company}</div>
            <div class="company-card-item"><span class="company-card-label">Country:</span> {profile["country"]}</div>
            <div class="company-card-item"><span class="company-card-label">Founded:</span> {profile["founded"]}</div>
            <div class="company-card-item"><span class="company-card-label">Focus:</span> {profile["focus"]}</div>
            <div class="company-card-tag">{profile["strength"]}</div>
        </div>
        """, unsafe_allow_html=True)

# -----------------------
# Sidebar
# -----------------------
st.sidebar.header("Filter Options")

selected_companies = st.sidebar.multiselect(
    "Select Companies",
    options=df["company"].unique(),
    default=df["company"].unique()
)

selected_years = st.sidebar.multiselect(
    "Select Years",
    options=sorted(df["year"].unique()),
    default=sorted(df["year"].unique())
)

# -----------------------
# Metric Categories
# -----------------------
metric_categories = {
    "Growth": ["revenue_growth", "net_income_growth"],
    "Profitability": ["roa", "roe", "net_profit_margin"],
    "Risk / Leverage": ["debt_ratio"],
    "Investment / Innovation": ["r_and_d_ratio", "capex_ratio"]
}

# -----------------------
# Main Page Category + Ratio Selector
# -----------------------
st.markdown('<div class="section-title">Explore Financial Ratios</div>', unsafe_allow_html=True)

col_cat, col_ratio, _ = st.columns([1, 1, 1.2])

with col_cat:
    selected_category = st.selectbox(
        "Choose a Category",
        options=list(metric_categories.keys())
    )

with col_ratio:
    selected_metric_key = st.selectbox(
        "Choose a Financial Ratio",
        options=metric_categories[selected_category],
        format_func=lambda x: metric_options[x]
    )

selected_label = metric_options[selected_metric_key]

# -----------------------
# Filter Data
# -----------------------
filtered_df = df[
    (df["company"].isin(selected_companies)) &
    (df["year"].isin(selected_years))
].copy()

# -----------------------
# Empty Data Check
# -----------------------
if filtered_df.empty:
    st.warning("No data available for the selected filters. Please adjust your company or year selection.")
    st.stop()

# -----------------------
# KPI Calculations
# -----------------------
avg_value = filtered_df[selected_metric_key].mean()

higher_is_better = metric_preference[selected_metric_key]

company_avg = filtered_df.groupby("company")[selected_metric_key].mean().sort_values(
    ascending=not higher_is_better
)
top_performer = company_avg.index[0]

company_std = filtered_df.groupby("company")[selected_metric_key].std().fillna(0).sort_values()
most_stable = company_std.index[0]

latest_year = filtered_df["year"].max()
latest_df = filtered_df[filtered_df["year"] == latest_year]

latest_company_avg = latest_df.groupby("company")[selected_metric_key].mean().sort_values(
    ascending=not higher_is_better
)
latest_leader = latest_company_avg.index[0]

# -----------------------
# Dashboard Snapshot
# -----------------------
st.markdown('<div class="section-title">Dashboard Snapshot</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
        <div class="metric-box">
            <div class="metric-box-title">Average Value</div>
            <div class="metric-box-value">{avg_value:.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
        <div class="metric-box">
            <div class="metric-box-title">Best Performer</div>
            <div class="metric-box-value">{top_performer}</div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
        <div class="metric-box">
            <div class="metric-box-title">Most Stable Company</div>
            <div class="metric-box-value">{most_stable}</div>
        </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
        <div class="metric-box">
            <div class="metric-box-title">Latest Year Leader ({latest_year})</div>
            <div class="metric-box-value">{latest_leader}</div>
        </div>
    """, unsafe_allow_html=True)

# -----------------------
# Financial Ratio Overview
# -----------------------
st.markdown('<div class="section-title">Financial Ratio Overview</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.75, 1])

with col1:
    company_order = ["BYD", "Toyota", "Tesla", "Ford"]

    pivot_df = filtered_df.pivot(
        index="year",
        columns="company",
        values=selected_metric_key
    ).sort_index()

    pivot_df = pivot_df.reindex(columns=[c for c in company_order if c in pivot_df.columns])

    st.markdown(
        f"""
        <style>
        .ratio-table-title{{
            width:85%;
            margin: 0 0 10px 0;
            font-size:24px;
            font-weight:700;
            color:#2b2d42;
            text-align:left;
        }}
        .ratio-table-wrap{{
            width:85%;
            margin: 0;
        }}
        .ratio-row{{
            display:grid;
            grid-template-columns: repeat({len(["Year"] + list(pivot_df.columns))}, 1fr);
            background:#ffffff;
        }}
        .ratio-head{{
            background:#f8fbff;
        }}
        .ratio-cell{{
            border:1px solid #e6ecf3;
            padding:18px 12px;
            text-align:center;
            color:#1d3557;
            font-size:24px;
            font-weight:900;
        }}
        .ratio-head .ratio-cell{{
            font-size:18px;
            color:#355070;
            font-weight:400;
        }}
        .ratio-year{{
            font-weight:400 !important;
        }}
        </style>

        <div class="ratio-table-title">{selected_label} Table</div>
        """,
        unsafe_allow_html=True
    )

    cols = ["Year"] + list(pivot_df.columns)

    html = '<div class="ratio-table-wrap">'
    html += '<div class="ratio-row ratio-head">'
    for c in cols:
        html += f'<div class="ratio-cell">{c}</div>'
    html += '</div>'

    for year, row in pivot_df.iterrows():
        html += '<div class="ratio-row">'
        html += f'<div class="ratio-cell ratio-year">{year}</div>'
        for val in row:
            if pd.isna(val):
                html += '<div class="ratio-cell">-</div>'
            else:
                html += f'<div class="ratio-cell">{val:.2f}</div>'
        html += '</div>'

    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

with col2:
    st.subheader(f"{selected_label} Interpretation")
    st.markdown(f"""
        <div class="text-card">
            {metric_explanations[selected_label]}
        </div>
    """, unsafe_allow_html=True)

# -----------------------
# Analysis Modules in Tabs
# -----------------------
st.markdown('<div class="section-title">Analysis Modules</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="mini-note">Click different tabs to explore trend analysis, year-specific comparison, and dynamic insights.</div>',
    unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs([
    "📈 Trends",
    "📊 Comparison",
    "🧠 Insights"
])

# -----------------------
# Tab 1: Trends
# -----------------------
with tab1:
    st.markdown(
        '<div class="mini-note">Compare the year-by-year movement of the selected financial ratio across the chosen companies.</div>',
        unsafe_allow_html=True
    )

    company_order = ["BYD", "Toyota", "Tesla", "Ford"]

    company_color_map = {
        "BYD": "#263a59",
        "Toyota": "#5b84a1",
        "Tesla": "#3c9d8f",
        "Ford": "#d07a61"
    }

    left_spacer, center_col, right_spacer = st.columns([0.1, 0.8, 0.1])

    line_df = filtered_df.copy()
    line_df["company"] = pd.Categorical(
        line_df["company"],
        categories=company_order,
        ordered=True
    )
    line_df = line_df.sort_values(["company", "year"])

    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(9, 5))

    sns.lineplot(
        data=line_df,
        x="year",
        y=selected_metric_key,
        hue="company",
        hue_order=company_order,
        marker="o",
        linewidth=2.6,
        markersize=8,
        palette=company_color_map,
        ax=ax
    )

    ax.set_title(
        f"{selected_label} Trend by Company",
        fontsize=17,
        pad=16,
        fontweight="bold",
        color="#2b2d42"
    )
    ax.set_xlabel("Year", fontsize=12.5, fontweight="semibold", color="#33415c")
    ax.set_ylabel(selected_label, fontsize=12.5, fontweight="semibold", color="#33415c")

    year_ticks = sorted(filtered_df["year"].unique())
    ax.set_xticks(year_ticks)
    ax.set_xticklabels([str(y) for y in year_ticks])

    ax.grid(True, linestyle="--", alpha=0.25)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#c7d0d9")
    ax.spines["bottom"].set_color("#c7d0d9")

    ax.tick_params(axis="x", labelsize=11, colors="#495057")
    ax.tick_params(axis="y", labelsize=11, colors="#495057")

    ax.legend(
        title="Company",
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
        frameon=False
    )

    plt.tight_layout()

    with center_col:
        st.pyplot(fig)

# -----------------------
# Tab 2: Comparison
# -----------------------
with tab2:
    st.markdown(
        '<div class="mini-note">Select one year to compare how companies perform on the chosen financial ratio in the same period.</div>',
        unsafe_allow_html=True
    )

    left_spacer, center_col, right_spacer = st.columns([0.1, 0.8, 0.1])

    with center_col:
        st.markdown(
            '<div class="year-select-label">Select a year for comparison</div>',
            unsafe_allow_html=True
        )

        select_col, _ = st.columns([0.32, 0.78])

        with select_col:
            selected_year_for_bar = st.selectbox(
                "Select a year for comparison",
                options=sorted(filtered_df["year"].unique()),
                key="year_bar_tab",
                label_visibility="collapsed"
            )

        company_order = ["BYD", "Toyota", "Tesla", "Ford"]

        company_color_map = {
            "BYD": "#263a59",
            "Toyota": "#5b84a1",
            "Tesla": "#3c9d8f",
            "Ford": "#d07a61"
        }

        bar_df = filtered_df[filtered_df["year"] == selected_year_for_bar].copy()

        bar_df["company"] = pd.Categorical(
            bar_df["company"],
            categories=company_order,
            ordered=True
        )
        bar_df = bar_df.sort_values("company")

        fig2, ax2 = plt.subplots(figsize=(9, 5))

        sns.barplot(
            data=bar_df,
            x="company",
            y=selected_metric_key,
            hue="company",
            order=company_order,
            hue_order=company_order,
            palette=company_color_map,
            dodge=False,
            legend=False,
            ax=ax2
        )

        ax2.set_title(
            f"{selected_label} Comparison in {selected_year_for_bar}",
            fontsize=17,
            pad=16,
            fontweight="bold",
            color="#2b2d42"
        )
        ax2.set_xlabel("Company", fontsize=12.5, fontweight="semibold", color="#33415c")
        ax2.set_ylabel(selected_label, fontsize=12.5, fontweight="semibold", color="#33415c")

        ax2.grid(True, axis="y", linestyle="--", alpha=0.25)
        ax2.set_axisbelow(True)
        ax2.spines["top"].set_visible(False)
        ax2.spines["right"].set_visible(False)
        ax2.spines["left"].set_color("#c7d0d9")
        ax2.spines["bottom"].set_color("#c7d0d9")

        ax2.tick_params(axis="x", labelsize=11, colors="#495057")
        ax2.tick_params(axis="y", labelsize=11, colors="#495057")

        y_values = bar_df[selected_metric_key].dropna()
        if len(y_values) > 0:
            y_min = y_values.min()
            y_max = y_values.max()
            y_range = y_max - y_min

            if y_range == 0:
                padding = max(abs(y_max) * 0.2, 0.5)
            else:
                padding = y_range * 0.18

            ax2.set_ylim(y_min - padding, y_max + padding)

        for patch in ax2.patches:
            height = patch.get_height()
            x = patch.get_x() + patch.get_width() / 2

            if pd.notna(height):
                if height >= 0:
                    ax2.annotate(
                        f"{height:.2f}",
                        (x, height),
                        ha="center",
                        va="bottom",
                        fontsize=10,
                        fontweight="semibold",
                        color="#555",
                        xytext=(0, 4),
                        textcoords="offset points"
                    )
                else:
                    ax2.annotate(
                        f"{height:.2f}",
                        (x, height),
                        ha="center",
                        va="top",
                        fontsize=10,
                        fontweight="semibold",
                        color="#555",
                        xytext=(0, -4),
                        textcoords="offset points"
                    )

        plt.tight_layout()
        st.pyplot(fig2)

# -----------------------
# Tab 3: Insights
# -----------------------
with tab3:
    top_avg_company = company_avg.index[0]
    top_avg_value = company_avg.iloc[0]

    most_stable_company = company_std.index[0]
    most_stable_value = company_std.iloc[0]

    latest_leader_value = latest_company_avg.iloc[0]

    avg_direction_text = "highest" if higher_is_better else "lowest"
    latest_direction_text = "highest" if higher_is_better else "lowest"

    st.markdown(f"""
    <div class="insight-card">
        <b>Key findings for {selected_label}:</b><br><br>
        • <b>{top_avg_company}</b> shows the <b>{avg_direction_text}</b> average <b>{selected_label}</b> across the selected period, with an average value of <b>{top_avg_value:.2f}</b>.<br>
        • <b>{most_stable_company}</b> appears to be the most stable company, with the lowest variation in this metric (standard deviation = <b>{most_stable_value:.2f}</b>).<br>
        • In the most recent selected year (<b>{latest_year}</b>), <b>{latest_leader}</b> leads the group with the <b>{latest_direction_text}</b> value of approximately <b>{latest_leader_value:.2f}</b>.<br>
    </div>
    """, unsafe_allow_html=True)

# -----------------------
# Investment Suggestions
# -----------------------
st.markdown('<div class="section-title">Investment Suggestions</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="mini-note">Select an investor profile to view the most relevant suggestion.</div>',
    unsafe_allow_html=True
)

invest_tab1, invest_tab2, invest_tab3 = st.tabs([
    "Conservative",
    "Balanced",
    "Aggressive"
])

with invest_tab1:
    st.markdown(f"""
    <div class="advice-card">
        <h4>Conservative Investor</h4>
        <p>{investment_advice["Conservative"]}</p>
    </div>
    """, unsafe_allow_html=True)

with invest_tab2:
    st.markdown(f"""
    <div class="advice-card">
        <h4>Balanced Investor</h4>
        <p>{investment_advice["Balanced"]}</p>
    </div>
    """, unsafe_allow_html=True)

with invest_tab3:
    st.markdown(f"""
    <div class="advice-card">
        <h4>Aggressive Investor</h4>
        <p>{investment_advice["Aggressive"]}</p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------
# Download Filtered Data
# -----------------------
st.markdown('<div class="section-title">Download Filtered Data</div>', unsafe_allow_html=True)

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download current filtered data as CSV",
    data=csv,
    file_name="filtered_financial_data.csv",
    mime="text/csv"
)

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.caption("Dashboard created with Streamlit for financial ratio comparison and investor insight presentation.")