import streamlit as st
import nltk
import string

from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# ======================================
# DOWNLOAD DOS RECURSOS NLTK
# ======================================

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

# ======================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================

st.set_page_config(
    page_title="Atividades de NLP",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Atividades de Processamento de Linguagem Natural (NLP)")

st.write(
    """
Aplicação desenvolvida em **Python + Streamlit + NLTK**
demonstrando conceitos básicos de Processamento de Linguagem Natural.
"""
)

# ======================================
# STOPWORDS
# ======================================

stop_words = set(stopwords.words("portuguese"))

# ======================================
# DICIONÁRIO DE SENTIMENTOS
# ======================================

palavras_positivas = {

    "bom",
    "boa",
    "bons",
    "boas",

    "ótimo",
    "otimo",
    "ótima",
    "otima",

    "excelente",
    "excelentes",

    "maravilhoso",
    "maravilhosa",

    "perfeito",
    "perfeita",

    "incrível",
    "incrivel",

    "amei",
    "adoro",
    "adorei",

    "gostei",
    "gostamos",

    "feliz",

    "satisfeito",
    "satisfeita",

    "funcionou",

    "rápido",
    "rapido",

    "recomendo"
}

palavras_negativas = {

    "ruim",

    "péssimo",
    "pessimo",

    "horrível",
    "horrivel",

    "erro",

    "falha",

    "bug",

    "travando",
    "travou",
    "trava",

    "problema",
    "problemas",

    "lento",
    "demorado",

    "cancelar",
    "cancelamento",

    "insatisfeito",
    "insatisfeita",

    "triste",

    "cobrança",
    "cobranca",

    "duplicado",

    "recusado"
}

# ======================================
# DICIONÁRIO DE CATEGORIAS
# ======================================

financeiro = {

    "pagamento",
    "pagar",
    "fatura",
    "boleto",
    "pix",

    "cartão",
    "cartao",

    "assinatura",

    "estorno",

    "cobrança",
    "cobranca",

    "duplicado",

    "recusado",

    "valor",

    "renovação",
    "renovacao"
}

suporte = {

    "erro",

    "bug",

    "falha",

    "travando",
    "travou",

    "problema",

    "aplicativo",

    "play",

    "tv",

    "smart",

    "tela",

    "preta",

    "legenda",

    "conteúdo",
    "conteudo",

    "acessar",

    "abre",
    "abrindo",

    "fecha",
    "fechando",

    "filmes",

    "série",
    "serie",

    "reproduzir",

    "login",

    "conta"
}

# ======================================
# CRIAÇÃO DAS ABAS
# ======================================

tabs = st.tabs([
    "Atividade 1",
    "Atividade 2",
    "Atividade 3",
    "Atividade 4",
    "Atividade 5",
    "Atividade 6",
    "Atividade 7",
    "Atividade 8",
    "Atividade 9",
    "Atividade 10"
])

# ===================================================
# ATIVIDADE 1
# ===================================================
with tabs[0]:

    st.header("Atividade 1 - Tokenização")

    texto = st.text_area(
        "Digite um texto",
        key="a1"
    )

    if st.button("Executar", key="b1"):

        tokens = word_tokenize(
            texto,
            language="portuguese"
        )

        st.success("Palavras encontradas")

        st.write(tokens)

# ===================================================
# ATIVIDADE 2
# ===================================================
with tabs[1]:

    st.header("Atividade 2 - Frequência das palavras")

    texto = st.text_area(
        "Digite um texto",
        key="a2"
    )

    if st.button("Executar", key="b2"):

        tokens = word_tokenize(
            texto.lower(),
            language="portuguese"
        )

        tokens = [
            token
            for token in tokens
            if token not in string.punctuation
        ]

        contador = Counter(tokens)

        st.write("Frequência das palavras (ordem decrescente)")

        st.table(
            contador.most_common()
        )

# ===================================================
# ATIVIDADE 3
# ===================================================
with tabs[2]:

    st.header("Atividade 3 - Detectar palavras negativas")

    texto = st.text_area(
        "Digite uma mensagem",
        key="a3"
    )

    if st.button("Executar", key="b3"):

        tokens = word_tokenize(
            texto.lower(),
            language="portuguese"
        )

        tokens = [
            token
            for token in tokens
            if token not in string.punctuation
        ]

        negativas = [
            token
            for token in tokens
            if token in palavras_negativas
        ]

        if negativas:

            st.error("Mensagem NEGATIVA detectada.")

            st.write("Palavras negativas encontradas:")

            st.write(negativas)

        else:

            st.success("Nenhuma palavra negativa encontrada.")

# ===================================================
# ATIVIDADE 4
# ===================================================
with tabs[3]:

    st.header("Atividade 4 - Remover Stopwords")

    texto = st.text_area(
        "Digite um texto",
        key="a4"
    )

    if st.button("Executar", key="b4"):

        tokens = word_tokenize(
            texto.lower(),
            language="portuguese"
        )

        resultado = [

            token

            for token in tokens

            if token not in stop_words
            and token not in string.punctuation

        ]

        st.success("Texto após remoção das stopwords")

        st.write(resultado)

# ===================================================
# ATIVIDADE 5
# ===================================================
with tabs[4]:

    st.header("Atividade 5 - Classificação de Sentimento")

    texto = st.text_area(
        "Digite um comentário",
        key="a5"
    )

    if st.button("Executar", key="b5"):

        tokens = word_tokenize(
            texto.lower(),
            language="portuguese"
        )

        tokens = [

            token

            for token in tokens

            if token not in stop_words
            and token not in string.punctuation

        ]

        score = 0

        positivas = []

        negativas = []

        for token in tokens:

            if token in palavras_positivas:

                score += 1

                positivas.append(token)

            elif token in palavras_negativas:

                score -= 1

                negativas.append(token)

        st.write("Tokens analisados:")

        st.write(tokens)

        if positivas:

            st.write("Palavras positivas:")

            st.success(", ".join(sorted(set(positivas))))

        if negativas:

            st.write("Palavras negativas:")

            st.error(", ".join(sorted(set(negativas))))

        if score > 0:

            st.success("😊 Sentimento Positivo")

        elif score < 0:

            st.error("😞 Sentimento Negativo")

        else:

            st.warning("😐 Sentimento Neutro")

# ===================================================
# ATIVIDADE 6
# ===================================================
with tabs[5]:

    st.header("Atividade 6 - Detectar Palavras-chave")

    texto = st.text_area(
        "Digite uma mensagem",
        key="a6"
    )

    if st.button("Executar", key="b6"):

        tokens = word_tokenize(
            texto.lower(),
            language="portuguese"
        )

        tokens = [

            token

            for token in tokens

            if token not in stop_words
            and token not in string.punctuation

        ]

        qtd_financeiro = sum(
            token in financeiro
            for token in tokens
        )

        qtd_suporte = sum(
            token in suporte
            for token in tokens
        )

        st.write("Resumo da classificação")

        st.write(f"Financeiro: {qtd_financeiro}")

        st.write(f"Suporte Técnico: {qtd_suporte}")

        if qtd_financeiro > qtd_suporte:

            st.success("Encaminhar para Financeiro")

        elif qtd_suporte > qtd_financeiro:

            st.success("Encaminhar para Suporte Técnico")

        elif qtd_financeiro > 0 and qtd_suporte > 0:

            st.warning(
                "A mensagem possui termos das duas categorias."
            )

        else:

            st.info("Nenhuma categoria identificada.")
# ===================================================
# ATIVIDADE 7
# ===================================================
with tabs[6]:

    st.header("Atividade 7 - Palavras mais frequentes")

    texto = st.text_area(
        "Digite uma reclamação",
        key="a7"
    )

    if st.button("Executar", key="b7"):

        tokens = word_tokenize(
            texto.lower(),
            language="portuguese"
        )

        tokens = [

            token

            for token in tokens

            if token not in stop_words
            and token not in string.punctuation

        ]

        contador = Counter(tokens)

        palavras_negativas_encontradas = {

            palavra: contador[palavra]

            for palavra in contador

            if palavra in palavras_negativas

        }

        st.write("### Principais palavras negativas")

        if palavras_negativas_encontradas:

            st.table(
                Counter(
                    palavras_negativas_encontradas
                ).most_common()
            )

        else:

            st.success(
                "Nenhuma palavra negativa encontrada."
            )

# ===================================================
# ATIVIDADE 8
# ===================================================
with tabs[7]:

    st.header("Atividade 8 - Classificação por Categoria")

    texto = st.text_area(
        "Digite uma mensagem",
        key="a8"
    )

    if st.button("Executar", key="b8"):

        tokens = word_tokenize(
            texto.lower(),
            language="portuguese"
        )

        tokens = [

            token

            for token in tokens

            if token not in stop_words
            and token not in string.punctuation

        ]

        score_financeiro = 0
        score_suporte = 0

        palavras_financeiras = []
        palavras_suporte = []

        for token in tokens:

            if token in financeiro:

                score_financeiro += 1

                palavras_financeiras.append(token)

            if token in suporte:

                score_suporte += 1

                palavras_suporte.append(token)

        st.write("### Palavras identificadas")

        if palavras_financeiras:

            st.success(
                f"Financeiro: {', '.join(sorted(set(palavras_financeiras)))}"
            )

        if palavras_suporte:

            st.info(
                f"Suporte: {', '.join(sorted(set(palavras_suporte)))}"
            )

        st.divider()

        if score_financeiro > score_suporte:

            st.success("Categoria: Financeiro")

        elif score_suporte > score_financeiro:

            st.success("Categoria: Suporte Técnico")

        elif score_financeiro > 0 and score_suporte > 0:

            st.warning(
                "Mensagem contém assuntos de Financeiro e Suporte."
            )

        else:

            st.warning("Categoria não identificada.")

# ===================================================
# ATIVIDADE 9
# ===================================================
with tabs[8]:

    st.header("Atividade 9 - Limpeza do Texto")

    texto = st.text_area(
        "Digite um texto",
        key="a9"
    )

    if st.button("Executar", key="b9"):

        texto_limpo = texto.lower()

        texto_limpo = texto_limpo.translate(
            str.maketrans(
                "",
                "",
                string.punctuation
            )
        )

        st.write("Texto normalizado")

        st.success(texto_limpo)
# ===================================================
# ATIVIDADE 10
# ===================================================
with tabs[9]:

    st.header("Atividade 10 - Tokenização + Sentimento")

    texto = st.text_area(
        "Digite uma avaliação",
        key="a10"
    )

    if st.button("Executar", key="b10"):

        # Tokenização
        tokens = word_tokenize(
            texto.lower(),
            language="portuguese"
        )

        # Remoção de stopwords e pontuação
        tokens = [

            token

            for token in tokens

            if token not in stop_words
            and token not in string.punctuation

        ]

        score = 0

        positivas = []
        negativas = []

        # Classificação das palavras
        for token in tokens:

            if token in palavras_positivas:

                score += 1
                positivas.append(token)

            elif token in palavras_negativas:

                score -= 1
                negativas.append(token)

        # ============================
        # RESULTADOS
        # ============================

        st.subheader("Resultado da Análise")

        st.write("### Tokens encontrados")

        st.write(tokens)

        col1, col2 = st.columns(2)

        with col1:

            st.write("### Palavras positivas")

            if positivas:

                st.success(
                    ", ".join(sorted(set(positivas)))
                )

            else:

                st.info("Nenhuma palavra positiva encontrada.")

        with col2:

            st.write("### Palavras negativas")

            if negativas:

                st.error(
                    ", ".join(sorted(set(negativas)))
                )

            else:

                st.info("Nenhuma palavra negativa encontrada.")

        st.divider()

        st.write(f"### Score da avaliação: **{score}**")

        if score > 0:

            st.success("😊 Avaliação Positiva")

        elif score < 0:

            st.error("😞 Avaliação Negativa")

        else:

            st.warning("😐 Avaliação Neutra")