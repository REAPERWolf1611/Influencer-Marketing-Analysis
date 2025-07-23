# HealthKart Influencer Dashboard

This repository contains an interactive dashboard project that analyzes influencer marketing campaigns for HealthKart. The dashboard visualizes campaign ROI, platform performance, product orders, influencer engagement, and payout structures.

> ⚠️ **Note:** All data used in this project is simulated and does not reflect real HealthKart campaigns or influencer performance.


## 📊 Project Overview

The goal of this project is to simulate, track, and analyze the ROI of influencer campaigns across platforms like Instagram, YouTube, and Twitter for HealthKart brands such as MuscleBlaze, HKVitals, and Gritzo.

The dashboard is divided into two pages:

- **Page 1: Campaign Performance & ROI Overview**
  - Key KPIs: Total Revenue, Total Spend, ROAS, ROI, and Orders
  - Campaign- and product-level insights
  - Revenue and order comparisons across platforms, sources, and time

- **Page 2: Influencer & Engagement Insights**
  - Top and bottom influencers by revenue
  - Monthly revenue trends
  - Engagement metrics (reach, likes, comments)
  - Payout structure and platform breakdown

---

## 📁 Files Included

- `influencers.csv` – Influencer details (name, category, platform, follower count)
- `posts.csv` – Post performance data (reach, likes, comments)
- `tracking_data.csv` – Revenue and order tracking by influencer and campaign
- `payouts.csv` – Influencer payment logic and computed spend
- `Generated Data.py` – Python script to simulate the dataset using Faker & Pandas
- `Influencer Marketing Analysis.pbix` - PowerBI dashboard 

> ⚠️ **Disclaimer:** All data is synthetically generated for academic and demonstration purposes only.

---

## 🛠 Tools Used

- **Power BI** for dashboard creation and data modeling
- **Python (Pandas, Faker)** for generating 1000-row simulated datasets
- **Excel** for early exploration and data formatting

---

## 📈 Key Insights

- Overall ROAS was **0.84×**, with a negative ROI of **-0.16**, highlighting inefficient spend.
- Instagram and the **PowerBoost** campaign led in revenue performance.
- **Vitamin C** and **Creatine** were top products in both orders and revenue.
- Most payouts were **order-based (91%)**, though some high-spend influencers underperformed.
- **Engagement** (reach and likes) was highest on Twitter and YouTube.
- Revenue peaked in **May**, followed by a steady decline.

---
