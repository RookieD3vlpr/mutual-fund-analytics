import pandas as pd

def get_recommendations(risk_appetite):
    print(f"\n🔍 Generating Top 3 Recommendations for Risk Profile: {risk_appetite.upper()}...\n")
    
    try:
        # Load the scorecard you generated on Day 4
        df_scores = pd.read_csv('reports/fund_scorecard.csv')
        df_funds = pd.read_csv('data/processed/clean_fund_master.csv')
        
        df_merged = df_scores.merge(df_funds[['amfi_code', 'risk_category', 'category']], on='amfi_code')
        
        # Filter by requested risk grade
        matching_funds = df_merged[df_merged['risk_category'].str.lower() == risk_appetite.lower()]
        
        if matching_funds.empty:
            print("⚠️ No funds matched this exact risk profile.")
            return
            
        # Sort by Sharpe Ratio to find the optimal risk-adjusted returns
        top_3 = matching_funds.sort_values(by='sharpe_ratio', ascending=False).head(3)
        
        print("-" * 70)
        print(f"{'Scheme Name':<45} | {'Category':<10} | {'Sharpe'}")
        print("-" * 70)
        
        for _, row in top_3.iterrows():
            print(f"{row['scheme_name']:<45} | {row['category']:<10} | {row['sharpe_ratio']:.2f}")
            
        print("-" * 70)
        
    except FileNotFoundError:
        print("Error: Required dataset 'fund_scorecard.csv' not found.")

if __name__ == "__main__":
    print("Welcome to the BlueStock Mutual Fund Recommender Engine")
    while True:
        user_input = input("Enter Risk Appetite (Low / Moderate / High) or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        if user_input.lower() in ['low', 'moderate', 'high']:
            get_recommendations(user_input)
        else:
            print("Invalid input. Please enter Low, Moderate, or High.")