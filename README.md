# Automotive-Financial-Insights-Dashboard-
A comparative analysis of BYD, Toyota, Tesla, and Ford using key financial ratios, trend visualization, and investor-oriented insights.

---

## 1. Problem & User
This project provides an interactive financial analysis tool for four major automotive companies: BYD, Toyota, Tesla, and Ford.
It helps different types of investors understand profitability, risk, and growth potential, and make more informed investment decisions.

---

## 2. Data
**Source**: WRDS    
**Access date**: 15 April 2026  
**Key fields**: revenue growth, net income growth, ROA, ROE, net profit margin, debt ratio, R&D ratio, CAPEX ratio, year, company  
**Dataset file**: final_financial_dataset.csv  

---

## 3. Methods
1. Extract raw financial data from WRDS using Python in Jupyter Notebook
2. Clean and standardize data (rename fields, check missing values, filter years/companies)
3. Calculate key financial ratios for profitability, risk, growth and investment
4. Export cleaned dataset to CSV for visualization
5. Build interactive dashboard with Streamlit
6. Add trend analysis, year-on-year comparison and automatic key insights
7. Implement personalized investment suggestions for three investor profiles

---

## 4. Key Findings
Toyota shows strong operational stability and consistent profitability, suitable for conservative investors.  
BYD balances strong revenue growth with expanding market share, ideal for balanced investors.  
Tesla leads in innovation and R&D intensity, offering high long-term growth potential for aggressive investors.  
Each company has distinct strengths in stability, growth, or innovation.  

---

## 5. How to run
1. Install required packages:
   `pip install streamlit pandas matplotlib seaborn`
2. Ensure final_financial_dataset.csv is in the same folder as app.py
3. Run the app:
   `streamlit run app.py`

---

## 6. Product link / Demo
 GitHub Repository: https://github.com/jessicaaa729/Automotive-Financial-Insights-Dashboard-  
 Product link: https://automotive-financial-insights-dashboard.streamlit.app/  
 Demo Video: https://video.xjtlu.edu.cn/Mediasite/MyMediasite/embedded/presentations/083f96f507534702919a6c4d10bd893a1d  

---

## 7. Limitations & next steps
The dataset only covers 3 years, limiting long-term trend analysis.
External factors such as market policy, competition, and macroeconomic conditions are not included.
Future improvements could include adding more companies, real-time data updates, and predictive analysis.
