import streamlit as st
import pandas as pd
from PIL import Image
from utilidades.const import TITULO_ANALISE_EXPLORATORIA, TITULO_PRINCIPAL
from utilidades.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_ANALISE_EXPLORATORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    with open("assets/historia.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    st.header(f":green[{TITULO_ANALISE_EXPLORATORIA}]")
    st.markdown(
        """
    O **:green[Índice de Desenvolvimento Educacional (INDE)]** é uma medida síntese que avalia o desempenho dos alunos da Associação Passos Mágicos com base em três dimensões principais: acadêmica, psicossocial e psicopedagógica. Essas dimensões são analisadas por meio de sete indicadores: **:green[IAN, IDA, IEG, IAA, IPS, IPP e IPV]** que, ponderados, formam o índice final. Cada indicador reflete aspectos distintos do desenvolvimento dos alunos, permitindo uma visão abrangente do progresso educacional.

    Nesta análise, gostaríamos de dar ênfase maior a métrica do :green[Ponto de virada] partindo pela lógica de que esta métrica indicaria o estágio em que o aluno está totalmente integrado com os valores da insituição. Separando assim os alunos em dois grupos, os que :green[atingiram o Ponto de virada] e os alunos que ainda :green[não atingiram o ponto de virada.]  




        """
    )

tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, = st.tabs(
    tabs=[
        "Ponto de virada",
        "INDE",
        "Pedras",
        "Indicador de Aprendizagem",
        "Indicador de Engajamento",
        "Indicador de Adequação ao nível",
        "Indicador de Auto avaliação",
        "Indicador Psicossocial",
        "Indicador Psicopedagógico",
        "Indicador de Ponto de virada",
    ]
)

with tab0:
    st.subheader("Análise Ponto de virada")
    st.markdown(
        """
O Ponto de Virada representa um marco importante no desenvolvimento dos alunos da Associação Passos Mágicos. Ele reflete um estágio em que o aluno demonstra, de forma ativa e contínua, a conscientização sobre o valor da educação e a importância do aprendizado para sua trajetória pessoal e acadêmica. 

Alcançar esse ponto significa que o aluno está integrado aos valores e princípios da associação, e, além disso, demonstra uma maturidade emocional e acadêmica que lhe permite aproveitar as novas oportunidades de aprendizado que surgem. 

Ele :green[não é um ponto final], mas o início de uma transformação significativa na vida do aluno. Esse momento marca o começo de uma mudança significativa em suas atividades educacionais e de socialização, a Associação Passos Mágicos oferece uma estrutura de aprendizado e convivência que cria as condições ideais para que os alunos alcancem esse ponto de viradaa metodologia desenvolvida para o :green[Índice do Ponto de Virada (IPV)] é baseada em uma avaliação objetiva e homogênea. 

Um aluno atinge o ponto de virada quando sua :green[nota IPV é igual ou maior que a média da nota IPV de todos os alunos, acrescida de um desvio padrão.] Esse valor varia a cada avaliação, dependendo do desempenho de todos os alunos no momento em que o cálculo é realizado. 

Com base no gráfico que mostra a evolução do número de alunos que atingiram o :green[Ponto de Virada entre 2020 e 2022], podemos observar uma tendência de crescimento consistente. Esse aumento indica uma evolução positiva no desempenho e no engajamento dos alunos com o programa da associação. A tendência de crescimento sugere que as estratégias adotadas pela ONG estão funcionando e contribuindo para o desenvolvimento acadêmico e emocional dos estudantes.

        """)
    
    st.divider()

    image_path = 'assets/imgs/atingiram_pv.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por idade', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab1:
    st.subheader("Análise Índice do Desenvolvimento Educacional")
    st.markdown(
        """
O gráfico apresentado compara a :green[variação da média do INDE] entre os alunos que atingiram o Ponto de Virada (em azul) e aqueles que não atingiram (em vermelho), nos :green[anos de 2020, 2021 e 2022]. 

Os alunos que atingem o Ponto de Virada mantêm um desempenho significativamente mais elevado ao longo dos anos, enquanto os alunos que atingiram o IPV mostram apenas uma pequena queda, os que não atingiram sofreram uma queda acentuada no INDE, especialmente de 2020 para 2021.

Essas diferenças ressaltam a importância de iniciativas pedagógicas focadas em aumentar o número de alunos que atingem o Ponto de Virada, pois isso está diretamente relacionado a melhores resultados no INDE ao longo dos anos.

        """)
    
    st.divider()

    image_path = 'assets/imgs/inde_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por fase', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.subheader("Análise Pedras")
    st.markdown(
        """
Podemos classificar os alunos com base no desempenho do INDE, em quatro faixas, aplicáveis tanto aos resultados gerais quanto aos grupos de alunos universitários, do ensino médio e fundamental.

Essas faixas refletem a posição de cada aluno em relação ao desempenho total obtido na avaliação PEDE durante os anos, correspondendo aos conceitos Ametista, Ágata, Quartzo e Topázio.

Essas classificações permitem atribuir significados ao processo de avaliação, de acordo com os objetivos da Associação e sua visão educacional, em conformidade com os princípios de uma educação eficaz, respaldada por teorias pedagógicas. 

O gráfico indica a variação da quantidade de alunos de acordo com cada pedra ao passar dos anos. O conceito de classificação e dado por: 

- Quartzo = :green[2,405] a :green[5,506]

- Ágata = :green[5,506] a :green[6,868]

- Ametista = :green[6,868] a :green[8,230]

- Topázio = :green[8,230] a :green[9,294.]

        """)
    
    st.divider()

    image_path = 'assets/imgs/pedra_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por tipo de instituição', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.subheader("Análise IDA")
    st.markdown(
        """
O Indicador de Desempenho Acadêmico (IDA) é uma medida que avalia a dimensão acadêmica, refletindo os resultados das avaliações dos alunos da Associação Passos Mágicos em provas padronizadas ou em seus registros curriculares.

Os alunos em fase escolar, participantes do Programa de Aceleração do Conhecimento da Associação, realizam :green[duas provas padronizadas anuais em cada disciplina (Matemática, Português e Inglês)], abrangendo as Fases 0 a 7. 

A partir dessas provas, são analisados dois aspectos principais: :green[o sentido da variação e a magnitude da nota.] O sentido da variação observa se houve melhora, piora ou estabilidade no desempenho do aluno ao longo das avaliações. Já a magnitude compara o desempenho do aluno com o de seus colegas.

A nota final de cada disciplina é calculada levando em conta esses dois elementos, e o :green[IDA final corresponde à média das notas obtidas em todas as disciplinas.] 

O gráfico compara a média das notas IDA entre os alunos que atingiram ou não o ponto de virada. Esse comportamento reflete a diferença de evolução acadêmica entre os dois grupos, destacando que os alunos que atingiram o Ponto de Virada mantiveram um desempenho mais consistente ao longo dos anos. Já os que não atingiram mostraram uma queda significativa em 2021, com recuperação parcial no ano seguinte.
        
        """)
    
    st.divider()

    image_path = 'assets/imgs/ida_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab4:
    st.subheader("Análise IEG")
    st.markdown(
        """
O Indicador de Engajamento (IEG) mede o envolvimento dos alunos em diferentes atividades. Para os universitários, ele reflete a :green[participação em iniciativas de voluntariado], enquanto para os estudantes em fase escolar, o foco é na :green[entrega das tarefas do Programa de Aceleração do Conhecimento]. 

Esse indicador é gerado com base nos registros feitos pela equipe pedagógica, que levantou a participação em ambas as atividades e as converteu em um percentual. Posteriormente, esse percentual é transformado em uma nota padronizada, variando de 0 a 10. 

O gráfico apresentado compara a variação da média do Indicador de Engajamento (IEG) entre os alunos que atingiram o ponto de virada e os que não atingiram, nos anos de 2020, 2021 e 2022. A análise sugere que o engajamento contínuo é um fator importante para :green[alcançar o ponto de virada], já que aqueles que se engajam mais consistentemente apresentam resultados melhores ao longo do tempo. 

Para os alunos que atingiram o ponto de virada (linha azul), a média do IEG começa em torno de 9.0 em 2020 e, embora haja uma pequena queda em 2021, ela se mantém relativamente alta, voltando a subir levemente em 2022. Isso indica um alto nível de engajamento ao longo dos anos, mesmo com pequenas flutuações. Já para os alunos que não atingiram o ponto de virada (linha vermelha), observa-se uma queda significativa na média do IEG entre 2020 e 2021, caindo de aproximadamente 8.0 para 6.5. No entanto, em 2022, há uma recuperação, com a média subindo novamente para 7.5.
        """)
    
    st.divider()
    
    image_path = 'assets/imgs/ieg_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab5:
    st.subheader("Análise IAN")
    st.markdown(
        """
O Indicador de Adequação de Nível (IAN) avalia o :green[desempenho acadêmico dos alunos], funcionando como uma medida individual gerada a partir dos processos avaliativos usados para monitorar o progresso educacional de cada estudante na associação. Esse indicador busca refletir o quanto o aluno está :green[adequado à fase de ensino] em que foi alocado no ano específico, permitindo uma análise precisa de sua evolução em relação ao nível de ensino esperado. 

O gráfico comparando a variação da média do IAN mostra que o grupo que atingiu o ponto de virada começou com uma pontuação IAN mais alta :green[(~8,0)] em 2020, declinando gradualmente nos dois anos seguintes, atingindo cerca de :green[7,0 em 2022]. 

A linha vermelha representa o grupo que não atingiu o ponto de virada, começando com uma pontuação IAN mais baixa :green[(~7,0)] em 2020 e mostrando uma tendência de queda semelhante, chegando perto de :green[6,0] em 2022.

O gráfico sugere que ambos os grupos experimentaram um declínio gradual na média de IAN ao longo do tempo, com uma diferença perceptível entre os dois grupos em todos os anos.
        """)
    
    st.divider()
    
    image_path = 'assets/imgs/ian_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab6:
    st.subheader("Análise IAA")
    st.markdown(
        """
O Indicador de Autoavaliação (IAA) é uma ferramenta que avalia a :green[dimensão psicossocial], com base nas respostas fornecidas pelo próprio aluno sobre si mesmo, englobando :green[aspectos da sua vida e experiências diárias]. Esse indicador traz à PEDE a :green[perspectiva subjetiva] dos alunos da Associação Passos Mágicos.

Ressaltamos a importância de combinar os resultados dessa autoavaliação com as avaliações do conselho, desenvolvidas pelas diferentes equipes da associação, que se refletem nos indicadores IPS, IPP e IPV, promovendo uma visão mais completa.
        """)

    st.divider()

    image_path = 'assets/imgs/iaa_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab7:
    st.subheader("Análise IPS")
    st.markdown(
        """
O Indicador Psicossocial (IPS) é uma avaliação realizada pelo conselho na dimensão psicossocial, cujos resultados são obtidos por meio de :green[avaliações consensuais feitas pelos psicólogos da Associação Passos Mágicos]. O objetivo deste indicador é :green[analisar o estágio de desenvolvimento psicológico e as interações sociais do aluno], levando em consideração sua dinâmica de vida fora da associação, :green[incluindo os aspectos comunitários, familiares e sociais, além do acompanhamento psicológico que ele recebe].

Essa avaliação deve ser baseada na convivência do profissional com o aluno, seja de forma presencial ou, em tempos de pandemia, remota, buscando sempre uma observação detalhada e individualizada. O desenvolvimento desse indicador teve como prioridade garantir avaliações uniformes (utilizando sempre os mesmos critérios) e imparciais (evitando qualquer influência na formação dos conceitos avaliativos).

Os resultados do IPS são fruto de uma avaliação consensual e, juntamente com as demais avaliações e autoavaliações, contribuem para a compreensão do desenvolvimento dos alunos ano a ano. A análise do gráfico IPS mostra uma tendência de :green[crescimento em 2021 para ambos os grupos], seguida por uma :green[queda em 2022], onde o grupo que :green[Atingiu Ponto de Virada] ainda mantém uma vantagem, mas também sofreu um decréscimo. 

Ambos os grupos mostram que os ganhos :green[não foram sustentados] ao longo do tempo.
        """)

    st.divider()

    image_path = 'assets/imgs/ips_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab8:
    st.subheader("Análise IPP")
    st.markdown(
        """
O Indicador Psicopedagógico (IPP) avalia a :green[dimensão psicopedagógica] dos alunos e é baseado em avaliações individuais. O objetivo desse indicador é :green[examinar o estágio de desenvolvimento psicopedagógico dos alunos], levando em consideração suas interações e dinâmicas durante o processo de aprendizagem nas atividades oferecidas pela Associação.

Essas atividades incluem o Programa de Aceleração do Conhecimento e outras oportunidades educacionais proporcionadas aos alunos. As avaliações foram realizadas tanto presencialmente quanto remotamente, devido à pandemia, com base em observações diretas dos avaliadores. Foi recomendado que os profissionais utilizassem todos os registros e contatos disponíveis para garantir uma avaliação detalhada e precisa de cada aluno.

O gráfico do IPP mostra uma disparidade clara entre os dois grupos, sendo que o grupo que Atingiu Ponto de Virada começa com uma média mais alta, mas ambos os grupos sofrem :green[quedas em 2022], possivelmente devido a mudanças adversas no ambiente ou nos fatores que influenciam o IPP.
        """)
    
    st.divider()
    
    image_path = 'assets/imgs/ipp_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab9:
    st.subheader("Análise IPV")
    st.markdown(
        """
A metodologia aplicada ao Indicador de Potencial de Virada (IPV) foi desenvolvida com o objetivo de garantir avaliações consistentes e imparciais. Vale lembrar também que  :green[nenhuma avaliação individual teria o peso de determinar o resultado final isoladamente]; pelo contrário, o desempenho do aluno no IPV é construído a partir de uma :green[análise coletiva da equipe pedagógica], formando um panorama coerente da evolução de cada aluno ao longo do ano.

A avaliação do IPV considera :green[três aspectos principais:] A :red[ integração do aluno na associação], :red[seu desenvolvimento emocional] e :red[seu potencial acadêmico]. Com cada um sendo investigado e caracterizado pelos avaliadores. O gráfico de IPV revela que o grupo que :green[Atingiu Ponto de Virada] tem uma performance consistentemente superior, especialmente em 2021, mas ambos os grupos enfrentam :green[quedas no último ano da análise].
        """)
    
    st.divider()
    
    image_path = 'assets/imgs/ipv_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()