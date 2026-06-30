Scout Data Pipeline: Football scouting engine
Este projeto nasceu da necessidade de criar um sistema próprio para análise de dados de futebol, saindo da teoria e construindo um motor de busca de talentos que realmente funciona. A ideia surgiu da busca por transformar dados brutos em inteligência, permitindo filtrar jogadores por perfis específicos (os "pilares" do jogo) sem depender de ferramentas fechadas.

O Processo de Construção
A construção foi feita "na raça", em um processo de desenvolvimento orientado a objetos. A lógica central foi separar o sistema em camadas, onde cada módulo tem uma única responsabilidade. Não queríamos apenas um código que funcionasse, mas uma arquitetura de dados escalável.

O processo incluiu:

Modelagem de Classes: Criação do MetricsEngine (o Maestro), SearchEngine (o Motor) e DataLoader (o Carregador).

Limpeza de Dados: Luta contra caracteres invisíveis e formatação de CSV.

Pandas no Core: Substituição de loops manuais por Máscaras Booleanas, ganhando performance e clareza.

Visão de Futuro: O código foi desenhado para que, no futuro, a conexão com APIs como a do StatsBomb seja apenas uma questão de adaptar o DataLoader, sem tocar no motor de busca.

Estrutura do Projeto
O projeto está organizado para facilitar a manutenção e a expansão:

Plaintext
scout_futebol_mvp/
├── src/
│   ├── __main__.py          # O orquestrador: liga todas as pontas
│   ├── data_loader.py       # Gerencia a leitura do banco de dados (CSV)
│   ├── metrics_engine.py    # Validador: garante que só filtramos o que existe
│   └── search_engine.py     # O motor de busca: aplica filtros e ordena dados
├── players_data.csv         # Banco de dados de teste (Amostra estatística)
└── README.md
Como funciona (As Peças)
DataLoader: A ponte com o arquivo. Ele lê o CSV e limpa os nomes das colunas.

MetricsEngine: O "Maestro". Ele registra as colunas disponíveis e valida se o que você pediu no main realmente existe no banco, evitando erros antes de processar.

SearchEngine: O braço operacional. Recebe o dicionário de filtros e usa o poder do Pandas para filtrar e ordenar os atletas.

Banco de Dados
Para testar, criamos um banco de dados sintético (players_data.csv) com 20 jogadores por posição, totalizando uma amostra diversa para validar os filtros de pressão, passes progressivos e desarmes.

Nota: O sistema está pronto para ser conectado a bases de dados reais. A transição de um arquivo local para um banco SQL ou uma API (como a do StatsBomb) exige apenas a alteração do DataLoader. O restante do sistema (filtros e métricas) permanece intacto.

Próximos Passos
Este é apenas o MVP. O roadmap de evolução inclui:

Conexão direta com a API da StatsBomb para importar dados reais de partidas.

Implementação de fórmulas de cálculo (os 7 pilares) para normalizar métricas de 0 a 10.

Integração com interface web usando Streamlit.

Desenvolvido como um agente de IA para automação de análise de dados no futebol.
