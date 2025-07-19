import streamlit as st

st.set_page_config(page_title="Portfólio Sophia Sussa", layout="centered")

st.title("Sophia Sussa Campos Bastos")

tabs = st.tabs(["Perfil", "Formação & Certificações", "Projetos", "Contato"])

with tabs[0]:
    with st.expander("Objetivo Profissional", expanded=True):
        st.write("""Atuar como Engenheira de Dados Júnior, Cientista ou Analista de Dados, aplicando soluções de coleta, transformação, visualização e análise de dados com foco em valor estratégico, automação de processos e tomada de decisão orientada por dados.""")

    with st.expander("Perfil Profissional", expanded=True):
        st.write("""Sou uma profissional neurodivergente (autista), com forte atenção aos detalhes, pensamento analítico e criatividade na resolução de problemas. Acredito que a diversidade de perspectivas fortalece a tecnologia. Tenho interesse especial em projetos que gerem impacto social.""")

    with st.expander("Habilidades", expanded=True):
        st.markdown("""
        <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            text-align: left;
            padding: 6px;
            vertical-align: top;
        }
        </style>

        <table>
            <tr>
                <th>Categoria</th>
                <th>Detalhes</th>
            </tr>
            <tr>
                <td><strong>Linguagens</strong></td>
                <td>Python · Java</td>
            </tr>
            <tr>
                <td><strong>Banco de Dados</strong></td>
                <td>MySQL · PostgreSQL · SQLite</td>
            </tr>
            <tr>
                <td><strong>Dados & ETL</strong></td>
                <td>Pandas · Pipelines ETL · Metabase · Streamlit</td>
            </tr>
            <tr>
                <td><strong>Ferramentas & Deploy</strong></td>
                <td>Docker · Git/GitHub · Render</td>
            </tr>
            <tr>
                <td><strong>Frameworks e Bibliotecas</strong></td>
                <td>Vaadin · Matplotlib · Seaborn</td>
            </tr>
            <tr>
                <td><strong>Metodologias</strong></td>
                <td>UML · Scrum · Kanban</td>
            </tr>
            <tr>
                <td><strong>Soft Skills</strong></td>
                <td>Facilidade de aprendizado e adaptação · Comunicação clara e objetiva · Organização e gestão do tempo · Pensamento crítico e analítico · Proatividade e foco em resultados</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)

    with st.expander("Experiência Profissional"):
        st.markdown("""
        <p>
        <strong>ServerTI – Auxiliar de Suporte Técnico</strong><br>
        Jataí/GO · Nov/2022 – Mai/2023<br>
        Atendimento remoto e presencial a clientes, diagnóstico e resolução de problemas técnicos, instalação e configuração de softwares, documentação.
        </p>
        """, unsafe_allow_html=True)


    with st.expander("Idiomas"):
        st.markdown("""
        <p>
        <strong>Inglês:</strong> Avançado — confortável na leitura, escrita e conversação<br>
        <strong>Mandarim:</strong> Básico-intermediário — estudando para HSK3
        </p>
        """, unsafe_allow_html=True)

with tabs[1]:
    with st.expander("Formação Acadêmica", expanded=True):
        st.markdown("""
        <p>
        Tecnólogo em Análise e Desenvolvimento de Sistemas <br>
        Instituto Federal de Goiás (IFG) – Campus Jataí <br>
        Conclusão: 2024-02
        </p>
        """, unsafe_allow_html=True)

    with st.expander("Cursos e Certificações"):
        st.write("""
        - Git Completo: Do Básico ao Avançado – Udemy (7h)
        - Dominando Banco de Dados com MySQL – Udemy (4h)
        - Docker e Sistemas Embarcados – IFG (2h)
        - Metodologias Ágeis com Scrum: Fundamentos e Práticas – IFG (2h)
        """)

    with st.expander("Reconhecimentos"):
        st.write("""
        - Medalha de Bronze – World Mathematics Team Championship, Pequim (2019)
        - Participação – Asia International Mathematical Olympiad, Bangkok (2019)
        - Diploma – Ordem do Mérito Cidadão-Herói (2019)
        """)

with tabs[2]:
    with st.expander("Pipeline ETL para Dados de OSCs", expanded=True):
        st.markdown("""
        - **Repository:** [github.com/sophiasussa/pipeline-etl](https://github.com/sophiasussa/pipeline-etl)
        - **Deploy:** [oscs-pipeline-etl.onrender.com](https://oscs-pipeline-etl.onrender.com) (Deploy com banco de dados teste - pequeno)
        - **Tecnologias:** Python · Docker · Streamlit · Metabase · PostgreSQL/SQLite
        - Limpeza e padronização de dados públicos sobre OSCs
        - Visualizações com Streamlit e dashboard conectado ao Metabase
        - Exportação de dados tratados para diferentes formatos
        """)
        st.image("img/imagem_dispersao_geografica.png", caption="Dispersão Geografica das OSCs", use_container_width=True)
        st.image("img/dashboardMetabase.png", caption="Metabase Dashboard", use_container_width=True)
        st.image("img/streamlit.png", caption="Streamlit", use_container_width=True)

    with st.expander("Structura – Sistema para Marmorarias", expanded=True):
        st.markdown("""
        - **Repository:** [github.com/sophiasussa/structura](https://github.com/sophiasussa/structura)
        - **Vídeo demonstrativo:** [youtu.be/ikaWbtQyMxw](https://youtu.be/ikaWbtQyMxw)
        - **Tecnologias:** Java · Vaadin · MySQL
        - Controle de ordens de serviço, clientes, funcionários, estoque, entre outros
        - Interface com foco em boa usabilidade e experiência do usuário
        """)
        st.image("img/fornecedores.png", caption="Todos os fornecedores", use_container_width=True)
        st.image("img/os.png", caption="Todos as ordens de serviço", use_container_width=True)
        st.image("img/produtos.png", caption="Cadastro de produtos", use_container_width=True)

with tabs[3]:
    with st.expander("Contato", expanded=True):
        st.write("Endereço: Jataí - GO")
        st.write("Telefone: (64) 9280-7219")
        st.write("Email: sophiasussa@outlook.com")
        st.write("[LinkedIn](https://www.linkedin.com/in/sophia-sussa)")
        st.write("[GitHub](https://github.com/sophiasussa)")

    with open("assets/curriculo.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Baixar Currículo em PDF",
                       data=PDFbyte,
                       file_name="curriculo-sophia.pdf",
                       mime='application/pdf')
