import pandas as pd
from data_loader import DataLoader
from metrics_engine import MetricsEngine
from search_engine import SearchEngine


def main():

    loader = DataLoader("players_data.csv")
    df = loader.load_data()

    if df is not None:

        df.columns = df.columns.str.strip()

        metrics = MetricsEngine()
        metrics.load_available_attributes(df)


        print("DEBUG: Colunas reais no banco:", [str(c).strip() for c in df.columns])
        print("Atributos disponíveis:")
        metrics.list_available_attributes()
        print("-" * 30)


        user_choices = {
            "progressive_pass_p90": 7.0,
            "pressure_regain_p90": 6.0
        }


        choices = metrics.filter_by_metrics(user_choices)

        if choices:

            search = SearchEngine(df)

            search.apply_filters(choices)
            search.sort_results(sort_by="progressive_pass_p90", ascending=False)

            print("\nJogadores encontrados:")
            print(search.get_summary())
        else:
            print("Erro: As métricas escolhidas não são válidas.")
    else:
        print("Erro: Não foi possível carregar os dados do arquivo.")


if __name__ == "__main__":
    main()