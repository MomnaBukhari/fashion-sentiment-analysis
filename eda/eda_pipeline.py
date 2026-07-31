# .............................................
# Main EDA pipeline.
# Loads feature engineered dataset,
# performs statistical analysis,
# and generates visualizations.
# .............................................


import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)


from preprocessing.load_data import DataLoader
from config.paths import FEATURE_DATA, STATS_DATA_DIR

from eda.statistical_analysis import StatisticalAnalysis
from eda.visualization import Visualizer



# Output folder for plots

EDA_OUTPUT = (
    PROJECT_ROOT /
    "data" /
    "eda_results"
)



def main():


    print("\nLoading feature dataset...")


    loader = DataLoader(
        FEATURE_DATA
    )


    df = loader.load_csv()


    print(
        f"Rows loaded: {len(df)}"
    )


    print(
        f"Columns loaded: {len(df.columns)}"
    )



    # -----------------------------
    # Statistical Analysis
    # -----------------------------


    statistics = StatisticalAnalysis(
        df
    )


    statistics.save_statistics(
        STATS_DATA_DIR
    )



    # -----------------------------
    # Visualization
    # -----------------------------


    EDA_OUTPUT.mkdir(
        exist_ok=True
    )


    visualizer = Visualizer(
        df,
        EDA_OUTPUT
    )


    visualizer.plot_language_distribution()


    visualizer.plot_multilingual_distribution()


    visualizer.plot_engagement_distribution()



    print(
        "\nEDA completed successfully."
    )


    print(
        f"Results saved at: {EDA_OUTPUT}"
    )



if __name__ == "__main__":

    main()