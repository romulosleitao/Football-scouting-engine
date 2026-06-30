
class MetricsEngine:
    def __init__(self,metric_registry=None):
        if metric_registry is None:
            self.metric_registry = {}
        else:
            self.metric_registry = metric_registry

    def load_available_attributes(self, data_frame):
        self.metric_registry = list(data_frame.columns)
        return self.metric_registry

    def list_available_attributes(self):
        for atributo in self.metric_registry:
            print (f'Disponivel: {atributo}')

    def filter_by_metrics(self, user_choices):

        print(f"DEBUG: Métricas registradas no sistema: {self.metric_registry}")

        for chave in user_choices.keys():

            if chave not in self.metric_registry:
                print(f"erro: {chave} não existe no banco de dados")
                return None
        return user_choices