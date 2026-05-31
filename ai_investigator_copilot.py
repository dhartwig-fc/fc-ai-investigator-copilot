import streamlit as st

st.set_page_config(page_title="AI Investigator Copilot")

st.title("🕵️ AI Investigator Copilot")

st.header("Alert Summary")

st.write("Customer: Delta Commodities")

st.write("Risk Score: 145")

st.write("Priority: HIGH")

st.header("Risk Drivers")

st.write("""
• High-risk jurisdiction

• Transaction exceeds historical average

• New counterparty

• Adverse media identified

• Network relationship risk
""")

st.header("Recommended Actions")

st.write("""
✓ Review KYC

✓ Validate commercial rationale

✓ Enhanced due diligence

✓ Escalate for investigator review
""")


